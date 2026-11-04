---
title: "监控 DMDSC"
book: "DM8 数据共享集群"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dsc-monitor.html
tags:
  - dameng
  - dm8
  - dsc
---

DMDSC 集群的运行情况可以通过 DMCSSM 监视器（Dameng Cluster Synchronization Services Monitor，DMCSSM）进行查看，也可以查询 DMDSC 相关的动态视图获取更详细的信息。DMCSSM 监视器支持一些控制命令，可以用来启动、关闭 DMDSC 集群，还可以进行手动控制节点故障处理和节点重加入。

## 15.1 DMCSSM 监视器

配置了 DMCSS 的集群中，可配置 DMCSSM 对集群进行统一管理，可配置 0~10 个 DMCSSM。各 DMCSSM 作用一样，相互独立，互不干扰。

### 15.1.1 功能说明

1. 监控集群状态

DMCSS 每秒会发送集群中所有节点的状态信息、当前连接到 DMCSS 的监视器信息以及 DCR 的配置信息到活动的监视器上，监视器提供对应的 show 命令用于查看各类信息。

2. 打开/关闭指定组的自动拉起

DMCSSM 提供 SET AUTO RESTART ON/SET AUTO RESTART OFF 命令，通知 DMCSS 打开或关闭对指定组的自动拉起功能，此功能和 DMCSS 的监控打开或关闭没有关系。

3. 强制 OPEN 指定组

DMCSSM 提供 OPEN FORCE 命令，在启动 ASM 或 DB 组时，如果组中某个节点发生硬件故障等原因导致一直无法启动，可执行此命令通知 DMCSS 将 ASM 组或 DB 组强制 OPEN，不再等待故障节点启动成功。

4. 启动/退出集群

DMCSSM 提供 EP STARTUP/EP STOP 命令，可以通知 DMCSS 启动/退出指定的 ASM 或 DB 组。

5. 集群故障处理

DMCSSM 提供 EP BREAK/EP RECOVER 命令，在主 CSS 的监控功能被关闭的情况下，可以通过执行这些命令手动进行故障处理和故障恢复。另外在某些特殊场景下还可通过 EP HALT 命令强制退出指定节点，具体可参考 15.1.4 命令说明 。

### 15.1.2 配置文件 DMCSSM.INI

DMCSSM 的配置文件名称为 dmcssm.ini，所支持的配置项说明如下。

表15.1 dmcssm.ini配置项

| **配置项** | **配置含义** |
| --- | --- |
| CSSM\_OGUID | 用于和 DMCSS 通信校验使用，和 DMDCR\_CFG.INI 中的 DCR\_OGUID 值保持一致 |
| CSSM\_CSS\_IP | 集群中所有 DMCSS 所在机器的 IP 地址，以及 DMCSS 的监听端口，配置格式为“IP:PORT”的形式，其中 IP 和 PORT 分别对应 DMDCR\_CFG.INI 中 DMCSS 节点的 DCR\_EP\_HOST 和 DCR\_EP\_PORT。   如果使用 IPv6 地址，为了方便区分端口，需要用\[\]封闭 IP 地址。   对于 IPv6，若当前环境存在多块网卡，需要用 % 号指定具体有效的网卡序号或网卡名称；若只有一块网卡或者已配置默认网卡，则可以不指定序号或名称。例如：   CSSM\_CSS\_IP = \[fe80::6aa7:3f02:59b3:bcb4%3\]:52184 |
| CSSM\_LOG\_PATH | 日志文件路径，日志文件命名方式为 “dmcssm\_年月日时分秒.log”，例如“dmcssm\_20160614131123.log”。 如果 DMCSSM.INI 中配置有 CSSM\_LOG\_PATH 路径，则将 CSSM\_LOG\_PATH 作为日志文件路径，如果没有配置，则将 DMCSSM.INI 配置文件所在的路径作为日志文件路径 |
| CSSM\_LOG\_FILE\_SIZE | 单个日志文件大小，取值范围 16~2048，单位为 MB，缺省为 64MB，达到最大值后，会自动生成并切换到新的日志文件中 |
| CSSM\_LOG\_SPACE\_LIMIT | 日志总空间大小，取值 0 或者 256~4096，单位为 MB。缺省为 0，表示没有空间限制。如果达到设定的总空间限制，会自动删除创建时间最早的日志文件 |
| CSSM\_MESSAGE\_CHECK | 是否对 CSSM 通信消息启用通信体校验（只有当消息的发送端和接收端都配置为 1 才启用通信体校验）。0：不启用；1：启用。缺省为 1 |

> **说明**
> 
> 在有日志写入操作时，如果日志路径下没有日志文件，会自动创建一个新的日志文件，如果已经有日志文件，则根据设定的单个日志文件大小（CSSM\_LOG\_FILE\_SIZE）决定继续写入已有的日志文件或者创建新的日志文件写入。  
> 创建新的日志文件时，根据设定的日志总空间大小（CSSM\_LOG\_SPACE\_LIMIT）决定是否删除创建时间最早的日志文件。

### 15.1.3 配置步骤

同一个 DMDSC 集群中，允许最多同时启动 10 个监视器，建议监视器放在独立的第三方机器上，避免由于节点间网络不稳定等原因导致监视器误判节点故障。

下面举例说明监视器的配置步骤，以 [12 DMDSC 搭建](dsc-build.md) 中搭建的 2 节点 DSC 环境为基础，配置对应的监视器，监视器放在第三方机器上，为 windows 操作系统，DMCSSM.INI 配置文件路径为 D:\\cssm，可根据实际情况调整配置环境及路径。

1. 配置 DMCSSM.INI 文件
```
#和DMDCR_CFG.INI中的DCR_OGUID保持一致
CSSM_OGUID = 1071107589 

#配置所有CSS的连接信息，
#和DMDCR_CFG.INI中CSS配置项的DCR_EP_HOST和DCR_EP_PORT保持一致
CSSM_CSS_IP = 192.168.102.107:9836
CSSM_CSS_IP = 192.168.102.110:9837

CSSM_LOG_PATH =D:\cssm\log        #监视器日志文件存放路径
CSSM_LOG_FILE_SIZE = 32            #每个日志文件最大32M
CSSM_LOG_SPACE_LIMIT = 0        #不限定日志文件总占用空间
```
2. 启动 dmcssm 监视器
```
dmcssm.exe INI_PATH=D:\cssm\dmcssm.ini
```

### 15.1.4 命令说明

监视器提供一系列命令，支持集群的状态信息查看以及节点的故障处理，可输入 help 命令，查看命令使用说明。

表15.2 监视器命令

| **命令名称** | **含义** |
| --- | --- |
| help | 显示帮助信息 |
| show \[group\_name\] | 显示指定的组信息，如果没有指定 group\_name，则显示所有组信息 |
| show config | 显示 dmdcr\_cfg.ini 的配置信息 |
| show monitor | 显示当前连接到主 CSS 的所有监视器信息 |
| set group\_name auto restart on | 打开指定组的自动拉起功能（只修改 dmcss 内存值） |
| set group\_name auto restart off | 关闭指定组的自动拉起功能（只修改 dmcss 内存值） |
| open force group\_name | 强制 open 指定的 ASM 或 DB 组 |
| ep startup group\_name | 启动指定的 ASM 或 DB 组 |
| ep stop group\_name | 退出指定的 ASM 或 DB 组 |
| ep halt group\_name.ep\_name | 强制退出指定组中的指定节点 |
| extend node | 联机扩展节点 |
| ep crash group\_name.ep\_name | 手动指定节点故障 |
| check crash over group\_name | 检查指定组故障处理是否真正结束 |
| exit | 退出监视器 |

**命令使用说明：**

1. help

显示帮助信息。

2. show \[group\_name\]

显示指定的组信息，如果没有指定 group\_name，则显示所有组信息。

返回的组信息优先从主 CSS 获取，如果主 CSS 故障或尚未选出，则任选一个从 CSS 返回组信息。

3. show config

显示 DMDCR\_CFG.INI 的配置信息，对于 DB 类型的节点，会比 CSS/ASM 节点多一项 DCR\_EP\_SEQNO 的显示值，如果原本的 ini 文件中没有手动配置，则显示的是自动分配的序列值。

返回的配置信息优先从主 CSS 获取，如果主 CSS 故障或尚未选出，则任选一个从 CSS 返回信息。

4. show monitor

显示当前连接到主 CSS 的所有 CSSM 监视器信息，如果主 CSS 故障或尚未选出，则任选一个从 CSS 显示连接信息。

返回的信息中，第一行为当前执行命令的监视器的连接信息。

5. set group\_name auto restart on

打开指定组的自动拉起功能。

可借助 show css 命令查看每个节点的自动拉起标记，每个 css 只能控制和自己的 DMDCR.INI 中配置的 DMDCR\_SEQNO 相同节点的自动拉起。

6. set group\_name auto restart off

关闭指定组的自动拉起功能。

可借助 show css 命令查看每个节点的自动拉起标记，每个 css 只能控制和自己的 DMDCR.INI 中配置的 DMDCR\_SEQNO 相同节点的自动拉起。

DSCone node 模式下执行该命令无效果，仅会更改 DMCSS 中的自动拉起参数内存值，实际 DSC one node 模式下不会关闭自动拉起功能。

7. open force group\_name

在启动 ASM 或 DB 组时，如果某个节点故障一直无法启动，可借助此命令将 ASM 或 DB 组强制 OPEN。

此命令需要发送到主 CSS 执行，并且主 CSS 的监控需要处于打开状态，如果主 CSS 故障或尚未选出，则命令执行失败。

8. ep startup group\_name

通知 CSS 启动指定的 ASM 或 DB 组，如果 CSS 已经打开了指定组的自动拉起功能，则命令不允许执行，需要等待 CSS 自动检测故障并执行拉起操作。

每个 CSS 只负责拉起和自己的 dmdcr.ini 中配置的 DMDCR\_SEQNO 相同的 ASM 或 DB 节点，因此需要所有 CSS 都处于活动状态，否则只通知当前活动的 CSS 自动拉起相对应的节点。

> **说明**
> 
> 只有在ASM组正常启动到OPEN状态，并且所有活动的ASM节点都处于OPEN状态时，才允许启动DB组，否则执行DB组的启动命令会报错，CSS自动拉起DB组时也需要满足此条件。  
> 在命令执行前，如果CSS对指定组的自动拉起功能是关闭的，在节点拉起成功后，会打开对指定组的自动拉起功能。

9. ep stop group\_name

退出指定的 ASM 或 DB 组，如果主 CSS 故障或尚未选出，则命令执行失败。

> **注意**
> 
> 在退出ASM组时，需要保证DB组已经退出，否则会报错处理。  
> 在命令执行前，如果CSS对指定组的自动拉起功能是打开的，则会先通知CSS关闭对指定组的自动拉起功能，再通知指定组退出，避免命令执行成功后节点再次被自动拉起。  
> DSC one node模式下虽然会通知CSS关闭对指定组的自动拉起功能，但实际执行无效果，仅会更改DMCSS中的自动拉起参数内存值，实际DSC one node模式下不会关闭自动拉起功能。

10. ep halt group\_name.ep\_name

强制退出指定组的指定 EP。适用于下述场景：

场景一 某个 ASM 或 DB 集群节点故障，CSS 的心跳容错时间 DCR\_GRP\_DSKCHK\_CNT 配置值很大，在容错时间内，CSS 不会调整故障节点的 active 标记，一直是 TRUE，CSS 认为故障 EP 仍然处于活动状态，不会自动执行故障处理，并且不允许手动执行故障处理。

另外，执行 EP STARTUP 或 EP STOP 命令时，会误认为故障 EP 仍然处于活动状态，导致执行结果与预期不符。此时可以通过执行 EP HALT 命令，通知 CSS 再次 HALT 故障 EP，确认 EP 已经被 HALT 后，CSS 会及时调整 active 标记为 FALSE，在此之后，对自动/手动故障处理，EP STARTUP/EP STOP 命令都可以正常执行。

场景二 需要强制 HALT 某个正在运行的 ASM 或 DB 节点，也可以通过此命令完成。

11. extend node

DMDSC 集群联机增加节点时使用。

程序会通知所有实例(CSS/ASMSVR/dmserver)更新 dcr 信息。

使用 show 命令能看到新增节点信息，新增 ASMSVR/dmserver 为 ERROR 状态。

12. ep crash group\_name.ep\_name

手动指定节点故障，节点故障后，css 只有在 DCR\_GRP\_DSKCHK\_CNT 配置的时间过后才会判定实例故障，开始故障处理流程。用户如果明确知道实例已经故障，可以收到执行此命令，CSS 可以立即开始故障处理流程。

13. check crash over group\_name

DB 集群环境故障处理后，需要满足一定条件（控制节点重做 REDO 日志产生的数据页修改都已经刷盘完成），才允许故障节点重新加回集群环境。此命令用来显示 DB 集群环境故障处理是否真正结束。

14. exit

退出监视器。

## 15.2 动态视图

DMDSC 集群提供一系列动态视图来查看当前的系统运行信息。部分视图是全局的，任意节点登录查询的结果都是相同的，部分视图仅显示登录节点的信息。

### 15.2.1 DMDSC 通用视图

#### 15.2.1.1 V$DSC\_EP\_INFO

显示实例信息，登录任意节点查询得到的结果一致。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EP\_NAME | VARCHAR(128) | 实例名称 |
| 2 | EP\_SEQNO | INTEGER | DSC 节点序号 |
| 3 | EP\_GUID | BIGINT | EP 唯一标识码 |
| 4 | EP\_TIMESTAMP | BIGINT | EP 时间戳 |
| 5 | EP\_MODE | VARCHAR(32) | EP 模式，CONTROL NODE 或 NORMAL NODE |
| 6 | EP\_STATUS | VARCHAR(32) | EP 状态，OK 或 ERROR |

#### 15.2.1.2 V$DSC\_GBS\_POOL

显示 GBS 控制结构的信息，仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | N\_CTL | INTEGER | GBS 控制块总数 |
| 2 | N\_FREE\_CTL | INTEGER | 空闲的 GBS 控制块数目 |
| 3 | N\_SUB\_POOL | INTEGER | GBS\_POOL 个数 |

#### 15.2.1.3 V$DSC\_GBS\_POOLS\_DETAIL

显示分片的 GBS\_POOL 详细信息，仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | GBS\_POOL 编号 |
| 2 | N\_USED\_CTL | INTEGER | 正在使用的 GBS 控制块数目 |
| 3 | N\_REQUEST | INTEGER | 当已有的 GBS 控制块全部被使用时，系统会临时分配额外的 GBS 控制块，当临时分配的 GBS 控制块尚处于请求阶段时，会被统计至 N\_REQUEST 字段 |
| 4 | N\_FREE\_REQUEST | INTEGER | 当临时分配的 GBS 控制块使用完成后会被放入空闲链表中，N\_FREE\_REQUEST 字段统计的是空闲链表中的临时分配的 GBS 控制块数目 |

#### 15.2.1.4 V$DSC\_GBS\_CTL

显示 GBS 控制块信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | GBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_OWNER | INTEGER | 拥有权限的 EP 数 |
| 11 | N\_REQUEST | INTEGER | 请求授权的 EP 数 |
| 12 | N\_REVOKING | INTEGER | 正在回收权限的 EP 数 |
| 13 | N\_REVOKE\_X\_ONLY | INTEGER | 页的优化次数 |

#### 15.2.1.5 V$DSC\_GBS\_CTL\_DETAIL

显示 GBS 控制块详细信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | GBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_OWNER | INTEGER | 拥有权限的 EP 数 |
| 11 | N\_REQUEST | INTEGER | 请求授权的 EP 数 |
| 12 | N\_REVOKING | INTEGER | 正在回收权限的 EP 数 |
| 13 | TYPE | VARCHAR(32) | 详细信息类型（OWNER/REQUEST/REVOKING） |
| 14 | MODE | INTEGER | 封锁模式，0/1/2/4 分别表示 N\_LATCH/X\_LATCH/S\_LATCH/F\_LATCH。该字段值可能为上述值的组合值，如字段值为 3 表示同时拥有 X\_LATCH 和 S\_LATCH 两种封锁 |
| 15 | EP\_SEQNO | INTEGER | 拥有、请求、或者回收封锁的 EP |
| 16 | REAL\_FLUSH | CHAR | 是否真正执行刷盘请求（Y/N） |
| 17 | N\_REVOKE\_X\_ONLY | INTEGER | 页的优化次数 |

#### 15.2.1.6 V$DSC\_GBS\_CTL\_LRU\_FIRST

显示 GBS 控制块 LRU 链表首页信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | GBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_OWNER | INTEGER | 拥有权限的 EP 数 |
| 11 | N\_REQUEST | INTEGER | 请求授权的 EP 数 |
| 12 | N\_REVOKING | INTEGER | 正在回收权限的 EP 数 |
| 13 | N\_REVOKE\_X\_ONLY | INTEGER | 页的优化次数 |

#### 15.2.1.7 V$DSC\_GBS\_CTL\_LRU\_FIRST\_DETAIL

显示 GBS 控制块 LRU 链表首页详细信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | GBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_OWNER | INTEGER | 拥有权限的 EP 数 |
| 11 | N\_REQUEST | INTEGER | 请求授权的 EP 数 |
| 12 | N\_REVOKING | INTEGER | 正在回收权限的 EP 数 |
| 13 | TYPE | VARCHAR(32) | 详细信息类型（OWNER/REQUEST/REVOKING） |
| 14 | MODE | INTEGER | 封锁模式，0/1/2/4 分别表示 N\_LATCH/X\_LATCH/S\_LATCH/F\_LATCH。该字段值可能为上述值的组合值，如字段值为 3 表示同时拥有 X\_LATCH 和 S\_LATCH 两种封锁 |
| 15 | EP\_SEQNO | INTEGER | 拥有、请求、或者回收封锁的 EP |
| 16 | REAL\_FLUSH | CHAR | 是否真正执行刷盘请求（Y/N） |
| 17 | N\_REVOKE\_X\_ONLY | INTEGER | 页的优化次数 |

#### 15.2.1.8 V$DSC\_GBS\_CTL\_LRU\_LAST

显示 GBS 控制块 LRU 链表尾页信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | GBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_OWNER | INTEGER | 拥有权限的 EP 数 |
| 11 | N\_REQUEST | INTEGER | 请求授权的 EP 数 |
| 12 | N\_REVOKING | INTEGER | 正在回收权限的 EP 数 |
| 13 | N\_REVOKE\_X\_ONLY | INTEGER | 页的优化次数 |

#### 15.2.1.9 V$DSC\_GBS\_CTL\_LRU\_LAST\_DETAIL

显示 GBS 控制块 LRU 链表尾页详细信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | GBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_OWNER | INTEGER | 拥有权限的 EP 数 |
| 11 | N\_REQUEST | INTEGER | 请求授权的 EP 数 |
| 12 | N\_REVOKING | INTEGER | 正在回收权限的 EP 数 |
| 13 | TYPE | VARCHAR(32) | 详细信息类型（OWNER/REQUEST/REVOKING） |
| 14 | MODE | INTEGER | 封锁模式，0/1/2/4 分别表示 N\_LATCH/X\_LATCH/S\_LATCH/F\_LATCH。该字段值可能为上述值的组合值，如字段值为 3 表示同时拥有 X\_LATCH 和 S\_LATCH 两种封锁 |
| 15 | EP\_SEQNO | INTEGER | 拥有、请求、或者回收封锁的 EP |
| 16 | REAL\_FLUSH | CHAR | 是否真正执行刷盘请求（Y/N） |
| 17 | N\_REVOKE\_X\_ONLY | INTEGER | 页的优化次数 |

#### 15.2.1.10 V$DSC\_GBS\_REQUEST\_CTL

显示等待 GBS 控制块的请求信息。当已有的 GBS 控制块全部被使用时，系统会临时分配额外的 GBS 控制块，当临时分配的 GBS 控制块尚处于请求阶段时，会被记录至当前视图中。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | GBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | MODE | INTEGER | 封锁模式，0/1/2/4 分别表示 N\_LATCH/X\_LATCH/S\_LATCH/F\_LATCH。该字段值可能为上述值的组合值，如字段值为 3 表示同时拥有 X\_LATCH 和 S\_LATCH 两种封锁 |
| 6 | EP\_SEQNO | INTEGER | 请求封锁的 EP |
| 7 | FREQ\_CONFLICT | INTEGER | 是否为高频冲突数据页 |

#### 15.2.1.11 V$DSC\_LBS\_POOL

显示 LBS 控制结构的信息，仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | N\_CTL | INTEGER | LBS 控制块总数 |
| 2 | N\_FREE\_CTL | INTEGER | 空闲的 LBS 控制块数目 |
| 3 | N\_SUB\_POOL | INTEGER | LBS\_POOL 个数 |
| 4 | N\_FAST\_REQUEST | BIGINT | LBS 请求本地直接命中的次数。该项已废弃，恒为 0 |
| 5 | N\_GBS\_REQUEST | INTEGER | LBS 请求发送给 GBS 节点的次数。该项已废弃，恒为 0 |
| 6 | N\_PAGE\_CREATE\_REQUEST | INTEGER | 创建数据页请求次数。该项已废弃，恒为 0 |
| 7 | TOTAL\_REQUEST | BIGINT | 总的 LBS 请求次数。该项已废弃，恒为 0 |

#### 15.2.1.12 V$DSC\_LBS\_POOLS\_DETAIL

显示分片的 LBS\_POOL 详细信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | LBS\_POOL 编号 |
| 2 | N\_USED\_CTL | INTEGER | 正在使用的 LBS 控制块数目 |
| 3 | N\_REQUEST\_SPACE | INTEGER | 当已有的 LBS 控制块全部被使用时，系统会临时分配额外的 LBS 控制块，当临时分配的 LBS 控制块尚处于请求阶段时，会被统计至 N\_REQUEST\_SPACE 字段 |
| 4 | N\_FREE\_REQUEST | INTEGER | 当临时分配的 LBS 控制块使用完成后会被放入空闲链表中，N\_FREE\_REQUEST 字段统计的是空闲链表中的临时分配的 LBS 控制块数目 |
| 5 | N\_FAST\_REQUEST | INTEGER | LBS 请求本地直接命中的次数。该项已废弃，恒为 0 |
| 6 | N\_GBS\_REQUEST | INTEGER | LBS 请求发送给 GBS 节点的次数。该项已废弃，恒为 0 |
| 7 | N\_PAGE\_CREATE\_REQUEST | INTEGER | 创建数据页请求次数。该项已废弃，恒为 0 |
| 8 | TOTAL\_REQUEST | INTEGER | 总的 LBS 请求次数。该项已废弃，恒为 0 |

#### 15.2.1.13 V$DSC\_LBS\_CTL\_LRU\_FIRST

显示 LBS 的 LRU\_FIRST 控制块信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | LBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_FIXED | INTEGER | 引用计数 |
| 11 | MODE | INTEGER | 获得 GBS 授权的封锁模式 |
| 12 | PHY\_LSN | BIGINT | 数据页上的最新 LSN 值 |
| 13 | N\_REQUEST | INTEGER | 请求获得授权的工作线程数 |
| 14 | N\_REVOKE\_X\_ONLY | INTEGER | 页的优化次数 |

#### 15.2.1.14 V$DSC\_LBS\_CTL\_LRU\_LAST

显示 LBS 的 LRU\_LAST 控制块信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | LBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_FIXED | INTEGER | 引用计数 |
| 11 | MODE | INTEGER | 获得 GBS 授权的封锁模式 |
| 12 | PHY\_LSN | BIGINT | 数据页上的最新 LSN 值 |
| 13 | N\_REQUEST | INTEGER | 请求获得授权的工作线程数 |

#### 15.2.1.15 V$DSC\_LBS\_CTL\_DETAIL

显示 LBS 控制块详细信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | LBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_FIXED | INTEGER | 引用计数 |
| 11 | MODE | INTEGER | 获得 GBS 授权的封锁模式 |
| 12 | PHY\_LSN | BIGINT | 数据页上的最新 LSN 值 |
| 13 | N\_REQUEST | INTEGER | 请求获得授权的工作线程数 |
| 14 | REQUEST\_MODE | INTEGER | 请求的封锁模式 |
| 15 | REVOKE\_LSN | BIGINT | 回收权限时，GBS 上的最新 LSN 值 |
| 16 | N\_REMOTE\_READ | INTEGER | 数据页 REMOTE READ 的次数，数值越大，说明该数据页在节点间冲突越高 |
| 17 | TOTAL\_REQUEST | INTEGER | 数据页的总访问次数 |

#### 15.2.1.16 V$DSC\_LBS\_CTL\_LRU\_FIRST\_DETAIL

显示 LBS 的 LRU\_FIRST 控制块详细信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | LBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_FIXED | INTEGER | 引用计数 |
| 11 | MODE | INTEGER | 获得 GBS 授权的封锁模式 |
| 12 | PHY\_LSN | BIGINT | 数据页上的最新 LSN 值 |
| 13 | N\_REQUEST | INTEGER | 请求获得授权的工作线程数 |
| 14 | REQUEST\_MODE | INTEGER | 请求的封锁模式 |
| 15 | REVOKE\_LSN | BIGINT | 回收权限时，GBS 上的最新 LSN 值 |

#### 15.2.1.17 V$DSC\_LBS\_CTL\_LRU\_LAST\_DETAIL

显示 LBS 的 LRU\_LAST 控制块详细信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | LBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_FIXED | INTEGER | 引用计数 |
| 11 | MODE | INTEGER | 获得 GBS 授权的封锁模式 |
| 12 | PHY\_LSN | BIGINT | 数据页上的最新 LSN 值 |
| 13 | N\_REQUEST | INTEGER | 请求获得授权的工作线程数 |
| 14 | REQUEST\_MODE | INTEGER | 请求的封锁模式 |
| 15 | REVOKE\_LSN | BIGINT | 回收权限时，GBS 上的最新 LSN 值 |

#### 15.2.1.18 V$DSC\_GTV\_SYS

显示 GTV 控制结构的信息，仅登录集群环境控制节点才能获取数据，登录其他节点返回数据无效。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | T\_INFO\_NUM | INTEGER | 系统已提交、未 PURGE 事务所修改的表对象个数 |
| 2 | NEXT\_TRXID | BIGINT | 下一个事务 ID |
| 3 | MAX\_PURGABLE\_TRIXID | BIGINT | 最大可 PURGE 的事务 ID |
| 4 | UNDO\_TRIXID | BIGINT | 回滚段中，正在被访问的最小事务 ID |
| 5 | UNDO\_CNT | INTEGER | UNDO\_TRXID 被设置的次数 |

#### 15.2.1.19 V$DSC\_LBS\_CTL

显示 LBS 控制块信息。仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | POOL\_ID | INTEGER | LBS\_POOL 编号 |
| 2 | TS\_ID | INTEGER | 表空间号 |
| 3 | FILE\_ID | INTEGER | 文件号或-1。-1 表示全局表空间封锁的 LBS 页 |
| 4 | PAGE\_NO | INTEGER | 页号或表空间大小。当 FILE\_ID=-1 时，此处 PAGE\_NO 表示表空间大小 |
| 5 | ACCESS\_MAP | INTEGER | 曾经访问此数据页的 EP |
| 6 | FRESH\_EP | INTEGER | 最新数据所在 EP。-1 表示此数据页尚未被修改 |
| 7 | FRESH\_LSN | BIGINT | 最新修改对应的 LSN 值 |
| 8 | N\_REPLACED | INTEGER | 控制块被替换次数 |
| 9 | N\_REVOKED | INTEGER | 权限被回收次数 |
| 10 | N\_FIXED | INTEGER | 引用计数 |
| 11 | MODE | INTEGER | 获得 GBS 授权的封锁模式 |
| 12 | PHY\_LSN | BIGINT | 数据页上的最新 LSN 值 |
| 13 | N\_REQUEST | INTEGER | 请求获得授权的工作线程数 |
| 14 | N\_REMOTE\_READ | INTEGER | 数据页 REMOTE READ 的次数，数值越大，说明该数据页在节点间冲突越高 |
| 15 | TOTAL\_REQUEST | INTEGER | 数据页总的访问次数 |
| 16 | N\_REVOKE\_X\_ONLY | INTEGER | 页的优化次数 |
| 17 | REVOKE\_DELAY | INTEGER | BS\_CTL 延迟权限回收的次数 |

#### 15.2.1.20 V$DSC\_LOCK

显示全局活动的事务锁信息，登录任意节点查询得到的结果一致。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EP\_SEQNO | INTEGER | 拥有该锁的节点号 |
| 2 | ADDR | BIGINT | 全局封锁对象的地址 |
| 3 | TRX\_ID | BIGINT | 所属事务 ID |
| 4 | LTYPE | VARCHAR(10) | 锁类型：TID 锁、对象锁 |
| 5 | LMODE | CHAR(2) | 锁模式：S 锁、X 锁、IX 锁、IS 锁 |
| 6 | BLOCKED | INTEGER | 是否阻塞 |
| 7 | TABLE\_ID | INTEGER | 对应表锁、字典对象 ID |
| 8 | ROW\_IDX | BIGINT | 被封锁事务 ID |
| 9 | IGN\_FLAG | INTEGER | 锁对象的 IGNORABLE 标记，INI 参数 LOCK\_DICT\_OPT 开启时有效。   取值 0：表示锁正在使用中，IGN\_FLAG 最低位置为 0；   取值 1：表示事务 TRX1 已经提交，但是锁资源未释放，TRX1 重新封锁时可以直接使用，此时 IGN\_FLAG 最低位置为 1；   取值 2：为 0+2 的组合值。当锁正被使用时，另一事务要封锁同一对象，将当前正被使用的锁的 IGN\_FLAG 次低位置为 1；   取值 3：为 1+2 的组合值。当 TRX1 已提交，但锁未释放时，另一事务 TRX2 要封锁同一对象，此时 TRX2 可以忽略此 IGN\_FLAG=1 的锁，但是要将此锁的 IGN\_FLAG 次低位置为 1 |

#### 15.2.1.21 V$DSC\_TRX

显示所有活动事务的信息。通过该视图可以查看所有系统中所有的事务以及相关信息，如锁信息等，登录任意节点查询得到的结果一致。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EP\_SEQNO | INTEGER | 事务所在节点号 |
| 2 | ID | BIGINT | 当前活动事务的 ID 号 |
| 3 | NEXTID | BIGINT | 下一个事务 ID 号 |
| 4 | MIN\_ACTIVE\_ID | BIGINT | 所有活动事务 ID 号最小者 |
| 5 | STATUS | VARCHAR(20) | 当前事务的状态 |
| 6 | ISOLATION | INTEGER | 事务的隔离级别 0：读未提交 1：读提交 2：可重复读 3：串行化 |
| 7 | READ\_ONLY | CHAR(1) | 是否为只读事务（Y/N） |
| 8 | SESS\_ID | BIGINT | 当前事务所在的会话 ID |
| 9 | SESS\_SEQ | INTEGER | 会话序列号，用来唯一标识会话 |
| 10 | INS\_CNT | INTEGER | 插入回滚记录个数 |
| 11 | DEL\_CNT | INTEGER | 删除回滚记录个数 |
| 12 | UPD\_CNT | INTEGER | 更新回滚记录个数 |
| 13 | UPD\_INS\_CNT | INTEGER | 更新插入回滚记录个数 |
| 14 | UREC\_SEQNO | INTEGER | 当前 Undo 记录的递增序列号 |
| 15 | WAITING | BIGINT | 事务等待的锁 |
| 16 | THRD\_ID | INTEGER | 当前事务对应的线程 ID |

#### 15.2.1.22 V$DSC\_TRXWAIT

显示事务等待信息，登录任意节点查询得到的结果一致。当 DMDSC 系统的活动节点数超过 1 个时，使用 V$DSC\_TRXWAIT 查询事务等待信息，当为单节点系统或 DMDSC 系统仅剩一个活动节点时，应查询 V$TRXWAIT。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EP\_SEQNO | INTEGER | 事务所在节点号 |
| 2 | TRX\_ID | BIGINT | 事务 ID |
| 3 | WAIT\_FOR\_ID | BIGINT | 所等待的事务 ID |
| 4 | WAIT\_SEQNO | TINYINT | 等待的事务序列号 |
| 5 | WAIT\_TIME | INTEGER | 当前已等待时间，单位毫秒 |
| 6 | TRX\_OBJ | BIGINT | 事务对象 |
| 7 | WAIT\_TRX\_OBJ | BIGINT | 等待事务对象 |

#### 15.2.1.23 V$DCR\_INFO

查看 DCR 配置的全局信息，登录任意节点查询得到的结果一致。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | VERSION | INTEGER | DCR 版本号 |
| 2 | N\_GROUP | INTEGER | DCR 配置的组个数 |
| 3 | VTD\_PATH | VARCHAR(256) | VOTE 磁盘路径 |
| 4 | UDP\_FLAG | INTEGER | 是否使用 UDP 心跳机制，已无效 |
| 5 | UDP\_OGUID | BIGINT | DCR 磁盘 GUID 标识，用于校验 DCR 磁盘 |
| 6 | DCR\_PATH | VARCHAR(256) | DCR 磁盘路径 |

#### 15.2.1.24 V$DCR\_GROUP

查看 DCR 配置的组信息，登录任意节点查询得到的结果一致。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | GROUP\_TYPE | VARCHAR(32) | 组类型，CSS/ASM/DB |
| 2 | GROUP\_NAME | VARCHAR(128) | 组名称 |
| 3 | N\_EP | INTEGER | 组中配置的 EP 个数 |
| 4 | DSKCHK\_CNT | INTEGER | 磁盘心跳超时时间。单位秒 |
| 5 | NETCHK\_TIME | INTEGER | 预留参数，暂无意义，显示为 0 |

#### 15.2.1.25 V$DCR\_EP

查看 DCR 配置的节点信息，登录任意节点查询得到的结果一致。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | GROUP\_NAME | VARCHAR(128) | 节点所属的组名 |
| 2 | EP\_NAME | VARCHAR(128) | 节点名称 |
| 3 | EP\_SEQNO | INTEGER | 节点的组内序号： 对 CSS/ASM 组的节点，是自动分配的序号，对 DB 组的节点，如果没有配置，也是自动分配的序号，否则是实际的配置序号。 |
| 4 | EP\_HOST | VARCHAR(128) | 节点的 IP 地址，对 CSS/ASM 组的节点有效，表示登录节点的 IP 地址 |
| 5 | EP\_PORT | INTEGER | 节点的 TCP 监听端口，对应登录节点对应实例的端口号 |
| 6 | UDP\_PORT | INTEGER | 节点的 UDP 监听端口，已无效 |
| 7 | SHM\_KEY | INTEGER | 共享内存标识，初始化共享内存的标识符，对 ASM 组的节点有效 |
| 8 | SHM\_SIZE | INTEGER | 共享内存大小，单位 MB，初始化共享内存大小，对 ASM 组的节点有效 |
| 9 | ASM\_LOAD\_PATH | VARCHAR(256) | ASM 磁盘扫描路径，对 ASM 组的节点有效 |

#### 15.2.1.26 V$DMDCR\_INI

查看当前节点 dmdcr.ini 文件中的参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | NAME | VARCHAR(128) | 参数名称 |
| 2 | VALUE | VARCHAR(1024) | 参数的值 |

#### 15.2.1.27 V$DSC\_REQUEST\_STATISTIC

统计 DSC 环境内 TYPE 类型请求时间，仅显示登录节点的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TYPE | VARCHAR(64) | 请求类型，可能取值：logic read, physical read, remote read, remote page send, remote read failed, remote read processing,remote read transmission, remote rlog flush, remote rlog flush wait, physical write, lbs request fast, lbs x latch owned, lbs s latch owned, lbs f latch owned, lbs x latch waited, lbs s latch waited, lbs f latch waited, lbs x latch waited by revoke, lbs s latch waited by revoke, lbs f latch waited by revoke, lbs sent x latch request to local gbs, lbs sent s latch request to local gbs, lbs sent f latch request to local gbs, lbs sent x latch request to remote gbs, lbs sent s latch request to remote gbs, lbs sent f latch request to remote gbs, lbs request rollback, gbs synchronous revoke conflicts, gbs synchronous revoke roll conflicts, gbs asynchronous revoke conflicts, gbs asynchronous revoke roll conflicts, lls lock table, lls lock tid, lls lock release, lls dict remove, ltv view get |
| 2 | TOTAL\_REQUEST\_COUNT | BIGINT | 总请求次数 |
| 3 | MAX\_REQUEST\_TIME | INTEGER | 最大请求时间，单位为微秒 |
| 4 | MIN\_REQUEST\_TIME | INTEGER | 最小请求时间，单位为微秒 |
| 5 | AVERAGE\_REQUEST\_TIME | INTEGER | 平均请求时间，单位为微秒 |
| 6 | TOTAL\_REQUEST\_TIME | BIGINT | 总的请求时间，单位为微秒 |

#### 15.2.1.28 V$DSC\_CRASH\_OVER\_INFO

显示 DSC 环境各节点数据页最小 first\_modified\_lsn，以及故障节点 file\_lsn。

如果活动节点 buffer 中不存在更新页则 min\_first\_modified\_lsn 为 NULL；节点故障后，只有在所有 OK 节点 min\_first\_modified\_lsn 都大于或等于故障节点 file\_lsn 之后，才允许故障节点重加入；满足所有 OK 节点 min\_first\_modified\_lsn 都大于 crash\_lsn 之后，crash\_lsn 会清零。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EP\_SEQNO | INTEGER | DSC 节点号 |
| 2 | OK\_FLAG | INTEGER | 节点是否 OK。1 是，表示 OK；0 否，表示故障 |
| 3 | MIN\_FIRST\_MODIFIED\_LSN | BIGINT | 最小 first\_modified\_lsn |
| 4 | CRASH\_LSN | BIGINT | 内存中记录的故障节点 file\_lsn |

#### 15.2.1.29 V$DSC\_GLS\_SYS

显示 DSC 环境下的系统全局封锁相关信息。若发起一次封锁请求时，DSC 环境下全局封锁的缓存系统中与其冲突的封锁数目大于 1024，认为发生了一次死锁。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TOTAL\_SUCCESS | INTEGER | 封锁成功的次数 |
| 2 | TOTAL\_WAIT | INTEGER | 封锁冲突等待的次数 |
| 3 | TOTAL\_DEADLOCK | INTEGER | 发生死锁的次数 |
| 4 | HLCK\_SEQ | BIGINT | DSC 集群全局封锁的缓存系统当前使用的序列号 |

#### 15.2.1.30 V$DSCIDS

显示 DMDSC 中所有节点活动事务相关的信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | EPSEQ | INTEGER | DMDSC 节点序号 |
| 2 | MIN\_ACTIVE\_ID | BIGINT | 最小活动事务号 |
| 3 | NEXT\_ID | BIGINT | 即将产生的事务号 |
| 4 | N\_ACTIVE | INTEGER | 活动事务个数 |
| 5 | MAX\_CMT\_LSN | BIGINT | 事务提交生成的最大 LSN |
| 6 | MIN\_CMT\_TID | BIGINT | 已提交、且日志已刷盘的事务号 |
| 7 | MIN\_LAST\_CMT\_LSN | BIGINT | 最小活动事务上一次提交 LSN |
| 8 | NOTIFY\_VERSION | BIGINT | 活动事务广播信息版本号 |

#### 15.2.1.31 V$DSC\_TRX\_VIEW

显示 DSC 环境下活动事务视图信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TRXID | BIGINT | 当前活动事务的 ID 号 |
| 2 | NEXT\_ID | BIGINT | 下一个事务 ID 号，大于等于 next\_id 的事务不可见 |
| 3 | MIN\_ACTIVE\_ID | BIGINT | 所有活动事务最小 ID，小于 min\_active\_id 的事务不可见 |
| 4 | EGTS\_ENO | BIGINT | 刷新视图添加 snap 任务时的 egts 执行号 |
| 5 | TEMP\_ENO | BIGINT | 获取最小事务号时代替 trx 登记缓存事务提交计数的执行号 |
| 6 | TEMP\_CMTSEQ | BIGINT | 获取最小事务号时代替 trx 登记的缓存事务提交计数 |
| 7 | N\_LONG | INTEGER | 长事务数目 |
| 8 | LONG\_TIDS | CLOB | 长事务事务 ID 数组 |
| 9 | N\_PE | INTEGER | 数据页损坏事务信息数目 |
| 10 | PE\_TIDS | CLOB | 数据页损坏事务信息数组 |
| 11 | MVCC\_PAGE\_OPT | INTEGER | 数据页可见性判断优化标记 |
| 12 | LAST\_CMT\_LSN | BIGINT | 上次事务提交产生的 LSN |
| 13 | TRX\_START\_LSN | BIGINT | 第一次分配回滚页时的 LSN |
| 14 | MIN\_LAST\_CMT\_LSN | BIGINT | 可见视图里事务号最小事务的 last\_cmt\_lsn |
| 15 | REMOTE\_NEXT\_ID | VARCHAR(322) | DSC 集群其它节点的下一个事务 ID 号 |
| 16 | REMOTE\_MIN\_ID | VARCHAR(322) | DSC 集群其它节点的所有活动事务最小 ID |
| 17 | MAX\_CMT\_LSN | VARCHAR(322) | DSC 集群其它节点的最新已提交事务 LSN |
| 18 | MIN\_CMT\_TID | VARCHAR(322) | DSC 集群其它节点的最小已提交事务 ID |
| 19 | N\_INHASH\_IDS | INTEGER | 活动事务 ID 数组已使用数目 |
| 20 | INHASH\_IDS | CLOB | 活动事务 ID 数组 |

### 15.2.2 DMASM 通用视图

#### 15.2.2.1 V$ASMATTR

如果使用有 ASM 文件系统，可通过此视图查看 ASM 文件系统相关属性，登录任意节点查询得到的结果一致。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | AU\_SIZE | INTEGER | 单个 AU 大小，单位字节。在镜像环境中，该值为 NULL |
| 2 | EXTENT\_SIZE | INTEGER | 一个簇包含的 AU 个数 |
| 3 | LOCAL\_CODE | VARCHAR(64) | 当前所连接的 ASMSERVER 的编码格式 |
| 4 | LOCAL\_LANG | VARCHAR(64) | 当前所连接的 ASMSERVER 使用的语言： CN：中文 EN：英文 |
| 5 | USE\_SHM | VARCHAR(8) | 是否使用共享内存，TRUE/FALSE |
| 6 | EXTENT\_ARR\_SIZE | INTEGER | 共享内存能存放的 extent 个数，可以通过修改 DCR\_EP\_SHM\_SIZE 来控制，EXTENT\_ARR\_SIZE 等于 FREE\_EXTENTS\_SIZE 与 LRU\_EXTENTS\_SIZE 的和 |
| 7 | AUTO\_RBL\_TIME | INTEGER | 镜像专用。INTEGER ASMSERVER 自动重平衡间隔，单位为 s。非镜像环境下无意义 |
| 8 | FREE\_EXTENTS\_SIZE | INTEGER | 共享内存中的空闲簇个数 |
| 9 | LRU\_EXTENTS\_SIZE | INTEGER | 共享内存中的已使用的簇个数 |

#### 15.2.2.2 V$ASMGROUP

如果使用有 ASM 文件系统，可通过此视图查看 ASM 磁盘组信息，登录任意节点查询得到的结果一致。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | GROUP\_ID | INTEGER | 磁盘组 ID |
| 2 | GROUP\_NAME | VARCHAR(128) | 磁盘组名称 |
| 3 | N\_DISK | INTEGER | 磁盘组中包含的磁盘个数 |
| 4 | AU\_SIZE | INTEGER | 单个 AU 大小，单位为字节 |
| 5 | EXTENT\_SIZE(AU) | INTEGER | 一个簇包含的 AU 个数 |
| 6 | TOTAL\_SIZE | INTEGER | 磁盘组总大小，单位为 AU 个数 |
| 7 | FREE\_SIZE | INTEGER | 磁盘组空闲大小，单位为 AU 个数 |
| 8 | TOTAL\_FILE\_NUM | INTEGER | 磁盘组中总的文件个数，包括文件和目录 |
| 9 | TYPE | VARCHAR(16) | 镜像专用。磁盘组副本数：EXTERNAL 单副本；NORMAL 两副本；HIGH 三副本；UNDEFINED：未知。非镜像环境下为 EXTERNAL |
| 10 | REDO\_SIZE(MB) | INTEGER | 镜像专用。磁盘组日志文件大小，单位 MB。非镜像环境下为 1 |
| 11 | RBL\_STAT | INTEGER | 镜像专用。磁盘组重平衡状态。DISABLE：未启用；ENABLE 已启用。非镜像环境下为 DISABLE |
| 12 | RBL\_PWR | VARCHAR(8) | 镜像专用。磁盘组重平衡并行度。非镜像环境下为 0 |
| 13 | AU\_SIZE\_MB | INTEGER | 单个 AU 大小，单位为 MB |
| 14 | TOTAL\_MB | INTEGER | 磁盘组总大小，单位为 MB |
| 15 | FREE\_MB | INTEGER | 磁盘组空闲大小，单位为 MB |

#### 15.2.2.3 V$ASMDISK

如果使用有 ASM 文件系统，可通过此视图查看所有的 ASM 磁盘信息，登录任意节点查询得到的结果一致。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | GROUP\_ID | INTEGER | 所在的磁盘组 ID， 如果是未使用的磁盘，则值为-1 |
| 2 | DISK\_ID | INTEGER | 磁盘 ID， 如果是未使用的磁盘，则值为-1 |
| 3 | DISK\_NAME | VARCHAR(128) | 磁盘名称 |
| 4 | DISK\_PATH | VARCHAR(256) | 磁盘路径 |
| 5 | SIZE | INTEGER | 磁盘大小，单位为 MB |
| 6 | FREE\_AUNO | INTEGER | 磁盘最大 AU 号 |
| 7 | CREATE\_TIME | VARCHAR(64) | 磁盘创建时间 |
| 8 | MODIFY\_TIME | VARCHAR(64) | 磁盘最近一次修改时间 |
| 9 | FAILGROUP\_NAME | VARCHAR(128) | 镜像专用。故障磁盘组组名 |
| 10 | FREE\_MB | INTEGER | 镜像专用。磁盘剩余空间。非镜像环境下为-1 |
| 11 | STATUS | VARCHAR(16) | 镜像专用。磁盘状态。非镜像环境下为 NORMAL。镜像状态取值包括：NORMAL：正常；DELETED：已删除；FAIL：故障；OFFLINE：离线；RECONNECT：重连中。   若未使用磁盘，取值为 NULL |
| 12 | VERSION | INTEGER | 非镜像专用。磁盘版本号。镜像环境下为 0 |
| 13 | IS\_DESTROYED | INTEGER | 磁盘物理信息是否损坏。0 表示未损坏，1 表示损坏。每隔 10min 检测一次磁盘 |

#### 15.2.2.4 V$ASMFILE

如果使用有 ASM 文件系统，可通过此视图查看所有的 ASM 文件信息，登录任意节点查询得到的结果一致。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | FILE\_ID | BIGINT | 文件 ID |
| 2 | TYPE | VARCHAR(32) | 类型，目录或文件 |
| 3 | PATH | VARCHAR(256) | 文件完整路径 |
| 4 | SIZE\_BYTES | BIGINT | 文件实际大小，单位为字节， 目录类型的文件不占用空间，值为 0 |
| 5 | SIZE\_TOTAL | BIGINT | 文件占用总空间大小，单位为字节， 目录类型的文件不占用空间，值为 0 |
| 6 | CREATE\_TIME | VARCHAR(64) | 文件创建时间 |
| 7 | MODIFY\_TIME | VARCHAR(64) | 文件修改时间 |
| 8 | GROUP\_ID | INTEGER | 所在磁盘组 ID |
| 9 | DISK\_ID | INTEGER | inode 项所在磁盘 ID |
| 10 | DISK\_AUNO | INTEGER | inode 项所在磁盘 AU 编号 |
| 11 | AU\_OFFSET | INTEGER | inode 项在 AU 内的偏移 |
| 12 | REDUNDANCY | VARCHAR(6) | 镜像专用。文件副本数。非镜像环境下为 UNPROT |
| 13 | STRIPED | VARCHAR(6) | 镜像专用。文件条带化粒度。字段值为 COARSE 时表示条带化粒度为 0，即粗粒度条带化。非镜像环境下为 NONE |
| 14 | REDUNDANCY\_LOWERED | VARCHAR(2) | 标记文件是否存在缺失副本，取值 Y/N |

#### 15.2.2.5 V$ASM\_MAL\_SYS

ASVRMAL 系统信息视图。仅 DMDSC 环境可使用。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MAL\_CHECK\_INTERVAL | INTEGER | 链路检测间隔 |
| 2 | MAL\_CONN\_FAIL\_INTERVAL | INTEGER | 认定链路断开的时间间隔 |
| 3 | MAL\_CHECK\_TIMEOUT | INTEGER | 单个实例的 MAL 网络最大延迟时间，表示不进行 MAL 网络延迟时间检测。需要和 MAL\_CHECK\_IP 配合使用。仅当 MAL\_CHECK\_INTERVAL 不为 0 时有效。单位毫秒（ms），取值范围 0~65535，缺省为 0 |
| 4 | MAL\_CHECK\_IP | VARCHAR(128) | 第三方确认机器的 IP，用于检测各个实例的 MAL 网络延迟时间。需要和 MAL\_CHECK\_TIMEOUT 配合使用 |
| 5 | MAL\_LOGIN\_TIMEOUT | INTEGER | MPP/DBLINK 等实例间登录时的超时检测间隔 3~1800，单位秒，缺省为 15 |
| 6 | MAL\_BUF\_SIZE | INTEGER | 单个 MAL 缓存大小限制，单位 MB。当 MAL 的缓存邮件超过此大小，会将邮件存储到文件中。取值范围 0~500000，缺省为 100，配置为 0 表示无限制 |
| 7 | MAL\_SYS\_BUF\_SIZE | INTEGER | MAL 系统总内存大小限制，单位 MB。取值范围 0~500000，缺省为 0，表示无限制 |
| 8 | MAL\_VPOOL\_SIZE | INTEGER | MAL 配置的总的 POOL 大小，单位 MB。取值范围 1~500000，缺省为 128 |
| 9 | MAL\_MESSAGE\_CHECK | INTEGER | 是否对 MAL 通信消息启用消息体校验（只有当消息的发送端和接收端都配置为 1 才启用通信体校验）。0：不启用；1：启用。缺省为 1 |
| 10 | MAL\_COMPRESS\_LEVEL | INTEGER | 邮件压缩级别 |
| 11 | MAL\_USE\_RDMA | INTEGER | Linux 环境下，MAL 是否使用 RDMA 通讯方式。0：否；1：是。缺省为 0 |

#### 15.2.2.6 V$ASM\_MAL\_INI

ASVRMAL 参数信息。仅 DMDSC 环境可使用。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MAL\_NAME | VARCHAR (128) | MAL 名称 |
| 2 | MAL\_INST\_NAME | VARCHAR (256) | 实例名称 |
| 3 | MAL\_HOST | VARCHAR (256) | IP 地址 |
| 4 | MAL\_PORT | INTEGER | 端口号 |
| 5 | MAL\_INST\_HOST | VARCHAR (256) | 对应实例 IP 地址 |
| 6 | MAL\_INST\_PORT | INTEGER | 对应实例的端口号 |
| 7 | MAL\_LINK\_MAGIC | INTEGER | MAL 链路网段标识 |

### 15.2.3 DMASM 镜像专用视图

本节中 V$ASMPARTNER、V$ASM\_OPERATION、V$ASM\_REBALANCE\_HISTORY 和 V$ASM\_FAIL\_AU 为镜像环境专用视图。

#### 15.2.3.1 V$ASMPARTNER

如果使用有 DMASM 镜像，可通过此视图查看所有的 ASM 磁盘伙伴关系信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | GROUP\_ID | INTEGER | 磁盘组 ID |
| 2 | DISK\_ID | INTEGER | 磁盘 ID |
| 3 | PARTNER\_ID | INTEGER | 伙伴磁盘 ID |
| 4 | PARTNER\_FAILGROUP | VARCHAR(128) | 所属故障组名 |

#### 15.2.3.2 V$ASM\_OPERATION

如果使用有 DMASM 镜像，可通过此视图查看系统中重平衡或减少副本恢复进度信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | GROUP\_ID | INTEGER | 磁盘组 ID |
| 2 | DISK\_ID | INTEGER | 磁盘 ID |
| 3 | OPERATION | VARCHAR(16) | 操作类型 l REBALANCE(重平衡)\| REPAIR (缺失副本修复) |
| 4 | STATE | VARCHAR(5) | 操作状态 l RUN（正在运行） l WAIT（等待运行） l ERRS（发生错误停止） |
| 5 | POWER | INTEGER | 重平衡并行度 |
| 6 | SOFAR | INTEGER | 已经迁移 AU 数 |
| 7 | EST\_WORK | INTEGER | 预估需要迁移 AU 总数 |
| 8 | EST\_RATE | INTEGER | 预估每分钟迁移 AU 数 |
| 9 | EST\_MINUTES | INTEGER | 预估操作完成剩余时间（分钟） |
| 10 | BEGIN\_TIME | TIMESTAMP | 操作开始时间 |
| 11 | END\_TIME | TIMESTAMP | 操作结束时间（发生错误停止运行时间） |
| 12 | PROGRESS | VARCHAR(8) | 操作进度（百分比） |
| 13 | ERR\_CODE | INTEGER | 操作错误码 |

#### 15.2.3.3 V$ASM\_REBALANCE\_HISTORY

DMASM 镜像环境中，查看 AU 重平衡历史信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | GROUP\_ID | INTEGER | 磁盘组 ID |
| 2 | SRC\_DISK\_ID | INTEGER | 源磁盘 ID |
| 3 | SRC\_AUNO | INTEGER | 源 AU 号 |
| 4 | DST\_DISK\_ID | INTEGER | 目的磁盘 ID |
| 5 | DST\_AUNO | INTEGER | 目的 AU 号 |

#### 15.2.3.4 V$ASM\_FAIL\_AU

DMASM 镜像环境中，查看故障 AU 信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | GROUP\_ID | INTEGER | 磁盘组 ID |
| 2 | DISK\_ID | INTEGER | 磁盘 ID |
| 3 | AU\_NO | INTEGER | AU 编号 |
| 4 | FILE\_ID | BIGINT | 所属文件 ID |
| 5 | AU\_SEQ | INTEGER | 文件内 AU 编号 |

## 15.3 DMDSC 日志文件

DMDSC 集群、DMCSS 集群和 DMASM 集群在运行过程中，各节点均会生成各自的日志文件，日志文件位于各节点的 log 目录里。

### 15.3.1 DMDSC 集群日志

对于 DMDSC 集群，每个 DMSERVER 节点会生成相应的事件日志文件。事件日志文件记录了 DM 数据库运行时的关键事件。例如：系统启动、关闭、内存申请失败、IO 错误等一些致命错误；数据库运行过程中的日志信息；备份还原过程中备份还原操作的阶段性信息等。

事件日志文件主要用于系统出现严重错误时进行查看并定位问题。事件日志文件随着 DMSERVER 的运行一直存在。

事件日志文件打印的是中间步骤的信息，所以出现部分缺失属于正常现象。事件日志信息格式为：时间 + 日志类型（INFO/WARNING/ERROR/FATAL）+ 进程（database）+ 进程 ID（P 开头）+ 线程（dm\_sql\_thd/main\_thread 等）+ 日志内容。

DMSERVER 启动时，如遇到 dm.key、dm.ini 不存在等原因无法正常启动，因尚未获取到实例名，因此将生成的事件日志文件命名为“dm\_unknown\_年月”。例如：dm\_unknown\_202212。

DMSERVER 运行过程中产生的事件日志生成到当月的月度事件日志文件中，命名为“dm\_实例名\_年月”。例如：dm\_DSC01\_202212.log。

更多事件日志文件的介绍请参考《DM8 系统管理员手册》。

### 15.3.2 DMCSS 集群日志

对于 DMCSS 集群，每个 DMCSS 节点会产生各自的事件日志文件，记录 DMCSS 运行过程中的关键事件。例如：DMCSS 启动、关闭、操作数据库等。

DMCCS 事件日志文件命名为“dm\_实例名\_年月”。例如：dm\_CSS1\_202212.log。DMCSS 事件日志信息格式为：时间 + 日志类型（INFO/WARNING/ERROR/FATAL）+ 进程（dmcss）+ 进程 ID（P 开头）+ 线程 ID（T 开头）+ 日志内容。

### 15.3.3 DMASM 集群日志

DMASM 集群分为非镜像环境和镜像环境。两种环境下日志不同。下面分别进行介绍：

**非 DMASM 镜像环境下的日志**

在非 DMASM 镜像环境中，对于 DMASM 集群，每个节点会产生以下几种日志文件：

一 DMASM 事件日志文件，记录 DMASMSVR 运行过程中的关键事件。例如：DMASMSVR 启动，关闭、MAL 通信检查、DMCSS 命令检查等。该日志文件命名为“dm\_实例名\_年月”。例如：dm\_ASM1\_202212.log。DMASM 事件日志信息格式为：时间 + 日志类型（INFO/WARNING/ERROR/FATAL）+ 进程（dmasmsvr）+ 进程 ID（P 开头）+ 线程 ID（T 开头）+ 日志内容。

二 DMASMCMD 工具日志文件，记录 DMASMCMD 执行的各种操作。该日志文件命名为“dm\_dmasmcmd\_年月”。例如：dm\_dmasmcmd\_202212.log。该日志信息格式为：时间 + 日志类型（INFO/WARNING/ERROR/FATAL）+ 进程（dmasmcmd）+ 进程 ID（P 开头）+ 线程 ID（T 开头）+ 日志内容。

三 DMASMAPI 日志文件，记录通过 DMASMAPI 接口操作 DMASM 文件的内容。该日志文件命名为“dmasmapi\_进程 ID（P 开头）\_年月”。例如：dmasmapi\_P0000540862\_202210.log。DMASMAPI 日志信息格式为：时间 + 线程 ID（T 开头）+ 日志类型（TRACE/WARNING/ERROR/FATAL）+ 日志内容。

四 DMASMTOOL 工具日志文件，记录通过 DMASMTOOL 执行的各种操作。该日志文件命名为“dm\_dmasmtool\_年月”。例如：dm\_dmasmtool\_202212.log。该日志信息格式为：时间 + 线程 ID（T 开头）+ 日志类型（TRACE/WARNING/ERROR/FATAL）+ 日志内容。

五 DMASM 文件操作日志文件，记录系统对 DMASM 文件的打开、关闭、增加，删除等操作。该日志文件命名为“dmasm\_节点序号\_年月”，节点序号为 01、02……。例如：dmasm02\_202212.log。DMASM 文件操作日志信息格式为：时间 +DMASM+ 日志类型（TRACE/WARNING/ERROR/FATAL）+ 日志内容。

**DMASM 镜像环境下的日志**

在 DMASM 镜像环境中，对于 DMASM 集群，每个节点会产生几种日志文件：

一 DMASM 事件日志文件，记录 DMASMSVRM 运行过程中的关键事件。该日志文件在镜像环境下和非镜像环境下，用法完全一致。具体请参考非镜像环境下的 DMASM 事件日志文件。

二 DMASMCMDM 工具日志文件，记录 DMASMCMDM 执行的各种操作。该日志文件命名为“dm\_dmasmcmdm\_年月”。例如：dm\_dmasmcmdm\_202212.log。该日志信息格式为：时间 + 日志类型（INFO/WARNING/ERROR/FATAL）+ 进程（dmasmcmdm）+ 进程 ID（P 开头）+ 线程 ID（T 开头）+ 日志内容。

三 DMASMAPIM 日志文件，记录通过 DMASMAPIM 接口操作 DMASM 文件的内容。该日志文件命名为“dmasmapi3\_进程 ID（P 开头）\_年月”。例如：dmasmapi3\_P0000540862\_202210.log。DMASMAPI 日志信息格式为：时间 + 线程 ID（T 开头）+ 日志类型（TRACE/WARNING/ERROR/FATAL）+ 日志内容。

四 DMASMTOOLM 工具日志文件，记录通过 DMASMTOOLM 执行的各种操作。该日志文件命名为“dm\_dmasmtoolm\_年月”。例如：dm\_dmasmtoolm\_202212.log。该日志信息格式为：时间 + 线程 ID（T 开头）+ 日志类型（TRACE/WARNING/ERROR/FATAL）+ 日志内容。

五 DMASM 文件操作日志文件，记录系统对 DMASM 文件的打开、关闭、增加，删除等操作。该日志文件命名为“dmasm\_trace\_进程 ID（P 开头）\_年月日”。例如：dmasm\_trace\_P0000002432\_20221202.log。DMASM 文件操作日志信息格式为：时间 +DMASM+ 日志类型（TRACE/WARNING/ERROR/FATAL）+ 日志内容。