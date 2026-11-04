---
title: "DMDSC 配置文件"
book: "DM8 数据共享集群"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dsc-configuration-instructions.html
tags:
  - dameng
  - dm8
  - dsc
---

与 DMDSC 相关的配置文件包括：

下面分别介绍配置文件中各配置项的含义。

## 9.1 DMDCR\_CFG.INI

DMDCR\_CFG.INI 是格式化非镜像环境下 DCR DISK、VOTE DISK 和镜像环境下 DCRV 磁盘的配置文件。

配置信息包括三类：集群环境全局信息、集群组信息、以及组内节点信息。

集群环境全局信息为所有集群的公共信息，整个文件中只需要出现一次。例如:设置 DMCSS 集群、DMASM 集群和 DMDSC 集群三个集群的公共信息。

集群组信息用来设置一个集群中所有节点的公共信息，一个集群只需配置一个集群组信息。例如:设置 DMCSS 集群中两个节点 CSS0 和 CSS1 的公共信息。

组内节点信息，集群组中各节点的信息。例如：分别设置节点 CSS0 和 CSS1 的各自的节点信息。

使用 DMASMCMD 工具，可以根据 DMDCR\_CFG.INI 配置文件，格式化 DCR DISK 和 VOTE DISK。

表9.1 DMDCR\_CFG.INI配置项

<table><tbody><tr><td colspan="2"><b>集群环境全局信息</b></td></tr><tr><td>DCR_VTD_PATH</td><td>VOTE DISK路径</td></tr><tr><td>DCR_N_GRP</td><td>集群环境包括多少个组（即包括多少个集群），取值范围1~16。例如：配置了1个DMCSS集群、1个DMASM集群、1个DMDSC集群，则DCR_N_GRP=3。目前仅支持3个组</td></tr><tr><td>DCR_OGUID</td><td>消息标识，DMCSSM登录DMCSS消息校验用。取值范围：正整数</td></tr><tr><td colspan="2"><b>集群组信息</b></td></tr><tr><td>DCR_GRP_TYPE</td><td>组类型：CSS、ASM或DB。分别表示DMCSS集群、DMASM集群和DMDSC集群</td></tr><tr><td>DCR_GRP_NAME</td><td>组名，16字节，配置文件内不可重复</td></tr><tr><td>DCR_GRP_N_EP</td><td>组内节点个数N，最大8</td></tr><tr><td>DCR_GRP_EP_ARR</td><td>组内包含的节点序列号，{0,1,2,...N-1}<br>用户不能指定，仅用于从DCR磁盘export出来可见</td></tr><tr><td>DCR_GRP_N_ERR_EP</td><td>组内故障节点个数<br>用户不能指定，仅用于从DCR磁盘export出来可见</td></tr><tr><td>DCR_GRP_ERR_EP_ARR</td><td>组内故障节点序列号<br>用户不能指定，仅用于从DCR磁盘export出来可见</td></tr><tr><td>DCR_GRP_DSKCHK_CNT</td><td>磁盘心跳机制，容错时间，单位秒S，缺省60S，取值范围5~600</td></tr><tr><td colspan="2"><b>节点信息，某些属性可能只针对某一类型节点，比如SHM_KEY只针对ASM节点有效</b></td></tr><tr><td>DCR_EP_NAME</td><td>节点名，16字节，配置文件内不可重复。<br>DB的节点名必须和DM.INI里的INSTANCE_NAME保持一致，仅允许大小写不一致。<br>ASM的节点名必须和DMASVRMAL.INI里的MAL_INST_NAME一致，仅允许大小写不一致。<br>同一类型各节点的EP_NAME不能重复</td></tr><tr><td>DCR_EP_SEQNO</td><td>组内序号，CSS/ASM不能配置，自动分配<br>DB可以配置，0 ~ n_ep -1，组内不能重复，如不配置则自动分配</td></tr><tr><td>DCR_EP_HOST</td><td>节点IP(实例所在机器的IP地址)。<br>CSS中设置表示DMCSSM可以通过该IP连接CSS，可以不配置。<br>dmasmsvr允许通过IP/PORT远程访问，ASM必须配置</td></tr><tr><td>DCR_EP_PORT</td><td>节点TCP监听端口(CSS/ASM/DB有效，对应登录CSS/ASM/DB的端口号)，节点实例配置此参数，取值范围1024~65534；发起连接端的端口在1024~65535之间随机分配。<br>特别对DB来说，DB的DCR_EP_PORT与DM.INI中的PORT_NUM不一致时，DB端口以DM.INI中的PORT_NUM为准</td></tr><tr><td>DCR_EP_SHM_KEY</td><td>共享内存标识，数值类型(ASM有效，初始化共享内存的标识符)，应为大于0的4字节整数。同一机器上每个ASM节点对应的DCR_EP_SHM_KEY必须唯一，需要人为保证其唯一性</td></tr><tr><td>DCR_EP_SHM_SIZE</td><td>共享内存大小，单位MB，取值范围10~40000。共享内存大小与其能管理的磁盘大小的关系详见10.5 DMASM技术指标</td></tr><tr><td>DCR_EP_ASM_LOAD_PATH</td><td>ASM磁盘扫描路径，Linux下一般为/dev/raw，文件模拟情况，必须是全路径，不能是相对路径。<br>支持多路径配置，各路径以英文逗号','进行分隔，所有配置的路径都必须为有效路径，且暂不支持中文路径，例如：/dev/disk1,/dev/disk2,/dev/disk3。最多可以同时配置8个磁盘扫描路径，但配置的所有路径长度之和必须小于256，若超过该长度，只能减小磁盘扫描路径个数</td></tr></tbody></table>

**使用说明**

1. 在用 dmasmcmd 工具执行 init votedisk disk\_path from dcr\_cfg\_path 时，指定的 disk\_path 必须和 dcr\_cfg\_path 里面配置的 DCR\_VTD\_PATH 相同。
2. 如果配置 dmcssm，dmcssm 的 OGUID 必须和 DCR\_OGUID 保持一致。
3. DCR\_N\_GRP 必须和实际配置的组数目保持一致。
4. CSS 和 ASM 组的 DCR\_GRP\_N\_EP 要相等，DB 的 DCR\_GRP\_N\_EP 要小于等于 CSS/ASM 的 DCR\_GRP\_N\_EP。
5. ASM 节点的 DCR\_EP\_NAME 必须和 DMASM 系统使用的 DMASVRMAL.INI 配置文件里的 MAL\_INST\_NAME 保持一致，仅允许大小写不一致。
6. DB 节点的 DCR\_EP\_NAME 必须和数据库实例使用 DMMAL.INI 配置文件里的 MAL\_INST\_NAME、以及 DM.INI 配置文件里的 INSTANCE\_NAME 保持一致，仅允许大小写不一致。
7. 所有 DB 节点的 DCR\_EP\_NAME 都不能重复，DB 组内的 DCR\_EP\_SEQNO 不能重复。
8. DMDCR\_CFG.INI 配置文件中的所有路径均不支持中文路径。

**举例说明**

```
//集群环境全局信息
DCR_N_GRP           = 3
DCR_VTD_PATH        = /dev/raw/raw2
DCR_OGUID       = 63635

//DMCSS集群组的信息
[GRP]                //[GRP]表示新建一个Group
DCR_GRP_TYPE        = CSS
DCR_GRP_NAME        = CSS
DCR_GRP_N_EP        = 2
DCR_GRP_DSKCHK_CNT  = 60
//CSS0节点的信息
[CSS]                 //[]里的是组名，与DCR_GRP_NAME对应
DCR_EP_NAME         = CSS0
DCR_EP_HOST         = 10.0.2.101
DCR_EP_PORT         = 9341
//CSS1节点的信息
[CSS]                 //[]里的是组名，与DCR_GRP_NAME对应
DCR_EP_NAME         = CSS1
DCR_EP_HOST         = 10.0.2.102
DCR_EP_PORT         = 9343

//DMASM集群组的信息
[GRP]                //[GRP]表示新建一个Group
DCR_GRP_TYPE        = ASM
DCR_GRP_NAME        = ASM
DCR_GRP_N_EP        = 2
DCR_GRP_DSKCHK_CNT  = 60
//ASM0节点的信息
[ASM]                 //[]里的是组名，与DCR_GRP_NAME对应
DCR_EP_NAME         = ASM0
DCR_EP_SHM_KEY      = 93360
DCR_EP_SHM_SIZE     = 20
DCR_EP_HOST         = 10.0.2.101
DCR_EP_PORT         = 9349
DCR_EP_ASM_LOAD_PATH = /dev/raw
//ASM1节点的信息
[ASM]                 //[]里的是组名，与DCR_GRP_NAME对应
DCR_EP_NAME         = ASM1
DCR_EP_SHM_KEY      = 93361
DCR_EP_SHM_SIZE     = 20
DCR_EP_HOST         = 10.0.2.201
DCR_EP_PORT         = 9351
DCR_EP_ASM_LOAD_PATH = /dev/raw

//DMDSC集群组的信息
[GRP]               //[GRP]表示新建一个Group
DCR_GRP_TYPE        = DB
DCR_GRP_NAME        = DSC
DCR_GRP_N_EP        = 2
DCR_GRP_DSKCHK_CNT  = 60
//DSC01节点的信息
[DSC]                 //[]里的是组名，与DCR_GRP_NAME对应
DCR_EP_NAME        = DSC01
DCR_EP_SEQNO      = 0
DCR_EP_PORT          = 5236
//DSC02节点的信息
[DSC]                 //[]里的是组名，与DCR_GRP_NAME对应
DCR_EP_NAME     = DSC02
DCR_EP_SEQNO      = 1
DCR_EP_PORT          = 5237
```

## 9.2 DMDCR.INI

DMDCR.INI 是 DMCSS、DMASMSVR、DMASMTOOL 等工具的输入参数。记录了当前节点序列号以及 DCR 磁盘路径。

表9.2 DMDCR.INI配置项

| DMDCR\_PATH | 记录DCR磁盘路径 |
| --- | --- |
| DMDCR\_SEQNO | 记录当前节点序号(用来获取ASM登录信息) |
| DMDCR\_MAL\_PATH | 保存DMMAL.INI配置文件的路径，仅对DMASMSVR有效 |
| DMDCR\_ASM\_RESTART\_INTERVAL | DMCSS认定DMASM节点故障重启的时间间隔（取值范围0~86400s），单位S，DMCSS只负责和DMDCR\_SEQNO节点号相等的DMASM节点的故障重启，超过设置的时间后，如果DMASM节点的active标记仍然为FALSE，则DMCSS会执行自动拉起。   如果配置为0，则不会执行自动拉起操作，缺省为60s |
| DMDCR\_ASM\_STARTUP\_CMD | DMCSS认定DMASM节点故障后，执行自动拉起的命令串，命令串长度不应超过256，可以配置为服务方式或命令行方式启动，具体可参考表下方的DMDCR.INI使用说明 |
| DMDCR\_ASM\_TRACE\_LEVEL | 指定日志级别。1：TRACE级别；2：INFO级别；3：WARN级别；4：ERROR级别；5：FATAL级别。缺省为2。日志级别越低（参数值越小），输出的日志越详细。当设置日志级别为较低级别时，兼容输出级别大的日志，如WARN级别也可输出ERROR级别的日志 |
| DMDCR\_DB\_RESTART\_INTERVAL | DMCSS认定DMDSC节点故障重启的时间间隔（取值范围0~ 86400s），单位S，DMCSS只负责和DMDCR\_SEQNO节点号相等的DMDSC节点的故障重启，超过设置的时间后，如果DMDSC节点的active标记仍然为FALSE，则DMCSS会执行自动拉起。   如果配置为0，则不会执行自动拉起操作，缺省为60s |
| DMDCR\_DB\_STARTUP\_CMD | DMCSS认定DMDSC节点故障后，执行自动拉起的命令串，命令串长度不应超过256，可以配置为服务方式或命令行方式启动，具体可参考表下方的DMDCR.INI使用说明 |
| DMDCR\_AUTO\_OPEN\_CHECK | 指定时间内如果节点实例未启动，DMCSS会自动将节点踢出集群环境，取值范围30s~4294967294s，单位S。不配置此参数时表示不启用此功能，即缺省为不启用 |
| DMDCR\_MESSAGE\_CHECK | 是否对DMCSS通信消息启用通信体校验（只有当消息的发送端和接收端都配置为1才启用通信体校验）。0：不启用；1：启用。缺省为1 |
| DMDCR\_IPC\_CONTROL | 进程间互斥实现方式，0表示用全局信号量控制；1表示用全局互斥量控制；2表示用全局互斥量控制，并且有分片功能。缺省为2 |
| DMDCR\_LINK\_CHECK\_IP | 第三方确认机器的IP。可选参数，Linux专用。确认机器为DMDSC集群各节点均可访问到的、DMDSC集群环境之外的、一台独立机器，DMDCR\_LINK\_CHECK\_IP与内网通信网络位于同一网段。用于在DMDSC节点故障或意外断网时，各DMSERVER节点通过联通确认机器IP来检测网络是否畅通。DMCSS若由于断网而导致与确认机器IP联通失败，则DMDSC集群会强制HALT DMCSS节点。配置了DMDCR\_LINK\_CHECK\_IP之后，需要为DMSERVER、DMASMSVR（非DMASM镜像）和DMASMSVRM（DMASM镜像）、DMCSS赋予ping权限来完成联通功能。   使用ROOT权限执行以下语句分别进行赋权：   DMSERVER权限：   sudo setcap cap\_net\_raw,cap\_net\_admin=eip /opt/dmdbms/bin/dmserver   DMASMSVR权限：   sudo setcap cap\_net\_raw,cap\_net\_admin=eip /opt/dmdbms/bin/dmasmsvr   DMASMSVRM权限：   sudo setcap cap\_net\_raw,cap\_net\_admin=eip /opt/dmdbms/bin/dmasmsvrm   DMCSS权限：   sudo setcap cap\_net\_raw,cap\_net\_admin=eip /opt/dmdbms/bin/dmcss   其中，/opt/dmdbms/bin为dmserver、dmasmsvr、dmasmsvrm、dmcss所在目录。 如果DMDCR\_LINK\_CHECK\_IP配置成功，在DMSERVER、DMASMSVR、DMASMSVRM或DMCSS的事件日志中，会记录一条“comm\_self\_link\_check success”日志，否则记录一条“comm\_self\_link\_check create socket failed, ……” 日志 |
| DMDCR\_NEED\_PRE\_LOAD | 非镜像环境下，指定DMASMSVR启动时是否预加载文件EXTENT；镜像环境下，指定DMASMSVRM启动时是否预加载文件AU。0：否；1：是。预加载操作可以提升DMSERVER或DMASMSVRM运行时的性能，但是数据量非常大时，预加载操作比较耗时。缺省为0 |
| DMDCR\_AU\_PRE\_LOAD\_NUM | 非镜像环境下，指定DMASMSVR预加载的文件EXTENT个数；镜像环境下，指定DMASMSVRM预加载的文件AU个数。取值范围0~1024。若不指定该参数，则由DMASMAPI或DMASMAPIM根据读写文件大小来计算预加载的EXTENT或AU个数。该参数可以用于性能优化，一般情况下无需指定该参数 |
| DMDCR\_CSS\_PORT | 配置本节点CSS进程监听的端口号。默认为不配置，使用DCR磁盘配置的端口号；如果配置，则以当前配置为准，忽略DCR磁盘配置 |
| DMDCR\_ASM\_PORT | 配置本节点ASM进程监听的端口号。默认为不配置，使用DCR磁盘配置的端口号；如果配置，则以当前配置为准，忽略DCR磁盘配置 |
| DMDCR\_CHECK\_CSS\_ACTIVE | 指定是否监测本节点CSS进程活动状态。0：否；1：是。缺省为0。取值为1时，DMASMSVR和DMSERVER定期监测CSS进程活动状态，若CSS故障，则DMASMSVR和DMSERVER主动HALT |
| DMDCR\_CRASH\_CHECK\_OPT\_COUNT | 远程节点DMCSS/DMASMSVR/DMSERVER被判为故障的标准。   0：心跳信息在DCR\_GRP\_DSKCHK\_CNT时间内没有变化判定为节点故障，缺省为0；   N：表示DMCSS/DMASMSVR/DMSERVER的磁盘心跳确认次数都超过N次，并且网络联通超时N秒没有联通，才判定为节点故障。取值范围1~30 |
| DMDCR\_ASM\_MAX\_FILE\_OPEN | DMASMSVR进程内缓存ASM文件个数上限，达到上限会触发缓存淘汰。取值范围0~4294967294，缺省为4096 |

**使用说明**

1. DMASMSVR 和 DMSERVER 使用不同的 MAL 系统，需要配置两套 MAL 系统，配置文件 DMMAL.INI 需要分别生成，保存到不同的目录下，并且 DMMAL.INI 中的配置项不能重复、冲突。
2. DMDSC 集群环境下，只有当所有 OK 节点实例都启动时，整个集群环境才能启动。可能存在某些场景，部分 OK 节点无法正常启动，导致整个集群环境无法正常启动。指定参数 DMDCR\_AUTO\_OPEN\_CHECK 后，如果超过指定时间节点实例还未启动，DMCSS 自动将未启动节点踢出集群环境，变为 ERROR 节点，之后其他活动 OK 节点可以正常启动。

DMDSC 中至少一个 OK 节点启动后 DMCSS 才开始检查，所有 OK 节点都未启动情况下，DMCSS 不会主动踢出节点。

3. DMCSS 自动拉起故障 DMASMSVR 或 DMSERVER 实例。

故障认定间隔和启动命令串是配合使用的，DMASMSVR 和 DMSERVER 实例需要各自配置，如果没有配置启动命令串，故障间隔即使配置为大于 0 的值 DMCSS 也不会执行自动拉起操作，DMDCR\_ASM\_RESTART\_INTERVAL 和 DMDCR\_DB\_RESTART\_INTERVAL 默认的 60S 只有在配置有启动命令串时才会起作用。

DMDCR\_ASM\_STARTUP\_CMD 和 DMDCR\_DB\_STARTUP\_CMD 的配置方法相同，只是执行码名称和 ini 配置文件路径有区别，可以配置为服务名或命令行启动方式。

- DMASMSVR 实例启动命令举例如下：

1）linux 命令行方式启动（不能出现带有空格的路径）：

```
DMDCR_ASM_STARTUP_CMD = /opt/dmdbms/bin/dmasmsvr dcr_ini=/home/data/dmdcr.ini
```

2）linux 服务方式启动：

```
DMDCR_ASM_STARTUP_CMD = service dmasmserverd restart
```

3）Windows 命令行启动：

```
DMDCR_ASM_STARTUP_CMD = c:\dm\bin\dmasmsvr.exe  dcr_ini=d:\asmtest\dmdcr.ini
```

4）Windows 服务方式启动:

```
DMDCR_ASM_STARTUP_CMD = net start 注册服务名
```
- DMSERVER 实例启动命令如下：

1）linux 命令行方式启动（不能出现带有空格的路径）：

```
DMDCR_DB_STARTUP_CMD = /opt/dmdbms/bin/dmserver path=/home/data/dsc0_config/dm.ini dcr_ini=/home/data/dmdcr.ini
```

2）linux 服务方式启动：

```
DMDCR_DB_STARTUP_CMD = service DmServiceDSC01 restart
```

3）Windows 命令行启动：

```
DMDCR_DB_STARTUP_CMD = c:\dm\bin\dmserver.exe path=d:\asmtest\dsc0_config\dm.ini dcr_ini=d:\asmtest\dmdcr.ini
```

4）Windows 服务方式启动:

```
DMDCR_DB_STARTUP_CMD = net start 注册服务名
```
4. DMDCR\_LINK\_CHECK\_IP 使用场景

当 2 节点 DSC 集群节点间出现 MAL 网络异常时，如果两个节点实例都正常运行，DMCSS 的处理逻辑是主动 HALT 节点号大的 DSC1 节点，保留节点号小的 DSC0 节点。如果真实情况是 DSC0 和应用的网络断了，而 DSC1 和应用的网络是好的，那么 DMCSS 这种保留节点号小的逻辑就不合适。因此，须配置 DMDCR\_LINK\_CHECK\_IP 参数来解决上述问题。

DMDCR\_LINK\_CHECK\_IP 成功配置之后，当集群中出现节点间 MAL 网络异常时，节点还需要尝试联通一下 DMDCR\_LINK\_CHECK\_IP 配置的 IP（类似于 ping 功能），DMCSS 将联通结果共同作为处理网络异常的参考依据。例如：上述场景下，DSC0 和第三方确认 IP 无法联通，DSC1 和第三方确认 IP 可以联通，那么 DMCSS 综合判断之后主动 HALT 掉 DSC0 节点，保留了正常的 DSC1 节点。

如果没有配置 DMDCR\_LINK\_CHECK\_IP，或者配置错误，或者没有赋予进程权限，集群所有节点尝试联通 DMDCR\_LINK\_CHECK\_IP 时都会失败，那么 DMCSS 依然是保留节点号小的逻辑。

**举例说明**

```
DMDCR_PATH=/dev/raw/raw1
DMDCR_SEQNO=0
DMDCR_MAL_PATH=/home/data/dmasvrmal.ini

//故障认定间隔，以及启动命令中的执行码路径和INI路径需要根据实际情况调整
DMDCR_ASM_RESTART_INTERVAL = 60
DMDCR_ASM_STARTUP_CMD = /opt/dmdbms/bin/dmasmsvr dcr_ini=/home/data/dmdcr.ini

DMDCR_DB_RESTART_INTERVAL = 60
DMDCR_DB_STARTUP_CMD = /opt/dmdbms/bin/dmserver path=/home/data/dsc0_config/dm.ini dcr_ini=/home/data/dmdcr.ini
```

## 9.3 DMINIT.INI

DMINIT.INI 是 DMINIT 工具初始化数据库环境的配置文件。与初始化库使用普通文件系统不同，使用 DMASM 文件系统，必须使用 DMINIT 工具的 control 参数指定 DMINIT.INI 文件。DMINIT 工具的命令行参数都可以放在 DMINIT.INI 中，比如 db\_name、auto\_overwrite 等，DMINIT.INI 参数分为全局参数和节点参数。DMINIT 工具具体用法可以参考《DM8\_dminit 使用手册》，下面列出常用的一些参数。

表9.3 DMINIT.INI配置项

<table><tbody><tr><td colspan="2"><b>全局参数，对所有节点有效</b></td></tr><tr><td>SYSTEM_PATH</td><td>初始化数据库存放的路径</td></tr><tr><td>DB_NAME</td><td>初始化数据库名称</td></tr><tr><td>MAIN</td><td>MAIN表空间路径</td></tr><tr><td>MAIN_SIZE</td><td>MAIN表空间大小</td></tr><tr><td>SYSTEM</td><td>SYSTEM表空间路径</td></tr><tr><td>SYSTEM_SIZE</td><td>SYSTEM表空间大小</td></tr><tr><td>ROLL</td><td>ROLL表空间路径</td></tr><tr><td>ROLL_SIZE</td><td>ROLL表空间大小</td></tr><tr><td>CTL_PATH</td><td>DM.CTL控制文件路径</td></tr><tr><td>CTL_SIZE</td><td>DM.CTL控制文件大小</td></tr><tr><td>LOG_SIZE</td><td>日志文件大小</td></tr><tr><td>HUGE_PATH</td><td>MAIN表空间的HUGE数据文件路径</td></tr><tr><td>AUTO_OVERWRITE</td><td>文件存在时的处理方式</td></tr><tr><td>DCR_PATH</td><td>DCR磁盘路径</td></tr><tr><td>DCR_SEQNO</td><td>DCR序号</td></tr><tr><td>ASM_PORT</td><td>DMASM进程监听的端口号</td></tr><tr><td colspan="2"><b>节点参数，对具体节点有效</b></td></tr><tr><td>[XXX]</td><td>具体节点都是以[XXX]开始，节点实例名就是XXX</td></tr><tr><td>CONFIG_PATH</td><td>配置文件存放路径</td></tr><tr><td>PORT_NUM</td><td>节点服务器监听通讯端口号，服务器配置此参数，取值范围1024~65534，发起连接端的端口在1024~65535之间随机分配</td></tr><tr><td>MAL_HOST</td><td>节点MAL系统使用IP。<br>对于IPv6地址，若当前环境存在多块网卡，需要用%号指定具体有效的网卡序号或网卡名称；若只有一块网卡或者已配置默认网卡，则可以不指定序号或名称。例如：MAL_HOST = fe80::610e:9715:5ec6:4ea8%ens01，其中ens01为当前环境使用的网卡名称</td></tr><tr><td>MAL_PORT</td><td>MAL监听端口，用于数据守护、DSC、MPP等环境中各节点实例之间MAL链路配置，监听端端口配置此参数，取值范围1024~65534，发起连接端的端口在1024~65535之间随机分配</td></tr><tr><td>LOG_PATH</td><td>日志文件路径</td></tr></tbody></table>

**使用说明**

1. SYSTEM\_PATH 支持 ASM 文件系统，如果不指定 MAIN/SYSTEM/ROLL/CTL\_PATH/HUGE\_PATH，则数据文件、控制文件和 MAIN 表空间的 HUGE 数据文件目录都会默认生成在 SYSTEM\_PATH/db\_name 下面。
2. 在 DSC 集群环境里，除了 TEMP 表空间，所有其他表空间都只支持 ASM 文件路径，如果指定必须指定 SIZE。
3. 只有 DMINIT 工具使用 DMASM 文件系统，才会用到 DCR\_PATH 和 DCR\_SEQNO，并且不会写入其他配置文件。
4. CONFIG\_PATH 暂时只支持本地磁盘，不支持 ASM 文件系统。DSC 环境配置，各节点的 CONFIG\_PATH 要指定不同路径。
5. MAL\_HOST 和 MAL\_PORT 是为了自动创建 DMMAL.INI 文件使用，只有在初始化 DSC 环境时需要指定。
6. LOG\_PATH 可以不指定，默认会在 SYSTEM\_PATH 生成。如果指定，必须指定两个以上。
7. 必须指定实例名，也就是必须配置\[XXX\]。

**举例说明**

```
system_path= +DMDATA/data
db_name= dsc
main= +DMDATA/data/dsc/main.dbf
main_size= 128
roll = +DMDATA/data/dsc/roll.dbf
roll_size= 128
system = +DMDATA/data/dsc/system.dbf
system_size= 128
ctl_path = +DMDATA/data/dsc/dm.ctl
ctl_size = 8
log_size = 256
dcr_path = /dev/raw/raw1
dcr_seqno = 0
auto_overwrite=1
SYSDBA_PWD=DMdba_123
SYSAUDITOR_PWD=DMauditor_123

[dsc01]
config_path = /home/data/config1
port_num = 5236
mal_host = 10.0.2.101
mal_port = 9340
log_path = +DMDATA/log/log101.log
log_path = +DMDATA/log/log102.log
[dsc02]
config_path = /home/data/config2
port_num = 5237
mal_host = 10.0.2.102
mal_port = 9341
log_path = +DMDATA/log/log201.log
log_path = +DMDATA/log/log202.log
```

## 9.4 MAL 系统配置文件

MAL 配置文件包括 DMMAL.INI 和 DMASVRMAL.INI。使用同一套 MAL 系统的所有实例，MAL 系统配置文件须严格保持一致。

DMDSC 使用 MAL 配置文件的前提条件：

一 DMASMSVR 和 DMDSC 集群中的 DMSERVER 实例需要分别配置一套独立的 MAL 系统，两者配置的 MAL 环境不能冲突。

二 DMASMSVR 组成的集群环境使用一套 MAL 系统进行通讯，需要在 DMDCR.INI 配置文件中配置 DMDCR\_MAL\_PATH 参数，指定 MAL 配置文件路径。例如：DMDCR\_MAL\_PATH =/home/data/dmasvrmal.ini。

三 使用 MAL 系统的 DMSERVER 实例，需要将 DM.INI 配置项 MAL\_INI 设置为 1。同时 MAL 系统配置文件名称必须为 DMMAL.INI。

### 9.4.1 DMMAL.INI

表 9.4 DMMAL.INI 配置项

| **配置项** | **配置含义** |
| --- | --- |
| MAL\_CHECK\_INTERVAL | MAL 链路检测时间间隔，取值范围 0~1800，单位秒（s），缺省为 30s，配置为 0 表示不进行 MAL 链路检测 |
| MAL\_CONN\_FAIL\_INTERVAL | 判定实例之间 MAL 链路断开的时间，取值范围 2~1800，单位秒（s），缺省为 10s。 仅当 MAL\_CHECK\_INTERVAL 不为 0 时有效 |
| MAL\_CHECK\_TIMEOUT | 单个实例的 MAL 网络最大延迟时间，单位毫秒（ms），取值范围 0~65535，缺省为 0，表示不进行 MAL 网络延迟时间检测。需要和 MAL\_CHECK\_IP 配合使用。 仅当 MAL\_CHECK\_INTERVAL 不为 0 时有效 |
| MAL\_CHECK\_IP | 第三方确认机器的 IP，用于检测各个实例的 MAL 网络延迟时间。需要和 MAL\_CHECK\_TIMEOUT 配合使用。确认机器为 MAL 链路所有实例均可访问到的独立外网机器，MAL 链路实例包括 DMSERVER、DMASMSVR（非 DMASM 镜像）和 DMASMSVRM（DMASM 镜像）。 实例每隔 MAL\_CHECK\_INTERVAL 时间 ping 一次 MAL\_CHECK\_IP，若连接耗时超过 MAL\_CHECK\_TIMEOUT 指定时间，则该实例主动 HALT。 开启 MAL 网络延迟时间检测后，需要为 MAL 链路所有实例赋予 ping 权限，具体方法可以参考 DMDCR\_LINK\_CHECK\_IP 参数介绍 |
| MAL\_SEND\_THRESHOLD | 最大待发送邮件数，用于控制待发送邮件总数，防止发送邮件堆积。取值范围 1024~10000，缺省为 2048 |
| MAL\_LEAK\_CHECK | 是否打开 MAL 内存泄露检查。0：关闭；1：打开。缺省为 0 |
| MAL\_LOGIN\_TIMEOUT | MPP/DBLINK 等实例间登录时的超时检测间隔，取值范围 3~1800，单位 S，缺省为 15s |
| MAL\_BUF\_SIZE | 单个 MAL 缓存大小限制，以兆为单位。当此 MAL 的缓存邮件超过此大小，则会将邮件存储到文件中。取值范围 0~500000，缺省为 100 |
| MAL\_SYS\_BUF\_SIZE | MAL 系统总内存大小限制，单位 MB。取值范围 0~500000，缺省为 0，表示 MAL 系统无总内存限制 |
| MAL\_VPOOL\_SIZE | MAL 系统使用的内存初始化大小，单位 MB。取值范围 1~500000，缺省为 128，此值一般要设置的比 MAL\_BUF\_SIZE 大一些 |
| MAL\_COMPRESS\_LEVEL | MAL 消息压缩等级，取值范围 0~10。缺省为 0，不进行压缩；1~9 表示采用 zip 算法，从 1 到 9 表示压缩速度依次递减，压缩率依次递增；10 表示采用 snappy 算法，压缩速度高于 zip 算法，压缩率相对低 |
| MAL\_TEMP\_PATH | 指定临时文件的目录。当邮件使用的内存超过 mal\_buf\_size 或者 mal\_sys\_buf\_size 时，将新产生的邮件保存到临时文件中。如果缺省，则新产生的邮件保存到 temp.dbf 文件中 |
| MAL\_COMBIN\_BUF\_SIZE | 指定 MAL 消息合并发送的缓冲区大小，单位 KB。MAL 发送消息时进行合并，减少网络发送次数。取值范围 0~131072。0 表示不进行消息合并，为缺省值。最小缓冲区大小 128kB，当设置值大于 0 小于 128 时，自动调整为 128 |
| MAL\_MESSAGE\_CHECK | 是否对 MAL 通信消息启用消息体校验（只有当消息的发送端和接收端都配置为 1 才启用消息体校验）。0：不启用；1：启用。缺省为 1 |
| MAL\_MSG\_ENCRYPT | MAL 系统是否启用 SSL 通讯加密。0：不启用；1：启用。缺省为 0 |
| MAL\_USE\_RDMA | Linux 环境下，MAL 是否使用 RDMA 通讯方式。0：否，使用 TCP 方式；1：是，使用 RDMA 方式。当 MAL\_USE\_RDMA=1 时，MAL\_HOST 必须是 RDMA 网卡所绑定的 IP。使用 RDMA 之前需先安装好迈络思 ofed 驱动（RDMA 协议的基础库 libibverbs.so 和 librdmacm.so） |
| MAL\_RDMA\_MAGIC | MAL 链路通信方式标识，取值范围 0~65534，缺省为 0。相同 MAL\_RDMA\_MAGIC 的节点使用 RDMA 通信，否则使用 TCP 通信。若不配置 MAL\_RDMA\_MAGIC，缺省为 0，那么可以和 MAL\_RDMA\_MAGIC 为 0 的节点进行 RDMA 通信 |
| \[MAL\_NAME\] | MAL 名称，同一个配置文件中 MAL 名称需保持唯一性 |
| MAL\_INST\_NAME | 数据库实例名，与 DM.INI 的 INSTANCE\_NAME 配置项保持一致，MAL 系统中数据库实例名要保持唯一 |
| MAL\_HOST | MAL IP 地址，使用 MAL\_HOST+MAL\_PORT 创建 MAL 链路。   对于 IPv6 地址，若当前环境存在多块网卡，需要用 % 号指定具体有效的网卡序号或网卡名称；若只有一块网卡或者已配置默认网卡，则可以不指定序号或名称。例如：MAL\_HOST = fe80::610e:9715:5ec6:4ea8%ens01，其中 ens01 为当前环境使用的网卡名称 |
| MAL\_PORT | MAL 监听端口，用于数据守护、DSC、MPP 等环境中各节点实例之间 MAL 链路配置，监听端端口配置此参数，取值范围 1024~65534，发起连接端的端口在 1024~65535 之间随机分配 |
| MAL\_INST\_HOST | MAL\_INST\_NAME 实例对外服务 IP 地址 |
| MAL\_INST\_PORT | MAL\_INST\_NAME 实例服务器监听通讯端口号，服务器配置此参数，取值范围 1024~65534，发起连接端的端口在 1024~65535 之间随机分配 此参数的配置应与 DM.INI 中的 PORT\_NUM 保持一致 |
| MAL\_DW\_PORT | MAL\_INST\_NAME 实例守护进程的监听端口，其他守护进程或监视器使用 MAL\_HOST + MAL\_DW\_PORT 创建与该实例守护进程的 TCP 连接，监听端配置此参数，取值范围 1024~65534，发起连接端的端口在 1024~65535 之间随机分配。缺省为 0，表示不配置端口号，无法监听 |
| MAL\_INST\_DW\_PORT | 节点实例监听守护进程的端口，实例服务器配置此参数，取值范围 1024~65534，发起连接端的端口在 1024~65535 之间随机分配。缺省为 0，表示不配置端口号，无法监听 |

### 9.4.2 DMASVRMAL.INI

表 9.5 DMASVRMAL.INI 配置项

| **配置项** | **配置含义** |
| --- | --- |
| MAL\_CHECK\_INTERVAL | MAL 链路检测时间间隔，取值范围 0~1800，单位秒（s），缺省为 30s，配置为 0 表示不进行 MAL 链路检测 |
| MAL\_CONN\_FAIL\_INTERVAL | 判定实例之间 MAL 链路断开的时间，取值范围 2~1800，单位秒（s），缺省为 10s。 仅当 MAL\_CHECK\_INTERVAL 不为 0 时有效 |
| MAL\_CHECK\_TIMEOUT | 单个实例的 MAL 网络最大延迟时间，单位毫秒（ms），取值范围 0~65535，缺省为 0，表示不进行 MAL 网络延迟时间检测。需要和 MAL\_CHECK\_IP 配合使用。 仅当 MAL\_CHECK\_INTERVAL 不为 0 时有效 |
| MAL\_CHECK\_IP | 第三方确认机器的 IP，用于检测各个实例的 MAL 网络延迟时间。需要和 MAL\_CHECK\_TIMEOUT 配合使用。确认机器为 MAL 链路所有实例均可访问到的独立外网机器，MAL 链路实例包括 DMSERVER、DMASMSVR（非 DMASM 镜像）和 DMASMSVRM（DMASM 镜像）。 实例每隔 MAL\_CHECK\_INTERVAL 时间 ping 一次 MAL\_CHECK\_IP，若连接耗时超过 MAL\_CHECK\_TIMEOUT 指定时间，则该实例主动 HALT。 开启 MAL 网络延迟时间检测后，需要为 MAL 链路所有实例赋予 ping 权限，具体方法可以参考 DMDCR\_LINK\_CHECK\_IP 参数介绍 |
| MAL\_LOGIN\_TIMEOUT | MPP/DBLINK 等实例间登录时的超时检测间隔，取值范围 3~1800，单位 S，缺省为 15s |
| MAL\_BUF\_SIZE | 单个 MAL 缓存大小限制，以兆为单位。当此 MAL 的缓存邮件超过此大小，则会将邮件存储到文件中。取值范围 0~500000，缺省为 100 |
| MAL\_SYS\_BUF\_SIZE | MAL 系统总内存大小限制，单位 MB。取值范围 0~500000，缺省为 0，表示 MAL 系统无总内存限制 |
| MAL\_VPOOL\_SIZE | MAL 系统使用的内存初始化大小，单位 MB。取值范围 1~500000，缺省为 128，此值一般要设置的比 MAL\_BUF\_SIZE 大一些 |
| MAL\_COMPRESS\_LEVEL | MAL 消息压缩等级，取值范围 0~10。缺省为 0，不进行压缩；1~9 表示采用 zip 算法，从 1 到 9 表示压缩速度依次递减，压缩率依次递增；10 表示采用 snappy 算法，压缩速度高于 zip 算法，压缩率相对低 |
| MAL\_TEMP\_PATH | 指定临时文件的目录。当邮件使用的内存超过 mal\_buf\_size 或者 mal\_sys\_buf\_size 时，将新产生的邮件保存到临时文件中。如果缺省，则新产生的邮件保存到 temp.dbf 文件中 |
| MAL\_MESSAGE\_CHECK | 是否对 MAL 通信消息启用消息体校验（只有当消息的发送端和接收端都配置为 1 才启用消息体校验）。0：不启用；1：启用。缺省为 1 |
| \[MAL\_NAME\] | MAL 名称，同一个配置文件中 MAL 名称需保持唯一性 |
| MAL\_INST\_NAME | 数据库实例名，与 DM.INI 的 INSTANCE\_NAME 配置项保持一致，MAL 系统中数据库实例名要保持唯一 |
| MAL\_HOST | MAL IP 地址，使用 MAL\_HOST+MAL\_PORT 创建 MAL 链路。   对于 IPv6 地址，若当前环境存在多块网卡，需要用 % 号指定具体有效的网卡序号或网卡名称；若只有一块网卡或者已配置默认网卡，则可以不指定序号或名称。例如：MAL\_HOST = fe80::610e:9715:5ec6:4ea8%ens01，其中 ens01 为当前环境使用的网卡名称 |
| MAL\_PORT | MAL 监听端口，用于数据守护、DSC、MPP 等环境中各节点实例之间 MAL 链路配置，监听端端口配置此参数，取值范围 1024 ~~65534，发起连接端的端口在 1024~~ 65535 之间随机分配 |
| MAL\_INST\_HOST | MAL\_INST\_NAME 实例对外服务 IP 地址 |
| MAL\_INST\_PORT | MAL\_INST\_NAME 实例服务器监听通讯端口号，服务器配置此参数，取值范围 1024 ~~65534，发起连接端的端口在 1024~~ 65535 之间随机分配 此参数的配置应与 DMDCR\_CFG.INI 中的 PORT\_NUM 保持一致 |
| MAL\_LINK\_MAGIC | 用以区分不同网段。取值范围 0-65534。默认为 0。 |

## 9.5 DM.INI

DM.INI 是 DMSERVER 使用的配置文件，详细介绍可以参考《DM8 系统管理员手册》相关章节。

各 DMDSC 节点之间的部分 INI 参数必须保持一致，如果不一致，会导致后启动的节点启动失败，日志会记录失败原因。每个节点使用 SQL 语句或者系统函数修改本节点的 INI 时，DMDSC 会将新修改值同步到其它节点，始终保持 INI 参数值的一致性。

对于节点间必须保持一致的 INI 参数，用户使用 SQL 语句或者系统函数修改参数值时，建议指定修改 INI 文件中的参数值，若仅修改内存中的参数值，则当部分节点故障重启时，可能出现节点间参数不一致的情况。

须保持一致的 INI 参数是：BUFFER、BUFFER\_POOLS、BUFFER\_MODE、FAST\_POOL\_PAGES、FAST\_ROLL\_PAGES、KEEP、RECYCLE、RECYCLE\_POOLS、ROLLSEG、ROLLSEG\_POOLS、MULTI\_PAGE\_GET\_NUM、ENABLE\_INJECT\_HINT、ORDER\_BY\_NULLS\_FLAG、OPTIMIZER\_MODE、DIRECT\_IO、MAX\_SESSIOS、TRX\_VIEW\_MODE、FAST\_LOGIN、TS\_RESERVED\_EXTENTS、TS\_SAFE\_FREE\_EXTENTS、TS\_MAX\_ID、TS\_FIL\_MAX\_ID、RLOG\_APPEND\_LOGIC、ISOLATION\_LEVEL、LOCK\_DICT\_OPT、BACKSLASH\_ESCAPE、STR\_LIKE\_IGNORE\_MATCH\_END\_SPACE、MS\_PARSE\_PERMIT、COMPATIBLE\_MODE、JSON\_MODE、CASE\_COMPATIBLE\_MODE、COUNT\_64BIT、CALC\_AS\_DECIMAL、CMP\_AS\_DECIMAL、CAST\_VARCHAR\_MODE、PL\_SQLCODE\_COMPATIBLE、LEGACY\_SEQUENCE、DM6\_TODATE\_FMT、DROP\_CASCADE\_VIEW、ENABLE\_FREQROOTS、ENABLE\_OFFLINE\_TS、DSC\_N\_CTLS、DSC\_TRX\_VIEW\_SYNC、DSC\_REMOTE\_READ\_MODE、CHECK\_SVR\_VERSION、COMMIT\_WRITE、PARAM\_DOUBLE\_TO\_DEC、RLOG\_SYNC\_MODE、DSC\_NTP\_MAX\_DIFFTIME、DSC\_NTP\_POLICY、DSC\_REQUEST\_TIMEOUT、PAGE\_FLUSH\_CHECK、DSC\_SLOT\_WAIT\_TIMEOUT、BINDDATA\_COLTYPE、USE\_JSON\_DATATYPE、ENABLE\_RLS。

另外，下面几个参数需要按要求进行配置：

- INSTANCE\_NAME：DMSERVER 如果需要使用 DMASM 文件系统，INSTANCE\_NAME 必须和 DMDCR\_CFG.INI 里面配置的 DCR\_EP\_NAME 相同；
- MAL\_INI：必须为 1，可缺省。在 DMDSC 系统中，为了确保通信正常，MAL\_INI 缺省或为 0 的情况下，系统会将 MAL\_INI 强制设置为 1；
- DSC\_USE\_SBT： 是否使用辅助的平衡二叉树。取值 0 或 1。1：是，0：否。缺省为 1。DM 的检查点机制要求 BUFFER 更新链表保持有序性，所有被修改过的数据页，要根据其第一次修改的 LSN 值（FIRST\_MODIFIED\_LSN）从小到大有序排列。而 DMDSC 的缓存交换机制要求数据页在节点间传递，当一个更新页 P1 由普通节点 EP0 传递到节点 EP1 时，为了不破坏节点 EP1 更新链表 FIRST\_MODIFIED\_LSN 的有序性，需要扫描更新链，将 P1 加入到更新链中的合适位置。极端情况下，可能需要扫描整个更新链，才能找到 P1 的插入位置，在 BUFFER 比较大，更新链表比较长的情况下，这种扫描、定位代价十分昂贵，特别是在高并发情况下，会引发严重的并发冲突，影响并发性能。开启 DSC\_USE\_SBT 参数后，系统内部维护一个平衡二叉树，在将数据页加入更新链表时，根据这个平衡二叉树进行 log2N 次比较，就可以找到插入位置；
- DSC\_N\_POOLS：LBS/GBS 池数目。取值范围 2~1024，缺省为 19。与 BUFFER\_POOLS 类似，DSC\_N\_POOLS 将系统中的 LBS/GBS 根据页号进行分组，以降低 LBS/GBS 处理的并发冲突；
- CONFIG\_PATH：指定 DMSERVER 所读取的配置文件（DMMAL.INI、DMARCH.INI、DMTIMER.INI 等）的路径。不允许指定 ASM 目录。缺省使用 SYSTEM\_PATH 路径。如果 SYSTEM\_PATH 保存在 ASM 上，则直接报错；
- TRACE\_PATH：存放系统 trace 文件的路径。不允许指定 ASM 目录。默认的 TRACE\_PATH 是 SYSTEM\_PATH；如果 SYSTEM\_PATH 保存在 ASM 上，则../config\_path/trace 作为 TRACE\_PATH。

## 9.6 DMARCH.INI

DMARCH.INI 是开启本地归档或远程归档时使用的配置文件。不开启归档，可不用配置 DMARCH.INI。更多 DMARCH.INI 用法请参考《DM8 数据守护与读写分离集群 V4.0》。

## 9.7 DMCSSM.INI

DMCSSM.INI 是 DMCSSM 监视器的配置文件。具体请参考 [15.1.2 配置文件 DMCSSM.INI](dsc-monitor.md) 。