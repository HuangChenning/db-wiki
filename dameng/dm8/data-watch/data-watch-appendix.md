---
title: "附录"
book: "DM8 数据守护与读写分离集群"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/data-watch-appendix.html
tags:
  - dameng
  - dm8
  - data-watch
---

## 10.1 系统视图

用于数据守护环境下的一些系统信息查询。

### 1.V$UTSK\_INFO

查询守护进程向服务器发送请求的执行情况。

此视图仅用于查看当前服务器的命令执行情况，在 CMD 字段值不为空时，说明是有效的命令信息；此时如果 CODE 字段值是 100，说明命令还在执行中；如果 CODE 字段值是 0，说明命令已经执行成功；如果 CODE 字段值小于 0，则说明命令执行失败。

其中，RUNNING/RECOVER\_BREAK/AUTO\_SWITCH 为系统全局信息，为保持兼容在此视图中仍然保留这三个字段，但字段值统一置为 NULL，没有实际意义，可再通过查询 V$UTSK\_SYS2 视图来查看系统全局信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RUNNING | VARCHAR(64) | 当前系统是否正在处理守护进程请求，TRUE 表示正在处理，FALSE 表示没有。兼容保留字段，升级后直接显示 NULL 值 |
| 2 | DSEQ | INTEGER | 守护进程发送的报文序号，此字段为兼容保留字段，没有实际意义，字段值直接显示为 0，真正的报文序号可查询 DSEQ2 字段值获取 |
| 3 | CODE | INTEGER | DSEQ 对应的执行结果 |
| 4 | SEND\_LSN | BIGINT | 主库当前已发送给备库的 LSN 值 |
| 5 | RECOVER\_BREAK | VARCHAR(64) | 用于显示主库的 Recovery 流程是否被中断， TRUE 表示被中断，FALSE 表示没有。兼容保留字段，升级后直接显示 NULL 值 |
| 6 | AUTO\_SWITCH | VARCHAR(64) | 守护系统配置的切换模式，TRUE 表示故障自动切换，FALSE 表示故障手动切换。兼容保留字段，升级后直接显示 NULL 值 |
| 7 | NTH | INTEGER | 命令所在的数组序号 |
| 8 | CMD | VARCHAR(64) | 待执行或已经执行完成的命令 |
| 9 | INST\_NAME | VARCHAR(64) | 需要恢复的备库实例名，只在主库启动恢复时会设置 |
| 10 | MAX\_SEND\_LSN | BIGINT | 主库向备库发送的最大 LSN 值 |
| 11 | DSEQ2 | BIGINT | 守护进程发送的报文序号 |

### 2.V$UTSK\_SYS2

显示服务器当前的全局信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RUNNING | VARCHAR(64) | 当前系统是否正在处理守护进程请求，TRUE 表示正在处理，FALSE 表示没有 |
| 2 | BREAK\_FLAG | VARCHAR(64) | 守护进程命令是否被中断，取值：TRUE/FALSE |
| 3 | AUTO\_SWITCH | VARCHAR(64) | 守护系统配置的切换模式，TRUE 表示故障自动切换，FALSE 表示故障手动切换 |
| 4 | MAX\_WAIT\_TIME | INTEGER | 服务器等待守护进程启动的最大时间，取 本地 dm.ini 中的 DW\_MAX\_SVR\_WAIT\_TIME 值 |
| 5 | LAST\_MSG\_TIME | DATETIME(0) | 服务器最近一次收到控制守护进程的时间 |
| 6 | DW\_VERSION | VARCHAR(64) | 数据守护版本号 |

### 3.V$RECOVER\_STATUS

该视图需要在主库上查询（DMDSC 主库需要在控制节点上查询），用于查询备库的恢复进度，如果已恢复完成，查询结果为空。

注意这里显示的是主库向备库发送日志的进度，由于备库重做日志也需要时间，在最后一批日志发送完成后，KBYTES\_TO\_RECOVER 为 0，RECOVER\_PERCENT 为 100%，表示主库已经完成所有日志发送，需要等待备库将最后一批日志重做完成，此时主库的守护进程可能仍然处于 Recovery 状态，待备库重做完成后，主库的守护进程会自动切换 Open 状态。

```
RECOVER_PERCENT = (KBYTES_TOTAL - KBYTES_TO_RECOVER)/ KBYTES_TOTAL
```

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PRIMARY\_NAME | VARCHAR(256) | 主库实例名 |
| 2 | STANDBY\_NAME | VARCHAR(256) | 当前正在恢复的备库实例名 |
| 3 | PRIM\_LSN | BIGINT | 主库当前的 FLSN |
| 4 | SEND\_LSN | BIGINT | 主库已发给备库的最大 LSN |
| 5 | KBYTES\_TOTAL | BIGINT | 主库需要发送给备库的日志量，单位为字节 |
| 6 | KBYTES\_TO\_RECOVER | BIGINT | 主库剩余需要发送给备库的日志量，单位为字节。 |
| 7 | FILES\_TO\_RECOVER | INTEGER | 主库需要发给备库重做的总的日志文件个数 |
| 8 | RECOVER\_PERCENT | VARCHAR(64) | 主库向备库已发送日志的比例 |

### 4.V$KEEP\_RLOG\_PKG

该视图需要在备库上查询（DMDSC 备库需要在控制节点（重演节点）上查询），用于查询备库上的 KEEP\_RLOG\_PKG 信息，在备库归档状态有效的情况下可以查到内容。

即时备库没有 KEEP\_RLOG\_PKG 机制，该视图查询结果为空。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TYPE | VARCHAR(64) | 主库的日志同步类型，REATIME 类型 |
| 2 | MIN\_LSN | BIGINT | KEEP\_RLOG\_PKG 中的最小 LSN |
| 3 | MAX\_LSN | BIGINT | KEEP\_RLOG\_PKG 中的最大 LSN |
| 4 | PTX\_OFF | SMALLINT | KEEP\_RLOG\_PKG 中的 PTX 偏移 |
| 5 | LOG\_SIZE | INTEGER | KEEP\_RLOG\_PKG 中的有效日志长度，单位为字节 |
| 6 | DSC\_SEQNO | INTEGER | 标识对应的主库实例节点的序号 DSC\_SEQNO。如果主库是单机，则显示为 0 |
| 7 | DB\_MAGIC | BIGINT | 产生 KEEP\_RLOG\_PKG 包的源数据库的 DB\_MAGIC |
| 8 | PKG\_TYPE | VARCHAR(64) | KEEP\_RLOG\_PKG 包的类型 |
| 9 | PKG\_SEQNO | BIGINT | KEEP\_RLOG\_PKG 包的全局序号 |
| 10 | PREV\_LSN | BIGINT | KEEP\_RLOG\_PKG 包的前一个包的最大 LSN 值 |
| 11 | PKG\_LEN | BIGINT | KEEP\_RLOG\_PKG 包的长度，单位为字节 |

### 5.V$RAPPLY\_SYS

该视图需要在备库上查询（DMDSC 备库需要在控制节点（重演节点）上查询），用于查询备库重做日志时的一些系统信息。

对备库上的日志堆积情况进行监控时，如果 TASK\_NUM 字段值超过了 REDOS\_BUF\_NUM 参数值，或者 TASK\_MEM\_USED 字段值超过了 REDOS\_BUF\_SIZE 参数值，则会触发备库的日志堆积控制机制，备库会延迟响应主库直到堆积值降至 REDOS\_BUF\_NUM 和 REDOS\_BUF\_SIZE 所规定的阈值以下。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | APPLYING | VARCHAR(64) | 备库的重做线程是否正在处理任务，查询结果为 TRUE 或 FALSE |
| 2 | SSEQ | BIGINT | 备库可重演到的最大包序号值 |
| 3 | SLSN | BIGINT | 备库可重演到的最大 LSN 值 |
| 4 | KSEQ | BIGINT | 非自动切换模式下，备库保持不重演的 RLOG\_PKG 的序号。 |
| 5 | KLSN | BIGINT | 非自动切换模式下，备库保持不重演的 RLOG\_PKG 的最大 LSN |
| 6 | TASK\_NUM | INTEGER | 备库上尚未开始重做，处于等待中的任务个数（在主库为 DSC 的情况下，备库重演全部任务都放到 0 号节点对应重演结构中。因此只有 0 号节点重演结构任务数会改变，其余节点重演结构 TASK\_NUM=0） |
| 7 | PRIMARY\_NAME | VARCHAR(128) | 备库对应的主库实例名 |
| 8 | HAS\_KEEP\_PKG | VARCHAR(64) | 备库上是否有 KEEP\_RLOG\_PKG，查询结果为 TRUE 或 FALSE |
| 9 | TASK\_MEM\_USED | BIGINT | 尚未开始重做的所有任务占用的内存大小（字节）。包括还没来得及放在 KEEP\_RLOG\_PKG 上的任务、已经放在 KEEP\_RLOG\_PKG 上的任务、从 KEEP\_RLOG\_PKG 上取下来正在等待重做的任务（TASK\_NUM 任务数）（在主库为 DSC 的情况下，备库重演全部任务都放到 0 号节点对应重演结构中，所占空间也存储在 0 号重演结构中。因此只有 0 号节点重演结构 TASK\_MEM\_USED 会改变，其余节点重演结构 TASK\_MEM\_USED=0） |
| 10 | TASK\_START\_TIME | TIMESTAMP | 当前正在重做日志 PKG 的开始时间 |
| 11 | LAST\_REDO\_TIME | BIGINT | 最近一次日志 PKG 重做的耗时（毫秒） |
| 12 | TASK\_NUM\_APPLIED | BIGINT | 备库上已经重做的日志 PKG 总个数 |
| 13 | APPLIED\_TOTAL\_TIME | BIGINT | 备库上重做的日志 PKG 的总时间（毫秒） |
| 14 | SEQNO | INTEGER | 标识对应的主库实例节点的序号 DSC\_SEQNO。如果主库是单机，则显示为 0 |
| 15 | RREC\_TYPE | VARCHAR(64) | 当前重演的物理记录类型。取值如下：RTYPE\_FILE\_EXTEND：文件扩展；RTYPE\_FILE\_CREATE：文件创建；RTYPE\_NONE：没有文件相关动作 |

### 6.V$RAPPLY\_LOG\_TASK

该视图需要在备库上查询（DMDSC 备库需要在控制节点（重演节点）上查询），用于查询备库当前重做任务的日志信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TYPE | VARCHAR(64) | 主库的日志同步类型，REATIME/TIMELY/ASYNC |
| 2 | MIN\_LSN | BIGINT | 日志 PKG 的最小 LSN 值 |
| 3 | MAX\_LSN | BIGINT | 日志 PKG 的最大 LSN 值 |
| 4 | PTX\_OFF | SMALLINT | 日志 PKG 的 PTX 偏移 |
| 5 | LOG\_SIZE | INTEGER | 日志 PKG 的有效长度，单位为字节 |
| 6 | DSC\_SEQNO | INTEGER | 标识对应的主库实例节点的序号 DSC\_SEQNO。如果主库是单机，则显示为 0 |
| 7 | DB\_MAGIC | BIGINT | 产生日志 PKG 的源数据库的 DB\_MAGIC |
| 8 | PKG\_TYPE | VARCHAR(64) | 日志 PKG 的类型 |
| 9 | PKG\_SEQNO | BIGINT | 日志 PKG 的序号 |
| 10 | PREV\_LSN | BIGINT | 前一个 PKG 的最大 LSN |
| 11 | PKG\_LEN | BIGINT | 日志 PKG 的长度，单位为字节 |

### 7.V$ARCH\_FILE

查询本地已经归档的日志信息。对 DMDSC 集群，除了显示本地归档外，也显示远程归档信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | DB\_MAGIC | BIGINT | 写入日志的数据库的 MAGIC 值 |
| 2 | STATUS | VARCHAR(64) | 归档日志状态 |
| 3 | LEN | BIGINT | 日志长度，单位为字节 |
| 4 | FREE | BIGINT | 写日志偏移位置 |
| 5 | ARCH\_LSN | BIGINT | 归档文件起始 LSN，仅对归档文件有意义 |
| 6 | CLSN | BIGINT | 已归档的最大 LSN |
| 7 | ARCH\_SEQ | BIGINT | 归档文件起始包序号，仅对归档文件有意义 |
| 8 | NEXT\_SEQ | BIGINT | 已归档的最大包序号 |
| 9 | CREATE\_TIME | DATETIME(6) | 归档文件创建时间 |
| 10 | CLOSE\_TIME | DATETIME(6) | 归档文件关闭时间 |
| 11 | PATH | VARCHAR(256) | 归档文件所在路径，包括归档文件名 |
| 12 | PMNT\_MAGIC | BIGINT | 数据库的永久 MAGIC |
| 13 | DSC\_SEQNO | INTEGER | DSC 节点序号，单节点为 0 |
| 14 | CRC\_CHECK | INTEGER | 是否进行 CRC 校验 |
| 15 | LAST\_PKG\_OFF | BIGINT | 最后一个有效的日志包在文件中的偏移位置 |
| 16 | PREV\_LSN | BIGINT | 前一个归档文件已归档的最大 LSN |
| 17 | GLOBAL\_NEXT\_SEQ | BIGINT | 已归档的最大包序号 |
| 18 | SRC\_DB\_MAGIC | BIGINT | 产生日志的源数据库的 MAGIC 值 |
| 19 | LLOG\_FIRST\_TIME | DATETIME(6) | 归档文件中包含的第一条逻辑日志的生成时间，仅在开启逻辑日志时有效 |
| 20 | LLOG\_LAST\_TIME | DATETIME(6) | 归档文件中包含的最后一条逻辑日志的生成时间，仅在开启逻辑日志时有效 |

### 8.V$ARCH\_STATUS

查询归档状态信息。当在备库上查询该视图时，REALTIME/TIMELY/RAFT/LEARNER 归档的归档状态为 NULL，说明这四个归档类型应在主库上查询归档状态；当为非备库模式，或非上述四种归档类型，则显示实际的归档状态。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ARCH\_TYPE | VARCHAR(256) | 归档类型 |
| 2 | ARCH\_DEST | VARCHAR(512) | 归档目标，本地归档为本地归档路径，远程归档为远程节点的本地归档日志文件存放路径，其他类型为归档目标实例名 |
| 3 | ARCH\_STATUS | VARCHAR(256) | 归档状态，VALID 为有效状态，INVALID 为无效状态，ASYNC\_SEND 表示正在进行归档日志同步 |
| 4 | ARCH\_SRC | VARCHAR(256) | 远程归档为远程节点实例名，其他归档类型为本地实例名 |

### 9.V$DM\_ARCH\_INI

归档参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ARCH\_NAME | VARCHAR (128) | 归档名称 |
| 2 | ARCH\_TYPE | VARCHAR (128) | 归档类型 |
| 3 | ARCH\_DEST | VARCHAR (512) | 对于本地归档，表示归档路径；对于远程归档，表示远程节点实例名；对于其余类型的归档，表示归档目标实例名 |
| 4 | ARCH\_FILE\_SIZE | INTEGER | 归档文件大小 |
| 5 | ARCH\_SPACE\_LIMIT | INTEGER | 归档文件的磁盘空间限制，单位是 MB |
| 6 | ARCH\_HANG\_FLAG | INTEGER | 如果写入本地归档时磁盘空间不够，是否让服务器挂起。仅对本地归档有效，其他归档类型显示为 NULL |
| 7 | ARCH\_TIMER\_NAME | VARCHAR (128) | 对于异步归档，表示定时器名称；其余类型归档显示 NULL |
| 8 | ARCH\_IS\_VALID | CHAR(1) | 归档状态，是否有效 |
| 9 | ARCH\_WAIT\_APPLY | INTEGER | 在主备系统中，主库发送归档日志给备库之前，是否需要等待备库将上一批日志重演完成。取值 0：高性能模式，不用等待重演完成；1：事务一致模式，需等待重演完成。除即时归档和实时归档外，其他归档取值均为 NULL |
| 10 | ARCH\_INCOMING\_PATH | VARCHAR(256) | 对于远程归档，表示远程节点的本地归档日志文件存放路径；其余类型归档显示 NULL |
| 11 | ARCH\_CURR\_DEST | VARCHAR(256) | 当前归档目标实例名，如果备库是 DMDSC 集群，则归档目标是备库控制节点，该字段表示当前被选定为归档目标的节点实例名。备库是单机的情况下，就是指的备库实例名 |
| 12 | ARCH\_FLUSH\_BUF\_SIZE | INTEGER | 归档刷盘缓存大小，单位 MB，取值范围 0~128。0 表示不使用归档刷盘缓存机制。缺省为 2 |
| 13 | ARCH\_RESERVE\_TIME | INTEGER | 归档日志保留时间，单位分钟。只对本地归档有效。服务器每隔 5 分钟检查是否存在超过保留时间的归档并删除。缺省为 0，表示不删除归档 |
| 14 | ARCH\_LOCAL\_SHARE | INTEGER | 保留字段，始终为 1 |
| 15 | ARCH\_LOCAL\_SHARE\_CHECK | INTEGER | 保留字段，始终为 1 |
| 16 | ARCH\_SEND\_DELAY | INTEGER | 源库到异步备库的归档延时发送时间。单位分钟。0 表示未启用归档延时发送功能 |
| 17 | ARCH\_DEST\_IP | VARCHAR(64) | 归档目标 IP（该字段对数据守护集群没有意义） |
| 18 | ARCH\_DEST\_PORT | INTEGER | 归档目标端口（该字段对数据守护集群没有意义） |
| 19 | ARCH\_DEST\_ID | INTEGER | 归档目标多副本节点编号，用于标识多副本 RAFT 组中不同的节点（该字段对数据守护集群没有意义） |
| 20 | ARCH\_ASM\_MIRROR | SMALLINT | 归档文件配置在 DMASM 上的镜像类型，DMASM 镜像专用，取值：1：单副本，表示外部冗余，不提供任何镜像，假设磁盘高度可靠；2：双副本，表示正常冗余，提供双向镜像，可较好的保证数据完整性；3：三副本，表示高度冗余，提供三向镜像，能够更好的保证数据的完整性。未配置显示 NULL |
| 21 | ARCH\_ASM\_STRIPING | SMALLINT | 归档文件配置在 DMASM 上的条带化粒度，DMASM 镜像专用，取值 0 表示粗粒度，32/64/128/256 表示细粒度条带化大小，单位 KB。未配置显示 NULL |
| 22 | ARCH\_RECOVER\_TIME | INTEGER | 主库向归档状态为 Invalid 的同步备库发起异步恢复的时间间隔，单位为秒 |

### 10.V$DM\_MAL\_INI

MAL 参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | MAL\_NAME | VARCHAR (128) | MAL 名称 |
| 2 | MAL\_INST\_NAME | VARCHAR (256) | 实例名称 |
| 3 | MAL\_HOST | VARCHAR (256) | IP 地址 |
| 4 | MAL\_PORT | INTEGER | 端口号 |
| 5 | MAL\_INST\_HOST | VARCHAR (256) | 对应实例 IP 地址 |
| 6 | MAL\_INST\_PORT | INTEGER | 对应实例的端口号 |
| 7 | MAL\_DW\_PORT | INTEGER | MAL\_INST\_NAME 实例的守护进程监听远程守护进程或监视器连接请求的端口 |
| 8 | MAL\_LINK\_MAGIC | INTEGER | MAL 链路网段标识 |
| 9 | MAL\_INST\_DW\_PORT | INTEGER | MAL\_INST\_NAME 实例监听守护进程连接请求的端口 |

### 11.V$DM\_TIMER\_INI

定时器参数信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | TIMER\_NAME | VARCHAR(128) | 定时器名称 |
| 2 | TYPE | TINYINT | 类型 |
| 3 | FREQ\_MONTH\_WEEK\_INTERVAL | INTEGER | 月或周的间隔 |
| 4 | FREQ\_SUB\_INTERVAL | INTEGER | 间隔天数 |
| 5 | FREQ\_MINUTE\_INTERVAL | INTEGER | 分钟间隔 |
| 6 | START\_TIME | TIME(0) | 开始时间 |
| 7 | END\_TIME | TIME(0) | 结束时间 |
| 8 | DURING\_START\_DATE | DATETIME(6) | 有效时间段的开始日期时间 |
| 9 | DURING\_END\_DATE | DATETIME(6) | 有效时间段的结束日期时间 |
| 10 | NO\_END\_DATE\_FLAG | CHAR(1) | 无结束日期标识，Y 无结束日期；N 有结束日期。对应 dmtimer.ini 中的 NO\_END\_DATA\_FLAG 配置项。Y 对应 1；N 对应 0 |
| 11 | DESCRIBE | VARCHAR(256) | 描述 |
| 12 | IS\_VALID | CHAR(1) | 是否有效，Y 是；N 否。对应 dmtimer.ini 中的 IS\_VALID 配置项。Y 对应 1；N 对应 0 |
| 13 | REPEAT\_INTERVAL | VARCHAR(4000) | 日历表达式 |

### 12.V$DMWATCHER

查询当前登录实例所对应的守护进程信息，注意一个守护进程可以同时守护多个组的实例，因此查询结果中部分字段（N\_GROUP、SWITCH\_COUNT）为守护进程的全局信息，并不是当前登录实例自身的守护信息。在 DMDSC 集群环境中，只显示控制守护进程的信息。

另外 MPP 主备环境下，全局登录方式返回的是所有 MPP 站点上查询返回的守护进程信息，可以根据 INST\_NAME 实例名字段来区分。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | N\_GROUP | INTEGER | 守护进程全局信息，指实例所在的守护进程守护的组个数 |
| 2 | GROUP\_NAME | VARCHAR(128) | 实例所在的守护进程组名 |
| 3 | INST\_NAME | VARCHAR(128) | 实例名 |
| 4 | DW\_TYPE | VARCHAR(32) | 实例所在守护进程组的守护类型 |
| 5 | DW\_MODE | VARCHAR(32) | 实例所在守护进程组的守护模式 |
| 6 | AUTO\_RESTART | INTEGER | 守护进程对本实例是否配置有自动重启， 1：自动重启 0：不自动重启 |
| 7 | DW\_STATUS | VARCHAR(64) | 实例的守护进程状态 |
| 8 | DW\_SUB\_STATUS | VARCHAR(64) | 实例的守护进程子状态 |
| 9 | LAST\_MSG\_TIME | DATETIME(6) | 实例最近一次收到守护进程消息的时间 |
| 10 | SWITCH\_COUNT | INTEGER | 守护进程全局信息，指守护进程组内主库的变迁次数（包括 SWITCHOVER 主备库切换，TAKEOVER 手动/自动接管，TAKEOVER 强制接管导致的主库变迁操作） |
| 11 | CTL\_NUM | INTEGER | 实例的守护进程收到的远程实例控制文件信息个数 |
| 12 | INST\_NUM | INTEGER | 实例的守护进程收到的远程实例信息个数 |
| 13 | MAX\_CONN\_NUM | INTEGER | 实例的守护进程当前最大的 TCP 连接数 |

### 13.V$ARCH\_SEND\_INFO

此视图用于在主库上查询各备库的日志发送统计信息。

如果主库是 DMDSC 集群，并且主库当前正在执行 Recovery 恢复动作，则只有控制节点上会有最新的归档发送信息，如果主库在向备库正常同步数据，则凡是有日志生成并发送的节点上都可以查询到最新的归档发送信息。

主备异步恢复失败时，可以通过 LAST\_SEND\_CODE、LAST\_SEND\_DESC 查看最近一次的恢复失败原因。

主库执行异步恢复过程中，可以通过 TOTAL\_ASYNC\_TIME、TOTAL\_ASYNC\_RPKG 计算平均每个日志包的同步耗时（单位为毫秒），根据主库已刷盘的日志包序号和备库已重演的日志包序号可以估算剩余待同步的日志量所需耗时。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ARCH\_DEST | VARCHAR(512) | 归档目标实例名 |
| 2 | ARCH\_TYPE | INTEGER | 归档类型 |
| 3 | FOR\_RECOVERY | CHAR(1) | 是否为 Recovery 状态下的日志同步（Y/N） |
| 4 | RECNT\_SEND\_CNT | INTEGER | 最近累计日志发送的次数 N |
| 5 | TOTAL\_SEND\_CNT | BIGINT | 累计日志发送次数 |
| 6 | TOTAL\_SEND\_LEN | BIGINT | 累计日志发送长度（字节） |
| 7 | TOTAL\_PTX\_CNT | BIGINT | 累计发送的 PTX 个数 |
| 8 | TOTAL\_SEND\_TIME | BIGINT | 累计日志发送耗时（微秒） |
| 9 | MAX\_SEND\_TIME | BIGINT | 最大的日志发送耗时（微秒） |
| 10 | MAX\_END\_TIME | DATETIME(6) | 最大耗时发送的结束时间 |
| 11 | MAX\_PTX\_CNT | INTEGER | 最大耗时发送的 PTX 个数 |
| 12 | MAX\_SEND\_LEN | INTEGER | 最大耗时发送的日志长度（字节） |
| 13 | MAX\_SEND\_LSN | BIGINT | 最大耗时发送的结束 LSN |
| 14 | LAST\_SEND\_LEN | INTEGER | 最近一次发送的日志长度（字节） |
| 15 | LAST\_SEND\_PTX | INTEGER | 最近一次日志发送的 PTX 个数 |
| 16 | LAST\_SEND\_LSN | BIGINT | 最近一次日志发送的结束 LSN |
| 17 | LAST\_SEND\_TIME | BIGINT | 最近一次日志发送耗时（微秒） |
| 18 | LAST\_START\_TIME | DATETIME(6) | 最近一次日志发送的起始时间 |
| 19 | LAST\_END\_TIME | DATETIME(6) | 最近一次日志发送的结束时间 |
| 20 | RECNT\_SEND\_LEN | BIGINT | 最近 RECNT\_SEND\_CNT 次发送的日志长度（字节） |
| 21 | RECNT\_SEND\_PTX | BIGINT | 最近 RECNT\_SEND\_CNT 次发送的 PTX 个数 |
| 22 | RECNT\_SEND\_TIME | BIGINT | 最近 RECNT\_SEND\_CNT 次发送的耗时（微秒） |
| 23 | LAST\_SEND\_CODE | INTEGER | 最近一次日志发送错误码 |
| 24 | LAST\_SEND\_DESC | VARCHAR(1024) | 最近一次日志发送的描述信息 |
| 25 | TOTAL\_ASYNC\_RPKG | BIGINT | 主库在异步恢复过程中，到 ARCH\_DEST 累计已同步的日志包个数，每次启动异步恢复时重新进行计数 |
| 26 | TOTAL\_ASYNC\_TIME | BIGINT | 主库在异步恢复过程中，到 ARCH\_DEST 已同步日志的累计耗时（毫秒），每次启动异步恢复时重新进行计数 |

### 14.V$RAPPLY\_STAT

此视图用于在备库上查询备库重演日志的统计信息。

如果备库是 DMDSC 集群，则需要在控制节点（重演节点）上查询。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RECNT\_APPLY\_NUM | INTEGER | 备库最近重演的日志个数 N |
| 2 | TSK\_MEM\_USED | BIGINT | 备库上重做日志堆积占用的内存大小（字节） |
| 3 | TSK\_START\_TIME | DATETIME(6) | 当前正在重做日志 BUF 的开始时间 |
| 4 | TOTAL\_RECVED\_NUM | BIGINT | 累计收到日志包个数 |
| 5 | TOTAL\_RECVED\_LEN | BIGINT | 累计收到日志量（字节） |
| 6 | TOTAL\_RECVED\_TIME | BIGINT | 累计消息响应时间（微秒） |
| 7 | TOTAL\_APPLY\_NUM | BIGINT | 累计重演日志个数 |
| 8 | TOTAL\_APPLY\_LEN | BIGINT | 累计重演日志量（字节） |
| 9 | TOTAL\_APPLY\_TIME | BIGINT | 累计日志重演时间（微秒） |
| 10 | TOTAL\_WAIT\_TIME | BIGINT | 累计任务等待时间（微秒） |
| 11 | MAX\_RECVED\_TIME | BIGINT | 最大消息响应时间（微秒） |
| 12 | MAX\_WAIT\_TIME | BIGINT | 最大任务等待时间（微秒） |
| 13 | MAX\_APPLY\_TIME | BIGINT | 最大任务重演时间（微秒） |
| 14 | MAX\_APPLY\_LEN | BIGINT | 和 MAX\_APPLY\_TIME 对应的重演日志长度（字节） |
| 15 | LAST\_RECVED\_LEN | BIGINT | 最近一次收到的日志长度（字节） |
| 16 | LAST\_RECVED\_TIME | BIGINT | 最近一次响应时间（微秒） |
| 17 | RECNT\_RECVED\_LEN | BIGINT | 最近 RECNT\_APPLY\_NUM 次收到的日志长度（字节） |
| 18 | RECNT\_RECVED\_TIME | BIGINT | 最近 RECNT\_APPLY\_NUM 次响应时间（微秒） |
| 19 | LAST\_WAIT\_TIME | BIGINT | 最近一次等待时间（微秒） |
| 20 | RECNT\_WAIT\_TIME | BIGINT | 最近 RECNT\_APPLY\_NUM 次等待时间（微秒） |
| 21 | LAST\_APPLY\_LEN | BIGINT | 最后一次日志重演长度（字节） |
| 22 | LAST\_APPLY\_TIME | BIGINT | 最近一次日志重演时间（微秒） |
| 23 | RECNT\_APPLY\_LEN | BIGINT | 最近 RECNT\_APPLY\_NUM 次日志重演长度（字节） |
| 24 | RECNT\_APPLY\_TIME | BIGINT | 最近 RECNT\_APPLY\_NUM 次日志重演时间（微秒） |
| 25 | SEQNO | INTEGER | 标识对应的主库实例节点的序号 DSC\_SEQNO。如果主库是单机，则显示为 0 |
| 26 | LAST\_CMT\_TIME | DATETIME(6) | 备库最新解析的主库最新事务提交记录对应的时间戳 |
| 27 | APPLY\_CMT\_TIME | DATETIME(6) | 备库最新重演的主库最新事务提交记录对应的时间戳 |
| 28 | PKG\_RECEIVE\_DELAY | BIGINT | 日志接收延迟时间（微秒），备库最近一次创建日志包的时间和主库创建对应包的时间的差值。值为 NULL 时表示备库从未收到过主库日志。 主库创建日志包和备库创建日志包的时间和备库最近一次日志包重演时间取的都是本地操作系统时间，因此这 v$ 中这个字段和 PKG\_APPLY\_DELAY 字段会受到主备库操作系统时间的影响，建议在监控此字段之前把主备库的操作系统时间调到一致 |
| 29 | PKG\_APPLY\_DELAY | BIGINT | 日志重演延迟时间（微秒），备库最近一次日志包重演时间和备库对应包创建时间的差值。值为 NULL 时表示备库从未收到过主库日志 |

### 15.V$RAPPLY\_LSN\_INFO

查询备库的重演信息，如果备库是 DMDSC 集群，则需要在控制节点（重演节点）上查询。如果在主库上查询此视图，则查到的是主库曾经作为备库时的历史重演信息。其中后面四个 CKPT\_XX 字段，是在备库刷检查点时才调整，前面四个是随备库重演而动态调整的。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | P\_DB\_MAGIC | BIGINT | 主库 DB\_MAGIC |
| 2 | N\_EP | INTEGER | 主库节点数 |
| 3 | PKG\_SEQ\_ARR | VARCHAR(2048) | 备库对应主库各节点已经写入到联机日志文件的原始包序号数组 |
| 4 | APPLY\_LSN\_ARR | VARCHAR(2048) | 备库对应主库各节点已经写入到联机日志文件的原始 LSN 数组 |
| 5 | CKPT\_P\_DB\_MAGIC | BIGINT | 此字段无实际含义，是保留字段，和 P\_DB\_MAGIC 字段值相等 |
| 6 | CKPT\_N\_EP | INTEGER | 此字段无实际含义，是保留字段，和 N\_EP 字段值相等 |
| 7 | CKPT\_PKG\_SEQ\_ARR | VARCHAR(2048) | 此字段无实际含义，是保留字段，和 PKG\_SEQ\_ARR 字段值相等 |
| 8 | CKPT\_APPLY\_LSN\_ARR | VARCHAR(2048) | 此字段无实际含义，是保留字段，和 APPLY\_LSN\_ARR 字段值相等 |
| 9 | TOTAL\_RPKG\_CNT | BIGINT | 备库重演的日志包总个数 |
| 10 | NEED\_WAIT\_CNT | BIGINT | 备库需要切换为串行重演的日志包个数 |

### 16.V$RLOG\_PKG

显示日志包信息。通过该视图可以查询日志系统中当前日志包的使用情况，如包的长度、最大 LSN、最小 LSN 等。通过该视图还可以查询当前实例日志系统中等待刷盘的链表上的日志包信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | PKG\_LEN | BIGINT | 日志包的长度，单位为字节 |
| 2 | DATA\_OFF | BIGINT | 日志包中有效数据长度 |
| 3 | ENC\_LEN | BIGINT | 日志包加密后数据长度 |
| 4 | CMPR\_LEN | BIGINT | 日志包压缩后数据长度 |
| 5 | HDR\_SIZE | INTEGER | 日志包包头长度 |
| 6 | N\_MAGIC | BIGINT | 日志包固定魔数 |
| 7 | DB\_MAGIC | BIGINT | 数据库魔数 |
| 8 | N\_DSC | INTEGER | DSC 集群节点数 |
| 9 | DSC\_SEQNO | INTEGER | DSC 集群节点号 |
| 10 | FROM\_PRIMARY | INTEGER | 是否为主库生成的日志。1：是 0：否。备库上需要进行填充的日志包一定不是来自主库的。所以在备库模式下，当 PKG\_STAT 字段值为 0 或 1 时，FROM\_PRIMARY 值一定为 0；只有当 PKG\_STAT 字段为 2 时，FROM\_PRIMARY 值才可能为 1 |
| 11 | PKG\_TYPE | INTEGER | 日志包包类型 |
| 12 | ENC\_CMPR | INTEGER | 加密压缩标记，0 表示不加密不压缩，1 表示只加密，2 表示只压缩，3 表示加密压缩 |
| 13 | L\_SEQNO | BIGINT | 本地包序号 |
| 14 | G\_SEQNO | BIGINT | 全局包序号 |
| 15 | MIN\_LSN | BIGINT | 包内日志最小 LSN |
| 16 | MAX\_LSN | BIGINT | 包内日志最大 LSN |
| 17 | PREV\_LSN | BIGINT | 前一个包的日志最大 LSN |
| 18 | N\_FIXED | INTEGER | 包的日志填充次数 |
| 19 | N\_FILLED | INTEGER | 包的填充完成的次数 |
| 20 | PKG\_STAT | INTEGER | 日志包状态，0 表示正在填充的串行包，1 表示正在填充的并行包，2 表示已填充完成待刷盘的日志包 |

### 17.V$RLOG\_PKG\_STAT

显示当前实例日志系统中日志包使用的统计信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | N\_FLUSH\_TO | BIGINT | 请求刷盘的次数 |
| 2 | N\_FLUSH\_WAIT | BIGINT | 刷盘等待的次数 |
| 3 | N\_PUSHED | BIGINT | 拷贝到 flush\_lst 次数 |
| 4 | N\_COPY\_WAIT | BIGINT | 拷贝到 flush\_lst 过程中产生等待的次数 |
| 5 | N\_FOR\_CKPT | BIGINT | 检查点类型的日志包个数 |
| 6 | N\_DISCARDED | BIGINT | 日志刷盘线程中丢弃的日志包个数 |
| 7 | N\_FLUSHED | BIGINT | 刷盘日志包个数 |
| 8 | BYTES\_FLUSHED | BIGINT | 刷盘日志包长度总和 |
| 9 | PKG\_AVG\_BYTES | INTEGER | 刷盘日志包平均长度 |
| 10 | NEXT\_SEQNO | BIGINT | 下一个日志包序号 |
| 11 | N\_ALLOC\_WAIT | BIGINT | 分配日志包过程中产生等待的次数 |
| 12 | GLOBAL\_NEXT\_SEQNO | BIGINT | 下一个全局日志包序号 |
| 13 | PKG\_AVG\_PLL | INTEGER | 日志包的平均并行度 |
| 14 | N\_FLUSH\_LST | INTEGER | 待刷盘的日志包个数 |

### 18.V$RAPPLY\_PARALLEL\_INFO

查询备库的并行重演信息，如果备库是 DMDSC 集群，则需要在控制节点（重演节点）上查询。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | DSC\_SEQNO | INTEGER | 主库节点序号，如果主库是单节点，则序号为 0 |
| 2 | APPLY\_PKG\_SEQ | BIGINT | 备库对应主库各节点已经写入到联机日志文件的原始日志包序号 |
| 3 | APPLY\_LSN | BIGINT | 备库对应主库各节点已经写入到联机日志文件的原始 LSN 值，和 APPLY\_PKG\_SEQ 相对应 |
| 4 | REDOS\_PARALLEL\_NUM | INTEGER | 备库并行重演线程数 |
| 5 | REDO\_LSN\_ARR | VARCHAR(8188) | 备库各路并行重演线程已重演到的 LSN 值 |
| 6 | RPKG\_SEQ | BIGINT | 备库已重演到的日志包序号 |
| 7 | RPKG\_LSN | BIGINT | 备库已重演到的 LSN 值，和 RPKG\_SEQ 相对应 |

### 19.V$DMMONITOR

查询当前登录实例上记录的监视器的相关信息，仅会打印有效的监视器连接信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | DW\_CONN\_TIME | VARCHAR(32) | 监视器与守护进程连接建立的时间 |
| 2 | MON\_CONFIRM | VARCHAR(8) | 是否是确认监视器 |
| 3 | MID | BIGINT | 监视器 MID，监视器系统的唯一标识 |
| 4 | MON\_ID | INTEGER | 监视器在监视器系统中的 ID，仅对多实例监视器有意义 |
| 5 | MON\_TERM | BIGINT | 监视器在监视器系统中的任期号，仅对多实例监视器有意义 |
| 6 | MON\_IP | VARCHAR(64) | 监视器 IP |
| 7 | MON\_VERSION | VARCHAR(128) | 监视器版本号 |
| 8 | HP\_FLAG | VARCHAR(8) | 监视器日志堆积标记，FALSE 表示没有日志堆积，TRUE 表示存在日志堆积，NULL 表示未知是否有日志堆积 |

特殊说明：

1. 多实例监视器配置环境下，仅打印 Leader 信息。
2. 在多实例监视器配置环境下，如果查到多行，其中只有一行是多实例监视器的 Leader；其余信息是另外启动的非确认监视器，不属于多实例监视器集群。
3. 监视器日志堆积标记（HP\_FLAG）可以表示此时多实例监视器 Leader 是否可以正常工作。若出现日志堆积（HP\_FLAG 为 TRUE），说明此时 Leader 监视器无法进行提交，可能多数备库出现故障，Leader 监视器已不能正常工作。对于单实例监视器或数据守护进程或旧版本监视器此字段查询结果无效（HP\_FLAG 为 NULL）。

### 20.V$RLOG\_FREE\_LIST

显示日志空闲链表中的空闲日志包信息。

对于主库或 NORMAL 模式的库，如果开启了 RLOG\_PARALLEL\_ENABLE，则会显示每路并行日志的空闲链表信息，显示行数为 WORKER\_THREADS + 1，否则只显示 1 行。

其中 RLOG\_BUF\_SIZE 和 RLOG\_POOL\_SIZE 会结合日志并行信息、工作线程个数等因素再进行调整，不一定是 dm.ini 中的配置大小。

日志包内存分配关系说明如下：

（1）默认日志包大小 = RLOG\_BUF\_SIZE \* 512 字节。

（2）FREE\_RPKG\_LEN = FREE\_RPKG\_CNT \* 默认日志包大小，代表已分配但未使用的空闲空间。

（3）FREE\_RPKG\_LEN 一定不会超过 RLOG\_POOL\_SIZE 大小。

（4）已分配出的默认大小的日志包内存空间 = N\_ALLOC\_PAGE \* 512 字节，此空间大小大于等于 FREE\_RPKG\_LEN，但不会超过 RLOG\_POOL\_SIZE 大小。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | RLOG\_BUF\_SIZE | INTEGER | 单个日志缓冲区大小（以日志页个数为单位） |
| 2 | RLOG\_POOL\_SIZE | BIGINT | 最大日志缓冲区大小，单位字节 |
| 3 | N\_ALLOC\_PAGE | INTEGER | 空闲链表中已分配出的日志页个数 |
| 4 | FREE\_RPKG\_CNT | INTEGER | 空闲链表中存放的日志包个数 |
| 5 | FREE\_RPKG\_LEN | BIGINT | 空闲链表中存放的日志包总大小，单位字节 |

### 21\. V$ARCH\_APPLY\_INFO

主库或级联异步备库上记录的备库重演信息。重演信息来源于备库，且与备库上真实的重演信息存在 60s 延迟。该视图 60s 刷新一次，并非实时刷新。如果本视图查不到信息，那么可能因为备库上无重演信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | DEST\_NAME | VARCHAR(512) | 归档目标名，如果备库是 DSC 集群，则打印控制节点实例名，若控制节点不存在，则打印归档对象字符串中首个归档对象实例名 |
| 2 | ARCH\_STANDBY\_APPLY | INTEGER | DMARCH.INI 中归档目标的 ARCH\_STANDBY\_APPLY 配置 |
| 3 | DSC\_SEQNO | INTEGER | 重演信息对应的主库 DSC 节点号 |
| 4 | APPLY\_SEQNO | BIGINT | 备库刷盘到的日志包序号 |
| 5 | APPLY\_LSN | BIGINT | 备库刷盘到的最大 LSN |
| 6 | KEEP\_SEQNO | BIGINT | 备库保持不重演的最大日志包序号 |
| 7 | KEEP\_LSN | BIGINT | 备库保持不重演的最大 LSN |
| 8 | STANDBY\_SEQNO | BIGINT | 备库已接收到的最大日志包序号 |
| 9 | STANDBY\_LSN | BIGINT | 备库已接收到的最大 LSN |
| 10 | RPKG\_SEQNO | BIGINT | 备库已重演到的日志包序号 |
| 11 | RPKG\_LSN | BIGINT | 备库已重演到的 LSN |
| 12 | C\_SEQNO | BIGINT | 备库已提交到的日志包序号，仅在 DMDPC 的多副本系统中有效 |
| 13 | C\_LSN | BIGINT | 备库已提交到的 LSN，仅在 DMDPC 的多副本系统中有效 |

### 22\. V$ARCH\_FILE\_HISTORY

当 INI 参数 ENABLE\_MONITOR=1 时，该视图显示因归档空间不足而被服务器主动删除的所有归档文件信息。

1. 此视图只能查询到已被服务器主动删除的归档文件信息，对于尚未被删除或者用户手动删除的归档文件则无法查询到；
2. 此视图最多能够查询到最近 10000 个被服务器主动删除的归档文件信息；
3. 若存在多路本地归档，则该视图的查询结果中将包含每一路本地归档下被删除的归档文件信息；
4. 此视图记录的归档文件历史信息是内存值，不会持久化到磁盘，因此服务器重启后将无法再查询到此前被删除的归档文件信息；
5. 可以通过系统过程 SP\_DYNAMIC\_VIEW\_DATA\_CLEAR 来清空此视图的历史信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | DSC\_SEQNO | INTEGER | DSC 节点序号，单节点为 0 |
| 2 | SRC\_DB\_MAGIC | BIGINT | 产生日志的源数据库的 MAGIC 值 |
| 3 | PMNT\_MAGIC | BIGINT | 数据库的永久 MAGIC |
| 4 | DB\_MAGIC | BIGINT | 写入日志的数据库的 MAGIC 值 |
| 5 | CREATE\_TIME | TIMESTAMP | 归档文件创建时间 |
| 6 | CLOSE\_TIME | TIMESTAMP | 归档文件关闭时间 |
| 7 | DELETE\_TIME | TIMESTAMP | 归档文件删除时间 |
| 8 | LEN | BIGINT | 日志长度，单位为字节 |
| 9 | FREE | BIGINT | 写日志偏移位置 |
| 10 | ARCH\_LSN | BIGINT | 归档文件起始 LSN |
| 11 | CLSN | BIGINT | 已归档的最大 LSN |
| 12 | ARCH\_SEQ | BIGINT | 归档文件起始包序号 |
| 13 | NEXT\_SEQ | BIGINT | 已归档的最大包序号 |
| 14 | PATH | VARCHAR(256) | 归档文件所在路径，包括归档文件名 |

### 23\. V$RPKG\_WARN\_SEND\_INFO

主库日志包发送警告信息。须连接主库查询，在 DM AFC 环境中不支持。

当主库日志包 SEND\_TIME\_USED、RECV\_TIME\_USED 中任意一个耗时超过 RPKG\_PROCESS\_TIMEOUT 时，就生成一条记录登记到 RPKG\_WARN\_SEND\_INFO 中，最多登记 128 条最新记录。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | G\_SEQNO | BIGINT | 全局日志包序号 |
| 2 | MIN\_LSN | BIGINT | 日志包最小 LSN |
| 3 | MAX\_LSN | BIGINT | 日志包最大 LSN |
| 4 | ARCH\_DEST | VARCHAR(512) | 归档目标实例名 |
| 5 | ARCH\_TYPE | VARCHAR(256) | 归档类型 |
| 6 | SEND\_START\_TIME | DATETIME(6) | 日志包发送开始时间 |
| 7 | SEND\_TIME\_USED | BIGINT | 日志包发送耗时，单位微秒 |
| 8 | RECV\_START\_TIME | DATETIME(6) | 日志包回复接收开始时间 |
| 9 | RECV\_TIME\_USED | BIGINT | 日志包回复接收耗时，单位微秒 |

### 24\. V$RPKG\_WARN\_RECV\_INFO

备库日志包接收和回复处理警告信息。须连接备库查询，在 DM AFC 环境中不支持。

当备库日志包 TSK\_CREATE\_USED、TSK\_ENQUEUE\_USED、RES\_TIME\_USED 中任意一个耗时超过 RPKG\_PROCESS\_TIMEOUT 时，就生成一条记录登记到 RPKG\_WARN\_RECV\_INFO 中，最多登记 128 条记录。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | DSC\_SEQNO | INTEGER | 日志包来源 DSC 节点序号 |
| 2 | G\_SEQNO | BIGINT | 全局日志包序号 |
| 3 | MIN\_LSN | BIGINT | 日志包最小 LSN |
| 4 | MAX\_LSN | BIGINT | 日志包最大 LSN |
| 5 | RECV\_START\_TIME | DATETIME(6) | 日志包收到时间 |
| 6 | TSK\_CREATE\_USED | BIGINT | 日志包创建耗时，微秒 |
| 7 | TSK\_ENQUEUE\_USED | BIGINT | 日志包加入重演队列耗时，微秒 |
| 8 | SEND\_START\_TIME | DATETIME(6) | 日志包回复发送开始时间 |
| 9 | SEND\_TIME\_USED | BIGINT | 日志包回复发送耗时，微秒 |
| 10 | RES\_TIME\_USED | BIGINT | 从接收到发回响应的总耗时，单位微妙 |
| 11 | PKG\_FROM | VARCHAR(256) | 日志包来源站点名称 |
| 12 | PKG\_TYPE | INTEGER | 日志包类型：RLOG 或 PLOG（并行日志包） |

### 25\. V$ARCH\_DETACH\_INFO

查询当前已登记的备库 detach 记录。仅在数据守护环境下查询有效，若要在 DSC 主库或 DSC 备库上查询，则仅在控制节点上查询有效。

此视图信息是以 redo 日志的方式从主库同步到备库的，因此对于归档状态无效的备库，查询结果可能会与主库不一致。若需要获取当前最新的已被 detach 出集群的备库信息，建议优先选择主库进行查询。

| 序号 | 列 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| 1 | DB\_DETACHED | VARCHAR(256) | 已被 detach 出集群的备库实例名 |

#### 26\. V$RPKG\_TIME\_USED\_INFO

查询最近主库产生或备库重演的 rpkg 各阶段耗时，最多能查询 128 行。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | G\_SEQNO | BIGINT | 如果为 0，表示该行是各阶段总耗时；如果为 1，表示该行是各阶段平均耗时；如果是其他值，表示全局日志包序号 |
| 2 | MAL\_TIME\_USED | BIGINT | rpkg 涉及 mal 通信的耗时，仅统计主库，备库为 0，单位：微秒 |
| 3 | WRITE\_TIME\_USED | BIGINT | 主库指写日志耗时，备库指日志创建到加入 preload 间的耗时，单位：微秒 |
| 4 | FLST\_TIME\_USED | BIGINT | rpkg 在日志刷盘链表中的耗时，单位：微秒 |
| 5 | FLUSH\_TIME\_USED | BIGINT | 日志刷盘线程处理 rpkg 的耗时，单位：微秒 |
| 6 | RLST\_TIME\_USED | BIGINT | rpkg 在归档任务链表的耗时，单位：微秒 |
| 7 | LOCAL\_TIME\_USED | BIGINT | 本地归档线程处理 rpkg 的耗时，单位：微秒 |
| 8 | PRELOAD\_TIME\_USED | BIGINT | 重演中 preload 的耗时，仅统计备库，主库为 0，单位：微秒 |
| 9 | TSKWAIT\_TIME\_USED | BIGINT | 重演任务等待的耗时，仅统计备库，主库为 0，单位：微秒 |
| 10 | APPLY\_TIME\_USED | BIGINT | 重演耗时，仅统计备库，主库为 0，单位：微秒 |

#### 27\. V$RDMA\_CONN\_INFO

MAL 系统使用 RDMA 通信的连接信息视图。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SEND\_SIGNAL\_CNT | INTEGER | 发送带有 SIGNAL 的工作请求个数 |
| 2 | SEND\_CQ\_POLL\_CNT | INTEGER | 发送端 POLL\_CQ(轮询完成队列)次数 |
| 3 | MBLK\_SIZE | INTEGER | 每次接收消息缓存大小 |
| 4 | MAX\_SEND\_WR | INTEGER | 允许发送的最大请求数 |
| 5 | CQ\_MOD | INTEGER | 发送端生成 CQE(完成队列条目)的批量次数，连续执行 CQ\_MOD 次 POST\_SEND 生成一个 CQE |
| 6 | SEND\_NUM | BIGINT | POST\_SEND 执行次数，CQ\_MOD 配合决定是否生成 CQE，与 MAX\_SEND\_WR 配置决定是否等待 ACK 响应 |
| 7 | MAX\_INLINE\_DATA | INTEGER | 发送队列上内联数据最大大小 |
| 8 | MAX\_RECV\_WR | INTEGER | 允许接收的最大请求数 |
| 9 | POLL\_RCNT | BIGINT | 接收操作 POLL\_CQ(轮询完成队列)返回总次数 |
| 10 | COPY\_RCNT | BIGINT | 已经拷贝走的消息块个数 |
| 11 | IS\_CONNECTED | CHAR(1) | 是否成功连接 |
| 12 | MAL\_PORT | INTEGER | MAL 监听端口，用于数据守护、DSC、MPP 等环境中各节点实例之间 MAL 链路配置，监听端端口配置此参数，取值范围 1024 ~~65534，发起连接端的端口在 1024~~ 65535 之间随机分配 |
| 13 | MAL\_HOST | VARCHAR(20) | 节点实例 |
| 14 | CONN\_TYPE | VARCHAR(25) | 连接链路类型，有三种类型：控制链路、数据链路、RAC 链路，RAC 连接链路只有在 DSC 集群环境下才会出现 |

## 10.2 监视器接口

### 10.2.1 DLL 依赖

监视器 DLL 依赖了其他的一些动态链接库，编程时需要在加载动态链接库时指定 bin 目录。

### 10.2.2 返回值说明

监视器接口总体的返回值策略为：小于 0 表示执行失败，其他值表示执行成功。对于启动/关闭守护进程监控和实例的相关接口，返回值为 100 表示执行前状态已经和预期状态一致，接口实际并未执行。

相关的错误码说明可借助 dwmon\_get\_error\_msg\_by\_code 接口获取错误码对应的错误描述信息。

### 10.2.3 接口调整说明（V4.0）

数据守护 V4.0 版本对监 c、新增、调整了部分接口。

**1\. 删除的接口列表**

1. dwmon\_get\_nth\_watch\_ctl\_item

不再支持。

**2\. 调整过接口定义的列表**

1. dwmon\_get\_split\_sub\_group\_inst

更名为 dwmon\_get\_split\_sub\_group\_database

2. dwmon\_get\_nth\_instance\_info

更名为 dwmon\_get\_nth\_database\_info，接口参数有调整。

3. dwmon\_get\_instance\_info\_by\_name

更名为 dwmon\_get\_database\_info\_by\_name，接口参数有调整。

4. dwmon\_get\_instance\_ep\_info

更名为 dwmon\_get\_database\_info，接口参数有调整。

5. dwmon\_get\_nth\_ep\_info

接口参数有调整。

6. dwmon\_get\_ep\_info\_by\_name

接口参数有调整。

7. dwmon\_get\_inst\_arch\_info

更名为 dwmon\_get\_database\_arch\_info

8. dwmon\_get\_watch\_ctl\_info

接口参数有调整。

9. dwmon\_get\_monitor\_info\_with\_version

更名为 dwmon\_get\_monitor\_info

10. dwmon\_set\_inst\_recover\_time

更名为 dwmon\_set\_database\_recover\_time。

11. dwmon\_set\_inst\_arch\_invalid

更名为 dwmon\_set\_database\_arch\_invalid。

12. dwmon\_stop\_instance

更名为 dwmon\_stop\_database。

13. dwmon\_startup\_instance

更名为 dwmon\_startup\_database。

14. dwmon\_kill\_instance

更名为 dwmon\_kill\_database。

15. dwmon\_open\_instance

更名为 dwmon\_open\_database。

16. dwmon\_detach\_instance

更名为 dwmon\_detach\_database。

17. dwmon\_attach\_instance

更名为 dwmon\_attach\_database。

18. dwmon\_get\_source\_instance\_name

更名为 dwmon\_get\_source\_database\_name。

19. dwmon\_get\_ep\_nth\_apply\_info

更名为 dwmon\_get\_ep\_nth\_apply\_stat，接口参数有调整。

20. dwmon\_get\_ep\_nth\_apply\_lsn\_info

更名为 dwmon\_get\_ep\_nth\_apply\_info。

21. dwmon\_clear\_inst\_arch\_send\_info

更名为 dwmon\_clear\_database\_arch\_send\_info。

22. dwmon\_clear\_inst\_rapply\_info

更名为 dwmon\_clear\_database\_rapply\_stat。

23. dwmon\_clear\_group\_rapply\_info

更名为 dwmon\_clear\_group\_rapply\_stat。

**3\. 新增的接口列表**

1. dwmon\_get\_database\_open\_history
2. dwmon\_get\_nth\_open\_history
3. dwmon\_startup\_database\_watch
4. dwmon\_stop\_database\_watch
5. dwmon\_get\_ep\_nth\_apply\_with\_parallel\_info

### 10.2.4 C 接口说明

#### 1.dwmon\_alloc\_handle

**函数原型：**

```
DWMON_RETURN

dwmon_alloc_handle(

    mhandle* mhdle

);
```

**功能说明：**

分配监视器操作句柄，监视器的接口都通过此句柄调用执行。

**参数说明：**

mhdle: 输出参数，分配到的监视器句柄。

**返回值：**

0：执行成功。

<0：执行失败。

#### 2.dwmon\_get\_error\_msg\_by\_code

**函数原型：**

```
DWMON_RETURN

dwmon_get_error_msg_by_code(

    mhandle mhdle,

    mint4 code,

    mschar* buf_msg,

    muint4 buf_len,

    muint4* msg_len_out

);
```

**功能说明：**

获取输入 code 对应的错误描述信息，code 必须是小于 0 的值。

**参数说明：**

mhdle: 输入参数，分配到的监视器句柄，注意如果是分配句柄或初始化环境时失败，允许 mhdle 是无效的，否则要求 mhdle 必须是有效句柄。

code：输入参数，需要获取错误信息的错误码 code，注意 code 必须是小于 0 的值。

buf\_msg：输出参数，输出错误描述信息，注意 buf\_msg 缓存长度建议大于 4096，避免输出信息被截断。

buf\_len:输入参数，指定 buf\_msg 可写入的最大长度。

msg\_len\_out：输出参数，buf\_msg 缓存实际写入长度。

**返回值：**

0：执行成功。

<0：执行失败，-17 表示没有找到 code 对应的错误信息。

#### 3.dwmon\_init

**函数原型：**

```
DWMON_RETURN

dwmon_init(

    mhandle mhdle,

    mschar* ini_path,

    mschar* log_path

);
```

**功能说明：**

初始化监视器环境。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

ini\_path: 输入参数，指定 dmmonitor.ini 的绝对路径。

log\_path: 输入参数，指定日志文件的存放路径，如果为 NULL 或空串，则将 dmmonitor.ini 中配置的 MON\_LOG\_PATH 作为日志文件路径，如果 dmmonitor.ini 中没有配置 MON\_LOG\_PATH，则将 dmmonitor.ini 的同级目录作为日志文件路径。

**返回值：**

0：执行成功。

<0：执行失败，-15 表示监视器尝试建立到所有守护进程的连接失败，可能守护进程都未启动，允许忽略此错误继续执行其他操作，如果不忽略此错误，认定初始化失败，则需要先正常销毁监视器环境（调用 dwmon\_deinit 接口），再释放操作句柄（调用 dwmon\_free\_handle 接口）。

#### 4.dwmon\_msg\_event\_wait

**函数原型：**

```
void

dwmon_msg_event_wait(

    mhandle mhdle

);
```

**功能说明：**

等待消息事件。监视器检测到守护进程或实例状态发生变化，或者接口命令执行过程中，产生中间输出消息时会将消息写入到缓存并通知消息事件，调用者只需要调用此接口等待即可，等待事件发生后，可通过接口 dwmon\_get\_exec\_msg 去读取输出消息。

这种方式需要单独起一个线程来处理消息，以免消息被阻塞。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

无

#### 5.dwmon\_get\_exec\_msg

**函数原型：**

```
DWMON_RETURN

dwmon_get_exec_msg(

    mhandle mhdle,

    mschar* buf_msg,

    muint4 buf_len,

    muint4* msg_len_out,

    muint4* get_flag

);
```

**功能说明：**

获取输出信息，和 dwmon\_msg\_event\_wait 配合使用。

**参数说明：**

mhdle:

输入参数，监视器操作句柄。

buf\_msg：

输出参数，保存获取到的输出消息，注意 buf\_msg 缓存长度需要大于 4096，以免长度不够导致消息被截断。

buf\_len:

输入参数，指定 buf\_msg 可写入的最大长度，建议 buf\_msg 缓存长度及 buf\_len 输入值大于 4096，避免消息被截断。

msg\_len\_out:

输出参数，写消息成功后，输出实际写入的消息长度。

get\_flag:

输出参数，是否继续读取消息，TRUE 表示还有消息可读，FALSE 表示已全部读完。

**返回值：**

0：执行成功。

<0：执行失败。

#### 6.dwmon\_get\_msg\_exit\_flag

**函数原型：**

```
mbool

dwmon_get_msg_exit_flag(

    mhandle mhdle

);
```

**功能说明：**

如果上层应用程序中有单独的消息线程，可通过调用此接口获取退出标记，在标记为 TRUE 时可正常退出线程。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

1: 允许线程退出。

0: 不允许线程退出，需要继续等待获取输出消息。

#### 7.dwmon\_set\_msg\_exit\_event

**函数原型：**

```
void

dwmon_set_msg_exit_event(

    mhandle mhdle

);
```

**功能说明：**

设置消息退出事件。如果上层应用程序中有单独的消息线程，在 dwmon\_get\_msg\_exit\_flag 接口获取到退出标记为 TRUE 时，需要调用此接口设置退出事件。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

无

#### 8.dwmon\_msg\_event\_deinit

**函数原型：**

```
void

dwmon_msg_event_deinit(

    mhandle mhdle

);
```

**功能说明：**

通知并等待消息退出。使用等待事件方式获取监视器消息时，需要单独起一个线程，在程序结束，退出线程时，需要调用此接口通知并等待消息线程退出。

消息线程相关的接口有 dwmon\_msg\_event\_wait、dwmon\_get\_exec\_msg、dwmon\_get\_msg\_exit\_flag、dwmon\_set\_msg\_exit\_event 和 dwmon\_msg\_event\_deinit，这几个接口需要配合使用。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

无

#### 9.dwmon\_get\_version

**函数原型：**

```
DWMON_RETURN

dwmon_get_version(

    mhandle mhdle,

    mschar* version

);
```

**功能说明：**

获取当前的监视器版本信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

version: 输出参数，输出当前的监视器版本信息，version 的缓存长度不能小于 129，避免溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 10.dwmon\_get\_mpp\_flag

**函数原型：**

```
DWMON_RETURN

dwmon_get_mpp_flag (

    mhandle mhdle,

    mbool* mpp_flag

);
```

**功能说明：**

获取 MPP 主备环境标记，用于判断当前是否为 MPP 主备环境。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

mpp\_flag:输出参数，MPP 主备环境下输出为 TRUE，否则为 FALSE。

**返回值：**

0：执行成功。

<0：执行失败。

#### 11.dwmon\_get\_n\_group

**函数原型：**

```
DWMON_RETURN

dwmon_get_n_group(

    mhandle mhdle,

    muint4* n_group,

    mschar** group_name_arr

);
```

**功能说明：**

获取当前监控的组个数和组名称。

只有 MPP 主备环境下允许配置多组。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

n\_group: 输入输出参数，监视器配置的监控组个数。输入参数：指定可获取的最大组个数，输出参数：实际获取的组个数，建议输入值不小于 16，避免取不到完整信息。

group\_name\_arr: 输出参数，输出监视器配置的监控组名，参数是字符串指针数组类型，数组长度是 n\_group 的输入值，每个指针元素指向的缓存长度不能小于 65，避免长度溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 12.dwmon\_get\_group\_info

**函数原型：**

```
DWMON_RETURN

dwmon_get_group_info(

    mhandle mhdle,

    mschar* group_name,

    muint4* oguid,

    muint4* n_dw,

    mschar** dw_ip_arr,

    msint2* port_arr,

    mschar* dw_type,

    mschar* dw_mode,

    mschar* primary_name,

    muint4* n_split,

    mschar** split_iname_arr,

    muint4* n_db,

    mschar** db_name_arr,

    muint4* n_local,

    mschar** local_name_arr

);
```

**功能说明：**

获取指定组的守护进程组信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要获取信息的组名，只有一组时允许不指定组名。

oguid: 输出参数，输出指定守护进程组的 OGUID 值。

n\_dw: 输入输出参数，指定组配置的控制守护进程个数。输入参数：可获取的最大守护进程个数，输出参数：实际获取的守护进程个数，建议输入值不小于 25，避免取不到完整信息。

dw\_ip\_arr: 输出参数，输出指定组配置的控制守护进程 IP，参数是字符串指针数组类型，数组长度是 n\_dw 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免长度溢出。

port\_arr: 输出参数，输出指定组配置的控制守护进程端口，参数是 msint2 数组类型，数组长度是 n\_dw 的输入值。

dw\_type: 输出参数，输出守护进程类型，注意缓存长度不能小于 65，避免长度溢出。

dw\_mode: 输出参数，输出守护进程切换模式，注意缓存长度不能小于 65，避免溢出。

primary\_name: 输出参数，输出当前的主库实例名，如果组中有多个 PRIMARY 实例，则返回处于 Open 状态的 PRIMARY 实例，如果都是 Mount 状态，则返回 LSN 最大的 PRIMARY 实例，如果有多个 Open 状态的 PRIMARY 实例，则接口会报错返回。注意缓存长度不能小于 65，避免溢出。

n\_split: 输入输出参数，当前的子组个数，如果组中有发生分裂，每个分裂库是一个子组，剩余没有分裂的正常库也是一个子组，如果组中没有分裂情况，则子组个数就是整个的组个数，输出值为 1。输入参数：可获取的最大子组个数，输出参数：实际获取的子组个数，建议输入值不小于 9，避免取不到完整信息。

split\_iname\_arr: 输出参数，输出子组中其他库可加入的库名称，参数是字符串指针数组类型，数组长度是 n\_split 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免溢出。

n\_db: 输入输出参数，配置为 Global 守护类型的库个数。输入参数：可获取的最大库个数，输出参数：实际获取的库个数，建议输入值不小于 9，避免取不到完整信息。

db\_name\_arr: 输出参数，输出配置为 Global 守护类型的库名，参数是字符串指针数组类型，数组长度是 n\_db 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免溢出。

n\_local: 输入输出参数，配置为 local 守护类型的库个数。输入参数：可获取的最大库个数，输出参数：实际获取的库个数，建议输入值不小于 16，避免取不到完整信息。

local\_name\_arr: 输出参数，输出配置为 local 守护类型的库名，参数是字符串指针数组类型，数组长度是 n\_local 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 13.dwmon\_get\_split\_sub\_group\_database

**函数原型：**

```
DWMON_RETURN

dwmon_get_split_sub_group_database(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    muint4* n_db,

    mschar** db_name_arr

);
```

**功能说明：**

获取可加入指定库的库名信息，可以和 dwmon\_get\_group\_info 接口配合使用，其中 db\_name 是 dwmon\_get\_group\_info 中 split\_iname\_arr 数组取出的某个库名。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要获取可加入信息的库名，此参数必须指定。

n\_db: 输入输出参数，可加入指定库的库个数。输入参数：指定可获取的最大库个数，输出参数：实际获取的库个数，建议输入值不小于 8，避免取不到完整信息。

db\_name\_arr: 输出参数，输出可加入指定库的库名，参数是字符串指针数组类型，数组长度是 n\_db 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 14.dwmon\_get\_nth\_database\_info

**函数原型：**

```
DWMON_RETURN

dwmon_get_nth_database_info(

    mhandle mhdle,

    mschar* group_name,

    muint4 nth,

    mschar* dw_time,

    mschar* dw_ip,

    msint2* dw_port,

    mschar* dw_type,

    mschar* dw_mode,

    muint4* dw_err_time,

    mschar* dw_sta,

    mschar* dw_sub_sta,

    mschar* dw_ctl_sta,

    mschar* db_name,

    mschar* db_ok_str,

    mschar* svr_mode,

    mschar* svr_status,

    mschar* arch_type,

    mschar* arch_status,

    muint4* pmnt_magic,

    muint4* db_magic,

    msint2* n_ep,

    msint2* ep_seqno_arr,

    mschar** ep_name_arr,

    msint2* dsc_ctl_node,

    mschar* dsc_status,

    msint2* n_ok_ep,

    msint2* ok_ep_arr,

    msint2* n_break_ep,

    msint2* break_ep_arr

);
```

**功能说明：**

获取指定组中第 nth 个库的全局信息，这里的 nth 是根据 dmmonitor.ini 指定组中所配置的守护进程先后顺序来排序的，每个组的 nth 都是从 0 开始，依次递增。

**参数说明：**

> **注意**
> 
> 对字符串类型的输出参数，指向的缓存长度不能小于65，避免溢出。

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定的守护进程组名，只有一组时可以不指定。

nth: 输入参数，输入要获取的数据库实例下标。

dw\_time: 输出参数，输出守护进程最近一次收到本地 dmserver 消息的时间，取自控制守护进程。在系统时间一致的情况下，可用于计算监视器和 dmserver 间的延迟时间。NULL 表示未收到过本地 dmserver 消息。

dw\_ip: 输出参数，输出控制守护进程配置的 IP 地址。

dw\_port: 输出参数，输出控制守护进程配置的端口。

dw\_type: 输出参数，输出配置的守护类型。

dw\_mode：输出参数，输出配置的切换模式。

dw\_err\_time: 输出参数，输出配置的守护进程故障认定时间。

dw\_sta: 输出参数，输出控制守护进程状态。

dw\_sub\_sta: 输出参数，输出控制守护进程子状态。

dw\_ctl\_sta: 输出参数，输出守护进程控制文件状态。

db\_name: 输出参数，输出守护的数据库名称。

db\_ok\_str: 输出参数，输出守护进程认定的库状态(OK/Error)。

svr\_mode: 输出参数，输出库模式(Normal/PRIMARY/STANDBY)。

svr\_status: 输出参数，输出库状态(Startup/After Redo/Mount/Open/Suspend/Shutdown)。

arch\_type: 输出参数，输出库上配置的归档类型（REALTIME/TIMELY）

arch\_status: 输出参数，指定待获取的库为实时备库或即时备库时，输出组中主库到此备库的归档状态，如果是异步备库，则输出为“NULL”，如果是主库，则输出“VALID”。

pmnt\_magic: 输出参数，输出数据库永久魔数。

db\_magic: 输出参数，输出数据库魔数。

n\_ep: 输入输出参数，指定库中包含的节点实例个数。输入参数：可获取的最大实例个数，输出参数：实际获取到的实例个数，建议输入值不小于 16，避免获取不到完整信息。

ep\_seqno\_arr: 输出参数，输出指定库中所有实例的 seqno 数组，参数是 msint2 数组类型，数组长度是 n\_ep 的输入值。

ep\_name\_arr: 输出参数，输出指定库中所有实例的实例名数组，参数是字符串指针数组类型，数组长度是 n\_ep 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免长度溢出。

dsc\_ctl\_node: 输出参数，输出指定库中控制节点的 seqno，对单节点库，输出值为 0。

dsc\_status: 输出参数，输出指定库的状态。

n\_ok\_ep: 输入输出参数，指定库中包括的 ok 节点实例个数。输入参数：可获取的最大实例个数，输出参数：实际获取到的实例个数，建议输入值不小于 16，避免获取不到完整信息。对单节点库，输出值为 1。

ok\_ep\_arr: 输出参数，输出指定库中所有 ok 节点实例的 seqno 数组，参数是 msint2 数组类型 数组长度是 n\_ok\_ep 的输入值。

n\_break\_ep: 输入输出参数，指定库中当前正在故障处理的节点数。输入参数：可获取的最大实例个数，输出参数：实际获取到的实例个数，建议输入值不小于 16，避免获取不到完整信息。

break\_ep\_arr: 输出参数，输出指定库中当前正在故障处理的节点 seqno 数组，参数是 msint2 数组类型，数组长度是 n\_break\_ep 的输入值。

**返回值：**

0：执行成功。

<0：执行失败。

#### 15.dwmon\_get\_database\_info\_by\_name

**函数原型：**

```
DWMON_RETURN

dwmon_get_database_info_by_name(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    mschar* dw_time,

    mschar* dw_ip,

    msint2* dw_port,

    mschar* dw_type,

    mschar* dw_mode,

    muint4* dw_err_time,

    mschar* dw_sta,

    mschar* dw_sub_sta,

    mschar* dw_ctl_sta,

    mschar* dbt_ok_str,

    mschar* svr_mode,

    mschar* svr_status,

    mschar* arch_type,

    mschar* arch_status,

    muint4* pmnt_magic,

    muint4* db_magic,

    msint2* n_ep,

    msint2* ep_seqno_arr,

    mschar** ep_name_arr,

    msint2* dsc_ctl_node,

    mschar* dsc_status,

    msint2* n_ok_ep,

    msint2* ok_ep_arr,

    msint2* n_break_ep,

    msint2* break_ep_arr

);
```

**功能说明：**

根据指定的数据库名称获取库的全局信息。

**参数说明：**

对字符串类型的输出参数，指向的缓存长度不能小于 65，避免溢出。

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定的守护进程组名，只有一组时可以不指定。

db\_name: 输入参数，指定要获取信息的数据库名称。

dw\_time: 输出参数，输出控制守护进程本地的当前时间。

dw\_ip: 输出参数，输出控制守护进程配置的 IP 地址。

dw\_port: 输出参数，输出控制守护进程配置的端口。

dw\_type: 输出参数，输出配置的守护类型。

dw\_mode：输出参数，输出配置的切换模式。

dw\_err\_time: 输出参数，输出配置的守护进程故障认定时间。

dw\_sta: 输出参数，输出控制守护进程状态。

dw\_sub\_sta: 输出参数，输出控制守护进程子状态。

dw\_ctl\_sta: 输出参数，输出守护进程控制文件状态。

dbt\_ok\_str: 输出参数，输出守护进程认定的库状态是否正常(OK/Error)。

svr\_mode: 输出参数，输出库模式(NORMAL/PRIMARY/STANDBY)。

svr\_status: 输出参数，输出库状态(Startup/AFTER Redo/Mount/Open/SUSPEND/Shutdown)。

arch\_type: 输出参数，输出库上配置的归档类型（REALTIME/TIMELY）

arch\_status: 输出参数，指定待获取的库为实时备库或即时备库时，输出组中主库到此备库的归档状态，如果是异步备库，则输出为“NULL”，如果是主库，则输出“VALID”。

pmnt\_magic: 输出参数，输出数据库永久魔数。

db\_magic: 输出参数，输出数据库魔数。

n\_ep: 输入输出参数，指定库中包含的节点实例个数。输入参数：可获取的最大实例个数，输出参数：实际获取到的实例个数，建议输入值不小于 16，避免获取不到完整信息。

ep\_seqno\_arr: 输出参数，输出指定库中所有实例的 seqno 数组，参数是 msint2 数组类型，数组长度是 n\_ep 的输入值。

ep\_name\_arr:m 输出参数，输出指定库中所有实例的实例名数组，参数是字符串指针数组类型，数组长度是 n\_ep 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免长度溢出。

dsc\_ctl\_node: 输出参数，输出指定库中控制节点的 seqno，对单节点库，输出值为 0。

dsc\_status: 输出参数，输出指定库的状态。

n\_ok\_ep: 输入输出参数，指定库中包括的 ok 节点实例个数。输入参数：可获取的最大实例个数，输出参数：实际获取到的实例个数，建议输入值不小于 16，避免获取不到完整信息。对单节点库，输出值为 1。

ok\_ep\_arr: 输出参数，输出指定库中所有 ok 节点实例的 seqno 数组，参数是 msint2 数组类型 数组长度是 n\_ok\_ep 的输入值。

n\_break\_ep: 输入输出参数，指定库中当前正在故障处理的节点数。输入参数：可获取的最大实例个数，输出参数：实际获取到的实例个数，建议输入值不小于 16，避免获取不到完整信息。

break\_ep\_arr: 输出参数，输出指定库中当前正在故障处理的节点 seqno 数组，参数是 msint2 数组类型，数组长度是 n\_break\_ep 的输入值。

**返回值：**

0：执行成功。

<0：执行失败。

#### 16.dwmon\_get\_database\_info

**函数原型：**

```
DWMON_RETURN
dwmon_get_database_info(
    mhandle         mhdle,
    mschar*         group_name,
    mschar*         db_name,
    msint2*         n_ep,
    msint2*         ep_seqno_arr,
    mschar**        ep_name_arr,
    msint2*         dsc_ctl_node,
    mschar*         dsc_status,
    msint2*         n_ok_ep,
    msint2*         ok_ep_arr,
    msint2*         n_break_ep,
    msint2*         break_ep_arr
);
```

**功能说明：**

获取指定库上的实例信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取实例信息的数据库名称。

n\_ep: 输入输出参数，指定库中包含的节点实例个数。输入参数：可获取的最大实例个数，输出参数：实际获取到的实例个数，建议输入值不小于 16，避免获取不到完整信息。

ep\_seqno\_arr: 输出参数，输出指定库中所有实例的 seqno 数组，参数是 msint2 数组类型，数组长度是 n\_ep 的输入值。

ep\_name\_arr: 输出参数，输出指定库中所有实例的实例名数组，参数是字符串指针数组类型，数组长度是 n\_ep 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免长度溢出。

dsc\_ctl\_node: 输出参数，输出指定库中控制节点的 seqno，对单节点库，输出值为 0。

dsc\_status: 输出参数，输出指定库的状态。

n\_ok\_ep: 输入输出参数，指定库中包括的 ok 节点实例个数。输入参数：可获取的最大实例个数，输出参数：实际获取到的实例个数，建议输入值不小于 16，避免获取不到完整信息。对单节点库，输出值为 1。

ok\_ep\_arr: 输出参数，输出指定库中所有 ok 节点实例的 seqno 数组，参数是 msint2 数组类型，数组长度是 n\_ok\_ep 的输入值。

n\_break\_ep: 输入输出参数，指定库中当前正在故障处理的节点数。输入参数：可获取的最大 例个数，输出参数：实际获取到的实例个数，建议输入值不小于 16，避免获取不到完整信息。

break\_ep\_arr: 输出参数，输出指定库中当前正在故障处理的节点 seqno 数组，参数是 msint2 数组类型，数组长度是 n\_break\_ep 的输入值。

**返回值：**

0：执行成功。

<0：执行失败。

#### 17.dwmon\_get\_nth\_ep\_info

**函数原型：**

```
DWMON_RETURN

dwmon_get_nth_ep_info(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    muint4 nth,

    mschar* ep_name,

    muint4* ep_port,

    mschar* ep_ok_str,

    mschar* svr_mode,

    mschar* svr_status,

    mschar* prim_inst,

    mschar* prim_mal_sta,

    mschar* prim_arch_type,

    mschar* prim_arch_sta,

    muint8* fseq,

    muint8* flsn,

    muint8* cseq,

    muint8* clsn,

    mschar* arch_type,

    muint4* n_arch,

    muint4* n_async,

    msint2* dsc_seqno,

    mschar* g_dw_status,

    mbyte* mpp_flag_mem,

    mbyte* mpp_flag_file

);
```

**功能说明：**

获取指定库上第 nth 个实例信息，可先通过 dwmon\_get\_database\_info 接口获取到库上的节点实例个数 n\_ep，nth 取值范围为\[0, n\_ep–1\]。

**参数说明：**

对字符串类型的输出参数，指向的缓存长度不能小于 65，避免溢出。

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取实例信息的数据库名称，此参数必须指定。

nth: 输入参数，指定要获取 inst\_name 库上的第 nth 个实例信息。

ep\_name: 输出参数，输出第 nth 个实例名称。

ep\_port: 输出参数，输出实例端口号。

ep\_ok\_str: 输出参数，输出守护进程认定的实例状态(Ok/Error)。

svr\_mode: 输出参数，输出实例模式(Normal/PRIMARY/STANDBY)。

svr\_status: 输出参数，输出实例状态(Startup/After Redo/Mount/Open/ Suspend/Shutdown)。

prim\_inst: 输出参数，当前实例是 STANDBY 模式时该字段才有意义，输出对应的 PRIMARY 实例名，如果是 PRIMARY 模式，则输出为空。

prim\_mal\_sta: 输出参数，当前实例是 STANDBY 模式时该字段才有意义，输出主库控制节点到当前库的控制节点之间的 mal 链路状态。

prim\_arch\_type: 输出参数，当前实例是 STANDBY 模式时该字段才有意义，输出主库到当前实例的归档类型，包括 REALTIME/TIMELY/ASYNC 这三种类型。

prim\_arch\_sta: 输出参数，当前实例是 STANDBY 模式时该字段才有意义，输出主库控制节点到当库的控制节点的归档状态，local 守护类型的除外。

fseq: 输出参数，输出实例的 file\_pkg\_seq 值。

flsn: 输出参数，输出实例的 flsn 值。

cseq: 输出参数，输出实例的 cur\_pkg\_seq 值。

clsn: 输出参数，输出实例的 clsn 值。

arch\_type: 输出参数，输出实例自身配置的归档类型，只统计 REALTIME/TIMELY 这两种归档类型，不考虑本地 LOCAL 归档类型。

n\_arch: 输出参数，输出实例自身配置的归档个数，只统计 REALTIME/TIMELY 这两种归档类型下配置的归档个数。

n\_async: 输出参数，输出实例自身配置的异步归档个数。

dsc\_seqno: 输出参数，对 DMDSC 集群才有意义，输出实例在集群中的 seqno 序号。

g\_dw\_status: 输出参数，输出实例上设置的守护进程执行标记。

mpp\_flag\_mem: 输出参数，输出实例内存中的 mpp\_ini 值。

mpp\_flag\_file: 输出参数，输出实例 dm.ini 中配置的 mpp\_ini 值。

**返回值：**

0：执行成功。

<0：执行失败。

#### 18.dwmon\_get\_ep\_info\_by\_name

**函数原型：**

```
DWMON_RETURN

dwmon_get_ep_info_by_name(

    mhandle mhdle,

    mschar* group_name,

    mschar* ep_name,

    muint4* ep_port,

    mschar* ep_ok_str,

    mschar* svr_mode,

    mschar* svr_status,

    mschar* prim_inst,

    mschar* prim_mal_sta,

    mschar* prim_arch_type,

    mschar* prim_arch_sta,

    muint8* fseq,

    muint8* flsn,

    muint8* cseq,

    muint8* clsn,

    mschar* arch_type,

    muint4* n_arch,

    muint4* n_async,

    msint2* dsc_seqno,

    mschar* g_dw_status,

    mbyte* mpp_flag_mem,

    mbyte* mpp_flag_file

);
```

**功能说明：**

根据指定的实例名获取实例的详细信息。

**参数说明：**

对字符串类型的输出参数，指向的缓存长度不能小于 65，避免溢出。

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，输入指定实例所在的守护进程组名，如果只有一组可以不指定。

ep\_name: 输入参数，输入要获取信息的实例名。

ep\_port: 输出参数，输出实例端口号。

ep\_ok\_str: 输出参数，输出守护进程认定的实例状态(Ok/Error)。

svr\_mode: 输出参数，输出实例模式(Normal/PRIMARY/STANDBY)。

svr\_status: 输出参数，输出实例状态(Startup/After Redo/Mount/Open/Suspend/Shutdown)。

prim\_inst: 输出参数，当前实例是 STANDBY 模式时该字段才有意义，输出对应的 PRIMARY 实例名，如果是 PRIMARY 模式，则输出为空。

prim\_mal\_sta: 输出参数，当前实例是 STANDBY 模式时该字段才有意义，输出主库控制节点到当前库的控制节点之间的 mal 链路状态。

prim\_arch\_type: 输出参数，当前实例是 STANDBY 模式时该字段才有意义，输出主库到当前实例的归档类型，包括 REALTIME/TIMELY/ASYNC 这三种类型。

prim\_arch\_sta: 输出参数，当前实例是 STANDBY 模式时该字段才有意义，输出主库控制节点到当前库的控制节点的归档状态，local 守护类型的除外。

fseq: 输出参数，输出实例的 file\_pkg\_seq 值。

flsn: 输出参数，输出实例的 flsn 值。

cseq: 输出参数，输出实例的 cur\_pkg\_seq 值。

clsn: 输出参数，输出实例的 clsn 值。

arch\_type: 输出参数，输出实例自身配置的归档类型，只统计 REALTIME/TIMELY 这两种归档类型，不考虑本地 LOCAL 归档类型。

n\_arch: 输出参数，输出实例自身配置的归档个数，只统计 REALTIME/TIMELY 这两种归档类型下配置的归档个数。

n\_async: 输出参数，输出实例自身配置的异步归档个数。

dsc\_seqno: 输出参数，对 DMDSC 集群才有意义，输出实例在集群中的 seqno 序号。

g\_dw\_status: 输出参数，输出实例上设置的守护进程执行标记。

mpp\_flag\_mem: 输出参数，输出实例内存中的 mpp\_ini 值。

mpp\_flag\_file: 输出参数，输出实例 dm.ini 中配置的 mpp\_ini 值。

**返回值：**

0：执行成功。

<0：执行失败。

#### 19.dwmon\_get\_database\_arch\_info

**函数原型：**

```
DWMON_RETURN

dwmon_get_database_arch_info(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    mschar* arch_type,

    muint4* n_arch,

    mschar** arch_dest,

    mschar** mal_sta,

    mschar** arch_sta,

    muint4* n_async,

    mschar** async_dest,

    mschar** async_mal_sta

);
```

**功能说明：**

获取指定库配置的归档信息，包括归档目标实例名，到归档目标的 mal 链路状态和归档状态，以及异步归档信息。

**参数说明：**

arch\_dest、mal\_sta、arch\_sta、async\_dest 和 async\_mal\_sta 都是字符串指针数组类型，其中 arch\_dest、mal\_sta 和 arch\_sta 的数组长度是 n\_arch 的输入值，async\_dest 和 async\_mal\_sta 的数组长度是 n\_async 的输入值，建议 n\_arch 和 n\_async 的输入值不小于 8，避免取不到完整信息。

如果归档目标是 DMDSC 集群，则 arch\_dest、async\_dest 会输出完整的归档配置串（比如“DSC01/DSC02”），为避免发生溢出，arch\_dest 和 async\_dest 数组中的每个指针元素指向的缓存长度不能小于 272。除此之外，其他字符串指针数组中的指针元素指向的缓存长度不能小于 65，避免溢出。

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取归档信息的数据库名称。

arch\_type: 输出参数，输出指定库配置的归档类型，只检查 REALTIME/TIMELY 这两种归档类型，注意缓存长度不能小于 65，避免溢出。

n\_arch: 输入输出参数，指定库配置的归档个数，只检查 REALTIME/TIMELY 这两种归档类型。输入参数：指定可获取的最大归档个数，输出参数：实际获取的归档个数，建议输入值不小于 8，避免取不到完整信息。

arch\_dest: 输出参数，输出指定库配置的归档目标名称，只检查 REALTIME/TIMELY 这两种归档类型，如果归档目标是 DMDSC 集群，则输出完整的归档配置串（形如“DSC01/DSC02”），为避免发生溢出，arch\_dest 数组中的每个指针元素指向的缓存长度不能小于 272。

mal\_sta: 输出参数，输出指定库的控制节点到每个归档目标控制节点的 mal 链路状态数组，只检查 REALTIME/TIMELY 这两种归档类型，如果未找到控制节点，则输出“UNKNOWN”。

arch\_sta： 输出参数，输出指定库的控制节点到每个归档目标控制节点的归档状态数组，指定实例是 PRIMARY 模式时，该参数输出的是有效值，只检查 REALTIME/TIMELY 这两种归档类型。

n\_async: 输入输出参数，指定库配置的异步归档个数。输入参数：指定可获取的最大归档个数，输出参数：实际获取的归档个数，建议输入值不小于 8，避免取不到完整信息。

async\_dest: 输出参数，输出指定库配置的异步归档目标名称，如果归档目标是 DMDSC 集群，则输出完整的归档配置串（形如“DSC01/DSC02”），为避免发生溢出，async\_dest 数组中的每个指针元素指向的缓存长度不能小于 272。

async\_mal\_sta：输出参数，输出指定库的控制节点到每个异步归档目标控制节点的 mal 链路状态数组。

**返回值：**

0：执行成功。

<0：执行失败。

#### 20.dwmon\_get\_watch\_ctl\_info

**函数原型：**

```
DWMON_RETURN

dwmon_get_watch_ctl_info(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    mschar* ctl_status,

    mschar* desc

);
```

**功能说明：**

获取指定库的守护进程控制文件状态信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取控制文件信息的守护进程对应的数据库名称。

ctl\_status: 输出参数，输出守护进程控制文件状态，注意缓存长度不能小于 65，避免溢出。

desc: 输出参数，输出本地分裂库的描述信息，如果是有效状态，描述信息为空。注意缓存长度不能小于 513，避免溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 21.dwmon\_get\_database\_open\_history

**函数原型：**

```
DWMON_RETURN

dwmon_get_database_open_history(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    muint4* n_item

);
```

**功能说明：**

获取指定库的 OPEN 记录项个数。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取 OPEN 记录的守护进程对应的数据库名称。

n\_item: 输出参数，输出 db\_name 指定的库的 OPEN 记录项个数。

**返回值：**

0：执行成功。

<0：执行失败。

#### 22.dwmon\_get\_nth\_open\_history

**函数原型：**

```
DWMON_RETURN

dwmon_get_nth_open_history(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    muint4 nth,

    mschar* tguid,

    muint8* rowid,

    mschar* time,

    mschar* sys_mode,

    mschar* p_db_name,

    mschar* c_db_name,

    muint4* p_db_magic,

    muint4* c_db_magic,

    msint2* n_ep,

    muint8* aseq_arr,

    muint8    * alsn_arr

);
```

**功能说明：**

获取指定组中指定库的第 nth 个 open 记录信息。

**参数说明：**

> **注意**
> 
> 对字符串类型的输出参数，指向的缓存长度不能小于65，避免溢出。

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定的守护进程组名，只有一组时可以不指定。

db\_name: 输入参数，指定要获取信息的数据库名称。

nth: 输入参数，输入要获取指定第 nth 个 OPEN 记录项。

tguid: 输出参数，输出 OPEN 记录唯一标识。

rowid: 输出参数，输出系统表所在行的 rowid 值。

time: 输出参数，输出 OPEN 的时间点。

sys\_mode: 输出参数，输出 OPEN 时所处的系统模式（PRIMARY/NORMAL）。

p\_db\_name: 输出参数，输出对应主库的实例名。

c\_db\_name: 输出参数，输出当前库的实例名。

p\_db\_magic: 输出参数，输出对应主库的 db\_magic 值。

c\_db\_magic: 输出参数，输出当前库的 db\_magic 值。

n\_ep: 输入输出参数，指定库中包含的节点实例个数。输入参数：可获取的最大实例个数，输出参数：实际获取到的实例个数，建议输入值不小于 16，避免获取不到完整信息。

aseq\_arr: 输出参数，输出 pkg\_seqno 数组，长度不能小于 16。

alsn\_arr: 输出参数，输出 apply\_lsn 数组，长度不能小于 16.

#### 23.dwmon\_get\_watch\_config\_info

\*\*函数原型： \*\*

```
DWMON_RETURN
dwmon_get_watch_config_info(
    mhandle     mhdle,
    mschar*     group_name,
    mschar*     inst_name,
    mschar*     dw_type,
    mschar*     dw_mode,
    muint4*     dw_error_time,
    muint4*     inst_oguid,
    muint4*     inst_error_time,
    muint4*     inst_recover_time,
    mschar*     inst_ini,
    mschar*     dcr_ini,
    muint4*     inst_auto_restart,
    mschar*     inst_startup_cmd,
    muint4*     inst_host_check,
    muint4*     rlog_send_threshold,
    muint4*     rlog_apply_threshold,
    mschar*        dcs_startup_cmd,
    mschar*        dcs_ini,
    muint4*        dcs_port
);
```

**功能说明：**

获取指定实例本地的守护进程配置信息。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name:输入输出参数，当前有多个组时，作为输入参数，指定实例所在的守护进程组名，只有一组时允许不指定，如果组名为空串，则作为输出参数，输出实例所在的守护进程组名，输出缓存长度不能小于 65，避免长度溢出。

inst\_name: 输入参数，指定要获取配置信息的守护进程本地的实例名。

dw\_type：输出参数，输出 dmwatcher.ini 的 dw\_type 配置值，注意缓存长度不能小于 65，避免溢出。

dw\_mode：输出参数，输出 dmwatcher.ini 的 dw\_mode 配置值，注意缓存长度不能小于 65，避免溢出。

dw\_error\_time：输出参数，输出 dmwatcher.ini 的 dw\_error\_time 配置值。

inst\_oguid：输出参数，输出 dmwatcher.ini 的 inst\_oguid 配置值。

inst\_error\_time：输出参数，输出 dmwatcher.ini 的 inst\_error\_time 配置值。

inst\_recover\_time：输出参数，输出 dmwatcher.ini 的 inst\_recover\_time 配置值。

inst\_ini：输出参数，输出 dmwatcher.ini 的 inst\_ini 配置值，注意缓存长度不能小于 257，避免溢出。

dcr\_ini：输出参数，输出 dmwatcher.ini 的 dcr\_ini 配置值（守护 DMDSC 集群时需要配置），注意缓存长度不能小于 257，避免溢出。

inst\_auto\_restart：输出参数，输出 dmwatcher.ini 的 inst\_auto\_restart 配置值。

inst\_startup\_cmd：输出参数，输出 dmwatcher.ini 的 inst\_startup\_cmd 配置值，注意缓存长度不能小于 257，避免溢出。

inst\_host\_check：输出参数，输出守护进程是否检查实例对外服务 IP 的网卡故障，0 表示不检查，1 表示检查。

rlog\_send\_threshold：输出参数，输出主库发送日志到备库的时间阈值。

rlog\_apply\_threshold：输出参数，输出备库重演日志的时间阈值。

dcs\_startup\_cmd：输出参数，输出 dmwatcher.ini 的 dcs\_startup\_cmd 配置值，注意缓存长度不能小于 257，避免溢出。该参数已废弃，输出值无实际意义。

dcs\_ini：输出参数，输出 dmwatcher.ini 的 dcs\_ini 配置值，注意缓存长度不能小于 257，避免溢出。该参数已废弃，输出值无实际意义。

dcs\_port：输出参数，输出 dmwatcher.ini 的 dcs\_port 配置值。该参数已废弃，输出值无实际意义。

**返回值：**

0：执行成功。

<0：执行失败。

#### 24.dwmon\_get\_css\_config\_info

**函数原型：**

```
DWMON_RETURN

dwmon_get_css_config_info(

    mhandle mhdle,

    mschar* group_name,

    mschar* inst_name,

    muint4* asm_restart_itvl,

    muint4* db_restart_itvl

);
```

**功能说明：**

获取和指定实例的 dcr\_seqno 相同的 dmcss 配置的自动拉起检测间隔（DMDCR\_ASM\_RESTART\_INTERVAL、DMDCR\_DB\_RESTART\_INTERVAL）。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入输出参数，不能为空，只有一组时允许不指定组名，输入组名为空串的情况下，接口会输出实例所在的守护进程组名，输出缓存长度不能小于 65，避免长度溢出。

inst\_name: 输入参数，指定要获取配置信息的实例名。

asm\_restart\_itvl: 输出参数，输出实例本地的 dmcss 配置文件（dmdcr.ini）中配置的 dmasmsvr 自动拉起检测间隔（DMDCR\_ASM\_RESTART\_INTERVAL）。

db\_restart\_itvl: 输出参数，输出实例本地的 dmcss 配置文件（dmdcr.ini）中配置的 DMServer 自动拉起检测间隔（DMDCR\_DB\_RESTART\_INTERVAL）。

**返回值：**

0：执行成功。

<0：执行失败。

#### 25.dwmon\_get\_monitor\_info

**函数原型：**

```
DWMON_RETURN

dwmon_get_monitor_info (

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    muint4* n_mon,

    mschar** conn_time_arr,

    muint4* confirm_arr,

    muint8* mid_arr,

    mschar** mon_ip_arr,

    mschar** mon_version_arr

)
```

**功能说明：**

获取指定守护进程的监视器连接信息。同一个守护系统中允许最多 10 个监视器同时启动连接到守护进程，可通过调用此接口获取指定守护进程上的监视器连接信息，包括连接时间、确认监视器配置、监视器 ID、监视器 IP 和监视器版本信息。

其中 db\_name 是输入输出参数，表示指定守护进程对应的实例名，如果此参数为空，则根据 dmmonitor.ini 对应组中的配置顺序，选择第一个活动的守护进程获取监视器连接信息，并输出选中的守护进程本地库名称；如果指定有合法值，则返回指定库的控制守护进程上的监视器连接信息。

另外输出的数组参数中第一个数组元素存放的是本地监视器的连接信息。

**参数说明：**

conn\_time\_arr 和 mon\_ip\_arr 是字符串指针数组类型，数组长度不能小于 10，每个数组中的指针元素指向的缓存长度不能小于 65，避免溢出。

mon\_version\_arr 也是字符串指针数组类型，数组长度不能小于 10，每个数组中的指针元素指向的缓存长度不能小于 129，避免溢出。

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入输出参数，指定要获取信息的守护进程对应的实例名，在 db\_name 为空串的情况下，会作为输出参数输出实际获取信息的实例名，此时缓存长度不能小于 65，避免输出时长度溢出。

n\_mon: 输入输出参数，指定守护进程上连接的监视器总个数。输入参数：可获取的最大个数，输出参数：实际获取的个数，建议输入值不小于 10，避免取不到完整信息。

conn\_time\_arr: 输出参数，输出守护进程上建立连接的时间，数组长度是 n\_mon 的输入值。

confirm\_arr: 输出参数，输出监视器的确认配置信息，参数为 muint4 数组类型，数组长度是 n\_mon 的输入值。

mid\_arr: 输出参数，输出监视器的唯一 ID，参数为 muint8 数组类型，数组长度是 n\_mon 的输入值。

mon\_ip\_arr: 输出参数，输出监视器的 IP 地址，数组长度是 n\_mon 的输入值。

mon\_version\_arr：输出参数，输出监视器的版本信息，数组长度是 n\_mon 的输入值。

**返回值：**

0：执行成功。

<0：执行失败。

#### 26.dwmon\_set\_cmd\_execing\_with\_command

**函数原型：**

```
DWMON_RETURN

dwmon_set_cmd_execing_with_command (

    mhandle mhdle,

    mschar* command

);
```

**功能说明：**

如果上层有控制台工具界面，通过用户输入命令的方式调用接口，可通过此接口设置命令执行标记并传入用户执行的命令串信息，用于监视器 log 日志记录用户的操作信息。

在确认监视器模式下或者监视器设置有自动记录系统状态间隔（通过 dwmon\_set\_show\_interval 或者 dwmon\_set\_log\_interval 设置），调用命令接口之前，需要先调用此接口设置执行标记，避免和确认监视器自动接管故障主库或者监视器自动记录系统状态的操作发生并发冲突。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

command: 输入参数，如果上层有控制台工具界面，则表示用户手工输入的执行命令串，允许为 NULL 或空串。

**返回值：**

0：执行成功。

<0：执行失败。

#### 27.dwmon\_reset\_cmd\_execing

**函数原型：**

```
DWMON_RETURN

dwmon_reset_cmd_execing(

    mhandle mhdle

);
```

**功能说明：**

重置命令执行标记，和 dwmon\_set\_cmd\_execing\_with\_command 接口配合使用，在调用命令接口执行完成后，需要调用此接口，重置执行标记，避免确认监视器无法执行自动接管故障主库的操作。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

0：执行成功。

<0：执行失败。

#### 28.dwmon\_get\_dw\_confirm

**函数原型：**

```
DWMON_RETURN

dwmon_get_dw_confirm(

    mhandle mhdle,

    mbool* dw_confirm

)
```

**功能说明：**

获取确认监视器标记，用于判断当前的监视器是否为确认监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄

dw\_confirm: 输出参数，输出确认监视器标记，1：是确认监视器， 0：不是确认监视器。

**返回值：**

0：执行成功。

<0：执行失败。

#### 29.dwmon\_set\_show\_interval

**函数原型：**

```
DWMON_RETURN

dwmon_set_show_interval(

    mhandle mhdle,

    muint4 show_interval

)
```

**功能说明：**

设置自动显示间隔。监视器根据指定的 show\_interval 值，每隔 show\_interval 个时间间隔，自动输出各实例的状态信息给用户，需要使用 dwmon\_get\_exec\_msg 接口获取到输出消息，show\_interval 单位为秒，默认值为 0。

**参数说明：**

mhdle: 输入参数，监视器操作句柄

show\_interval: 输入参数，设置定时输出状态信息的时间间隔，单位为秒，取值范围为 0，或 5~3600，取值为 0 表示取消自动输出，缺省值为 0。

**返回值：**

0：执行成功。

<0：执行失败。

#### 30.dwmon\_get\_show\_interval

**函数原型：**

```
DWMON_RETURN

dwmon_get_show_interval(

    mhandle mhdle,

    muint4* show_interval

);
```

**功能说明：**

获取当前设置的自动显示时间间隔，单位为秒。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

show\_interval: 输出参数，输出当前设置的自动显示时间间隔。

**返回值：**

0：获取成功。

<0：获取失败。

#### 31.dwmon\_set\_log\_interval

**函数原型：**

```
DWMON_RETURN

dwmon_set_log_interval(

    mhandle mhdle,

    muint4 log_interval

);
```

**功能说明：**

设置自动写入日志文件间隔。监视器按照设置的 log\_interval 值，每隔 log\_interval 个时间间隔，自动将各实例的状态信息写入到日志文件，log\_interval 单位为秒，缺省值为 1。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

log\_interval: 输入参数，设置定时写入状态信息到日志文件的时间间隔，单位为秒，取值为 0，1 或 5~3600。

取值为 0 表示不写入任何信息到日志文件。

取值为 1 表示只写入普通的状态变化日志，例如收到新的信息或者检测到状态变化等。

取值为 5~3600 范围内的数值时，除了生成普通日志信息外，会按照设置的间隔定期写入站点状态信息到日志文件中。

**返回值：**

0：执行成功。

<0：执行失败。

#### 32.dwmon\_get\_log\_interval

**函数原型：**

```
DWMON_RETURN

dwmon_get_log_interval(

    mhandle mhdle,

    muint4* log_interval

)
```

**功能说明：**

获取当前设置的自动写入日志的时间间隔，单位为秒。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

log\_interval：输出参数，输出当前设置的时间间隔。

**返回值：**

0：执行成功。

<0：执行失败。

#### 33.dwmon\_set\_log\_file\_size

**函数原型：**

```
DWMON_RETURN

dwmon_set_log_file_size(

    mhandle mhdle,

    muint4 log_file_size

)
```

**功能说明：**

设置监视器单个的日志文件大小，达到最大值后，会自动生成并切换到新的日志文件中，如果达到最大的日志总空间限制，会自动删除创建时间最早的日志文件，日志文件命名方式为“dmmonitor\_年月日时分秒.log”，例如“dmmonitor\_20160201155820.log”。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

log\_file\_size: 输入参数，设置单个日志文件大小，单位为 M，取值范围为 16~2048，缺省值为 64。

**返回值：**

0：执行成功。

<0：执行失败。

#### 34.dwmon\_get\_log\_file\_size

**函数原型：**

```
DWMON_RETURN

dwmon_get_log_file_size(

    mhandle mhdle,

    muint4* log_file_size

);
```

**功能说明：**

获取当前设置的单个日志文件大小，单位为 M。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

log\_file\_size: 输出参数，输出当前设置的单个日志文件大小。

**返回值：**

0：执行成功。

<0：执行失败。

#### 35.dwmon\_get\_log\_path

**函数原型：**

```
DWMON_RETURN

dwmon_get_log_path(

    mhandle mhdle,

    mschar* log_path

);
```

**功能说明：**

获取当前的日志文件路径。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

log\_path: 输出参数，输出当前的日志文件路径，log\_path 的缓存长度不能小于 257，避免溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 36.dwmon\_set\_log\_space\_limit

**函数原型：**

```
DWMON_RETURN

dwmon_set_log_space_limit(

    mhandle mhdle,

    muint4 log_space_limit

);
```

**功能说明：**

调用此接口，可以设置监视器的日志总空间大小，达到设置的总空间大小后，会自动删除创建时间最早的日志文件。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

log\_space\_limit: 输入参数，设置日志总空间大小，单位为 M，取值为 0 或 256~4096，缺省值为 0，表示没有空间限制。

**返回值：**

0：执行成功。

<0：执行失败。

#### 37.dwmon\_get\_log\_space\_limit

**函数原型：**

```
DWMON_RETURN

dwmon_get_log_space_limit(

    mhandle mhdle,

    muint4* log_space_limit

);
```

**功能说明：**

获取当前设置的日志总空间大小，单位为 M。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

log\_space\_limit：输出参数，输出当前设置的日志总空间大小。

**返回值：**

0：执行成功。

<0：执行失败。

#### 38.dwmon\_login

**函数原型：**

```
DWMON_RETURN

dwmon_login(

    mhandle mhdle,

    mschar* username,

    mschar* password

);
```

**功能说明：**

登录监视器，这里的登录口令和服务器的登录口令是一致的，且必须有 DBA 权限。

校验登录信息时由守护进程转发给服务器校验，并返回校验结果给监视器，因此需要保证系统中至少有一个活动库，否则无法校验成功。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

username: 输入参数，登录用户名。

password: 输入参数，登录密码。

**返回值：**

0：执行成功。

<0：执行失败。

#### 39\. dwmon\_login\_with\_key

**函数原型：**

```
DWMON_RETURN
dwmon_login_with_key(
  mhandle     mhdle,
  mschar*     login_str  
);
```

**功能说明：**

Key 认证方式登录监视器。

**参数说明：**

mhdle：输入参数，监视器操作句柄。

login\_str：输入参数，登录连接串。

**返回值：**

0：执行成功。

<0：执行失败。

#### 40.dwmon\_logout

**函数原型：**

```
DWMON_RETURN

dwmon_logout(

    mhandle mhdle

);
```

**功能说明：**

退出登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

0：执行成功。

<0：执行失败。

#### 41.dwmon\_set\_database\_recover\_time

**函数原型：**

```
DWMON_RETURN

dwmon_set_database_recover_time(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    muint4 recover_time

);
```

**功能说明：**

设置指定备库的恢复间隔时间，设置成功后，recover\_time 值保存在对应主库的守护进程内存中，并且只对指定的备库起作用。

此接口只允许对指定备库执行修改操作，如果需要考虑对某个组或所有组中的备库执行修改操作，则可以使用 dwmon\_set\_group\_recover\_time 接口来实现。

执行此操作需要先登录监视器。

**参数说明：**

mhdle：输入参数，监视器操作句柄。

group\_name：输入参数，指定执行操作的守护进程组名，只有一组时可以不指定组名。

db\_name：输入参数，指定要设置恢复间隔时间的备库实例名。

recover\_time：输入参数，指定要设置的恢复间隔时间，单位秒，取值范围 3~86400，详细说明可参考 [3.1.9 故障恢复处理](data-watch-daemon.md) 。

**返回值：**

0：执行成功。

<0：执行失败。

#### 42.dwmon\_set\_database\_arch\_invalid

**函数原型：**

```
DWMON_RETURN

dwmon_set_database_arch_invalid(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

设置主库到指定备库的归档状态无效。

此接口只允许对指定备库设置归档无效，如果需要考虑对某个组或所有组中的备库执行设置操作，则可以使用 dwmon\_set\_group\_arch\_invalid 接口来实现。

执行此操作需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定执行操作的守护进程组名，只有一组时可以不指定组名。

db\_name：输入参数，指定要修改归档状态无效的备库实例名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 43.dwmon\_startup\_database\_watch

**函数原型：**

```
DWMON_RETURN

dwmon_startup_database_watch(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

打开指定库的守护进程监控功能，守护进程启动后，默认监控功能处于打开状态。

对 DMDSC 集群，此接口只通知控制守护进程执行。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要打开监控的守护进程组名，只有一组时可以不指定组名。

db\_name:输入参数，指定要打开监控的守护进程所在的本地实例名称。

**返回值：**

\>=0：执行成功，执行前组中所有守护进程的监控已经处于打开状态时，返回值为 100。

<0：执行失败。

#### 44.dwmon\_startup\_watch

**函数原型：**

```
DWMON_RETURN

dwmon_startup_watch(

    mhandle mhdle,

    mschar* group_name

);
```

**功能说明：**

打开指定组的守护进程监控功能，守护进程启动后，默认监控功能处于打开状态。

对 DMDSC 集群，此接口只通知控制守护进程执行。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要打开监控的守护进程组名，只有一组时可以不指定组名。

**返回值：**

\>=0：执行成功，执行前组中所有守护进程的监控已经处于打开状态时，返回值为 100。

<0：执行失败。

#### 45.dwmon\_startup\_watch\_all

**函数原型：**

```
DWMON_RETURN

dwmon_startup_watch_all(

    mhandle mhdle

);
```

**功能说明：**

打开所有组的守护进程监控功能，守护进程启动后，默认监控功能处于打开状态。

只有 MPP 主备环境允许调用此接口。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

\>=0：执行成功，执行前执行库的守护进程的监控已经处于打开状态时，返回值为 100。

<0：执行失败。

#### 46.dwmon\_stop\_database\_watch

**函数原型：**

```
DWMON_RETURN

dwmon_stop_database_watch(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

关闭指定库的守护进程的监控功能，监控功能被关闭后，守护进程还可以正常地接收和发送消息，但无法根据当前的实例状态来自动处理故障以及实例的自动拉起等，关闭后守护进程处于 Shutdown 状态。

如果需要正常地退出实例或者保持实例为 Mount 状态，则可以关闭监控功能，否则建议保持监控功能为打开状态，以保证能够及时处理系统的各种情况。

对 DMDSC 集群，此接口只通知控制守护进程执行。

执行此操作需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要关闭监控的守护进程组名，只有一组时可以不指定组名。

db\_name：输入参数，指定要关闭监控的守护进程的本地实例名。

**返回值：**

\>=0：指定库的守护进程的监控关闭成功。执行前守护进程的监控已经处于关闭状态时，返回值为 100。

<0：执行失败。

#### 47.dwmon\_stop\_watch

**函数原型：**

```
DWMON_RETURN

dwmon_stop_watch(

    mhandle mhdle,

    mschar* group_name

);
```

**功能说明：**

关闭指定组的所有守护进程的监控功能，监控功能被关闭后，守护进程还可以正常地接收和发送消息，但无法根据当前的实例状态来自动处理故障以及实例的自动拉起等，关闭后守护进程处于 Shutdown 状态。

如果需要正常地退出实例或者保持实例为 Mount 状态，则可以关闭监控功能，否则建议保持监控功能为打开状态，以保证能够及时处理系统的各种情况。

对 DMDSC 集群，此接口只通知控制守护进程执行。

执行此操作需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要关闭监控的守护进程组名，只有一组时可以不指定组名。

**返回值：**

\>=0：所有守护进程的监控关闭成功。执行前组中所有守护进程的监控已经处于关闭状态时，返回值为 100。

<0：执行失败

#### 48.dwmon\_stop\_watch\_all

**函数原型：**

```
DWMON_RETURN

dwmon_stop_watch_all(

    mhandle mhdle

);
```

**功能说明：**

关闭所有组的守护进程监控功能，监控功能被关闭后，守护进程还可以正常地接收和发送消息，但无法根据当前的实例状态来自动处理故障以及实例的自动拉起等，关闭后守护进程处于 Shutdown 状态。

如果需要正常地退出实例或者保持实例为 Mount 状态，则可以关闭监控功能，否则建议保持监控功能为打开状态，以保证能够及时处理系统的各种情况。

执行此操作需要先登录监视器，只有 MPP 主备环境下允许调用此接口。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

\>=0：所有守护进程的监控关闭成功，执行前所有组守护进程的监控已经处于关闭状态时，返回值为 100。

<0：执行失败。

#### 49.dwmon\_startup\_group

**函数原型：**

```
DWMON_RETURN

dwmon_startup_group(

    mhandle mhdle,

    mschar* group_name

);
```

**功能说明：**

启动指定组的所有实例，在 dmwatcher.ini 中 INST\_AUTO\_RESTART 配置为 0 时该接口可以成功执行，配置为 1 时在守护进程的监控功能打开的情况下，守护进程可以自动完成启动实例的功能，不需要再调用接口执行。

对 DMDSC 集群，由 dmcss 执行拉起动作，和 dmwatcher.ini 中的 INST\_AUTO\_RESTART 配置参数没有关系，由 dmdcr.ini 中的配置参数决定是否可以执行自动拉起，如果某个实例可以被 dmcss 自动拉起，则 dmcss 会忽略收到的拉起命令，等待自动拉起。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要启动实例的守护进程组名，只有一组时可以不指定。

**返回值：**

\>=0：所有实例都启动成功，执行前组中所有实例已经处于活动状态时，返回值为 100。

<0：执行失败。

#### 50.dwmon\_startup\_group\_all

**函数原型：**

```
DWMON_RETURN

dwmon_startup_group_all(

    mhandle mhdle

);
```

**功能说明：**

启动所有组的实例，在 dmwatcher.ini 中 INST\_AUTO\_RESTART 配置为 0 时该接口可以成功执行，配置为 1 时在守护进程的监控功能打开的情况下，守护进程可以自动完成启动实例的功能，不需要再调用接口执行。

只有 MPP 主备环境下允许调用此接口。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

\>=0：所有实例都启动成功，执行前所有组的实例已经处于活动状态时，返回值为 100。

<0：执行失败。

#### 51.dwmon\_stop\_group

**函数原型：**

```
DWMON_RETURN

dwmon_stop_group(

    mhandle mhdle,

    mschar* group_name

);
```

**功能说明：**

关闭指定组中的所有活动实例，关闭所有活动实例之前，会先关闭所有控制守护进程的监控功能，避免守护进程将实例再次拉起。

对 DMDSC 集群，是由 dmcss 执行退出操作，在 dmcss 通知所有实例退出之前，会先关闭 dmcss 的自动拉起功能。执行此操作需要先登录监视器，另外关闭守护进程只是将守护进程切换为 Shutdown 状态，并没有退出。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要关闭实例的守护进程组名，只有一组时可以不指定。

**返回值：**

\>=0：所有实例都退出成功，执行前组中实例已经全部退出时，返回值为 100。

<0：执行失败。

#### 52.dwmon\_stop\_group\_all

**函数原型：**

```
DWMON_RETURN

dwmon_stop_group_all(

    mhandle mhdle

);
```

**功能说明：**

关闭所有组的所有活动实例，关闭实例之前，会先关闭所有守护进程的监控功能，避免守护进程将实例再次拉起。

只有 MPP 主备环境下允许调用此接口，执行此操作需要先登录监视器，另外关闭守护进程只是将守护进程切换为 Shutdown 状态，并没有退出。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

\>=0：所有实例都退出成功，执行前所有组的实例已经全部退出时，返回值为 100。

<0：执行失败。

#### 53.dwmon\_kill\_group

**函数原型：**

```
DWMON_RETURN

dwmon_kill_group(

    mhandle mhdle,

    mschar* group_name

);
```

**功能说明：**

强制杀掉指定组中的活动实例。

调用 dwmon\_stop\_group 关闭指定组的实例时，如果实例正在执行守护进程发起的命令，或者守护进程不是 STARTUP、OPEN 或 RECOVERY 状态，会导致接口执行失败，在这种情况下，如果需要强制关闭实例，则可以通过调用 dwmon\_kill\_group 接口来完成。

此接口执行时不要求先登录监视器，并且也会将守护进程切换为 Shutdown 状态（如果已经是 Shutdown 状态则跳过不再切换），避免守护进程将实例重新拉起。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要强杀实例的守护进程组名，只有一组时可以不指定。

**返回值：**

\>=0：所有实例都强杀成功，执行前组中实例已经全部退出并且守护进程都是 Shutdown 状态时返回值为 100。

<0：执行失败。

#### 54.dwmon\_kill\_group\_all

**函数原型：**

```
DWMON_RETURN

dwmon_kill_group_all(

    mhandle mhdle

);
```

**功能说明：**

强制杀掉所有组中的活动实例。

调用 dwmon\_stop\_group\_all 关闭所有组的实例时，如果实例正在执行守护进程发起的命令，或者守护进程不是 STARTUP、OPEN 或 RECOVERY 状态，会导致接口执行失败，在这种情况下，如果需要强制关闭实例，则可以通过调用 dwmon\_kill\_group\_all 接口来完成。

只有 MPP 主备环境下允许调用此接口，此接口执行时不要求先登录监视器，并且也会将守护进程切换为 Shutdown 状态（如果已经是 Shutdown 状态则跳过不再切换），避免守护进程将实例重新拉起。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

\>=0：所有实例都强杀成功，执行前所有组的实例已经全部退出并且守护进程都是 Shutdown 状态则返回值为 100。

<0：执行失败。

#### 55.dwmon\_startup\_database

**函数原型：**

```
DWMON_RETURN

dwmon_startup_database(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

启动指定组中指定的数据库实例。

如果指定的库是单机，则由守护进程执行拉起动作，如果指定的库是 DMDSC 集群，则由守护进程再去通知主从 css 各自执行拉起动作。

此命令执行前，如果守护进程处于 Shutdown 状态，会将其切换为 Startup 状态，如果主从 css 的自动拉起功能是关闭的，在各节点实例拉起成功后，会将其打开。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要启动的库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要启动的数据库名称，此参数必须指定。

**返回值：**

\>=0：执行成功，执行前库已经处于活动状态时返回值为 100。

<0：执行失败。

#### 56.dwmon\_stop\_database

**函数原型：**

```
DWMON_RETURN

dwmon_stop_database(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

关闭指定组中指定的数据库实例。

如果指定的库是单机，则由守护进程通知单机库正常退出，如果指定的库是 DMDSC 集群，则由守护进程再去通知主 css 依次退出每个节点实例。

此命令执行完成后，会将守护进程切换为 Shutdown 状态，并将主从 css 的自动拉起功能关闭。

> **注意**
> 
> 如果要退出的是全局守护类型的备库，为了避免触发主库的Failover动作，要求此备库已经被detach分离出去，也就是备库归档要处于无效状态，才允许将其正常退出。  
> 如果要退出的是主库，在自动切换模式下，为了避免触发备库的自动接管，要求所有备库都已经被detach分离出去，也就是所有备库归档都处于无效状态，才允许退出主库，手动切换模式下没有此要求。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要关闭的库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要关闭的数据库名称，此参数必须指定。

**返回值：**

\>=0：执行成功，执行前库已经退出时返回值为 100。

<0：执行失败。

#### 57.dwmon\_kill\_database

**函数原型：**

```
DWMON_RETURN

dwmon_kill_database(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

强制关闭指定组中指定的数据库实例。

如果指定的库是单机，则由守护进程强制杀掉指定库的进程，如果指定的库是 DMDSC 集群，则由守护进程再去通知主 css 强杀所有节点实例。

> **注意**
> 
> 此命令执行完成后，会将守护进程切换为Shutdown状态。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要强制关闭的库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要强制关闭的数据库名称，此参数必须指定。

**返回值：**

\>=0：执行成功，执行前库已经不是活动状态时返回值为 100。

<0：执行失败。

#### 58.dwmon\_open\_database

**函数原型：**

```
DWMON_RETURN

dwmon_open_database(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

在系统中存在其他故障实例时，守护进程无法自动 Open 主库，或者系统中没有活动主库时，守护进程无法自动 Open 备库，这种情况下，可以调用此接口强制 Open 指定的数据库。

执行此操作需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要强制 Open 库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要强制 Open 的数据库名称，此参数必须指定。

**返回值：**

\>=0：执行成功，执行前库已经处于 Open 状态时返回值为 100。

<0：执行失败。

#### 59.dwmon\_get\_switchover\_standby

**函数原型：**

```
DWMON_RETURN

dwmon_get_switchover_standby(

    mhandle mhdle,

    mschar* group_name,

    muint4* n_db,

    mschar** db_name_arr

);
```

**功能说明：**

获取可以切换为主库的备库信息，这里的切换是指主备库都正常，且处于 Open 状态时，交换主备库模式，将备库切换为新的主库，主库切换为备库的操作。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要获取切换信息的组名，只有一组时可以不指定。

n\_db: 输入输出参数，可以执行切换的备库个数。输入参数：指定可获取的最大备库个数，输出参数：实际获取的备库个数，建议输入值不小于 8，避免取不到完整信息。

db\_name\_arr: 输出参数，输出可以执行切换的备库名称，参数是字符串指针数组类型，数组长度是 n\_db 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 60.dwmon\_switchover

**函数原型：**

```
DWMON_RETURN

dwmon_switchover(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

使用指定的备库和当前的主库执行切换操作，这里的切换是指主备库都正常，且处于 Open 状态时，交换主备库模式，将备库切换为新的主库，主库切换为备库的操作。

此接口只有在指定的备库满足切换条件时才能够执行成功，可以先调用 dwmon\_get\_switchover\_standby 获取到满足条件的备库列表。

执行此操作需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要执行切换的备库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要执行切换的备库名称，只有一个备库时可以不指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 61.dwmon\_get\_takeover\_standby

**函数原型：**

```
DWMON_RETURN
dwmon_takeover(
    mhandle         mhdle,
    mschar*         group_name,
    mschar*         db_name
);
```

**功能说明：**

获取可以接管为主库的备库信息，在主库发生故障时，可以通过调用此接口查找可以接管为新的主库的备库实例，其中包括正常接管和强制接管，通过输入参数 force\_flag 可以指定接管方式。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要获取接管信息的组名，只有一组时可以不指定。

force\_flag: 输入参数，指定接管方式，TRUE: 强制接管，FALSE: 正常接管。

n\_db: 输入输出参数，可以执行接管操作的备库个数。输入参数：可获取的最大备库个数，输出参数：实际获取的备库个数，建议输入值不小于 8，避免取不到完整信息。

db\_name\_arr: 输出参数，输出可以执行接管操作的备库实例名，参数是字符串指针数组类型，数组长度是 n\_db 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 62.dwmon\_takeover

**函数原型：**

```
DWMON_RETURN
dwmon_takeover(
mhandle mhdle,
mschar* group_name,
mschar* db_name
);
```

**功能说明：**

主库故障后，可以通过调用此接口执行正常地接管操作，注意，此接口只有在指定备库满足正常接管条件时才能够执行成功，可以先调用 dwmon\_get\_takeover\_standby 获取到符合正常接管条件的备库实例，force\_flag 指定为 FALSE。

执行此操作需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要执行接管的备库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要执行接管的备库名称，只有一个备库时可以不指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 63.dwmon\_takeover\_force

**函数原型：**

```
DWMON_RETURN

dwmon_takeover_force(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

主库故障后，可以通过调用此接口执行强制接管操作，注意，此接口只有在指定备库满足强制接管条件时才能够执行成功，可以先调用 dwmon\_get\_takeover\_standby 获取到符合强制接管条件的备库实例，force\_flag 指定为 TRUE。

执行此操作需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要执行强制接管的备库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要执行强制接管的备库名称，只有一个备库时可以不指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 64.dwmon\_check\_mppctl

**函数原型：**

```
DWMON_RETURN

dwmon_check_mppctl(

    mhandle mhdle

);
```

**功能说明：**

配置为 MPP 主备环境时，可通过调用此接口检查当前各个活动节点的 dmmpp.ctl 是否处于一致状态，只有 MPP 主备环境下允许调用此接口。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

0：处于一致状态。

<0：检查失败，或者控制文件不一致(返回值为-12)。

#### 65.dwmon\_recover\_mppctl

**函数原型：**

```
DWMON_RETURN

dwmon_recover_mppctl(

    mhandle mhdle

);
```

**功能说明：**

配置为 MPP 主备环境时，如果某个活动节点的 dmmpp.ctl 不一致，可通过调用此接口恢复到一致状态。

只有 MPP 主备环境下允许调用此接口，并且需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

0：执行成功。

<0：执行失败。

#### 66.dwmon\_get\_mpp\_site\_info

**函数原型：**

```
DWMON_RETURN

dwmon_get_mpp_site_info(

    mhandle mhdle,

    muint4* n_site,

    muint4* ep_seqno,

    mschar** db_name,

    mschar** db_ip,

    muint4* db_port

);
```

**功能说明：**

配置为 MPP 主备环境时，可通过调用此接口获取 MPP 节点信息，注意只有 MPP 主备环境下允许调用此接口。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

n\_site: 输入输出参数，MPP 节点数。输入参数：可获取的最大节点数，输出参数：实际获取的节点数，建议输入值不小于 1024，避免取不到完整信息。

ep\_seqno: 输出参数，输出 MPP 节点号，参数为 muint4 数组类型，数组长度是 n\_site 的输入值。

db\_name: 输出参数，输出 MPP 节点实例名，参数是字符串指针数组类型，数组长度是 n\_sit 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免溢出。

db\_ip: 输出参数，输出 MPP 节点 IP 地址，参数是字符串指针数组类型，数组长度是 n\_site 的输入值，数组中每个指针元素指向的缓存长度不能小于 65，避免溢出。

db\_port: 输出参数，输出 MPP 节点端口号，参数为 muint4 数组类型，数组长度是 n\_site 的输入值。

**返回值：**

0：执行成功。

<0：执行失败。

#### 67.dwmon\_tip

**函数原型：**

```
DWMON_RETURN

dwmon_tip(

    mhandle mhdle

);
```

**功能说明：**

可调用此接口查看系统当前运行状态，输出的系统状态信息可通过消息相关接口获取到。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

0：系统运行正常，所有实例和守护进程都处于 OPEN 状态。

\-25：所有组中都有正常的主库实例（实例和守护进程都是 OPEN 状态），不影响系统使用，但是存在有其他异常实例，具体描述信息可通过消息相关接口获取。

\-26：系统运行异常，不是所有组都有正常的主库实例，守护进程正在自动处理，请稍后再次调用接口判断，具体描述信息可通过消息相关接口获取。

\-27：系统运行异常，不是所有组都有正常的主库实例，需要用户根据描述信息确认是否进行人工干预，具体描述信息可通过消息相关接口获取。

其他<0 的值：表示接口执行失败。

#### 68.dwmon\_set\_group\_arch\_invalid

**函数原型：**

```
DWMON_RETURN

dwmon_set_group_arch_invalid(

    mhandle mhdle,

    mschar* group_name

);
```

**功能说明：**

修改指定组中所有备库的归档为无效状态，如果未指定组名，则通知所有组执行。

注意：执行此操作需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，守护组名，不指定则对所有组执行。

**返回值：**

0：执行成功。

<0：执行失败。

#### 69.dwmon\_set\_group\_recover\_time

**函数原型：**

```
DWMON_RETURN

dwmon_set_group_recover_time(

    mhandle mhdle,

    mschar* group_name,

    muint4 recover_time

);
```

**功能说明：**

修改指定组中所有备库的恢复间隔(3~86400s)，只修改组中主库对应守护进程的内存值，如果未指定组名，则通知所有组执行。

注意：执行此操作需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，守护组名，不指定则对所有组执行。

recover\_time: 输入参数，指定恢复间隔(3~86400s)，只修改组中主库守护进程的内存值。

**返回值：**

0：执行成功。

<0：执行失败。

#### 70.dwmon\_set\_group\_para\_value

**函数原型：**

```
DWMON_RETURN

dwmon_set_group_para_value(

    mhandle mhdle,

    mschar* group_name,

    mschar* para_name,

    mschar* para_value

);
```

**功能说明：**

修改指定组的所有守护进程的指定配置参数，同时修改 dmwatcher.ini 配置文件和内存值，如果未指定组名，则通知所有组执行。

目前可修改的参数包括：DW\_ERROR\_TIME、INST\_RECOVER\_TIME、INST\_ERROR\_TIME、INST\_AUTO\_RESTART、INST\_SERVICE\_IP\_CHECK、RLOG\_SEND\_THRESHOLD、RLOG\_APPLY\_THRESHOLD。

如果组中某个守护进程故障，则跳过不修改，如果要重启故障的守护进程，需要在重启前修改守护进程 dmwatcher.ini 中的 DW\_ERROR\_TIME 和远程一致，否则 dmmonitor 执行命令时会报错处理。

注意：执行此操作需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，守护组名，不指定则对所有组执行。

para\_name: 输入参数，指定要修改的参数名称，目前只允许是 DW\_ERROR\_TIME、INST\_RECOVER\_TIME、INST\_ERROR\_TIME、INST\_AUTO\_RESTART、INST\_SERVICE\_IP\_CHECK、RLOG\_SEND\_THRESHOLD、RLOG\_APPLY\_THRESHOLD 中的一种。

para\_value: 输入参数，指定要修改的参数值，和 para\_name 对应。

**返回值：**

0：执行成功。

<0：执行失败。

#### 71.dwmon\_set\_group\_auto\_restart\_on

**函数原型：**

```
DWMON_RETURN

dwmon_set_group_auto_restart_on(

    mhandle mhdle,

    mschar* group_name

);
```

**功能说明：**

打开指定组内所有单节点或 DMDSC 集群节点实例的自动拉起标记。

对单节点，直接修改 dmwatcher 自动拉起标记的内存值。

对 DMDSC 集群，自动拉起是靠 dmcss 执行的，dmcss 只负责拉起和自己的 dcr\_seqno 相同的 db 节点。如果 dmcss 未配置自动拉起参数（DMDCR\_DB\_RESTART\_INTERVAL/ DMDCR\_DB\_STARTUP\_CMD），此命令会执行失败。

此接口只修改 dmwatcher 或 dmcss 内存中的自动拉起标记值，不会修改 dmwathcer.ini 或 dmdcr.ini 中的配置值，如果重启，此修改会丢失。

此接口执行时，有可能所有节点实例都还未启动，无法校验登录口令，因此不要求先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要执行操作的组名，只有一组时可以不指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 72.dwmon\_set\_group\_auto\_restart\_off

**函数原型：**

```
DWMON_RETURN

dwmon_set_group_auto_restart_off(

    mhandle mhdle,

    mschar* group_name

);
```

**功能说明：**

关闭指定组内所有单节点或 DMDSC 集群节点实例的自动拉起标记。

对单节点，直接修改 dmwatcher 自动拉起标记的内存值。

对 DMDSC 集群，和 dwmon\_set\_group\_auto\_restart\_on 接口相对应，可以一次性关闭守护系统内所有 DMDSC 集群上 dmcss 的自动拉起标记。

此命令只修改 dmcss 或内存中的自动拉起标记值，如果重启，此修改会丢失。

执行此操作需要先登录监视器。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要执行操作的组名，只有一组时可以不指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 73.dwmon\_detach\_database

**函数原型：**

```
DWMON_RETURN

dwmon_detach_database(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

此接口允许将指定的备库分离出守护进程组，执行此接口需要先登录监视器。

对于全局守护类型的备库，使用此命令不会触发主库的 Failover 故障处理流程。该接口不会修改相关的配置信息，只是为了需要主动维护备库时使用。

接口会依次执行下列操作：

1. 设置指定备库的恢复间隔为 86400(s)
2. 修改主库到指定备库的归档状态无效

本接口不会主动退出备库实例，如果需要执行退出操作，可再通过调用 dwmon\_stop\_database 接口完成。

在备库维护结束后，如果备库是退出状态，可先调用 dwmon\_startup\_database 接口将备库启动，然后再调用 dwmon\_attach\_database 接口将备库重加入守护进程组。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要执行操作的守护进程组名，只有一组时可以不指定。

db\_name: 输入参数，指定要正常分离出的备库名称，此参数必须指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 74.dwmon\_attach\_database

**函数原型：**

```
DWMON_RETURN
dwmon_attach_database(
    mhandle mhdle,
    mschar* group_name,
    mschar* db_name
);
```

**功能说明：**

在使用 dwmon\_detach\_database 接口分离出去的备库维护完成后，可通过调用此接口将备库重加入守护进程组，执行此接口需要先登录监视器。

此接口执行时，会通知主库将指定备库的恢复间隔调整为 3s，3s 后主库守护进程会发起 Recovery 流程，将备库重加入守护系统。

注意，此接口不会将备库拉起，如果备库处于退出状态，需要先调用 dwmon\_startup\_database 接口将备库启动。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定要执行操作的守护进程组名，只有一组时可以不指定。

db\_name: 输入参数，指定要重加入的备库名称，此参数必须指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 75.dwmon\_get\_source\_database\_name

**函数原型：**

```
DWMON_RETURN

dwmon_get_source_database_name(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    mschar* source_name

);
```

**功能说明：**

获取指定库的源库名称，指定库为备库时才有意义，可以是异步备库。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

source\_name: 输出参数，输出备库的源库名称，注意缓存长度不能小于 65，避免发生溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 76.dwmon\_get\_ep\_arch\_send\_info

**函数原型：**

```
DWMON_RETURN

dwmon_get_ep_arch_send_info(

    mhandle mhdle,

    mschar* group_name,

    mschar* source_name,

    mschar* db_name,

    muint4* time_in_ini,

    muint4* time_in_mem,

    mschar* last_recover_time,

    mint4* last_recover_code,

    mschar* arch_type,

    mschar* mal_sta,

    mschar* arch_sta,

    mschar* send_type,

    mschar* last_start_time,

    mschar* last_end_time,

    mint8* last_send_time,

    muint8* last_start_lsn,

    muint8* last_end_lsn,

    muint4* last_send_len,

    muint4* last_send_ptx,

    mint4* code,

    mschar* desc_info,

    mint4* recnt_cnt,

    mint8* recnt_send_len,

    mint8* recnt_ptx_cnt,

    mint8* recnt_send_time,

    mint8* max_send_time,

    mschar* max_end_time,

    muint4* max_ptx_cnt,

    muint4* max_send_len,

    mint8* max_send_lsn,

    mint8* total_send_cnt,

    mint8* total_send_len,

    mint8* total_ptx_cnt,

    mint8* total_send_time

);
```

**功能说明：**

获取指定的源实例到指定备库的归档发送信息。

源库如果是 DMDSC 集群，则需要依次取出集群内每个源实例到指定备库的归档发送信息，这个需要结合 dwmon\_get\_source\_database\_name 和 dwmon\_get\_database\_ep\_info 这两个接口来完成。

首先用 dwmon\_get\_source\_database\_name 获取到源库名称，再通过 dwmon\_get\_database\_ep\_info 获取到源库的所有实例名，再通过本接口依次取出源库每个实例到指定备库的归档发送信息，接口中的 source\_name 字段就是指源库中的某个实例名。

如果备库是 DMDSC 集群，则备库控制节点为重演节点，以下参数说明中的备库均指备库控制节点，包括 mal\_sta 和 arch\_sta 这两个字段，如果备库是单节点，则就指备库自身。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，输入指定备库所在的守护进程组名，如果只有一组可以不指定。

source\_name：输入参数，输入要获取归档发送信息的源库实例名。

db\_name: 输入参数，输入要获取归档发送信息的备库名称。

time\_in\_ini：输出参数，输出源库守护进程 dmwatcher.ini 中配置 INST\_RECOVER\_TIME 值。

time\_in\_mem：输出参数，输出源库守护进程内存中的 INST\_RECOVER\_TIME 值。

last\_recover\_time：输出参数，输出源实例上次对指定备库执行恢复操作的时间，对 local 守护类型的备库无效，NONE 表示未执行过恢复操作，注意缓存长度不能小于 65，避免溢出。

last\_recover\_code：输出参数，输出源实例上次对指定备库执行恢复操作的执行结果 code，对 local 守护类型无效，0 表示执行成功，100 表示实际未执行，小于 0 表示执行失败。

arch\_type：输出参数，输出源实例 source\_name 到备库的归档类型，包括 REALTIME/TIMELY/ASYNC 这三种类型，注意缓存长度不能小于 65，避免溢出。

mal\_sta：输出参数，输出源实例 source\_name 到备库的 mal 链路状态，注意缓存长度不能小于 65，避免溢出。

arch\_sta：输出参数，输出源实例 source\_name 到备库的归档状态，注意缓存长度不能小于 65，避免溢出。

send\_type：输出参数，输出源实例 source\_name 到备库的归档发送类型，FOR REALTIME SEND 和 FOR TIMELY SEND 表示正常的归档发送，FOR RECOVER SEND 表示守护进程发起的归档发送，FOR ASYNC SEND 表示定时器触发的异步归档发送，注意缓存长度不能小于 65，避免溢出。

last\_start\_time：输出参数，输出源实例 source\_name 到备库的最近一次归档发送起始时间，NONE 表示未执行过发送操作，注意缓存长度不能小于 65，避免溢出。

last\_end\_time：输出参数，输出源实例 source\_name 到备库的最近一次归档发送结束时间，end\_time 为 NONE 时，如果 start\_time 也为 NONE，则表示未执行过发送操作，如果 start\_time 为具体时间，则表示发送尚未结束，注意缓存长度不能小于 65，避免溢出。

last\_send\_time：输出参数，输出源实例 source\_name 到备库的最近一次归档发送耗时（微秒）。

last\_start\_lsn：输出参数，输出源实例 source\_name 到备库的最近一次归档发送起始 lsn。

last\_end\_lsn：输出参数，输出源实例 source\_name 到备库的最近一次归档发送结束 lsn。

last\_send\_len：输出参数，输出源实例 source\_name 到备库的最近一次归档发送长度（字节）。

last\_send\_ptx：输出参数，输出源实例 source\_name 到备库的最近一次发送的 PTX 个数。

code：输出参数，输出源实例 source\_name 到备库的最近一次归档发送 code，0 表示执行成功，100 表示实际未执行，小于 0 表示执行失败。

desc\_info：输出参数，输出源实例 source\_name 到备库的最近一次归档发送描述信息，注意缓存长度不能小于 513，避免溢出。

recnt\_cnt：输出参数，输出源实例 source\_name 到备库的最近日志发送次数 N。

recnt\_send\_len: 输出参数，输出源实例 source\_name 到备库的最近 N 次累计日志发送长度（字节），N 值取 recnt\_cnt 值，下同。

recnt\_ptx\_cnt：输出参数，输出源实例 source\_name 到备库的最近 N 次累计发送的 PTX 个数。

recnt\_send\_time：输出参数，输出源实例 source\_name 到备库的最近 N 次累计日志发送耗时（微秒）。

max\_send\_time：输出参数，输出源实例 source\_name 到备库的最大发送耗时（微秒）。

max\_end\_time：输出参数，输出源实例 source\_name 到备库最大发送耗时的结束时间，注意缓存长度不能小于 65，避免溢出。

max\_ptx\_cnt：输出参数，输出源实例 source\_name 到备库发送的最大 PTX 个数。

max\_send\_len：输出参数，输出源实例 source\_name 到备库发送的最大日志长度（字节）。

max\_send\_lsn：输出参数，输出源实例 source\_name 到备库发送的最大日志 LSN。

total\_send\_cnt: 输出参数，输出源实例 source\_name 到备库总的归档发送次数。

total\_send\_len：输出参数，输出源实例 source\_name 到备库总的归档发送长度（字节）。

total\_ptx\_cnt：输出参数，输出源实例 source\_name 到备库总的 PTX 发送个数。

total\_send\_time：输出参数，输出源实例 source\_name 到备库总的归档发送耗时（微秒）。

**返回值：**

0：执行成功。

<0：执行失败。

#### 77.dwmon\_get\_n\_apply

**函数原型：**

```
DWMON_RETURN

dwmon_get_n_apply(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    mschar* ep_name,

    msint2* n_apply,

    mschar* prim_name

);
```

**功能说明：**

获取指定备库上的重演节点个数信息，也就是源库的节点个数。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

ep\_name: 输出参数，输出获取重演信息的备库控制节点名称。

n\_apply: 输出参数，输出备库控制节点上记录的重演节点个数。

prim\_name: 输出参数，输出备库对应的源库名称。

**返回值：**

0：执行成功。

<0：执行失败。

#### 78.dwmon\_get\_ep\_nth\_apply\_info

**函数原型：**

```
DWMON_RETURN

dwmon_get_ep_nth_apply_info(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    muint4 nth,

    mschar* prim_name,

    msint2* dsc_seqno,

    muint8* sseq,

    muint8* slsn,

    muint8* kseq,

    muint8* klsn,

    muint8* aseq,

    muint8* alsn,

    muint4* n_task,

    muint8* tsk_mem_used

);
```

**功能说明：**

获取指定备库上第 nth 组重演信息上记录的 lsn 等信息。

当备库对应的源库是 DMDSC 集群时，假如 DMDSC 集群有 N 个节点，那么备库上就会有 N 组重演信息依次和源库的每个节点相对应，N 值可以通过 dwmon\_get\_n\_apply 接口中的 n\_apply 字段值获取，本接口的输入参数 nth 的取值范围为\[0,n\_apply-1\]。

此接口只输出 dsc\_seqno、sseq、slsn、kseq、klsn、aseq、alsn 等简略的重演信息，如果还需要获取详细的重演统计信息，请参考 dwmon\_get\_ep\_nth\_apply\_stat 接口说明。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

nth: 输入参数，指定要获取备库上第 nth 组重演信息。

prim\_name: 输出参数，第 nth 组重演信息对应的源库实例名，注意缓存长度不能小于 65，避免溢出。

dsc\_seqno: 输出参数，第 nth 组重演信息对应的源库实例的 seqno 序号。

sseq：输出参数，备库可重演到的最大日志包序号。

slsn: 输出参数， 备库可重演到的最大 LSN，对应的日志包序号为 sseq。

kseq：输出参数，非自动切换模式下，备库保持不重演的日志包序号。

klsn：输出参数，非自动切换模式下，备库保持不重演的最大 LSN，对应的日志包序号为 kseq。

aseq：输出参数，备库已经写入联机日志文件的原始日志包序号。

alsn: 输出参数，备库已经写入联机日志文件的原始 LSN 值，对应的日志包序号为 aseq。

n\_task: 输出参数，第 nth 组重演信息中当前还剩余的重演任务个数。

tsk\_mem\_used: 输出参数，第 nth 组重演信息中执行重演任务所占用的内存大小（字节）。

**返回值：**

0：执行成功。

<0：执行失败。

#### 79.dwmon\_get\_ep\_nth\_apply\_stat

**函数原型：**

```
DWMON_RETURN

dwmon_get_ep_nth_apply_stat(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name,

    muint4 nth,

    mschar* prim_name,

    msint2* dsc_seqno,

    muint8* sseq,

    muint8* slsn,

    muint8* kseq,

    muint8* klsn,

    muint8* aseq,

    muint8* alsn,

    muint4* n_task,

    muint8* tsk_mem_used,

    mint4* recnt_apply_num,

    muint4* last_recved_len,

    mint8* last_res_time,

    mint8* last_wait_time,

    muint4 last_apply_len,

    mint8* last_apply_time,

    mint8* recnt_recved_len,

    mint8* recnt_res_time,

    mint8* recnt_wait_time,

    mint8* recnt_apply_len,

    mint8* recnt_apply_time,

    mint8* max_res_time,

    mint8* max_wait_time,

    mint8* max_apply_time,

    muint4* max_apply_len,

    mint8* total_recved_num,

    mint8* total_recved_len,

    mint8* total_apply_num,

    mint8* total_apply_len,

    mint8* total_res_time,

    mint8* total_wait_time,

    mint8* total_apply_time

);
```

**功能说明：**

获取指定备库上第 nth 组重演信息，包含详细的重演统计信息。

当备库对应的源库是 DMDSC 集群时，假如 DMDSC 集群有 N 个节点，那么备库上就会有 N 组重演信息依次和源库的每个节点相对应，N 值可以通过 dwmon\_get\_n\_apply 接口中的 n\_apply 字段值获取，本接口的输入参数 nth 的取值范围为\[0,n\_apply-1\]。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，输入指定备库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取重演信息的备库名称。

nth: 输入参数，指定要获取备库上第 nth 组重演信息。

prim\_name: 输出参数，第 nth 组重演信息对应的源库实例名，注意缓存长度不能小于 65，避免溢出。

dsc\_seqno: 输出参数，第 nth 组重演信息对应的源库实例的 seqno 序号。

sseq: 输出参数，备库可重演到的最大日志序号值。

slsn: 输出参数，备库可重演到的最大 LSN 值，对应的日志包序号为 sseq。

kseq: 输出参数，非自动切换模式下，备库保持不重演的日志的序号。

klsn：输出参数，非自动切换模式下，备库保持不重演的最大 LSN 值，对应的日志包序号为 kseq。

aseq: 输出参数，备库已经写入联机日志文件的原始日志包序号。

alsn: 输出参数，备库已经写入到联机日志文件的原始 LSN 值，对应的日志包序号为 aseq。

n\_task: 输出参数，第 nth 组重演信息中当前还剩余的重演任务个数。

tsk\_mem\_used: 输出参数，第 nth 组重演信息中执行重演任务所占用的内存大小（字节）。

/\*\* 以下均为指定备库相对于主库第 nth 个节点的重演统计信息 \*\*/

recnt\_apply\_num：输出参数，输出最近重演的日志包个数 N。

last\_recved\_len：输出参数，输出最近一次收到的日志长度（字节）。

last\_res\_time：输出参数，输出最近一次消息响应时间（微秒）。

last\_wait\_time：输出参数，输出最近一次任务等待时间（微秒）。

last\_apply\_len：输出参数，输出最近一次重演的日志长度（字节）。

last\_apply\_time：输出参数，输出最近一次重演耗时（微秒）。

recnt\_recved\_len：输出参数，输出最近 N 次累计接收日志长度（字节），N 值取自 recnt\_apply\_num，下同。

recnt\_res\_time：输出参数，输出最近 N 次累计响应时间（微秒）。

recnt\_wait\_time：输出参数，输出最近 N 次累计任务等待时间（微秒）。

recnt\_apply\_len：输出参数，输出最近 N 次累计重演日志长度（字节）。

recnt\_apply\_time：输出参数，输出最近 N 次累计重演耗时（微秒）。

max\_res\_time：输出参数，输出最大的消息响应时间（微秒）。

max\_wait\_time：输出参数，输出最大的任务等待时间（微秒）。

max\_apply\_time：输出参数，输出最大的任务重演时间（微秒）。

max\_apply\_len：输出参数，输出和 max\_apply\_time 对应的重演日志长度（字节）。

total\_recved\_num：输出参数，输出累计收到的日志包个数。

total\_recved\_len：输出参数，输出累计收到的日志量（字节）。

total\_apply\_num：输出参数，输出累计重演的日志缓存个数。

total\_apply\_len：输出参数，输出累计重演日志量（字节）。

total\_res\_time：输出参数，输出累计消息响应时间（微秒）。

total\_wait\_time：输出参数，输出累计任务等待时间（微秒）。

total\_apply\_time：输出参数，输出累计任务重演时间（微秒）。

**返回值：**

0：执行成功。

<0：执行失败。

#### 80.dwmon\_clear\_database\_arch\_send\_info

**函数原型：**

```
DWMON_RETURN

dwmon_clear_database_arch_send_info(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

清理指定组中主库到指定备库实例的最近 N 次归档发送信息（通知主库执行）。函数在使用前，需要先登录监视器。

N 值取主库 dm.ini 中配置的 RLOG\_SEND\_APPLY\_MON 值和实际归档发送次数中的较小值，实际归档发送次数可通过查询 V$ARCH\_SEND\_INFO 获取。

如果主库是 DMDSC 集群，则会通知集群内所有实例执行清理。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

**返回值：**

0：执行成功。

<0：执行失败。

#### 81.dwmon\_clear\_group\_arch\_send\_info

**函数原型：**

```
DWMON_RETURN

dwmon_clear_group_arch_send_info(

    mhandle mhdle,

    mschar* group_name

);
```

**功能说明：**

清理指定组中主库到所有实时或即时备库实例的最近 N 次归档发送信息（通知主库执行）。函数在使用前，需要先登录监视器。

N 值取主库 dm.ini 中配置的 RLOG\_SEND\_APPLY\_MON 值和实际归档发送次数中的较小值，实际归档发送次数可通过查询 V$ARCH\_SEND\_INFO 获取。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定守护进程组名，如果不指定则通知所有组执行。

**返回值：**

0：执行成功。

<0：执行失败。

#### 82.dwmon\_clear\_database\_rapply\_stat

**函数原型：**

```
DWMON_RETURN

dwmon_clear_database_rapply_stat(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

清理指定备库实例的最近 N 次日志重演信息（通知备库执行）。函数在使用前，需要先登录监视器。

N 值取备库 dm.ini 中配置的 RLOG\_SEND\_APPLY\_MON 值和实际重演次数中的较小值，实际重演次数可通过查询 V$RAPPLY\_STAT 获取。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

**返回值：**

0：执行成功。

<0：执行失败。

#### 83.dwmon\_clear\_group\_rapply\_stat

**函数原型：**

```
DWMON_RETURN

dwmon_clear_group_rapply_stat(

    mhandle mhdle,

    mschar* group_name

);
```

**功能说明：**

清理指定组中所有备库实例的最近 N 次日志重演信息（通知所有备库执行）。函数在使用前，需要先登录监视器。

N 值取备库 dm.ini 中配置的 RLOG\_SEND\_APPLY\_MON 值和实际重演次数中的较小值，实际重演次数可通过查询 V$RAPPLY\_STAT 获取。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定守护进程组名，如果不指定则通知所有组执行。

**返回值：**

0：执行成功。

<0：执行失败。

#### 84.dwmon\_check\_recover

**函数原型：**

```
DWMON_RETURN

dwmon_check_recover(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

检查指定组的指定备库是否满足自动 Recover 条件，如果不满足条件，主库的守护进程不会对指定备库发起自动 Recovery 流程。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

**返回值：**

0：符合自动 Recover 条件，备库已经在待恢复列表或者主库的守护进程即将发起对指定备库的 Recover 操作。

\-20：当前无法判断是否符合自动 Recover 条件，比如有监视器命令正在执行、指定备库还未达到恢复间隔或者指定备库上的 RLOG\_PKG 还未全部重演完成等情况，需要稍后再次调用接口判断，具体的描述信息可通过消息相关接口获取到。

\-21：表示备库不满足自动 Recover 条件，具体的描述信息可通过消息相关接口获取到。

其他<0 的值：表示接口执行失败。

#### 85.dwmon\_check\_open

**函数原型：**

```
DWMON_RETURN

dwmon_check_open(

    mhandle mhdle,

    mschar* group_name,

    mschar* db_name

);
```

**功能说明：**

检查指定组的指定库是否满足自动 Open 条件，如果不满足条件，守护进程不会通知数据库实例执行 Open 操作。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定数据库名称。

**返回值：**

0：符合自动 Open 条件，库已经 Open 成功或者正在执行 Open，或者库的守护进程即将通知实例执行 Open 操作。

\-22：当前无法判断库是否满足自动 Open 条件，比如有监视器命令正在执行，或者数据库实例还未启动到 MOUNT 状态等情况，需要稍后再次调用接口判断，具体的描述信息可通过消息相关接口获取到。

\-23：表示库不满足自动 Open 条件，并且库自身不是 OPEN 状态，具体的描述信息可通过消息相关接口获取到。

\-24：表示库不满足自动 Open 条件，其中库实例已经是 OPEN 状态，但库的守护进程不是 OPEN 状态，具体的描述信息可通过消息相关接口获取到。

其他<0 的值：表示接口执行失败。

#### 86.dwmon\_deinit

**函数原型：**

```
DWMON_RETURN

dwmon_deinit(

    mhandle mhdle

);
```

**功能说明：**

销毁监视器执行环境。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

**返回值：**

0：执行成功。

<0：执行失败。

#### 87.dwmon\_free\_handle

**函数原型：**

```
DWMON_RETURN

dwmon_free_handle(

    mhandle mhdle

);
```

**功能说明：**

释放分配到的监视器句柄。释放完成后，需要用户将 mhdle 置空，避免重复执行 dwmon\_free\_handle 引发异常。推荐使用 dwmon\_free\_handle\_low 释放句柄。

**参数说明：**

mhdle: 输入参数，分配到的句柄。

**返回值：**

0：执行成功。

<0：执行失败。

#### 88.dwmon\_get\_monitor\_state

**函数原型：**

```
DWMON_RETURN

dwmon_get_monitor_state(

    mhandle     mhdle,
    muint4*     n_mon,
    mschar**    mon_name_arr,
    muint4*     mon_state_arr,
    muint4*     mon_id_arr,
    muint4*     mon_role_arr,
    mschar**    mon_ip_arr,
    muint4*     mon_port_arr,
    muint4*     mon_bro,
    muint4*     mon_vote

);
```

**功能说明：**

配置为主备多监视器环境时，可通过调用此接口获取监视器信息。本函数只在确认监视器上执行有效。若在确认监视器非 leader 上执行，获取的监视器状态数组 mon\_state\_array 不准确。此接口功能已被 dwmon\_get\_monitor\_state\_from\_watcher 替代，出于兼容考虑仍保留原接口。建议使用函数 dwmon\_get\_monitor\_state\_from\_watcher 代替该函数，dwmon\_get\_monitor\_state\_from\_watcher 在确认监视器和非确认监视器上都可执行，且可获取多实例监视器的堆积标志，且 n\_mon 改为输入输出参数。

**参数说明：**

mon\_state\_arr 数组元素取值范围(0, 1, 2)，分别对应监视器 show state 命令的("INVALID", "VALID", "ASYNC\_SEND")状态。而 mon\_role\_arr 数组元素取值范围(0, 1, 2, 3, 4)，分别对应监视器 show state 命令的("CANDIDATE", "LEADER", "FOLLOWER", "NOT LEADER", "UNKNOWN")角色。（上述状态或角色的具体含义见 4.5 监视器命令中关于 show state 命令的说明）。

mhdle: 输入参数，监视器操作句柄。

n\_mon: 输出参数，监视器个数。

mon\_name\_arr: 输出参数，monitor 名字数组，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。

mon\_state\_arr: 输出参数，monitor 的监视器状态数组，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。

mon\_id\_arr: 输出参数，monitorID 数组，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。

mon\_role\_arr: 输出参数，monitor 角色数组，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。

mon\_ip\_arr: 输出参数，monitor 的 IP 地址数组，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。

mon\_port\_arr: 输出参数，monitor 的端口号信息，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。

mon\_bro: 输出参数，monitor 的广播延时。

mon\_vote: 输出参数，monitor 的投票延时。

**返回值：**

0：执行成功。

<0：执行失败。

#### 89.dwmon\_get\_ep\_nth\_apply\_with\_parallel\_info

**函数原型：**

```
DWMON_RETURN
dwmon_get_ep_nth_apply_with_parallel_info(
mhandle     mhdle,
mschar*     group_name,
mschar*     db_name,
muint4      nth,
mschar*     prim_name,
msint2*     dsc_seqno,
muint8*     sseq,
muint8*     slsn,
muint8*     kseq,
muint8*     klsn,
muint8*     rseq,
muint8*     rlsn,
msint2*     n_pll,
muint8*     redo_lsn_arr,
muint4*     n_task,
muint8*     tsk_mem_used
);
```

**功能说明：**

获取指定备库上第 nth 组并行重演信息。

当备库对应的源库是 DMDSC 集群时，假如 DMDSC 集群有 N 个节点，那么备库上就会有 N 组重演信息依次和源库的每个节点相对应，N 值可以通过 dwmon\_get\_n\_apply 接口中的 n\_apply 字段值获取，本接口的输入参数 nth 的取值范围为\[0, n\_apply-1\]。

**参数说明：**

mhdle：输入参数，监视器操作句柄。

group\_name: 输入参数，守护组名，只有一组时可以不指定。

db\_name: 输入参数，需要获取日志同步信息的备库名。

nth: 输入参数，获取指定备库的第 nth 个重演状态统计信息。

prim\_name: 输出参数，第 nth 个重演状态统计信息上记录的备库对应主库的实例名，可能为空。

dsc\_seqno: 输出参数，主库节点序号，主库是单节点时序号为 0。

sseq: 输出参数，备库可重演到的最大日志包序号。

slsn: 输出参数，备库可重演到的最大 LSN 。

kseq: 输出参数，备库保持不重演的日志包序号。

klsn: 输出参数，备库保持不重演的最大 LSN。

rseq: 输出参数，备库已经重演到的日志包序号，和 dsc\_seqno 对应。

rlsn: 输出参数，备库已经重演到的 LSN 值。

n\_pll: 输出参数，备库并行重演线程数。

redo\_lsn\_arr: 输出参数，记录备库各路并行重演线程已重演到的 LSN 值数组。数组大小需设置为 320，并分配足够的空间，若空间不足可能触发异常。

n\_task：输出参数，当前还剩余的重演任务数。

tsk\_mem\_used: 输出参数，当前任务队列占用的总内存大小。

**返回值：**

0：执行成功。

<0：执行失败。

#### 90.dwmon\_set\_database\_until\_time

**函数原型：**

```
DWMON_RETURN
dwmon_set_database_until_time(
    mhandle         mhdle,
    mschar*         group_name,
    mschar*         db_name,
    mschar*         until_time
);
```

**功能说明：**

设置指定组的指定异步备库重演到的时间点。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定异步备库名称。

until\_time：输入参数，指定异步备库重演到的时间点，可精确到微秒。

**返回值：**

0：执行成功。

<0：执行失败。

#### 91.dwmon\_get\_database\_until\_time

**函数原型：**

```
DWMON_RETURN
dwmon_get_database_until_time(
    mhandle         mhdle,
    mschar*         group_name,
    mschar*         db_name,
    mschar*         until_time,
    mbool*           apply_over
```

**功能说明：**

获取指定组的指定异步备库设置的重演到的时间点。

**参数说明：**

mhdle：输入参数，监视器操作句柄。

group\_name：输入参数，指定库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定异步备库名称。

until\_time：输出参数，异步备库设置的重演到的时间点。输出“NONE”表示没有设置重演到的时间点。

apply\_over：输出参数，表示异步备库是否已重演到指定的 until\_time 时间点， 0：否，1：是。

**返回值：**

0：执行成功。

<0：执行失败。

#### 92.dwmon\_free\_handle\_low

**函数原型：**

```
DWMON_RETURN
dwmon_free_handle_low(
  Mhandle*     mhdle
);
```

**功能说明：**

释放分配到的监视器句柄。

**参数说明：**

mhdle: 输入参数，分配到的句柄。

**返回值：**

0：执行成功。

<0：执行失败。

#### 93.dwmon\_get\_takeover\_time\_by\_group\_name

**函数原型：**

```
DWMON_RETURN
dwmon_get_takeover_time_by_group_name(
   mhandle     mhdle,
   mschar*     group_name,
   muint4*     remain_time,
   mschar*     inst_name
);
```

**功能说明：**

获取指定组的自动接管时间。

**参数说明：**

mhdle：输入参数，监视器操作句柄。

group\_name：输入参数，指定库所属的守护进程组名，只有一组时可以不指定。

remain\_time：输出参数，自动接管时间。当输出 0 时存在三种可能：（1）输出 0 且返回值为 100，原因为指定组上没有找到 takeover 信息；（2）没有启用主库正常退出，备库自动接管的功能；（3）故障开始到当前的时间已经超过配置的 MON\_TAKEOVER\_SHUTDOWN。

inst\_name：输出参数，接管实例名。

**返回值：**

0：执行成功。

<0：执行失败。

100：指定组上没有找到 takeover 信息。

#### 94\. dwmon\_get\_database\_apply\_wait

**函数原型：**

```
DWMON_RETURN
dwmon_get_database_apply_wait(
     mhandle     mhdle,
     mschar*     group_name,
     mschar4*    db_name,
     mbool;*     apply_wait
);
```

**功能说明：**

获取监视器所获取指定备库的 APPLY\_WAIT 标记，标记用于表示备库是否是事务一致的。

**参数说明：**

mhdle：输入参数，监视器操作句柄。

group\_name：输入参数，指定库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，备库名。

apply\_wait：输出参数，事务一致性。

**返回值：**

0：执行成功。

<0：执行失败。

#### 95\. dwmon\_login\_wallet

**函数原型：**

```
DWMON_RETURN
dwmon_login_wallet(
  mhandle     mhdle,
  mschar*     service_name
);
```

**功能说明：**

使用 wallet 方式登录监视器。使用此接口前需要用户先使用 dmmkstore 工具创建好 wallet 文件，配置服务名及对应的用户名和口令，将该文件拷贝到监视器所在的机器上，然后将 MON\_WALLET\_LOCATION 参数指定为 wallet 文件所在路径。这里的用户名及口令和服务器的登录口令是一致的，且必须有 DBA 权限。

校验登录信息时由守护进程转发给服务器校验，并返回校验结果给监视器，因此需要保证系统中至少有一个活动库，否则无法校验成功。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

service\_name：输入参数，服务名，最长可为 128 字节,超长则接口执行失败。

**返回值：**

0：执行成功。

<0：执行失败。

#### 96.dwmon\_get\_database\_sync\_arch\_info

**函数原型：**

```
DWMON_RETURN
dwmon_get_database_sync_arch_info(
    mhandle         mhdle,
    mschar*         group_name,
    mschar*         db_name,
    muint4*         n_sync,
    mschar**        sync_dest,
    mschar**        sync_mal_sta,
    mschar**        sync_arch_sta
);
```

**功能说明：**

获取指定库配置的同步归档信息的 C 接口，包括归档目标实例名，到归档目标的 mal 链路状态和归档状态。

**参数说明：**

sync\_dest、sync\_mal\_sta、sync\_arch\_sta：都为字符串指针数组类型，它们的数组长度是 n\_sync 的输入值，建议 n\_sync 的输入值不小于 8，避免取不到完整信息。由于 SYNC 归档与 DSC 不能兼容，所以目前 sync\_dest 数组中每个指针元素指向的缓存长度最小可以为 65，sync\_mal\_sta 和 sync\_arch\_sta 中每个指针元素指向的缓存长度也不能小于 65。

mhdle：输入参数，监视器操作句柄。

group\_name：输入参数，指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name：输入参数，指定要获取同步归档信息的数据库名称。

n\_sync：输入输出参数，传入要获取信息的同步归档个数，传出实际获取到的同步归

**返回值：**

0：执行成功。

<0：执行失败。

#### 97.dwmon\_get\_ep\_host

**函数原型：**

```
DWMON_RETURN
dwmon_get_ep_host(
  mhandle     mhdle,
  mschar*     group_name,
  mschar*     ep_name,
  mschar*       ep_host
);
```

**功能说明：**

获取指定组中指定实例的 IP 地址。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，输入指定实例所在的守护进程组名，如果只有一组可以不指定。

ep\_name: 输入参数，输入要获取 IP 地址的实例名。

ep\_host: 输出参数，输出实例的 IP 地址。如果配置有外网 IP，则输出外网 IP；否则输出内网 IP。对字符串类型的输出参数，指向的缓存长度不能小于 65，避免溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 98\. dwmon\_get\_hp\_flag

**函数原型：**

```
DWMON_RETURN
dwmon_get_hp_flag(
  mhandle     mhdle,
  mbool*      hp_flag
);
```

**功能说明：**

获取当前监视器日志堆积标记。

**参数说明：**

Mhdle：输入参数，监视器操作句柄。

hp\_flag：监视器日志堆积标记。

**返回值：**

0：执行成功。

<0：执行失败。

#### 99\. dwmon\_get\_real\_group\_db\_name

**函数原型：**

```
DWMON_RETURN
dwmon_get_real_group_db_name(
  mhandle     mhdle,
  mschar*     group_name,
  mschar*     db_name,
  mschar*       real_grpname,
  mschar*       real_dbname
);
```

**功能说明：**

根据输入的库名及其所在的组名，查找是否存在对应的库。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name: 输入参数，指定库所在的守护进程组名。如果只有一组可以不指定。

db\_name: 输入参数，将要查找的数据库名。若只需要查找备库，且指定组内只有一个备库时，可以不指定。

real\_grpname: 输出参数，输出真实的组名。该输出参数指向的缓存长度不能小于 65，避免数据溢出。

real\_dbname: 输出参数，输出真实的库名。该输出参数指向的缓存长度不能小于 65，避免数据溢出。

**返回值：**

0：执行成功。

<0：执行失败。

#### 100\. dwmon\_create\_mlog

**函数原型：**

```
DWMON_RETURN
dwmon_create_mlog(
    mhandle         mhdle,
    mschar*         file_path,
    muint8          file_size,
    mschar*         mon_name,
    muint4          mon_magic,
    muint4           overwrite
);
```

**功能说明：**

创建多实例监视器的联机日志文件。

**参数说明：**  
对字符串类型的输出参数，指向的缓存长度不能小于 65，避免溢出。

mhdle：输入参数，监视器操作句柄。

file\_path：输入参数，指定的监视器联机日志文件路径，需要与 dmmonitor.ini 中 MON\_LOG\_PATH 保持一致。

file\_size：输入参数，监视器联机日志文件大小，单位 MB，取值范围 512~10240。

mon\_name：输入参数，监视器实例名，需要与 dmmonitor.ini 中的 MON\_NAME 保持一致。

mon\_magic：输入参数，监视器联机日志文件魔数，取值范围 0~4294967294；对于同一个多实例监视器组的监视器，需要相同。

overwrite：输入参数，在 file\_path 指定路径下已经有同名的联机日志文件的情况下，是否覆盖原有文件。0：否；1：是。。

**返回值：**

0：执行成功。

<0：执行失败。

#### 101\. dwmon\_get\_exit\_all

**函数原型：**

```
DWMON_RETURN
dwmon_get_exit_all(
    mhandle         mhdle,
    muint4*         exit_all
);
```

**功能说明：**

获取监视器协同退出标记。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

exit\_all: 输出参数，监视器协同退出标记。

**返回值：**

0：执行成功。

<0：执行失败。

#### 102\. dwmon\_set\_exit\_all

**函数原型：**

```
DWMON_RETURN
dwmon_set_exit_all();
```

**功能说明：**

设置监视器协同退出标记，仅多实例监视器有效。

**返回值：**

0：执行成功。

<0：执行失败。

#### 103\. dwmon\_get\_mraft\_info

**函数原型：**

```
DWMON_RETURN
dwmon_get_mraft_info(
    mhandle         mhdle,
    muint4*         n_dest, 
    mbyte*          vote_stat,
    muint4*         leader_id,
    mbool*          hp_flag,
    muint4*         l_term_id,
    muint8*         c_seqno,
    muint8*         f_seq_arr,
    muint4*         term_id_arr
);
```

**功能说明：**

获取多实例监视器的多副本信息。

**参数说明：**  
mhdle: 输入参数，监视器操作句柄。

n\_dest: 输出参数，多实例监视器组中监视器数目。

vote\_stat: 输出参数，监视器选举角色。

leader\_id: 输出参数，监视器 leader 序号。

hp\_flag: 输出参数，监视器日志堆积标记。

l\_term\_id: 输出参数，监视器本地任期号。

c\_seqno: 输出参数，监视器已提交日志包序号。

f\_seq\_arr: 输出参数，监视器已刷盘序号数组，仅 leader 查询有效。

term\_id\_arr：输出参数,监视器已刷盘日志包任期号数组，仅 leader 查询有效。

**返回值：**

0：执行成功。

<0：执行失败。

#### 104\. dwmon\_check\_db\_detached

**函数原型：**

```
DWMON_RETURN
dwmon_check_db_detached(
mhandle         mhdle,
     mschar*         group_name,
     mschar*         db_name,
     mbool*          detached
);
```

**功能说明：**

检查指定库是否已经被分离出集群。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

group\_name：输入参数，指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name：输入参数，指定检查的数据库名称。

detached：输出参数，指定库是否已经被分离出集群。若已被分离出集群，则为 TRUE，否则为 FALSE。此输出值只对 REALTIME/TIMELY 备库有效，对于主库或者守护进程配置为 LOCAL 的备库，此字段输出值一定为 FALSE。

**返回值：**

0：执行成功。

<0：执行失败。

#### 105\. dwmon\_get\_monitor\_state\_from\_watcher

**函数原型：**

```
DWMON_RETURN
dwmon_get_monitor_state_from_watcher(
mhandle     mhdle,
muint4*      n_mon,
mschar**    mon_name_arr,
muint4*     mon_state_arr,
muint4*     mon_id_arr,
muint4*     mon_role_arr,
mschar**    mon_ip_arr,
muint4*     mon_port_arr,
muint4*     mon_bro,
muint4*     mon_vote,
mbool*       hp_flag
);
```

**功能说明：**

配置为主备多实例监视器环境时，可通过调用此接口获取监视器信息。在确认监视器调用时，会直接从自身获取多实例监视器信息；在非确认监视器调用时，会从某个守护进程发来的信息中获取集群中多实例监视器信息。若在确认监视器非 leader 上执行，获取的监视器状态数组 mon\_state\_array 不准确。

**参数说明：**

mhdle: 输入参数，监视器操作句柄。

n\_mon: 输入输出参数，监视器个数，输入值为期望获取的最大个数，输出值为实际获取的个数，输出值 <=输入值。

mon\_name\_arr: 输出参数，monitor 名字数组，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。

mon\_state\_arr: 输出参数，monitor 的监视器状态数组，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。mon\_state\_arr 数组元素取值范围(0, 1, 2)，分别对应监视器 show state 命令的("INVALID", "VALID", "ASYNC\_SEND")状态。上述状态的具体含义见\[4.5 监视器命令\](#4.5 监视器命令)中关于 show state 命令的说明。

mon\_id\_arr: 输出参数，monitorID 数组，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。

mon\_role\_arr: 输出参数，monitor 角色数组，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。mon\_role\_arr 数组元素取值范围(0, 1, 2, 3, 4)，分别对应监视器 show state 命令的("CANDIDATE", "LEADER", "FOLLOWER", "NOT LEADER", "UNKNOWN")角色。上述角色的具体含义见\[4.5 监视器命令\](#4.5 监视器命令)中关于 show state 命令的说明。

mon\_ip\_arr: 输出参数，monitor 的 IP 地址数组，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。

mon\_port\_arr: 输出参数，monitor 的端口号信息，数组长度和 n\_mon 对应；且数组大小应不小于 dmmonitor.ini 中设置的 MON\_INST\_NUM 参数值。

mon\_bro: 输出参数，monitor 的广播延时。

mon\_vote: 输出参数，monitor 的投票延时。

hp\_flag: 输出参数，monitor 的日志堆积标记。

**返回值：**

0：执行成功。如果当前不存在 dmwatcher，或者 dmwatcher 中没有多实例监视器信息，也会返回 0，同时 n\_mon 也为 0

<0：执行失败。

#### 106\. dwmon\_get\_db\_mode\_change\_stat

**函数原型：**

```
DWMON_RETURN
dwmon_get_db_mode_change_stat(
    mhandle    mhdle,
    mschar*    group_name,
    mschar*    db_name,
    mschar*    mode_change
);
```

**功能说明：**

获取指定实例的自动升降级状态。

**参数说明：**

mhdle: 输入参数，监视器句柄。

group\_name: 输入参数，实例所属组名

db\_name: 输入参数，实例名

mode\_change: 输出参数，自动升降级状态，至少需要 17 个字节的空间

**返回值：**

0：执行成功。

<0：执行失败。

### 10.2.5 JNI 接口说明

#### 1.dwmon\_init\_handle

**函数原型：**

```
boolean

dwmon_init_handle();
```

**功能说明：**

分配监视器操作句柄。

**参数说明：**

无

**返回值：**

true：分配成功。

false:分配失败。

#### 2.dwmon\_get\_error\_msg\_by\_code

**函数原型：**

```
DwMonMsg

dwmon_get_error_msg_by_code(

    int code

);
```

**功能说明：**

获取输入 code 对应的错误描述信息，code 必须是小于 0 的值。

**参数说明：**

code：输入参数，需要获取错误信息的错误码 code，注意 code 必须是小于 0 的值。

**返回值：**

返回 DwMonMsg 对象，该对象结构如下：

```
DwMonMsg：
String msg：code对应的错误描述信息
Integer msgFlag : 0
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonMsg 的对象成员 msg 获取输出消息。

<0：执行失败，-17 表示没有找到 code 对应的错误信息。

#### 3.dwmon\_init\_env

**函数原型：**

```
int

dwmon_init_env(

    String ini_path,

    String log_path

);
```

**功能说明：**

初始化监视器环境。

**参数说明：**

ini\_path: 输入参数，指定 dmmonitor.ini 的绝对路径。

log\_path: 输入参数，指定日志文件的存放路径，如果为 NULL 或空串，则将 dmmonitor.ini 中配置的 MON\_LOG\_PATH 作为日志文件路径，如果 dmmonitor.ini 中没有配置 MON\_LOG\_PATH，则将 dmmonitor.ini 的同级目录作为日志文件路径。

**返回值：**

0：执行成功。

<0：执行失败，-15 表示监视器尝试建立到所有守护进程的连接失败，可能守护进程都未启动，允许忽略此错误继续执行其他操作，如果不忽略此错误，认定初始化失败，则需要先正常销毁监视器环境（调用 dwmon\_deinit\_env 接口），再释放操作句柄（调用 dwmon\_free\_handle 接口）。

#### 4.dwmon\_msg\_event\_wait

**函数原型：**

```
void

dwmon_msg_event_wait();
```

**功能说明：**

监视器检测到守护进程或实例状态发生变化，或者接口命令执行过程中，产生中间输出消息时会将消息写入到缓存并通知消息事件，调用者只需要调用此接口等待即可，等待事件发生后，可通过接口 dwmon\_get\_exec\_msg 去读取输出消息。

这种方式需要单独起一个线程来处理消息，以免消息被阻塞。

**参数说明：**

无

**返回值：**

无

#### 5.dwmon\_get\_exec\_msg

**函数原型：**

```
DwMonMsg

dwmon_get_exec_msg();
```

**功能说明：**

获取输出信息，和 dwmon\_msg\_event\_wait 配合使用。

**参数说明：**

无

**返回值：**

返回 DwMonMsg 对象，该对象结构如下：

```
DwMonMsg：
String msg：消息缓冲区
Integer msgFlag : 是否还有未读消息
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonMsg 的对象成员 msg 获取输出消息，其中 msgFlag 值用来标记是否继续读取消息，为 1 表示还有消息可读，为 0 表示已全部读完。

<0：执行失败。

#### 6.dwmon\_get\_msg\_exit\_flag

**函数原型：**

```
boolean

dwmon_get_msg_exit_flag();
```

**功能说明：**

如果上层应用程序中有单独的消息线程，可通过调用此接口获取退出标记，在标记为 TRUE 时可正常退出线程。

**参数说明：**

无

**返回值：**

true: 允许线程退出。

false: 不允许线程退出，需要继续等待获取输出消息。

#### 7.dwmon\_set\_msg\_exit\_event

**函数原型：**

```
void

dwmon_set_msg_exit_event();
```

**功能说明：**

如果上层应用程序中有单独的消息线程，在 dwmon\_get\_msg\_exit\_flag 接口获取到退出标记为 true 时，需要调用此接口设置退出事件。

**参数说明：**

无

**返回值：**

无

#### 8.dwmon\_msg\_event\_deinit

**函数原型：**

```
void

dwmon_msg_event_deinit();
```

**功能说明：**

使用等待事件方式获取监视器消息时，需要单独起一个线程，在程序结束，退出线程时，需要调用此接口通知并等待消息线程退出。

消息线程相关的接口有 dwmon\_msg\_event\_wait、dwmon\_get\_exec\_msg、dwmon\_get\_msg\_exit\_flag、dwmon\_set\_msg\_exit\_event 和 dwmon\_msg\_event\_deinit，这几个接口需要配合使用。

**参数说明：**

无

**返回值：**

无

#### 9.dwmon\_get\_version

**函数原型：**

```
DwMonData

dwmon_get_version();
```

**功能说明：**

获取当前的监视器版本信息。

**参数说明：**

无

**返回值：**

返回 DwMonData 对象，该对象结构如下:

```
DwMonData：
Integer dataValue：0
String stringValue : 监视器版本信息
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过对象成员 stringValue 获取监视器版本信息。

<0：执行失败。

#### 10.dwmon\_get\_mpp\_flag

**函数原型：**

```
DwMonData

dwmon_get_mpp_flag();
```

**功能说明：**

获取 MPP 主备环境标记，用于判断当前是否为 MPP 主备环境。

**参数说明：**

无

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：是否是MPP主备环境
String stringValue : “”
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过对象成员 dataValue 获取确认标记，1：是 MPP 主备环境，0：不是 MPP 主备环境。

<0：执行失败。

#### 11.dwmon\_get\_n\_group

**函数原型：**

```
DwMonGrpNameArray

dwmon_get_n_group();
```

**功能说明：**

获取当前监控的组个数和组名称。只有 mpp 主备环境下允许配置多组。

**参数说明：**

无

**返回值：**

返回 DwMonGrpNameArray 对象，该对象结构如下:

```
DwMonGrpNameArray：
Integer groupNum：组个数
String[] nameArray : 组名称
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonGrpNameArray 的其他对象成员获取监控组信息。

<0：执行失败。

#### 12.dwmon\_get\_group\_info

**函数原型：**

```
DwMonGroup

dwmon_get_group_info(

    String group_name

);
```

**功能说明：**

获取指定组的守护进程组信息。

**参数说明：**

group\_name: 输入参数，指定要获取信息的组名，只有一组时可以不指定。

**返回值：**

返回 DwMonGroup 对象，该对象结构如下：

```
DwMonGroup：
Integer     oguid：oguid值
Integer     dwNum：dmwatcher个数
String[]     dwIpArray：dmwatcher的ip
Integer[]    dwPortArray: dmwatcher的port

String     dwType: dmwatcher配置的类型local/global
String      dwMode: 故障切换模式auto/manual
String      primaryName: 主实例名

Integer     splitNum：分裂组个数
String[]     splitNameArray: 分裂组ctl文件最新的实例名

Integer     dbNum：非本地库个数
String[]     dbNameArray: 非本地库名数组

Integer     localNum：本地实例个数
String[]     localNameArray: 本地实例名数组

Integer     returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonGroup 的其他对象成员获取监控组信息。

<0：执行失败。

#### 13.dwmon\_get\_split\_sub\_group\_database

**函数原型：**

```
DwMonDatabaseNameArray

dwmon_get_split_sub_group_database(

    String group_name,

    String db_name

);
```

**功能说明：**

获取可加入指定库的库名信息。

**参数说明：**

group\_name: 输入参数，指定实例所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要获取可加入信息的实例名，此参数必须指定。

**返回值：**

返回 DwMonDatabaseNameArray 对象，该对象结构如下：

```
DwMonDatabaseNameArray ：
Integer dbNum：从属于该库的个数，不一定是备机，也可能是其他从属的主机
String[] nameArray : 库名数组
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功, 可通过 DwMonDatabaseNameArray 的其他对象成员获取实例信息。

<0：执行失败。

#### 14.dwmon\_get\_nth\_database\_info

**函数原型：**

```
DwMonDatabase

dwmon_get_nth_database_info(

    String group_name,

    int nth

);
```

**功能说明：**

获取指定组中第 nth 个库的全局信息，这里的 nth 是根据 dmmonitor.ini 指定组中所配置的守护进程先后顺序来排序的，每个组的 nth 都是从 0 开始，依次递增。

**参数说明：**

group\_name: 输入参数，指定的守护进程组名，只有一组时可以不指定。

nth: 输入参数，输入要获取的数据库实例下标。

**返回值：**

返回 DwMonDatabase 对象，该对象结构如下：

```
DwMonDatabase：
Integer returnCode : 执行结果
String dwTime:守护进程最近一次收到本地dmserver消息的时间，取自控制守护进程。在系统时间一致的情况下，可用于计算监视器和dmserver间的延迟时间。NULL表示未收到过本地dmserver消息
String dwIp:守护进程IP地址
Integer dwPort:守护进程TCP端口
String dwType:守护类型
String dwMode:故障切换模式
Integer dwErrTime:远程守护进程故障认定时间间隔
String dwSta:守护进程状态
String dwSubSta:守护进程子状态
String dwCtlSta:守护进程控制文件状态
String dbName:实例名
String dbOkString:实例是否正常
String svrMode:实例模式
String svrStatus:实例状态
String archType:库上主ep配置的归档类型
String archStatus:当前库为realtime/timely备库时，主库到当前备库的归档状态
Long pmntMagic:数据库永久魔数
Long dbMagic:数据库魔数
Integer epNum:库中的ep个数
Integer[] epSeqno:库中的ep seqno数组
String[] epName:库中的ep实例名数组
Integer dscCtlNode:库中控制ep的seqno
String dscStatus:库的hpc状态
Integer okEpNum:库中的ok ep个数
Integer[] okEpArr:库中的ok ep的seqno数组
Integer breakEpNum:当前正在故障处理的节点数
Integer[] breakEpArr:当前正在故障处理的ep seqno数组
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonDatabase 的其他对象成员获取实例信息。

<0：执行失败。

#### 15.dwmon\_get\_database\_info\_by\_name

**函数原型：**

```
DwMonDatabase

dwmon_get_database_info_by_name(

    String group_name,

    String db_name

);
```

**功能说明：**

根据指定的数据库名称获取库的全局信息。

**参数说明：**

group\_name: 输入参数，指定的守护进程组名，只有一组时可以不指定。

db\_name: 输入参数，指定要获取信息的数据库名称。

**返回值：**

返回 DwMonDatabase 对象，该对象结构如下：

```
DwMonDatabase：
Integer returnCode : 执行结果
String dwTime:守护进程当前时间
String dwIp:守护进程IP地址
Integer dwPort:守护进程TCP端口
String dwType:守护类型
String dwMode:故障切换模式
Integer dwErrTime:远程守护进程故障认定时间间隔
String dwSta:守护进程状态
String dwSubSta:守护进程子状态
String dwCtlSta:守护进程控制文件状态
String dbName:实例名
String dbOkString:实例是否正常
String svrMode:实例模式
String svrStatus:实例状态
String archType:库上主ep配置的归档类型
String archStatus:当前库为realtime/timely备库时，主库到当前备库的归档状态
Long pmntMagic:数据库永久魔数
Long dbMagic:数据库魔数
Integer epNum:库中的ep个数
Integer[] epSeqno:库中的ep seqno数组
String[] epName:库中的ep实例名数组
Integer dscCtlNode:库中控制ep的seqno
String dscStatus:库的hpc状态
Integer okEpNum:库中的ok ep个数
Integer[] okEpArr:库中的ok ep的seqno数组
Integer breakEpNum:当前正在故障处理的节点数
Integer[] breakEpArr:当前正在故障处理的ep seqno数组
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonDatabase 的其他对象成员获取实例信息。

<0：执行失败。

#### 16.dwmon\_get\_database\_info

**函数原型：**

```
DwDbInfo

dwmon_get_database_info(

    String group_name,

    String db_name

);
```

**功能说明：**

获取指定库上的实例信息。

**参数说明：**

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取实例信息的数据库名称。

**返回值：**

返回 DwDbInfo 对象，该对象结构如下：

```
DwDbInfo：
Integer returnCode : 执行结果
Integer epNum:ep个数
Integer[] epSeqno:所有ep的seqno数组
String[] epName:所有ep实例名数组
Integer dscCtlNode:库中控制ep的seqno
String dscStatus:库的hpc状态
Integer okEpNum:库中ok ep个数
Integer[] okEpArray:库中ok ep的seqno数组
Integer breakEpNum:当前正在故障处理的节点数
Integer[] breakEpArray:当前正在故障处理的ep seqno数组
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwDbInfo 的其他对象成员获取实例信息。

<0：执行失败。

#### 17.dwmon\_get\_nth\_ep\_info

**函数原型：**

```
DwEpInfo

dwmon_get_nth_ep_info(

    String group_name,

    String db_name,

    int nth

);
```

**功能说明：**

获取指定库上第 nth 个实例信息，可先通过 dwmon\_get\_database\_info 接口获取到库上的节点实例个数 n\_ep，nth 取值范围为\[0,n\_ep–1\]。

**参数说明：**

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取实例信息的数据库名称，此参数必须指定。

nth: 输入参数，指定要获取 db\_name 库上的第 nth 个实例信息。

**返回值：**

返回 DwEpInfo 对象，该对象结构如下：

```
DwEpInfo：
Integer returnCode : 执行结果
Integer epName:ep实例名
Integer epPort:实例端口号
String epOkStr:实例是否正常
String svrMode:实例模式
String svrStatus:实例状态
String primInst:对应PRIMARY实例名
String primMalSta:对应PRIMARY实例到本实例的MAL链路状态  只对备库有效，输出主库主ep到ep_name所在的备库主ep的mal链路状态
String primArchType:对应PRIMARY实例到本实例的归档类型
String primArchSta:对应PRIMARY实例到本实例的归档状态，只对备库有效，输出主库主ep到ep_name所在的备库主ep的归档状态
Long fseq:已写入联机日志的rlog_pkg包序号
Long flsn:已写入联机日志的flsn值，对应的包序号为fseq
Long cseq:系统当前已经分配的最大RLOG_PKG包序号
Long clsn:系统当前已经分配的最大LSN值，对应的包序号为cseq
String archType:实例自身配置的归档类型realtime/timely
Integer archNum:实例自身配置的realtime/timely归档数
Integer asyncNum:实例自身配置的异步归档数
Integer dscSeqno:实例的seqno
String gDwStatus:ep上设置的全局状态标记
Integer mppFlagMem:内存中的mpp_ini
Integer mppFlagFile:ini文件中的mpp_ini
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwEpInfo 的其他对象成员获取实例信息。

<0：执行失败。

#### 18.dwmon\_get\_ep\_info\_by\_name

**函数原型：**

```
DwEpInfo

dwmon_get_ep_info_by_name(

    String group_name,

    String ep_name

);
```

**功能说明：**

根据指定的实例名获取实例的详细信息。

**参数说明：**

group\_name: 输入参数，输入指定实例所在的守护进程组名，如果只有一组可以不指定。

ep\_name: 输入参数，输入要获取信息的实例名。

**返回值：**

返回 DwEpInfo 对象，该对象结构如下：

```
DwEpInfo：
Integer returnCode : 执行结果
Integer epName:ep实例名
Integer epPort:实例端口号
String epOkStr:实例是否正常
String svrMode:实例模式
String svrStatus:实例状态
String primInst:对应PRIMARY实例名
String primMalSta:对应PRIMARY实例到本实例的MAL链路状态  只对备库有效，输出主库主ep到ep_name所在的备库主ep的mal链路状态
String primArchType:对应PRIMARY实例到本实例的归档类型
String primArchSta:对应PRIMARY实例到本实例的归档状态，只对备库有效，输出主库主ep到ep_name所在的备库主ep的归档状态
Long fseq:已写入联机日志的rlog_pkg包序号
Long flsn:已写入联机日志的flsn值，对应的包序号为fseq
Long cseq:系统当前已经分配的最大RLOG_PKG包序号
Long clsn:系统当前已经分配的最大LSN值，对应的包序号为cseq
String archType:实例自身配置的归档类型realtime/timely
Integer archNum:实例自身配置的realtime/timely归档数
Integer asyncNum:实例自身配置的异步归档数
Integer dscSeqno:实例的seqno
String gDwStatus:ep上设置的全局状态标记
Integer mppFlagMem:内存中的mpp_ini
Integer mppFlagFile:ini文件中的mpp_ini
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwEpInfo 的其他对象成员获取实例信息。

<0：执行失败。

#### 19.dwmon\_get\_database\_arch\_info

**函数原型：**

```
DwMonArch

dwmon_get_database_arch_info(

    String group_name,

    String db_name

);
```

**功能说明：**

获取指定库配置的归档信息，包括归档目标实例名，到归档目标的 mal 链路状态和归档状态，以及异步归档信息。

**参数说明：**

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取归档信息的数据库名称。

**返回值：**

返回 DwMonArch 对象，该对象结构如下：

```
DwMonArch：
Integer returnCode : 执行结果
String archType:配置的归档类型realtime/timely/mpp
Integer archNum:配置realtime/timely/mpp归档数
String[] archDest:归档目标实例名数组
String[] malSta:mal链路状态数组
String[] archSta:归档状态数组
Integer asyncNum:配置异步归档数
String[] asyncDest:异步归档目标实例名数组
String[] asyncMalSta:到异备的mal链路状态数组
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonArch 的其他对象成员获取相关归档信息。

<0：执行失败。

#### 20.dwmon\_get\_watch\_ctl\_info

**函数原型：**

```
DwCtlInfo

dwmon_get_watch_ctl_info(

    String group_name,

    String db_name

);
```

**功能说明：**

获取指定库的守护进程控制文件状态信息。

**参数说明：**

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取控制文件信息的守护进程对应的数据库名称。

**返回值：**

返回 DwCtlInfo 对象，该对象结构如下：

```
DwCtlInfo：
Integer returnCode : 执行结果
String ctlStatus:输出守护进程控制文件状态
String desc:输出本地分裂库的描述信息，如果是有效状态，描述信息为空
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwCtlInfo 的其他对象成员获取相关控制文件信息。

<0：执行失败。

#### 21.dwmon\_get\_database\_open\_history

**函数原型：**

```
DwOpenHistory

dwmon_get_database_open_history(

    String group_name,

    String db_name

);
```

**功能说明：**

获取指定库的 OPEN 记录项个数。

**参数说明：**

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取 OPEN 记录的守护进程对应的数据库名称。

**返回值：**

返回 DwOpenHistory 对象，该对象结构如下：

```
DwOpenHistory：
Integer returnCode : 执行结果
Integer ctlNum:OPEN记录项个数
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwOpenHistory 的其他对象成员获取相关 OPEN 记录信息。

<0：执行失败。

#### 22.dwmon\_get\_nth\_open\_history

**函数原型：**

```
DwOpenHistory

dwmon_get_nth_open_history(

    String group_name,

    String db_name,

    int nth

);
```

**功能说明：**

获取指定组中指定库的第 nth 个 open 记录信息。

**参数说明：**

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取 OPEN 记录的守护进程对应的数据库名称。

nth: 输入参数，输入要获取指定第 nth 个 OPEN 记录项。

**返回值：**

返回 DwOpenHistory 对象，该对象结构如下：

```
DwOpenHistory：
Integer returnCode : 执行结果
String tGuid:OPEN记录唯一标识
Long rowid:系统表所在行的rowid值
String time:OPEN的时间点
String sysMode:OPEN时所处的系统模式（PRIMARY/NORMAL）
String pDbName:对应主库的实例名
String cDbName:当前库的实例名
Integer pDbMagic:对应主库的db_magic值
Integer cDbMagic:当前库的db_magic值
Integer epNum:指定库中包含的节点实例个数
Long[] aseqArr:pkg_seqno数组
Long[] alsnArr:apply_lsn数组
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwOpenHistory 的其他对象成员获取相关 OPEN 记录信息。

<0：执行失败。

#### 23.dwmon\_get\_watch\_config\_info

**函数原型：**

```
DwConfigInfo

dwmon_get_watch_config_info(

    String group_name,

    String inst_name

);
```

**功能说明：**

获取指定实例本地的守护进程配置信息。

**参数说明：**

group\_name: 输入参数，只有一组时允许不指定。

inst\_name: 输入参数，指定要获取配置信息的守护进程本地的实例名。

**返回值：**

返回 DwConfigInfo 对象，该对象结构如下：

```
DwConfigInfo：
Integer returnCode : 执行结果
String groupName:输入组名为空串的情况下，接口会输出实例所在的守护进程组名
String instName:要获取配置信息的守护进程本地的实例名
String dwType:dmwatcher.ini的dw_type配置值
String dwMode:mwatcher.ini的dw_mode配置值
Integer dwErrorTime:dmwatcher.ini的dw_error_time配置值
Integer instOguid:dmwatcher.ini的inst_oguid配置值
Integer instErrorTime:dmwatcher.ini的inst_error_time配置值
Integer instRecoverTime:dmwatcher.ini的inst_recover_time配置值
String instIni:dmwatcher.ini的inst_ini配置值
String dcrIni:dmwatcher.ini的dcr_ini配置值（守护DMDSC集群时需要配置）
Integer instAutoRestart:dmwatcher.ini的inst_auto_restart配置值
String instStartupCmd:dmwatcher.ini的inst_startup_cmd配置值
Integer instHostCheck:守护进程是否检查实例对外服务IP的网卡故障，0表示不检查，1表示检查
Integer rlogSendThreshold:主库发送日志到备库的时间阈值
Integer rlogApplyThreshold:备库重演日志的时间阈值
String dcsStartupCmd:dmwatcher.ini的dcs_startup_cmd配置值；该参数已废弃，输出值无实际意义
String dcsIni:dmwatcher.ini的dcs_ini配置值；该参数已废弃，输出值无实际意义
Integer dcsPort:dmwatcher.ini的dcs_port配置值；该参数已废弃，输出值无实际意义
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwConfigInfo 的其他对象成员获取配置信息。

<0：执行失败。

#### 24.dwmon\_get\_css\_config\_info

**函数原型：**

```
DcrConfigInfo

dwmon_get_css_config_info(

    String group_name,

    String inst_name

);
```

**功能说明：**

获取和指定实例的 dcr\_seqno 相同的 dmcss 配置的自动拉起检测间隔（DMDCR\_ASM\_RESTART\_INTERVAL、DMDCR\_DB\_RESTART\_INTERVAL）。

**参数说明：**

group\_name: 输入参数，只有一组时允许不指定。

inst\_name: 输入参数，指定要获取配置信息的实例名。

**返回值：**

返回 DcrConfigInfo 对象，该对象结构如下：

```
DcrConfigInfo：
Integer returnCode : 执行结果
String groupName:输入组名为空串的情况下，接口会输出实例所在的守护进程组名
String instName:要获取配置信息的守护进程本地的实例名
Integer asmRestartItvl:dmdcr.ini的asm_restart_itvl配置值
Integer dbRestartItvl:dmdcr.ini的db_restart_itvl配置值
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DcrConfigInfo 的其他对象成员获取配置信息。

<0：执行失败。

#### 25.dwmon\_get\_monitor\_info

**函数原型：**

```
DwMonInfo

dwmon_get_monitor_info (

    String group_name,

    String db_name

);
```

**功能说明：**

获取指定守护进程的监视器连接信息。同一个守护系统中允许最多 10 个监视器同时启动连接到守护进程，可通过调用此接口获取指定守护进程上的监视器连接信息，包括连接时间、确认监视器配置、监视器 ID、监视器 IP 和监视器版本信息。

其中 db\_name 是输入输出参数，表示指定守护进程对应的实例名，如果此参数为空，则根据 dmmonitor.ini 对应组中的配置顺序，选择第一个活动的守护进程获取监视器连接信息，并输出选中的守护进程本地库名称；如果指定有合法值，则返回指定库的控制守护进程上的监视器连接信息。

**参数说明：**

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取信息的守护进程对应的实例名。

**返回值：**

返回 DwMonInfo 对象，该对象结构如下：

```
DwMonInfo：
Integer returnCode : 执行结果
String dbName:在db_name为空串的情况下，会作为输出参数输出实际获取信息的实例名
Integer monNum:守护进程上连接的监视器总个数
String[] connTimeArray:守护进程上建立连接的时间，数组长度是n_mon的输入值
Integer[] confirmArray:监视器的确认配置信息，数组长度是n_mon的输入值
Long[] midArray:monitor唯一ID数组，和n_mon对应
String[] monIpArray:monitor的IP地址数组，和n_mon对应
String[] monVersionArray:monitor的版本信息，和n_mon对应
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonInfo 的其他对象成员获取记录项信息，取出的第一个数组元素是当前 monitor 的连接信息。

<0：执行失败。

#### 26.dwmon\_set\_cmd\_execing\_with\_command

**函数原型：**

```
int

dwmon_set_cmd_execing_with_command(

    String command

);
```

**功能说明：**

如果上层有控制台工具界面，通过用户输入命令的方式调用接口，可通过此接口设置命令执行标记并传入用户执行的命令串信息，用于监视器 log 日志记录用户的操作信息。

在确认监视器模式下或者监视器设置有自动记录系统状态间隔（通过 dwmon\_set\_show\_interval 或者 dwmon\_set\_log\_interval 设置），调用命令接口之前，需要先调用此接口设置执行标记，避免和确认监视器自动接管故障主库或者监视器自动记录系统状态的操作发生冲突。

**参数说明：**

command：输入参数，如果上层有控制台工具界面，则表示用户手工输入的执行命令串，允许为 NULL 或空串。

**返回值：**

0：执行成功。

<0：执行失败。

#### 27.dwmon\_reset\_cmd\_execing

**函数原型：**

```
int

dwmon_reset_cmd_execing();
```

**功能说明：**

重置命令执行标记，和 dwmon\_set\_cmd\_execing\_with\_command 接口配合使用，在调用命令接口执行完成后，需要调用此接口，重置执行标记，避免确认监视器无法执行自动接管故障主库的操作。

**参数说明：**

无

**返回值：**

0：执行成功。

<0：执行失败。

#### 28.dwmon\_get\_dw\_confirm

**函数原型：**

```
DwMonData

dwmon_get_dw_confirm();
```

**功能说明：**

获取确认监视器标记，用于判断当前的监视器是否为确认监视器。

**参数说明：**

无

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：1：是确认监视器， 0：不是确认监视器
String stringValue : ""
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过对象成员 dataValue 获取确认标记，1：是确认监视器，0：不是确认监视器。

<0：执行失败。

#### 29.dwmon\_set\_show\_interval

**函数原型：**

```
int

dwmon_set_show_interval(

    int show_interval

);
```

**功能说明：**

监视器根据指定的 show\_interval 值，每隔 show\_interval 个时间间隔，自动输出各实例的状态信息给用户，需要使用 dwmon\_get\_exec\_msg 接口获取到输出消息，show\_interval 单位为秒，缺省值为 0。

**参数说明：**

show\_interval:输入参数，设置定时输出状态信息的时间间隔，单位为秒，取值为 0，或 5~3600，取值为 0 表示取消自动输出，缺省值为 0。

**返回值：**

0：执行成功。

<0：执行失败。

#### 30.dwmon\_get\_show\_interval

**函数原型：**

```
DwMonData

dwmon_get_show_interval();
```

**功能说明：**

获取当前设置的自动显示时间间隔，单位为秒。

**参数说明：**

无

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：当前设置的自动显示时间间隔
String stringValue : ""
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：获取成功，可通过对象成员 dataValue 获取自动显示间隔。

<0：获取失败。

#### 31.dwmon\_set\_log\_interval

**函数原型：**

```
int

dwmon_set_log_interval(

    int log_interval

);
```

**功能说明：**

监视器按照设置的 log\_interval 值，每隔 log\_interval 个时间间隔，自动将各实例的状态信息写入到日志文件，log\_interval 单位为秒，缺省值为 1。

**参数说明：**

log\_interval:输入参数，设置定时写入状态信息到日志文件的时间间隔，单位为秒，取值为 0，1 或 5~3600。

取值为 0 表示不写入任何信息到日志文件。

取值为 1 表示只写入普通的状态变化日志，例如收到新的信息或者检测到状态变化等。

取值为 5~3600 范围内的数值时，除了生成普通日志信息外，会按照设置的间隔定期写入站点状态信息到日志文件中。

**返回值：**

0：执行成功。

<0：执行失败。

#### 32.dwmon\_get\_log\_interval

**函数原型：**

```
DwMonData

dwmon_get_log_interval();
```

**功能说明：**

获取当前设置的自动写入日志的时间间隔，单位为秒。

**参数说明：**

无

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：当前设置的自动写入日志的时间间隔
String stringValue : ""
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：获取成功，可通过对象成员 dataValue 获取自动写入日志文件间隔。

<0：获取失败。

#### 33.dwmon\_set\_log\_file\_size

**函数原型：**

```
int

dwmon_set_log_file_size(

    int log_file_size

);
```

**功能说明：**

调用此接口，可以设置监视器单个的日志文件大小，达到最大值后，会自动生成并切换到新的日志文件中，如果达到最大的日志总空间限制，会自动删除创建时间最早的日志文件，日志文件命名方式为“dmmonitor\_年月日时分秒.log”，例如“dmmonitor\_20160201155820.log”。

**参数说明：**

log\_file\_size: 输入参数，设置单个日志文件大小，单位为 M，取值范围为 16~2048，缺省值为 64。

**返回值：**

0：执行成功。

<0：执行失败。

#### 34.dwmon\_get\_log\_file\_size

**函数原型：**

```
DwMonData

dwmon_get_log_file_size();
```

**功能说明：**

获取当前设置的单个日志文件大小，单位为 M。

**参数说明：**

无

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：获取当前设置的单个日志文件大小
String stringValue : ""
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：获取成功，可通过对象成员 dataValue 获取单个日志文件大小。

<0：获取失败。

#### 35.dwmon\_get\_log\_path

**函数原型：**

```
DwMonData

dwmon_get_log_path();
```

**功能说明：**

获取当前的日志文件路径。

**参数说明：**

无

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：0
String stringValue : 当前的日志文件路径
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过对象成员 stringValue 获取日志文件路径。

<0：执行失败。

#### 36.dwmon\_set\_log\_space\_limit

**函数原型：**

```
int

dwmon_set_log_space_limit(

    int log_space_limit

);
```

**功能说明：**

调用此接口，可以设置监视器的日志总空间大小，达到设置的总空间大小后，会自动删除创建时间最早的日志文件。

**参数说明：**

log\_space\_limit: 输入参数，设置日志总空间大小，单位为 M，取值范围为 0 或 256~4096，缺省值为 0，表示没有空间限制。

**返回值：**

0：执行成功。

<0：执行失败。

#### 37.dwmon\_get\_log\_space\_limit

**函数原型：**

```
DwMonData
dwmon_get_log_space_limit();
```

**功能说明：**

获取当前设置的日志总空间大小，单位为 M。

**参数说明：**

无

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：当前设置的日志总空间大小
String stringValue : ""
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过对象成员 dataValue 获取当前设置的日志总空间大小。

<0：执行失败。

#### 38.dwmon\_login

**函数原型：**

```
int 
dwmon_login(
    String             username, 
    String             password
);
```

**功能说明：**

登录监视器，这里的登录口令和服务器的登录口令是一致的，且必须有 DBA 权限。

校验登录信息时由守护进程转发给服务器校验，并返回校验结果给监视器，因此需要保证系统中至少有一个活动库，否则无法校验成功。

**参数说明：**

username: 输入参数，登录用户名。

password: 输入参数，登录密码。

**返回值：**

0：执行成功。

<0：执行失败。

#### 39\. dwmon\_login\_with\_key

**函数原型：**

```
int
dwmon_login_with_key(
    String          login_str
);
```

**功能说明：**

Key 认证方式登录监视器。

**参数说明：**

login\_str：输入参数，登录连接串。

**返回值：**

0：执行成功。

<0：执行失败。

#### 40.dwmon\_logout

**函数原型：**

```
int

dwmon_logout();
```

**功能说明：**

退出登录监视器。

**参数说明：**

无

**返回值：**

0：执行成功。

<0：执行失败。

#### 41.dwmon\_set\_database\_recover\_time

**函数原型：**

```
int

dwmon_set_database_recover_time(

    String group_name,

    String db_name,

    int recover_time

);
```

**功能说明：**

设置指定备库的恢复间隔时间，设置成功后，recover\_time 值保存在对应主库的守护进程内存中，并且只对指定的备库起作用。

此接口只允许对指定备库执行修改操作，如果需要考虑对某个组或所有组中的备库执行修改操作，则可以使用 dwmon\_set\_group\_recover\_time 接口来实现。

执行此操作需要先登录监视器。

**参数说明：**

group\_name：输入参数，指定执行操作的守护进程组名，只有一组时可以不指定组名。

db\_name：输入参数，指定要设置恢复间隔时间的备库实例名。

recover\_time：输入参数，指定要设置的恢复间隔时间，单位秒，取值范围 3~86400，详细说明可参考 [3.1.9 故障恢复处理](data-watch-daemon.md) 。

**返回值：**

0：执行成功。

<0：执行失败。

#### 42.dwmon\_set\_database\_arch\_invalid

**函数原型：**

```
int

dwmon_set_database_arch_invalid(

    String group_name,

    String db_name

);
```

**功能说明：**

设置主库到指定备库的归档状态无效。

此接口只允许对指定备库设置归档无效，如果需要考虑对某个组或所有组中的备库执行设置操作，则可以使用 dwmon\_set\_group\_arch\_invalid 接口来实现。

执行此操作需要先登录监视器。

**参数说明：**

group\_name: 输入参数，指定执行操作的守护进程组名，只有一组时可以不指定组名。

db\_name：输入参数，指定要修改归档状态无效的备库实例名。

**返回值：**

0：执行成功。

<0：执行失败。

#### 43.dwmon\_startup\_database\_watch

**函数原型：**

```
int

dwmon_startup_database_watch(

    String group_name,

    String db_name

);
```

**功能说明：**

打开指定库的守护进程监控功能，守护进程启动后，默认监控功能处于打开状态。

对 DMDSC 集群，此接口只通知控制守护进程执行。

**参数说明：**

group\_name: 输入参数，指定要打开监控的守护进程组名，只有一组时可以不指定组名。

db\_name：输入参数，指定要打开监控的守护进程的本地实例名。

**返回值：**

\>=0：执行成功，执行前守护进程的监控已经处于打开状态时，返回值为 100。

<0：执行失败。

#### 44.dwmon\_startup\_watch

**函数原型：**

```
int

dwmon_startup_watch(

    String group_name

);
```

**功能说明：**

打开指定组的守护进程监控功能，守护进程启动后，默认监控功能处于打开状态。

对 DMDSC 集群，此接口只通知控制守护进程执行。

**参数说明：**

group\_name: 输入参数，指定要打开监控的守护进程组名，只有一组时可以不指定组名。

**返回值：**

\>=0：执行成功，执行前组中所有守护进程的监控已经处于打开状态时，返回值为 100。

<0：执行失败。

#### 45.dwmon\_startup\_watch\_all

**函数原型：**

```
int

dwmon_startup_watch_all();
```

**功能说明：**

打开所有组的守护进程监控功能，守护进程启动后，默认监控功能处于打开状态。

只有 MPP 主备环境下允许调用此接口。

**参数说明：**

无 **返回值：**

\>=0：执行成功，执行前所有组守护进程的监控已经处于打开状态时，返回值为 100。

<0：执行失败。

#### 46.dwmon\_stop\_database\_watch

**函数原型：**

```
int

dwmon_stop_database_watch(

    String group_name,

    String db_name

);
```

**功能说明：**

关闭指定库的守护进程的监控功能，监控功能被关闭后，守护进程还可以正常地接收和发送消息，但无法根据当前的实例状态来自动处理故障以及实例的自动拉起等，关闭后守护进程处于 Shutdown 状态。

如果需要正常地退出实例或者保持实例为 Mount 状态，则可以关闭监控功能，否则建议保持监控功能为打开状态，以保证能够及时处理系统的各种情况。

对 DMDSC 集群，此接口只通知控制守护进程执行。

执行此操作需要先登录监视器。

**参数说明：**

group\_name: 输入参数，指定要关闭监控的守护进程组名，只有一组时可以不指定组名。

db\_name：输入参数，指定要关闭监控的守护进程的本地实例名。

**返回值：**

\>=0：守护进程的监控关闭成功。执行前守护进程的监控已经处于关闭状态时，返回值为 100。

<0：执行失败

#### 47.dwmon\_stop\_watch

**函数原型：**

```
int

dwmon_stop_watch(

    String group_name

);
```

**功能说明：**

关闭指定组的所有守护进程的监控功能，监控功能被关闭后，守护进程还可以正常地接收和发送消息，但无法根据当前的实例状态来自动处理故障以及实例的自动拉起等，关闭后守护进程处于 Shutdown 状态。

如果需要正常地退出实例或者保持实例为 Mount 状态，则可以关闭监控功能，否则建议保持监控功能为打开状态，以保证能够及时处理系统的各种情况。

对 DMDSC 集群，此接口只通知控制守护进程执行。

执行此操作需要先登录监视器。

**参数说明：**

group\_name: 输入参数，指定要关闭监控的守护进程组名，只有一组时可以不指定组名。

**返回值：**

\>=0：所有守护进程的监控关闭成功。执行前组中所有守护进程的监控已经处于关闭状态时，返回值为 100。

<0：执行失败

#### 48.dwmon\_stop\_watch\_all

**函数原型：**

```
int

dwmon_stop_watch_all();
```

**功能说明：**

关闭所有组的守护进程监控功能，监控功能被关闭后，守护进程还可以正常地接收和发送消息，但无法根据当前的实例状态来自动处理故障以及实例的自动拉起等，关闭后守护进程处于 Shutdown 状态。

如果需要正常地退出实例或者保持实例为 Mount 状态，则可以关闭监控功能，否则建议保持监控功能为打开状态，以保证能够及时处理系统的各种情况。

执行此操作需要先登录监视器，只有 MPP 主备环境下允许调用此接口。

**参数说明：**

无

**返回值：**

\>=0：所有守护进程的监控关闭成功，执行前所有组守护进程的监控已经处于关闭状态时，返回值为 100。

<0：执行失败。

#### 49.dwmon\_startup\_group

**函数原型：**

```
int

dwmon_startup_group(

    String group_name

);
```

**功能说明：**

启动指定组的所有实例，在 dmwatcher.ini 中 INST\_AUTO\_RESTART 配置为 0 时该接口可以成功执行，配置为 1 时在守护进程的监控功能打开的情况下，守护进程可以自动完成启动实例的功能，不需要再调用接口执行。

对 DMDSC 集群，由 dmcss 执行拉起动作，和 dmwatcher.ini 中的 INST\_AUTO\_RESTART 配置参数没有关系，由 dmdcr.ini 中的配置参数决定是否可以执行自动拉起，如果某个实例可以被 dmcss 自动拉起，则 dmcss 会忽略收到的拉起命令，等待自动拉起。

**参数说明：**

group\_name: 输入参数，指定要启动实例的守护进程组名，只有一组时可以不指定。

**返回值：**

\>=0：所有实例都启动成功，执行前组中所有实例已经处于活动状态时，返回值为 100。

<0：执行失败。

#### 50.dwmon\_startup\_group\_all

**函数原型：**

```
int

dwmon_startup_group_all();
```

**功能说明：**

启动所有组的实例，在 dmwatcher.ini 中 INST\_AUTO\_RESTART 配置为 0 时该接口可以成功执行，配置为 1 时在守护进程的监控功能打开的情况下，守护进程可以自动完成启动实例的功能，不需要再调用接口执行。

只有 MPP 主备环境下允许调用此接口。

**参数说明：**

无

**返回值：**

\>=0：所有实例都启动成功，执行前所有组的实例已经处于活动状态时，返回值为 100。

<0：执行失败。

#### 51.dwmon\_stop\_group

**函数原型：**

```
int

dwmon_stop_group(

    String group_name

);
```

**功能说明：**

关闭指定组中的所有活动实例，关闭所有活动实例之前，会先关闭所有控制守护进程的监控功能，避免守护进程将实例再次拉起。

对 DMDSC 集群，是由 dmcss 执行退出操作，在 dmcss 通知所有实例退出之前，会先关闭 dmcss 的自动拉起功能。

执行此操作需要先登录监视器，另外关闭守护进程只是将守护进程切换为 Shutdown 状态，并没有退出。

**参数说明：**

group\_name: 输入参数，指定要关闭实例的守护进程组名，只有一组时可以不指定。

**返回值：**

\>=0：所有实例都退出成功，执行前组中实例已经全部退出时，返回值为 100。

<0：执行失败。

#### 52.dwmon\_stop\_group\_all

**函数原型：**

```
int

dwmon_stop_group_all();
```

**功能说明：**

关闭所有组的所有活动实例，关闭实例之前，会先关闭所有守护进程的监控功能，避免守护进程将实例再次拉起。

只有 MPP 主备环境下允许调用此接口，执行此操作需要先登录监视器，另外关闭守护进程只是将守护进程切换为 Shutdown 状态，并没有退出。

**参数说明：**

无

**返回值：**

\>=0：所有实例都退出成功，执行前所有组的实例已经全部退出时，返回值为 100。

<0：执行失败。

#### 53.dwmon\_kill\_group

**函数原型：**

```
int

dwmon_kill_group(

    String group_name

);
```

**功能说明：**

强制杀掉指定组中的活动实例。

调用 dwmon\_stop\_group 关闭指定组的实例时，如果实例正在执行守护进程发起的命令，或者守护进程不是 STARTUP、OPEN 或 RECOVERY 状态，会导致接口执行失败，在这种情况下，如果需要强制关闭实例，则可以通过调用 dwmon\_kill\_group 接口来完成。

此接口执行时不要求先登录监视器，并且也会将守护进程切换为 Shutdown 状态（如果已经是 Shutdown 状态则跳过不再切换），避免守护进程将实例重新拉起。

**参数说明：**

group\_name: 输入参数，指定要强杀实例的守护进程组名，只有一组时可以不指定。

**返回值：**

\>=0：所有实例都退出成功，执行前组中实例已经全部退出并且守护进程都是 Shutdown 状态时返回值为 100。

<0：执行失败。

#### 54.dwmon\_kill\_group\_all

**函数原型：**

```
int

dwmon_kill_group_all();
```

**功能说明：**

强制杀掉所有组中的活动实例。

调用 dwmon\_stop\_group\_all 关闭所有组的实例时，如果实例正在执行守护进程发起的命令，或者守护进程不是 STARTUP、OPEN 或 RECOVERY 状态，会导致接口执行失败，在这种情况下，如果需要强制关闭实例，则可以通过调用 dwmon\_kill\_group\_all 接口来完成。

只有 MPP 主备环境下允许调用此接口，此接口执行时不要求先登录监视器，并且也会将守护进程切换为 Shutdown 状态（如果已经是 Shutdown 状态则跳过不再切换），避免守护进程将实例重新拉起。

**参数说明：**

无

**返回值：**

\>=0：所有实例都退出成功，执行前所有组的实例已经全部退出并且守护进程都是 Shutdown 状态则返回值为 100。

<0：执行失败。

#### 55.dwmon\_startup\_database

**函数原型：**

```
int

dwmon_startup_database(

    String group_name,

    String db_name

);
```

**功能说明：**

启动指定组中指定的数据库实例。

如果指定的库是单机，则由守护进程执行拉起动作，如果指定的库是 DMDSC 集群，则由守护进程再去通知主从 css 各自执行拉起动作。

此命令执行前，如果守护进程处于 Shutdown 状态，会将其切换为 Startup 状态，如果主从 css 的自动拉起功能是关闭的，在各节点实例拉起成功后，会将其打开。

**参数说明：**

group\_name: 输入参数，指定要启动的库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要启动的数据库名称，此参数必须指定。

**返回值：**

\>=0：执行成功，执行前库已经处于活动状态，或守护进程配置了自动拉起且监控没有被关闭时返回值为 100。

<0：执行失败。

#### 56.dwmon\_stop\_database

**函数原型：**

```
int

dwmon_stop_database(

    String group_name,

    String db_name

);
```

**功能说明：**

关闭指定组中指定的数据库实例。

如果指定的库是单机，则由守护进程通知单机库正常退出，如果指定的库是 DMDSC 集群，则由守护进程再去通知主 css 依次退出每个节点实例。

此命令执行完成后，会将守护进程切换为 Shutdown 状态，并将主从 css 的自动拉起功能关闭。

> **注意**
> 
> 如果要退出的是全局守护类型的备库，为了避免触发主库的Failover动作，要求此备库已经被detach分离出去，也就是备库归档要处于无效状态，才允许将其正常退出。  
> 如果要退出的是主库，在自动切换模式下，为了避免触发备库的自动接管，要求所有备库都已经被detach分离出去，也就是所有备库归档都处于无效状态，才允许退出主库，手动切换模式下没有此要求。

**参数说明：**

group\_name: 输入参数，指定要关闭的库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要关闭的数据库名称，此参数必须指定。

**返回值：**

\>=0：执行成功，执行前库已经退出时返回值为 100。

<0：执行失败。

#### 57.dwmon\_kill\_database

**函数原型：**

```
int

dwmon_kill_database(

    String group_name,

    String db_name

);
```

**功能说明：**

强制关闭指定组中指定的数据库实例。

如果指定的库是单机，则由守护进程强制杀掉指定库的进程，如果指定的库是 DMDSC 集群，则由守护进程再去通知主 css 强杀所有节点实例。

注意：此命令执行完成后，会将守护进程切换为 Shutdown 状态。

**参数说明：**

group\_name: 输入参数，指定要强制关闭的库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要强制关闭的数据库名称，此参数必须指定。

**返回值：**

\>=0：执行成功，执行前库已经不是活动状态时返回值为 100。

<0：执行失败。

#### 58.dwmon\_open\_database

**函数原型：**

```
int

dwmon_open_database(

    String group_name,

    String db_name

);
```

**功能说明：**

在系统中存在其他故障实例时，守护进程无法自动 Open 主库，或者系统中没有活动主库时，守护进程无法自动 Open 备库，这种情况下，可以调用此接口强制 Open 指定的数据库。

执行此操作需要先登录监视器。

**参数说明：**

group\_name: 输入参数，指定要强制 Open 库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要强制 Open 的数据库名称，此参数必须指定。

**返回值：**

\>=0：执行成功，执行前库已经处于 Open 状态时返回值为 100。

<0：执行失败。

#### 59.dwmon\_get\_switchover\_standby

**函数原型：**

```
DwMonDatabaseNameArray

dwmon_get_switchover_standby(

    String group_name

);
```

**功能说明：**

获取可以切换为主库的备库信息，这里的切换是指主备库都正常，且处于 Open 状态时，交换主备库模式，将备库切换为新的主库，主库切换为备库的操作。

**参数说明：**

group\_name: 输入参数，指定要获取切换信息的组名，只有一组时可以不指定。

**返回值：**

返回 DwMonDatabaseNameArray 对象，该对象结构如下：

```
DwMonDatabaseNameArray：
Integer returnCode : 执行结果
Integer dbNum:实际获取的可以执行切换的备库个数
String[] nameArray:可以执行切换的备库名称
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonDatabaseNameArray 的其他对象成员获取备库实例信息。

<0：执行失败。

#### 60.dwmon\_switchover

**函数原型：**

```
int

dwmon_switchover(

    String group_name,

    String db_name

);
```

**功能说明：**

使用指定的备库和当前的主库执行切换操作，这里的切换是指主备库都正常，且处于 Open 状态时，交换主备库模式，将备库切换为新的主库，主库切换为备库的操作。

此接口只有在指定的备库满足切换条件时才能够执行成功，可以先调用 dwmon\_get\_switchover\_standby 获取到满足条件的备库列表。

执行此操作需要先登录监视器。

**参数说明：**

group\_name: 输入参数，指定要执行切换的备库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要执行切换的备库名称，只有一个备库时可以不指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 61.dwmon\_get\_takeover\_standby

**函数原型：**

```
DwMonDatabaseNameArray

dwmon_get_takeover_standby(

    String group_name,

    boolean force_flag

);
```

**功能说明：**

获取可以接管为主库的备库信息，在主库发生故障时，可以通过调用此接口查找可以接管为新的主库的备库实例，其中包括正常接管和强制接管，通过输入参数 force\_flag 可以指定接管方式。

**参数说明：**

group\_name: 输入参数，指定要获取接管信息的组名，只有一组时可以不指定。

force\_flag: 输入参数，指定接管方式，true: 强制接管，false: 正常接管。

**返回值：**

返回 DwMonDatabaseNameArray 对象，该对象结构如下：

```
DwMonDatabaseNameArray：
Integer returnCode : 执行结果
Integer dbNum:实际获取可以执行接管操作的备库个数
String[] nameArray:可以执行接管的备库名称
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonDatabaseNameArray 的其他对象成员获取备库实例信息。

100：有活动 PRIMARY 实例，不再查找可接管实例列表。

<0：执行失败。

#### 62.dwmon\_takeover

**函数原型：**

```
int

dwmon_takeover(

    String group_name,

    String db_name

);
```

**功能说明：**

主库故障后，可以通过调用此接口执行正常的接管操作，注意，此接口只有在指定备库满足正常接管条件时才能够执行成功，可以先调用 dwmon\_get\_takeover\_standby 获取到符合正常接管条件的备库实例，force\_flag 指定为 false。

执行此操作需要先登录监视器。

**参数说明：**

group\_name: 输入参数，指定要执行接管的备库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要执行接管的备库名称，只有一个备库时可以不指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 63.dwmon\_takeover\_force

**函数原型：**

```
int 
dwmon_takeover_force(
    String             group_name, 
    String             db_name
);
```

**功能说明：**

主库故障后，可以通过调用此接口执行强制接管操作。此接口只有在指定备库满足强制接管条件时才能够执行成功，可以先调用 dwmon\_get\_takeover\_standby 获取到符合强制接管条件的备库实例，force\_flag 指定为 TRUE。

执行此操作需要先登录监视器。

**参数说明：**

group\_name: 输入参数，指定要执行强制接管的备库所在的组名，只有一组时可以不指定。

db\_name: 输入参数，指定要执行强制接管的备库名称，只有一个备库时可以不指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 64.dwmon\_check\_mppctl

**函数原型：**

```
int

dwmon_check_mppctl();
```

**功能说明：**

配置为 mpp 主备环境时，可通过调用此接口检查当前各个活动节点的 dmmpp.ctl 是否处于一致状态，注意只有 MPP 主备环境下允许调用此接口。

**参数说明：**

无

**返回值：**

0：处于一致状态。

<0：检查失败，或者控制文件不一致(返回值为-12)。

#### 65.dwmon\_recover\_mppctl

**函数原型：**

```
int

dwmon_recover_mppctl();
```

**功能说明：**

配置为 mpp 主备环境下时，如果某个活动节点的 dmmpp.ctl 不一致，可通过调用此接口恢复到一致状态。

只有 MPP 主备环境下允许调用此接口，并且需要先登录监视器。

**参数说明：**

无

**返回值：**

0：执行成功。

<0：执行失败。

#### 66.dwmon\_get\_mpp\_site\_info

**函数原型：**

```
DwMonMpp

dwmon_get_mpp_site_info();
```

**功能说明：**

配置为 mpp 主备环境时，可通过调用此接口获取 mpp 节点信息，注意只有 MPP 主备环境下允许调用此接口。

**参数说明：**

无

**返回值：**

返回 DwMonMpp 对象，该对象结构如下：

```
DwMonMpp：
Integer returnCode : 执行结果
Integer siteNum:实际获取的MPP节点数
Integer[] epSeqno:MPP节点号
String[] dbName:MPP节点实例名
String[] dbIp:MPP节点IP地址
Integer[] dbPort:MPP节点端口号
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonMpp 其他对象成员获取 MPP 节点信息。

<0：执行失败。

#### 67.dwmon\_tip

**函数原型：**

```
int

dwmon_tip();
```

**功能说明：**

可调用此接口查看系统当前运行状态，输出的系统状态信息可通过消息相关接口获取到。

**参数说明：**

无

**返回值：**

0：系统运行正常，所有实例和守护进程都处于 OPEN 状态。

\-25：所有组中都有正常的主库实例（实例和守护进程都是 OPEN 状态），不影响系统使用，但是存在有其他异常实例，具体描述信息可通过消息相关接口获取。

\-26：系统运行异常，不是所有组都有正常的主库实例，守护进程正在自动处理，请稍后再次调用接口判断，具体描述信息可通过消息相关接口获取。

\-27：系统运行异常，不是所有组都有正常的主库实例，需要用户根据描述信息确认是否进行人工干预，具体描述信息可通过消息相关接口获取。

其他<0 的值：表示接口执行失败。

#### 68.dwmon\_set\_group\_arch\_invalid

**函数原型：**

```
int

dwmon_set_group_arch_invalid(

    String group_name

);
```

**功能说明：**

修改指定组中所有备库的归档为无效状态，如果未指定组名，则通知所有组执行。

注意：执行此操作需要先登录监视器。

**参数说明：**

group\_name: 输入参数，守护组名，不指定则对所有组执行。

**返回值：**

0：执行成功。

<0：执行失败。

#### 69.dwmon\_set\_group\_recover\_time

**函数原型：**

```
int

dwmon_set_group_recover_time(

    String group_name,

    int recover_time

);
```

**功能说明：**

修改指定组中所有备库的恢复间隔(3~86400s)，只修改组中主库对应守护进程的内存值，如果未指定组名，则通知所有组执行。

注意：执行此操作需要先登录监视器。

**参数说明：**

group\_name: 输入参数，守护组名，不指定则对所有组执行。

recover\_time:输入参数，指定恢复间隔(3~86400s)，只修改组中主库守护进程的内存值。

**返回值：**

0：执行成功。

<0：执行失败。

#### 70.dwmon\_set\_group\_para\_value

**函数原型：**

```
int

dwmon_set_group_para_value(

    String group_name,

    String para_name,

    String para_value

);
```

**功能说明：**

修改指定组的所有守护进程的指定配置参数，同时修改 dmwatcher.ini 配置文件和内存值，如果未指定组名，则通知所有组执行。

目前可修改的参数包括：DW\_ERROR\_TIME、INST\_RECOVER\_TIME、INST\_ERROR\_TIME、INST\_AUTO\_RESTART、INST\_SERVICE\_IP\_CHECK、RLOG\_SEND\_THRESHOLD、RLOG\_APPLY\_THRESHOLD。

如果组中某个守护进程故障，则跳过不修改，如果要重启故障的守护进程，需要在重启前修改守护进程 dmwatcher.ini 中的 DW\_ERROR\_TIME 和远程一致，否则 dmmonitor 执行命令时会报错处理。

注意：执行此操作需要先登录监视器。

**参数说明：**

group\_name: 输入参数，守护组名，不指定则对所有组执行。

para\_name: 输入参数，指定要修改的参数名称，目前只允许是 DW\_ERROR\_TIME、INST\_RECOVER\_TIME、INST\_ERROR\_TIME、INST\_AUTO\_RESTART、INST\_SERVICE\_IP\_CHECK、RLOG\_SEND\_THRESHOLD、RLOG\_APPLY\_THRESHOLD 中的一种。

para\_value: 输入参数，指定要修改的参数值，和 para\_name 对应。

**返回值：**

0：执行成功。

<0：执行失败。

#### 71.dwmon\_set\_group\_auto\_restart\_on

**函数原型：**

```
int

dwmon_set_group_auto_restart_on(

    String group_name

);
```

**功能说明：**

打开指定组内所有单节点或 DMDSC 集群节点实例的自动拉起标记。

对单节点，直接修改 dmwatcher 自动拉起标记的内存值。

对 DMDSC 集群，自动拉起是靠 dmcss 执行的，dmcss 只负责拉起和自己的 dcr\_seqno 相同的 db 节点。如果 dmcss 未配置自动拉起参数（DMDCR\_DB\_RESTART\_INTERVAL/ DMDCR\_DB\_STARTUP\_CMD），此命令会执行失败。

此接口只修改 dmwatcher 或 dmcss 内存中的自动拉起标记值，不会修改 dmwathcer.ini 或 dmdcr.ini 中的配置值，如果重启，此修改会丢失。

此接口执行时，有可能所有节点实例都还未启动，无法校验登录口令，因此不要求先登录监视器。

**参数说明：**

group\_name: 输入参数，指定要执行操作的组名，只有一组时可以不指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 72.dwmon\_set\_group\_auto\_restart\_off

**函数原型：**

```
int

dwmon_set_group_auto_restart_off(

    String group_name

);
```

**功能说明：**

关闭指定组内所有单节点或 DMDSC 集群节点实例的自动拉起标记。

对单节点，直接修改 dmwatcher 自动拉起标记的内存值。对 DMDSC 集群，和 dwmon\_set\_group\_auto\_restart\_on 接口相对应，可以一次性关闭守护系统内所有 DMDSC 集群上 dmcss 的自动拉起标记。

此命令只修改 dmwatcher 或 dmcss 内存中的自动拉起标记值，如果重启，此修改会丢失。

执行此操作需要先登录监视器。

**参数说明：**

group\_name: 输入参数，指定要执行操作的组名，只有一组时可以不指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 73.dwmon\_detach\_database

**函数原型：**

```
int

dwmon_detach_database(

    String group_name,

    String db_name

);
```

**功能说明：**

此接口允许将指定的备库分离出守护进程组，执行此接口需要先登录监视器。

对于全局守护类型的备库，使用此命令不会触发主库的 Failover 故障处理流程。该接口不会修改相关的配置信息，只是为了需要主动维护备库时使用。

接口会依次执行下列操作：

1. 设置指定备库的恢复间隔为 86400(s)
2. 修改主库到指定备库的归档状态无效

本接口不会主动退出备库实例，如果需要执行退出操作，可再通过调用 dwmon\_stop\_database 接口完成。

在备库维护结束后，如果备库是退出状态，可先调用 dwmon\_startup\_database 接口将备库启动，然后再调用 dwmon\_attach\_database 接口将备库重加入守护进程组。

**参数说明：**

group\_name: 输入参数，指定要执行操作的守护进程组名，只有一组时可以不指定。

db\_name: 输入参数，指定要正常分离出的备库名称，此参数必须指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 74.dwmon\_attach\_database

**函数原型：**

```
int

dwmon_attach_database(

    String group_name,

    String db_name

);
```

**功能说明：**

在使用 dwmon\_detach\_database 接口分离出去的备库维护完成后，可通过调用此接口将备库重加入守护进程组，执行此接口需要先登录监视器。

此接口执行时，会通知主库将指定备库的恢复间隔调整为 3s，3s 后主库守护进程会发起 Recovery 流程，将备库重加入守护系统。

注意，此接口不会将备库拉起，如果备库处于退出状态，需要先调用 dwmon\_startup\_database 接口将备库启动。

**参数说明：**

goup\_name: 输入参数，指定要执行操作的守护进程组名，只有一组时可以不指定。

db\_name: 输入参数，指定要重加入的备库名称，此参数必须指定。

**返回值：**

0：执行成功。

<0：执行失败。

#### 75.dwmon\_get\_source\_database\_name

**函数原型：**

```
DwMonData

dwmon_get_source_database_name(

    String group_name,

    String db_name

);
```

**功能说明：**

获取指定库的源库名称，指定库为备库时才有意义，可以是异步备库。

**参数说明：**

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：0
String stringValue : 指定库的源库名称
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过对象成员 stringValue 获取源库名称。

<0：执行失败。

#### 76.dwmon\_get\_ep\_arch\_send\_info

**函数原型：**

```
ArchSendInfo

dwmon_get_ep_arch_send_info(

    String group_name,

    String source_name,

    String db_name

);
```

**功能说明：**

获取指定的源实例到指定备库的归档发送信息。

源库如果是 DMDSC 集群，则需要依次取出集群内每个源实例到指定备库的归档发送信息，这个需要结合 dwmon\_get\_source\_database\_name 和 dwmon\_get\_database\_info 这两个接口来完成。

首先用 dwmon\_get\_source\_database\_name 获取到源库名称，再通过 dwmon\_get\_database\_info 获取到源库的所有实例名，再通过本接口依次取出源库每个实例到指定备库的归档发送信息，接口中的 source\_name 字段就是指源库中的某个实例名。

**参数说明：**

group\_name: 输入参数，输入指定备库所在的守护进程组名，如果只有一组可以不指定。

source\_name：输入参数，输入要获取归档发送信息的源库实例名。

db\_name: 输入参数，输入要获取归档发送信息的备库名称。

**返回值：**

返回 ArchSendInfo 对象，该对象结构如下：

```
ArchSendInfo：
Integer returnCode : 执行结果
String dbName:要获取归档发送信息的备库名称
String sourceName:要获取归档发送信息的源库实例名
Integer recovTimeInIni:源库守护进程dmwatcher.ini中配置INST_RECOVER_TIME值
Integer recovTimeInMem:源库守护进程内存中的INST_RECOVER_TIME值
String lastRecoverTime:源实例上次对指定备库执行恢复操作的执行结果code，对local守护类型无效，0表示执行成功，100表示实际未执行，小于0表示执行失败
String archType:源实例source_name到备库的归档类型，包括REALTIME/TIMELY/ASYNC这三种类型
String malSta:源实例source_name到备库的mal链路状态
String archSta:源实例source_name到备库的归档状态
String sendType:源实例source_name到备库的归档发送类型，FOR REALTIME SEND和FOR TIMELY SEND表示正常的归档发送，FOR RECOVER SEND表示守护进程发起的归档发送，FOR ASYNC SEND表示定时器触发的异步归档发送
String lastStartTime:源实例source_name到备库的最近一次归档发送起始时间，NONE表示未执行过发送操作
String lastEndTime:源实例source_name到备库的最近一次归档发送结束时间
Long lastSendTime:源实例source_name到备库的最近一次归档发送耗时（微秒）
Long lastStartLsn:源实例source_name到备库的最近一次归档发送起始lsn
Long lastEndLsn:源实例source_name到备库的最近一次归档发送结束lsn
Integer lastSendLen:实例source_name到备库的最近一次归档发送长度（字节）
Integer lastSendPtx:源实例source_name到备库的最近一次发送的PTX个数
Integer code:源实例source_name到备库的最近一次归档发送code，0表示执行成功，100表示实际未执行，小于0表示执行失败
String descInfo:源实例source_name到备库的最近一次归档发送描述信息
Integer recntCnt:源实例source_name到备库的最近日志发送次数N
Long recntSendLen:源实例source_name到备库的最近N次累计日志发送长度（字节），N值取recnt_cnt值，下同
Long recntPtxCnt:源实例source_name到备库的最近N次累计发送的PTX个数
Long recntSendTime:源实例source_name到备库的最近N次累计日志发送耗时（微秒）
Long maxSendTime:源实例source_name到备库的最大发送耗时（微秒）
String maxEndTime:源实例source_name到备库最大发送耗时的结束时间
Integer maxPtxCnt:源实例source_name到备库发送的最大PTX个数
Integer maxSendLen:源实例source_name到备库发送的最大日志长度（字节）
Long maxSendLsn:源实例source_name到备库发送的最大日志LSN
Long totalSendCnt:源实例source_name到备库总的归档发送次数
Long totalSendLen:源实例source_name到备库总的归档发送长度（字节）
Long totalPtxCnt:源实例source_name到备库总的PTX发送个数
Long totalSendTime:源实例source_name到备库总的归档发送耗时（微秒）
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 ArchSendInfo 的其他对象成员获取归档发送信息。

<0：执行失败。

#### 77.dwmon\_get\_n\_apply

**函数原型：**

```
ApplyNumInfo

dwmon_get_n_apply(

    String group_name,

    String db_name

);
```

**功能说明：**

获取指定备库上的重演节点个数信息，也就是源库的节点个数。

**参数说明：**

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

**返回值：**

返回 ApplyNumInfo 对象，该对象结构如下：

```
ApplyNumInfo：
Integer returnCode : 执行结果
Integer applyNum:备库控制节点上记录的重演节点个数
String epName:备库主ep名称
String primName:备库当前对应的主库实例名
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 ApplyNumInfo 的其他对象成员获取详细信息。

<0：执行失败。

#### 78.dwmon\_get\_ep\_nth\_apply\_info

**函数原型：**

```
ApplyInfo

dwmon_get_ep_nth_apply_info(

    String group_name,

    String db_name,

    int nth

);
```

**功能说明：**

获取指定备库上第 nth 组重演信息上记录的 lsn 等信息。

当备库对应的源库是 DMDSC 集群时，假如 DMDSC 集群有 N 个节点，那么备库控制节点上就会有 N 组重演信息依次和源库的每个节点相对应，N 值可以通过 dwmon\_get\_n\_apply 接口中的 applyNum 字段值获取，本接口的输入参数 nth 的取值范围为\[0,applyNum-1\]。

此接口只输出简略的 lsn 重演信息，如果还需要获取详细的重演统计信息，请参考 dwmon\_get\_ep\_nth\_apply\_info 接口说明。

**参数说明：**

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

nth: 输入参数，指定要获取备库上第 nth 组重演信息。

**返回值：**

返回 ApplyInfo 对象，该对象结构如下：

```
ApplyInfo：
Integer returnCode : 执行结果
String primName:第nth个apply_info上记录的pname信息，可能为空
Integer dscSeqno:主库节点seqno
Long sseq:备库可重演到的最大日志包序号
Long slsn:备库可重演到的最大LSN，对应日志包序号为sseq（和dsc_seqno对应）
Long kseq:非自动切换模式下，备库保持不重演的日志包序号
Long klsn:非自动切换模式下，备库保持不重演的最大LSN，对应的日志包序号为kseq（和dsc_seqno对应）
Long aseq:备库已经重演到的日志包序号（和dsc_seqno对应）
Long alsn:备库已经重演到的lsn值，对应的日志包序号为aseq（和dsc_seqno对应）
Integer tskNum:当前还剩余的重演任务数，在watch/monitor中使用
Long tskMemUsed:当前任务队列占用的总内存大小（字节）
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 ApplyInfo 的其他对象成员获取重演 lsn 信息。

<0：执行失败。

#### 79.dwmon\_get\_ep\_nth\_apply\_stat

**函数原型：**

```
ArchApplyStat

dwmon_get_ep_nth_apply_stat(

    String group_name,

    String db_name,

    int nth

);
```

**功能说明：**

获取指定备库上第 nth 组重演信息，包含详细的重演统计信息。

当备库对应的源库是 DMDSC 集群时，假如 DMDSC 集群有 N 个节点，那么备库控制节点上就会有 N 组重演信息依次和源库的每个节点相对应，N 值可以通过 dwmon\_get\_n\_apply 接口中的 applyNum 字段值获取，本接口的输入参数 nth 的取值范围为\[0,applyNum -1\]。

**参数说明：**

group\_name: 输入参数，输入指定备库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取重演信息的备库名称。

nth: 输入参数，指定要获取备库上第 nth 组重演信息。

**返回值：**

返回 ArchApplyStat 对象，该对象结构如下：

```
ArchApplyStat：
Integer returnCode : 执行结果
String primName:第nth个apply_stat上记录的主库节点名称
Integer dscSeqno:主库节点seqno
Long sseq:备库可重演到的最大日志包序号
Long slsn:备库可重演到的最大LSN，对应的日志包序号为sseq（和dsc_seqno对应）
Long kseq:非自动切换模式下，备库保持不重演的日志包序号
Long klsn:非自动切换模式下，备库保持不重演的最大LSN，对应日志包序号为kseq（和dsc_seqno对应）
Long aseq:备库已经重演到的日志包序号
Long alsn:备库已经重演到的lsn值，对应日志包序号为aseq（和dsc_seqno对应）
Integer tskNum:当前还剩余的重演任务数，在watch/monitor中使用
Long tskMemUsed:当前任务队列占用的总内存大小（字节）
Integer recntApplyNum:最近累计重演的次数N
Integer lastRecvedLen:最近一次收到的日志长度（字节）
Long lastResTime:最近一次消息响应时间（微秒）
Long lastWaitTime:最近一次任务等待时间（微秒）
Integer lastApplyLen:最近一次重演的日志长度（字节）
Long lastApplyTime:最近一次重演耗时（微秒）
Long recntRecvedLen:最近N次累计接收长度（N值取自recnt_apply_num）
Long recntResTime:最近N次累计响应时间（微秒）
Long recntWaitTime:最近N次累计等待时间（微秒）
Long recntApplyLen:最近N次累计重演长度（字节）
Long recntApplyTime:最近N次累计重演时间（微秒）
Long maxResTime:最大消息响应时间（微秒）
Long maxWaitTime:最大任务等待时间（微秒）
Long maxApplyTime:最大任务重演时间（微秒）
Integer maxApplyLen:和max_apply_time对应的日志长度（字节）
Long totalRecvedNum:累计收到日志缓冲区个数
Long totalRecvedLen:累计收到日志量（字节）
Long totalApplyNum:累计重演日志个数
Long totalApplyLen:累计重演日志量（字节）
Long totalResTime:累计消息响应时间，收到消息到响应消息（微秒）
Long totalWaitTime:累计任务等待时间（微秒）
Long totalApplyTime:累计日志重演时间（微秒）
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 ArchApplyStat 的其他对象成员获取详细的重演信息。

<0：执行失败。

#### 80.dwmon\_clear\_database\_arch\_send\_info

**函数原型：**

```
int

dwmon_clear_database_arch_send_info(

    String group_name,

    String db_name

);
```

**功能说明：**

清理指定组中主库到指定备库实例的最近 N 次归档发送信息（通知主库执行）。函数在使用前，需要先登录监视器。

N 值取主库 dm.ini 中配置的 RLOG\_SEND\_APPLY\_MON 值和实际归档发送次数中的较小值，实际归档发送次数可通过查询 V$ARCH\_SEND\_INFO 获取。

如果主库是 DMDSC 集群，则会通知集群内所有实例执行清理。

**参数说明：**

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

**返回值：**

0：执行成功。

<0：执行失败。

#### 81.dwmon\_clear\_group\_arch\_send\_info

**函数原型：**

```
int

dwmon_clear_group_arch_send_info (

    String group_name

);
```

**功能说明：**

清理指定组中主库到所有实时或即时备库实例的最近 N 次归档发送信息（通知主库执行）。函数在使用前，需要先登录监视器。

N 值取主库 dm.ini 中配置的 RLOG\_SEND\_APPLY\_MON 值和实际归档发送次数中的较小值，实际归档发送次数可通过查询 V$ARCH\_SEND\_INFO 获取。

**参数说明：**

group\_name：输入参数，指定守护进程组名，如果不指定则通知所有组执行。

**返回值：**

0：执行成功。

<0：执行失败。

#### 82.dwmon\_clear\_database\_rapply\_stat

**函数原型：**

```
int

dwmon_clear_database_rapply_stat(

    String group_name,

    String db_name

);
```

**功能说明：**

清理指定备库实例的最近 N 次日志重演信息（通知备库执行）。函数在使用前，需要先登录监视器。

N 值取备库 dm.ini 中配置的 RLOG\_SEND\_APPLY\_MON 值和实际重演次数中的较小值，实际重演次数可通过查询 V$RAPPLY\_STAT 获取。

**参数说明：**

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

**返回值：**

0：执行成功。

<0：执行失败。

#### 83.dwmon\_clear\_group\_rapply\_stat

**函数原型：**

```
int

dwmon_clear_group_rapply_stat(

    String group_name

);
```

**功能说明：**

清理指定组中所有备库实例的最近 N 次日志重演信息（通知所有备库执行）。函数在使用前，需要先登录监视器。

N 值取备库 dm.ini 中配置的 RLOG\_SEND\_APPLY\_MON 值和实际重演次数中的较小值，实际重演次数可通过查询 V$RAPPLY\_STAT 获取。

**参数说明：**

group\_name：输入参数，指定守护进程组名，如果不指定则通知所有组执行。

**返回值：**

0：执行成功。

<0：执行失败。

#### 84.dwmon\_check\_recover

**函数原型：**

```
int

dwmon_check_recover(

    String group_name,

    String db_name

);
```

**功能说明：**

检查指定组的指定备库是否满足自动 Recover 条件，如果不满足条件，主库的守护进程不会对指定备库发起自动 Recovery 流程。

**参数说明：**

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

inst\_name：输入参数，指定备库名称。

**返回值：**

0：符合自动 Recover 条件，备库已经在待恢复列表或者主库的守护进程即将发起对指定备库的 Recover 操作。

\-20：当前无法判断是否符合自动 Recover 条件，比如有监视器命令正在执行、指定备库还未达到恢复间隔或者指定备库上的 RLOG\_PKG 还未全部重演完成等情况，需要稍后再次调用接口判断，具体的描述信息可通过消息相关接口获取到。

\-21：表示备库不满足自动 Recover 条件，具体的描述信息可通过消息相关接口获取到。

其他<0 的值：表示接口执行失败。

#### 85.dwmon\_check\_open

**函数原型：**

```
int

dwmon_check_open(

    String group_name,

    String db_name

);
```

**功能说明：**

检查指定组的指定库是否满足自动 Open 条件，如果不满足条件，守护进程不会通知数据库实例执行 Open 操作。

**参数说明：**

group\_name：输入参数，指定库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定数据库名称。

**返回值：**

0：符合自动 Open 条件，库已经 Open 成功或者正在执行 Open，或者库的守护进程即将通知实例执行 Open 操作。

\-22：当前无法判断库是否满足自动 Open 条件，比如有监视器命令正在执行，或者数据库实例还未启动到 MOUNT 状态等情况，需要稍后再次调用接口判断，具体的描述信息可通过消息相关接口获取到。

\-23：表示库不满足自动 Open 条件，并且库自身不是 OPEN 状态，具体的描述信息可通过消息相关接口获取到。

\-24：表示库不满足自动 Open 条件，其中库实例已经是 OPEN 状态，但库的守护进程不是 OPEN 状态，具体的描述信息可通过消息相关接口获取到。

其他<0 的值：表示接口执行失败。

#### 86.dwmon\_deinit\_env

**函数原型：**

```
int

dwmon_deinit_env();
```

**功能说明：**

销毁监视器执行环境。

**参数说明：**

无

**返回值：**

0：执行成功。

<0：执行失败。

#### 87.dwmon\_free\_handle

**函数原型：**

```
int

dwmon_free_handle();
```

**功能说明：**

释放分配到的监视器句柄。

**参数说明：**

无

**返回值：**

0：执行成功。

<0：执行失败。

#### 88.dwmon\_get\_monitor\_state

**函数原型：**

```
DWMonState

dwmon_get_monitor_state();
```

**功能说明：**

配置为主备多实例监视器环境时，可通过调用此接口获取监视器信息。本函数只在确认监视器上执行有效。若在确认监视器非 leader 上执行，获取的监视器状态数组 monStateArray 不准确。此接口功能已被 dwmon\_get\_monitor\_state\_from\_watcher 替代，出于兼容考虑仍保留原接口。建议使用函数 dwmon\_get\_monitor\_state\_from\_watcher 代替该函数，dwmon\_get\_monitor\_state\_from\_watcher 在确认监视器和非确认监视器上都可执行，且可获取多实例监视器的堆积标志。

**参数说明：**

无

**返回值：**

返回 DwMonState 对象，该对象结构如下：

```
DwMonState：
Integer returnCode : 执行结果
Integer monNum:监视器个数
String[] monNameArray:monitor名字数组
Integer[] monStateArray:monitor的监视器状态数组
Integer[] monIDArray:monitorID数组
Integer[] monRoleArray:monitor角色数组
String[] monIpArray:monitor的IP地址数组
Integer[] monPortArray:monitor的端口号信息
Integer broTimeout:monitor的广播延时
Integer voteTimeout:monitor的投票延时
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonState 的其他对象成员获取监视器信息。其中 monStateArray 和 monRoleArray 数组元素值含义见 10.2.4 C 接口说明 中关于 dwmon\_get\_monitor\_state 接口 mon\_state\_arr 和 mon\_role\_arr 参数的描述。

<0：执行失败。

#### 89.dwmon\_get\_ep\_nth\_apply\_with\_parallel\_info

**函数原型：**

```
ApplyParallelInfo

dwmon_get_ep_nth_apply_with_parallel_info(

    String group_name,

    String db_name,

    int nth

);
```

**功能说明：**

获取指定备库上第 nth 组重演信息上记录的 lsn 值、包序号、并行度以及各路并行 lsn 信息。

当备库对应的源库是 DMDSC 集群时，假如 DMDSC 集群有 N 个节点，则备库控制节点上就会有 N 组重演信息依次和源库的每个节点相对应，N 值可以通过 dwmon\_get\_n\_apply 接口中的 applyNum 字段获取，本接口的输入参数 nth 的取值范围为\[0, applyNum-1\]。

**参数说明：**

group\_name：输入参数，指定备库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定备库名称。

nth：输入参数，指定要获取备库上第 nth 组重演信息。

**返回值：**

返回 ApplyParallelInfo 对象，该对象结构如下：

```
ApplyParallelInfo：
Integer returnCode : 执行结果
String primName:第nth个apply_stat上记录的主库节点名称
Integer dscSeqno:主库节点seqno
Long sseq:备库可重演到的最大日志包序号
Long slsn:备库可重演到的最大LSN，对应的日志包序号为sseq（和dsc_seqno对应）
Long kseq:非自动切换模式下，备库保持不重演的日志包序号
Long klsn:非自动切换模式下，备库保持不重演的最大LSN，对应日志包序号为kseq（和dsc_seqno对应）
Long rseq:备库已经重演到的日志包序号
Long rlsn:备库已经重演到的lsn值，对应日志包序号为aseq（和dsc_seqno对应）
Integer tskNum:当前还剩余的重演任务数，在watch/monitor中使用
Long tskMemUsed:当前任务队列占用的总内存大小（字节）
Integer n_pll:备库并行重演线程数
String[] redoLsnArr:备库各路并行重演线程已重演到的LSN值
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 ApplyParallelInfo 的其他对象成员获取监视器信息。

<0：执行失败。

#### 90.dwmon\_set\_database\_until\_time

**函数原型：**

```
Int
dwmon_set_database_until_time (
    String    group_name,
    String    db_name,
    String    until_time
);
```

**功能说明：**

设置指定组的指定异步备库重演到的时间点。

**参数说明：**

group\_name：输入参数，指定库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定异步备库名称。

until\_time：输入参数，指定异步备库重演到的时间点，可精确到微秒。

**返回值：**

0：执行成功。

<0：执行失败。

#### 91.dwmon\_get\_database\_until\_time

**函数原型：**

```
DwMonData
dwmon_get_database_until_time (
    String group_name,
    String db_name
);
```

**功能说明：**

获取指定组的指定异步备库设置的重演到的时间点。

**参数说明：**

group\_name：输入参数，指定库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，指定异步备库名称。

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：1(TRUE)/0(FALSE)，备库是否已重演到指定的时间点
String stringValue : 异步备库设置的重演到的时间点
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过对象成员 stringValue 获取异步备库设置的重演到的时间点。

<0：执行失败。

#### 92\. dwmon\_get\_group\_takeover\_time

**函数原型：**

```
DwMonTkovtime
dwmon_get_group_takeover_time(
   String group_name
);
```

**功能说明：**

获取指定组的自动接管时间。

**参数说明：**

group\_name：输入参数，指定库所属的守护进程组名，只有一组时可以不指定。

**返回值：**

返回 DwMonTkovtime 对象，该对象结构如下：

```
DwMonTkovtime：
Integer remainTime：自动接管时间
String instName : 接管实例名
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功。

<0：执行失败。

#### 93\. dwmon\_get\_database\_apply\_wait

**函数原型：**

```
DwMonData
dwmon_get_database_apply_wait(
   String group_name,
   String db_name
);
```

**功能说明：**

获取指定备库用于表示备库是否是事务一致的标记。

**参数说明：**

group\_name：输入参数，指定库所属的守护进程组名，只有一组时可以不指定。

db\_name：输入参数，备库名。

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：1(TRUE)/0(FALSE)，事务一致标志
String stringValue : ""
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功。

<0：执行失败。

#### 94\. dwmon\_login\_wallet

**函数原型：**

```
int 
dwmon_login_wallet(
    String      service_name
);
```

**功能说明：**

使用 wallet 方式登录监视器。使用此接口前需要用户先使用 dmmkstore 工具创建好 wallet 文件，配置服务名及对应的用户名和口令，将该文件拷贝到监视器所在的机器上，然后将 MON\_WALLET\_LOCATION 参数指定为 wallet 文件所在路径。这里的用户名及口令和服务器的登录口令是一致的，且必须有 DBA 权限。

校验登录信息时由守护进程转发给服务器校验，并返回校验结果给监视器，因此需要保证系统中至少有一个活动库，否则无法校验成功。

**参数说明：**

service\_name: 输入参数，服务名，最长可为 128 字节，超长则接口执行失败。

**返回值：**

0：执行成功。

<0：执行失败。

#### 95\. dwmon\_get\_database\_sync\_arch\_info

**函数原型：**

```
DwMonSyncInfo 
dwmon_get_database_sync_arch_info(
    String             group_name, 
    String             db_name
);
```

**功能说明：**

获取指定库配置的同步归档信息的 JNI 接口，包括归档目标实例名，到归档目标的 mal 链路状态和归档状态。

**参数说明：**

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要获取同步归档信息的数据库名称。

**返回值：**

返回 DwMonSyncInfo 对象，该对象结构如下：

```
DwMonSyncInfo：
Integer nSync：实际填充的sync归档数
String[] syncDest:同步归档目标实例名数组
String[] syncMalSta:到同步备库的mal链路状态数组
String[] syncArchSta:到同步备库的归档状态数组
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonSyncInfo 的其他对象成员获取相关归档信息。

<0：执行失败。

#### 96\. dwmon\_get\_ep\_host

**函数原型：**

```
DwMonData
dwmon_get_ep_host(
    String          group_name,
    String          ep_name
);
```

**功能说明：**

获取指定组中指定实例的 IP 地址。

**参数说明：**

group\_name: 输入参数，输入指定实例所在的守护进程组名，如果只有一组可以不指定。

ep\_name: 输入参数，输入要获取 IP 地址的实例名。

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：0
String stringValue : ep的IP地址，如果配置有外网IP，则输出外网IP，否则输出内网IP
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过对象成员 stringValue 获取该实例的 IP 地址。如果配置有外网 IP，则返回外网 IP；否则返回内网 IP。

<0：执行失败。

#### 97\. dwmon\_get\_hp\_flag

**函数原型：**

```
DwMonData
dwmon_get_hp_flag();
```

**功能说明：**

获取当前监视器日志堆积标记。

**参数说明：**

无

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：监视器日志堆积标记
String stringValue : ""
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功。

<0：执行失败。

#### 98\. dwmon\_get\_real\_group\_db\_name

**函数原型：**

```
DwMonRealName
dwmon_get_real_group_db_name(
  String      group_name,
  String      db_name
);
```

**功能说明：**

根据输入的库名及其所在的组名，查找是否存在对应的库。

**参数说明：**

group\_name: 输入参数，指定库所在的守护进程组名。如果只有一组可以不指定。

db\_name: 输入参数，将要查找的数据库名。若只需要查找备库，且指定组内只有一个备库时，可以不指定。

**返回值：**

返回 DwMonRealName 对象，该对象结构如下：

```
DwMonRealName：
String realGname：真实组名
String realDname：真实库名
Integer returnCode：执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonRealName 的其它成员获取真实的组名和库名。

<0：执行失败。

#### 99\. dwmon\_create\_mlog

**函数原型：**

```
int
dwmon_create_mlog(
    String         file_path,
    int            file_size,
    String         mon_name,
    int            mon_magic,
    int           overwrite
);
```

**功能说明：**

创建多实例监视器的联机日志文件。

**参数说明：**

file\_path：输入参数，指定的监视器联机日志文件路径，需要与 dmmonitor.ini 中 MON\_LOG\_PATH 保持一致。

file\_size：输入参数，监视器联机日志文件大小，单位 MB，取值范围 512~10240。

mon\_name：输入参数，监视器实例名，需要与 dmmonitor.ini 中 MON\_NAME 保持一致。

mon\_magic：输入参数，监视器联机日志文件魔数，取值范围 0~4294967294；对于同一个多实例监视器组的监视器，需要相同。

overwrite：输入参数，在 file\_path 指定路径下已经有同名的联机日志文件的情况下，是否覆盖原有文件。0：否；1：是。

**返回值：**

0：执行成功。

<0：执行失败。

#### 100\. dwmon\_get\_exit\_all

**函数原型：**

```
DwExitAll
dwmon_get_exit_all();
```

**功能说明：**

获取监视器协同退出标记。

**返回值：**

返回 DwExitAll 对象，该对象结构如下：

```
DwExitAll：
Integer dataValue：协同退出标记
String stringValue : ""
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果

0：执行成功。可通过 DwExitAll 的成员 dataValue 获取协同退出标记。

<0：执行失败。

#### 101\. dwmon\_set\_exit\_all

**函数原型：**

```
int
dwmon_set_exit_all();
```

**功能说明：**

设置监视器协同退出标记，仅多实例监视器有效。

**返回值：**

0：执行成功。

<0：执行失败。

#### 102\. dwmon\_get\_mraft\_info

**函数原型：**

```
DwmonMraftInfo
dwmon_get_mraft_info();
```

**功能说明：**

获取多实例监视器多副本信息。

**返回值：**

返回 DwmonMraftInfo 对象，该对象结构如下：

```
DwmonMraftInfo：
Integer returnCode : 执行结果
Integer destNum:多实例监视器组中监视器数目
Integer voteStat:监视器选举角色
Integer leaderId:监视器leader序号
Integer hpFlag:监视器日志堆积标记
Integer ltermID:监视器本地任期号
Long cSeqno:监视器已提交日志包序号
Long[] fseqArr:监视器已刷盘序号数组，仅leader查询有效
Integer[] termArr:监视器已刷盘日志包任期号数组，仅leader查询有效
```

可通过对象成员 returnCode 获取执行结果。returnCode 为 0 表示执行成功。可通过 DwmonMraftInfo 的其他对象成员获取相关归档信息。

#### 103\. dwmon\_check\_db\_detached

**函数原型：**

```
DwMonData 
dwmon_check_db_detached(
string             group_name, 
string             db_name
);
```

**功能说明：**

检查指定库是否已经被分离出集群。

**参数说明：**

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要检查的数据库名称。

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：指定库是否已经被分离出集群。
String stringValue : ""
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过对象成员 dataValue 获取检查结果标记，1：指定库已经被分离出集群，0：指定库没有被分离出集群。检查结果只对 REALTIME/TIMELY 备库有效，对于主库或者守护进程配置为 LOCAL 的备库，检查结果一定为 0。

<0：执行失败。

#### 104\. dwmon\_get\_monitor\_state\_from\_watcher

**函数原型：**

```
DwMonState
dwmon_get_monitor_state_from_watcher();
```

**功能说明**

获取集群中多实例确认监视器信息。在非确认监视器上执行时，集群中需要有存活的守护进程；在确认监视器上执行无需守护进程。若在确认监视器非 leader 上执行，获取的监视器状态数组 monStateArray 不准确。

**参数说明**

无

**返回值：**

返回 DwMonState 对象，该对象结构如下：

```
DwMonState：
Integer returnCode : 执行结果
Integer monNum:监视器个数
String[] monNameArray:monitor名字数组
Integer[] monStateArray:monitor的监视器状态数组
Integer[] monIDArray:monitorID数组
Integer[] monRoleArray:monitor角色数组
String[] monIpArray:monitor的IP地址数组
Integer[] monPortArray:monitor的端口号信息
Integer broTimeout:monitor的广播延时
Integer voteTimeout:monitor的投票延时
Integer hpFlag:monitor的堆积标志，1：堆积；0：没有堆积
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过 DwMonState 的其他对象成员获取监视器信息。其中 monStateArray 和 monRoleArray 数组元素值含义见\[10.2.4 C 接口说明\](#10.2.4 C 接口说明) 中关于 dwmon\_get\_monitor\_state\_from\_watcher 接口 mon\_state\_arr 和 mon\_role\_arr 参数的描述。

<0：执行失败。

#### 105\. dwmon\_get\_db\_mode\_change\_stat

**函数原型：**

```
DwMonData
dwmon_get_db_mode_change_stat(
    string          group_name, 
    string          db_name
);
```

**功能说明：**

获取指定库的 AUTO\_MODE\_CHANGE 状态。检查结果只对 global 库有效. 对于 local 库此接口返回的 stringValue 为”OFF”。

**参数说明：**

group\_name: 输入参数，输入指定库所在的守护进程组名，如果只有一组可以不指定。

db\_name: 输入参数，指定要检查的数据库名称。

**返回值：**

返回 DwMonData 对象，该对象结构如下：

```
DwMonData：
Integer dataValue：0
String stringValue : 库的AUTO_MODE_CHANGE值
Integer returnCode : 执行结果
```

可通过对象成员 returnCode 获取执行结果。

0：执行成功，可通过对象成员 dataValue 获取结果。

<0：执行失败。

### 10.2.6 C 编程示例

#### 10.2.6.1 Windows 编程示例

这里给出 C 程序的编程示例，Windows 操作系统，使用 VS2010，通过配置项目属性，使用 dwmon.lib 隐式加载 dll 的方式，注意此处仅为使用示例，实际使用时可以根据自己的需求再做调整。本例中达梦安装路径为“D:\\dmdbms”，头文件 dwmon\_dll.h 和 lib 文件 dwmon.lib 位于“D:\\dmdbms\\include”目录下，动态链接库 dwmon.dll 位于“D:\\dmdbms\\bin”目录下。

本例中 VS2010 配置步骤如下：

1. 选择“文件”->“新建”->“项目”
2. 新建“Win32 控制台应用程序”，项目名称为“test\_dwmon”，位置为“E:\\test”，点击“确定”->“下一步”，进入配置向导，应用程序类型选择“控制台应用程序”，附加选项“空项目”，点击“完成”。
3. 在“头文件”目录上右键“添加”->“现有项”，选择“D:\\dmdbms\\include”目录下的 dwmon\_dll.h 添加。
4. 在“源文件”目录上右键“添加”->“新建项”，选择“C++ 文件(.cpp)”类型，名称为“test\_dwmon.c”，点击“添加”，文件创建完成，文件内容可参考下面的源码。
5. 配置项目属性，点击项目名称右键选择“属性”->“配置属性”->“调试”，“工作目录”中选择目录“D:\\dmdbms\\bin”。
6. 配置项目属性，点击项目名称右键选择“属性”-> “配置属性”-> “C/C++”->“常规”，“附加包含目录”中选择目录“D:\\dmdbms\\include”。
7. 配置项目属性，点击项目名称右键选择“属性”-> “配置属性”-> “C/C++”->“预处理器”，“预处理器定义”中增加“DM64;\_CRT\_SECURE\_NO\_WARNINGS;”，本例中使用 64 位平台，如果是 32 位平台，则不需要增加“DM64;”。
8. 配置项目属性，点击项目名称右键选择“属性”-> “配置属性”->“链接器”->“常规”， “附加库目录”中选择目录“D:\\dmdbms\\include”。
9. 配置项目属性，点击项目名称右键选择“属性”-> “配置属性”-> “链接器”->“输入”，“附加依赖项”中增加“dwmon.lib;”。

至此，VS2010 环境配置完成，注意 dll 和 lib 文件需要和项目平台保持一致，都是 32 位或者都是 64 位，否则会导致程序无法正常运行。

test\_dwmon.c 源码如下：

```
#include "dwmon_dll.h"
#include "stdio.h"
#include "stdlib.h"
#include "windows.h"
#include "process.h"

//消息线程 
DWORD
WINAPI
dwmon_get_msg_thread(
    mhandle     handle
)
{
    mschar          buf_msg[4097];
    muint4          msg_len_out;
    muint4          get_flag;
    DWMON_RETURN    code;
    while (TRUE)
    {
        //等待消息事件 
        dwmon_msg_event_wait(handle);
        //获取退出标记 
        if (dwmon_get_msg_exit_flag(handle) == TRUE)
        {
            break;
        }
        do 
        {
            //获取并打印消息
            code = dwmon_get_exec_msg(handle, buf_msg, 4097, &msg_len_out, &get_flag);
            if (code >=0 && msg_len_out > 0)
            {
                fprintf(stdout, "%s", buf_msg);
            }
        } while (get_flag); //判断是否还有未读消息 
    }
    //设置退出事件
    dwmon_set_msg_exit_event(handle);
    return 0;
}
//清理环境 
void
dwmon_clear_env(
    mhandle     handle
)
{
    //通知并等待dmmon_get_msg_thread消息线程退出
    dwmon_msg_event_deinit(handle);
    //销毁监视器环境
    dwmon_deinit(handle);
    //释放句柄
    dwmon_free_handle(handle);
}
int
main()
{
    DWMON_RETURN    ret;
    mhandle         handle;
HANDLE          thread_handle;
char             msg[4097];
int              msg_len;
    //分配操作句柄
    ret = dwmon_alloc_handle(&handle);
    if (ret < 0)
    {
        fprintf(stdout, "dwmon alloc handle failed!\n");
    //获取ret对应的错误描述信息
        dwmon_get_error_msg_by_code(handle, ret, msg, 4097, &msg_len);
        if (msg_len > 0)
        {
            fprintf(stdout, "code:%d, error msg:%s", ret, msg);
        }
        return ret;
    }
    //创建消息线程
    thread_handle = (HANDLE)_beginthreadex(NULL, 0, dwmon_get_msg_thread, handle, 0, NULL);
    if (thread_handle == NULL)
    {
        ret = GetLastError();
        fprintf(stderr, "_beginthreadex error! desc:%s, code:%d\n", strerror(ret), ret);
       dwmon_free_handle(handle);
        return ret;
    }
//初始化监视器环境，可以选择忽略-15错误（建立到所有守护进程连接失败，可能当前守护进程都还未启动）
    ret = dwmon_init(handle, "D:\\dwmon\\dmmonitor.ini", "D:\\dwmon\\log");
    if (ret < 0 && ret != -15)
{
    fprintf(stdout, "dwmon init failed!\n");
//获取ret对应的错误描述信息
        dwmon_get_error_msg_by_code(handle, ret, msg, 4097, &msg_len);
        if (msg_len > 0)
        {
            fprintf(stdout, "code:%d, error msg:%s", ret, msg);
        }
        dwmon_clear_env(handle);
        return ret;
    }
    //登录监视器
    ret = dwmon_login(handle, "SYSDBA", "DMdba_123");
    if (ret < 0)
    {
        fprintf(stdout, "dwmon login failed!\n");
        //获取ret对应的错误描述信息
        dwmon_get_error_msg_by_code(handle, ret, msg, 4097, &msg_len);
        if (msg_len > 0)
        {
            fprintf(stdout, "code:%d, error msg:%s", ret, msg);
        }
    }
    //执行其他命令 
    //...
    //退出登录
    dwmon_logout(handle);
    //清理环境 
    dwmon_clear_env(handle);
    system("pause");
    return 0;
}
```

#### 10.2.6.2 Linux 编程示例

这里给出 C 程序的编程示例，运行环境为 Linux 操作系统，使用时可根据实际情况调整代码。

本例中有两个源文件：test\_dwmon\_linux.h、test\_dwmon\_linux.c，存放在/dm/test 目录下，此目录下还包含 dll 头文件 dwmon\_dll.h 和监视器配置文件 dmmonitor.ini。

本例中动态链接库文件存放在/opt/dm/bin 目录下，程序中使用相对路径方式加载 libdwmon.so 文件，需要先设置环境变量：

```
export LD_LIBRARY_PATH=/opt/dm/bin:\$LD_LIBRARY_PATH
```

注意：此种方式只对当前会话有效，可考虑写入到~/.bashrc 或~/.bash\_profile 文件中永久生效。

gcc 编译命令：

```
gcc -o test_dwmon_linux test_dwmon_linux.c -ldl -rdynamic -lpthread
```

编译成功后，执行程序：

```
./test_dwmon_linux
```

test\_dwmon\_linux.h 源码如下：

```
##include "dwmon_dll.h"

##ifndef _TEST_DWMON_H _

##define _TEST_DWMON_H_

typedef void (*dwmon_msg_event_wait_fun_t)(mhandle mhdle);

typedef mbool (*dwmon_get_msg_exit_flag_fun_t)(mhandle mhdle);

typedef void (*dwmon_set_msg_exit_event_fun_t)(mhandle mhdle);

typedef void (*dwmon_msg_event_deinit_fun_t)(mhandle mhdle);

typedef DWMON_RETURN (*dwmon_deinit_fun_t)(mhandle mhdle);

typedef DWMON_RETURN (*dwmon_free_handle_fun_t)(mhandle mhdle);

typedef DWMON_RETURN (*dwmon_alloc_handle_fun_t)(mhandle* mhdle);

typedef DWMON_RETURN (*dwmon_logout_fun_t)(mhandle mhdle);

typedef

DWMON_RETURN

(*dwmon_get_exec_msg_fun_t)(

    mhandle mhdle,

    mschar* buf_msg,

    muint4 buf_len,

    muint4* msg_len_out,

    muint4* get_flag

);

typedef

DWMON_RETURN

(*dwmon_get_error_msg_by_code_fun_t)(

    mhandle mhdle,

    mint4 code,

    mschar* buf_msg,

    muint4 buf_len,

    muint4* msg_len_out

);

typedef

DWMON_RETURN

(*dwmon_init_fun_t)(

    mhandle mhdle,

    mschar* ini_path,

    mschar* log_path

);

typedef

DWMON_RETURN

(*dwmon_login_fun_t)(

    mhandle mhdle,

    mschar* username,

    mschar* password

);

##endif
```

test\_dwmon\_linux.c 源码如下：

```
#include "stdio.h"
#include "stdlib.h"
#include "dlfcn.h"
#include "pthread.h"
#include "test_dwmon_linux.h"

dwmon_alloc_handle_fun_t            dwmon_alloc_handle_fun;
dwmon_free_handle_fun_t             dwmon_free_handle_fun;
dwmon_init_fun_t                    dwmon_init_fun;
dwmon_deinit_fun_t                  dwmon_deinit_fun;
dwmon_msg_event_wait_fun_t          dwmon_msg_event_wait_fun;
dwmon_get_msg_exit_flag_fun_t       dwmon_get_msg_exit_flag_fun;
dwmon_set_msg_exit_event_fun_t      dwmon_set_msg_exit_event_fun;
dwmon_msg_event_deinit_fun_t        dwmon_msg_event_deinit_fun;
dwmon_get_exec_msg_fun_t            dwmon_get_exec_msg_fun;
dwmon_get_error_msg_by_code_fun_t   dwmon_get_error_msg_by_code_fun;
dwmon_login_fun_t                   dwmon_login_fun;
dwmon_logout_fun_t                  dwmon_logout_fun;

//消息线程 
void*
dwmon_get_msg_thread(
    mhandle         handle
)
{
    mschar          buf_msg[4097];
    muint4          msg_len_out;
    muint4          get_flag;
    DWMON_RETURN    code;

    while (1)
    {
        //等待消息事件
        dwmon_msg_event_wait_fun(handle);
        //获取退出标记
        if (dwmon_get_msg_exit_flag_fun(handle) == 1)
        {
            break;
        }
        do 
        {
            //获取并打印消息
            code = dwmon_get_exec_msg_fun(handle, buf_msg, 4097, &msg_len_out, &get_flag);
            if (code >=0 && msg_len_out > 0)
            {
                fprintf(stdout, "%s", buf_msg);
            }
        } while (get_flag); /* 判断是否还有未读消息 */
    }
  
    //设置退出事件 
    dwmon_set_msg_exit_event_fun(handle);
    return NULL;
}

//清理环境 
void
dwmon_clear_env(
    mhandle     handle
)
{
    //通知并等待dmmon_get_msg_thread消息线程退出 
    dwmon_msg_event_deinit_fun(handle);
    //销毁监视器环境 
    dwmon_deinit_fun(handle);
    //释放句柄
    dwmon_free_handle_fun(handle);
}

int
dwmon_load_fun(
    void*           handle
)
{
    char*           err = NULL;

    dwmon_alloc_handle_fun = dlsym(handle, "dwmon_alloc_handle");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_alloc_handle error! desc:%s\n", err);
        return -1;
    }

    dwmon_free_handle_fun   = dlsym(handle, "dwmon_free_handle");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_free_handle error! desc:%s\n", err);
        return -1;
    }
  
    dwmon_init_fun  = dlsym(handle, "dwmon_init");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_init error! desc:%s\n", err);
        return -1;
    }

    dwmon_deinit_fun    = dlsym(handle, "dwmon_deinit");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_deinit error! desc:%s\n", err);
        return -1;
    }

    dwmon_msg_event_wait_fun    = dlsym(handle, "dwmon_msg_event_wait");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_msg_event_wait error! desc:%s\n", err);
        return -1;
    }

    dwmon_get_msg_exit_flag_fun = dlsym(handle, "dwmon_get_msg_exit_flag");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_get_msg_exit_flag error! desc:%s\n", err);
        return -1;
    }

    dwmon_set_msg_exit_event_fun = dlsym(handle, "dwmon_set_msg_exit_event");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_set_msg_exit_event error! desc:%s\n", err);
        return -1;
    }

    dwmon_msg_event_deinit_fun = dlsym(handle, "dwmon_msg_event_deinit");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_msg_event_deinit error! desc:%s\n", err);
        return -1;
    }

    dwmon_get_exec_msg_fun = dlsym(handle, "dwmon_get_exec_msg");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_get_exec_msg error! desc:%s\n", err);
        return -1;
    }

    dwmon_get_error_msg_by_code_fun = dlsym(handle, "dwmon_get_error_msg_by_code");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_get_error_msg_by_code error! desc:%s\n", err);
        return -1;
    }

    dwmon_login_fun = dlsym(handle, "dwmon_login");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_login error! desc:%s\n", err);
        return -1;
    }

    dwmon_logout_fun = dlsym(handle, "dwmon_logout");
    if ((err = dlerror()) != NULL)
    {
        dlclose(handle);

        printf("dlsym dwmon_logout error! desc:%s\n", err);
        return -1;
    }

    return 0;
}

int
main()
{
    DWMON_RETURN    ret;
    mhandle         handle;
    void*           dlhandle;
    char            msg[4097];
    int             msg_len;
    pthread_t       tid;

    //打开动态链接库
    dlhandle    = dlopen("libdwmon.so", RTLD_NOW);
    if (dlhandle == NULL)
    {
        printf("dlopen error! desc: %s\n", dlerror());
        return -1;
    }
    //加载dll函数 
    ret = dwmon_load_fun(dlhandle);
    if (ret < 0)
    {
        dlclose(dlhandle);
        return -1;
    }

    //分配操作句柄 
    ret = dwmon_alloc_handle_fun(&handle);
    if (ret < 0)
    {
        fprintf(stdout, "dwmon alloc handle failed!\n");
      
        //获取ret对应的错误描述信息 
        dwmon_get_error_msg_by_code_fun(handle, ret, msg, 4097, &msg_len);
        if (msg_len > 0)
        {
            fprintf(stdout, "code:%d, error msg:%s", ret, msg);
        }

        dlclose(dlhandle);

        return ret;
    }

    //创建消息线程 
    ret     = pthread_create(&tid, NULL, dwmon_get_msg_thread, handle);
    if(ret != 0)
    {
        fprintf(stdout, "pthread_create failed!\n");
  
        dwmon_free_handle_fun(handle);
        dlclose(dlhandle);

        return ret;
    }

    //初始化监视器环境，可以选择忽略-15错误（建立到所有守护进程连接失败，可能当前守护进程都还未启动） 
    ret = dwmon_init_fun(handle, "/dm/test/dmmonitor.ini", "/dm/test/log");
    if (ret < 0 && ret != -15)
    {
        fprintf(stdout, "dwmon init failed!\n");
  
        // 获取ret对应的错误描述信息 
        dwmon_get_error_msg_by_code_fun(handle, ret, msg, 4097, &msg_len);
        if (msg_len > 0)
        {
            fprintf(stdout, "code:%d, error msg:%s", ret, msg);
        }

        dwmon_clear_env(handle);
        dlclose(dlhandle);

        return ret;
    }

    //登录监视器 
    ret = dwmon_login_fun(handle, "SYSDBA", "DMdba_123");
    if (ret < 0)
    {
        fprintf(stdout, "dwmon login failed!\n");

        //获取ret对应的错误描述信息 
        dwmon_get_error_msg_by_code_fun(handle, ret, msg, 4097, &msg_len);
        if (msg_len > 0)
        {
            fprintf(stdout, "code:%d, error msg:%s", ret, msg);
        }
    }

    //执行其他命令 
    //...

    //退出登录
    dwmon_logout_fun(handle);
  
    //清理环境 
    dwmon_clear_env(handle);

    dlclose(dlhandle);
  
    return 0;
}
```

### 10.2.7 Java 编程示例

这里给出 Java 程序的编程示例，运行环境为 Eclipse，使用加载监视器 jar 包的方式，jar 包名称为 com.dameng.jni\_8.0.0.jar，注意此处仅为使用示例，实际使用时可以根据自己的需求再做调整。

Linux 环境下需要安装 linux 版本的 jdk 和 Eclipse，下面的源码示例为 windows 环境，linux 下需要修改源码中的路径格式，其他不需要改动。

```
package com.dameng.test;
import com.dameng.console.dwmon.*;
public class DwMonTest {
    public DwMonDLL monDll = null;
    public DwMonMsg    monMsg = null;
    public Thread msgThread = null;
    public String ini_path = "D:\\dwmon\\dmmonitor.ini";
    public String log_path = "D:\\dwmon\\log";
    public String username = "SYSDBA";
    public String password = "DMdba_123";
    //接收消息线程
    public void startThread()
    {
        msgThread = new Thread(new Runnable()
        {
            @Override
            public void run()
            {
                while (true)
                {
                    //等待消息事件
                    monDll.dwmon_msg_event_wait();
      
                    //获取退出标记
                    if (monDll.dwmon_get_msg_exit_flag() == true)
                        break;
                    do
                    {
                        //获取并打印消息
                        monMsg = monDll.dwmon_get_exec_msg();
                        if(monMsg.getReturnCode() < 0)
                            break;
                        if(monMsg.getMsg().length() > 0)
                        {
                            System.out.print(monMsg.getMsg());
                        }
      
                    } while (monMsg.getMsgFlag() == 1); //是否还有未读消息
                }
                //设置退出标记
                monDll.dwmon_set_msg_exit_event();
            }
        });
        //启动线程
        msgThread.start();
    }
    //退出线程
    public void endThread() throws InterruptedException
    {
        if (msgThread != null && msgThread.isAlive())
        {
            //通知并等待消息线程退出
            monDll.dwmon_msg_event_deinit();
        }
    }
    public void test() throws InterruptedException
    {
        boolean     ret1 = false;
        int         ret2 = 0;
DwMonMsg    retMsg = null;

        monDll = new DwMonDLL();
        //分配句柄
        ret1 = monDll.dwmon_init_handle();
        if (ret1 == false)
        {
            System.out.println("dwmon alloc handle failed!");
            return;
        }
        else
        {
            System.out.println("dwmon alloc handle success!");
        }
        //启动消息接收线程
        startThread();
        //初始化监视器，可以选择忽略-15错误（建立到所有守护进程连接失败，可能当前守护进程都还未启动）
        ret2 = monDll.dwmon_init_env(ini_path, log_path);
        if (ret2 < 0 && ret2 != -15) 
        {
            System.out.println("dwmon init failed!");
            // 获取ret2对应的错误描述信息 
            retMsg = monDll.dwmon_get_error_msg_by_code(ret2);
            if (retMsg.getReturnCode() >= 0)
            {
                System.out.println("code:" + ret2 + "," + retMsg.getMsg());
            }
            //初始化失败，退出线程，销毁句柄
            endThread();
            monDll.dwmon_free_handle();
            return;
        }
        else
        {
            System.out.println("dwmon init success!");
        }
        //登录监视器
        ret2 = monDll.dwmon_login(username, password);
        if (ret2 < 0)
        {
            System.out.println("login failed!");
            //获取ret2对应的错误描述信息 
            retMsg = monDll.dwmon_get_error_msg_by_code(ret2);
            if (retMsg.getReturnCode() >= 0)
            {
                System.out.println("code:" + ret2 + "," + retMsg.getMsg());
            }
        }
        //退出登录
        monDll.dwmon_logout();
        //退出消息线程
        endThread();
        //销毁监视器环境
        monDll.dwmon_deinit_env();
        //销毁句柄
        monDll.dwmon_free_handle();
    }
    /**
     * @param args
     * @throws InterruptedException 
    **/
    public static void main(String[] args) throws InterruptedException {
        DwMonTest test = new DwMonTest();
        test.test();
    }
}
```

### 10.2.8 错误码汇编

#### 10.2.8.1 监视器

| **错误码** | **解释** |
| --- | --- |
| \-1 | 普通错误 |
| \-2 | 无效的句柄 |
| \-3 | 初始化日志信息失败 |
| \-4 | 初始化系统信息失败 |
| \-5 | 未登录监视器或服务器公钥发生变化，请重新登录 |
| \-6 | 读取 dmmonitor.ini 文件失败（路径错误或配置错误或没有权限） |
| \-7 | 无效的日志文件路径 |
| \-8 | 设置命令执行标记失败，此标记已被设置，在标记被重置后才允许再次设置 |
| \-9 | 重置命令执行标记失败，已经被重置过 |
| \-10 | 实例故障或者实例对应的守护进程故障 |
| \-11 | 系统运行异常 |
| \-12 | MPP 控制文件不一致 |
| \-13 | 守护进程控制文件中没有记录项 |
| \-14 | 同一个守护系统中有多个确认监视器 |
| \-15 | 建立到所有守护进程的连接失败，可能守护进程都未启动，由用户决定是否忽略此错误码继续往下执行，如果不忽略此错误，认定初始化失败，则需要先销毁监视器环境，再释放操作句柄 |
| \-16 | 非法的参数，参数为空或长度超长或值非法 |
| \-17 | 没有找到 code 对应的错误信息 |
| \-18 | 内存不足 |
| \-19 | 监视器已达到最大个数（同一个守护进程组中最多允许同时启动 10 个监视器） |
| \-20 | 当前无法判断备库是否满足恢复条件，需要稍后重试（可能存在监视器命令正在执行，指定实例还未达到恢复间隔，或者指定实例上的 RLOG\_BUF 还未全部重演完成等情况） |
| \-21 | 备库实例不满足恢复条件 |
| \-22 | 当前无法判断实例是否可自动 OPEN，需要稍后重试（可能存在监视器命令正在执行，或者实例还未启动到 MOUNT 状态等情况） |
| \-23 | 实例无法自动 OPEN |
| \-24 | 实例已经处于 OPEN 状态，但守护进程无法切换为 OPEN 状态 |
| \-25 | 主库实例处于 OPEN 状态且主库守护进程为 OPEN 状态，但存在其他异常实例 |
| \-26 | 没有正常主库（实例和守护进程都是 OPEN 状态），或者组中全部是 LOCAL 实例，但存在有实例没有 OPEN，需要等待守护进程处理完成 |
| \-27 | 没有正常主库（实例和守护进程都是 OPEN 状态），或者组中全部是 LOCAL 实例，但存在有实例没有 OPEN，需要用户确认是否手动干预 |
| \-28 | 需要先正常销毁环境，再释放句柄 |
| \-29 | MON\_WALLET\_LOCATION 为空，或该路径下没有合法的 wallet 文件 |
| \-30 | 第三方加密库加载失败，或者监视器生成密钥对失败，需要检查第三方加密库文件是否存在 |
| \-31 | 联机日志空间太小 |
| \-32 | 监视器名长度非法 |
| \-33 | 当前不是多实例监视器 |
| \-542 | SUSPEND 工作线程超时 |
| \-8013 | 接收守护进程消息超时 |
| \-8014 | 用户自定义异常或者未知错误 |
| \-8021 | 实例故障 |
| \-8037 | 实例不是 MOUNT 状态 |
| \-8038 | 有消息正在发送中,您的命令当前不能执行 |
| \-8042 | 实例故障, 操作终止 |
| \-8043 | 接收守护进程消息超时，操作终止 |
| \-8044 | 实例执行命令失败 |
| \-8045 | 实例名无效或尚未收到实例消息 |
| \-8046 | 守护进程不是 STARTUP 或 OPEN 状态 |
| \-8047 | DSC 集群 ckpt\_lsn < max\_redo\_lsn，操作被限制，建议对 DSC 控制节点手动执行 checkpoint 系统函数主动推进检查点 |
| \-8055 | STOP 守护进程组失败 |
| \-8058 | STARTUP 守护进程组失败 |
| \-8062 | 实例的模式不匹配 |
| \-8069 | 实例执行 SQL 语句失败 |
| \-8078 | 实例状态不匹配 |
| \-8079 | 组中存在多个 PRIMARY 实例，或不存在实例满足：1.实例是 PRIMARY&OPEN 状态 2.守护进程是 OPEN 状态 3.实例状态(INST\_OK)OK |
| \-8082 | 实例切换失败 |
| \-8083 | 使用实例接管失败 |
| \-8089 | 实例不是 MOUNT 或 SUSPEND 状态，不允许 OPEN |
| \-8099 | 修改所有实例归档为无效状态失败 |
| \-8100 | 组中存在多个 OPEN 状态的 PRIMARY 实例 |
| \-8106 | SWITCHOVER 所用的实例是 PRIMARY 模式 |
| \-8111 | 待切换实例归档不是有效状态 |
| \-8113 | 监视器操作冲突，终止操作 |
| \-8121 | 实例非 PRIMARY 或 STANDBY 模式 |
| \-8123 | 守护进程状态不匹配，不是 STARTUP、OPEN 或 RECOVERY 状态 |
| \-8125 | 实例故障，实例不是 OK 状态 |
| \-8128 | 实例开始执行 SQL 语句 |
| \-8136 | 监视器操作冲突，当前监视器的 mid 值与接收到的 mid 值不匹配 |
| \-8137 | 检测到故障实例已恢复，重新修改实例为 STANDBY&OPEN 状态 |
| \-8145 | 消息校验失败 |
| \-8146 | 无效的组名 |
| \-8148 | 系统组内没有或有多个活动全局守护类型的 PRIMARY 实例（如果是 DSC 集群，要求是 DSC\_OPEN 状态） |
| \-8149 | 内存分配失败 |
| \-8155 | 实例的 MPPCTL 文件更新失败 |
| \-8157 | MPPCTL 文件恢复失败 |
| \-8159 | 构造新的 MPPCTL 文件失败 |
| \-8163 | 通知实例更新 MPPCTL 文件失败 |
| \-8165 | 尚未收到组的 MPPCTL 消息，请确保组中有活动实例(实例 dm.ini 中的 MPP\_INI 配置为 1，且实例本地有 dmmpp.ctl 文件) |
| \-8178 | 实例 OPEN 失败 |
| \-8180 | 到守护进程的连接断开 |
| \-8182 | 根据实例名获取发送端口失败 |
| \-8183 | 不同组中主库实例的 MPP 控制文件不一致 |
| \-8191 | 用户名加密失败 |
| \-8192 | 密码加密失败 |
| \-8197 | 用户名或密码为空或长度超长 |
| \-8199 | 监视器尚未收到公钥信息，请稍候重试 |
| \-8201 | 监视器生成密钥对失败，请重试登录 |
| \-8203 | 守护进程不是 STARTUP/OPEN/RECOVERY 状态，或实例非 OK 状态，校验登录信息失败 |
| \-8204 | 当前没有活动实例或守护进程状态不匹配，登录信息校验失败 |
| \-8206 | 用户名或密码错误，或用户没有 DBA 权限 |
| \-8210 | 登录监视器失败 |
| \-8219 | 守护类型未知或是 LOCAL 守护类型(可使用 show 命令查看系统运行状态) |
| \-8220 | 守护进程不是 STARTUP/OPEN/SHUTDOWN 状态，不能修改参数 |
| \-8222 | 通知启动实例失败（启动实例的守护进程失败） |
| \-8223 | 通知启动实例失败，实例已处于运行状态，或 watch 已配置自动重启，或 watch 的启动参数配置有误 |
| \-8229 | 实例 SHUTDOWN 失败 |
| \-8231 | 退出组中所有活动实例失败 |
| \-8234 | STOP 所有守护进程组失败 |
| \-8236 | Startup 所有守护进程组失败 |
| \-8238 | 启动所有组的实例失败 |
| \-8240 | 退出所有组的活动实例失败 |
| \-8243 | 监视器还未收到操作组的任何一个守护进程消息(不包括 local 守护类型) |
| \-8257 | 组中所有实例均已处于 SHUTDOWN 状态 |
| \-8265 | 尚未收到任何组的 MPPCTL 消息 |
| \-8272 | STOP 实例的守护进程失败 |
| \-8275 | STARTUP 实例的守护进程失败 |
| \-8277 | 守护进程不是 Startup 或 SHUTDOWN 状态 |
| \-8280 | 启动组中的所有实例失败 |
| \-8299/-8427 | 切换守护进程状态失败 |
| \-8309 | 修改实例实时归档为无效状态失败 |
| \-8311 | 切换守护进程为 OPEN 状态失败 |
| \-8333 | 不符合 OPEN FORCE 条件 |
| \-8340 | 通知守护进程增加 CTL 记录失败 |
| \-8342 | 监视器未收到操作组的所有守护进程消息(不包括 local 守护类型) |
| \-8344 | 实例不满足条件：1.实例是 STANDBY&OPEN 状态 2.守护进程是 OPEN 状态 3.实例归档状态为 VALID |
| \-8345 | 尚未收到守护进程的控制文件消息 |
| \-8346 | 主备库的守护进程控制文件不一致 |
| \-8359 | 实例非 PRIMARY 模式 |
| \-8360 | 组中已经存在 PRIMARY&OPEN 状态的实例 |
| \-8368 | 请等待守护进程自动 OPEN 实例，不允许手动 OPEN FORCE |
| \-8371 | 守护进程不是 STARTUP 状态 |
| \-8380 | 守护进程的控制文件不是有效状态 |
| \-8387 | 守护类型未知或不是 MPP 主备环境，不支持此命令 |
| \-8388 | 组中有活动 PRIMARY 实例，不再查找可接管实例列表 |
| \-8389 | 存在分裂实例，不允许执行命令 |
| \-8390 | 守护进程不是 OPEN 状态 |
| \-8392 | 实例不是 STANDBY&OPEN 状态 |
| \-8393 | 存在 SLSN 更大的活动实例，不允许接管 |
| \-8394 | 存在 PRIMARY & OPEN 状态的实例，不允许接管 |
| \-8395 | 没有找到实例对应的 PRIMARY 实例，不允许接管 |
| \-8396 | 被接管实例故障前不是 PRIMARY&OPEN，不允许接管 |
| \-8397 | 被接管实例的 flsn 大于接管用实例的 slsn，不允许接管 |
| \-8398 | 守护进程故障前不是 OPEN 或 RECOVERY 状态，不允许接管 |
| \-8399 | 被接管实例仍然处于活动状态，不允许接管 |
| \-8400 | 被接管实例故障前到接管用实例的归档状态无效，不允许接管 |
| \-8401 | 守护进程的控制文件不是有效状态 |
| \-8402 | 实例的 OPEN 记录不一致 |
| \-8403 | 存在 SLSN 更大的实例，不允许接管 |
| \-8404 | 没有收到守护进程的实例的 OPEN 记录消息，不允许接管 |
| \-8405 | 存在多个或没有 PRIMARY&OPEN 状态的实例 |
| \-8406 | 备库对应的 PRIMARY 实例不是 PRIMARY&OPEN 状态 |
| \-8407 | 实例不是 PRIMARY&OPEN 状态 |
| \-8408 | 实例的归档状态无效或 MAL 链路异常 |
| \-8416 | 组中存在多个 PRIMARY&OPEN 状态的实例 |
| \-8419 | 未找到实例对应的 PRIMARY 实例 |
| \-8420 | 被接管实例仍然处于活动状态，模式/状态或 LSN 值不符合接管条件 |
| \-8424 | 守护进程配置不一致 |
| \-8425 | 非 MPP 主备环境，不支持配置多组 |
| \-8428 | 设置 DMWATCHER 的 MID 命令执行失败 |
| \-8430 | 实例 \[STANDBY, DW\_TYPE:LOCAL\]配置错误，被同时配置在多个实例，只允许配置在一个源实例上 |
| \-8431 | 组中守护进程故障或实例故障，或尚未收到消息 |
| \-8435 | 组中没有活动 PRIMARY 实例 |
| \-8436 | 实例发生分裂，需要用户干预 |
| \-8439 | 守护进程不是 OPEN 状态 |
| \-8440 | 实例不是 OPEN 状态 |
| \-8441 | 守护进程状态为 ERROR |
| \-8442 | 实例可作为 STANDBY 模式重加入，请等待守护进程自动处理 |
| \-8444 | 实例无法自动重加入，需要等实例恢复正常，或者用户干预 |
| \-8445 | 尚未收到组的 MPPCTL 消息，请检查组中有活动的 PRIMARY 实例，并且 MPP\_INI 已配置，且存在有 dmmpp.ctl 文件 |
| \-8446 | 实例运行异常 |
| \-8454 | 存在多个守护进程控制文件有效的实例，且不可互相加入 |
| \-8455 | 未指定实例名 |
| \-8456 | 未指定组名 |
| \-8457 | 组中没有活动的守护进程或尚未收到消息 |
| \-8458 | 守护进程不是 OPEN 或 STARTUP 状态 |
| \-8459 | 实例不是 STANDBY 模式 |
| \-8460 | 实例不是 OPEN 或 MOUNT 状态 |
| \-8461 | 实例属于其他组，不在指定的组中 |
| \-8496 | 组中当前没有可执行的备库 |
| \-8497 | 实例的守护进程是 local 守护类型 |
| \-8498 | 无效的参数名或者参数值 |
| \-8500 | 修改配置参数失败 |
| \-8503 | 修改组中实例对应的守护进程配置参数失败 |
| \-8504 | 监视器不支持监控不同守护类型的组，且只有 MPP 主备环境支持多组 |
| \-8505 | 组中不存在 PRIMARY&OPEN 状态的实例或者有多个 PRIMARY 实例或者 PRIMARY 实例故障 |
| \-8506 | 没有找到实例对应的 PRIMARY 实例 |
| \-8507 | 查找实例的归档信息失败 |
| \-8508 | 实例对应的 PRIMARY 实例的守护进程不是 STARTUP/OPEN/RECOVERY 状态，不允许执行此命令 |
| \-8514 | 修改组中实例的恢复时间间隔失败 |
| \-8515 | 指定的恢复时间间隔非法，必须在 3~86400(s)范围内 |
| \-8520 | 修改实例的归档为无效状态失败 |
| \-8521 | 实例是 PRIMARY 模式，不允许执行此命令 |
| \-8522 | 组中存在多个 PRIMARY 实例 |
| \-8523 | 组中当前没有活动的 PRIMARY 实例 |
| \-8524 | 实例的归档信息没有找到 |
| \-8525 | 没有找到实例的源实例或尚未收到消息 |
| \-8528 | 不符合设置归档失效条件 |
| \-8529 | 实例对应的主库不唯一 |
| \-8530 | 不符合退出实例条件 |
| \-8532 | 将实例分离出守护进程组失败 |
| \-8533 | 不符合 STARTUP 守护进程组执行条件 |
| \-8534 | 不符合启动组中的所有实例条件 |
| \-8535 | 不符合 STOP 守护进程组条件 |
| \-8536 | 修改组中所有备库归档无效失败 |
| \-8538 | 修改所有组的所有备库归档无效失败 |
| \-8540 | 修改组中所有备库的恢复间隔失败 |
| \-8542 | 修改所有组的所有备库的恢复间隔失败 |
| \-8545 | 修改所有组守护进程配置参数失败 |
| \-8547 | 实例加回到守护进程组失败 |
| \-8551 | 实例状态正常，归档有效，在守护进程组中运行正常，不需要再重加入 |
| \-8552 | 实例当前不是运行状态，不符合执行条件 |
| \-8553 | 守护进程不是 OPEN 或 RECOVERY 状态 |
| \-8556 | 尚未收到组中主库实例的 MPPCTL 消息，请确保组中有活动的 PRIMARY 实例(PRIMARY 实例的 MPP\_INI 配置为 1，且实例本地有 dmmpp.ctl 文件) |
| \-8557 | 尚未收到任何组中主库实例的 MPPCTL 消息 |
| \-8562 | 守护进程组执行 KILL INSTANCE 命令失败 |
| \-8564 | 强杀所有组当前的活动实例失败 |
| \-8565 | 实例正在执行守护进程发起的命令，请稍候重试 |
| \-8567 | 切换守护进程状态失败 |
| \-8568 | 守护进程组中存在多个 PRIMARY&OPEN 状态的实例，不满足 RECOVER 条件 |
| \-8569 | 守护进程组中没有 PRIMARY&OPEN 状态的实例，不满足 RECOVER 条件 |
| \-8570 | 指定实例不在主库实例的归档目标中，不满足 RECOVER 条件 |
| \-8571 | 指定实例是 PRIMARY 模式，不满足 RECOVER 条件 |
| \-8573 | 实例的守护进程 OPEN 记录不是有效状态，命令执行失败 |
| \-8574 | 接收守护进程消息超时，无法检测指定实例是否可以自动 OPEN |
| \-8575 | 实例的模式不匹配，获取实例对应的主库信息失败 |
| \-8576 | 获取实例对应的主库信息失败（实例未收到过主库发送的归档信息） |
| \-8617 | 实例的守护进程不是 STARTUP/OPEN 状态，不允许执行此命令。 |
| \-8618 | 当前无法比较 LSN 大小，存在交叉情况。 |
| \-8619 | 守护进程执行失败。 |
| \-8623 | 修改库中所有正常的守护进程配置参数失败。 |
| \-8624 | 在归档目标中未找到指定实例。 |
| \-8625 | 此命令不支持启动 DSC 集群，请等待 CSS 自动拉起或者通过 DSC 监视器手动拉起。 |
| \-8626 | 服务器当前有操作正在执行，需要等当前操作完成，请稍候再试！ |
| \-8627 | 库的控制节点尚未选出，请等待 CSS 自动处理！ |
| \-8631 | DSC 集群正在启动，或者正在执行故障处理或故障重加入，请等待 DSC 集群自动处理完成。 |
| \-8632 | 控制守护进程执行成功，从 dmwatcher 执行失败，不影响 DSC 集群使用。 |
| \-8633 | 修改组中主库的控制守护进程到备库的恢复时间间隔成功，从 dmwatcher 修改失败，不影响 DSC 集群使用。 |
| \-8634 | DSC 集群实例故障或者 DSC 集群不是 DSC\_OPEN 状态, 操作终止。 |
| \-8635 | 主库实例的 flsn 不等于备库实例的 flsn，命令执行失败。 |
| \-8636 | 待执行清理的源库实例的守护进程不是 STARTUP/OPEN/RECOVERY 状态，不允许执行此命令。 |
| \-8637 | 组中不存在活动主库。 |
| \-8638 | 获取集群的控制守护进程信息失败，请检查控制守护进程是否发生过变化并且已经启动。 |
| \-8639 | 系统中存在有未选出控制节点的库，需要先等控制节点选出，请稍候再试！ |
| \-8649 | 实例还未选出控制节点，请先等 DSC 集群选出控制节点。 |
| \-8650 | 实例的控制守护进程故障，无法判断是否可以自动 OPEN。 |
| \-8651 | 实例已经处于 OPEN 状态，但是控制守护进程故障。 |
| \-8652 | PRIMARY 实例的守护进程不是 STARTUP/OPEN/RECOVERY 状态，不允许执行此命令 |
| \-8653 | 被接管实例故障前没有控制守护进程，或者从 dmwatcher 还处于活动状态 |
| \-8654 | 实例的守护进程正在进行中断处理，请稍候重试! |
| \-8655 | 实例已经处于 SHUTDOWN 状态 |
| \-8656 | 主库到备库实例的归档仍然是有效状态，不允许执行此命令（需要先 detach 备库） |
| \-8657 | 实例模式未知，不允许执行此命令 |
| \-8659 | 强杀实例失败 |
| \-8661 | 实例已经不是活动状态并且守护进程已处于 SHUTDOWN 状态 |
| \-8664 | 退出实例失败 |
| \-8667 | 启动实例失败 |
| \-8668 | 通知启动实例失败，实例已处于运行状态，或者被 dmcss 强制 HALT，或者 dmcss 已配置自动重启，或者 dmcss 的启动参数配置有误 |
| \-8669 | 组中配置的 LOCAL 守护类型的库超过最大值，请减少 LOCAL 守护类型的库个数以避免出现异常 |
| \-8670 | 组中配置的 GLOBAL 守护类型的库超过最大值，请减少 GLOBAL 守护类型的库个数以避免出现异常 |
| \-8671 | 组中不存在 DSC 集群，不允许执行此命令 |
| \-8673 | 打开组中所有 DSC 节点的自动拉起功能失败 |
| \-8676 | 打开库中所有节点的自动拉起功能失败，请检查 dmcss 是否故障或者配置有自动拉起参数 |
| \-8679 | 关闭组中所有 DSC 节点的自动拉起功能失败 |
| \-8682 | 关闭库中所有节点的自动拉起功能失败 |
| \-8684 | 此命令需要转发 dmcss 执行，如果守护进程正常，请检查 dmcss 是否出现异常 |
| \-8685 | 守护进程接收监视器消息超时，命令执行信息已经被清理，操作终止 |
| \-8686 | 实例的守护进程配置有自动拉起，请等待守护进程将其自动拉起 |
| \-8687 | DSC 集群中存在有可以执行自动拉起的 dmcss，请确保所有 dmcss 的自动拉起功能是打开状态，并等待 dmcss 将其自动拉起 |
| \-8688 | 实例所在 DSC 集群控制守护进程故障或该命令不能发送到普通守护进程上执行, 操作终止 |
| \-8689 | dmmonitor.ini 中存在有需要合并的 MON\_DW\_IP 配置项（属于同一个 DMDSC 集群），需要以“/”分隔开，修改完成后，需要重启监视器！ |
| \-8690 | dmmonitor.ini 中存在有不完整的 MON\_DW\_IP 配置项（需要配置 DMDSC 集群内所有守护进程的连接信息），以“/”分隔开，修改完成后，需要重启监视器！ |
| \-8691 | 指定库中的控制节点尚未选出! |
| \-8699 | 守护进程到实例的连接断开，命令执行失败 |
| \-8700 | 守护进程到服务器链路断开，校验登录口令失败，请稍后重试 |
| \-8701 | 服务器公钥发生变化，请重新登录 |
| \-8702 | STARTUP 实例的守护进程失败 |
| \-8703 | STOP 实例的守护进程失败 |
| \-8704 | 不符合 STARTUP 库的守护进程监控功能的执行条件 |
| \-8705 | 不符合 STOP 库的守护进程监控功能的执行条件 |
| \-8706 | 开始清理组中源库到所有备库（包括异步备库和同步备库）的归档发送信息 |
| \-8707 | 实例正在状态切换中，或者守护进程正在状态处理中 |
| \-8708 | 当前监视器不是 LEADER |
| \-8709 | 实例故障前的守护进程是 ERROR 状态，不符合被其他实例自动接管的条件 |
| \-8710 | 无效的 ARCH SEND UNTIL TIME 时间值 |
| \-8711 | 实例不是异步备库，不允许执行此命令 |
| \-8712 | 修改组中源库到实例的重演时间点为成功 |
| \-8713 | 修改组中源库到实例的重演时间点为失败 |
| \-8714 | 取消组中源库到实例的重演时间点成功 |
| \-8715 | 实例对应的源库实例的守护进程不是 STARTUP/OPEN/RECOVERY 状态，不允许执行此命令 |
| \-8716 | 修改组中源库到实例的重演时间点为成功，但通知源库立即发送归档失败，后续定时器会再触发发送动作 |
| \-8717 | 取消组中源库到实例的重演时间点失败 |
| \-8718 | 实例与实例之间的异步备库配置不一致 |
| \-8719 | 组中待接管备库可能存在消息延迟，上次执行自动接管失败，继续重试 |
| \-8720 | 组上找不到自动接管信息 |
| \-8721 | 主库的控制节点不是 0 号节点，不允许切换为备库 |
| \-8722 | 指定的服务名无效 |
| \-8724 | 归档类型不满足监视器命令的执行条件 |
| \-8725 | 尚未收到库的消息或者主 ep 尚未选出 |
| \-8726 | 本监视器不是确认监视器，不支持此操作 |
| \-8727 | 指定的优先级非法，必须在 1~8 范围内 |
| \-8728 | 实例的守护进程为 MANUAL 模式，不支持此操作 |
| \-8729 | 修改组中实例的自动接管优先级成功 |
| \-8730 | 实例个数非法，自动接管组仅允许指定 2~9 个实例 |
| \-8731 | 设置组的自动接管组成功 |
| \-8732 | 设置组的自动接管组失败 |
| \-8733 | 取消组的自动接管组成功 |
| \-8734 | 取消组的自动接管组失败 |
| \-8735 | 非法的自动接管组配置串，不能指定重复的或者属于同一个数据库的实例名 |
| \-8736 | 非法的自动接管组配置串，格式必须为：(inst1, inst2,...) |
| \-8737 | 实例故障，或者系统状态不匹配，不是 OPEN、SUSPEND 或者 MOUNT 状态 |
| \-8739 | 组中不存在守护进程处于活动状态的 GLOBAL 备库实例，不允许执行此命令 |
| \-8740 | 存在比当前认定主库 ohis 更多的库，不允许备库接管 |
| \-8741 | 开始从守护进程上获取主库的历史信息 |
| \-8742 | 从守护进程上获取主库的历史信息成功 |
| \-8743 | 从守护进程上获取主库的历史信息失败 |
| \-8744 | 选取最新的主库历史信息失败 |
| \-8745 | 无法从备库的守护进程上获取到主库的历史信息 |
| \-8746 | 主库实例故障前没有主 dmwatcher，或者从 dmwatcher 还处于活动状态 |
| \-8747 | 没有找到主库守护进程对应的连接配置项\[IP,PORT\]，请检查 dmmonitor.ini 配置是否正确 |
| \-8748 | 在主库的历史信息中没有找到归档字段，请确认守护进程的版本是否支持此命令 |
| \-8749 | 主库的守护进程仍然存活 |
| \-8750 | 监视器上已经有更新的主库的历史信息 |
| \-8753 | 在守护进程上没有找到主库的历史信息 |

#### 10.2.8.2 守护进程

| **错误码** | **解释** |
| --- | --- |
| \-10194 | 存在有 ep 实例状态不一致，守护进程需要转入 unify\_ep 状态统一各 ep 实例状态。 |
| \-10195 | 守护进程当前处于 unify\_ep 状态或者 login\_check 状态，需要等当前操作完成。 |
| \-10196 | 本地守护进程为 LOCAL 守护类型，可以将实例自动 OPEN。 |
| \-10197 | 本地库不是 PRIMARY 或 STANDBY 模式 |
| \-10201 | 主库或者被恢复备库校验日志失败 |
| \-10203 | 实例广播出来的 dw\_stat\_flag 值和预期值不匹配，当前操作已经被中断。 |
| \-10204 | 主库上未找到被恢复备库需要的归档日志 |
| \-10205 | 守护进程收到监视器命令, 但是本地 server 的 dw\_stat\_flag 标记值已经被设置，不允许执行监视器命令，返回错误给监视器。 |
| \-10209 | 通知本地主库由 suspend 状态重新 open 失败 |
| \-10211 | 检测到远程实例模式、状态不匹配，设置中断标记为 TRUE，等待中断当前处理 |
| \-10212 | 控制节点出现故障 |
| \-10213 | 控制守护进程设置中断标记 5s 之后，DMServer 当前操作还没有被中断掉，先返回错误 code 给监视器，避免监视器命令卡住。 |
| \-10214 | 备库和主库的 PERMANENT\_MAGIC 不匹配 |
| \-10215 | 备库系统状态正在切换中 |
| \-10216 | 需要等待远程 SUSPEND 实例处理完成 |
| \-10217 | 本地主库或备库 DSC 集群 ckpt\_lsn<max\_redo\_lsn，操作被限制，建议对 DSC 控制节点手动执行 checkpoint 系统函数主动推进检查点 |
| \-10219 | 接收 CSS 消息超时 |
| \-10220 | CSS 执行操作冲突，CSS 端当前的 mid 值和发起命令的监视器 mid 值不一致 |
| \-10221 | 到 dmcss 的连接断开 |
| \-10222 | CSS 执行失败 |
| \-10223 | 检测到 CSS 控制节点发生变化，命令中断执行 |
| \-10226 | 获取 CSS 控制节点通信端口失败，CSS 控制节点尚未选出或 CSS 未启动 |
| \-10229 | 设置 CSS 的 MID 命令执行失败 |
| \-10230 | 通知 CSS 拉起本地 EP 失败 |
| \-10233 | 守护进程超时仍未等到 EP STARTUP 成功，命令执行失败 |
| \-10239 | 通知 CSS 退出所有 EP 失败 |
| \-10240 | 守护进程超时仍未等到组中的所有 EP STOP 或 KILL 成功，命令执行失败 |
| \-10242 | 通知 CSS 强制 HALT 所有 EP 失败 |
| \-10244 | 组中节点对应的 CSS 配置的自动拉起参数不匹配，不再通知 CSS 打开自动拉起功能，请检查是否需要修改配置 |
| \-10248 | 通知 CSS 打开节点的自动拉起功能失败 |
| \-10250 | 通知 CSS 关闭节点的自动拉起功能失败 |
| \-10251 | OPEN 实例时实时归档 APPLY\_LSN 校验失败,设置所有归档失效 |
| \-10252 | 没有找到可以执行当前命令的活动 CSS，可能 CSS 故障或者还未选出控制节点或者不符合执行条件 |
| \-10254 | 从 CSS 控制节点广播出来的信息中查找本地 EP 所属的 DB 组失败 |
| \-10255 | 在 DB 组中查找和当前 CSS 相同 dcr\_seqno 的 EP 失败 |
| \-10256 | MID 已经被清理，当前命令执行失败 |
| \-10263 | 收到监视器执行 sql 语句的请求，但是守护进程状态不匹配，当前状态下不允许执行此操作 |
| \-10264 | 本地实例不可加入远程实例，强制 shutdown 本地实例 |
| \-10265 | 正在处理监视器命令，同一时刻只能处理一个监视器命令 |
| \-10266 | 正在执行监视器命令 |
| \-10267 | 没有监视器命令在执行 |
| \-10268 | 已收到相同报文序号的监视器命令 |
| \-10269 | 收到监视器命令，守护进程当前状态不允许执行监视器命令，返回错误 |

#### 10.2.8.3 服务器

show arch send info 命令以及 dwmon\_get\_ep\_arch\_send\_info 接口中输出的服务器错误 code 说明。

<table><tbody><tr height="20"><td colspan="2" height="20" width="144"><b>守护进程通知恢复</b> <font><b>code</b></font> <font><b>：</b></font></td></tr><tr height="20"><td height="20" width="72"><b>错误码</b></td><td width="72"><b>解释</b></td></tr><tr height="31"><td height="31" width="72"><span>0</span></td><td width="72">恢复执行成功</td></tr><tr height="31"><td height="31" width="72"><span>100</span></td><td width="72">未执行恢复操作</td></tr><tr height="61"><td height="61" width="72"><span>-10050</span></td><td width="72">恢复失败，远程实例的模式或状态不匹配</td></tr><tr height="20"><td colspan="2" height="20" width="144"><b>服务器发送归档</b> <font><b>code</b></font> <font><b>：</b></font></td></tr><tr height="20"><td height="20" width="72"><b>错误码</b></td><td width="72"><b>解释</b></td></tr><tr height="20"><td height="20" width="72"><span>0</span></td><td width="72">发送成功</td></tr><tr height="61"><td height="61" width="72"><span>100</span></td><td width="72">未执行发送操作或正在等待归档目标响应</td></tr><tr height="46"><td height="46" width="72"><span>-6018</span></td><td width="72">消息长度超出网络发送消息缓存区</td></tr><tr height="62"><td height="62" width="72"><span>-6010</span></td><td width="72"><span>MAL <font>连接丢失（源库到归档发送目标）</font></span></td></tr><tr height="62"><td height="62" width="72"><span>-6021</span></td><td width="72"><span>MAL <font>链路已断开（源库到归档发送目标）</font></span></td></tr><tr height="31"><td height="31" width="72"><span>-517</span></td><td width="72">系统处于状态切换中</td></tr><tr height="31"><td height="31" width="72"><span>-703</span></td><td width="72">服务器模式不匹配</td></tr><tr height="31"><td height="31" width="72"><span>-518</span></td><td width="72">无效的系统状态</td></tr><tr height="63"><td height="63" width="72"><span>-533</span></td><td width="72">数据库的 <font>PERMANENT_MAGIC</font> <font>不匹配</font></td></tr><tr height="92"><td height="92" width="72"><span>-701</span></td><td width="72">日志复制 <font>LSN</font> <font>值错误（归档目标收到的日志和本地日志不连续）</font></td></tr><tr height="31"><td height="31" width="72"><span>-503</span></td><td width="72">服务器内存不足</td></tr><tr height="32"><td height="32" width="72"><span>-9512</span></td><td width="72"><span>MPP <font>执行停止</font></span></td></tr><tr height="32"><td height="32" width="72"><span>-9513</span></td><td width="72"><span>MPP <font>清理执行</font></span></td></tr><tr height="47"><td height="47" width="72"><span>-9504</span></td><td width="72"><span>MPP <font>收到新的计划，终止当前执行</font></span></td></tr><tr height="46"><td height="46" width="72"><span>-715</span></td><td width="72">（源库）归档日志不存在</td></tr><tr height="62"><td height="62" width="72"><span>-718</span></td><td width="72">（源库）收集到的归档日志和起始 <font>LSN</font> <font>不连续</font></td></tr><tr height="77"><td height="77" width="72"><span>-721</span></td><td width="72">守护进程发起的 <font>recover</font> <font>恢复操作被中断</font></td></tr><tr height="31"><td height="31" width="72"><span>-108</span></td><td width="72">打开重做日志失败</td></tr><tr height="46"><td height="46" width="72"><span>-702</span></td><td width="72">归档日志错，备库重做日志失败</td></tr><tr height="46"><td height="46" width="72"><span>-716</span></td><td width="72">归档日志文件仅包含检查包</td></tr><tr height="31"><td height="31" width="72"><span>-730</span></td><td width="72">归档日志缺失</td></tr><tr height="31"><td height="31" width="72"><span>-731</span></td><td width="72">归档日志重叠</td></tr><tr height="46"><td height="46" width="72"><span>-732</span></td><td width="72">包含多个数据库的归档日志</td></tr><tr height="47"><td height="47" width="72"><span>-733</span></td><td width="72">包含多个 <font>DSC</font> <font>节点的归档日志</font></td></tr><tr height="20"><td height="20" width="72"><span>-6526</span></td><td width="72">重演超时</td></tr><tr height="31"><td height="31" width="72"><span>-9713</span></td><td width="72">数据库魔数校验失败</td></tr><tr height="31"><td height="31" width="72"><span>-737</span></td><td width="72">备库上传重演未结束，需等待备库重演完成</td></tr><tr height="31"><td height="31" width="72"><span>-967</span></td><td width="72">ARCH_SEND_DELAY未配置</td></tr><tr height="31"><td height="31" width="72"><span>-968</span></td><td width="72">实例对应归档配置项未找到</td></tr><tr height="31"><td height="31" width="72"><span>-969</span></td><td width="72">普通节点不支持该操作</td></tr><tr height="31"><td height="31" width="72"><span>-970</span></td><td width="72">UNTIL TIME未配置</td></tr><tr height="31"><td height="31" width="72"><span>-971</span></td><td width="72">ARHC_SEND_DELAY未配置</td></tr><tr height="31"><td height="31" width="72"><span>-6025</span></td><td width="72">获取备库信息失败，请检查备库是否正常</td></tr><tr height="31"><td height="31" width="72"><span>-849</span></td><td width="72">解析dmtimer.ini中日历表达式无效</td></tr></tbody></table>

#### 10.2.8.4 DSC 集群控制器（DMCSS）

| **错误码** | **解释** |
| --- | --- |
| \-1075 | \[CSS\]: 没有找到指定组的信息 |
| \-1012 | 只有 CSS 控制节点能执行该操作 |
| \-1078 | \[CSS\]: CSS 监控处于关闭状态，不允许执行此命令 |
| \-1071 | \[CSS\]: 正在操作的组中没有活动 EP |
| \-1098 | \[CSS\]: 正在操作的组中没有非活动 EP |
| \-1059 | \[CSS\]: 正在操作组和预期状态不一致 |
| \-1073 | \[CSS\]: CSS 对需要手动拉起的组已经配置有自动重启，请等待 CSS 自动检测重启 |
| \-1090 | \[CSS\]: CSS 没有对需要执行拉起的组配置重启参数 |
| \-1074 | \[CSS\]: EP 已经处于 active 状态 |
| \-1099 | \[CSS\]: ASM 组没有活动节点或者活动节点不是 OPEN 状态，或者 ASM 组不是 OPEN 状态，不允许启动 DB 组 |
| \-1091 | \[CSS\]: 非法的 EP 序号 |
| \-1102 | 无效的组名 |