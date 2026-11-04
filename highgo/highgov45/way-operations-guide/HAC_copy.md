---
title: "29、流复制运维实践"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HAC_copy.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## HGDB-SEE-V4.5 流复制运维实践

## 一、文档说明

### 1．文档目的

本文档用于指导 `Hgdb-see 4.5` 一主一备物理流复制环境的日常监控、备库启用、切回主库、风险控制与验证操作。

### 2．适用范围

适用于以下场景：

- `Hgdb-see 4.5` 一主一备物理流复制架构；
- 主备模式为流复制，支持异步复制或同步复制；
- 需要人工执行主备切换和回切；
- 需要形成现场运维标准与故障应急手册。

### 3．重要前提

- 本手册以 `Hgdb-see 4.5` 为准。
- 本手册默认操作系统为 `Rocky Linux` 或兼容的 `RHEL` 系发行版。
- 本手册默认数据库数据目录示例为 `$PGDATA` ，实际实施时需要替换为现场路径。
- 本手册重点覆盖人工切换，不包含自动切换组件如 `Patroni` 、 `repmgr` 的自动化流程。
- 本手册中的示例 SQL 和命令均需在变更前结合现场实际环境校验。

---

## 二、架构说明

### 1．典型架构

- `Primary` ：主库，对外提供读写服务；
- `Standby` ：备库，通过物理流复制接收并回放主库 `WAL` ；
- 复制链路：主库 `walsender` → 备库 `walreceiver` ；
- 可选组件：
	- `replication slot`
		- `archive_command`
		- `VIP` 、代理、中间件或应用连接串切换机制

### 2．角色识别

所有节点可通过以下 SQL 判断当前角色：

```sql
SELECT pg_is_in_recovery();
```

判定规则：

- 返回 `false` ：主库
- 返回 `true` ：备库

### 3．版本说明

`Hgdb-see 4.5` 中需要特别注意：

- 使用 `standby.signal` 标识备库恢复模式；
- `recovery.conf` 已废弃；
- 可通过 `SELECT pg_promote();` 提升备库；
- `pg_stat_wal_receiver` 在 `hgdb-see 4.5` 中 **没有** `written_lsn` 、 `flushed_lsn` 字段；
- 备库延迟判断不能只依赖 `pg_last_xact_replay_timestamp()` 。

---

## 三、运维目标与控制原则

### 1．运维目标

- 确保主备复制链路持续健康；
- 及时发现复制中断、延迟扩大、 `WAL` 堆积、归档失败等风险；
- 在主库故障或计划切换场景下，能够安全启用备库；
- 在故障恢复后，能够规范完成切回主库；
- 避免双主、数据丢失、误切换和业务长时间中断。

### 2．控制原则

#### 2．1 数据安全优先

任何切换操作必须优先保障数据一致性和可恢复性。

#### 2．2 严禁双主

备库提升前，必须确认旧主已经停机、隔离或不再对外提供写服务。

#### 2．3 切换前先确认复制追平

计划内切换必须在主备基本追平后进行。

#### 2．4 切回主库必须先重建复制关系

故障后原主不能直接上线重新作为主库，必须先重建为现主的备库，再安排计划切换。

---

## 四、主备流复制监控方法和手段

### 1．监控总原则

主备流复制监控应覆盖以下三个层面：

- 数据库角色与复制状态；
- 复制延迟与 `WAL` 堆积；
- 操作系统资源与网络状态。

### 2．主库监控项

#### 2．1 主库角色确认

```sql
SELECT pg_is_in_recovery();
```

期望结果：

- 返回 `false`

#### 2．2 主库复制状态检查

```sql
SELECT
    application_name,
    client_addr,
    state,
    sync_state,
    sent_lsn,
    write_lsn,
    flush_lsn,
    replay_lsn,
    write_lag,
    flush_lag,
    replay_lag,
    pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS byte_lag
FROM pg_stat_replication;
```

重点关注：

- `state` 是否为 `streaming`
- `sync_state` 是否符合设计预期，例如 `async` 或 `sync`
- `byte_lag` 是否持续增大
- `write_lag` 、 `flush_lag` 、 `replay_lag` 是否异常升高

#### 2．3 复制槽检查

```sql
SELECT
    slot_name,
    slot_type,
    active,
    restart_lsn,
    confirmed_flush_lsn
FROM pg_replication_slots;
```

重点关注：

- `active` 是否为 `true`
- 是否存在长期不活跃的物理复制槽
- `restart_lsn` 是否滞后过大，导致 `WAL` 无法回收

#### 2．4 归档状态检查

```sql
SELECT
    archived_count,
    last_archived_wal,
    last_archived_time,
    failed_count,
    last_failed_wal,
    last_failed_time
FROM pg_stat_archiver;
```

重点关注：

- `failed_count` 是否增长
- 最近归档时间是否持续更新

---

### 3．备库监控项

#### 3．1 备库角色确认

```sql
SELECT pg_is_in_recovery();
```

期望结果：

- 返回 `true`

#### 3．2 备库 wal receiver 状态检查

```sql
SELECT
    pid,
    status,
    receive_start_lsn,
    receive_start_tli,
    received_lsn,
    received_tli,
    last_msg_send_time,
    last_msg_receipt_time,
    latest_end_lsn,
    latest_end_time,
    slot_name,
    sender_host,
    sender_port
FROM pg_stat_wal_receiver;
```

重点关注：

- `status` 是否为 `streaming`
- `last_msg_receipt_time` 是否持续更新
- `latest_end_lsn` 是否持续推进

#### 3．3 备库接收与回放检查

```sql
SELECT
    pg_last_wal_receive_lsn() AS receive_lsn,
    pg_last_wal_replay_lsn()  AS replay_lsn,
    pg_wal_lsn_diff(pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn()) AS replay_byte_lag,
    pg_last_xact_replay_timestamp() AS last_replay_ts,
    now() - pg_last_xact_replay_timestamp() AS replay_delay;
```

判读原则：

- `replay_byte_lag = 0` 或接近 `0` ：说明备库已基本追平；
- `receive_lsn = replay_lsn` ：说明没有“收到未回放”的积压；
- `replay_delay` 只能辅助参考， **不能单独作为复制异常依据** ；
- 如果主库长时间没有事务提交，则 `replay_delay` 可能很大，但复制仍然健康。

#### 3．4 检查是否暂停回放

```sql
SELECT pg_is_wal_replay_paused();
```

期望结果：

- 返回 `false`

若返回 `true` ，则备库不适合作为切换目标，必须先查明原因。

---

### 4．复制延迟的正确判定方法

#### 4．1 优先使用字节延迟

主库侧：

```sql
SELECT
    application_name,
    pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS byte_lag
FROM pg_stat_replication;
```

备库侧：

```sql
SELECT
    pg_wal_lsn_diff(pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn()) AS replay_byte_lag;
```

#### 4．2 谨慎使用时间延迟

```sql
SELECT now() - pg_last_xact_replay_timestamp() AS replay_delay;
```

注意事项：

- 该值表示当前时间与最后一次已回放事务时间的差值；
- 如果主库近期没有提交事务，则该值会持续变大；
- 不能据此直接判断复制落后。

---

### 5．操作系统层监控项

建议同时监控以下指标：

- CPU 使用率与负载；
- 内存使用与页缓存；
- 数据目录空间；
- `WAL` 目录空间；
- 磁盘 `I/O` 延迟与队列；
- 网络丢包、时延；
- `postgres` 进程状态。

建议命令：

```bash
uptime
vmstat 1
iostat -dx 1
free -h
df -h
ss -lntp | grep 5866
ps -ef | grep postgres
```

---

### 6．建议告警阈值

以下为推荐起始阈值，需根据现场 `RPO` 、 `RTO` 和业务峰值调整。

| 监控项 | 建议阈值 | 告警级别 | 说明 |
| --- | --- | --- | --- |
| 复制连接中断 | 立即 | 严重 | `pg_stat_replication` 或 `pg_stat_wal_receiver` 异常 |
| 主库到备库 `byte_lag` 持续增长 | 超过现场阈值 | 告警／严重 | 按业务量设定 |
| 备库 `replay_byte_lag` 持续增长 | 超过现场阈值 | 告警／严重 | 说明回放跟不上 |
| `pg_is_wal_replay_paused()` 为 `true` | 立即 | 严重 | 备库不可切换 |
| `failed_count` 增长 | 立即 | 严重 | 归档异常 |
| 复制槽长期不活跃 | `> 10` 分钟 | 告警 | 防止 `WAL` 打满磁盘 |
| 数据目录或 `WAL` 目录使用率 | `> 70%` / `> 85%` | 告警／严重 | 需要结合增长速度判断 |

---

## 五、日常巡检步骤

### 1．主库日常巡检

按以下顺序执行：

1. 确认当前为主库；
2. 检查 `pg_stat_replication` ；
3. 检查复制槽；
4. 检查归档状态；
5. 检查 OS 资源。

### 2．备库日常巡检

按以下顺序执行：

1. 确认当前为备库；
2. 检查 `pg_stat_wal_receiver` ；
3. 检查接收与回放 `LSN` ；
4. 检查回放暂停状态；
5. 检查 OS 资源。

### 3．建议巡检频率

- 核心复制状态：每 `1` 分钟；
- `WAL` 目录、磁盘空间、归档状态：每 `5` 分钟；
- 人工巡检：每日不少于 `1` 次；
- 切换前专项巡检：变更前立即执行。

---

## 六、启用备库的操作步骤和注意事项

本章分为两类场景：

- 计划内切换到备库；
- 主库故障后启用备库。

---

### 6．1 计划内切换到备库

#### 6．1．1 适用场景

适用于以下场景：

- 主机维护；
- 存储维护；
- 操作系统补丁；
- 数据库版本内补丁更新；
- 计划演练。

#### 6．1．2 切换前前提条件

必须同时满足：

- 主备复制正常；
- 主备 `LSN` 已追平或接近追平；
- 业务方确认可进入维护窗口；
- 已确定业务连接切换方式；
- 已明确回滚方案。

#### 6．1．3 操作步骤

##### 步骤 1：确认主备状态正常

主库执行：

```sql
SELECT
    application_name,
    state,
    sync_state,
    sent_lsn,
    write_lsn,
    flush_lsn,
    replay_lsn,
    pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS byte_lag
FROM pg_stat_replication;
```

备库执行：

```sql
SELECT
    pg_is_in_recovery() AS is_standby,
    pg_last_wal_receive_lsn() AS receive_lsn,
    pg_last_wal_replay_lsn()  AS replay_lsn,
    pg_wal_lsn_diff(pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn()) AS replay_byte_lag,
    pg_last_xact_replay_timestamp() AS last_replay_ts,
    now() - pg_last_xact_replay_timestamp() AS replay_delay;
```

判定要求：

- 主库侧 `state = 'streaming'`
- 主库侧 `byte_lag` 为 `0` 或接近 `0`
- 备库侧 `replay_byte_lag = 0` 或接近 `0`
- 备库未暂停回放

##### 步骤 2：停止业务写入

建议方式：

- 应用切只读；
- 业务停写；
- 关闭写流量入口；
- 从代理／负载均衡摘除写入口。

如需数据库层保护，可在主库执行：

```sql
ALTER SYSTEM SET default_transaction_read_only = on;
SELECT pg_reload_conf();
```

注意：

- 该设置只能降低新增写入风险， **不能替代应用停写** ；
- 超级用户或显式控制仍可能写入。

##### 步骤 3：再次确认主备追平

主库执行：

```sql
SELECT
    application_name,
    pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS byte_lag
FROM pg_stat_replication;
```

备库执行：

```sql
SELECT
    pg_last_wal_receive_lsn() AS receive_lsn,
    pg_last_wal_replay_lsn()  AS replay_lsn,
    pg_wal_lsn_diff(pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn()) AS replay_byte_lag;
```

判定要求：

- `byte_lag = 0`
- `replay_byte_lag = 0`

##### 步骤 4：提升备库

在备库执行：

```sql
SELECT pg_promote();
```

或在 OS 上执行：

```bash
pg_ctl promote -D $PGDATA
```

##### 步骤 5：确认备库已转为新主

在原备库执行：

```sql
SELECT pg_is_in_recovery();
```

期望结果：

- 返回 `false`

再执行简单写入验证：

```sql
CREATE TABLE IF NOT EXISTS failover_check(id int);
INSERT INTO failover_check VALUES (1);
DROP TABLE failover_check;
```

##### 步骤 6：切换业务连接

执行方式视现场架构而定，包括：

- 修改应用连接串；
- 切换 `VIP` ；
- 切换代理路由；
- 更新中间件主库指向。

##### 步骤 7：验证业务与数据库状态

验证内容包括：

- 应用可连接；
- 读写正常；
- 核心业务链路正常；
- 旧主不再对外提供写服务。

---

#### 6．1．4 注意事项

- 必须先停写再提升；
- 必须防止旧主重新接入业务；
- 切换后应及时更新监控对象；
- 异步复制场景下，若停写控制不严格，可能存在极短时间窗口的数据丢失风险。

---

### 6．2 主库故障后启用备库

#### 6．2．1 适用场景

适用于以下场景：

- 主库主机宕机；
- 主库存储不可用；
- 主库数据库实例无法恢复；
- 业务要求立即恢复对外服务。

#### 6．2．2 操作原则

故障切换最关键的前提是： **必须先确认旧主不可继续写入，或已完成隔离。**

#### 6．2．3 操作步骤

##### 步骤 1：确认主库不可用或已隔离

至少满足以下之一：

- 主机断电；
- 数据库实例已停；
- 网络已隔离；
- `VIP` 已迁移；
- 业务入口已从旧主摘除。

##### 步骤 2：确认备库当前状态

在备库执行：

```sql
SELECT
    pg_is_in_recovery() AS is_standby,
    pg_last_wal_receive_lsn() AS receive_lsn,
    pg_last_wal_replay_lsn()  AS replay_lsn,
    pg_wal_lsn_diff(pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn()) AS replay_byte_lag,
    pg_last_xact_replay_timestamp() AS last_replay_ts,
    now() - pg_last_xact_replay_timestamp() AS replay_delay;
```

同时执行：

```sql
SELECT
    status,
    last_msg_send_time,
    last_msg_receipt_time,
    latest_end_lsn,
    latest_end_time
FROM pg_stat_wal_receiver;
```

判断目的：

- 确认备库是否仍在正常接收或至少已回放到最近位置；
- 评估当前可能的 `RPO` 损失。

##### 步骤 3：提升备库

```sql
SELECT pg_promote();
```

##### 步骤 4：确认新主可写

```sql
SELECT pg_is_in_recovery();
```

期望结果：

- 返回 `false`

然后执行写入验证：

```sql
CREATE TABLE IF NOT EXISTS emergency_promote_check(id int);
INSERT INTO emergency_promote_check VALUES (1);
DROP TABLE emergency_promote_check;
```

##### 步骤 5：切换业务连接到新主

执行以下动作：

- 修改业务连接目标；
- 切换 `VIP` ／代理；
- 验证应用连接；
- 验证核心业务功能。

##### 步骤 6：记录故障切换信息

应记录：

- 切换时间；
- 执行人；
- 故障原因；
- 旧主隔离方式；
- 新主验证结果；
- 可能的数据影响范围。

---

#### 6．2．4 注意事项

- 在异步复制下，故障切换可能存在数据丢失；
- 未确认旧主隔离前，严禁提升备库；
- 旧主恢复后，严禁直接作为主库重新上线；
- 故障切换后必须尽快规划复制关系重建。

---

## 七、切回主库的操作步骤和注意事项

### 1．总体原则

切回主库分为两个阶段：

- 阶段一：将原主修复为现主的备库；
- 阶段二：选择维护窗口执行计划切换，将业务切回原主。

### 2．为什么不能直接让原主重新上线为主库

原因如下：

- 原主与新主可能已经出现时间线分叉；
- 原主停机前可能存在新主没有的数据页状态；
- 直接上线极易形成双主或数据不一致；
- 正确做法是基于现主重建原主。

---

### 7．1 阶段一：将原主修复为现主的备库

#### 7．1．1 方案 A：使用 pg\_rewind

##### 适用条件

- 原主与现主来自同一集群分叉；
- 原主数据目录仍可用；
- 已满足 `pg_rewind` 使用条件；
- 现主保留足够的 `WAL` ；
- 现场已验证可执行 `pg_rewind` 。

##### 操作步骤

###### 步骤 1：停止原主数据库

```bash
pg_ctl stop -D $PGDATA
```

###### 步骤 2：执行 pg\_rewind

```bash
pg_rewind \
  --target-pgdata=$PGDATA \
  --source-server="host=现主IP port=5866 user=replication dbname=highgo"
```

###### 步骤 3：配置为现主的备库

在原主配置文件中设置：

```
primary_conninfo = 'host=现主IP port=5866 user=replication password=密码 application_name=old_primary'
```

创建：

```bash
touch $PGDATA/standby.signal
```

###### 步骤 4：启动原主实例

```bash
pg_ctl start -D $PGDATA
```

###### 步骤 5：验证其已成为备库

```sql
SELECT pg_is_in_recovery();
```

期望结果：

- 返回 `true`

现主执行：

```sql
SELECT application_name, client_addr, state, sync_state
FROM pg_stat_replication;
```

要求原主节点已重新出现在复制列表中，且 `state = 'streaming'` 。

---

#### 7．1．2 方案 B：全量重建为备库

##### 适用条件

- `pg_rewind` 条件不满足；
- 原主数据损坏；
- 原主时间线差异较大；
- 需要最稳妥、最可控的恢复方式。

##### 操作步骤

###### 步骤 1：停止原主数据库

```bash
pg_ctl stop -D $PGDATA
```

###### 步骤 2：备份并清理原数据目录

```bash
mv $PGDATA $PGDATA_bak_$(date +%F_%H%M%S)
mkdir -p $PGDATA
chown -R highgo:highgo $PGDATA
chmod 700 $PGDATA
```

###### 步骤 3：从现主拉取基准备份

```bash
pg_basebackup \
  -h 现主IP \
  -p 5866 \
  -U replication \
  -D $PGDATA \
  -Fp \
  -Xs \
  -Pv
```

###### 步骤 4：配置复制连接

在配置文件中设置：

```
primary_conninfo = 'host=现主IP port=5866 user=replication password=密码 application_name=old_primary'
```

创建：

```bash
touch $PGDATA/standby.signal
```

###### 步骤 5：启动实例

```bash
pg_ctl start -D $PGDATA
```

###### 步骤 6：验证复制关系恢复

现主执行：

```sql
SELECT application_name, client_addr, state, sync_state
FROM pg_stat_replication;
```

原主执行：

```sql
SELECT pg_is_in_recovery();
```

要求：

- 原主已进入恢复模式；
- 现主可看到其复制连接。

---

### 7．2 阶段二：计划切回原主

当原主已作为备库稳定运行后，可在维护窗口内执行计划切换，将业务切回原主。

#### 7．2．1 切回步骤

##### 步骤 1：确认现主与原主备库同步正常

现主执行：

```sql
SELECT
    application_name,
    state,
    sync_state,
    pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS byte_lag
FROM pg_stat_replication;
```

原主执行：

```sql
SELECT
    pg_last_wal_receive_lsn() AS receive_lsn,
    pg_last_wal_replay_lsn()  AS replay_lsn,
    pg_wal_lsn_diff(pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn()) AS replay_byte_lag;
```

要求：

- `byte_lag = 0`
- `replay_byte_lag = 0`

##### 步骤 2：停止业务写入

执行方式同“计划内切换到备库”。

##### 步骤 3：再次确认追平

重复步骤 1，确保完全追平。

##### 步骤 4：提升原主备库

在原主执行：

```sql
SELECT pg_promote();
```

##### 步骤 5：确认原主已成为主库

```sql
SELECT pg_is_in_recovery();
```

期望结果：

- 返回 `false`

##### 步骤 6：切换业务连接回原主

- 切换 `VIP` ／代理；
- 更新应用连接；
- 验证业务。

##### 步骤 7：将现主重建为原主的新备库

执行方法与前述“阶段一”相同，可选：

- `pg_rewind`
- `pg_basebackup`

---

## 八、回滚策略

### 1．计划内切换回滚

如果在提升备库前发现异常：

- 取消变更；
- 恢复业务写入；
- 继续由原主提供服务。

如果已提升备库但业务未切换：

- 视现场情况选择继续切换或重新规划；
- 不建议在未重建复制关系前直接回退角色。

### 2．故障切换回滚

故障切换通常不建议“立刻回滚”，推荐流程为：

- 先确保新主稳定服务；
- 修复原主；
- 将原主重建为新主的备库；
- 通过计划切换方式回切。

---

## 九、风险与注意事项

### 1．双主风险

风险说明：

- 旧主未隔离，新主已提升；
- 应用仍有部分写流量写入旧主；
- 最终造成双主分裂写入。

控制措施：

- 提升前必须执行旧主隔离检查；
- 业务入口必须统一切换；
- 禁止旧主自行恢复上线。

### 2．异步复制下的数据丢失风险

风险说明：

- 主库故障时，最后一段 `WAL` 可能尚未传输到备库；
- 故障切换后可能丢失最后部分事务。

控制措施：

- 现场需提前明确 `RPO` ；
- 关键业务可考虑同步复制；
- 故障切换后执行业务核对。

### 3．复制槽导致 WAL 堆积风险

风险说明：

- 备库异常或网络中断；
- 复制槽仍保留旧位置；
- 主库 `WAL` 无法回收，最终打满磁盘。

控制措施：

- 持续监控复制槽；
- 监控 `WAL` 目录空间；
- 对长期失效槽及时处理。

### 4．时间延迟指标误判风险

风险说明：

- `now() - pg_last_xact_replay_timestamp()` 在主库空闲时会持续变大；
- 容易误判为复制延迟很大。

控制措施：

- 以 `LSN` 差异为主；
- 时间延迟仅作辅助。

### 5．连接切换风险

风险说明：

- 应用连接池未刷新；
- DNS 缓存未过期；
- 中间件未更新路由。

控制措施：

- 切换前明确业务连接切换方案；
- 切换后执行应用重连与功能验证。

---

## 十、验证方法

### 1．角色验证

```sql
SELECT pg_is_in_recovery();
```

### 2．主库复制状态验证

```sql
SELECT
    application_name,
    client_addr,
    state,
    sync_state,
    sent_lsn,
    write_lsn,
    flush_lsn,
    replay_lsn
FROM pg_stat_replication;
```

### 3．备库复制状态验证

```sql
SELECT
    status,
    received_lsn,
    latest_end_lsn,
    last_msg_receipt_time
FROM pg_stat_wal_receiver;
```

### 4．追平验证

主库：

```sql
SELECT
    application_name,
    pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS byte_lag
FROM pg_stat_replication;
```

备库：

```sql
SELECT
    pg_wal_lsn_diff(pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn()) AS replay_byte_lag;
```

### 5．业务写入验证

在当前主库执行：

```sql
CREATE TABLE IF NOT EXISTS switchover_test(id int, ts timestamp);
INSERT INTO switchover_test VALUES (1, now());
SELECT * FROM switchover_test ORDER BY ts DESC LIMIT 1;
DROP TABLE switchover_test;
```

### 6．备库回放验证

主库执行：

```sql
CREATE TABLE IF NOT EXISTS repl_test(id int, ts timestamp);
INSERT INTO repl_test VALUES (100, now());
```

备库执行：

```sql
SELECT * FROM repl_test ORDER BY ts DESC LIMIT 1;
```

---

## 十一、附录 A：常用 SQL 清单

### 1．角色识别

```sql
SELECT pg_is_in_recovery();
```

### 2．主库复制状态

```sql
SELECT
    application_name,
    client_addr,
    state,
    sync_state,
    sent_lsn,
    write_lsn,
    flush_lsn,
    replay_lsn,
    write_lag,
    flush_lag,
    replay_lag,
    pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS byte_lag
FROM pg_stat_replication;
```

### 3．复制槽状态

```sql
SELECT
    slot_name,
    slot_type,
    active,
    restart_lsn,
    confirmed_flush_lsn
FROM pg_replication_slots;
```

### 4．归档状态

```sql
SELECT
    archived_count,
    last_archived_wal,
    last_archived_time,
    failed_count,
    last_failed_wal,
    last_failed_time
FROM pg_stat_archiver;
```

### 5．备库 wal receiver

```sql
SELECT
    pid,
    status,
    receive_start_lsn,
    receive_start_tli,
    received_lsn,
    received_tli,
    last_msg_send_time,
    last_msg_receipt_time,
    latest_end_lsn,
    latest_end_time,
    slot_name,
    sender_host,
    sender_port
FROM pg_stat_wal_receiver;
```

### 6．备库接收与回放

```sql
SELECT
    pg_last_wal_receive_lsn() AS receive_lsn,
    pg_last_wal_replay_lsn()  AS replay_lsn,
    pg_wal_lsn_diff(pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn()) AS replay_byte_lag,
    pg_last_xact_replay_timestamp() AS last_replay_ts,
    now() - pg_last_xact_replay_timestamp() AS replay_delay;
```

### 7．回放暂停检查

```sql
SELECT pg_is_wal_replay_paused();
```

### 8．提升备库

```sql
SELECT pg_promote();
```

---

## 十二、附录 B：常用 Linux 命令清单

```bash
uptime
vmstat 1
iostat -dx 1
free -h
df -h
ss -lntp | grep 5866
ps -ef | grep postgres
tail -100 $PGDATA/hgdb_log/*.csv
```

---

## 十三、建议

对于 `Hgdb-see 4.5` 一主一备流复制，推荐执行策略如下：

- 日常运维以“主库 `pg_stat_replication` ＋ 备库 `pg_stat_wal_receiver` ＋ `LSN` 差值”为主；
- 切换操作遵循“先停写、再追平、后提升、再切流量”的顺序；
- 故障后原主必须先重建为备库，再通过计划切换完成回切；
- 避免将 `replay_delay` 单独作为复制异常判断依据。