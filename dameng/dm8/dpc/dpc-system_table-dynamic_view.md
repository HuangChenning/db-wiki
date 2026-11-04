---
title: "相关系统表和动态视图"
book: "DM8 分布计算集群"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dpc-system_table-dynamic_view.html
tags:
  - dameng
  - dm8
  - dpc
---

可在 SP、BS 模式的 BP、MP 节点查询下列系统表和动态视图。在 SP、BS 模式的 BP 节点可查询到的是整个集群所有站点的信息，在 MP 上查询到的只有 MP 站点自身的信息。

## 12.1 DPC\_NETWORK

记录网段信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 网段号 |
| 2 | NAME | VARCHAR(128) | 网段名称 |
| 3 | PREFIX | VARCHAR(64) | 前缀，如 192.168.0 |
| 4 | DESCRIPTION | VARCHAR(256) | 描述信息 |

## 12.2 DPC\_HOST

记录主机信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 主机号 |
| 2 | NAME | VARCHAR(128) | 主机名 |
| 3 | DESCRIPTION | VARCHAR(256) | 描述信息 |

## 12.3 DPC\_HOST\_ADDR

记录主机上多块网卡的地址信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 主机号 |
| 2 | NET\_ID | INTEGER | 网段号 |
| 3 | NET\_ADDR | VARCHAR(64) | IP 地址 |

## 12.4 DPC\_FOLDER

记录 BP 域相关的主机的目录信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 目录号 |
| 2 | DOMAIN\_ID | INTEGER | 域号 |
| 3 | NAME | VARCHAR(128) | 目录名 |
| 4 | HOST\_ID | INTEGER | 主机号 |
| 5 | PATH | VARCHAR(256) | 路径 |
| 6 | DESCRIPTION | VARCHAR(256) | 描述信息 |
| 7 | XMAL\_PORT | INTEGER | XMAL 通信端口号 |

## 12.5 DPC\_BP\_DOMAIN

记录 BP 域信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | BP 域号 |
| 2 | NAME | VARCHAR(128) | 域名 |
| 3 | DESCRIPTION | VARCHAR(256) | 描述信息 |

## 12.6 DPC\_DOMAIN\_FOLDER

记录每个域内包含的所有目录信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | DOMAIN\_ID | INTEGER | 域号 |
| 2 | FOLDER\_ID | INTEGER | 目录号 |
| 3 | BP\_XMAL\_PORT | INTEGER | XMAL 通信端口号 |

## 12.7 DPC\_FOLDER\_INSTANCE

记录每个目录下的所有实例号信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | FOLDER\_ID | INTEGER | 目录号 |
| 2 | INSTANCE\_ID | INTEGER | 实例号 |

## 12.8 DPC\_BP\_GROUP

记录系统中注册的每个 BP 组信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | BP 组号 |
| 2 | NAME | VARCHAR(128) | BP 组名 |
| 3 | DESCRIPTION | VARCHAR(256) | 描述信息 |
| 4 | RAFT\_NUM | INTEGER | 包含 RAFT 组的个数 |
| 5 | RAFT\_INFO | VARBINARY(2048) | 包含的所有 RAFT 组的 Id 信息 |
| 6 | INFO1 | INTEGER | 预留字段 |
| 7 | INFO2 | BIGINT | 预留字段 |
| 8 | INFO3 | VARBINARY(1024) | 预留字段 |

## 12.9 DPC\_BP\_RAFT

记录系统中注册的每个 RAFT 组信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | RAFT\_ID | INTEGER | RAFT 组号 |
| 2 | GROUP\_ID | INTEGER | 本字段废弃，全部记为-1，无意义 |
| 3 | DPC\_MODE | VARCHAR(8) | DMDPC 模式 |
| 4 | NAME | VARCHAR(128) | RAFT 组名 |
| 5 | IS\_VALID | INTEGER | BP 节点是否有效（节点是否可用，0 无效，1 有效） |
| 6 | INFO1 | INTEGER | 预留字段 |
| 7 | INFO2 | BIGINT | 预留字段 |
| 8 | INFO3 | VARBINARY(1024) | 预留字段 |

## 12.10 DPC\_INSTANCE

记录系统中所有实例对象信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | RAFT\_ID | INTEGER | 系统内部 RAFT 组号。取值范围：0~1023 |
| 2 | INST\_ID | INTEGER | 系统内部实例号。取值范围：4096~8191 |
| 3 | NAME | VARCHAR(128) | 实例名 |
| 4 | DPC\_MODE | VARCHAR(8) | DMDPC 模式。取值：MP，SP 或 BP |
| 5 | XMAL\_PORT | INTEGER | XMAL 通信端口号。用户通过 SP\_CREATE\_DPC\_INSTANCE 中 AP\_PORT 注册时配置，取值范围：1024~65534 |
| 6 | INST\_PORT | INTEGER | 实例端口。用户通过 SP\_CREATE\_DPC\_INSTANCE 中 INST\_PORT 注册时配置，取值范围：1024~65534 |
| 7 | IP\_INTERNAL | VARCHAR(512) | 实例内网 IP 地址 |
| 8 | SYS\_MODE | VARCHAR(32) | 系统模式 |
| 9 | SYS\_STATUS | INTEGER | 系统状态。1：启动；2：启动，redo 完成；3：MOUNT；4：打开；5：挂起；6：关闭 |
| 10 | STATUS | INTEGER | 实例状态。1：有效；0：无效；2：SP 正常退出标记；4：SP 灰度升级。仅对 SP 有效 |
| 11 | DESCRIPTION | VARCHAR(256) | 描述信息 |
| 12 | IP\_EXTERNAL | VARCHAR(512) | 实例外网 IP 地址 |
| 13 | INFO1 | INTEGER | 预留字段 |
| 14 | INFO2 | BIGINT | 预留字段 |
| 15 | INFO3 | VARBINARY(1024) | 预留字段 |

## 12.11 DPC\_NET\_CONF

记录连接配置参数。

| **序号** | **列** | **列类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PARA\_NAME | VARCHAR(128) | 参数名。   COMPRESS\_LEVEL 消息压缩级别，取值范围 0~10。0 代表不进行消息压缩，为默认值。1~9 表示采用 zip 算法，从 1 到 9 表示压缩速度依次递减，压缩率依次递增。10 表示采用 snappy 算法，压缩速度高于 zip 算法，压缩率相对低；   CRC\_CHECK 消息的 CRC 检验；   MONITOR\_XLNK\_TIME 监控链路消息收发用时，单位微秒；   TIMEOUT 通信超时，单位为秒；   XLNK\_NUM 链路数；   CENTER\_COMPRESS\_LEVEL 数据中心间通信的压缩等级描述串。格式：’(1,11,2):10/(2,5):2/.../(3,1,4):9’，括号中的数字是中心序号，':'后的数字是上个括号中的数据中心间通信的压缩级别，每个括号内最多 18 个序号，数据中心序号范围 1~18，不能为 0；压缩级别范围 0~10。若某两个数据中心间的压缩等级未在此参数中配置，则以 COMPRESS\_LEVEL 的配置为准。 |
| 2 | PARA\_VALUE | VARCHAR(128) | 参数值 |

## 12.12 DPC\_TABLESPACE

记录 DMDPC 系统的用户表空间。

| **序号** | **列** | **列类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TS\_ID | INTEGER | 全局表空间 ID，全局唯一 |
| 2 | RAFT\_ID | INTEGER | RAFT 组 ID |
| 3 | STATE | INTEGER | 表空间状态。0：联机状态；1：脱机状态 |
| 4 | NAME | VARCHAR(256) | 表空间名，主键 |
| 5 | INFO1 | INTEGER | 预留字段 |
| 6 | INFO2 | BIGINT | 预留字段 |
| 7 | INFO3 | VARBINARY(1024) | 预留字段 |

## 12.13 DPC\_HTS

记录 DMDPC 系统的混合表空间。

| **序号** | **列** | **列类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TS\_ID | INTEGER | 全局表空间 ID，全局唯一 |
| 2 | RAFT\_ID | INTEGER | RAFT 组 ID |
| 3 | STATE | INTEGER | 表空间状态。0：联机状态；1：脱机状态 |
| 4 | NAME | VARCHAR(256) | 表空间名，主键 |
| 5 | INFO1 | INTEGER | 预留字段 |
| 6 | INFO2 | BIGINT | 预留字段 |
| 7 | INFO3 | VARBINARY(1024) | 预留字段 |

## 12.14 DPC\_LONG\_TRX

记录 DMDPC 中长事务相关信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | RAFT\_ID | SMALLINT | 长事务所在的 RAFT 组号 |
| 2 | TYPE | SMALLINT | 长事务的类型（0：全局 min\_tid；1：指定 raft\_id 的一个长事务 id；2：mp 代理故障 sp 的 trxid） |
| 3 | TID | BIGINT | 长事务的 id |
| 4 | START\_TIME | DATETIME | 长事务添加到系统表的时间 |
| 5 | INFO | VARBINARY(1024) | 预留字段 |

## 12.15 V$DPC\_STASK\_THRD

查看每个子任务、每个线程的执行统计信息。当 DM.INI 参数 ENABLE\_MONITOR=1 时有效。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EXEC\_ID | BIGINT | 执行号 |
| 2 | MPP\_EXEC\_ID | BIGINT | 内部的表示执行号 |
| 3 | STASK\_NO | INTEGER | 子任务序号 |
| 4 | THRD\_NO | INTEGER | 工作线程序号 |
| 5 | PLAN\_NO | INTEGER | 子计划序号 |
| 6 | START\_TIME | DATETIME(0) | 当前线程的开始工作时间 |
| 7 | TIME\_USED | INTEGER | 当前线程执行子任务的耗时，单位毫秒 |
| 8 | FIRST\_ROW\_USED | INTEGER | 返回第一行数据的耗时，单位毫秒 |
| 9 | N\_ROWS\_SEND | BIGINT | 子任务输出的行数，对于 HTAB 操作符为存储的行数 |
| 10 | N\_BYTES\_SEND | BIGINT | 子任务输出的数据大小，字节为单位 |
| 11 | N\_ROWS\_RECV | VARCHAR(1024) | 如果子任务有 ERECV 操作符，展示接收的行数 |
| 12 | P\_WAIT\_TIMES | VARCHAR(1024) | 打开限流时，请求资源操作的等待次数。未打开限流时，此值无意义 |
| 13 | IS\_OVER | CHAR(1) | 工作线程执行是否结束。Y 是；N 否 |
| 14 | THRD\_ID | BIGINT | 工作线程 ID |
| 15 | SESS\_ID | BIGINT | 会话号 |

例 查看执行号 16777624 的执行情况。

```
select * from v$dpc_stask_thrd where exec_id  = 16777624;
```

由于 V$dpc\_stask\_thrd 记录的是原始信息，我们也可以在它的基础上定义视图方便查看。

例 创建一个视图 v\_eet，将 V$DPC\_STASK\_THRD 中的信息，通过 v\_eet 展示出来。

```
create or replace view v_eet as select y.name name, 
                                       exec_id, 
                                       mpp_exec_id, 
                                       stask_no, 
                                       thrd_no, 
                                       cast(start_time as varchar(30)) as START_TIME, 
                                       time_used as TIME_USED_IN_MS, 
                                       first_row_used as FIRST_ROW_IN_MS, 
                                       n_rows_send as SENT_ROWS,
                                       case when n_bytes_send > 1024 * 1024 * 1024 then cast(n_bytes_send / 1024.0 / 1024 / 1024 as decimal(38,3)) || 'G' 
                                            when n_bytes_send > 1024 * 1024 then cast(n_bytes_send / 1024.0 / 1024 as decimal(38,3)) || 'M' 
                                            when n_bytes_send = 0 then 0 
                                            else cast(n_bytes_send / 1024.0 as decimal(38,3)) || 'K' end as SENT,
                                       n_rows_recv as RECV_ROWS,
                                       is_over
                                 from SYS.V$DPC_STASK_THRD x, SYS.DPC_BP_RAFT y
                                 where SF_GET_EP_SEQNO(x.rowid) = y.raft_id
                                 order by stask_no, name, thrd_no;
```

通过 v\_eet 查看执行事务号为 16777624 的执行语句的执行时间。

```
select * from v_eet where exec_id = 16777624;
```

查看结果：

图12.1 执行语句的统计信息

从上图观察同一个 stask\_no 的不同 thrd\_no 线程的执行时间（TIME\_USED\_IN\_MS），可以大概看出工作线程间的负载是否均衡，哪一个子任务耗时最久等信息。

通过观察 SENT\_ROWS、SENT 和 RECV\_ROWS 字段信息，可以看到每个线程发送、接收的数据量，分析出是否数据分布不均匀。比如某个子任务并行度为 2、THRD\_NO=0 的线程接收了 1000000 记录，THRD\_NO=1 的线程接收了 500 条记录，差别这么大的情况下我们可以继续分析数据来源，为何会存在这么大的不均衡。

例 执行事务号 16777624 对应的绿色区域为最根层子任务（stask\_no 等于-1），安排了一个工作线程，耗时 78 毫秒。

红色区域为子任务 0，共安排了 8 个线程调度执行，耗时最久的为 2 号线程用时 16ms，其余都是 0ms。由于子任务 0 工作量不大，所以这点差距可以忽略。

假设某个子任务工作量很大的前提下，不同线程完成的时间差距很大，这时可以先观察 START\_TIME，查看线程是否同时被调度？接收、发送行数是否均衡？

通过调整数据分布和工作线程个数，或者改变数据分发方式，我们可以对数据负载做出一定程度的均衡。

## 12.16 V$RLOG\_RAFT\_INFO

查询当前节点的选举状态和日志提交信息。配置成多副本系统的情况下，V$RLOG\_RAFT\_INFO 的值才是真实有效的，单副本系统情况下，V$RLOG\_RAFT\_INFO 的值无实际意义。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TERM\_ID | INTEGER | 当前节点所处的任期号 |
| 2 | STATE | VARCHAR(16) | 当前节点所处的角色 |
| 3 | LEADER | VARCHAR(256) | 当前的主库（领导者）实例名 |
| 4 | LOG\_TERM\_ID | INTEGER | 当前节点已经刷盘的任期号 |
| 5 | C\_SEQ | BIGINT | 当前节点已经提交到的日志包序号 |
| 6 | C\_LSN | BIGINT | 当前节点已经提交到的 LSN 值 |
| 7 | F\_SEQ\_ARR | VARCHAR(2048) | 所有实例已经刷盘完成的日志包序号数组，仅在主库上查询才有效 |
| 8 | F\_LSN\_ARR | VARCHAR(2048) | 所有实例已经刷盘完成的 LSN 数组，仅在主库上查询才有效 |
| 9 | H\_SEQ | BIGINT | 主节点已经提交到的日志包序号 |
| 10 | H\_LSN | BIGINT | 主节点已经提交到的 LSN 值 |
| 11 | NEED\_WAIT | VARCHAR(8) | 备库是否达到日志堆积上限，仅在主库上查询才有效 |
| 12 | SELF\_STATUS | VARCHAR(8) | 当前节点实例状态是否有效，仅在主库上查询才有效 |
| 13 | HP\_FLAG | VARCHAR(8) | 当前节点日志是否堆积 |
| 14 | SWITCH\_TIME | VARCHAR(50) | 当前节点上一次模式切换的时间 |
| 15 | ARCH\_CHG\_FLAG | VARCHAR(16) | 当前节点是否在执行节点变更 |
| 16 | ARCH\_CHG\_STAT | VARCHAR(32) | 当前节点所处的变更状态 |
| 17 | DEST\_ID\_ARR | VARCHAR(2048) | 当前节点实例 ID 数组。与 F\_SEQ\_ARR 和 F\_LSN\_ARR 一一对应 |
| 18 | RAFT\_SHADOW | INTEGER | 当前节点是否是影子库。0：否；1：是 |
| 19 | TOTAL\_CACHE\_TIME | BIGINT | 当前日志包总缓存时间。仅 RAFT 备库查询有效。单位：US |

## 12.17 V$SQL\_NODE\_HISTORY

通过该视图既可以查询 sql 执行节点信息，包括 sql 节点的类型、进入次数和使用时间等等；又可以查询所有执行的 sql 节点执行情况，如哪些使用最频繁、耗时多少等。

当 INI 参数 ENABLE\_MONITOR 和 MONITOR\_SQL\_EXEC 都开启时，才会记录 SQL 执行节点信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEQ\_NO | INTEGER | 操作符在计划中的序号，即 explain 显示执行计划时的行号 |
| 2 | EXEC\_ID | BIGINT | 执行 ID |
| 3 | NODE | BIGINT | 节点 ID |
| 4 | TYPE$ | INTEGER | 节点类型 |
| 5 | BYTES\_DYNAMIC\_ALLOCED | BIGINT | 动态分配字节数 |
| 6 | BYTES\_DYNAMIC\_FREED | BIGINT | 动态释放字节数 |
| 7 | N\_ENTER | INTEGER | 节点进入次数 |
| 8 | TIME\_USED | BIGINT | 节点执行所耗时，单位为微秒 |
| 9 | PLN\_OP\_ID | INTEGER | MPP 模式下，节点所属通讯操作符中的序号 |
| 10 | BYTES\_SEND | BIGINT | 发送的字节数，仅在 MPP 环境下有效 |
| 11 | BYTES\_RECV | BIGINT | 接收的字节数，仅在 MPP 环境下有效 |
| 12 | ROWS\_SEND | BIGINT | 发送的行数，仅在 MPP 环境下有效 |
| 13 | ROWS\_RECV | BIGINT | 接收的行数，仅在 MPP 环境下有效 |
| 14 | BDTA\_SEND | BIGINT | 发送 BDTA 的次数，仅在 MPP 环境下有效 |
| 15 | BDTA\_RECV | BIGINT | 接收 BDTA 的次数，仅在 MPP 环境下有效 |
| 16 | MAL\_ID | BIGINT | 邮件标识号 |
| 17 | MPP\_EXEC\_ID | BIGINT | MPP 会话句柄上的执行序号，同一个会话上的每个节点上值相同 |
| 18 | HASH\_USED\_CELLS | BIGINT | 哈希表上使用的槽数 |
| 19 | HASH\_CONFLICT | BIGINT | 哈希表上每个槽的冲突的个数 |
| 20 | STASK\_NO | INTEGER | 节点所在的子任务号 |
| 21 | THRD\_NO | INTEGER | 节点所在的线程号 |
| 22 | MEM\_USED | BIGINT | 操作符使用的内存空间，单位 KB |
| 23 | DISK\_USED | BIGINT | 操作符预期使用的磁盘空间，单位 KB |
| 24 | DHASH3\_USED\_CELLS | VARCHAR(500) | 动态哈希表中使用的槽数 |
| 25 | DHASH3\_CONFLICT | VARCHAR(300) | 动态哈希表中的冲突情况 |
| 26 | HASH\_SAME\_VALUE | BIGINT | 开启哈希相同值挂链优化时，记录哈希表中相同值的总数，唯一值不纳入计数。例如：哈希表中存在一个 0 和两个相同值链 1—1—1、3—3，此时 HASH\_SAME\_VALUE=5 |
| 27 | SORT\_BUF\_ROWS | BIGINT | 排序操作符的排序缓冲区存放的总行数（关闭大内存排序时）或每路排序的行数（开启大内存排序时） |
| 28 | SORT\_BUF\_AVG\_ROWSIZE | BIGINT | 排序操作符的排序缓冲区存放数据的预估平均行长，单位 Byte |

## 12.18 V$DPC\_MP\_CFG

记录 RAFT 组内的 MP 实例信息。由于一个 RAFT 内最多 9 个实例，因此最多 9 条记录。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INST\_NAME | VARCHAR(128) | 实例名 |
| 2 | IP\_ADDRESS | VARCHAR(128) | IP 地址 |
| 3 | MP\_PORT | INTEGER | MP\_PORT |
| 4 | RECONN\_TIMEOUT | INTEGER | 连接 MP 失败时，尝试重连的超时时间，单位为秒。-2 表示无限制（即 MP\_RECONN\_TIMEOUT 取最大值）。该值由 MP.INI 中参数 MP\_RECONN\_TIMEOUT 来设置 |

## 12.19 V$DPC\_QC\_HISTORY

记录查询调度总单元 QC 的历史信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SESS\_ID | BIGINT | 和 V$SESSIONS 的 SESS\_ID 字段匹配 |
| 2 | SESS\_SEQ | INTEGER | 和 V$SESSIONS 的 SESS\_SEQ 字段匹配 |
| 3 | EID | BIGINT | ESESSION 的 ID |
| 4 | THRD\_ID | BIGINT | 创建 QC 的线程 ID |
| 5 | STMT\_ID | INTEGER | 句柄 ID |
| 6 | EXEC\_ID | BIGINT | 执行 ID |
| 7 | MPP\_EXEC\_ID | BIGINT | 内部执行 ID |
| 8 | SQC\_EXEC\_ID | BIGINT | 内部执行 ID，当函数调用包含 SQL 时，每一行调用时取值会不同 |
| 9 | N\_STASK | INTEGER | 子任务的个数 |
| 10 | IDU\_FLAG | VARCHAR(6) | 增删改的优化标记 |
| 11 | N\_BP | INTEGER | 计划涉及到的集群中节点个数，可能包含 SP、BP、MP |
| 12 | N\_HTAB | INTEGER | 子计划中 HTAB 操作符的个数 |
| 13 | N\_SPL | INTEGER | 子计划中 SPOOL 操作符的个数 |
| 14 | N\_DPP | INTEGER | 子计划中涉及的动态分区裁剪参数个数 |
| 15 | IS\_OVER | CHAR(1) | 是否执行结束。Y 是；N 否 |

## 12.20 V$ARCH\_STATUS

查询归档状态信息，归档状态是由主库记录和维护的，此视图只在主库上查询有效，备库上的查询结果没有实际意义。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ARCH\_TYPE | VARCHAR(256) | 归档类型 |
| 2 | ARCH\_DEST | VARCHAR(256) | 归档目标，本地归档和 REMOTE 归档为归档路径，其他类型为归档目标实例名。 |
| 3 | ARCH\_STATUS | VARCHAR(256) | 归档状态，Valid 为有效状态，Invalid 为无效状态，ASYNC\_SEND 为异步恢复状态。 |
| 4 | ARCH\_SRC | VARCHAR(256) | 对 REMOTE 归档为源实例名，对其他归档类型为本地实例名 |

## 12.21 V$DPC\_EGTS\_MP\_INFO

MP 上记录的各 SP 和 BP 的全局时钟系统（GTS）信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | RAFT\_ID | INTEGER | SP 和 BP 的 RAFT\_ID |
| 2 | STAT | VARCHAR(20) | 状态(OPEN/SHUTDOWN/CONN\_LOST) |
| 3 | MIN\_TID | BIGINT | 最小 TRXID |
| 4 | N\_LONG | INTEGER | 长事务个数 |
| 5 | LAST\_CHK\_TICK | BIGINT | 上次检查的 TICK 计数 |
| 6 | PROXY\_STAT | INTEGER | MP 代理故障 SP 的进度状态 |
| 7 | PROXY\_VER | INTEGER | MP 代理时故障 SP 的网络版本 |
| 8 | PROXY\_TID | BIGINT | MP 代理时的事务 ID，标识故障 SP 的最大事务 ID |
| 9 | PROXY\_FLAG | INTEGER | MP 代理处理时广播 BP 的标记 |
| 10 | PROXY\_FLAG\_ARR | VARCHAR(2048) | 各 RAFT 节点的 PROXY\_FLAG |

## 12.22 V$DPC\_ENET\_HISTORY

获取 ENET 模块更新各个节点的设置历史。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | SELF\_RAFT\_ID | INTEGER | 自身的 RAFT\_ID |
| 2 | SELF\_INST\_ID | INTEGER | 自身的 INST\_ID |
| 3 | DEST\_RAFT\_ID | INTEGER | 目标的 RAFT\_ID |
| 4 | DEST\_INST\_ID | INTEGER | 目标的 INST\_ID |
| 5 | TYPE | VARCHAR(20) | 操作类型(SET/RELEASE) |
| 6 | SITE\_ADDR | VARBINARY(8) | 节点 XSITE 的内存地址 |
| 7 | DESC | VARCHAR(30) | 变更原因描述 |
| 8 | TIME | TIMESTAMP | 变更发生的时间 |

## 12.23 V$ARCH\_SYS

获取全局归档配置信息。

| **序号** | **列名** | **列类型** | **含义** |
| --- | --- | --- | --- |
| 1 | ARCH\_COUNT | INTEGER | 归档数目 |
| 2 | ARCH\_CFG\_CHANGING | INTEGER | 归档变更标记 |
| 3 | ARCH\_WAIT\_APPLY | INTEGER | 全局事务一致标记 |
| 4 | RAFT\_SELF\_ID | INTEGER | 自身 RAFT 归档序号，仅 RAFT 归档有效 |
| 5 | XMAL\_IP | VARCHAR(64) | RAFT 归档通信 IP |
| 6 | XMAL\_PORT | INTEGER | RAFT 归档通信端口 |
| 7 | XMAL\_HB\_INTERVAL | INTEGER | RAFT 归档 XMAL 链路心跳检测间隔 |
| 8 | RAFT\_HB\_INTERVAL | INTEGER | RAFT 归档心跳检测间隔 |
| 9 | RAFT\_VOTE\_INTERVAL | INTEGER | RAFT 归档选举超时间隔 |
| 10 | ARCH\_RESERVE\_TIME | INTEGER | 归档保留时间。单位分钟 |
| 11 | ARCH\_LOCAL\_SHARE | INTEGER | 远程归档是否共享其它节点本地归档路径。0：否；1：是 |
| 12 | ARCH\_LOCAL\_SHARE\_CHECK | INTEGER | 是否检查远程归档路径和其它节点本地归档路径相等。0：否；1：是 |

## 12.24 V$DM\_ARCH\_INI

归档参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ARCH\_NAME | VARCHAR (128) | 归档名称 |
| 2 | ARCH\_TYPE | VARCHAR (128) | 归档类型 |
| 3 | ARCH\_DEST | VARCHAR (512) | 对于 LOCAL 归档，表示归档路径；对于 REMOTE 归档，表示本节点归档要发送到的实例名；对于其余类型的归档，表示归档目标实例名 |
| 4 | ARCH\_FILE\_SIZE | INTEGER | 归档文件大小 |
| 5 | ARCH\_SPACE\_LIMIT | INTEGER | 归档文件的磁盘空间限制，单位 MB |
| 6 | ARCH\_HANG\_FLAG | INTEGER | 如果本地归档时磁盘空间不够，是否让服务器挂起。无实际意义，对本地归档类型和远程归档类型显示为 1，其他归档类型显示为 NULL |
| 7 | ARCH\_TIMER\_NAME | VARCHAR (128) | 对于异步归档，表示定时器名称；其余类型归档显示 NULL |
| 8 | ARCH\_IS\_VALID | CHAR(1) | 归档状态，是否有效。0：否；1：是 |
| 9 | ARCH\_WAIT\_APPLY | INTEGER | 在主备系统中，主库发送归档日志给备库之前，是否需要等待备库将上一批日志重演完成。取值 0：高性能模式，不用等待重演完成；1：事务一致模式，需等待重演完成。除即时归档和实时归档外，其他归档取值均为 NULL |
| 10 | ARCH\_INCOMING\_PATH | VARCHAR(256) | 对 REMOTE 归档，表示远程节点发送过来的归档在本地的保存目录。其余类型归档显示 NULL |
| 11 | ARCH\_CURR\_DEST | VARCHAR(256) | 当前归档目标实例名。如果备库是 DMDSC 集群，则归档目标是备库控制节点，该字段表示当前被选定为归档目标的节点实例名。备库是单机的情况下，就是指的备库实例名 |
| 12 | ARCH\_FLUSH\_BUF\_SIZE | INTEGER | 归档刷盘日志包合并缓存大小。 单位为 KB |
| 13 | ARCH\_RESERVE\_TIME | INTEGER | 归档保留时间。单位分钟 |
| 14 | ARCH\_LOCAL\_SHARE | INTEGER | 远程归档是否共享其它节点本地归档路径。0：否；1：是 |
| 15 | ARCH\_LOCAL\_SHARE\_CHECK | INTEGER | 是否检查远程归档路径和其它节点本地归档路径相等。0：否；1：是 |
| 16 | ARCH\_SEND\_DELAY | INTEGER | 源库到异步备库的归档延时发送时间。单位分钟。0 表示未启用归档延时发送功能 |
| 17 | ARCH\_DEST\_IP | VARCHAR(64) | RAFT 归档目标 IP |
| 18 | ARCH\_DEST\_PORT | INTEGER | RAFT 归档目标端口 |
| 19 | ARCH\_DEST\_ID | INTEGER | 归档目标多副本节点编号，用于标识多副本 RAFT 组中不同的节点 |
| 20 | ARCH\_ASM\_MIRROR | SMALLINT | 归档文件配置在 DMASM 上的镜像类型，DMASM 镜像专用，取值：1：单副本，表示外部冗余，不提供任何镜像，假设磁盘高度可靠；2：双副本，表示正常冗余，提供双向镜像，可较好的保证数据完整性；3：三副本，表示高度冗余，提供三向镜像，能够更好的保证数据的完整性。未配置显示 NULL。 仅在 DMASM 镜像环境下有效 |
| 21 | ARCH\_ASM\_STRIPING | SMALLINT | 归档文件配置在 DMASM 上的条带化粒度，DMASM 镜像专用，取值 0 表示粗粒度，32/64/128/256 表示细粒度条带化大小，单位 KB。未配置显示 NULL。 仅在 DMASM 镜像环境下有效 |
| 22 | ARCH\_RECOVER\_TIME | INTEGER | 主库向归档状态为 Invalid 的同步备库发起异步恢复的时间间隔，单位为秒 |

## 12.25 V$DPC\_ESESS\_STMTS

查询 DMDPC 系统内部所有 ESESSION 的所有语句句柄信息。ESESSION 为 SP 和其他节点之间的内部会话。该视图提供给达梦内部开发人员调试之用。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | STMT\_ID | INTEGER | 句柄 ID |
| 2 | SESS\_ID | BIGINT | 会话 ID |
| 3 | ESESS\_ID | BIGINT | ESESSION 的 ID |
| 4 | PLAN\_NO | INTEGER | 计划序号 |
| 5 | SQC\_EXEC\_ID | BIGINT | 语句执行序号 |
| 6 | N\_BOXID\_REUSE | INTEGER | 当前句柄上已分配的 BOXID |
| 7 | FREE\_FLAG | INTEGER | 空闲句柄标记 |

## 12.26 V$DPC\_EXA\_INFO

查询当前连接的服务器正在自动处理的异步事务信息。异步事务是指 DPC 下事务提交失败、节点故障重启时，不再和会话绑定，而是将事务抛出执行异步处理。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TID | BIGINT | 异步处理事务 ID |
| 2 | STATUS | INTEGER | 事务处理状态 |
| 3 | BRANCH\_STATUS | INTEGER | 重构异步事务在来源站点的状态 |
| 4 | CMTSEQ | BIGINT | 提交序号 |
| 5 | ACKID | BIGINT | 异步处理通信标识 |
| 6 | TICK | BIGINT | 开始异步处理的时间戳 |
| 7 | N\_RAFT | INTEGER | 事务涉及的站点数 |
| 8 | RAFTID\_ARR | VARCHAR | 事务涉及的站点 RAFT ID |
| 9 | STATUS\_ARR | VARCHAR | 事务在各站点的分支事务状态 |
| 10 | SRC\_SITE | INTEGER | 发起该事务的站点的 RAFT ID |

## 12.27 V$DPC\_ROT\_INFO

查询集群各个节点已加载的只读表信息。此外，可以通过 SF\_GET\_EP\_SEQNO(ROWID);查看本视图数据所在实例的 RAFT\_ID。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ROT\_TID | INTEGER | 只读表 ID |
| 2 | ROT\_VERSION | INTEGER | 只读表版本号 |
| 3 | TEMP\_TID | INTEGER | 只读表对应的临时表 ID |
| 4 | TEMP\_VERSION | INTEGER | 只读表对应的临时表版本号 |
| 5 | LOAD\_TIME | DATETIME(0) | 加载时间 |
| 6 | LAST\_USED\_TIME | DATETIME(0) | 最后一次使用时间 |

## 12.28 V$DPC\_ESESS

查询 DMDPC 系统内部所有 ESESSION 的信息。ESESSION 为 SP 和其他节点之间的内部会话。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EID | BIGINT | 会话 ID |
| 2 | SRC\_SITEID | INTEGER | 对应 SP 的 RAFT\_ID |
| 3 | BP\_CTL\_BOXID | INTEGER | BP 端 ESESS 会话用于接收消息的消息盒子号 |
| 4 | TRX\_BOXID | INTEGER | SP 上用于处理事务使用的消息盒子号 |
| 5 | SESS\_ID | BIGINT | 对应会话的 ID |
| 6 | M\_EID | BIGINT | 目前未使用（废弃字段），全是 NULL |
| 7 | N\_SITE | INTEGER | 缓存的远程站点对象数 |
| 8 | N\_TRX\_SITE | INTEGER | 当前事务涉及的节点个数 |
| 9 | STHD\_GRP\_ID | INTEGER | ESESS 对应的线程池编号，非 ethd 线程为-1 |
| 10 | THRD\_ID | INTEGER | ESESS 对应的线程号，不与线程关联时为-1 |
| 11 | N\_STMT | INTEGER | ESESS 的语句句柄个数 |

## 12.29 V$DPC\_EDCT\_RAFT

查询 DMDPC 系统各节点内存中记录的 RAFT 信息。MP 上的信息对应 DPC\_BP\_RAFT 系统表的内容。SP 和 BP 上的内容是 MP 发送过来的。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RAFT\_ID | INTEGER | RAFT 组号 |
| 2 | DPC\_MODE | VARCHAR(16) | DMDPC 模式 |
| 3 | IS\_VALID | CHAR(1) | BP 节点是否有效（节点是否可用，0 无效，1 有效） |
| 4 | NAME | VARCHAR(128) | RAFT 组名 |
| 5 | L\_TERM\_ID | BIGINT | 主库的任期号 |
| 6 | DISCARD\_TICK | BIGINT | 废弃时的 tick 时间值 |

## 12.30 V$DPC\_EDCT\_INSTANCE

查询 DMDPC 系统各节点内存中记录的实例信息。MP 上的信息对应 DPC\_INSTANCE 系统表的内容。SP 和 BP 上的内容是 MP 发送过来的。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RAFT\_ID | INTEGER | 系统内部 RAFT 组号。取值范围：0~1023 |
| 2 | INST\_ID | INTEGER | 系统内部实例号。取值范围：4096~8191 |
| 3 | NAME | VARCHAR(128) | 实例名 |
| 4 | MODE | VARCHAR(16) | DMDPC 模式。取值范围：MP，SP 或 BP |
| 5 | XMAL\_PORT | INTEGER | XMAL 通信端口号。用户通过 SP\_CREATE\_DPC\_INSTANCE 中 AP\_PORT 注册时配置，取值范围：1024~6553 |
| 6 | INST\_PORT | INTEGER | 实例端口。用户通过 SP\_CREATE\_DPC\_INSTANCE 中 INST\_PORT 注册时配置，取值范围：1024~65534 |
| 7 | IP\_INTERNAL | VARCHAR(64) | 实例内网 IP 地址 |
| 8 | IP\_EXTERNAL | VARCHAR(64) | 实例外网 IP 地址 |
| 9 | SYS\_MODE | VARCHAR(16) | 系统模式 |
| 10 | SYS\_STATUS | VARCHAR(16) | 系统状态 |
| 11 | STATUS | VARCHAR(16) | 实例状态 |
| 12 | AUX\_SP | CHAR(1) | 是否辅助 SP |
| 13 | DISCARD\_TICK | BIGINT | 废弃时的 tick 时间值 |
| 14 | DESC | VARCHAR(256) | 描述信息 |
| 15 | BS\_FLAG | INTEGER | BS 启动标记。0：非 BS；1：BS |
| 16 | FAULT\_DOMAIN | INTEGER | 保留字段 |

## 12.31 V$TABLE\_ROWCNT\_CACHE

显示 DMDPC 系统中各节点中的缓存表行数情况。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TAB\_ID | INTEGER | 表 ID |
| 2 | ROWCNT | BIGINT | 表行数 |
| 3 | ACCESS\_NUM | INTEGER | 访问次数 |

## 12.32 V$DPC\_TS\_MOVE

查询 DMDPC 系统当前表空间迁移进度等信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TS\_ID | INTEGER | 表空间 ID |
| 2 | READ\_ONLY | INTEGER | 只读迁移标记。1：只读，0：读写 |
| 3 | SRC\_RAFT\_ID | INTEGER | 表空间迁移源 RAFT\_ID |
| 4 | DEST\_RAFT\_ID | INTEGER | 表空间迁移目标 RAFT\_ID |
| 5 | BP\_TS\_CRT\_LSN | BIGINT | 目标 BP 主库创建 TS 后的 CUR\_LSN |
| 6 | START\_TIME | DATETIME(0) | 开始迁移时间 |
| 7 | DURING\_TIME | INTEGER | 从开始迁移的持续的时间(秒） |
| 8 | PROGRESS\_TYPE | VARCHAR(128) | 当前进行的操作进度类型。PROGRESS\_TYPE 为字符串类型，其值包含 2 部分： **\[**当前进度类型:进度值**\]\[**当前进度序号/迁移总进度值**\]** 。 进度类型包括：字典封锁（LOCK\_DICT）、表空间清理（PURG\_TS）、执行检查点（CHECKPOINT）、文件拷贝（FILE\_COPY）、日志重演（APPLY\_ARCH）。例如：\*\*\[**FILE\_COPY:1442818560/2097152000(%68)**\]\[**2/6**\]\*\*表示处于文件拷贝阶段，已经拷贝的字节数/总字节数（完成百分比），处于 6 阶段中的第 2 阶段； \*\*\[**APPLY\_ARCH:1**\]\[**3/6**\]\*\*表示处于重演日志阶段，第 1 次重演，处于 6 阶段中的第 3 阶段 |

## 12.33 V$DPC\_QC\_SCHED\_HISTORY

查询 DMDPC 任务调度历史信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MPP\_EXEC\_ID | BIGINT | 执行号 |
| 2 | STMT\_ID | INTEGER | 句柄号 |
| 3 | EID | BIGINT | DPC 全局会话 ID |
| 4 | STASK\_NO | INTEGER | 子任务号 |
| 5 | STATUS | VARCHAR(8) | 调度状态，取值：   NONE：未调度   SCHDLED：已调度   COMPLETE：调度完成 |
| 6 | EXEC\_ID | BIGINT | VM 执行号 |

## 12.34 V$GLOBAL\_RAFT\_INFO

查询 DMDPC 系统全局多副本信息。仅会打印可正常通信的 MP/BP/BS 库的多副本信息；若节点异常，则不会打印该实例信息；或若 RAFT 组内无有效主库，则对应 RAFT 组中所有节点信息均不会打印。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | RAFT\_ID | INTEGER | RAFT 组 ID |
| 3 | IS\_SHADOW | VARCHAR(8) | 是否是影子库 |
| 4 | IS\_LEARNER | VARCHAR(8) | 是否是学习者 |
| 5 | RAFT\_STAT | VARCHAR(16) | 副本角色 |
| 6 | TERM\_ID | INTEGER | 任期号 |
| 7 | LOG\_TERM\_ID | INTEGER | 日志任期号 |
| 8 | SYS\_MODE | VARCHAR(16) | 系统模式 |
| 9 | SYS\_STATUS | VARCHAR(16) | 系统状态 |
| 10 | ARCH\_STATUS | VARCHAR(16) | 归档状态。该字段结果在 DMDPC 下，连接主库或 SP 查询有效，连接备库查询无效；在 RAFT 下，连接主库查询有效，连接备库查询无效 |
| 11 | C\_SEQNO | BIGINT | 已经提交到的日志包序号 |
| 12 | C\_LSN | BIGINT | 节点已经提交到的 LSN 值 |
| 13 | H\_SEQNO | BIGINT | 主库已经提交到的日志包序号 |
| 14 | H\_LSN | BIGINT | 主库节点已经提交到的 LSN 值 |
| 15 | F\_SEQNO | BIGINT | 已经刷盘的最大日志包序号 |
| 16 | F\_LSN | BIGINT | 已经刷盘到的最大 LSN 值 |
| 17 | CENTER\_ID | INTEGER | 数据中心序号。Learner 节点无意义，显示为 0 |

## 12.35 V$RAFT\_SWITCH\_INFO

记录多副本系统中当前节点的历史切换信息，直连多副本节点查询。最多纪录 128 条，超过 128 条时新的历史切换信息会覆盖之前的历史切换信息。

当 DM.INI 参数 ENABLE\_MONITOR=1 时有效。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 执行切换的实例名 |
| 2 | RAFT\_ID | INTEGER | 所属 RAFT 组序号 |
| 3 | OLD\_MODE | VARCHAR(16) | 切换前服务器模式 |
| 4 | NEW\_MODE | VARCHAR(16) | 切换后服务器模式 |
| 5 | OLD\_STATUS | VARCHAR(16) | 切换前服务器状态 |
| 6 | NEW\_STATUS | VARCHAR(16) | 切换后服务器状态 |
| 7 | OLD\_ROLE | VARCHAR(16) | 切换前角色 |
| 8 | NEW\_ROLE | VARCHAR(16) | 切换后角色 |
| 9 | OLD\_LEADER | VARCHAR(128) | 切换前 LEADER 实例名，若 LEADER 不存在则该值为空 |
| 10 | NEW\_LEADER | VARCHAR(128) | 切换后 LEADER 实例名，若 LEADER 不存在则该值为空 |
| 11 | SWITCH\_TIME | VARCHAR(50) | 切换执行的时间，精确到微秒 |
| 12 | INST\_NUM | INTEGER | RAFT 组内的节点个数，包含 LEARNER 节点 |

## 12.36 V$DPC\_ESITE

获取各个节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SELF\_RAFT\_ID | INTEGER | 自身的 RAFT 组号，用于统合时区分 |
| 2 | SELF\_INST\_ID | INTEGER | 自身的实例号，用于统合时区分 |
| 3 | DEST\_RAFT\_ID | INTEGER | 目标节点的服务器的 RAFT 组号 |
| 4 | DEST\_INST\_ID | INTEGER | 目标节点的实例号 |
| 5 | DEST\_DPC\_MODE | CHAR(2) | 目标节点的 dpc\_mode |
| 6 | SITE\_ID | BIGINT | 节点 XSITE 的 id |
| 7 | SITE\_ADDR | VARBINARY(8) | 节点 XSITE 的内存地址 |
| 8 | SITE\_TYPE | VARCHAR(16) | 节点 XSITE 的类型（AP、EP） |
| 9 | ASITE\_CONN\_IP | VARCHAR(128) | 节点 XSITE 连接的 IP（仅 AP） |
| 10 | ESITE\_ASITE\_ID | BIGINT | 节点 XSITE 的 asite\_id（仅 EP） |
| 11 | SITE\_STAT | VARCHAR(16) | 节点 XSITE 链路状态（CLOSE/OPEN） |
| 12 | SITE\_N\_LNK | INTEGER | 节点 XSITE 有效的链路个数 |
| 13 | ROUTE\_PRIORITY | INTEGER | 目标节点的路由优先级 |

## 12.37 V$XBOX

获取并显示系统中所有 XBOX 的槽信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | XBOX ID |
| 2 | SLOT\_NO | INTEGER | XBOX 内的槽号 |
| 3 | LETTER\_NUM | INTEGER | 槽内收到的邮件数 |
| 4 | FILE\_NAME | VARCHAR(256) | 创建 XBOX 的文件名 |
| 5 | FILE\_LINE | INTEGER | 创建 XBOX 的文件行号 |
| 6 | EID | BIGINT | 使用 XBOX 的 ESESS\_ID |
| 7 | SIO | INTEGER | 使用 XBOX 的 ERECV 操作符在计划中的行序号 |
| 8 | STASK\_NO | INTEGER | 使用 XBOX 的 ERECV 操作符在计划中的子任务号 |
| 9 | NO\_IN\_STASK | INTEGER | 使用 XBOX 的 ERECV 操作符在子任务中的序号 |
| 10 | DUMP\_LEN\_BYTES | BIGINT | XBOX 上使用临时文件保存的邮件总量，单位 BYTE |
| 11 | LONG\_BYTES | BIGINT | 槽内缓存的大于 32KB 的消息空间大小 |
| 12 | SHORT\_NUM | INTEGER | 槽内缓存的 1KB 大小的消息数 |
| 13 | MIDDLE\_NUM | INTEGER | 槽内缓存的 32KB 大小的消息数 |
| 14 | LONG\_NUM | INTEGER | 槽内缓存的大于 32KB 大小的消息数 |
| 15 | DUMP\_NUM | INTEGER | 槽内缓存的需转储的消息数 |

## 12.38 GV$DM\_INI

DPC 环境下查询所有正常打开实例的 INI 参数。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR (128) | 实例名 |
| 2 | PARA\_NAME | VARCHAR (128) | 参数名称 |
| 3 | PARA\_VALUE | VARCHAR(256) | 系统参数值 |
| 4 | MIN\_VALUE | VARCHAR(256) | 最小值 |
| 5 | MAX\_VALUE | VARCHAR(256) | 最大值 |
| 6 | DEFAULT\_VALUE | VARCHAR(256) | 默认值 |
| 7 | MPP\_CHK | CHAR(1) | 是否检查 MPP 节点间参数一致性。Y 是，N 否 |
| 8 | SESS\_VALUE | VARCHAR(256) | 会话参数值 |
| 9 | FILE\_VALUE | VARCHAR(256) | INI 文件中参数值 |
| 10 | DESCRIPTION | VARCHAR(256) | 参数描述 |
| 11 | PARA\_TYPE | VARCHAR(200) | 参数类型 |
| 12 | SYNC\_FLAG | VARCHAR(16) | 已废弃，取值 UNKNOWN |
| 13 | SYNC\_LEVEL | VARCHAR(16) | 已废弃，取值 UNKNOWN |
| 14 | PARA\_MODULE | VARCHAR(32) | 标识参数所属模块，有如下可能取值： files location、instance name、memory pool and buffer、thread、query、select rate、cpu、checkpoint、IO、database、pre-load table、redo log、redo、transaction、security、security2、compatibility、drop table、fast insert、request trace、system trace、ecs、monitor、data watch、for test only、for context index、rdma、configuration file、DSC、mem only、backup and restore |
| 15 | PRIMARY\_SYNC | CHAR(1) | 参数是否会进行主备同步，取值：Y/N。Y：会进行主备同步，N：不会主备同步 |
| 16 | DSC\_SYNC | CHAR(1) | 参数是否进行 DSC 节点间同步，取值：Y/N。Y：会进行 DSC 节点间同步，N：不会进行 DSC 节点间同步 |

## 12.39 GV$DPC\_CENTER\_COMPRESS\_LEVEL

查询 dpc 内所有节点数据中心间通信的消息压缩等级描述串信息。SP 执行会打印可正常通信的所有 MP/BP/BS 库的信息；若节点异常，则不会打印该实例信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 实例名 |
| 2 | CENTER\_COMPRESS\_LEVEL | VARCHAR(128) | 数据中心间通信的消息压缩等级描述串 |

## 12.40 GV$RAFT\_SWITCH\_INFO

记录整个多副本系统的历史切换信息，直连多副本节点查询。每个节点最多纪录 128 条，超过 128 条时新的历史切换信息会覆盖之前的历史切换信息。

若连接 SP/BS 查询该视图，可以查询到整个 DMDPC 集群的历史切换信息。

当 DM.INI 参数 ENABLE\_MONITOR=1 时有效。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | INSTANCE\_NAME | VARCHAR(128) | 执行切换的实例名 |
| 2 | RAFT\_ID | INTEGER | 所属 RAFT 组序号 |
| 3 | OLD\_MODE | VARCHAR(16) | 切换前服务器模式 |
| 4 | NEW\_MODE | VARCHAR(16) | 切换后服务器模式 |
| 5 | OLD\_STATUS | VARCHAR(16) | 切换前服务器状态 |
| 6 | NEW\_STATUS | VARCHAR(16) | 切换后服务器状态 |
| 7 | OLD\_ROLE | VARCHAR(16) | 切换前角色 |
| 8 | NEW\_ROLE | VARCHAR(16) | 切换后角色 |
| 9 | OLD\_LEADER | VARCHAR(128) | 切换前 LEADER 实例名，若 LEADER 不存在则该值为空 |
| 10 | NEW\_LEADER | VARCHAR(128) | 切换后 LEADER 实例名，若 LEADER 不存在则该值为空 |
| 11 | SWITCH\_TIME | VARCHAR(50) | 切换执行的时间，精确到微秒 |
| 12 | INST\_NUM | INTEGER | RAFT 组内的节点个数，包含 LEARNER 节点 |