---
title: "数据守护搭建"
book: "DM8 数据守护与读写分离集群"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/data-guard-construction.html
tags:
  - dameng
  - dm8
  - data-watch
---

在搭建数据守护系统前，应注意数据守护系统中各实例使用的 DM 服务器版本应一致，同时还应注意各实例所在主机的操作系统位数、大小端模式、时区及时间设置都应一致，以及使用同一个用户启动 DM 服务器和守护进程 dmwatcher，以免系统在运行时出现意想不到的错误。

## 7.1 数据准备

配置数据守护 V4.0 之前，必须先通过备份还原方式同步各数据库的数据，确保各数据库的数据保持完全一致。主库可以是新初始化的数据库，也可以是正在生产、使用中的数据库。备库在备份还原前，需要先准备初始化一个新库。

不能使用分别初始化库或者直接拷贝数据文件的方法来直接配置数据库守护，原因如下：

1. 每个库都有一个永久魔数（permenant\_magic），一经生成，永远不会改变，主库传送日志时会判断这个值是否一样，确保是来自同一个数据守护环境中的库，否则传送不了日志。
2. 由于 dminit 初始化数据库时，会生成随机密钥用于加密，每次生成的密钥都不相同，备库无法解析采用主库密钥加密的数据。
3. 每个库都有一个数据库魔数（DB\_MAGIC），每经过一次还原、恢复操作，DB\_MAGIC 就会产生变化，需要通过这种方式来区分同一个数据守护环境中各个不同的库。

> **注意**
> 
> 如果需要使用Huge表，在初始化库时需要将建库参数HUGE\_WITH\_DELTA和RLOG\_GEN\_FOR\_HUGE都配置为1。  
> 对于新初始化的库，首次启动不允许使用Mount方式，需要先正常启动并正常退出，然后才允许Mount方式启动。  
> 准备数据时，如果主库是新初始化的库，先正常启动并正常退出，然后再使用备份还原方式准备备库数据。

如果是初始搭建环境，可以通过对主库脱机备份、对备库脱机还原的方式来准备数据，如果主库已经处于运行状态，则可以对主库进行联机备份、对备库脱机还原的方式来准备数据。

两种方式都需要服务器配置本地归档，本地归档配置方式如下：

1.配置 dm.ini，打开 ARCH\_INI 参数

```
ARCH_INI = 1 ##打开归档配置
```

2.配置 dmarch.ini

```
[ARCHIVE_LOCAL1]

ARCH_TYPE = LOCAL ##本地归档类型

ARCH_DEST = /dm/data/DAMENG/arch ##本地归档文件存放路径

ARCH_FILE_SIZE = 128 ##单位Mb，本地单个归档文件最大值

ARCH_SPACE_LIMIT = 0 ##单位Mb，0表示无限制，范围1024~2147483647M
```

关于备份还原更详细的说明可以参考《DM8 备份与还原》。

### 7.1.1 脱机备份、脱机还原方式

1. 正常关闭数据库
2. 进行脱机备份
```
./dmrman CTLSTMT="BACKUP DATABASE '/dm/data/DAMENG/dm.ini' FULL TO BACKUP_FILE1 BACKUPSET  '/dm/data/BACKUP_FILE_01'"
```
3. 拷贝备份文件到备库所在机器
4. 执行脱机数据库还原与恢复

数据库还原：

```
./dmrman CTLSTMT="RESTORE DATABASE '/dm/data/DAMENG/dm.ini' FROM BACKUPSET '/dm/data/BACKUP_FILE_01'"
```

因为脱机备份没有产生任何 REDO 日志，所以恢复这一步此处省略。

数据库更新：

```
./dmrman CTLSTMT="RECOVER DATABASE '/dm/data/DAMENG/dm.ini' UPDATE DB_MAGIC"
```

### 7.1.2 联机备份、脱机还原方式

1. 对主库进行联机备份操作
```
SQL> BACKUP DATABASE BACKUPSET '/dm/data/BACKUP_FILE_01';
```
2. 拷贝备份文件到备库所在机器
3. 执行脱机数据库还原与恢复
```
./dmrman CTLSTMT="RESTORE DATABASE '/dm/data/DAMENG/dm.ini' FROM BACKUPSET '/dm/data/BACKUP_FILE_01'"
./dmrman CTLSTMT="RECOVER DATABASE '/dm/data/DAMENG/dm.ini' FOR STANDBY FROM BACKUPSET '/dm/data/BACKUP_FILE_01'"
./dmrman CTLSTMT="RECOVER DATABASE '/dm/data/DAMENG/dm.ini' UPDATE DB_MAGIC"
```

> **注意**
> 
> 如果单节点系统已经上线，数据库服务不允许中断情况下，可以按照第“ [6.14备库重建](<#6.14 备库重建>) ”的步骤完成备库数据准备。  
> 备份文件中会记录原备份库的模式和OGUID信息，使用备份文件还原成功后，需要再根据实际配置情况修改数据库的模式和OGUID值。  
> 如果执行备份时，待备份的库是Normal模式，并且不能确定这个库一定作为主库使用，则对Normal模式的库必须使用脱机备份，不能使用联机备份方式，避免备份完成后，Normal模式的库LSN有增长，又将其修改为STANDBY模式，而使用备份集还原后的库修改为PRIMARY模式，备库数据比主库数据多，导致主备数据不一致的情况出现。因此，对执行联机备份的库，建议是已经修改为PRIMARY模式的库。

## 7.2 配置实时主备

配置实时主备，有以下几种配置方案，可以根据实际情况部署：

1. 只配置主库和最多 8 个实时备库。
2. 只配置主库和最多 8 个异步备库。
3. 配置主库、最多 8 个实时备库，和最多 8 个异步备库。

在实际应用中，如果数据库规模很大，并且对数据的实时性要求不是很严格，则可以配置多个异步备库用于分担统计报表等任务。

异步备库的配置可以参考 7.6 配置异步备库 ，由于实时主备、读写分离集群、MPP 主备、、DMDSC 主备都支持配置异步备库，因此单独在 7.6 配置异步备库 进行配置说明。

为了帮助大家更加直观地理解 DM 数据守护方案，下面举例说明如何配置一个完整的实时主备的过程，配置方案为常见的一个主库和一个实时备库。

> **注意**
> 
> 实际配置时，相关的端口配置和OGUID值建议不要和手册示例使用完全相同的值，避免多个用户在同一个环境下搭建不同的数据守护系统，出现消息混乱或者端口冲突等问题。

### 7.2.1 环境说明

准备三台机器 DW\_P、DW\_S1、DW\_M，DW\_P 和 DW\_S1 用来部署主备库，DW\_M 用来部署确认监视器。其中 DW\_P 和 DW\_S1 配置两块网卡，一块接入内部网络交换模块，一块接入到外部交换机，DW\_M 接入内部网络。

三台机器都事先安装了 DM，安装路径为'/dm'，执行程序保存在'/dm/bin'目录中，数据存放路径为'/dm/data'。

各主备库的实例名建议采用“组名\_守护环境\_序号”的方式命名，方便按组区分不同实例，注意总长度不能超过 16。本示例中组名为“GRP1”，配置为实时主备，主库命名为“GRP1\_RT\_01”，备库命名为“GRP1\_RT\_02”。

表7.1 配置环境说明

| **机器名** | **IP 地址** | **初始状态** | **操作系统** | **备注** |
| --- | --- | --- | --- | --- |
| DW\_P | 192.168.1.131 192.168.0.141 | 主库 GRP1\_RT\_01 | Linux rh6-141.test 2.6.32-220.el6.x86\_64##1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux | 192.168.1.131 外部服务 IP；   192.168.0.141 内部通信 IP |
| DW\_S1 | 192.168.1.132 192.168.0.142 | 备库 GRP1\_RT\_02 | Linux rh6-142.localdomain 2.6.32-220.el6.x86\_64##1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux | 192.168.1.132 外部服务 IP；   192.168.0.142 内部通信 IP |
| DW\_M | 192.168.0.73 | 确认监视器 | Linux rh6-73.localdomain 2.6.32-220.el6.x86\_64##1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux |  |

表7.2 端口规划

| **实例名** | **PORT\_NUM** | **MAL\_INST\_DW\_PORT** | **MAL\_HOST** | **MAL\_PORT** | **MAL\_DW\_PORT** |
| --- | --- | --- | --- | --- | --- |
| GRP1\_RT\_01 | 32141 | 33141 | 192.168.0.141 | 61141 | 52141 |
| GRP1\_RT\_02 | 32142 | 33142 | 192.168.0.142 | 61142 | 52142 |

### 7.2.2 数据准备

DW\_P 机器上初始化主库至目录/dm/data：

```
./dminit path=/dm/data SYSDBA_PWD=DMdba_123 SYSAUDITOR_PWD=DMauditor_123
```

DW\_S1 机器上初始化备库至目录/dm/data：

```
./dminit path=/dm/data SYSDBA_PWD=DMdba_123 SYSAUDITOR_PWD=DMauditor_123
```

然后按照 7.1 数据准备 中的方法准备备库数据。

### 7.2.3 配置主库 GRP1\_RT\_01

#### 7.2.3.1 配置 dm.ini

在 DW\_P 机器上配置主库的实例名为 GRP1\_RT\_01，dm.ini 参数修改如下：

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP1_RT_01

PORT_NUM = 32141 ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60 ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0 ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2 ##不允许备库OFFLINE表空间

MAL_INI = 1 ##打开MAL系统

ARCH_INI = 1 ##打开归档配置

RLOG_SEND_APPLY_MON = 64 ##统计最近64次的日志发送信息
```

#### 7.2.3.2 配置 dmmal.ini

配置 MAL 系统，各主备库的 dmmal.ini 配置必须完全一致，MAL\_HOST 使用内部网络 IP，MAL\_PORT 与 dm.ini 中 PORT\_NUM 使用不同的端口值，MAL\_DW\_PORT 是各实例对应的守护进程之间，以及守护进程和监视器之间的通信端口，配置如下：

```
MAL_CHECK_INTERVAL = 5                 ##MAL链路检测时间间隔

MAL_CONN_FAIL_INTERVAL = 5             ##判定MAL链路断开的时间

[MAL_INST1]

    MAL_INST_NAME = GRP1_RT_01         ##实例名，和dm.ini中的INSTANCE_NAME一致

    MAL_HOST = 192.168.0.141         ##MAL系统监听TCP连接的IP地址

    MAL_PORT = 61141                 ##MAL系统监听TCP连接的端口

    MAL_INST_HOST = 192.168.1.131    ##实例的对外服务IP地址

    MAL_INST_PORT = 32141             ##实例的对外服务端口，和dm.ini中的PORT_NUM一致

    MAL_DW_PORT = 52141             ##实例本地的守护进程监听TCP连接的端口

    MAL_INST_DW_PORT = 33141         ##实例监听守护进程TCP连接的端口

[MAL_INST2]

    MAL_INST_NAME = GRP1_RT_02

    MAL_HOST = 192.168.0.142

    MAL_PORT = 61142

    MAL_INST_HOST = 192.168.1.132

    MAL_INST_PORT = 32142

    MAL_DW_PORT = 52142

    MAL_INST_DW_PORT = 33142
```

#### 7.2.3.3 配置 dmarch.ini

修改 dmarch.ini，配置本地归档和实时归档。

除了本地归档外，其他归档配置项中的 ARCH\_DEST 表示实例是 PRIMARY 模式时，需要同步归档数据的目标实例名。

当前实例 GRP1\_RT\_01 是主库，需要向 GRP1\_RT\_02（实时备库）同步数据，因此实时归档的 ARCH\_DEST 配置为 GRP1\_RT\_02。

```
[ARCHIVE_REALTIME]

ARCH_TYPE = REALTIME                 ##实时归档类型

ARCH_DEST = GRP1_RT_02                 ##实时归档目标实例名

[ARCHIVE_LOCAL1]

ARCH_TYPE = LOCAL                     ##本地归档类型

ARCH_DEST = /dm/data/DAMENG/arch     ##本地归档文件存放路径

ARCH_FILE_SIZE = 128                 ##单位Mb，本地单个归档文件最大值

ARCH_SPACE_LIMIT = 0                ##单位Mb，0表示无限制，范围1024~2147483647M
```

#### 7.2.3.4 配置 dmwatcher.ini

修改 dmwatcher.ini 配置守护进程，配置为全局守护类型，使用自动切换模式。

```
[GRP1]

DW_TYPE = GLOBAL                     ##全局守护类型

DW_MODE = AUTO                         ##自动切换模式

DW_ERROR_TIME = 10                     ##远程守护进程故障认定时间

INST_RECOVER_TIME = 60                 ##主库守护进程启动恢复的间隔时间

INST_ERROR_TIME = 10                 ##本地实例故障认定时间

INST_OGUID = 453331                 ##守护系统唯一OGUID值

INST_INI = /dm/data/DAMENG/dm.ini     ##dm.ini配置文件路径

INST_AUTO_RESTART = 1                 ##打开实例的自动启动功能

INST_STARTUP_CMD = /dm/bin/dmserver    ##命令行方式启动

RLOG_SEND_THRESHOLD = 0             ##指定主库发送日志到备库的时间阈值，默认关闭

RLOG_APPLY_THRESHOLD = 0             ##指定备库重演日志的时间阈值，默认关闭
```

#### 7.2.3.5 启动主库

以 Mount 方式启动主库

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

> **注意**
> 
> 一定要以Mount方式启动数据库实例，否则系统启动时会重构回滚表空间，生成Redo日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动Open数据库。

#### 7.2.3.6 设置 OGUID

启动命令行工具 DIsql，登录主库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(453331);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.2.3.7 修改数据库模式

启动命令行工具 DIsql，登录主库修改数据库为 PRIMARY 模式

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>ALTER DATABASE PRIMARY;
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.2.4 配置备库 GRP1\_RT\_02

#### 7.2.4.1 配置 dm.ini

在 DW\_S1 机器上配置备库的实例名为 GRP1\_RT\_02，dm.ini 参数修改如下：

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP1_RT_02

PORT_NUM = 32142                 ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60        ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0             ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2             ##不允许备库OFFLINE表空间

MAL_INI = 1                     ##打开MAL系统

ARCH_INI = 1                    ##打开归档配置

RLOG_SEND_APPLY_MON = 64        ##统计最近64次的日志重演信息
```

#### 7.2.4.2 配置 dmmal.ini

配置 MAL 系统，各主备库的 dmmal.ini 配置必须完全一致，MAL\_HOST 使用内部网络 IP，MAL\_PORT 与 dm.ini 中 PORT\_NUM 使用不同的端口值，MAL\_DW\_PORT 是各实例对应的守护进程之间，以及守护进程和监视器之间的通信端口，配置如下：

```
MAL_CHECK_INTERVAL = 5                 ##MAL链路检测时间间隔

MAL_CONN_FAIL_INTERVAL = 5             ##判定MAL链路断开的时间

[MAL_INST1]

    MAL_INST_NAME = GRP1_RT_01         ##实例名，和dm.ini中的INSTANCE_NAME一致

    MAL_HOST = 192.168.0.141         ##MAL系统监听TCP连接的IP地址

    MAL_PORT = 61141                 ##MAL系统监听TCP连接的端口

    MAL_INST_HOST = 192.168.1.131     ##实例的对外服务IP地址

    MAL_INST_PORT = 32141             ##实例的对外服务端口，和dm.ini中的PORT_NUM一致

    MAL_DW_PORT = 52141             ##实例对应的守护进程监听TCP连接的端口

    MAL_INST_DW_PORT = 33141         ##实例监听守护进程TCP连接的端口

[MAL_INST2]

    MAL_INST_NAME = GRP1_RT_02

    MAL_HOST = 192.168.0.142

    MAL_PORT = 61142

    MAL_INST_HOST = 192.168.1.132

    MAL_INST_PORT = 32142

    MAL_DW_PORT = 52142

    MAL_INST_DW_PORT = 33142
```

#### 7.2.4.3 配置 dmarch.ini

修改 dmarch.ini，配置本地归档和实时归档。

除了本地归档外，其他归档配置项中的 ARCH\_DEST 表示实例是 PRIMARY 模式时，需要同步归档数据的目标实例名。

当前实例 GRP1\_RT\_02 是备库，守护系统配置完成后，可能在各种故障处理中，GRP1\_RT\_02 切换为新的主库，正常情况下，GRP1\_RT\_01 会切换为新的备库，需要向 GRP1\_RT\_01 同步数据，因此实时归档的 ARCH\_DEST 配置为 GRP1\_RT\_01。

```
[ARCHIVE_REALTIME]

    ARCH_TYPE = REALTIME                 ##实时归档类型

    ARCH_DEST = GRP1_RT_01                 ##实时归档目标实例名

[ARCHIVE_LOCAL1]

    ARCH_TYPE = LOCAL                     ##本地归档类型

    ARCH_DEST = /dm/data/DAMENG/arch    ##本地归档文件路径

    ARCH_FILE_SIZE = 128                 ##单位Mb，本地单个归档文件最大值

    ARCH_SPACE_LIMIT = 0                 ##单位Mb，0表示无限制，范围1024~2147483647M
```

#### 7.2.4.4 配置 dmwatcher.ini

修改 dmwatcher.ini 配置守护进程，配置为全局守护类型，使用自动切换模式。

```
[GRP1]

    DW_TYPE = GLOBAL                 ##全局守护类型

    DW_MODE = AUTO                     ##自动切换模式

    DW_ERROR_TIME = 10                 ##远程守护进程故障认定时间

    INST_RECOVER_TIME = 60             ##主库守护进程启动恢复的间隔时间

    INST_ERROR_TIME = 10            ##本地实例故障认定时间

    INST_OGUID = 453331             ##守护系统唯一OGUID值

    INST_INI = /dm/data/DAMENG/dm.ini##dm.ini配置文件路径

    INST_AUTO_RESTART = 1             ##打开实例的自动启动功能

    INST_STARTUP_CMD = /dm/bin/dmserver ##命令行方式启动

    RLOG_APPLY_THRESHOLD = 0         ##指定备库重演日志的时间阈值，默认关闭
```

#### 7.2.4.5 启动备库

以 Mount 方式启动备库

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

> **注意**
> 
> 一定要以Mount方式启动数据库实例，否则系统启动时会重构回滚表空间，生成Redo日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动Open数据库。

#### 7.2.4.6 设置 OGUID

启动命令行工具 DIsql，登录备库设置 OGUID 值为 453331

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(453331);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.2.4.7 修改数据库模式

启动命令行工具 DIsql，登录备库修改数据库为 STANDBY 模式。

如果当前数据库不是 Normal 模式，需要先修改 dm.ini 中 ALTER\_MODE\_STATUS 值为 1，允许修改数据库模式，修改 STANDBY 模式成功后再改回为 0。如果是 Normal 模式，请忽略下面的第 1 步和第 3 步。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);     //第1步
SQL>alter database standby;                         //第2步
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);     //第3步
```

### 7.2.5 配置监视器

由于主库和实时备库的守护进程配置为自动切换模式，因此这里必须配置确认监视器。和普通监视器相比，确认监视器除了相同的命令支持外，在主库发生故障时，能够自动通知实时备库接管为新的主库，具有自动故障处理的功能。

配置确认监视器时可以选择配置单实例监视器或配置多实例监视器，下面将分别介绍配置单实例监视器以及多实例监视器时 dmmonitor.ini 配置文件中的配置信息。

#### 7.2.5.1 配置单实例监视器

修改 dmmonitor.ini 配置确认监视器，其中 MON\_DW\_IP 中的 IP 和 PORT 和 dmmal.ini 中的 MAL\_HOST 和 MAL\_DW\_PORT 配置项保持一致。

```
MON_DW_CONFIRM = 1             ##确认监视器模式

MON_LOG_PATH = /dm/data/log ##监视器日志文件存放路径

MON_LOG_INTERVAL = 60         ##每隔60s定时记录系统信息到日志文件

MON_LOG_FILE_SIZE = 32         ##每个日志文件最大32M

MON_LOG_SPACE_LIMIT = 0     ##不限定日志文件总占用空间

[GRP1]

    MON_INST_OGUID = 453331 ##组GRP1的唯一OGUID值

##以下配置为监视器到组GRP1的守护进程的连接信息，以“IP:PORT”的形式配置

##IP对应dmmal.ini中的MAL_HOST，PORT对应dmmal.ini中的MAL_DW_PORT

    MON_DW_IP = 192.168.0.141:52141

    MON_DW_IP = 192.168.0.142:52142
```

#### 7.2.5.2 配置多实例监视器

为每个实例配置一个 dmmonitor.ini。众多 dmmonitor.ini 中，除 MON\_ID 和 MON\_NAME 参数不同以外，其他参数应完全一致。

使用配置文件启动多实例监视器实例之前，需要先初始化联机日志文件。初始化联机日志文件的具体操作请查看 [4.2.2.2.2 初始化联机日志文件](data-watch-monitor.md) 。

以其中一个实例的 dmmonitor.ini 为例进行介绍。各实例的 MON\_ID 应与某一个实例配置项中的 MON\_INST\_ID 相同，各实例的 MON\_NAME 与对应的监视器实例名相同。dmmonitor.ini 配置文件中的内容如下：

```
MON_LOG_PATH            = /dm/data/log
MON_LOG_INTERVAL          = 60
MON_LOG_FILE_SIZE          = 32
MON_LOG_SPACE_LIMIT        = 0
MON_DW_CONFIRM           = 1
MON_INST_NUM            = 3         #实例总个数
MON_HB_INTERVAL           = 60         #通信心跳校验间隔
MON_BRO_INTERVAL          = 100        #raft协议中实例通信心跳间隔
MON_VOTE_INTERVAL          = 100        #raft协议中基础投票间隔
MON_ID                   = 1          #当前监视器在监视器系统中的ID
MON_MID                   = 45614       #当前监视器系统的唯一标识
MON_NAME                = MON1  #监视器名

[GRP1]
MON_INST_OGUID      = 453331
MON_DW_IP              = 192.168.0.141:52141
MON_DW_IP              = 192.168.0.142:52142

[MON1] #监视器实例信息
MON_HOST                  = 192.168.0.143         #MON1监视器所在IP 
MON_PORT                  = 8339                     #MON1监视器监听端口
MON_INST_ID                = 1                     #监视器实例在监视器系统中的ID
MON_VOTE_PRIORITY        = 3                        #监视器实例成为LEADER的优先级

[MON2]
MON_HOST                  = 192.168.0.144         #MON2监视器所在IP 
MON_PORT                  = 8340                     #MON2监视器监听端口
MON_INST_ID                = 2                     #监视器实例在监视器系统中的ID
MON_VOTE_PRIORITY        = 2                        #监视器实例成为LEADER的优先级

[MON3]
MON_HOST                  = 192.168.0.145         #MON3监视器所在IP 
MON_PORT                  = 8341                     #MON3监视器监听端口
MON_INST_ID                = 3                     #监视器实例在监视器系统中的ID
MON_VOTE_PRIORITY        = 1                        #监视器实例成为LEADER的优先级
```

### 7.2.6 启动守护进程

启动各个主备库上的守护进程：

```
./dmwatcher /dm/data/DAMENG/dmwatcher.ini
```

守护进程启动后，进入 Startup 状态，此时实例都处于 Mount 状态。守护进程开始广播自身和其监控实例的状态信息，结合自身信息和远程守护进程的广播信息，守护进程将本地实例 Open，并切换为 Open 状态。

### 7.2.7 启动监视器

启动监视器命令：

```
./dmmonitor /dm/data/dmmonitor.ini
```

多实例确认监视器系统中，需逐个单独启动各节点上的监视器（启动后，多实例监视器暂不支持动态修改配置，具体说明请查看 [4.2.2.2.3 启动多实例监视器](data-watch-monitor.md) ）。

监视器提供一系列命令，支持当前守护系统状态查看以及故障处理，可输入 help 命令，查看各种命令使用说明，结合实际情况选择使用。

至此一主一备的实时数据守护系统搭建完毕，在搭建步骤和各项配置都正确的情况下，在监视器上执行 show 命令，可以监控到所有实例都处于 Open 状态，所有守护进程也都处于 Open 状态，即为正常运行状态。

## 7.3 配置读写分离集群

配置读写分离集群，有以下几种配置方案，可以根据实际情况部署：

1. 只配置主库和最多 8 个即时备库。
2. 只配置主库和最多 8 个实时备库。
3. 只配置主库和最多 8 个异步备库。
4. 配置主库、最多 8 个即时备库和最多 8 个异步备库。
5. 配置主库、最多 8 个实时备库和最多 8 个异步备库。

在实际应用中，如果数据库规模很大，并且对数据的实时性要求不是很严格，则可以配置多个异步备库用于分担统计报表等任务。

异步备库的配置可以参考 7.6 配置异步备库 ，由于实时主备、读写分离集群、MPP 主备、DMDSC 主备都支持配置异步备库，因此单独在 7.6 配置异步备库 进行配置说明。

为了帮助大家更加直观的理解 DM 数据守护方案，下面举例说明如何配置一个完整的读写分离集群的过程，配置方案为一个主库和两个即时备库。

> **注意**
> 
> 实际配置时，相关的端口配置和OGUID值建议不要和手册示例使用完全相同的值，避免多个用户在同一个环境下搭建不同的数据守护系统，出现消息混乱或者端口冲突等问题。

### 7.3.1 环境说明

准备四台机器 DW\_P、DW\_S1、DW\_S2、DW\_M，DW\_P、DW\_S1 和 DW\_S2 用来部署主备库，DW\_M 用来部署确认监视器。其中 DW\_P、DW\_S1 和 DW\_S2 配置两块网卡，一块接入内部网络交换模块，一块接入到外部交换机，DW\_M 接入内部网络。

四台机器事先都安装了 DM，安装路径为'/dm'，执行程序保存在'/dm/bin'目录中，数据存放路径为'/dm/data'。

各主备库的实例名建议采用“组名\_守护环境\_序号”的方式命名，方便按组区分不同实例，注意总长度不能超过 16。本示例中组名为“GRP1”，配置为读写分离集群，主库命名为“GRP1\_RWW\_01”，备库分别命名为“GRP1\_RWW\_02”和“GRP1\_RWW\_03”。

表7.3 配置环境说明

| **机器名** | **IP 地址** | **初始状态** | **操作系统** | **备注** |
| --- | --- | --- | --- | --- |
| DW\_P | 192.168.1.131 192.168.0.141 | 主库 GRP1\_RWW\_01 | Linux rh6-141.test 2.6.32-220.el6.x86\_64##1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux | 192.168.1.131 外部服务 IP；   192.168.0.141 内部通信 IP |
| DW\_S1 | 192.168.1.132 192.168.0.142 | 备库 GRP1\_RWW\_02 | Linux rh6-142.localdomain 2.6.32-220.el6.x86\_64##1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux | 192.168.1.132 外部服务 IP；   192.168.0.142 内部通信 IP |
| DW\_S2 | 192.168.1.133 192.168.0.143 | 备库 GRP1\_RWW\_03 | Linux rh6-143.localdomain 2.6.32-220.el6.x86\_64##1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux | 192.168.1.133 外部服务 IP；   192.168.0.143 内部通信 IP |
| DW\_M | 192.168.0.73 | 确认监视器 | Linux rh6-73.localdomain 2.6.32-220.el6.x86\_64##1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux |  |

表7.4 端口规划

| **实例名** | **PORT\_NUM** | **MAL\_INST\_DW\_PORT** | **MAL\_HOST** | **MAL\_PORT** | **MAL\_DW\_PORT** |
| --- | --- | --- | --- | --- | --- |
| GRP1\_RWW\_01 | 32141 | 33141 | 192.168.0.141 | 61141 | 52141 |
| GRP1\_RWW\_02 | 32142 | 33142 | 192.168.0.142 | 61142 | 52142 |
| GRP1\_RWW\_03 | 32143 | 33143 | 192.168.0.143 | 61143 | 52143 |

### 7.3.2 数据准备

DW\_P 机器上初始化库至目录/dm/data：

```
/dminit path=/dm/data SYSDBA_PWD=DMdba_123 SYSAUDITOR_PWD=DMauditor_123
```

然后按照 7.1 数据准备 中的方法分别准备备数据库数据。

### 7.3.3 配置主库 GRP1\_RWW\_01

#### 7.3.3.1 配置 dm.ini

在 DW\_P 机器上配置主库的实例名为 GRP1\_RWW\_01，dm.ini 参数修改如下：

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP1_RWW_01

PORT_NUM = 32141                 ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60         ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0             ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2             ##不允许备库OFFLINE表空间

MAL_INI = 1                     ##打开MAL系统

ARCH_INI = 1                     ##打开归档配置

RLOG_SEND_APPLY_MON = 64        ##统计最近64次的日志发送信息
```

#### 7.3.3.2 配置 dmmal.ini

配置 MAL 系统，各主备库的 dmmal.ini 配置必须完全一致，MAL\_HOST 使用内部网络 IP，MAL\_PORT 与 dm.ini 中 PORT\_NUM 使用不同的端口值，MAL\_DW\_PORT 是各实例对应的守护进程之间，以及守护进程和监视器之间的通信端口，配置如下：

```
MAL_CHECK_INTERVAL = 5             ##MAL链路检测时间间隔

MAL_CONN_FAIL_INTERVAL = 5         ##判定MAL链路断开的时间

[MAL_INST1]

    MAL_INST_NAME = GRP1_RWW_01 ##实例名，和dm.ini中的INSTANCE_NAME一致

    MAL_HOST = 192.168.0.141     ##MAL系统监听TCP连接的IP地址

    MAL_PORT = 61141             ##MAL系统监听TCP连接的端口

    MAL_INST_HOST = 192.168.1.131 ##实例的对外服务IP地址

    MAL_INST_PORT = 32141         ##实例的对外服务端口，和dm.ini中的PORT_NUM一致

    MAL_DW_PORT = 52141         ##实例对应的守护进程监听TCP连接的端口

    MAL_INST_DW_PORT = 33141     ##实例监听守护进程TCP连接的端口

[MAL_INST2]

    MAL_INST_NAME = GRP1_RWW_02

    MAL_HOST = 192.168.0.142

    MAL_PORT = 61142

    MAL_INST_HOST = 192.168.1.132

    MAL_INST_PORT = 32142

    MAL_DW_PORT = 52142

    MAL_INST_DW_PORT = 33142

[MAL_INST3]

    MAL_INST_NAME = GRP1_RWW_03

    MAL_HOST = 192.168.0.143

    MAL_PORT = 61143

    MAL_INST_HOST = 192.168.1.133

    MAL_INST_PORT = 32143

    MAL_DW_PORT = 52143

    MAL_INST_DW_PORT = 33143
```

#### 7.3.3.3 配置 dmarch.ini

修改 dmarch.ini，配置本地归档和即时归档。

除了本地归档外，其他归档配置项中的 ARCH\_DEST 表示实例是 PRIMARY 模式时，需要同步归档数据的目标实例名。

当前实例 GRP1\_RWW\_01 是主库，需要向即时备库 GRP1\_RWW\_02/GRP1\_RWW\_03 同步数据，因此即时归档的 ARCH\_DEST 分别配置为 GRP1\_RWW\_02 和 GRP1\_RWW\_03。

```
[ARCHIVE_TIMELY1]

    ARCH_TYPE = TIMELY                    ##即时归档类型

    ARCH_DEST = GRP1_RWW_02             ##即时归档目标实例名

[ARCHIVE_TIMELY2]

    ARCH_TYPE = TIMELY                     ##即时归档类型

    ARCH_DEST = GRP1_RWW_03             ##即时归档目标实例名

[ARCHIVE_LOCAL1]

    ARCH_TYPE = LOCAL                     ##本地归档类型

    ARCH_DEST = /dm/data/DAMENG/arch     ##本地归档文件存放路径

    ARCH_FILE_SIZE = 128                 ##单位Mb，本地单个归档文件最大值

    ARCH_SPACE_LIMIT = 0                 ##单位Mb，0表示无限制，范围1024~2147483647M
```

#### 7.3.3.4 配置 dmwatcher.ini

修改 dmwatcher.ini 配置守护进程，配置为全局守护类型，使用自动切换模式。

```
[GRP1]

    DW_TYPE = GLOBAL                     ##全局守护类型

    DW_MODE = AUTO                        ##自动切换模式

    DW_ERROR_TIME = 10                     ##远程守护进程故障认定时间

    INST_RECOVER_TIME = 60                 ##主库守护进程启动恢复的间隔时间

    INST_ERROR_TIME = 10                 ##本地实例故障认定时间

    INST_OGUID = 453332                    ##守护系统唯一OGUID值

    INST_INI = /dm/data/DAMENG/dm.ini     ##dm.ini配置文件路径

    INST_AUTO_RESTART = 1                 ##打开实例的自动启动功能

    INST_STARTUP_CMD = /dm/bin/dmserver ##命令行方式启动

    RLOG_SEND_THRESHOLD = 0             ##指定主库发送日志到备库的时间阈值，默认关闭

    RLOG_APPLY_THRESHOLD = 0             ##指定备库重演日志的时间阈值，默认关闭
```

#### 7.3.3.5 启动主库

以 Mount 方式启动主库

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

> **注意**
> 
> 一定要以Mount方式启动数据库实例，否则系统启动时会重构回滚表空间，生成Redo日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动Open数据库。

#### 7.3.3.6 设置 OGUID

启动命令行工具 DIsql，登录主库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(453332);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.3.3.7 修改数据库模式

启动命令行工具 DIsql，登录主库修改数据库为 PRIMARY 模式

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>ALTER DATABASE PRIMARY;
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.3.4 配置备库 GRP1\_RWW\_02

#### 7.3.4.1 配置 dm.ini

在 DW\_S1 机器上配置备库的实例名为 GRP1\_RWW\_02，dm.ini 参数修改如下：

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP1_RWW_02

PORT_NUM = 32142             ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60     ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0         ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2         ##不允许备库OFFLINE表空间

MAL_INI = 1                 ##打开MAL系统

ARCH_INI = 1                 ##打开归档配置

RLOG_SEND_APPLY_MON = 64     ##统计最近64次的日志重演信息
```

#### 7.3.4.2 配置 dmmal.ini

配置 MAL 系统，各主备库的 dmmal.ini 配置必须完全一致，MAL\_HOST 使用内部网络 IP，MAL\_PORT 与 dm.ini 中 PORT\_NUM 使用不同的端口值，MAL\_DW\_PORT 是各实例对应的守护进程之间，以及守护进程和监视器之间的通信端口，配置如下：

```
MAL_CHECK_INTERVAL = 5             ##MAL链路检测时间间隔

MAL_CONN_FAIL_INTERVAL = 5         ##判定MAL链路断开的时间

[MAL_INST1]

    MAL_INST_NAME = GRP1_RWW_01 ##实例名，和dm.ini中的INSTANCE_NAME一致

    MAL_HOST = 192.168.0.141     ##MAL系统监听TCP连接的IP地址

    MAL_PORT = 61141             ##MAL系统监听TCP连接的端口

    MAL_INST_HOST = 192.168.1.131 ##实例的对外服务IP地址

    MAL_INST_PORT = 32141         ##实例的对外服务端口，和dm.ini中的PORT_NUM一致

    MAL_DW_PORT = 52141         ##实例对应的守护进程监听TCP连接的端口

      MAL_INST_DW_PORT = 33141     ##实例监听守护进程TCP连接的端口

[MAL_INST2]

    MAL_INST_NAME = GRP1_RWW_02

    MAL_HOST = 192.168.0.142

    MAL_PORT = 61142

    MAL_INST_HOST = 192.168.1.132

    MAL_INST_PORT = 32142

    MAL_DW_PORT = 52142

    MAL_INST_DW_PORT = 33142

[MAL_INST3]

    MAL_INST_NAME = GRP1_RWW_03

    MAL_HOST = 192.168.0.143

    MAL_PORT = 61143

    MAL_INST_HOST = 192.168.1.133

    MAL_INST_PORT = 32143

    MAL_DW_PORT = 52143

    MAL_INST_DW_PORT = 33143
```

#### 7.3.4.3 配置 dmarch.ini

修改 dmarch.ini，配置本地归档和即时归档。

除了本地归档外，其他归档配置项中的 ARCH\_DEST 表示实例是 PRIMARY 模式时，需要同步归档数据的目标实例名。

当前实例 GRP1\_RWW\_02 是备库，守护系统配置完成后，可能在各种故障处理中，GRP1\_RWW\_02 切换为新的主库，正常情况下，GRP1\_RWW\_01 会切换为新的备库，需要向 GRP1\_RWW\_01 和 GRP1\_RWW\_03 同步数据，因此即时归档的 ARCH\_DEST 分别配置为 GRP1\_RWW\_01 和 GRP1\_RWW\_03。

```
[ARCHIVE_TIMELY1]

    ARCH_TYPE = TIMELY                 ##即时归档类型

    ARCH_DEST = GRP1_RWW_01         ##即时归档目标实例名

[ARCHIVE_TIMELY2]

    ARCH_TYPE = TIMELY                 ##即时归档类型

    ARCH_DEST = GRP1_RWW_03         ##即时归档目标实例名

[ARCHIVE_LOCAL1]

    ARCH_TYPE = LOCAL               ##本地归档类型

    ARCH_DEST = /dm/data/DAMENG/arch ##本地归档文件存放路径

    ARCH_FILE_SIZE = 128             ##单位Mb，本地单个归档文件最大值

    ARCH_SPACE_LIMIT = 0             ##单位Mb，0表示无限制，范围1024~2147483647M
```

#### 7.3.4.4 配置 dmwatcher.ini

修改 dmwatcher.ini 配置守护进程，配置为全局守护类型，使用自动切换模式。

```
[GRP1]

    DW_TYPE =GLOBAL                     ##全局守护类型

    DW_MODE = AUTO                         ##自动切换模式

    DW_ERROR_TIME = 10                     ##远程守护进程故障认定时间

    INST_RECOVER_TIME = 60                 ##主库守护进程启动恢复的间隔时间

    INST_ERROR_TIME = 10                 ##本地实例故障认定时间

    INST_OGUID = 453332                 ##守护系统唯一OGUID值

    INST_INI = /dm/data/DAMENG/dm.ini     ##dm.ini配置文件路径

    INST_AUTO_RESTART = 1                 ##打开实例的自动启动功能

    INST_STARTUP_CMD = /dm/bin/dmserver ##命令行方式启动

    RLOG_SEND_THRESHOLD = 0             ##指定主库发送日志到备库的时间阈值，默认关闭

    RLOG_APPLY_THRESHOLD = 0             ##指定备库重演日志的时间阈值，默认关闭
```

#### 7.3.4.5 启动备库

以 Mount 方式启动备库。

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

> **注意**
> 
> 一定要以Mount方式启动数据库实例，否则系统启动时会重构回滚表空间，生成Redo日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动Open数据库。

#### 7.3.4.6 设置 OGUID

启动命令行工具 DIsql，登录备库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(453332);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.3.4.7 修改数据库模式

启动命令行工具 DIsql，登录备库修改数据库为 STANDBY 模式。

如果当前数据库不是 Normal 模式，需要先修改 dm.ini 中 ALTER\_MODE\_STATUS 值为 1，允许修改数据库模式，修改 STANDBY 模式成功后再改回为 0。如果是 Normal 模式，请忽略下面的第 1 步和第 3 步。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);     //第1步
SQL>alter database standby;                           //第2步
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);     //第3步
```

### 7.3.5 配置备库 GRP1\_RWW\_03

#### 7.3.5.1 配置 dm.ini

在 DW\_S2 机器上配置备库的实例名为 GRP1\_RWW\_03，dm.ini 参数修改如下：

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP1_RWW_03

PORT_NUM = 32143                 ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60         ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0             ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2             ##不允许备库OFFLINE表空间

MAL_INI = 1                     ##打开MAL系统

ARCH_INI = 1                     ##打开归档配置

RLOG_SEND_APPLY_MON = 64         ##统计最近64次的日志重演信息
```

#### 7.3.5.2 配置 dmmal.ini

配置 MAL 系统，各主备库的 dmmal.ini 配置必须完全一致，MAL\_HOST 使用内部网络 IP，MAL\_PORT 与 dm.ini 中 PORT\_NUM 使用不同的端口值，MAL\_DW\_PORT 是各实例对应的守护进程之间，以及守护进程和监视器之间的通信端口，配置如下：

```
MAL_CHECK_INTERVAL = 5                    ##MAL链路检测时间间隔

MAL_CONN_FAIL_INTERVAL = 5                 ##判定MAL链路断开的时间

[MAL_INST1]

    MAL_INST_NAME = GRP1_RWW_01         ##实例名，和dm.ini中的INSTANCE_NAME一致

    MAL_HOST = 192.168.0.141             ##MAL系统监听TCP连接的IP地址

    MAL_PORT = 61141                     ##MAL系统监听TCP连接的端口

    MAL_INST_HOST = 192.168.1.131         ##实例的对外服务IP地址

    MAL_INST_PORT = 32141                 ##实例的对外服务端口，和dm.ini中的PORT_NUM一致

    MAL_DW_PORT = 52141                 ##实例对应的守护进程监听TCP连接的端口

    MAL_INST_DW_PORT = 33141             ##实例监听守护进程TCP连接的端口

[MAL_INST2]

    MAL_INST_NAME = GRP1_RWW_02

    MAL_HOST = 192.168.0.142

    MAL_PORT = 61142

    MAL_INST_HOST = 192.168.1.132

    MAL_INST_PORT = 32142

    MAL_DW_PORT = 52142

    MAL_INST_DW_PORT = 33142

[MAL_INST3]

    MAL_INST_NAME = GRP1_RWW_03

    MAL_HOST = 192.168.0.143

    MAL_PORT = 61143

    MAL_INST_HOST = 192.168.1.133

    MAL_INST_PORT = 32143

    MAL_DW_PORT = 52143

    MAL_INST_DW_PORT = 33143
```

#### 7.3.5.3 配置 dmarch.ini

修改 dmarch.ini，配置本地归档和即时归档。

除了本地归档外，其他归档配置项中的 ARCH\_DEST 表示实例是 PRIMARY 模式时，需要同步归档数据的目标实例名。

当前实例 GRP1\_RWW\_03 是备库，守护系统配置完成后，可能在各种故障处理中，GRP1\_RWW\_03 切换为新的主库，正常情况下，GRP1\_RWW\_01 会切换为新的备库，需要向 GRP1\_RWW\_01 和 GRP1\_RWW\_02 同步数据，因此即时归档的 ARCH\_DEST 分别配置为 GRP1\_RWW\_01 和 GRP1\_RWW\_02。

```
[ARCHIVE_TIMELY1]

    ARCH_TYPE = TIMELY                     ##即时归档类型

    ARCH_DEST = GRP1_RWW_01             ##即时归档目标实例名

[ARCHIVE_TIMELY2]

    ARCH_TYPE = TIMELY                     ##即时归档类型

    ARCH_DEST = GRP1_RWW_02             ##即时归档目标实例名

[ARCHIVE_LOCAL1]

    ARCH_TYPE = LOCAL                     ##本地归档类型

    ARCH_DEST = /dm/data/DAMENG/arch     ##本地归档文件存放路径

    ARCH_FILE_SIZE = 128                 ##单位Mb，本地单个归档文件最大值

    ARCH_SPACE_LIMIT = 0                 ##单位Mb，0表示无限制，范围1024~2147483647M
```

#### 7.3.5.4 配置 dmwatcher.ini

修改 dmwatcher.ini 配置守护进程，配置为全局守护类型，使用自动切换模式。

```
[GRP1]

    DW_TYPE = GLOBAL                     ##全局守护类型

    DW_MODE = AUTO                         ##自动切换模式

    DW_ERROR_TIME = 10                     ##远程守护进程故障认定时间

    INST_RECOVER_TIME = 60                 ##主库守护进程启动恢复的间隔时间

    INST_ERROR_TIME = 10                 ##本地实例故障认定时间

    INST_OGUID = 453332                 ##守护系统唯一OGUID值

    INST_INI = /dm/data/DAMENG/dm.ini     ##dm.ini配置文件路径

    INST_AUTO_RESTART = 1                 ##打开实例的自动启动功能

    INST_STARTUP_CMD = /dm/bin/dmserver ##命令行方式启动

    RLOG_SEND_THRESHOLD = 0              ##指定主库发送日志到备库的时间阈值，默认关闭

    RLOG_APPLY_THRESHOLD = 0             ##指定备库重演日志的时间阈值，默认关闭
```

#### 7.3.5.5 启动备库

以 Mount 方式启动备库

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

> **注意**
> 
> 一定要以Mount方式启动数据库实例，否则系统启动时会重构回滚表空间，生成Redo日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动Open数据库。

#### 7.3.5.6 设置 OGUID

启动命令行工具 DIsql，登录备库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(453332);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.3.5.7 修改数据库模式

启动命令行工具 DIsql，登录备库修改数据库为 STANDBY 模式

如果当前数据库不是 Normal 模式，需要先修改 dm.ini 中 ALTER\_MODE\_STATUS 值为 1，允许修改数据库模式，修改 STANDBY 模式成功后再改回为 0。如果是 Normal 模式，请忽略下面的第 1 步和第 3 步。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);     //第1步
SQL>alter database standby;                         //第2步
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);    //第3步
```

### 7.3.6 配置监视器

由于主库和实时备库的守护进程配置为自动切换模式，因此这里必须配置确认监视器。和普通监视器相比，确认监视器除了相同的命令支持外，在主库发生故障时，能够自动通知实时备库接管为新的主库，具有自动故障处理的功能。

配置确认监视器时可以选择配置单实例监视器或配置多实例监视器，下面将分别介绍配置单实例监视器以及多实例监视器时 dmmonitor.ini 配置文件中的配置信息。

#### 7.3.6.1 配置单实例监视器

修改 dmmonitor.ini 配置确认监视器，其中 MON\_DW\_IP 中的 IP 和 PORT 和 dmmal.ini 中的 MAL\_HOST 和 MAL\_DW\_PORT 配置项保持一致。

```
MON_DW_Confirm = 1                         ##确认监视器模式

MON_LOG_PATH = /dm/data/log             ##监视器日志文件存放路径

MON_LOG_INTERVAL = 60                     ##每隔60s定时记录系统信息到日志文件

MON_LOG_FILE_SIZE = 32                     ##每个日志文件最大32M

MON_LOG_SPACE_LIMIT = 0                 ##不限定日志文件总占用空间

[GRP1]

    MON_INST_OGUID = 453332             ##组GRP1的唯一OGUID值

    ##以下配置为监视器到组GRP1的守护进程的连接信息，以“IP:PORT”的形式配置

    ##IP对应dmmal.ini中的MAL_HOST，PORT对应dmmal.ini中的MAL_DW_PORT

    MON_DW_IP = 192.168.0.141:52141

    MON_DW_IP = 192.168.0.142:52142

    MON_DW_IP = 192.168.0.143:52143
```

#### 7.3.6.2 配置多实例监视器

为每个实例配置一个 dmmonitor.ini。众多 dmmonitor.ini 中，除 MON\_ID 和 MON\_NAME 参数不同以外，其他参数应完全一致。

使用配置文件启动多实例监视器实例之前，需要先初始化联机日志文件。初始化联机日志文件的具体操作请查看 [4.2.2.2.2 初始化联机日志文件](data-watch-monitor.md) 。

以其中一个实例的 dmmonitor.ini 为例进行介绍。各实例的 MON\_ID 应与某一个实例配置项中的 MON\_INST\_ID 相同，各实例的 MON\_NAME 与对应的监视器实例名相同。dmmonitor.ini 配置文件中的内容如下：

```
MON_LOG_PATH            = /dm/data/log
MON_LOG_INTERVAL          = 60
MON_LOG_FILE_SIZE          = 32
MON_LOG_SPACE_LIMIT        = 0
MON_DW_CONFIRM           = 1
MON_INST_NUM            = 3         #实例总个数
MON_HB_INTERVAL           = 60         #通信心跳校验间隔
MON_BRO_INTERVAL          = 100        #raft协议中实例通信心跳间隔
MON_VOTE_INTERVAL          = 100        #raft协议中基础投票间隔
MON_ID                   = 1          #当前监视器在监视器系统中的ID
MON_MID                   = 45614       #当前监视器系统的唯一标识
MON_NAME                = MON1  #监视器名

[GRP1]
MON_INST_OGUID           = 453332
MON_DW_IP                  = 192.168.0.141:52141
MON_DW_IP                  = 192.168.0.142:52142
MON_DW_IP                  = 192.168.0.143:52143
 
[MON1] #监视器实例信息
MON_HOST                  = 192.168.0.144         #MON1监视器所在IP 
MON_PORT                  = 8339                     #MON1监视器监听端口
MON_INST_ID                = 1                     #监视器实例在监视器系统中的ID
[MON2]
MON_HOST                  = 192.168.0.145         #MON2监视器所在IP 
MON_PORT                  = 8340                     #MON2监视器监听端口
MON_INST_ID                = 2                     #监视器实例在监视器系统中的ID 
[MON3]
MON_HOST                  = 192.168.0.146         #MON3监视器所在IP 
MON_PORT                  = 8341                     #MON3监视器监听端口
MON_INST_ID                = 3                     #监视器实例在监视器系统中的ID
```

### 7.3.7 启动守护进程

启动各个主备库上的守护进程：

```
./dmwatcher /dm/data/DAMENG/dmwatcher.ini
```

守护进程启动后，进入 Startup 状态，此时实例都处于 Mount 状态。守护进程开始广播自身和其监控实例的状态信息，结合自身信息和远程守护进程的广播信息，守护进程将本地实例 Open，并切换为 Open 状态。

### 7.3.8 启动监视器

启动监视器命令：

```
./dmmonitor /dm/data/dmmonitor.ini
```

多实例确认监视器系统中，需逐个单独启动各节点上的监视器（启动后，多实例监视器暂不支持动态修改配置，具体说明请查看 [4.2.2.2.3 启动多实例监视器](data-watch-monitor.md) ）。

监视器提供一系列命令，支持当前守护系统状态查看以及故障处理，可输入 help 命令，查看各种命令使用说明，结合实际情况选择使用。

至此读写分离集群搭建完毕，在搭建步骤和各项配置都正确的情况下，在监视器上执行 show 命令，可以监控到所有实例都处于 Open 状态，所有守护进程也都处于 Open 状态，即为正常运行状态。

### 7.3.9 接口说明

DM 多种客户端接口都支持读写分离集群连接设置，以下说明客户端连接服务器时如何设置读写分离属性，详细可参考《DM8 程序员手册》。

#### 7.3.9.1 JDBC 接口

JDBC 连接串中可设置以下连接属性：

- rwSeparate 是否使用读写分离系统，缺省为 0；取值（0 不使用，1 使用）。
- rwPercent 分发到主库的事务占主备库总事务的百分比，取值范围 0~100，缺省值 25。
```
<DRIVER>dm.jdbc.driver.DmDriver</DRIVER>

<URL>jdbc:dm://192.168.0.206:5236?rwSeparate=1&rwPercent=10</URL>
```

#### 7.3.9.2 Node.js 接口

Node.js 连接串中可设置以下连接属性：

- rwSeparate 是否使用读写分离系统，缺省为 false，取值范围（false：不使用，true：使用）。
- rwPercent 分发到主库的事务占主备库总事务的百分比，取值范围 0~100，缺省值 25。
```
db.createPool({
    connectString: "dm://SYSDBA:DMdba_123@192.168.0.206:5236?rwSeparate=true&rwPercent=10",
    poolMin: 1,
    poolMax: 3,
    poolAlias: "DM5236"
}).then(function(pool) {
    do_something_with_pool();
}) .catch(function(err) {
    console.log(err);
})
```

#### 7.3.9.3 Go 接口

Go 连接串中可设置以下连接属性：

- rwSeparate 是否使用读写分离系统，缺省为 false，取值范围（false：不使用，true：使用）。
- rwPercent 分发到主库的事务占主备库总事务的百分比，取值范围 0~100，缺省值 25。
```
db, err := sql.Open("dm", "dm://SYSDBA:DMdba_123@192.168.0.206:5236?rwSeparate=true&rwPercent=10")
```

#### 7.3.9.4 DPI 接口

DPI 接口的连接句柄上可设置读写分离属性：

- DSQL\_ATTR\_RWSEPARATE：读写分离（可读写）
- DSQL\_ATTR\_RWSEPARATE\_PERCENT：读写分离比例（可读写）

属性设置举例：

```
dhenv env;

dhcon con;

dpi_alloc_env(&env);

dpi_alloc_con(env, &con);

dpi_set_con_attr(con, DSQL_ATTR_RWSEPARATE, (dpointer) DSQL_RWSEPARATE_ON, 0);

dpi_set_con_attr(con, DSQL_ATTR_RWSEPARATE_PERCENT, (dpointer)25, 0);
```

DIsql 工具可以直接设置读写分离的属性：

```
>disql /nolog

SQL> login

服务名:

用户名:

密码:

端口号:

SSL路径:

SSL密码:

UKEY名称:

UKEY PIN码:

MPP类型:

是否读写分离(y/n):y

读写分离百分比(0-100):25
```

#### 7.3.9.5 ODBC 接口

ODBC 接口中读写分离相关的连接关键字为：

- RW\_SEPARATE：是否配置读写分离：TRUE，FALSE
- RW\_SEPARATE\_PERCENT：读写分离的比例：0~100

连接串举例说明：

```
"DSN=DM8;DRIVER=DM ODBC
DRIVER;UID=SYSDBA;PWD=DMdba_123;TCP_PORT=5236;RW_SEPARATE=TRUE;RW_SEPARATE_PERCENT=25";
```

#### 7.3.9.6 Provider 接口

DM.NET Provider 接口主要实现了 DmConnection，DmConnection 对象表示一个 DM 数据库打开的连接。其支持的读写分离属性包括：

- RW\_Separate：是否读写分离，有效值为 true 或者 false；
- RW\_Percent：表示分发到主库的事务占主备库总事务的百分比，有效值范围：0~100，默认值为 25。

连接串举例：

```
static DmConnection cnn = new DmConnection();

cnn.ConnectionString = "Server=localhost; User Id=SYSDBA; PWD=DMdba_123; RW_Separate=true; RW_Percent=25";
```

#### 7.3.9.7 DCI 接口

DCI 接口支持会话上的读写分离属性设置：

- OCI\_ATTR\_RW\_SEPARATE 是否读写分离，有效值为 1 或者 0，缺省为 0；
- OCI\_ATTR\_RW\_SEPARATE\_PERCENT 表示分发到主库的事务占主备库总事务的百分比，取值范围：0~100，缺省值为 25。

例如，利用接口编程进行举例说明。

```
OCIEnv* envhp;

OCISession* authp;

OCIError* errhp;

OCIInitialize(OCI_DEFAULT, NULL, NULL, NULL, NULL);

OCIEnvInit(&envhp, OCI_DEFAULT,0, 0);

OCIHandleAlloc(envhp, (dvoid**)&authp, OCI_HTYPE_SESSION, 0, 0);

OCIAttrSet(authp,OCI_HTYPE_SESSION,(void*)OCI_RW_SEPARATE_ON,(ub4)sizeof(ub4),OCI_ATTR_RW_SEPARATE,errhp);

OCIAttrSet(authp,OCI_HTYPE_SESSION,(void*)25,(ub4)sizeof(ub4),OCI_ATTR_RW_SEPARATE_PERCENT,errhp);
```

#### 7.3.9.8 dmPython 接口

dmPython 接口支持以下两个读写分离的连接属性：

- rwseparate 是否启用读写分离方式，取值为 TRUE 或 FALSE，缺省为 FALSE；
- rwseparate\_percent 设置读写分离比例(%)，缺省为 25。
	例如，利用接口编程进行举例说明。
```
import dmPython
conn = dmPython.connect(rwseparate=True, rwseparate_percent=25)
```

## 7.4 配置 MPP 主备

为了提高 MPP 系统可靠性，克服由于单节点故障导致整个系统不能继续正常工作，DM 在普通的 MPP 系统基础上，引入主备守护机制，将 MPP 节点作为主库节点，增加备库作为备份节点，必要时可切换为主库代替故障节点工作，提高系统的可靠性和可用性。

### 7.4.1 环境说明

本例配置 2 个 MPP 节点，每个节点作为主库，与其备库组成一个守护组，因此需要配置两个守护组，取名分别为 GRP1、GRP2，主库名为 GRP1\_MPP\_EP01/GRP2\_MPP\_EP02，对应的备库实例名分别为 GRP1\_MPP\_EP11/GRP2\_MPP\_EP22。

准备 3 台机器 A、B、C，A 和 B 用来交叉部署实例，C 用来部署监视器。其中 A 和 B 配置两块网卡，一块接入内部网络交换模块，一块接入到外部交换机，C 接入内部网络。

机器事先都安装了 DM，安装路径为'/dm'，执行程序保存在'/dm/bin'目录中，数据存放路径为'/dm/data/EP01','/dm/data/EP02'。

> **注意**
> 
> 实际配置时，相关的端口配置和OGUID值建议不要和手册示例使用完全相同的值，避免多个用户在同一个环境下搭建不同的数据守护系统，出现消息混乱或者端口冲突等问题。

表7.5 配置环境说明

| **机器名** | **IP 地址** | **初始状态** | **操作系统** |
| --- | --- | --- | --- |
| A | 192.168.1.131 192.168.0.141 | 主库 GRP1\_MPP\_EP01 备库 GRP2\_MPP\_EP22 | Linux rh6-2.6.32-220.el6.x86\_64 |
| B | 192.168.1.132 192.168.0.142 | 主库 GRP2\_MPP\_EP02 备库 GRP1\_MPP\_EP11 | Linux rh6-2.6.32-220.el6.x86\_64 |
| C | 192.168.0.144 | 监视器 | Linux rh6-2.6.32-220.el6.x86\_64 |

表7.6 端口规划—主库

| **实例名** | **PORT\_NUM** | **MAL\_INST\_DW\_PORT** | **MAL\_HOST** | **MAL\_PORT** | **MAL\_DW\_PORT** | **MPP 实例序号** |
| --- | --- | --- | --- | --- | --- | --- |
| GRP1\_MPP\_EP01 | 5236 | 5243 | 192.168.0.141 | 5337 | 5253 | 0 |
| GRP2\_MPP\_EP02 | 5236 | 5243 | 192.168.0.142 | 5337 | 5253 | 1 |

表7.7 端口规划—备库

| **实例名** | **PORT\_NUM** | **MAL\_INST\_DW\_PORT** | **MAL\_HOST** | **MAL\_PORT** | **MAL\_DW\_PORT** | **对应主库** |
| --- | --- | --- | --- | --- | --- | --- |
| GRP1\_MPP\_EP11 | 5237 | 5244 | 192.168.0.142 | 5338 | 5254 | GRP1\_MPP\_EP01 |
| GRP2\_MPP\_EP22 | 5237 | 5244 | 192.168.0.141 | 5338 | 5254 | GRP2\_MPP\_EP02 |

表7.8 守护进程规划

| **组名** | **实例名** | **所在机器** |
| --- | --- | --- |
| GRP1 | GRP1\_MPP\_EP01 | 192.168.0.141 |
|  | GRP1\_MPP\_EP11 | 192.168.0.142 |
| GRP2 | GRP2\_MPP\_EP02 | 192.168.0.142 |
|  | GRP2\_MPP\_EP22 | 192.168.0.141 |

### 7.4.2 数据准备

A 机器上初始化库至目录/dm/data/EP01：

```
./dminit path=/dm/data/EP01 SYSDBA_PWD=DMdba_123 SYSAUDITOR_PWD=DMauditor_123
```

B 机器上初始化库至目录/dm/data/EP02：

```
./dminit path=/dm/data/EP02 SYSDBA_PWD=DMdba_123 SYSAUDITOR_PWD=DMauditor_123
```

即完成两个主数据库的初始化，然后按照 7.1 数据准备 中的方法分别同步两个备数据库。

本例中采取机器交叉的方式配置两个备数据库，分别对应存放的目录为：

```
B机器的/dm/data/EP11
A机器的/dm/data/EP22
```

### 7.4.3 配置主库 GRP1\_MPP\_EP01

#### 7.4.3.1 配置 dm.ini

在 A 机器上配置主库的实例名为 GRP1\_MPP\_EP01，dm.ini 参数修改如下：

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP1_MPP_EP01

PORT_NUM = 5236 ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60 ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0 ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2 ##不允许备库OFFLINE表空间

MAL_INI = 1 ##打开MAL系统

ARCH_INI = 1 ##打开归档配置

MPP_INI = 1 ##启用MPP配置

RLOG_SEND_APPLY_MON = 64 ##统计最近64次的日志发送信息
```

#### 7.4.3.2 配置 dmmal.ini

配置 MAL 系统，各主备库的 dmmal.ini 配置必须完全一致，MAL\_HOST 使用内部网络 IP，MAL\_PORT 与 dm.ini 中 PORT\_NUM 使用不同的端口值，MAL\_DW\_PORT 是各实例对应的守护进程之间，以及守护进程和监视器之间的通信端口，配置如下：

```
MAL_CHECK_INTERVAL = 5 ##MAL链路检测时间间隔

MAL_CONN_FAIL_INTERVAL = 5 ##判定MAL链路断开的时间

[MAL_INST1]

    MAL_INST_NAME = GRP1_MPP_EP01 ##实例名，和dm.ini中的INSTANCE_NAME一致

    MAL_HOST = 192.168.0.141 ##MAL系统监听TCP连接的IP地址

    MAL_PORT = 5337 ##MAL系统监听TCP连接的端口

    MAL_INST_HOST = 192.168.1.131 ##实例的对外服务IP地址

    MAL_INST_PORT = 5236 ##实例的对外服务端口，和dm.ini中的PORT_NUM一致

    MAL_DW_PORT = 5253 ##实例对应的守护进程监听TCP连接的端口

    MAL_INST_DW_PORT = 5243 ##实例监听守护进程TCP连接的端口

[MAL_INST2]

    MAL_INST_NAME = GRP2_MPP_EP02

    MAL_HOST = 192.168.0.142

    MAL_PORT = 5337

    MAL_INST_HOST = 192.168.1.132

    MAL_INST_PORT = 5236

    MAL_DW_PORT = 5253

    MAL_INST_DW_PORT = 5243

[MAL_INST3]

    MAL_INST_NAME = GRP1_MPP_EP11

    MAL_HOST = 192.168.0.142

    MAL_PORT = 5338

    MAL_INST_HOST = 192.168.1.132

    MAL_INST_PORT = 5237

    MAL_DW_PORT = 5254

    MAL_INST_DW_PORT = 5244

[MAL_INST4]

    MAL_INST_NAME = GRP2_MPP_EP22

    MAL_HOST = 192.168.0.141

    MAL_PORT = 5338

    MAL_INST_HOST = 192.168.1.131

    MAL_INST_PORT = 5237

    MAL_DW_PORT = 5254

    MAL_INST_DW_PORT = 5244
```

#### 7.4.3.3 配置 dmarch.ini（实时归档）

修改 dmarch.ini，配置实时归档。

除了本地归档外，其他归档配置项中的 ARCH\_DEST 表示实例是 PRIMARY 模式时，需要同步归档数据的目标实例名。

当前实例 GRP1\_MPP\_EP01 是主库，需要向 MPP 备库 GRP1\_MPP\_EP11 同步数据，因此实时归档的 ARCH\_DEST 配置为 GRP1\_MPP\_EP11。

```
[ARCHIVE_REALTIME1]

    ARCH_TYPE = REALTIME                     ##实时归档类型

    ARCH_DEST = GRP1_MPP_EP11                 ##实时归档目标实例名

[ARCHIVE_LOCAL1]

    ARCH_TYPE = LOCAL                         ##本地归档类型

    ARCH_DEST = /dm/data/EP01/DAMENG/arch     ##本地归档文件存放路径

    ARCH_FILE_SIZE = 128                     ##单位Mb，本地单个归档文件最大值

    ARCH_SPACE_LIMIT = 0                     ##单位Mb，0表示无限制，范围1024~4294967294M
```

#### 7.4.3.4 配置 dmmpp.ctl

dmmpp.ctl 是二进制文件，由 dmmpp.ini 文本通过 dmctlcvt 工具转换而来，dmmpp.ini 配置项如下表：

表7.9 dmmpp.ini配置项

| **配置项** | **配置含义** |
| --- | --- |
| \[SERVICE\_NAME\] | 标识每个实例的选项名 |
| MPP\_SEQ\_NO | 实例在 MPP 系统内的序号 |
| MPP\_INST\_NAME | 节点实例名 |

本例中两节点的 dmmpp.ini 配置如下：

```
[service_name1]

    mpp_seq_no = 0

    mpp_inst_name = GRP1_MPP_EP01

[service_name2]

    mpp_seq_no = 1

    mpp_inst_name = GRP2_MPP_EP02
```

转换命令如下：

```
./dmctlcvt     TYPE=2     SRC=/dm/data/EP01/DAMENG/dmmpp.ini  DEST=/dm/data/EP01/DAMENG/dmmpp.ctl
```

#### 7.4.3.5 启动主库

以 Mount 方式启动主库。

```
./dmserver /dm/data/EP01/DAMENG/dm.ini mount
```

> **注意**
> 
> 一定要以Mount方式启动数据库实例，否则系统启动时会重构回滚表空间，生成Redo日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动Open数据库。

#### 7.4.3.6 设置 OGUID

启动命令行工具 DIsql，使用 MPP 类型为 LOCAL 方式，登录主库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(45330);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.4.3.7 修改数据库模式

启动命令行工具 DIsql，使用 MPP 类型为 LOCAL 方式，登录主库修改数据库为 PRIMARY 模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>ALTER DATABASE PRIMARY;
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.4.4 配置主库 GRP2\_MPP\_EP02

#### 7.4.4.1 配置 dm.ini

在 B 机器上配置主库的实例名为 GRP2\_MPP\_EP02，dm.ini 参数修改如下：

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP2_MPP_EP02

PORT_NUM = 5236                 ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60         ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0             ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2             ##不允许备库OFFLINE表空间

MAL_INI = 1                     ##打开MAL系统

ARCH_INI = 1                     ##打开归档配置

MPP_INI = 1                         ##启用MPP配置

RLOG_SEND_APPLY_MON = 64         ##统计最近64次的日志发送信息
```

#### 7.4.4.2 配置 dmmal.ini

直接将 A 机器上实例 GRP1\_MPP\_EP01 配置的 dmmal.ini 拷贝到/dm/data/EP02/DAMENG 目录中。

#### 7.4.4.3 配置 dmarch.ini（实时归档）

修改 dmarch.ini，配置实时归档。

除了本地归档外，其他归档配置项中的 ARCH\_DEST 表示实例是 PRIMARY 模式时，需要同步归档数据的目标实例名。

当前实例 GRP2\_MPP\_EP02 是主库，需要向 MPP 备库 GRP2\_MPP\_EP22 同步数据，因此实时归档的 ARCH\_DEST 配置为 GRP2\_MPP\_EP22。

```
[ARCHIVE_REALTIME1]

    ARCH_TYPE = REALTIME                     ##实时归档类型

    ARCH_DEST = GRP2_MPP_EP22                 ##实时归档目标实例名

[ARCHIVE_LOCAL1]

    ARCH_TYPE = LOCAL                         ##本地归档类型

    ARCH_DEST = /dm/data/EP02/DAMENG/arch     ##本地归档文件存放路径

    ARCH_FILE_SIZE = 128                     ##单位Mb，本地单个归档文件最大值

    ARCH_SPACE_LIMIT = 0                     ##单位Mb，0表示无限制，范围1024~4294967294M
```

#### 7.4.4.4 配置 dmmpp.ctl

同 7.4.3.4 配置 dmmpp.ctl ，拷贝 dmmpp.ctl 到/dm/data/EP02/DAMENG 目录即可。

#### 7.4.4.5 启动主库

以 Mount 方式启动主库。

```
./dmserver /dm/data/EP02/DAMENG/dm.ini mount
```

> **注意**
> 
> 一定要以Mount方式启动数据库实例，否则系统启动时会重构回滚表空间，生成Redo日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动Open数据库。

#### 7.4.4.6 设置 OGUID

启动命令行工具 DIsql，使用 MPP 类型为 LOCAL 方式，登录主库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(45331);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.4.4.7 修改数据库模式

启动命令行工具 DIsql，使用 MPP 类型为 LOCAL 方式，登录主库修改数据库为 PRIMARY 模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>ALTER DATABASE PRIMARY;
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.4.5 配置备库 GRP1\_MPP\_EP11

#### 7.4.5.1 配置 dm.ini

在 B 机器上配置备库的实例名为 GRP1\_MPP\_EP11，dm.ini 参数修改如下：

##实例名，建议使用“组名\_守护环境\_序号”的命名方式，总长度不能超过 16

```
INSTANCE_NAME = GRP1_MPP_EP11

PORT_NUM = 5237                 ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60         ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0             ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2             ##不允许备库OFFLINE表空间

MAL_INI = 1                     ##打开MAL系统

ARCH_INI = 1                     ##打开归档配置

MPP_INI = 1                     ##打开MPP配置

RLOG_SEND_APPLY_MON = 64 ##统计最近64次的日志重演信息
```

#### 7.4.5.2 配置 dmmal.ini

直接将 A 机器上实例 GRP1\_MPP\_EP01 配置的 dmmal.ini 拷贝到 `/dm/data/EP11/DAMENG` 目录中。

#### 7.4.5.3 配置 dmarch.ini（实时归档）

修改 dmarch.ini，配置实时归档。

除了本地归档外，其他归档配置项中的 ARCH\_DEST 表示实例是 PRIMARY 模式时，需要同步归档数据的目标实例名。

当前实例 GRP1\_MPP\_EP11 是备库，守护系统配置完成后，可能在各种故障处理中，GRP1\_MPP\_EP11 切换为新的主库，正常情况下，GRP1\_MPP\_EP01 会切换为新的备库，需要向 GRP1\_MPP\_EP01 同步数据，因此实时归档的 ARCH\_DEST 配置为 GRP1\_MPP\_EP01。

```
[ARCHIVE_REALTIME1]
    ARCH_TYPE = REALTIME                     #实时归档类型
    ARCH_DEST = GRP1_MPP_EP01                 #实时归档目标实例名
[ARCHIVE_LOCAL1]
    ARCH_TYPE = LOCAL                         #本地归档类型
    ARCH_DEST = /dm/data/EP11/DAMENG/arch     #本地归档文件存放路径
    ARCH_FILE_SIZE = 128                     #单位Mb，本地单个归档文件最大值
    ARCH_SPACE_LIMIT = 0                 #单位Mb，0表示无限制，范围1024~4294967294M
```

#### 7.4.5.4 配置 dmmpp.ctl

数据守护 V2.1 及以上版本中，MPP 备库同样需要配置 dmmpp.ctl 文件，可以直接从主库上拷贝。

本例中将 A 机器上实例 GRP1\_MPP\_EP01 配置的 dmmpp.ctl 拷贝到 `/dm/data/EP11/DAMENG` 目录中。

#### 7.4.5.5 启动备库

以 Mount 方式启动备库

```
./dmserver /dm/data/EP11/DAMENG/dm.ini mount
```

> **注意**
> 
> 一定要以Mount方式启动数据库实例，否则系统启动时会重构回滚表空间，生成Redo日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动Open数据库。

#### 7.4.5.6 设置 OGUID

启动命令行工具 DIsql，登录备库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(45330);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.4.5.7 修改数据库模式

启动命令行工具 DIsql，登录实例修改数据库为 STANDBY 模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>alter database standby;

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.4.6 配置备库 GRP2\_MPP\_EP22

#### 7.4.6.1 配置 dm.ini

在 A 机器上配置备库的实例名为 GRP2\_MPP\_EP22，dm.ini 参数修改如下：

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP2_MPP_EP22

PORT_NUM = 5237                 ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60         ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0             ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2             ##不允许备库OFFLINE表空间

MAL_INI = 1                     ##打开MAL系统

ARCH_INI = 1                     ##打开归档配置

MPP_INI = 1                     ##打开MPP配置

RLOG_SEND_APPLY_MON = 64         ##统计最近64次的日志重演信息
```

#### 7.4.6.2 配置 dmmal.ini

直接将 A 机器上实例 GRP1\_MPP\_EP01 配置的 dmmal.ini 拷贝到 `/dm/data/EP22/DAMENG` 目录中。

#### 7.4.6.3 配置 dmarch.ini

修改 dmarch.ini，配置实时归档。

除了本地归档外，其他归档配置项中的 ARCH\_DEST 表示实例是 PRIMARY 模式时，需要同步归档数据的目标实例名。

当前实例 GRP2\_MPP\_EP22 是备库，守护系统配置完成后，可能在各种故障处理中，GRP2\_MPP\_EP22 切换为新的主库，正常情况下，GRP2\_MPP\_EP02 会切换为新的备库，需要向 GRP2\_MPP\_EP02 同步数据，因此实时归档的 ARCH\_DEST 配置为 GRP2\_MPP\_EP02。

```
[ARCHIVE_REALTIME1]
    ARCH_TYPE = REALTIME                     #实时归档类型
    ARCH_DEST = GRP2_MPP_EP02                 #实时归档目标实例名
[ARCHIVE_LOCAL1]
    ARCH_TYPE = LOCAL                         #本地归档类型
    ARCH_DEST = /dm/data/EP22/DAMENG/arch     #本地归档文件存放路径
    ARCH_FILE_SIZE = 128                     #单位Mb，本地单个归档文件最大值
    ARCH_SPACE_LIMIT = 0                 #单位Mb，0表示无限制，范围1024~4294967294M
```

#### 7.4.6.4 配置 dmmpp.ctl

数据守护 V2.1 及以上版本中，MPP 备库同样需要配置 dmmpp.ctl 文件，可以直接从主库上拷贝。

本例中将 A 机器上实例 GRP1\_MPP\_EP01 配置的 dmmpp.ctl 拷贝到 `/dm/data/EP22/DAMENG` 目录中。

#### 7.4.6.5 启动备库

以 Mount 方式启动实例。

```
./dmserver /dm/data/EP22/DAMENG/dm.ini mount
```

> **注意**
> 
> 一定要以Mount方式启动数据库实例，否则系统启动时会重构回滚表空间，生成Redo日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动Open数据库。

#### 7.4.6.6 设置 OGUID

启动命令行工具 DIsql，登录实例设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(45331);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.4.6.7 修改数据库模式

启动命令行工具 DIsql，登录实例修改数据库为 STANDBY 模式:

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>alter database standby;

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.4.7 配置 dmwatcher.ini

一般来说，每个单独的实例都是使用一个单独的守护进程守护。比如前面的实时主备和读写分离集群的配置。

本例中，由于同一台机器上有不同组的两个实例，我们可以只配置一个守护进程，同时守护两个实例。

A 机器上配置 dmwatcher.ini，配置为全局守护类型，使用自动切换模式。

```
[GRP1]
    DW_TYPE = GLOBAL                         #全局守护类型
    DW_MODE = AUTO                             #自动切换模式
    DW_ERROR_TIME = 10                         #远程守护进程故障认定时间
    INST_RECOVER_TIME = 60                     #主库守护进程启动恢复的间隔时间
    INST_ERROR_TIME = 10                     #本地实例故障认定时间
    INST_OGUID = 45330                         #守护系统唯一OGUID值
    INST_INI = /dm/data/EP01/DAMENG/dm.ini     #dm.ini配置文件路径
    INST_AUTO_RESTART = 1                     #打开实例的自动启动功能
    INST_STARTUP_CMD = /dm/bin/dmserver     #命令行方式启动
    RLOG_SEND_THRESHOLD = 0             #指定主库发送日志到备库的时间阈值，默认关闭
    RLOG_APPLY_THRESHOLD = 0                #指定备库重演日志的时间阈值，默认关闭
[GRP2]
    DW_TYPE = GLOBAL                         #全局守护类型
    DW_MODE = AUTO                             #自动切换模式
    DW_ERROR_TIME = 10                         #远程守护进程故障认定时间
    INST_RECOVER_TIME = 60                     #主库守护进程启动恢复的间隔时间
    INST_ERROR_TIME = 10                     #本地实例故障认定时间
    INST_OGUID = 45331                         #守护系统唯一OGUID值
    INST_INI = /dm/data/EP22/DAMENG/dm.ini     #dm.ini配置文件路径
    INST_AUTO_RESTART = 1                     #打开实例的自动启动功能
    INST_STARTUP_CMD = /dm/bin/dmserver     #命令行方式启动
    RLOG_SEND_THRESHOLD = 0             #指定主库发送日志到备库的时间阈值，默认关闭
    RLOG_APPLY_THRESHOLD = 0                 #指定备库重演日志的时间阈值，默认关闭
```

B 机器上配置 dmwatcher.ini，配置为全局守护类型，使用自动切换模式。

```
[GRP1]
    DW_TYPE = GLOBAL                         #全局守护类型
    DW_MODE = AUTO                             #自动切换模式
    DW_ERROR_TIME = 10                         #远程守护进程故障认定时间
    INST_RECOVER_TIME = 60                     #主库守护进程启动恢复的间隔时间
    INST_ERROR_TIME = 10                     #本地实例故障认定时间
    INST_OGUID = 45330                         #守护系统唯一OGUID值
    INST_INI = /dm/data/EP11/DAMENG/dm.ini     #dm.ini配置文件路径
    INST_AUTO_RESTART = 1                     #打开实例的自动启动功能
    INST_STARTUP_CMD = /dm/bin/dmserver     #命令行方式启动
    RLOG_SEND_THRESHOLD = 0             #指定主库发送日志到备库的时间阈值，默认关闭
    RLOG_APPLY_THRESHOLD = 0                 #指定备库重演日志的时间阈值，默认关闭
[GRP2]
    DW_TYPE = GLOBAL                         #全局守护类型
    DW_MODE = AUTO                             #自动切换模式
    DW_ERROR_TIME = 10                         #远程守护进程故障认定时间
    INST_RECOVER_TIME = 60                     #主库守护进程启动恢复的间隔时间
    INST_ERROR_TIME = 10                     #本地实例故障认定时间
    INST_OGUID = 45331                         #守护系统唯一OGUID值
    INST_INI = /dm/data/EP02/DAMENG/dm.ini     #dm.ini配置文件路径
    INST_AUTO_RESTART = 1                     #打开实例的自动启动功能
    INST_STARTUP_CMD = /dm/bin/dmserver     #命令行方式启动
    RLOG_SEND_THRESHOLD = 0             #指定主库发送日志到备库的时间阈值，默认关闭
    RLOG_APPLY_THRESHOLD = 0                 #指定备库重演日志的时间阈值，默认关闭
```

### 7.4.8 配置监视器

由于主库和实时备库的守护进程配置为自动切换模式，因此这里必须配置确认监视器。和普通监视器相比，确认监视器除了相同的命令支持外，在主库发生故障时，能够自动通知实时备库接管为新的主库，具有自动故障处理的功能。

配置确认监视器时可以选择配置单实例监视器或配置多实例监视器，下面将分别介绍配置单实例监视器以及多实例监视器时 dmmonitor.ini 配置文件中的配置信息。

#### 7.4.8.1 配置单实例监视器

修改 dmmonitor.ini 配置确认监视器，其中 MON\_DW\_IP 中的 IP 和 PORT 和 dmmal.ini 中的 MAL\_HOST 和 MAL\_DW\_PORT 配置项保持一致。

```
MON_DW_CONFIRM = 1                         ##确认监视器模式

MON_LOG_PATH = /dm/data/log             ##监视器日志文件存放路径

MON_LOG_INTERVAL = 60                     ##每隔60s定时记录系统信息到日志文件

MON_LOG_FILE_SIZE = 32                     ##每个日志文件最大32M

MON_LOG_SPACE_LIMIT = 0                 ##不限定日志文件总占用空间

[GRP1]

    MON_INST_OGUID = 45330 ##组GRP1的唯一OGUID值

    ##以下配置为监视器到组GRP1的守护进程的连接信息，以“IP:PORT”的形式配置

    ##IP对应dmmal.ini中的MAL_HOST，PORT对应dmmal.ini中的MAL_DW_PORT

    MON_DW_IP = 192.168.0.141:5253

    MON_DW_IP = 192.168.0.142:5254

[GRP2]

    MON_INST_OGUID = 45331 ##组GRP2的唯一OGUID值

    ##以下配置为监视器到组GRP2的守护进程的连接信息，以“IP:PORT”的形式配置

    ##IP对应dmmal.ini中的MAL_HOST，PORT对应dmmal.ini中的MAL_DW_PORT

    MON_DW_IP = 192.168.0.142:5253

    MON_DW_IP = 192.168.0.141:5254
```

#### 7.4.8.2 配置多实例监视器

为每个实例配置一个 dmmonitor.ini。众多 dmmonitor.ini 中，除 MON\_ID 和 MON\_NAME 参数不同以外，其他参数应完全一致。

使用配置文件启动多实例监视器实例之前，需要先初始化联机日志文件。初始化联机日志文件的具体操作请查看 [4.2.2.2.2 初始化联机日志文件](data-watch-monitor.md) 。

以其中一个实例的 dmmonitor.ini 为例进行介绍。各实例的 MON\_ID 应与某一个实例配置项中的 MON\_INST\_ID 相同，各实例的 MON\_NAME 与对应的监视器实例名相同。dmmonitor.ini 配置文件中的内容如下：

```
MON_LOG_PATH                = /dm/data/log
MON_LOG_INTERVAL            = 60
MON_LOG_FILE_SIZE            = 32
MON_LOG_SPACE_LIMIT            = 0
MON_DW_CONFIRM                = 1
MON_INST_NUM                = 3            #实例总个数
MON_HB_INTERVAL                = 60         #通信心跳校验间隔
MON_BRO_INTERVAL            = 100         #raft协议中实例通信心跳间隔
MON_VOTE_INTERVAL            = 100         #raft协议中基础投票间隔
MON_ID                        = 1             #当前监视器在监视器系统中的ID
MON_MID                        = 45614        #当前监视器系统的唯一标识
MON_NAME                = MON1  #监视器名

[GRP1]
MON_INST_OGUID                = 45330
MON_DW_IP                     = 192.168.0.141:5253
MON_DW_IP                     = 192.168.0.142:5254
[GRP2]
MON_INST_OGUID                = 45331
MON_DW_IP                     = 192.168.0.142:5253
MON_DW_IP                     = 192.168.0.141:5254

[MON1] #监视器实例信息
MON_HOST                  = 192.168.0.143         #MON1监视器所在IP 
MON_PORT                  = 8339                     #MON1监视器监听端口
MON_INST_ID                = 1                     #监视器实例在监视器系统中的ID
[MON2]
MON_HOST                  = 192.168.0.144         #MON2监视器所在IP 
MON_PORT                  = 8340                     #MON2监视器监听端口
MON_INST_ID                = 2                     #监视器实例在监视器系统中的ID 
[MON3]
MON_HOST                  = 192.168.0.145         #MON3监视器所在IP 
MON_PORT                  = 8341                     #MON3监视器监听端口
MON_INST_ID                = 3                     #监视器实例在监视器系统中的ID
```

### 7.4.9 启动守护进程

分别启动 A、B 机器上的守护进程，例如：

```
./dmwatcher /dm/data/EP01/DAMENG/dmwatcher.ini
```

守护进程启动后，进入 Startup 状态，此时实例都处于 Mount 状态。守护进程开始广播自身和其监控实例的状态信息，结合自身信息和远程守护进程的广播信息，守护进程将本地实例 Open，并切换为 Open 状态。

### 7.4.10 启动监视器

启动监视器命令：

```
./dmmonitor /dm/data/dmmonitor.ini
```

多实例确认监视器系统中，需逐个单独启动各节点上的监视器（启动后，多实例监视器暂不支持动态修改配置，具体说明请查看 [4.2.2.2.3 启动多实例监视器](data-watch-monitor.md) ）。

监视器提供一系列命令，支持当前守护系统状态查看以及故障处理，可输入 help 命令，查看各种命令使用说明，结合实际情况选择使用。

至此 MPP 实时主备搭建完毕，在搭建步骤和各项配置都正确的情况下，在监视器上执行 show 命令，可以监控到所有实例都处于 Open 状态，所有守护进程也都处于 Open 状态，即为正常运行状态。

## 7.5 配置 DMDSC 主备环境

DMDSC 主备环境搭建和单节点主备环境搭建步骤类似，区别主要在于首先要准备 DMDSC 集群环境，DM8 支持单节点和单节点、DMDSC 集群和单节点之间搭建主备环境。

### 7.5.1 配置说明

DMDSC 集群可以作为主库，也可以作为实时备库、即时备库或者异步备库，一般建议将 DMDSC 集群配置为主库，将单节点配置为备库。如果要将 DMDSC 集群作为备库配置在数据守护系统中，则要将其作为一个整体配置在源库的 dmarch.ini 中，也就是 DMDSC 集群所有节点要配置在同一个归档配置项中，每个节点实例名以“/”分隔开来。

假如 DMDSC 集群有两个节点 GRP1\_RT\_DSC01 和 GRP1\_RT\_DSC02，DMDSC 集群要作为备库进行配置，其源库为 A，则要在 A 的 dmarch.ini 文件中增加 DMDSC 集群的归档配置，这里以实时备库为例说明如下：

```
[ARCHIVE_REALTIME1]

    ARCH_TYPE = REALTIME

    ARCH_DEST = GRP1_RT_DSC01/GRP1_RT_DSC02
```

如果 DMDSC 集群要作为即时备库或者异步备库来配置，ARCH\_DEST 的配置方式和示例中是相同的，ARCH\_TYPE 则要分别替换为 TIMELY 或者 ASYNC，中括号内的配置项名称中包含的归档类型也建议修改和 ARCH\_TYPE 一致。

而如果异步备库的源库为 DMDSC 集群，则要求 DMDSC 集群中的所有节点都将 INI 参数 TIMER\_INI 置为 1 并配置 dmtimer.ini。

### 7.5.2 环境说明

下面以 DMDSC 集群和单节点之间搭建实时主备环境为例，对搭建步骤进行说明。

准备三台机器 DW\_P、DW\_S、DW\_M，DW\_P 和 DW\_S 用来部署主备库，DW\_M 用来部署确认监视器。其中 DW\_P 和 DW\_S 配置两块网卡，一块接入内部网络交换模块，一块接入到外部交换机，DW\_M 接入内部网络。

三台机器事先都安装了 DM，安装路径为'/dm'，执行程序保存在'/dm/bin'目录中，数据存放路径为'/dm/data'。

各主备库的实例名建议采用“组名\_守护环境\_序号”的方式命名，方便按组区分不同实例，注意总长度不能超过 16。本示例中组名为“GRP1”，配置为实时主备，主库 DMDSC 集群的两个节点实例名分别命名为“GRP1\_RT\_DSC01”、“GRP1\_RT\_DSC02”，备库命名为“GRP1\_RT\_01”。

表7.10 配置环境说明

| **机器名** | **IP 地址** | **初始状态** | **操作系统** | **备注** |
| --- | --- | --- | --- | --- |
| DW\_P | 192.168.1.131 192.168.0.141 | 主库 GRP1\_RT\_DSC01 GRP1\_RT\_DSC02 | Linux rh6-141.test 2.6.32-220.el6.x86\_64##1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux | 192.168.1.131 外部服务 IP；   192.168.0.141 内部通信 IP |
| DW\_S | 192.168.1.132 192.168.0.142 | 备库 GRP1\_RT\_01 | Linux rh6-142.localdomain 2.6.32-220.el6.x86\_64##1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux | 192.168.1.132 外部服务 IP；   192.168.0.142 内部通信 IP |
| DW\_M | 192.168.0.73 | 确认监视器 | Linux rh6-73.localdomain 2.6.32-220.el6.x86\_64##1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux |  |

表7.11 端口规划

| **实例名** | **PORT\_NUM** | **MAL\_INST\_DW\_PORT** | **MAL\_HOST** | **MAL\_PORT** | **MAL\_DW\_PORT** |
| --- | --- | --- | --- | --- | --- |
| GRP1\_RT\_DSC01 | 8344 | 4567 | 192.168.0.141 | 8338 | 3567 |
| GRP1\_RT\_DSC02 | 8346 | 4568 | 192.168.0.141 | 8339 | 3568 |
| GRP1\_RT\_01 | 9344 | 4569 | 192.168.0.142 | 8738 | 3569 |

### 7.5.3 配置 DMDSC 主库环境

使用 DMDSC 集群手册《DM8 数据共享集群》或者相应脚本搭建好两节点 DMDSC 集群环境，DMDSC 实例名分别为 GRP1\_RT\_DSC01、GRP1\_RT\_DSC02。

注意 dmcss 对 DMServer 的自动拉起功能先不要打开，避免影响到配置过程。

搭建完成后，正常退出 DMDSC 集群的两个 DMServer 节点实例，不需要退出 dmcss 和 dmasmsvr。

#### 7.5.3.1 配置 dmarch.ini

分别编辑两个 DMDSC 节点的 dmarch.ini 文件，增加本地归档和远程归档。dmarch.ini 文件放在各自 dm.ini 中指定的 CONFIG\_PATH 目录下。

如果 DMDSC 主库的本地归档路径发生了变化，需要保证 DMDSC 主库本地归档的完整性，例如将本地归档路径发生变化前的归档文件拷至变化后的路径下，否则 DMDSC 主备环境会由于主库归档日志不完整，将备库归档状态置为 INVALID，归档同步失败（dmmonitor 执行 show arch send info EP，系统报错）。

**（1）配置 GRP1\_RT\_DSC01 的 dmarch.ini 文件**

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE = LOCAL
    ARCH_DEST = +DMDATA/DSC/DSC01/arch
    ARCH_FILE_SIZE = 128
    ARCH_SPACE_LIMIT = 0
[ARCHIVE_REMOTE]
    ARCH_TYPE = REMOTE
    ARCH_DEST = GRP1_RT_DSC02
    ARCH_INCOMING_PATH =  +DMDATA/DSC/DSC02/arch
```

**（2）配置 GRP1\_RT\_DSC02 的 dmarch.ini 文件**

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE = LOCAL
    ARCH_DEST = +DMDATA/DSC/DSC02/arch
    ARCH_FILE_SIZE = 128
    ARCH_SPACE_LIMIT = 0
[ARCHIVE_REMOTE]
    ARCH_TYPE = REMOTE
    ARCH_DEST = GRP1_RT_DSC01
    ARCH_INCOMING_PATH = +DMDATA/DSC/DSC01/arch
```

#### 7.5.3.2 配置 dm.ini

分别编辑两个 DMDSC 节点的 dm.ini 文件，打开归档参数：

```
ARCH_INI = 1
```

#### 7.5.3.3 备份 DMDSC 库

重启 DMDSC 集群的两个 DMServer 实例，然后再正常退出。在 DMDSC 集群生成有归档日志的情况下进行脱机备份，以便后续校验日志连续性时使用。

```
//启动dmrman

./dmrman use_ap=2 dcr_ini=/dm/data/DSC/conf/dmdcr1.ini

//脱机备份DMDSC集群

RMAN>BACKUP DATABASE '/dm/data/DSC/DSC01/dm.ini' FULL BACKUPSET  '/dm/data/DSC/DSC01/bak/db_full_bak_for_DSC';
```

### 7.5.4 配置单节点备库

按照以下步骤准备单节点备库环境：

```
//初始化备库

./dminit path=/dm/data/EP01/ SYSDBA_PWD=DMdba_123 SYSAUDITOR_PWD=DMauditor_123

//启动dmrman

./dmrman use_ap=2

//使用DMDSC库的备份集还原恢复到单节点备库

RMAN>RESTORE DATABASE '/dm/data/EP01/DAMENG/dm.ini' FROM BACKUPSET '/dm/data/DSC/DSC01/bak/db_full_bak_for_DSC';

RMAN>RECOVER DATABASE '/dm/data/EP01/DAMENG/dm.ini' FOR STANDBY FROM BACKUPSET '/dm/data/DSC/DSC01/bak/db_full_bak_for_DSC';

RMAN>RECOVER DATABASE '/dm/data/EP01/DAMENG/dm.ini' UPDATE DB_MAGIC;
```

### 7.5.5 配置 dm.ini

依次配置 DMDSC 主库所有节点和单节点备库的 dm.ini 文件，修改数据守护相关的参数配置。

**（1）配置 GRP1\_RT\_DSC01 的 dm.ini 文件**

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP1_RT_DSC01

PORT_NUM = 8344                 ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60         ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0             ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2             ##不允许备库OFFLINE表空间

MAL_INI = 1                     ##打开MAL系统

ARCH_INI = 1                     ##打开归档配置

RLOG_SEND_APPLY_MON = 64         ##统计最近64次的日志发送信息
```

**（2）配置 GRP1\_RT\_DSC02 的 dm.ini 文件**

```
INSTANCE_NAME = GRP1_RT_DSC02

PORT_NUM = 8346

DW_INACTIVE_INTERVAL = 60

ALTER_MODE_STATUS = 0

ENABLE_OFFLINE_TS = 2

MAL_INI = 1

ARCH_INI = 1

RLOG_SEND_APPLY_MON = 64
```

**（3）配置 GRP1\_RT\_01 的 dm.ini 文件**

```
INSTANCE_NAME = GRP1_RT_01

PORT_NUM = 9344

DW_INACTIVE_INTERVAL = 60

ALTER_MODE_STATUS = 0

ENABLE_OFFLINE_TS = 2

MAL_INI = 1

ARCH_INI = 1

RLOG_SEND_APPLY_MON = 64
```

### 7.5.6 配置 dmmal.ini

在 DMDSC 集群的 dmmal.ini 文件基础上，增加备库 GRP1\_RT\_01 的配置项。

所有节点实例的 dmmal.ini 文件内容是一致的，配置完成后，拷贝到每个节点实例 dm.ini 中指定的 CONFIG\_PATH 目录下。

```
MAL_CHECK_INTERVAL = 30             ##MAL链路检测时间间隔

MAL_CONN_FAIL_INTERVAL = 10         ##判定MAL链路断开的时间

[MAL_INST0]

    MAL_INST_NAME = GRP1_RT_DSC01     ##实例名，和dm.ini中的INSTANCE_NAME一致

    MAL_HOST = 192.168.0.141         ##MAL系统监听TCP连接的IP地址

    MAL_PORT = 8338                 ##MAL系统监听TCP连接的端口

    MAL_INST_HOST = 192.168.1.131     ##实例的对外服务IP地址

    MAL_INST_PORT = 8344             ##实例的对外服务端口，和dm.ini中的PORT_NUM一致

    MAL_DW_PORT = 3567                 ##实例本地的守护进程监听TCP连接的端口

    MAL_INST_DW_PORT = 4567         ##实例监听守护进程TCP连接的端口

[MAL_INST1]

    MAL_INST_NAME = GRP1_RT_DSC02

    MAL_HOST = 192.168.0.141

    MAL_PORT = 8339

    MAL_INST_HOST = 192.168.1.131

    MAL_INST_PORT = 8346

    MAL_DW_PORT = 3568

    MAL_INST_DW_PORT = 4568

[MAL_INST2]

    MAL_INST_NAME = GRP1_RT_01

    MAL_HOST = 192.168.0.142

    MAL_PORT = 8738

    MAL_INST_HOST = 192.168.1.132

    MAL_INST_PORT = 9344

    MAL_DW_PORT = 3569

    MAL_INST_DW_PORT = 4569
```

### 7.5.7 配置 dmarch.ini

再次编辑各个节点的 dmarch.ini 文件，增加实时归档配置。

**（1）修改 GRP1\_RT\_DSC01 的 dmarch.ini 文件**

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE = LOCAL
    ARCH_DEST = +DMDATA/DSC/DSC01/arch
    ARCH_FILE_SIZE = 128
    ARCH_SPACE_LIMIT = 0

[ARCHIVE_REMOTE]
    ARCH_TYPE = REMOTE
    ARCH_DEST = GRP1_RT_DSC02
    ARCH_INCOMING_PATH =  +DMDATA/DSC/DSC02/arch

[ARCHIVE_REALTIME]
    ARCH_TYPE = REALTIME
    ARCH_DEST = GRP1_RT_01
```

**（2）修改 GRP1\_RT\_DSC02 的 dmarch.ini 文件**

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE = LOCAL
    ARCH_DEST = +DMDATA/DSC/DSC02/arch
    ARCH_FILE_SIZE = 128
    ARCH_SPACE_LIMIT = 0

[ARCHIVE_REMOTE]
    ARCH_TYPE = REMOTE
    ARCH_DEST = GRP1_RT_DSC01
    ARCH_INCOMING_PATH = +DMDATA/DSC/DSC01/arch

[ARCHIVE_REALTIME]
    ARCH_TYPE = REALTIME
    ARCH_DEST = GRP1_RT_01
```

**（3）修改 GRP1\_RT\_01 的 dmarch.ini 文件**

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE            = LOCAL
    ARCH_DEST            = /dm/data/EP01/DAMENG/arch
    ARCH_FILE_SIZE        = 128
    ARCH_SPACE_LIMIT    = 0

[ARCHIVE_REALTIME1]
    ARCH_TYPE            = REALTIME
    ARCH_DEST            = GRP1_RT_DSC01/GRP1_RT_DSC02
```

### 7.5.8 配置 dmwatcher.ini

依次配置每个节点实例的 dmwatcher.ini 文件，放到各自 dm.ini 中指定的 CONFIG\_PATH 目录下。

另外要注意，DMDSC 集群各节点实例的自动拉起是由各自本地的 dmcss 执行的，不是由守护进程执行，如果要打开 DMDSC 集群的自动拉起，需要再去配置 dmdcr.ini 中的自动拉起参数，为避免 dmcss 在所有配置步骤完成之前提前将 DMServer 自动拉起，这里先不修改 dmdcr.ini 配置，放到后面步骤中修改。

**（1）配置 GRP1\_RT\_DSC01 的 dmwatcher.ini 文件**

```
[GRP1]

    DW_TYPE = GLOBAL                         ##全局守护类型

    DW_MODE = MANUAL                         ##手动切换模式

    DW_ERROR_TIME = 60                         ##远程守护进程故障认定时间

    INST_RECOVER_TIME = 60                     ##主库守护进程启动恢复的间隔时间

    INST_ERROR_TIME = 35                     ##本地实例故障认定时间

    INST_INI = /dm/data/DSC/DSC01/dm.ini     ##dm.ini配置文件路径

    DCR_INI = /dm/data/DSC/conf/dmdcr1.ini     ##dmdcr.ini配置文件路径

    INST_OGUID = 1000                         ##守护系统唯一OGUID值

    INST_STARTUP_CMD = /dm/bin/dmserver     ##命令行方式启动

    INST_AUTO_RESTART = 0                     ##关闭实例的自动启动功能

    RLOG_SEND_THRESHOLD = 0                 ##指定主库发送日志到备库的时间阈值，默认关闭

    RLOG_APPLY_THRESHOLD = 0                 ##指定备库重演日志的时间阈值，默认关闭
```

**（2）配置 GRP1\_RT\_DSC02 的 dmwatcher.ini 文件**

```
[GRP1]

    DW_TYPE = GLOBAL

    DW_MODE = MANUAL

    DW_ERROR_TIME = 60

    INST_RECOVER_TIME = 60

    INST_ERROR_TIME = 35

    INST_INI = /dm/data/DSC/DSC02/dm.ini

    DCR_INI = /dm/data/DSC/conf/dmdcr2.ini

    INST_OGUID = 1000

    INST_STARTUP_CMD = /dm/bin/dmserver

    INST_AUTO_RESTART = 0

    RLOG_SEND_THRESHOLD = 0

    RLOG_APPLY_THRESHOLD = 0
```

**（3）配置 GRP1\_RT\_01 的 dmwatcher.ini 文件**

```
[GRP1]

    DW_TYPE = GLOBAL

    DW_MODE = MANUAL

    DW_ERROR_TIME = 60

    INST_RECOVER_TIME = 60

    INST_ERROR_TIME = 35

    INST_INI = /dm/data/EP01/dm.ini

    INST_OGUID = 1000

    INST_STARTUP_CMD = /dm/bin/dmserver

    INST_AUTO_RESTART = 0 ##对单节点，如果需要打开自动拉起功能，将此配置修改为1即可

    RLOG_SEND_THRESHOLD = 0

    RLOG_APPLY_THRESHOLD = 0
```

> **注意**
> 
> 实际配置时，相关的端口配置和OGUID值建议不要和手册示例使用完全相同的值，避免多个用户在同一个环境下搭建不同的数据守护系统，出现消息混乱或者端口冲突等问题。

### 7.5.9 配置 dmmonitor.ini

编辑 dmmonitor.ini 文件，放在/dm/data 目录下:

```
MON_LOG_PATH = /dm/data/log

MON_LOG_INTERVAL = 60

MON_LOG_FILE_SIZE = 64

MON_LOG_SPACE_LIMIT = 0

MON_DW_CONFIRM = 0

[GRP1]

MON_INST_OGUID = 1000

MON_DW_IP = 192.168.0.141:3567/192.168.0.141:3568

MON_DW_IP = 192.168.0.142:3569
```

### 7.5.10 配置 dmdcr.ini

DMDSC 集群中 DMServer 的自动拉起是由 dmcss 执行的，如果不需要打开 dmcss 的自动拉起功能，则可以跳过此章节。

否则需要修改 dmdcr.ini 中的自动拉起配置参数，此参数修改完成后，需要重启 dmcss 才可以生效，为了避免重启 dmcss 引发 dmasmsvr 被强制关闭，这里先将 dmcss 和 dmasmsvr 都正常退出。

**1\. 打开 GRP1\_RT\_DSC01 的自动拉起参数**

修改对应 dmcss 的 dmdcr.ini 文件，打开自动拉起参数。

```
##打开DB重启参数，命令行方式启动

DMDCR_DB_RESTART_INTERVAL = 60

DMDCR_DB_STARTUP_CMD = /dm/bin/dmserver path=/dm/data/DSC/DSC01/dm.ini

dcr_ini=/dm/data/DSC/conf/dmdcr1.ini mount
```

**2\. 打开 GRP1\_RT\_DSC02 的自动拉起参数**

修改对应 dmcss 的 dmdcr.ini 文件，打开自动拉起参数。

```
##打开DB重启参数，命令行方式启动

DMDCR_DB_RESTART_INTERVAL = 60

DMDCR_DB_STARTUP_CMD = /dm/bin/dmserver path=/dm/data/DSC/DSC02/dm.ini

dcr_ini=/dm/data/DSC/conf/dmdcr2.ini mount
```

**3\. 重启 dmcss 和 dmasmsvr**

```
./dmcss dcr_ini=/dm/data/DSC/conf/dmdcr1.ini

./dmcss dcr_ini=/dm/data/DSC/conf/dmdcr2.ini

./dmasmsvr dcr_ini=/dm/data/DSC/conf/dmdcr1.ini

./dmasmsvr dcr_ini=/dm/data/DSC/conf/dmdcr2.ini
```

### 7.5.11 启动主备库

注意实例都要使用 Mount 方式启动。

1. 启动 DMDSC 集群的两个 DMServer 实例

如果 dmcss 打开有自动拉起功能，也可以等待 dmcss 将本地的 DMServer 实例自动拉起（要保证以 Mount 方式拉起）。

手动启动命令如下：

```
./dmserver /dm/data/DSC/DSC01/dm.ini DCR_INI=/dm/data/DSC/conf/dmdcr1.ini mount

./dmserver /dm/data/DSC/DSC02/dm.ini DCR_INI=/dm/data/DSC/conf/dmdcr2.ini mount
```
2. 启动单节点备库
```
./dmserver /dm/data/EP01/dm.ini mount
```

### 7.5.12 设置 OGUID

启动命令行工具 DIsql，连接 DMDSC 集群中的任意一个节点，设置 DMDSC 主库的 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>SP_SET_OGUID(1000);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

DIsql 连接单节点备库，设置备库 OGUID。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>SP_SET_OGUID(1000);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.5.13 修改主备库模式

启动命令行工具 DIsql，连接 DMDSC 集群中的任意一个节点，修改 DMDSC 库为 Primary 模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>ALTER DATABASE PRIMARY;
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

DIsql 连接单节点备库，修改备库为 STANDBY 模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>ALTER DATABASE STANDBY;
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.5.14 启动守护进程

启动 DMDSC 主库的所有守护进程：

```
./dmwatcher /dm/data/DSC/DSC01/dmwatcher.ini

./dmwatcher /dm/data/DSC/DSC02/dmwatcher.ini
```

启动备库的守护进程：

```
./dmwatcher /dm/data/EP01/dmwatcher.ini
```

### 7.5.15 启动监视器

启动数据守护监视器：

```
./dmmonitor path=/dm/data/dmmonitor.ini
```

监视器提供一系列命令，支持当前守护系统状态查看以及故障处理，可输入 help 命令，查看各种命令使用说明，结合实际情况选择使用。

另外，DMDSC 集群也有自己的监视器工具，需要时也可以启动：

```
./dmcssm ini_path=/dm/data/DSC/conf/dmcssm.ini
```

至此 DMDSC 集群的实时数据守护系统搭建完毕，在搭建步骤和各项配置都正确的情况下，在监视器上执行 show 命令，可以监控到所有实例都处于 Open 状态，所有守护进程也都处于 Open 状态，即为正常运行状态。

## 7.6 配置异步备库

在实际应用中，如果数据库规模很大，并且对数据的实时性要求不是很严格，则可以配置多个异步备库用于分担统计报表等任务。

异步备库支持多源配置，目的是在实时或即时主备环境中，当主备库切换或者主库故障时，备库接管以后可以继续向同一个异步备库同步数据，因此如果主库配置了异步备库，在所有备库上也需要配置相同的异步备库，备库只有在切换为主库时才会向其同步数据。

这里以实时主备环境为例，仍然采用 7.2 配置实时主备 小节的配置环境，对异步备库的搭建步骤做举例说明，读写分离集群、MPP 主备和 DMDSC 主备的异步备库搭建步骤是相同的，只需要根据实际情况调整配置项的具体值即可。

这里将配置两个异步备库 GRP1\_LOCAL\_01 和 GRP1\_LOCAL\_02。其中 GRP1\_LOCAL\_01 配置在主库 GRP1\_RT\_01 上；而 GRP1\_LOCAL\_02 以级联方式配置在 GRP1\_LOCAL\_01 上，如果不需要级联备库，则可以直接跳过和 GRP1\_LOCAL\_02 相关的配置步骤。

> **注意**
> 
> 如果只需要搭建一主一异步备库的环境，则主库守护进程需要配置为LOCAL守护类型，并把本章节示例的dmmal.ini和dmarch.ini中去掉实时备库相关配置即可，其他配置方法没有差别。

### 7.6.1 环境说明

这里采用 7.2 配置实时主备 的实时主备环境，增加一台机器用来部署异步备库，其他环境不变。

新增的机器事先安装了 DM，安装路径为'/dm'，执行程序保存在'/dm/bin'目录中，数据存放路径为'/dm/data'。

新增的异步备库实例名为“GRP1\_LOCAL\_01”和“GRP1\_LOCAL\_02”，按照“组名\_守护环境\_序号”的建议方式命名，注意总长度不能超过 16。

表7.12 配置环境说明

| **机器名** | **IP 地址** | **初始状态** | **操作系统** | **备注** |
| --- | --- | --- | --- | --- |
| DW\_S2 | 192.168.1.133 192.168.0.143 | 异步备库 GRP1\_LOCAL\_01 | Linux rh6-143.localdomain 2.6.32-220.el6.x86\_64#1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux | 192.168.1.133 外部服务 IP；   192.168.0.143 内部通信 IP |
| DW\_S3 | 192.168.1.134 192.168.0.144 | 异步备库 GRP1\_LOCAL\_02 | Linux rh6-143.localdomain 2.6.32-220.el6.x86\_64 #1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux | 192.168.1.134 外部服务 IP； 192.168.0.144 内部通信 IP |

### 7.6.2 数据准备

按照 7.1 数据准备 中的方法准备异步备库的数据。

如果实时主备守护环境已经处于运行状态，需要先正常退出主备库实例和守护进程。

### 7.6.3 配置主库 GRP1\_RT\_01

#### 7.6.3.1 配置 dm.ini

在 7.2.3.1 配置 dm.ini 的基础上，打开定时器配置，其他配置不变。

```
##配置有异步归档时，打开定时器，定时同步归档到异备库

TIMER_INI = 1
```

#### 7.6.3.2 配置 dmmal.ini

在 7.2.3.2 配置 dmmal.ini 的基础上，增加异步备库 GRP1\_LOCAL\_01 和 GRP1\_LOCAL\_02 的 MAL 配置项。

```
[MAL_INST3]
    MAL_INST_NAME = GRP1_LOCAL_01         #实例名，和dm.ini中的INSTANCE_NAME一致
    MAL_HOST = 192.168.0.143             #MAL系统监听TCP连接的IP地址
    MAL_PORT = 61143                     #MAL系统监听TCP连接的端口
    MAL_INST_HOST = 192.168.1.133         #实例的对外服务IP地址
    MAL_INST_PORT = 32143             #实例的对外服务端口，和dm.ini中的PORT_NUM一致
    MAL_DW_PORT = 52143                 #实例对应的守护进程监听TCP连接的端口
    MAL_INST_DW_PORT = 33143             #实例监听守护进程TCP连接的端口
[MAL_INST4]
      MAL_INST_NAME= GRP1_LOCAL_02         #实例名，和dm.ini中的INSTANCE_NAME一致
      MAL_HOST = 192.168.0.144            #MAL系统监听TCP连接的IP地址
      MAL_PORT= 61144                    #MAL系统监听TCP连接的端口
      MAL_INST_HOST= 192.168.1.134        #实例的对外服务IP地址
      MAL_INST_PORT= 32144            #实例的对外服务端口，和dm.ini中的PORT_NUM一致
     MAL_DW_PORT= 52144                    #实例对应的守护进程监听TCP连接的端口
     MAL_INST_DW_PORT= 33144             #实例监听守护进程TCP连接的端口
```

#### 7.6.3.3 配置 dmarch.ini

在 7.2.3.3 配置 dmarch.ini 的基础上，增加异步归档的配置项。

```
[ARCHIVE_ASYNC]

    ARCH_TYPE = ASYNC                 ##异步归档类型

    ARCH_DEST = GRP1_LOCAL_01         ##异步归档目标实例名

    ARCH_TIMER_NAME = RT_TIMER         ##定时器名称，和dmtimer.ini中的名称一致
```

如果异步备库为 DMDSC 集群，则 ARCH\_DEST 中需要配置 DMDSC 集群中所有节点实例名称，不同实例名之间使用“/”分隔。假设 DMDSC 集群中包含两个节点实例，实例名分别为 DSC01 和 DSC02，则需要配置 ARCH\_DEST=DSC01/DSC02。

#### 7.6.3.4 配置 dmtimer.ini

配置 dmtimer.ini，用于定时触发实例发送归档日志到异步备库。

下面示例中定时器配置为每天 00:00:00 触发主库发送归档日志到异步备库，可以根据实际情况再做调整。

```
[RT_TIMER] #和dmarch.ini中的ARCH_TIMER_NAME一致
    TYPE = 2
    FREQ_MONTH_WEEK_INTERVAL = 1
    FREQ_SUB_INTERVAL = 0
    FREQ_MINUTE_INTERVAL = 0
    START_TIME = 00:00:00
    END_TIME = 23:59:59
    DURING_START_DATE = 2016-02-11 17:36:09
    DURING_END_DATE = 9999-12-31 23:59:59
    NO_END_DATE_FLAG = 1
    DESCRIBE = RT TIMER
    IS_VALID = 1
```

#### 7.6.3.5 其他配置说明

如果配置异步备库时，实时主备环境已经配置完成，这里对主库不需要再做其他配置，由于在配置异步备库之前实时主备环境已经被正常关闭，此处可以使用 Mount 方式将主库重启启动，并启动主库的守护进程。

如果同时也在搭建主库和实时备库，则主库其他的配置步骤请再参考 7.2.3 配置主库 GRP1\_RT\_01 的配置说明。

### 7.6.4 配置备库 GRP1\_RT\_02

主库上配置异步备库，备库上也需要增加相同的异步备库配置，保证备库在切换为主库后可以继续向同一个异步备库同步数据。

#### 7.6.4.1 配置 dm.ini

在 7.2.4.1 配置 dm.ini 的基础上，打开定时器配置，其他配置不变。

```
##配置有异步归档时，打开定时器，定时同步归档到异备库

TIMER_INI = 1
```

#### 7.6.4.2 配置 dmmal.ini

dmmal.ini 中需要增加到异步备库 GRP1\_LOCAL\_01 的 MAL 配置项，可以直接拷贝 7.6.3.2 配置 dmmal.ini 修改后的 dmmal.ini 文件地/dm/data/DAMENG/目录中。

#### 7.6.4.3 配置 dmarch.ini

在 7.2.4.3 配置 dmarch.ini 的基础上，增加异步归档的配置项。

```
[ARCHIVE_ASYNC]

    ARCH_TYPE = ASYNC ##异步归档类型

    ARCH_DEST = GRP1_LOCAL_01 ##异步归档目标实例名

    ARCH_TIMER_NAME = RT_TIMER ##定时器名称，和dmtimer.ini中的名称一致
```

#### 7.6.4.4 配置 dmtimer.ini

配置 dmtimer.ini，用于备库切换为主库后，定时触发实例发送归档日志到异步备库。

下面示例中定时器配置为每天 00:00:00 触发主库发送归档日志到异步备库，可以根据实际情况再做调整。

```
[RT_TIMER] #和dmarch.ini中的ARCH_TIMER_NAME一致
  TYPE                             = 2
  FREQ_MONTH_WEEK_INTERVAL      = 1
  FREQ_SUB_INTERVAL     = 0
  FREQ_MINUTE_INTERVAL = 0
  START_TIME             = 00:00:00
  END_TIME              = 23:59:59
  DURING_START_DATE       = 2016-02-11 17:36:09
  DURING_END_DATE         = 9999-12-31 23:59:59
  NO_END_DATE_FLAG        = 1
  DESCRIBE                 = RT TIMER
  IS_VALID                 = 1
```

#### 7.6.4.5 其他配置说明

如果配置异步备库时，实时主备环境已经配置完成，这里对实时备库不需要再做其他配置，由于在配置异步备库之前实时主备环境已被正常关闭，此处可以使用 Mount 方式将实时备库重新启动，并启动实时备库的守护进程。

如果同时也在搭建主库和实时备库，则实时备库其他的配置步骤请再参考 7.2.4 配置备库 GRP1\_RT\_02 的配置说明。

### 7.6.5 配置异步备库 GRP1\_LOCAL\_01

#### 7.6.5.1 配置 dm.ini

在 DW\_S2 机器上配置备库的实例名为 GRP1\_LOCAL\_01，dm.ini 参数修改如下：

```
#实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16
INSTANCE_NAME            = GRP1_LOCAL_01
PORT_NUM                = 32143    #数据库实例监听端口
DW_INACTIVE_INTERVAL    = 60     #接收守护进程消息超时时间
ALTER_MODE_STATUS        = 0        #不允许手工方式修改实例模式/状态/OGUID
ENABLE_OFFLINE_TS        = 2        #不允许备库OFFLINE表空间
MAL_INI                    = 1        #打开MAL系统
ARCH_INI                = 1        #打开归档配置
TIMER_INI                = 1        #打开定时器，定时同步归档到异步备库。目的是使GRP1_LOCAL_01能够定时发送归档信息到GRP1_LOCAL_02
RLOG_SEND_APPLY_MON        = 64    #统计最近64次的日志重演信息
```

#### 7.6.5.2 配置 dmmal.ini

同一个守护进程组中，所有主备库必须使用相同的 dmmal.ini 配置文件，这里可以直接拷贝 7.6.3.2 配置 dmmal.ini 的 dmmal.ini 文件到本地的/dm/data/DAMENG/目录中。

#### 7.6.5.3 配置 dmarch.ini

修改 dmarch.ini，配置本地归档和异步归档。

在异步归档配置项中，ARCH\_DEST 表示当前实例需要同步归档数据的目标实例名。

由于需要在当前实例 GRP1\_LOCAL\_01 上级联配置异步备库 GRP1\_LOCAL\_02，因此异步归档的 ARCH\_DEST 配置为 GRP1\_LOCAL\_02。

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE = LOCAL                         #本地归档类型
    ARCH_DEST = /dm/data/DAMENG/arch         #本地归档文件路径
    ARCH_FILE_SIZE = 128                     #单位Mb，本地单个归档文件最大值
    ARCH_SPACE_LIMIT = 0                 #单位Mb，0表示无限制，范围1024~4294967294M
[ARCHIVE_ASYNC] 
    ARCH_TYPE= ASYNC                        #异步归档类型
    ARCH_DEST= GRP1_LOCAL_02                #异步归档目标实例名
    ARCH_TIMER_NAME= RT_TIMER                 #定时器名称，和dmtimer.ini中的名称一致
```

#### 7.6.5.4 配置 dmtimer.ini

配置 dmtimer.ini，用于定时触发实例发送归档日志到异步备库。

下面示例中定时器配置为每天 00:00:00 触发 GRP1\_LOCAL\_01 发送归档日志到异步备库 GRP1\_LOCAL\_02，可以根据实际情况再做调整。

```
[RT_TIMER] #和dmarch.ini中的ARCH_TIMER_NAME一致
 TYPE                             = 2
 FREQ_MONTH_WEEK_INTERVAL    = 1
 FREQ_SUB_INTERVAL             = 0
 FREQ_MINUTE_INTERVAL         = 0
 START_TIME                 = 00:00:00
 END_TIME                      = 23:59:59
 DURING_START_DATE       = 2016-02-11 17:36:09
 DURING_END_DATE         = 9999-12-31 23:59:59
 NO_END_DATE_FLAG        = 1
 DESCRIBE                 = RT TIMER
 IS_VALID                 = 1
```

#### 7.6.5.5 配置 dmwatcher.ini

修改 dmwatcher.ini 配置守护进程，配置为本地守护类型，异步备库不具备故障自动切换等功能，DW\_MODE 配置并不起作用，此处配置为 MANUAL 即可。

```
[GRP1]
    DW_TYPE = LOCAL                         #本地守护类型
    DW_MODE = MANUAL                         #故障手动切换模式
    DW_ERROR_TIME = 10                         #远程守护进程故障认定时间
    INST_ERROR_TIME = 10                    #本地实例故障认定时间
    INST_OGUID = 453331                     #守护系统唯一OGUID值
    INST_INI = /dm/data/DAMENG/dm.ini         #dm.ini配置文件路径
    INST_AUTO_RESTART = 1                    #打开实例的自动启动功能
    INST_STARTUP_CMD = /dm/bin/dmserver     #命令行方式启动
```

#### 7.6.5.6 启动异步备库

以 Mount 方式启动备库

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

一定要以 Mount 方式启动数据库实例，否则系统启动时会重构回滚表空间，生成 Redo 日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动 Open 数据库。

#### 7.6.5.7 设置 OGUID

启动命令行工具 DIsql，登录异步备库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>sp_set_oguid(453331);
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

系统通过 OGUID 值确定一个守护进程组，由用户保证 OGUID 值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的 OGUID 值。

#### 7.6.5.8 修改数据库模式

启动命令行工具 DIsql，登录异备库修改数据库为 STANDBY 模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>alter database standby;
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.6.6 级联配置异步备库 GRP1\_LOCAL\_02

#### 7.6.6.1 配置 dm.ini

在 DW\_S3 机器上配置备库的实例名为 GRP1\_LOCAL\_02。dm.ini 参数修改如下：

#实例名，建议使用“组名\_守护环境\_序号”的命名方式，总长度不能超过 16

```
INSTANCE_NAME      = GRP1_LOCAL_02
PORT_NUM        = 32144 #数据库实例监听端口
DW_INACTIVE_INTERVAL  = 60   #接收守护进程消息超时时间
ALTER_MODE_STATUS    = 0   #不允许手工方式修改实例模式/状态/OGUID
ENABLE_OFFLINE_TS    = 2   #不允许备库OFFLINE表空间
MAL_INI         = 1   #打开MAL系统
ARCH_INI        = 1   #打开归档配置
RLOG_SEND_APPLY_MON  = 64  #统计最近64次的日志重演信息
```

#### 7.6.6.2 配置 dmmal.ini

同一个守护进程组中，所有主备库必须使用相同的 dmmal.ini 配置文件，这里可以直接拷贝 7.6.3.2 配置 dmmal.ini 的 dmmal.ini 文件到本地的/dm/data/DAMENG/目录中。

#### 7.6.6.3 配置 dmarch.ini

本地守护类型的备库只需要配置本地归档。

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE         = LOCAL #本地归档类型
    ARCH_DEST         = /dm/data/DAMENG/arch  #本地归档文件路径
    ARCH_FILE_SIZE      = 128  #单位Mb，本地单个归档文件最大值
    ARCH_SPACE_LIMIT    = 0   #单位Mb，0表示无限制，范围1024~4294967294M
```

#### 7.6.6.4 配置 dmwatcher.ini

修改 dmwatcher.ini 配置守护进程，配置为本地守护类型，异步备库不具备故障自动切换等功能，DW\_MODE 配置并不起作用，此处配置为 MANUAL 即可。

```
[GRP1]

    DW_TYPE = LOCAL                         ##本地守护类型

    DW_MODE = MANUAL                         ##故障手动切换模式

    DW_ERROR_TIME = 10                         ##远程守护进程故障认定时间

    INST_ERROR_TIME = 10                    ##本地实例故障认定时间

    INST_OGUID = 453331                     ##守护系统唯一OGUID值

    INST_INI = /dm/data/DAMENG/dm.ini         ##dm.ini配置文件路径

    INST_AUTO_RESTART = 1                    ##打开实例的自动启动功能

    INST_STARTUP_CMD = /dm/bin/dmserver     ##命令行方式启动
```

#### 7.6.6.5 启动异步备库

以 Mount 方式启动备库

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

一定要以 Mount 方式启动数据库实例，否则系统启动时会重构回滚表空间，生成 Redo 日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动 Open 数据库。

#### 7.6.6.6 设置 OGUID

启动命令行工具 DIsql，登录异步备库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(453331);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

系统通过 OGUID 值确定一个守护进程组，由用户保证 OGUID 值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的 OGUID 值。

#### 7.6.6.7 修改数据库模式

启动命令行工具 DIsql，登录异备库修改数据库为 STANDBY 模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>alter database standby;

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.6.7 配置监视器

在 7.2.5 配置监视器 的配置基础上，需要增加到异步备库守护进程的“IP:PORT”信息，否则监视器无法收到异步备库消息，其他配置项不需要改动。

配置监视器时可以选择配置单实例监视器或配置多实例监视器，下面将分别介绍配置单实例监视器以及多实例监视器时 dmmonitor.ini 配置文件中的配置信息。

#### 7.6.7.1 配置单实例监视器

修改 dmmonitor.ini 配置确认监视器，增加到 GRP1\_LOCAL\_01 和 GRP1\_LOCAL\_02 守护进程的 MON\_DW\_IP 配置项，需要找到 dmmal.ini 中对应的配置项信息，MON\_DW\_IP 中的 IP 信息和 dmmal.ini 配置项中的 MAL\_HOST 一致，PORT 信息和 dmmal.ini 配置项中的 MAL\_DW\_PORT 配置项保持一致。

```
MON_DW_CONFIRM             = 1      #确认监视器模式
MON_LOG_PATH             = /dm/data/log        #监视器日志文件存放路径
MON_LOG_INTERVAL        = 60    #每隔60s定时记录系统信息到日志文件
MON_LOG_FILE_SIZE         = 32    #每个日志文件最大32M
MON_LOG_SPACE_LIMIT     = 0        #不限定日志文件总占用空间
[GRP1]
    MON_INST_OGUID             = 453331 #组GRP1的唯一OGUID值
#以下配置为监视器到组GRP1的守护进程的连接信息，以“IP:PORT”的形式配置
#IP对应dmmal.ini中的MAL_HOST，PORT对应dmmal.ini中的MAL_DW_PORT
    MON_DW_IP                 = 192.168.0.141:52141
    MON_DW_IP                 = 192.168.0.142:52142
#新增到异步备库GRP1_LOCAL_01/GRP1_LOCAL_02守护进程的连接信息
    MON_DW_IP                 = 192.168.0.143:52143
    MON_DW_IP                = 192.168.0.144:52144
```

#### 7.6.7.2 配置多实例监视器

为每个实例配置一个 dmmonitor.ini。众多 dmmonitor.ini 中，除 MON\_ID 和 MON\_NAME 参数不同以外，其他参数应完全一致。

使用配置文件启动多实例监视器实例之前，需要先初始化联机日志文件。初始化联机日志文件的具体操作请查看 [4.2.2.2.2 初始化联机日志文件](data-watch-monitor.md) 。

以其中一个实例的 dmmonitor.ini 为例进行介绍。各实例的 MON\_ID 应与某一个实例配置项中的 MON\_INST\_ID 相同，各实例的 MON\_NAME 与对应的监视器实例名相同。dmmonitor.ini 配置文件中的内容如下：

```
MON_LOG_PATH                = /dm/data/log
MON_LOG_INTERVAL            = 60
MON_LOG_FILE_SIZE            = 32
MON_LOG_SPACE_LIMIT            = 0
MON_DW_CONFIRM                = 1
MON_INST_NUM                = 3            #实例总个数
MON_HB_INTERVAL                = 60         #通信心跳校验间隔
MON_BRO_INTERVAL            = 100         #raft协议中实例通信心跳间隔
MON_VOTE_INTERVAL            = 100         #raft协议中基础投票间隔
MON_ID                        = 1             #当前监视器在监视器系统中的ID
MON_MID                        = 45614        #当前监视器系统的唯一标识
MON_NAME                = MON1  #监视器名

[GRP1]
MON_INST_OGUID                = 453331
MON_DW_IP                 = 192.168.0.141:52141
MON_DW_IP                 = 192.168.0.142:52142
#新增到异步备库GRP1_LOCAL_01/GRP1_LOCAL_02守护进程的连接信息
MON_DW_IP                 = 192.168.0.143:52143
MON_DW_IP                = 192.168.0.144:52144

[MON1] #监视器实例信息
MON_HOST                  = 192.168.0.145         #MON1监视器所在IP 
MON_PORT                  = 8339                     #MON1监视器监听端口
MON_INST_ID                = 1                     #监视器实例在监视器系统中的ID
[MON2]
MON_HOST                  = 192.168.0.146         #MON2监视器所在IP 
MON_PORT                  = 8340                     #MON2监视器监听端口
MON_INST_ID                = 2                     #监视器实例在监视器系统中的ID 
[MON3]
MON_HOST                  = 192.168.0.147         #MON3监视器所在IP 
MON_PORT                  = 8341                     #MON3监视器监听端口
MON_INST_ID                = 3                     #监视器实例在监视器系统中的ID
```

### 7.6.8 启动守护进程

启动异步备库的守护进程：

```
./dmwatcher /dm/data/DAMENG/dmwatcher.ini
```

守护进程启动后，进入 Startup 状态，此时实例处于 Mount 状态，异步备库的守护进程会将本地实例自动 Open，并切换守护进程自身为 Open 状态。

### 7.6.9 启动监视器

修改监视器配置后，需要重新启动监视器：

```
./dmmonitor /dm/data/dmmonitor.ini
```

监视器提供一系列命令，支持当前守护系统状态查看以及故障处理，可输入 help 命令，查看各种命令使用说明，结合实际情况选择使用。

至此，实时主备环境下的异步备库和级联异步备库搭建完成。在实际使用过程中，如果想配置更多异步备库，每个异步备库源实例的配置方式都可以参考主库 GRP1\_RT\_01 和备库 GRP1\_LOCAL\_01 的配置，级联异步备库可参考 GRP1\_LOCAL\_02 的配置。在搭建步骤和各项配置都正确的情况下，在监视器上执行 show 命令，可以监控到异步备库实例和异步备库守护进程都处于 Open 状态。

## 7.7 配置同步备库

同步备库支持多源配置，目的是在实时或即时主备环境中，当主备库切换或者主库故障时，备库接管以后可以继续向同一个同步备库同步数据，因此如果主库配置了同步备库，在所有实时或即时备库上也需要配置相同的同步备库，实时或即时备库只有在切换为主库时才会向其同步数据。

这里以实时主备环境为例，仍然采用 7.2 配置实时主备 小节的配置环境，对同步备库的搭建步骤做举例说明，读写分离集群和 MPP 主备的同步备库搭建步骤是相同的，只需要根据实际情况调整配置项的具体值即可。

这里将配置一个同步备库 GRP1\_SYNC\_01。

### 7.7.1 环境说明

这里采用 7.2 配置实时主备 的实时主备环境，增加一台机器用来部署同步备库，其他环境不变。

新增的机器事先安装了 DM，安装路径为’/dm’，执行程序保存在’/dm/bin’目录中，数据存放路径为’/dm/data’。

新增的同步备库实例名为“GRP1\_SYNC\_01” ，按照“组名\_守护环境\_序号”的建议方式命名，注意总长度不能超过 16。

表7.13 配置环境说明

| **机器名** | **IP\*\*\*\*地址** | **初始状态** | **操作系统** | **备注** |
| --- | --- | --- | --- | --- |
| DW\_S2 | 192.168.1.135 192.168.0.145 | 同步备库 GRP1\_SYNC\_01 | Linux rh6-143.localdomain 2.6.32-220.el6.x86\_64 #1 SMP Wed Nov 9 08:03:13 EST 2011 x86\_64 x86\_64 x86\_64 GNU/Linux | 192.168.1.135 外部服务 IP； 192.168.0.145 内部通信 IP |

### 7.7.2 数据准备

按照 7.1 数据准备 中的方法准备同步备库的数据。

如果实时主备守护环境已经处于运行状态，需要先正常退出主备库实例和守护进程。

### 7.7.3 配置主库 GRP1\_RT\_01

#### 7.7.3.1 配置 dm.ini

保持 7.2.3.1 配置 dm.ini 中的配置不变。

#### 7.7.3.2 配置 dmmal.ini

在 7.2.3.2 配置 dmmal.ini 的基础上，增加同步备库 GRP1\_SYNC\_01 的 MAL 配置项。

```
[MAL_INST3]
      MAL_INST_NAME       = GRP1_SYNC_01 #实例名，和dm.ini中的INSTANCE_NAME一致
      MAL_HOST             = 192.168.0.145    #MAL系统监听TCP连接的IP地址
      MAL_PORT            = 61145            #MAL系统监听TCP连接的端口
      MAL_INST_HOST         = 192.168.1.135    #实例的对外服务IP地址
      MAL_INST_PORT        = 32145    #实例的对外服务端口，和dm.ini中的PORT_NUM一致
     MAL_DW_PORT        = 52145    #实例对应的守护进程监听TCP连接的端口
     MAL_INST_DW_PORT    = 33145 #实例监听守护进程TCP连接的端口
```

#### 7.7.3.3 配置 dmarch.ini

在 7.2.3.3 配置 dmarch.ini 的基础上，增加同步归档的配置项。

```
ARCHIVE_SYNC] 
    ARCH_TYPE                 = SYNC            #同步归档类型
    ARCH_DEST                 = GRP1_SYNC_01    #同步归档目标实例名
    ARCH_RECOVER_TIME        = 60            #同步备库的异步恢复间隔
```

#### 7.7.3.4 其他配置说明

如果配置同步备库时，实时主备环境已经配置完成，这里对主库不需要再做其他配置，由于在配置同步备库之前实时主备环境已经被正常关闭，此处可以使用 Mount 方式将主库重启启动，并启动主库的守护进程。

如果同时也在搭建主库和实时备库，则主库其他的配置步骤请再参考 7.2.3 配置主库 GRP1\_RT\_01 的配置说明。

### 7.7.4 配置备库 GRP1\_RT\_02

主库上配置同步备库，备库上也需要增加相同的同步备库配置，保证备库在切换为主库后可以继续向同一个同步备库同步数据。

#### 7.7.4.1 配置 dm.ini

保持 7.2.4.1 配置 dm.ini 中的配置不变。

#### 7.7.4.2 配置 dmmal.ini

dmmal.ini 中需要增加到同步备库 GRP1\_SYNC\_01 的 MAL 配置项，可以直接拷贝 7.7.3.2 配置 dmmal.ini 修改后的 dmmal.ini 文件到本地/dm/data/DAMENG/目录中。

#### 7.7.4.3 配置 dmarch.ini

在 7.2.4.3 配置 dmarch.ini 的基础上，增加同步归档的配置项。

```
[ARCHIVE_SYNC] 
ARCH_TYPE                 = SYNC            #同步归档类型
ARCH_DEST                 = GRP1_SYNC_01    #同步归档目标实例名
ARCH_RECOVER_TIME        = 60            #同步备库的异步恢复间隔
```

#### 7.7.4.4 其他配置说明

如果配置同步备库时，实时主备环境已经配置完成，这里对实时备库不需要再做其他配置，由于在配置同步备库之前实时主备环境已被正常关闭，此处可以使用 Mount 方式将实时备库重新启动，并启动实时备库的守护进程。

如果同时也在搭建主库和实时备库，则实时备库其他的配置步骤请再参考 7.2.4 配置备库 GRP1\_RT\_02 的配置说明。

### 7.7.5 配置同步备库 GRP1\_SYNC\_01

#### 7.7.5.1 配置 dm.ini

在 DW\_S2 机器上配置备库的实例名为 GRP1\_SYNC\_01，dm.ini 参数修改如下：

```
#实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16
INSTANCE_NAME            = GRP1_SYNC_01
PORT_NUM                = 32145    #数据库实例监听端口
DW_INACTIVE_INTERVAL    = 60     #接收守护进程消息超时时间
ALTER_MODE_STATUS        = 0        #不允许手工方式修改实例模式/状态/OGUID
ENABLE_OFFLINE_TS        = 2        #不允许备库OFFLINE表空间
MAL_INI                    = 1        #打开MAL系统
ARCH_INI                = 1        #打开归档配置
RLOG_SEND_APPLY_MON        = 64    #统计最近64次的日志重演信息
```

#### 7.7.5.2 配置 dmmal.ini

同一个守护进程组中，所有主备库必须使用相同的 dmmal.ini 配置文件，这里可以直接拷贝 7.7.3.2 配置 dmmal.ini 的 dmmal.ini 文件到本地的/dm/data/DAMENG/目录中。

#### 7.7.5.3 配置 dmarch.ini

修改 dmarch.ini，配置本地归档。

```
[ARCHIVE_LOCAL1]
ARCH_TYPE                 = LOCAL    #本地归档类型
ARCH_DEST                 = /dm/data/DAMENG/arch     #本地归档文件路径
ARCH_FILE_SIZE             = 128    #单位Mb，本地单个归档文件最大值
ARCH_SPACE_LIMIT        = 0       #单位Mb，0表示无限制，范围1024~4294967294M
```

#### 7.7.5.4 配置 dmwatcher.ini

修改 dmwatcher.ini 配置守护进程，配置为本地守护类型，同步备库不具备故障自动切换等功能，DW\_MODE 配置并不起作用，此处配置为 MANUAL 即可。

```
[GRP1]
    DW_TYPE             = LOCAL      #本地守护类型
    DW_MODE             = MANUAL    #故障手动切换模式
    DW_ERROR_TIME        = 10        #远程守护进程故障认定时间
    INST_ERROR_TIME      = 10        #本地实例故障认定时间
    INST_OGUID            = 453331    #守护系统唯一OGUID值
    INST_INI              = /dm/data/DAMENG/dm.ini    #dm.ini配置文件路径
    INST_AUTO_RESTART  = 1            #打开实例的自动启动功能
    INST_STARTUP_CMD   = /dm/bin/dmserver    #命令行方式启动
```

#### 7.7.5.5 启动同步备库

以 Mount 方式启动备库

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

一定要以 Mount 方式启动数据库实例，否则系统启动时会重构回滚表空间，生成 Redo 日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动 Open 数据库。

#### 7.7.5.6 设置 OGUID

启动命令行工具 DIsql，登录同步备库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>sp_set_oguid(453331);
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

系统通过 OGUID 值确定一个守护进程组，由用户保证 OGUID 值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的 OGUID 值。

#### 7.7.5.7 修改数据库模式

启动命令行工具 DIsql，登录同步备库修改数据库为 STANDBY 模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1); 
SQL>ALTER DATABASE STANDBY; 
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.7.6 配置监视器

在 7.2.5 配置监视器 的配置基础上，需要增加到同步备库守护进程的“IP:PORT”信息，否则监视器无法收到同步备库消息，其他配置项不需要改动。

配置确认监视器时可以选择配置单实例监视器或配置多实例监视器，下面将分别介绍配置单实例监视器以及多实例监视器时 dmmonitor.ini 配置文件中的配置信息。

#### 7.7.6.1 配置单实例监视器

修改 dmmonitor.ini 配置确认监视器，增加到 GRP1\_SYNC\_01 守护进程的 MON\_DW\_IP 配置项，需要找到 dmmal.ini 中对应的配置项信息，MON\_DW\_IP 中的 IP 信息和 dmmal.ini 配置项中的 MAL\_HOST 一致，PORT 信息和 dmmal.ini 配置项中的 MAL\_DW\_PORT 配置项保持一致。

```
MON_DW_CONFIRM             = 1      #确认监视器模式
MON_LOG_PATH             = /dm/data/log        #监视器日志文件存放路径
MON_LOG_INTERVAL        = 60    #每隔60s定时记录系统信息到日志文件
MON_LOG_FILE_SIZE         = 32    #每个日志文件最大32M
MON_LOG_SPACE_LIMIT     = 0        #不限定日志文件总占用空间
[GRP1]
    MON_INST_OGUID             = 453331 #组GRP1的唯一OGUID值
#以下配置为监视器到组GRP1的守护进程的连接信息，以“IP:PORT”的形式配置
#IP对应dmmal.ini中的MAL_HOST，PORT对应dmmal.ini中的MAL_DW_PORT
    MON_DW_IP                 = 192.168.0.141:52141
    MON_DW_IP                 = 192.168.0.142:52142
#新增到同步备库GRP1_SYNC_01守护进程的连接信息
    MON_DW_IP                 = 192.168.0.145:52145
```

#### 7.7.6.2 配置多实例监视器

为每个实例配置一个 dmmonitor.ini。众多 dmmonitor.ini 中，除 MON\_ID 和 MON\_NAME 参数不同以外，其他参数应完全一致。

使用配置文件启动多实例监视器实例之前，需要先初始化联机日志文件。初始化联机日志文件的具体操作请查看 [4.2.2.2.2 初始化联机日志文件](data-watch-monitor.md) 。

以其中一个实例的 dmmonitor.ini 为例进行介绍。各实例的 MON\_ID 应与某一个实例配置项中的 MON\_INST\_ID 相同，各实例的 MON\_NAME 与对应的监视器实例名相同。dmmonitor.ini 配置文件中的内容如下：

```
MON_LOG_PATH                = /dm/data/log
MON_LOG_INTERVAL            = 60
MON_LOG_FILE_SIZE            = 32
MON_LOG_SPACE_LIMIT            = 0
MON_DW_CONFIRM                = 1
MON_INST_NUM                = 3            #实例总个数
MON_HB_INTERVAL                = 60         #通信心跳校验间隔
MON_BRO_INTERVAL            = 100         #raft协议中实例通信心跳间隔
MON_VOTE_INTERVAL            = 100         #raft协议中基础投票间隔
MON_ID                        = 1             #当前监视器在监视器系统中的ID
MON_MID                        = 45614        #当前监视器系统的唯一标识
MON_NAME                = MON1  #监视器名

[GRP1]
MON_INST_OGUID                = 453331
MON_DW_IP                 = 192.168.0.141:52141
MON_DW_IP                 = 192.168.0.142:52142
#新增到同步备库GRP1_SYNC_01守护进程的连接信息
MON_DW_IP                 = 192.168.0.145:52145

[MON1] #监视器实例信息
MON_HOST                  = 192.168.0.146         #MON1监视器所在IP 
MON_PORT                  = 8339                     #MON1监视器监听端口
MON_INST_ID                = 1                     #监视器实例在监视器系统中的ID
[MON2]
MON_HOST                  = 192.168.0.147         #MON2监视器所在IP 
MON_PORT                  = 8340                     #MON2监视器监听端口
MON_INST_ID                = 2                     #监视器实例在监视器系统中的ID 
[MON3]
MON_HOST                  = 192.168.0.148         #MON3监视器所在IP 
MON_PORT                  = 8341                     #MON3监视器监听端口
MON_INST_ID                = 3                     #监视器实例在监视器系统中的ID
```

### 7.7.7 启动守护进程

启动同步备库的守护进程：

```
./dmwatcher /dm/data/DAMENG/dmwatcher.ini
```

守护进程启动后，进入 Startup 状态，此时实例处于 Mount 状态，同步备库的守护进程会将本地实例自动 Open，并切换守护进程自身为 Open 状态。

### 7.7.8 启动监视器

修改监视器配置后，需要重新启动监视器：

```
./dmmonitor /dm/data/dmmonitor.ini
```

监视器提供一系列命令，支持当前守护系统状态查看以及故障处理，可输入 help 命令，查看各种命令使用说明，结合实际情况选择使用。

至此，实时主备环境下的同步备库搭建完成。在搭建步骤和各项配置都正确的情况下，在监视器上执行 show 命令，可以监控到所有实例都处于 Open 状态，所有守护进程也都处于 Open 状态，即为正常运行状态。

## 7.8 注册服务

如果想让 dmserver、dmwatcher 和 dmmonitor 服务开机自启动，需要手动注册服务，注册步骤必须用 root 用户进行，注册完成后重启机器时，就会自动启动 dmserver、dmwatcher 和 dmmonitor 服务。其中，因为确认监视器一直处于工作状态，所以确认监视器需要注册 dmmonitor 服务，自动启动；非确认监视器是在查看信息时才使用，届时手动启动控制台 dmmonitor 服务即可，可以不用注册 dmmonitor 服务。详细的配置请参考《DM8\_Linux 服务脚本使用手册》。

## 7.9 动态增加读写分离集群节点

当需要进行系统扩容，希望系统运行不中断，或者影响运行的时间尽可能短时，可通过动态增加集群节点的方式进行。下面举例对读写分离集群进行动态增加节点。

本例是在 7.3 配置读写分离集群 的基础上，再增加一个备库，实例名为 GRP1\_RWW\_04。

表7.14 配置环境说明

| **机器名** | **IP 地址** | **初始状态** | **操作系统** | **备注** |
| --- | --- | --- | --- | --- |
| DW\_S3 | 192.168.1.134 192.168.0.144 | 备库 GRP1\_RWW\_04 | Linux rh6 x86\_64 | 192.168.1.134 外部服务 IP；   192.168.0.144 内部通信 IP |

详细步骤如下：

### 7.9.1 数据准备

1.对主库进行联机备份操作：

```
SQL> BACKUP DATABASE BACKUPSET 'BACKUP_FILE_01';
```

2.初始化备机数据库

```
./dminit path=/dm/data/ SYSDBA_PWD=DMdba_123 SYSAUDITOR_PWD=DMauditor_123
```

3.还原恢复新增备库

拷贝生成的备份集目录 BACKUP\_FILE\_01 到 144 上/dm/data/目录，使用 DMRMAN 工具脱机还原。

```
./dmrman CTLSTMT="RESTORE DATABASE '/dm/data/DAMENG/dm.ini' FROM BACKUPSET '/dm/data/BACKUP_FILE_01'"
./dmrman CTLSTMT="RECOVER DATABASE '/dm/data/DAMENG/dm.ini' FOR STANDBY FROM BACKUPSET '/dm/data/BACKUP_FILE_01'"
./dmrman  CTLSTMT="RECOVER DATABASE '/dm/data/DAMENG/dm.ini' UPDATE DB_MAGIC"
```

### 7.9.2 配置新备库

#### 7.9.2.1 配置 dm.ini

在 DW\_S3 机器上配置备库的实例名为 GRP1\_RWW\_04，dm.ini 参数修改如下：

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP1_RWW_04

PORT_NUM = 32144                 ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60         ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0             ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2             ##不允许备库OFFLINE表空间

MAL_INI = 1                     ##打开MAL系统

ARCH_INI = 1                    ##打开归档配置

RLOG_SEND_APPLY_MON = 64         ##统计最近64次的日志重演信息
```

#### 7.9.2.2 配置 dmmal.ini

拷贝一份原系统 dmmal.ini 文件，并加上自己一项，最终配置如下：

```
MAL_CHECK_INTERVAL = 5                 ##MAL链路检测时间间隔

MAL_CONN_FAIL_INTERVAL = 5             ##判定MAL链路断开的时间

[MAL_INST1]

    MAL_INST_NAME = GRP1_RWW_01     ##实例名，和dm.ini中的INSTANCE_NAME一致

    MAL_HOST = 192.168.0.141         ##MAL系统监听TCP连接的IP地址

    MAL_PORT = 61141                 ##MAL系统监听TCP连接的端口

    MAL_INST_HOST = 192.168.1.131     ##实例的对外服务IP地址

    MAL_INST_PORT = 32141            ##实例的对外服务端口，和dm.ini中的PORT_NUM一致

    MAL_DW_PORT = 52141             ##实例对应的守护进程监听TCP连接的端口

    MAL_INST_DW_PORT = 33141         ##实例监听守护进程TCP连接的端口

[MAL_INST2]

    MAL_INST_NAME = GRP1_RWW_02

    MAL_HOST = 192.168.0.142

    MAL_PORT = 61142

    MAL_INST_HOST = 192.168.1.132

    MAL_INST_PORT = 32142

    MAL_DW_PORT = 52142

    MAL_INST_DW_PORT = 33142

[MAL_INST3]

    MAL_INST_NAME = GRP1_RWW_03

    MAL_HOST = 192.168.0.143

    MAL_PORT = 61143

    MAL_INST_HOST = 192.168.1.133

    MAL_INST_PORT = 32143

    MAL_DW_PORT = 52143

    MAL_INST_DW_PORT = 33143

[MAL_INST4]

    MAL_INST_NAME = GRP1_RWW_04

    MAL_HOST = 192.168.0.144

    MAL_PORT = 61144

    MAL_INST_HOST = 192.168.1.134

    MAL_INST_PORT = 32144

    MAL_DW_PORT = 52144

    MAL_INST_DW_PORT = 33144
```

#### 7.9.2.3 配置 dmarch.ini

修改 dmarch.ini，配置本地归档和即时归档。

```
[ARCHIVE_TIMELY1]

    ARCH_TYPE = TIMELY                     ##即时归档类型

    ARCH_DEST = GRP1_RWW_01             ##即时归档目标实例名

[ARCHIVE_TIMELY2]

    ARCH_TYPE = TIMELY                     ##即时归档类型

    ARCH_DEST = GRP1_RWW_02             ##即时归档目标实例名

[ARCHIVE_TIMELY3]

    ARCH_TYPE = TIMELY                     ##即时归档类型

    ARCH_DEST = GRP1_RWW_03             ##即时归档目标实例名

[ARCHIVE_LOCAL1]

    ARCH_TYPE = LOCAL                     ##本地归档类型

    ARCH_DEST = /dm/data/DAMENG/arch     ##本地归档文件存放路径

    ARCH_FILE_SIZE = 128                 ##单位Mb，本地单个归档文件最大值

    ARCH_SPACE_LIMIT = 0                 ##单位Mb，0表示无限制，范围1024~4294967294M
```

#### 7.9.2.4 配置 dmwatcher.ini

修改 dmwatcher.ini 配置守护进程，配置为全局守护类型，使用自动切换模式。

```
[GRP1]

    DW_TYPE = GLOBAL                     ##全局守护类型

    DW_MODE = AUTO                         ##自动切换模式

    DW_ERROR_TIME = 10                     ##远程守护进程故障认定时间

    INST_RECOVER_TIME = 60                 ##主库守护进程启动恢复的间隔时间

    INST_ERROR_TIME = 10                 ##本地实例故障认定时间

    INST_OGUID = 453332                 ##守护系统唯一OGUID值

    INST_INI = /dm/data/DAMENG/dm.ini     ##dm.ini配置文件路径

    INST_AUTO_RESTART = 1                ##打开实例的自动拉起功能

    INST_STARTUP_CMD = /dm/bin/dmserver ##命令行方式启动

    RLOG_SEND_THRESHOLD = 0             ##指定主库发送日志到备库的时间阈值，默认关闭

    RLOG_APPLY_THRESHOLD = 0             ##指定备库重演日志的时间阈值，默认关闭
```

#### 7.9.2.5 启动备库

以 Mount 方式启动备库

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

#### 7.9.2.6 设置 OGUID

启动命令行工具 DIsql，登录备库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(453332);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

#### 7.9.2.7 修改数据库模式

启动命令行工具 DIsql，登录备库修改数据库为 STANDBY 模式:

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>alter database standby;

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.9.3 动态添加 MAL 配置

本小节的步骤需要分别连接原系统中每个数据库单独执行，如果是 DMDSC 集群，则需要连接集群内的每一个节点执行：

动态增加 MAL 中 GRP1\_RWW\_04 的相关配置信息：

```
SF_MAL_CONFIG(1,0);

SF_MAL_INST_ADD('MAL_INST4','GRP1_RWW_04','192.168.0.144',61144,'192.168.1.134',32144,52144,0,33144);

SF_MAL_CONFIG_APPLY();

SF_MAL_CONFIG(0,0);
```

### 7.9.4 动态添加归档配置

动态添加归档配置步骤如下：

1. 关闭原系统中所有数据库的守护进程和监视器

动态添加归档要求数据库处于 MOUNT 状态，守护进程处于活动状态下不允许用户手动修改模式状态，因此需要先关闭守护进程，同时也是为了防止手动切换 MOUNT 状态后又被守护进程通知自动 OPEN，另外监视器配置也需要修改，因此在这里一并关闭。

关闭顺序为：

1. 关闭监视器
2. 关闭备库守护进程
3. 关闭主库守护进程
2. 手动修改原系统中所有数据库为 MOUNT 状态

必须先修改主库，再修改备库，否则可能会引发主备数据同步失败导致主库挂起。

```
//临时修改ALTER_MODE_STATUS，允许用户手动修改模式状态，动态添加完毕后需要再改回原值
SQL> SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1); 
//临时关闭守护进程活动状态检测，允许用户手动修改模式状态，动态添加完毕后需要再改回原值
SQL> SP_SET_PARA_VALUE(1, 'DW_INACTIVE_INTERVAL', 0);
//修改数据库为MOUNT状态
SQL> ALTER DATABASE MOUNT;
```
3. 动态添加归档节点

分别连接原系统中的所有数据库执行，动态添加 dmarch.ini 中归档节点，如果是 DMDSC 集群，则需要连接集群内的每一个节点执行。

```
SQL> ALTER DATABASE ADD ARCHIVELOG 'DEST=GRP1_RWW_04, TYPE=TIMELY';
```
4. 手动修改原系统中所有数据库为 OPEN 状态

必须先修改备库，再修改主库，否则可能会引发主备数据同步失败导致主库挂起。

```
//修改数据库为OPEN状态
SQL> ALTER DATABASE OPEN FORCE;
//将ALTER_MODE_STATUS改回原值
SQL> SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0); 
//将DW_INACTIVE_INTERVAL改回原值，本例中为60
SQL> SP_SET_PARA_VALUE(1, 'DW_INACTIVE_INTERVAL', 60);
```

### 7.9.5 修改监视器 dmmonitor.ini

在 dmmonitor.ini 中添加新增的备库 GRP1\_RWW\_04：

```
MON_DW_IP = 192.168.0.144:52144
```

### 7.9.6 启动所有守护进程以及监视器

分别启动主库和备库（包括 GRP1\_RWW\_04）的所有守护进程，最后启动监视器。

## 7.10 动态增加实时备库

当需要进行系统扩容，希望系统运行不中断，或者影响运行的时间尽可能短时，可通过动态增加节点的方式进行。下面举例对实时主备进行动态增加节点。

本例在 7.2 配置实时主备集群 的基础上，再增加一个备库，实例名为 GRP1\_RT\_03。

表7.15 配置环境说明

| **机器名** | **IP 地址** | **初始状态** | **操作系统** | **备注** |
| --- | --- | --- | --- | --- |
| DW\_S2 | 192.168.1.133 192.168.0.143 | 备库 GRP1\_RT\_03 | Linux rh6-141.test 2.6.32-220.el6.x86\_64 | 192.168.1.133 外部服务 IP； 192.168.0.143 内部通信 IP |

详细步骤如下：

### 7.10.1 数据准备

1.对主库进行联机备份操作：

```
SQL> BACKUP DATABASE BACKUPSET 'BACKUP_FILE_01';
```

2.初始化备机数据库

```
./dminit path=/dm/data/ SYSDBA_PWD=DMdba_123 SYSAUDITOR_PWD=DMauditor_123
```

3.还原恢复新增备库

拷贝生成的备份集目录 BACKUP\_FILE\_01 到 143 上/dm/data/目录，使用 DMRMAN 工具脱机还原。

```
./dmrman CTLSTMT="RESTORE DATABASE '/dm/data/DAMENG/dm.ini' FROM BACKUPSET '/dm/data/BACKUP_FILE_01'"
./dmrman CTLSTMT="RECOVER DATABASE '/dm/data/DAMENG/dm.ini' FOR STANDBY FROM BACKUPSET '/dm/data/BACKUP_FILE_01'"
./dmrman  CTLSTMT="RECOVER DATABASE '/dm/data/DAMENG/dm.ini' UPDATE DB_MAGIC"
```

### 7.10.2 配置新备库

#### 7.10.2.1 配置 dm.ini

在 DW\_S3 机器上配置备库的实例名为 GRP1\_RT\_03，dm.ini 参数修改如下：

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP1_RT_03

PORT_NUM = 32143                 ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60         ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0             ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2             ##不允许备库OFFLINE表空间

MAL_INI = 1                     ##打开MAL系统

ARCH_INI = 1                     ##打开归档配置

RLOG_SEND_APPLY_MON = 64         ##统计最近64次的日志重演信息
```

#### 7.10.2.2 配置 dmmal.ini

```
拷贝一份原系统dmmal.ini文件，并加上自己一项，最终配置如下：

MAL_CHECK_INTERVAL = 5                 ##MAL链路检测时间间隔

MAL_CONN_FAIL_INTERVAL = 5             ##判定MAL链路断开的时间

[MAL_INST1]

    MAL_INST_NAME = GRP1_RT_01         ##实例名，和dm.ini中的INSTANCE_NAME一致

    MAL_HOST = 192.168.0.141        ##MAL系统监听TCP连接的IP地址

    MAL_PORT = 61141                 ##MAL系统监听TCP连接的端口

    MAL_INST_HOST = 192.168.1.131     ##实例的对外服务IP地址

    MAL_INST_PORT = 32141             ##实例的对外服务端口，和dm.ini中的PORT_NUM一致

    MAL_DW_PORT = 52141             ##实例本地的守护进程监听TCP连接的端口

    MAL_INST_DW_PORT = 33141         ##实例监听守护进程TCP连接的端口

[MAL_INST2]

    MAL_INST_NAME = GRP1_RT_02

    MAL_HOST = 192.168.0.142

    MAL_PORT = 61142

    MAL_INST_HOST = 192.168.1.132

    MAL_INST_PORT = 32142

    MAL_DW_PORT = 52142

    MAL_INST_DW_PORT = 33142

[MAL_INST3]

    MAL_INST_NAME = GRP1_RT_03

    MAL_HOST = 192.168.0.143

    MAL_PORT = 61142

    MAL_INST_HOST = 192.168.1.133

    MAL_INST_PORT = 32143

    MAL_DW_PORT = 52143

    MAL_INST_DW_PORT = 33143
```

#### 7.10.2.3 配置 dmarch.ini

修改 dmarch.ini，配置本地归档和即时归档。

```
[ARCHIVE_REALTIME]

ARCH_TYPE = REALTIME                 ##实时归档类型

ARCH_DEST = GRP1_RT_01                 ##实时归档目标实例名

[ARCHIVE_REALTIME2]

ARCH_TYPE = REALTIME                ##实时归档类型

ARCH_DEST = GRP1_RT_02                 ##实时归档目标实例名

[ARCHIVE_LOCAL1]

ARCH_TYPE = LOCAL                     ##本地归档类型

ARCH_DEST = /dm/data/DAMENG/arch    ##本地归档文件存放路径

ARCH_FILE_SIZE = 128                 ##单位Mb，本地单个归档文件最大值

ARCH_SPACE_LIMIT = 0                 ##单位Mb，0表示无限制，范围1024~4294967294M
```

#### 7.10.2.4 配置 dmwatcher.ini

修改 dmwatcher.ini 配置守护进程，配置为全局守护类型，使用自动切换模式。

```
[GRP1]

    DW_TYPE = GLOBAL                     ##全局守护类型

    DW_MODE = AUTO                         ##自动切换模式

    DW_ERROR_TIME = 10                     ##远程守护进程故障认定时间

    INST_RECOVER_TIME = 60                ##主库守护进程启动恢复的间隔时间

    INST_ERROR_TIME = 10                 ##本地实例故障认定时间

    INST_OGUID = 453331                 ##守护系统唯一OGUID值

    INST_INI = /dm/data/DAMENG/dm.ini     ##dm.ini配置文件路径

    INST_AUTO_RESTART = 1                 ##打开实例的自动拉起功能

    INST_STARTUP_CMD = /dm/bin/dmserver ##命令行方式启动

    RLOG_SEND_THRESHOLD = 0             ##指定主库发送日志到备库的时间阈值，默认关闭

    RLOG_APPLY_THRESHOLD = 0             ##指定备库重演日志的时间阈值，默认关闭
```

#### 7.10.2.5 启动备库

以 Mount 方式启动备库

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

#### 7.10.2.6 设置 OGUID

启动命令行工具 DIsql，登录备库设置 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>sp_set_oguid(453331);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

#### 7.10.2.7 修改数据库模式

启动命令行工具 DIsql，登录备库修改数据库为 STANDBY 模式:

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>alter database standby;

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.10.3 动态添加 MAL 配置

本小节的步骤需要分别连接原系统中每个实例单独执行：

动态增加 MAL 中 GRP1\_RT\_03 的相关配置信息：

```
SF_MAL_CONFIG(1,0);

SF_MAL_INST_ADD('MAL_INST3','GRP1_RT_03','192.168.0.143',61142,'192.168.1.133',32143,52143,0,33143);

SF_MAL_CONFIG_APPLY();

SF_MAL_CONFIG(0,0);
```

### 7.10.4 动态添加归档配置

动态添加归档配置步骤如下：

1. 关闭原系统中所有实例的守护进程和监视器

动态添加归档要求数据库处于 MOUNT 状态，守护进程处于活动状态下不允许用户手动修改模式状态，因此需要先关闭守护进程，同时也是为了防止手动切换 MOUNT 状态后又被守护进程通知自动 Open，另外监视器配置也需要修改，因此在这里一并关闭。

关闭顺序为：

1. 关闭监视器
2. 关闭备库守护进程
3. 关闭主库守护进程
2. 手动修改原系统中所有实例为 MOUNT 状态

必须先修改主库，再修改备库，否则可能会引发主备数据同步失败导致主库挂起。

```
//临时修改ALTER_MODE_STATUS，允许用户手动修改模式状态，动态添加完毕后需要再改回原值
SQL> SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1); 
//临时关闭守护进程活动状态检测，允许用户手动修改模式状态，动态添加完毕后需要再改回原值
SQL> SP_SET_PARA_VALUE(1, 'DW_INACTIVE_INTERVAL', 0);
//修改数据库为MOUNT状态
SQL> ALTER DATABASE MOUNT;
```
3. 动态添加归档节点

分别连接原系统中的所有实例，动态添加 dmarch.ini 中归档节点。

```
SQL> ALTER DATABASE ADD ARCHIVELOG 'DEST= GRP1_RT_03, TYPE= REALTIME';
```
4. 手动修改原系统中所有实例为 OPEN 状态

必须先修改备库，再修改主库，否则可能会引发主备数据同步失败导致主库挂起。

```
//修改数据库为OPEN状态
SQL> ALTER DATABASE OPEN FORCE;
//将ALTER_MODE_STATUS改回原值
SQL> SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0); 
//将DW_INACTIVE_INTERVAL改回原值，本例中为60
SQL> SP_SET_PARA_VALUE(1, 'DW_INACTIVE_INTERVAL', 60);
```

### 7.10.5 修改监视器 dmmonitor.ini

在 dmmonitor.ini 中添加新增的备库 GRP1\_RT\_03：

```
MON_DW_IP = 192.168.0.143:52143
```

### 7.10.6 启动所有守护进程以及监视器

分别启动主库和备库（包括 GRP1\_RT\_03）的所有守护进程，最后启动监视器。

## 7.11 动态增加实时 DMDSC 备库

当需要进行系统扩容，希望系统运行不中断，或者影响运行的时间尽可能短时，可通过动态增加节点的方式进行。下面举例对实时主备进行动态增加 DSC 备库节点。

本例在 7.2 配置实时主备集群 的基础上，再增加一个 DMDSC 集群备库，DMDSC 集群的两个节点实例名分别命名为“GRP1\_RT\_DSC01”、“GRP1\_RT\_DSC02”。

注意，本章节内容仅适用于原有的数据守护系统中不存在 DMDSC 集群的情况。

表7.16 配置环境说明

| **机器名** | **IP 地址** | **初始状态** | **操作系统** | **备注** |
| --- | --- | --- | --- | --- |
| DW\_S2 | 192.168.1.133 192.168.0.143 | 备库 GRP1\_RT\_DSC01 GRP1\_RT\_DSC02 | Linux rh6-141.test 2.6.32-220.el6.x86\_64 | 192.168.1.133 外部服务 IP；   192.168.0.143 内部通信 IP |

详细步骤如下：

### 7.11.1 数据准备

1.对主库进行联机备份操作：

```
SQL> BACKUP DATABASE BACKUPSET 'BACKUP_FILE_01';
```

2.搭建 DMDSC 环境作为备库

使用 DMDSC 集群手册《DM8 数据共享集群》或者相应脚本搭建好两节点 DMDSC 集群环境，DMDSC 实例名分别为 GRP1\_RT\_DSC01、GRP1\_RT\_DSC02。

注意 dmcss 对 DMServer 的自动拉起功能先不要打开，避免影响到配置过程。搭建完成后，正常退出 DMDSC 集群的两个 DMServer 节点实例，不需要退出 dmcss 和 dmasmsvr。

3.还原恢复新增备库

拷贝生成的备份集目录 BACKUP\_FILE\_01 到 143 上/dm/data/目录，使用 DMRMAN 工具脱机还原。

```
./dmrman use_ap=2 dcr_ini=/dm/data/DSC/conf/dmdcr1.ini
RMAN>RESTORE DATABASE '/dm/data/DSC/DSC01/dm.ini' FROM BACKUPSET '/dm/data/BACKUP_FILE_01'
RMAN>RECOVER DATABASE '/dm/data/DSC/DSC01/dm.ini' FOR STANDBY FROM BACKUPSET '/dm/data/BACKUP_FILE_01'
RMAN>RECOVER DATABASE '/dm/data/DSC/DSC01/dm.ini' UPDATE DB_MAGIC
```

### 7.11.2 配置新备库 DMDSC 环境

#### 7.11.2.1 配置 dm.ini

依次配置 DMDSC 备库所有节点的 dm.ini 文件，修改数据守护相关的参数配置。

**（1）配置 GRP1\_RT\_DSC01 的 dm.ini 文件**

```
##实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16

INSTANCE_NAME = GRP1_RT_DSC01

PORT_NUM = 31431                ##数据库实例监听端口

DW_INACTIVE_INTERVAL = 60         ##接收守护进程消息超时时间

ALTER_MODE_STATUS = 0             ##不允许手工方式修改实例模式/状态/OGUID

ENABLE_OFFLINE_TS = 2             ##不允许备库OFFLINE表空间

MAL_INI = 1                     ##打开MAL系统

ARCH_INI = 1                    ##打开归档配置

RLOG_SEND_APPLY_MON = 64         ##统计最近64次的日志发送信息
```

**（2）配置 GRP1\_RT\_DSC02 的 dm.ini 文件**

```
INSTANCE_NAME = GRP1_RT_DSC02

PORT_NUM = 31432

DW_INACTIVE_INTERVAL = 60

ALTER_MODE_STATUS = 0

ENABLE_OFFLINE_TS = 2

MAL_INI = 1

ARCH_INI = 1

RLOG_SEND_APPLY_MON = 64
```

#### 7.11.2.2 配置 dmmal.ini

在 DMDSC 集群的 dmmal.ini 文件基础上，增加主库 GRP1\_RT\_01、备库 GRP1\_RT\_02 的配置项。

```
MAL_CHECK_INTERVAL = 5                 ##MAL链路检测时间间隔

MAL_CONN_FAIL_INTERVAL = 5             ##判定MAL链路断开的时间

[MAL_INST1]

    MAL_INST_NAME = GRP1_RT_01         ##实例名，和dm.ini中的INSTANCE_NAME一致

    MAL_HOST = 192.168.0.141         ##MAL系统监听TCP连接的IP地址

    MAL_PORT = 61141                 ##MAL系统监听TCP连接的端口

    MAL_INST_HOST = 192.168.1.131     ##实例的对外服务IP地址

    MAL_INST_PORT = 32141             ##实例的对外服务端口，和dm.ini中的PORT_NUM一致

    MAL_DW_PORT = 52141             ##实例本地的守护进程监听TCP连接的端口

    MAL_INST_DW_PORT = 33141         ##实例监听守护进程TCP连接的端口

[MAL_INST2]

    MAL_INST_NAME = GRP1_RT_02

    MAL_HOST = 192.168.0.142

    MAL_PORT = 61142

    MAL_INST_HOST = 192.168.1.132

    MAL_INST_PORT = 32142

    MAL_DW_PORT = 52142

    MAL_INST_DW_PORT = 33142

[MAL_INST3]

    MAL_INST_NAME = GRP1_RT_DSC01     ##实例名，和dm.ini中的INSTANCE_NAME一致

    MAL_HOST = 192.168.0.143         ##MAL系统监听TCP连接的IP地址

    MAL_PORT = 8338                 ##MAL系统监听TCP连接的端口

    MAL_INST_HOST = 192.168.1.133     ##实例的对外服务IP地址

    MAL_INST_PORT = 31431             ##实例的对外服务端口，和dm.ini中的PORT_NUM一致

    MAL_DW_PORT = 3567                 ##实例本地的守护进程监听TCP连接的端口

    MAL_INST_DW_PORT = 4567         ##实例监听守护进程TCP连接的端口

[MAL_INST4]

    MAL_INST_NAME = GRP1_RT_DSC02

    MAL_HOST = 192.168.0.143

    MAL_PORT = 8339

    MAL_INST_HOST = 192.168.1.133

    MAL_INST_PORT = 31432

    MAL_DW_PORT = 3568
```

#### 7.11.2.3 配置 dmarch.ini

编辑各个节点的 dmarch.ini 文件，增加本地归档、实时归档及远程归档配置。

**（1）修改 GRP1\_RT\_DSC01 的 dmarch.ini 文件**

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE            = LOCAL 
    ARCH_DEST            = +DMDATA/DSC/DSC01/arch
    ARCH_FILE_SIZE        = 128 
    ARCH_SPACE_LIMIT    = 0 

[ARCHIVE_REMOTE]
    ARCH_TYPE            = REMOTE
    ARCH_DEST            = GRP1_RT_DSC02
    ARCH_INCOMING_PATH  = +DMDATA/DSC/DSC02/arch

[ARCHIVE_REALTIME1] 
ARCH_TYPE             = REALTIME
ARCH_DEST             = GRP1_RT_01

[ARCHIVE_REALTIME2] 
ARCH_TYPE             = REALTIME
ARCH_DEST             = GRP1_RT_02
```

**（2）修改 GRP1\_RT\_DSC02 的 dmarch.ini 文件**

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE            = LOCAL
    ARCH_DEST            = +DMDATA/DSC/DSC02/arch
    ARCH_FILE_SIZE        = 128
    ARCH_SPACE_LIMIT    = 0

[ARCHIVE_REMOTE]
    ARCH_TYPE            = REMOTE
    ARCH_DEST            = GRP1_RT_DSC01
    ARCH_INCOMING_PATH  = +DMDATA/DSC/DSC01/arch

[ARCHIVE_REALTIME1] 
    ARCH_TYPE             = REALTIME
    ARCH_DEST             = GRP1_RT_01

[ARCHIVE_REALTIME2] 
    ARCH_TYPE             = REALTIME
    ARCH_DEST             = GRP1_RT_02
```

#### 7.11.2.4 配置 dmwatcher.ini

依次配置每个节点实例的 dmwatcher.ini 文件，放到各自 dm.ini 中指定的 CONFIG\_PATH 目录下。

另外要注意，DMDSC 集群各节点实例的自动拉起是由各自本地的 dmcss 执行的，不是由守护进程执行，如果要打开 DMDSC 集群的自动拉起，需要再去配置 dmdcr.ini 中的自动拉起参数，为避免 dmcss 在所有配置步骤完成之前提前将 DMServer 自动拉起，这里先不修改 dmdcr.ini 配置，放到后面步骤中修改。

**（1）配置 GRP1\_RT\_DSC01 的 dmwatcher.ini 文件**

```
[GRP1]

    DW_TYPE = GLOBAL                         ##全局守护类型

    DW_MODE = MANUAL                         ##手动切换模式

    DW_ERROR_TIME = 60                         ##远程守护进程故障认定时间

    INST_RECOVER_TIME = 60                     ##主库守护进程启动恢复的间隔时间

    INST_ERROR_TIME = 30                     ##本地实例故障认定时间

    INST_INI = /dm/data/DSC/DSC01/dm.ini     ##dm.ini配置文件路径

    DCR_INI = /dm/data/DSC/conf/dmdcr1.ini    ##dmdcr.ini配置文件路径

    INST_OGUID = 453331                     ##守护系统唯一OGUID值

    INST_STARTUP_CMD = /dm/bin/dmserver     ##命令行方式启动

    INST_AUTO_RESTART = 0                     ##关闭实例的自动启动功能

    RLOG_SEND_THRESHOLD = 0                 ##指定主库发送日志到备库的时间阈值，默认关闭

    RLOG_APPLY_THRESHOLD = 0                 ##指定备库重演日志的时间阈值，默认关闭
```

**（2）配置 GRP1\_RT\_DSC02 的 dmwatcher.ini 文件**

```
[GRP1]

    DW_TYPE = GLOBAL

    DW_MODE = MANUAL

    DW_ERROR_TIME = 60

    INST_RECOVER_TIME = 60

    INST_ERROR_TIME = 30

    INST_INI = /dm/data/DSC/DSC02/dm.ini

    DCR_INI = /dm/data/DSC/conf/dmdcr2.ini

    INST_OGUID = 453331

    INST_STARTUP_CMD = /dm/bin/dmserver

    INST_AUTO_RESTART = 0

    RLOG_SEND_THRESHOLD = 0

    RLOG_APPLY_THRESHOLD = 0
```

> **注意**
> 
> 实际配置时，相关的端口配置和OGUID值建议不要和手册示例使用完全相同的值，避免多个用户在同一个环境下搭建不同的数据守护系统，出现消息混乱或者端口冲突等问题。

#### 7.11.2.5 配置 dmdcr.ini

DMDSC 集群中 DMServer 的自动拉起是由 dmcss 执行的，如果不需要打开 dmcss 的自动拉起功能，则可以跳过此章节。

否则需要修改 dmdcr.ini 中的自动拉起配置参数，此参数修改完成后，需要重启 dmcss 才可以生效，为了避免重启 dmcss 引发 dmasmsvr 被强制关闭，这里先将 dmcss 和 dmasmsvr 都正常退出。

**1\. 打开 GRP1\_RT\_DSC01 的自动拉起参数**

修改对应 dmcss 的 dmdcr.ini 文件，打开自动拉起参数。

```
#打开DB重启参数，命令行方式启动

DMDCR_DB_RESTART_INTERVAL = 60

DMDCR_DB_STARTUP_CMD = /dm/bin/dmserver path=/dm/data/DSC/DSC01/dm.ini

dcr_ini=/dm/data/DSC/conf/dmdcr1.ini mount
```

**2\. 打开 GRP1\_RT\_DSC02 的自动拉起参数**

修改对应 dmcss 的 dmdcr.ini 文件，打开自动拉起参数。

```
##打开DB重启参数，命令行方式启动

DMDCR_DB_RESTART_INTERVAL = 60

DMDCR_DB_STARTUP_CMD = /dm/bin/dmserver path=/dm/data/DSC/DSC02/dm.ini

dcr_ini=/dm/data/DSC/conf/dmdcr2.ini mount
```

**3\. 重启 dmcss 和 dmasmsvr**

```
./dmcss dcr_ini=/dm/data/DSC/conf/dmdcr1.ini

./dmcss dcr_ini=/dm/data/DSC/conf/dmdcr2.ini

./dmasmsvr dcr_ini=/dm/data/DSC/conf/dmdcr1.ini

./dmasmsvr dcr_ini=/dm/data/DSC/conf/dmdcr2.ini
```

#### 7.11.2.6 启动 DMDSC 备库

启动 DMDSC 集群的两个 DMServer 实例，注意实例都要使用 Mount 方式启动。

如果 dmcss 打开有自动拉起功能，也可以等待 dmcss 将本地的 DMServer 实例自动拉起（要保证以 Mount 方式拉起）。

手动启动命令如下：

```
./dmserver /dm/data/DSC/DSC01/dm.ini DCR_INI=/dm/data/DSC/conf/dmdcr1.ini mount

./dmserver /dm/data/DSC/DSC02/dm.ini DCR_INI=/dm/data/DSC/conf/dmdcr2.ini mount
```

#### 7.11.2.7 设置 OGUID

启动命令行工具 DIsql，连接 DMDSC 集群中的任意一个节点，设置 DMDSC 主库的 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);

SQL>SP_SET_OGUID(453331);

SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

#### 7.11.2.8 修改数据库模式

启动命令行工具 DIsql，连接 DMDSC 集群中的控制节点，修改 DMDSC 库为 STANDBY 模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>ALTER DATABASE STANDBY;
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

### 7.11.3 动态添加 MAL 配置

本小节的步骤需要分别连接原系统中每个实例单独执行：

动态增加 MAL 中 GRP1\_RT\_DSC01、GRP1\_RT\_DSC02 的相关配置信息：

```
SF_MAL_CONFIG(1,0);

SF_MAL_INST_ADD('MAL_INST3','GRP1_RT_DSC01','192.168.0.143',8338,'192.168.1.133',31431,3567,0,4567);

SF_MAL_INST_ADD('MAL_INST4','GRP1_RT_DSC02','192.168.0.143',8339,'192.168.1.133',31432, 3568,0,4568);

SF_MAL_CONFIG_APPLY();

SF_MAL_CONFIG(0,0);
```

### 7.11.4 动态添加归档配置

动态添加归档配置步骤如下：

1. 关闭原系统中所有实例的守护进程和监视器

动态添加归档要求数据库处于 MOUNT 状态，守护进程处于活动状态下不允许用户手动修改模式状态，因此需要先关闭守护进程，同时也是为了防止手动切换 MOUNT 状态后又被守护进程通知自动 Open，另外监视器配置也需要修改，因此在这里一并关闭。

关闭顺序为：

1. 关闭监视器
2. 关闭备库守护进程
3. 关闭主库守护进程
2. 手动修改原系统中所有实例为 MOUNT 状态

必须先修改主库，再修改备库，否则可能会引发主备数据同步失败导致主库挂起。

```
//临时修改ALTER_MODE_STATUS，允许用户手动修改模式状态，动态添加完毕后需要再改回原值
SQL> SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1); 
//临时关闭守护进程活动状态检测，允许用户手动修改模式状态，动态添加完毕后需要再改回原值
SQL> SP_SET_PARA_VALUE(1, 'DW_INACTIVE_INTERVAL', 0);
//修改数据库为MOUNT状态
SQL> ALTER DATABASE MOUNT;
```
3. 动态添加归档节点

分别连接原系统中的所有实例，动态添加 dmarch.ini 中归档配置项。

```
SQL> ALTER DATABASE ADD ARCHIVELOG 'DEST=GRP1_RT_DSC01/GRP1_RT_DSC02, TYPE= REALTIME';
```
4. 手动修改原系统中所有实例为 OPEN 状态

必须先修改备库，再修改主库，否则可能会引发主备数据同步失败导致主库挂起。

```
//修改数据库为OPEN状态
SQL> ALTER DATABASE OPEN FORCE;
//将ALTER_MODE_STATUS改回原值
SQL> SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0); 
//将DW_INACTIVE_INTERVAL改回原值，本例中为60
SQL> SP_SET_PARA_VALUE(1, 'DW_INACTIVE_INTERVAL', 60);
```

### 7.11.5 修改监视器 dmmonitor.ini

在 dmmonitor.ini 中添加新增的备库 GRP1\_RT\_DSC01/GRP1\_RT\_DSC02：

```
MON_DW_IP = 192.168.0.143:3567/192.168.0.143:3568
```

### 7.11.6 启动所有守护进程以及监视器

分别启动主库和备库（包括 DMDSC 集群 GRP1\_RT\_DSC01、GRP1\_RT\_DSC02）的所有守护进程，最后启动监视器。

## 7.12 普通单机动态切换为主备集群

DM 支持将运行中的单机动态切换为主备集群。

基本流程为：先将单机库动态切换为集群中的主库，然后配置新增加的备库，实现动态将单机库扩展为主备集群。

> **注意**
> 
> 1\. 要求单机库必须已经开启归档开关，并且已经配置好本地归档。  
> 2\. 在动态增加MAL配置时，要求提前对MAL各项配置参数进行检查，确保配置正确并且端口没有被占用，否则配置生效后无法再回退，只能手动修改dmmal.ini并重启生效。

下面以普通单机动态扩展为实时主备集群为例进行说明，示例中新增加的备库是单机备库。如果新增加的备库是 DSC 集群，则备库的配置步骤参考 7.11 动态增加实时 DMDSC 备库 ，主库的配置可以参考本章节示例，相应调整 MAL 和归档的配置方式即可。

### 7.12.1 普通单机库切换为实时主库

以一个普通单机库 GRP\_RT\_01 动态拓展为实时主备集群为例，端口规划如下。

表7.17 端口规划

| **实例名** | **PORT\_NUM （MAL\_INST\_PORT）** | **MAL\_INST\_DW\_PORT** | **MAL\_HOST** | **MAL\_PORT** | **MAL\_DW\_PORT** |
| --- | --- | --- | --- | --- | --- |
| GRP1\_RT\_01 | 32141 | 33141 | 192.168.0.141 | 61141 | 52141 |
| GRP1\_RT\_02 | 32142 | 33142 | 192.168.0.142 | 61142 | 52142 |

#### 7.12.1.1 配置 MAL 系统

本小节以单机库未配置 MAL 为前提进行举例说明，如果已经提前配置，则需要检查 dmmal.ini 相关配置参数是否正确，如果配置错误，则需要手动修改 dmmal.ini 并重启实例生效。

1.通过系统函数 SP\_MAL\_INST\_ADD\_APPLY 添加 MAL 配置项。语句如下（注意此修改无法回退，执行前需要检查并确保传入正确的参数值，并且相关端口没有被占用）：

```
--添加自身MAL信息
SF_MAL_INST_ADD_APPLY('MAL_INST1','GRP1_RT_01','192.168.0.141',61141,'192.168.1.131',32141,52141,4546,33141);
--添加备库MAL信息
SF_MAL_INST_ADD_APPLY('MAL_INST2','GRP1_RT_02','192.168.0.142',61142,'192.168.1.132',32142,52142,4546,33142);
```

2.开启 MAL\_INI。

```
SP_SET_PARA_VALUE(1,'MAL_INI',1);  或  ALTER SYSTEM SET 'MAL_INI' =1 BOTH;
```

3.检查 dmmal.ini 配置是否正确, dmmal.ini 文件内容预期如下：

```
#DaMeng Database Mail Configuration file
#this is comments
MAL_CHECK_INTERVAL     = 30
MAL_COMBIN_BUF_SIZE    = 0
MAL_SEND_THRESHOLD     = 2048
MAL_CONN_FAIL_INTERVAL = 10
MAL_LOGIN_TIMEOUT      = 15
MAL_BUF_SIZE           = 100
MAL_SYS_BUF_SIZE       = 0
MAL_VPOOL_SIZE         = 128
MAL_COMPRESS_LEVEL     = 0
MAL_TEMP_PATH          = 

[MAL_INST1]
MAL_INST_NAME    = GRP1_RT_01
MAL_HOST         = 192.168.0.141
MAL_PORT         = 61141
MAL_INST_HOST    = 192.168.1.131
MAL_INST_PORT    = 32141
MAL_DW_PORT      = 52141
MAL_LINK_MAGIC   = 4546
MAL_INST_DW_PORT = 33141

[MAL_INST2]
MAL_INST_NAME    = GRP1_RT_02
MAL_HOST         = 192.168.0.142
MAL_PORT         = 61142
MAL_INST_HOST    = 192.168.1.132
MAL_INST_PORT    = 32142
MAL_DW_PORT      = 52142
MAL_LINK_MAGIC   = 4546
MAL_INST_DW_PORT = 33142
```

#### 7.12.1.2 配置实时归档

要求单机库已提前开启归档，并且已经配置好本地归档。

1.配置实时归档。

```
SQL> ALTER DATABASE ADD ARCHIVELOG 'TYPE=REALTIME, DEST= GRP1_RT_02';
```

2.检查归档文件是否正确，此时 GRP1\_RT\_01 的 dmarch.ini 文件中内容预期如下：

```
#DaMeng Database Archive Configuration file
#this is comments
        ARCH_WAIT_APPLY      = 0 
[ARCHIVE_LOCAL1]
        ARCH_TYPE            = LOCAL 
        ARCH_DEST            = /dm/data/DAMENG/arch 
        ARCH_FILE_SIZE       = 1024 
        ARCH_SPACE_LIMIT     = 0 
        ARCH_FLUSH_BUF_SIZE  = 2 
        ARCH_HANG_FLAG       = 1 

[ARCHIVE_REALTIME]
        ARCH_TYPE            = REALTIME 
        ARCH_DEST            = GRP1_RT_02 
        WAIT_APPLY           = 0 
        ARCH_FAILOVER        = 0
```

#### 7.12.1.3 设置 OGUID

使用命令行工具 DIsql，连接单机库 GRP1\_RT\_01，设置 OGUID 值为 453331。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>SP_SET_OGUID(453331);--动态修改OGUID
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.12.1.4 联机备份

先启动 DMAP，为后续联机备份做准备。

```
./dmap
```

使用命令行工具 DIsql，连接单机库 GRP1\_RT\_01，对单机库（切换后的主库）进行联机备份。

```
--单机库执行联机备份
SQL> BACKUP DATABASE BACKUPSET '/dm/data/BACKUP_FILE_01';
```

#### 7.12.1.5 修改数据库模式

使用命令行工具 DIsql，登录 GRP1\_RT\_01，将单机实例切换为主库模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>ALTER DATABASE PRIMARY FORCE;
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

#### 7.12.1.6 配置 dmwatcher.ini

配置 dmwatcher.ini 文件，配置为全局守护类型，使用自动切换模式。

```
[GRP1]
DW_TYPE             = GLOBAL   #全局守护类型
DW_MODE             = AUTO         #自动切换模式
DW_ERROR_TIME        = 10        #远程守护进程故障认定时间
INST_RECOVER_TIME   = 60         #主库守护进程启动恢复的间隔时间
INST_ERROR_TIME      = 10        #本地实例故障认定时间
INST_OGUID            = 453331    #守护系统唯一OGUID值
INST_INI              = /dm/data/DAMENG/dm.ini    #dm.ini配置文件路径
INST_AUTO_RESTART   = 1            #打开实例的自动启动功能
INST_STARTUP_CMD    = /dm/bin/dmserver    #命令行方式启动
RLOG_SEND_THRESHOLD  = 0         #指定主库发送日志到备库的时间阈值，默认关闭
RLOG_APPLY_THRESHOLD = 0         #指定备库重演日志的时间阈值，默认关闭
```

### 7.12.2 配置单机实时备库

#### 7.12.2.1 备库初始化与还原恢复

初始化备库。

```
./dminit path=/dm/data port_num=32142
```

拷贝主库上的备份文件到备库 GRP1\_RT\_02 所在机器，并对备库 GRP1\_RT\_02 执行脱机还原与恢复。

```
./dmrman CTLSTMT="RESTORE DATABASE '/dm/data/DAMENG/dm.ini' FROM BACKUPSET '/dm/data/BACKUP_FILE_01'"
./dmrman CTLSTMT="RECOVER DATABASE '/dm/data/DAMENG/dm.ini' FOR STANDBY FROM BACKUPSET '/dm/data/BACKUP_FILE_01'"
./dmrman CTLSTMT="RECOVER DATABASE '/dm/data/DAMENG/dm.ini' UPDATE DB_MAGIC"
```

#### 7.12.2.2 配置 dm.ini

```
#实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16
INSTANCE_NAME            = GRP1_RT_02
PORT_NUM                = 32142    #数据库实例监听端口
DW_INACTIVE_INTERVAL    = 60     #接收守护进程消息超时时间
ALTER_MODE_STATUS        = 0        #不允许手工方式修改实例模式/状态/OGUID
ENABLE_OFFLINE_TS        = 2        #不允许备库OFFLINE表空间
MAL_INI                    = 1        #打开MAL系统
ARCH_INI                = 1        #打开归档配置
RLOG_SEND_APPLY_MON        = 64    #统计最近64次的日志重演信息
```

#### 7.12.2.3 配置 dmmal.ini

手动配置备库的 dmmal.ini 文件。主备库的 dmmal.ini 配置必须完全一致。

可以通过拷贝 GRP1\_RT\_01 的 dmmal.ini 配置，复制到 GRP1\_RT\_02 的配置文件路径下，保证主备的 dmmal.ini 内容一致。

#### 7.12.2.4 配置 dmarch.ini

手动配置备库的 dmarch.ini 文件，配置本地归档与实时归档。

除了本地归档外，其他归档配置项中的 ARCH\_DEST 表示实例是 PRIMARY 模式时，需要同步归档数据的目标实例名。

当前实例 GRP1\_RT\_02 是备库，守护系统配置完成后，可能在各种故障处理中，将 GRP1\_RT\_02 切换为新的主库，故障处理正常的情况下，GRP1\_RT\_01 会切换为新的备库，作为主库，GRP1\_RT\_02 需要向 GRP1\_RT\_01 同步数据，因此实时归档的 ARCH\_DEST 配置为 GRP1\_RT\_01。备库 GRP1\_RT\_02 的 dmarch.ini 文件配置如下：

```
#DaMeng Database Archive Configuration file
#this is comments
    ARCH_WAIT_APPLY      = 0 
[ARCHIVE_LOCAL1]
    ARCH_TYPE            = LOCAL 
    ARCH_DEST            = /dm/data/DAMENG/arch 
    ARCH_FILE_SIZE       = 1024 
    ARCH_SPACE_LIMIT     = 0 
    ARCH_FLUSH_BUF_SIZE  = 2 
    ARCH_HANG_FLAG       = 1 

[ARCHIVE_REALTIME1]
    ARCH_TYPE            = REALTIME 
    ARCH_DEST            = GRP1_RT_01 
    WAIT_APPLY           = 0 
    ARCH_FAILOVER        = 0
```

#### 7.12.2.5 配置 dmwatcher.ini

配置 dmwatcher.ini，配置 GRP1\_RT\_02 的守护进程，配置为全局守护类型，使用自动切换模式。

```
[GRP1]
DW_TYPE             = GLOBAL   #全局守护类型
DW_MODE             = AUTO         #自动切换模式
DW_ERROR_TIME        = 10        #远程守护进程故障认定时间
INST_RECOVER_TIME   = 60         #主库守护进程启动恢复的间隔时间
INST_ERROR_TIME      = 10        #本地实例故障认定时间
INST_OGUID            = 453331    #守护系统唯一OGUID值
INST_INI              = /dm/data/DAMENG/dm.ini    #dm.ini配置文件路径
INST_AUTO_RESTART   = 1            #打开实例的自动启动功能
INST_STARTUP_CMD    = /dm/bin/dmserver    #命令行方式启动
RLOG_SEND_THRESHOLD  = 0         #指定主库发送日志到备库的时间阈值，默认关闭
RLOG_APPLY_THRESHOLD = 0         #指定备库重演日志的时间阈值，默认关闭
```

#### 7.12.2.6 启动备库

以 Mount 方式启动备库。

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

> **注意**
> 
> 一定要以Mount方式启动数据库实例，否则系统启动时会重构回滚表空间，生成Redo日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动Open数据库。

#### 7.12.2.7 设置 OGUID

启动命令行工具 DIsql，登录备库 GRP1\_RT\_02，设置 OGUID 值为 453331。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>SP_SET_OGUID(453331);
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.12.2.8 修改数据库模式

启动命令行工具 DIsql，登录备库 GRP1\_RT\_02 修改数据库为 STANDBY 模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);      --第1步
SQL>ALTER DATABASE STANDBY;                              --第2步
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);        --第3步
```

### 7.12.3 配置监视器

由于主库和实时备库的守护进程配置为自动切换模式，因此这里必须配置确认监视器。和普通监视器相比，确认监视器除了相同的命令支持外，在主库发生故障时，能够自动通知实时备库接管为新的主库，具有自动故障处理的功能。

配置确认监视器时可以选择配置为单实例监视器或多实例监视器，下面将分别介绍配置为单实例监视器以及多实例监视器时 dmmonitor.ini 配置文件中需要配置的信息。

#### 7.12.3.1 配置单实例监视器

修改 dmmonitor.ini 配置文件，进行确认监视器的配置，其中 MON\_DW\_IP 中的 IP 和 PORT 和 dmmal.ini 中的 MAL\_HOST 和 MAL\_DW\_PORT 配置项保持一致。

```
MON_DW_CONFIRM             = 1      #确认监视器模式
MON_LOG_PATH             = /dm/data/log        #监视器日志文件存放路径
MON_LOG_INTERVAL        = 60    #每隔60s定时记录系统信息到日志文件
MON_LOG_FILE_SIZE         = 32    #每个日志文件最大32M
MON_LOG_SPACE_LIMIT     = 0        #不限定日志文件总占用空间
[GRP1]
    MON_INST_OGUID             = 453331 #组GRP1的唯一OGUID值
#以下配置为监视器到组GRP1的守护进程的连接信息，以“IP:PORT”的形式配置
#IP对应dmmal.ini中的MAL_HOST，PORT对应dmmal.ini中的MAL_DW_PORT
    MON_DW_IP                 = 192.168.0.141:52141
    MON_DW_IP                 = 192.168.0.142:52142
```

#### 7.12.3.2 配置多实例监视器

多实例确认监视器需要为每个实例配置一个 dmmonitor.ini。在各实例的 dmmonitor.ini 文件中，除 MON\_ID 和 MON\_NAME 参数不同以外，其他参数应完全一致。

使用配置文件启动多实例监视器实例之前，需要先初始化联机日志文件。初始化联机日志文件的具体操作请查看 [4.2.2.2.2 初始化联机日志文件](data-watch-monitor.md) 。

以其中一个实例的 dmmonitor.ini 为例进行介绍。各实例的 MON\_ID 应与某一个实例配置项中的 MON\_INST\_ID 相同，各实例的 MON\_NAME 与对应的监视器实例名相同。dmmonitor.ini 配置文件中的内容如下：

```
MON_LOG_PATH                = /dm/data/log
MON_LOG_INTERVAL            = 60
MON_LOG_FILE_SIZE            = 32
MON_LOG_SPACE_LIMIT            = 0
MON_DW_CONFIRM                = 1
MON_INST_NUM                = 3            #实例总个数
MON_HB_INTERVAL                = 60         #通信心跳校验间隔
MON_BRO_INTERVAL            = 100         #raft协议中实例通信心跳间隔
MON_VOTE_INTERVAL            = 100         #raft协议中基础投票间隔
MON_ID                        = 1             #当前监视器在监视器系统中的ID
MON_MID                        = 45614        #当前监视器系统的唯一标识
MON_NAME                    = MON1  #监视器名

[GRP1]
MON_INST_OGUID                = 453331
MON_DW_IP                     = 192.168.0.141:52141
MON_DW_IP                     = 192.168.0.142:52142

[MON1] #监视器实例信息
MON_HOST                  = 192.168.0.143         #MON1监视器所在IP 
MON_PORT                  = 8339                 #MON1监视器监听端口
MON_INST_ID                = 1                     #监视器实例在监视器系统中的ID
[MON2]
MON_HOST                  = 192.168.0.144         #MON2监视器所在IP 
MON_PORT                  = 8340                 #MON2监视器监听端口
MON_INST_ID                = 2                     #监视器实例在监视器系统中的ID 
[MON3]
MON_HOST                  = 192.168.0.145         #MON3监视器所在IP 
MON_PORT                  = 8341                 #MON3监视器监听端口
MON_INST_ID                = 3                     #监视器实例在监视器系统中的ID
```

### 7.12.4 启动主备库的守护进程及监视器

1.启动守护进程

分别启动主库和备库的守护进程：

```
./dmwatcher /dm/data/DAMENG/dmwatcher.ini
```

守护进程启动后，进入 Startup 状态，此时各实例都处于 Mount 状态。守护进程开始广播自身和其监控实例的状态信息，结合自身信息和远程守护进程的广播信息，守护进程将本地实例 Open，并切换为 Open 状态。

2.启动监视器

启动监视器命令：

```
./dmmonitor /dm/data/dmmonitor.ini
```

多实例确认监视器系统中，需逐个单独启动各节点上的监视器（启动后，多实例监视器暂不支持动态修改配置，具体说明请查看 [4.2.2.2.3 启动多实例监视器](data-watch-monitor.md) ）。

监视器提供一系列命令，支持当前守护系统状态查看以及故障处理，可输入 help 命令，查看各种命令使用说明，结合实际情况选择使用。

至此，单机成功动态切换为一主一备的实时数据守护系统，在切换步骤和各项配置都正确的情况下，在监视器上执行 show 命令，可以监控到所有实例都处于 Open 状态，所有守护进程也都处于 Open 状态，即为正常运行状态。

## 7.13 DSC 动态切换为 DSC 主备集群

DM 支持将运行中的 normal 模式的 DSC 动态切换为 DSC 主备集群。

基本流程为：先将 DSC 动态切换为集群中的主库，然后配置新增加的备库，实现动态将 DSC 扩展为 DSC 主备集群。

> **注意**
> 
> 1\. 要求DSC必须已经开启归档开关，并且已经配置好本地归档和远程归档。  
> 2\. DSC集群本身一定已经开启MAL开关，只是MAL配置项中可能缺少和数据守护相关的配置项，因此需要对已有的MAL配置项进行动态修改，在修改之前，需要确保待修改的MAL配置项正确，并且端口没有被占用，否则配置生效后无法再回退，只能手动修改dmmal.ini并重启生效。

以 2 节点 DSC 动态扩展为 DSC 主备集群为例进行说明如下，示例中新增加的备库是单机备库。如果新增加的备库是 DSC 集群，则备库的配置步骤参考 7.11 动态增加实时 DMDSC 备库 ，主库的配置可以参考本章节示例，相应调整 MAL 和归档的配置方式即可。

### 7.13.1 DSC 切换为实时主库

拓展后 DSC 主备集群端口规划如下。

表7.18 端口规划

| **实例名** | **MAL\_INST\_HOST** | **PORT\_NUM（MAL\_INST\_PORT）** | **MAL\_INST\_DW\_PORT** | **MAL\_HOST** | **MAL\_PORT** | **MAL\_DW\_PORT** |
| --- | --- | --- | --- | --- | --- | --- |
| GRP1\_RT\_DSC01 | 192.168.1.141 | 8344 | 4567 | 192.168.0.141 | 8338 | 3567 |
| GRP1\_RT\_DSC02 | 192.168.1.142 | 8346 | 4568 | 192.168.0.142 | 8339 | 3568 |
| GRP1\_RT\_02 | 192.168.1.143 | 9344 | 4569 | 192.168.0.143 | 8738 | 3569 |

#### 7.13.1.1 配置 MAL 系统

1.修改 DSC 集群各节点的 MAL 配置项。

DSC 集群本身一定已经开启 MAL，dmmal.ini 中已经配置有 DSC 各节点的 MAL 配置项，但各配置项中需要再增加数据守护相关的配置，如果已经提前配好，则可以忽略此步骤。

可通过查询 V$DM\_MAL\_INI 确认各节点配置情况。

和数据守护相关的配置项如下：

1）MAL\_DW\_PORT：守护进程的监听端口，必须配置，为 0 则表示没有配置。

2）MAL\_INST\_DW\_PORT：实例监听守护进程的端口，必须配置，为 0 则表示没有配置。

3）MAL\_INST\_HOST、MAL\_INST\_PORT：实例对外服务的 IP 地址和端口，这两个是可选配置，如果需要开启读写分离或者需要使用外网通信，则需要配置，否则可以不配。

MAL\_INST\_HOST 值为空则表示没有配置，MAL\_INST\_PORT 为 0 则表示没有配置。

对 DSC 集群中缺少的 MAL 配置项，可通过系统函数 SP\_MAL\_INST\_MODIFY 进行配置更改，方法如下：

启动 DISQL，登录 GRP1\_RT\_DSC01 执行下面语句：

```
--1. 修改GRP1_RT_DSC01的MAL配置项：
--（1）配置GRP1_RT_DSC01的MAL_DW_PORT，若已经配置可以跳过执行（执行前需要确保端口号没有被占用）
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC01', 'MAL_DW_PORT', 3567);
--（2）配置GRP1_RT_DSC01的MAL_INST_DW_PORT，若已经配置可以跳过执行（执行前需要确保端口号没有被占用）
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC01', 'MAL_INST_DW_PORT', 4567);
--（3）（可选配置）配置GRP1_RT_DSC01的MAL_INST_PORT，若已经配置可以跳过执行 
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC01', 'MAL_INST_PORT', 8344);
--（4）（可选配置）配置 GRP1_RT_DSC01的MAL_INST_HOST，若已经配置可以直接进行下一步
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC01', 'MAL_INST_HOST', '192.168.1.141');
--2. 修改GRP1_RT_DSC02的MAL配置项：
--（1）.配置GRP1_RT_DSC02的MAL_DW_PORT，若已经配置可以跳过执行（执行前需要确保端口号没有被占用）
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC02', 'MAL_DW_PORT', 3568);
--（2）配置GRP1_RT_DSC02的MAL_INST_DW_PORT，若已经配置可以跳过执行（执行前需要确保端口号没有被占用）
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC02', 'MAL_INST_DW_PORT', 4569);
--（3）（可选配置）配置GRP1_RT_DSC02的MAL_INST_PORT，若已经配置可以跳过执行
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC02', 'MAL_INST_PORT', 8346);
--（4）（可选配置）配置GRP1_RT_DSC02的MAL_INST_HOST，若已经配置可以跳过执行
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC02', 'MAL_INST_HOST', '192.168.1.142');
```

启动 DISQL，登录 GRP1\_RT\_DSC02 执行下面语句（和上面连接 GRP1\_RT\_DSC01 的执行语句相同）：

```
--1. 修改GRP1_RT_DSC01的MAL配置项：
--（1）配置GRP1_RT_DSC01的MAL_DW_PORT，若已经配置可以跳过执行（执行前需要确保端口号没有被占用）
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC01', 'MAL_DW_PORT', 3567);
--（2）配置GRP1_RT_DSC01的MAL_INST_DW_PORT，若已经配置可以跳过执行（执行前需要确保端口号没有被占用）
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC01', 'MAL_INST_DW_PORT', 4567);
--（3）（可选配置）配置GRP1_RT_DSC01的MAL_INST_PORT，若已经配置可以跳过执行 
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC01', 'MAL_INST_PORT', 8344);
--（4）（可选配置）配置 GRP1_RT_DSC01的MAL_INST_HOST，若已经配置可以直接进行下一步
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC01', 'MAL_INST_HOST', '192.168.1.141');
--2. 修改GRP1_RT_DSC02的MAL配置项：
--（1）.配置GRP1_RT_DSC02的MAL_DW_PORT，若已经配置可以跳过执行（执行前需要确保端口号没有被占用）
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC02', 'MAL_DW_PORT', 3568);
--（2）配置GRP1_RT_DSC02的MAL_INST_DW_PORT，若已经配置可以跳过执行（执行前需要确保端口号没有被占用）
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC02', 'MAL_INST_DW_PORT', 4569);
--（3）（可选配置）配置GRP1_RT_DSC02的MAL_INST_PORT，若已经配置可以跳过执行
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC02', 'MAL_INST_PORT', 8346);
--（4）（可选配置）配置GRP1_RT_DSC02的MAL_INST_HOST，若已经配置可以跳过执行
SQL>SP_MAL_INST_MODIFY('GRP1_RT_DSC02', 'MAL_INST_HOST', '192.168.1.142');
```

特别说明：

1）SP\_MAL\_INST\_MODIFY 函数仅支持将指定参数从 0 值修改为非 0 值或者从空串修改为非空串，配置生效后不允许再修改，因此在执行之前，需要检查并确保传入的参数值正确、相关端口号未被占用。

2）在 dsc 各节点的 dmmal.ini 修改完成之前，不允许启动守护进程，避免守护进程使用到配置中的信息导致异常。

2.增加备库的 MAL 配置项。

DISQL 登录 GRP1\_RT\_DSC01，GRP1\_RT\_DSC02 分别执行：

```
--添加备库MAL信息
SF_MAL_INST_ADD_APPLY('MAL_INST2','GRP1_RT_02','192.168.0.143',8738 ,'192.168.1.143',9344,3569,0,4569);
```

3.检查 dmmal.ini 配置是否正确, dmmal.ini 文件内容预期如下：

```
MAL_CHECK_INTERVAL      = 30        #MAL链路检测时间间隔
MAL_CONN_FAIL_INTERVAL     = 10        #判定MAL链路断开的时间
[MAL_INST0]
  MAL_INST_NAME             = GRP1_RT_DSC01 #实例名，和dm.ini中的INSTANCE_NAME一致
  MAL_HOST                  = 192.168.0.141  #MAL系统监听TCP连接的IP地址
  MAL_PORT                  = 8338             #MAL系统监听TCP连接的端口
  MAL_INST_HOST             = 192.168.1.141  #实例的对外服务IP地址
  MAL_INST_PORT             = 8344    #实例的对外服务端口，和dm.ini中的PORT_NUM一致
  MAL_DW_PORT                = 3567    #实例本地的守护进程监听TCP连接的端口
MAL_INST_DW_PORT            = 4567  #实例监听守护进程TCP连接的端口

[MAL_INST1]
  MAL_INST_NAME             = GRP1_RT_DSC02 
  MAL_HOST                  = 192.168.0.142
  MAL_PORT                  = 8339 
  MAL_INST_HOST             = 192.168.1.142 
  MAL_INST_PORT             = 8346  
  MAL_DW_PORT                = 3568
MAL_INST_DW_PORT            = 4568 

[MAL_INST2]
  MAL_INST_NAME             = GRP1_RT_02
  MAL_HOST                  = 192.168.0.143
  MAL_PORT                  = 8738
  MAL_INST_HOST             = 192.168.1.143 
  MAL_INST_PORT             = 9344 
  MAL_DW_PORT                = 3569
MAL_INST_DW_PORT            = 4569
```

#### 7.13.1.2 配置实时归档

要求 DSC 必须已经开启归档开关，并且已经配置好本地归档和远程归档。

增加实时备库归档，分别连接 GRP1\_RT\_DSC01, GRP1\_RT\_DSC02 执行：

```
SQL> ALTER DATABASE ADD ARCHIVELOG 'TYPE=REALTIME, DEST= GRP1_RT_02';
```

修改后 GRP1\_RT\_DSC01 的 dmarch.ini 文件。

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE            = LOCAL 
    ARCH_DEST            = +DMDATA/DSC/DSC01/arch
    ARCH_FILE_SIZE        = 128 
    ARCH_SPACE_LIMIT    = 0 

[ARCHIVE_REMOTE]
    ARCH_TYPE            = REMOTE
    ARCH_DEST            = GRP1_RT_DSC02
    ARCH_INCOMING_PATH  = +DMDATA/DSC/DSC02/arch

[ARCHIVE_REALTIME] 
ARCH_TYPE             = REALTIME
ARCH_DEST             = GRP1_RT_02
```

修改后 GRP1\_RT\_DSC02 的 dmarch.ini 文件。

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE            = LOCAL
    ARCH_DEST            = +DMDATA/DSC/DSC02/arch
    ARCH_FILE_SIZE        = 128
    ARCH_SPACE_LIMIT    = 0

[ARCHIVE_REMOTE]
    ARCH_TYPE            = REMOTE
    ARCH_DEST            = GRP1_RT_DSC01
    ARCH_INCOMING_PATH  = +DMDATA/DSC/DSC01/arch

[ARCHIVE_REALTIME] 
ARCH_TYPE             = REALTIME
ARCH_DEST             = GRP1_RT_02
```

#### 7.13.1.3 设置 OGUID

启动命令行工具 DIsql，连接 DMDSC 集群中的任意一个节点，设置 DMDSC 主库的 OGUID 值。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>SP_SET_OGUID(1000);
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

#### 7.13.1.4 联机备份

先启动 DMAP,为后续联机备份做准备。

```
./dmap
```

使用命令行工具 DIsql，连接 DSC 任一节点既可对整个 DSC 集群进行联机备份。

```
--备份
SQL> BACKUP DATABASE BACKUPSET '/dm/data/BACKUP_FILE_01';
```

#### 7.13.1.5 修改数据库模式

使用命令行工具 DIsql， 登录 DSC 控制节点，将 DSC 切换为主库模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>ALTER DATABASE PRIMARY force;
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

#### 7.13.1.6 配置 dmwatcher.ini

依次配置 DSC 每个节点实例的 dmwatcher.ini 文件，放到各自 dm.ini 中指定的 CONFIG\_PATH 目录下。

另外要注意，DMDSC 集群各节点实例的自动拉起是由各自本地的 dmcss 执行的，不是由守护进程执行，如果要打开 DMDSC 集群的自动拉起，需要再去配置 dmdcr.ini 中的自动拉起参数，为避免 dmcss 在所有配置步骤完成之前提前将 DMServer 自动拉起，这里先不修改 dmdcr.ini 配置，放到后面步骤中修改。

1.配置 GRP1\_RT\_DSC01 的 dmwatcher.ini 文件。

```
[GRP1]
   DW_TYPE                = GLOBAL  #全局守护类型
   DW_MODE                = MANUAL  #手动切换模式
   DW_ERROR_TIME        = 60        #远程守护进程故障认定时间
   INST_RECOVER_TIME    = 60        #主库守护进程启动恢复的间隔时间
   INST_ERROR_TIME     = 35        #本地实例故障认定时间
   INST_INI            = /dm/data/DSC/DSC01/dm.ini    #dm.ini配置文件路径
   DCR_INI                = /dm/data/DSC/conf/dmdcr1.ini #dmdcr.ini配置文件路径
   INST_OGUID          = 1000    #守护系统唯一OGUID值
   INST_STARTUP_CMD    = /dm/bin/dmserver #命令行方式启动
   INST_AUTO_RESTART    = 0        #关闭实例的自动启动功能
   RLOG_SEND_THRESHOLD    = 0        #指定主库发送日志到备库的时间阈值，默认关闭
   RLOG_APPLY_THRESHOLD = 0    #指定备库重演日志的时间阈值，默认关闭
```

2.配置 GRP1\_RT\_DSC02 的 dmwatcher.ini 文件。

```
[GRP1]
   DW_TYPE                 = GLOBAL
   DW_MODE                 = MANUAL
   DW_ERROR_TIME           = 60
   INST_RECOVER_TIME       = 60
   INST_ERROR_TIME         = 35
   INST_INI                = /dm/data/DSC/DSC02/dm.ini
   DCR_INI                      = /dm/data/DSC/conf/dmdcr2.ini
   INST_OGUID              = 1000
   INST_STARTUP_CMD        = /dm/bin/dmserver
   INST_AUTO_RESTART    = 0
   RLOG_SEND_THRESHOLD  = 0
   RLOG_APPLY_THRESHOLD = 0
```

### 7.13.2 配置单机实时备库

#### 7.13.2.1 初始化备库

初始化备库。

```
./dminit path=/dm/data port_num=9344
```

拷贝主库上的备份文件到备库 GRP1\_RT\_02 所在机器，并对备库 GRP1\_RT\_02 执行脱机还原与恢复。

```
./dmrman CTLSTMT="RESTORE DATABASE '/dm/data/DAMENG/dm.ini' FROM BACKUPSET '/dm/data/BACKUP_FILE_01'"
./dmrman CTLSTMT="RECOVER DATABASE '/dm/data/DAMENG/dm.ini' FOR STANDBY FROM BACKUPSET '/dm/data/BACKUP_FILE_01'"
./dmrman CTLSTMT="RECOVER DATABASE '/dm/data/DAMENG/dm.ini' UPDATE DB_MAGIC"
```

#### 7.13.2.2 配置 dm.ini

```
#实例名，建议使用“组名_守护环境_序号”的命名方式，总长度不能超过16
INSTANCE_NAME            = GRP1_RT_02
PORT_NUM                = 9344    #数据库实例监听端口
DW_INACTIVE_INTERVAL    = 60     #接收守护进程消息超时时间
ALTER_MODE_STATUS        = 0        #不允许手工方式修改实例模式/状态/OGUID
ENABLE_OFFLINE_TS        = 2        #不允许备库OFFLINE表空间
MAL_INI                    = 1        #打开MAL系统
ARCH_INI                = 1        #打开归档配置
RLOG_SEND_APPLY_MON        = 64    #统计最近64次的日志重演信息
```

#### 7.13.2.3 配置 dmmal.ini

配置备库的 dmmal.ini 文件。各主备库的 dmmal.ini 配置必须完全一致。

可以通过拷贝 GRP1\_RT\_DSC01 的 dmmal.ini 配置，复制到 GRP1\_RT\_02 的配置文件路径下，保证主备的 dmmal.ini 内容一致。

```
MAL_CHECK_INTERVAL      = 30        #MAL链路检测时间间隔
MAL_CONN_FAIL_INTERVAL     = 10        #判定MAL链路断开的时间
[MAL_INST0]
  MAL_INST_NAME             = GRP1_RT_DSC01 #实例名，和dm.ini中的INSTANCE_NAME一致
  MAL_HOST                  = 192.168.0.141  #MAL系统监听TCP连接的IP地址
  MAL_PORT                  = 8338             #MAL系统监听TCP连接的端口
  MAL_INST_HOST             = 192.168.1.141  #实例的对外服务IP地址
  MAL_INST_PORT             = 8344    #实例的对外服务端口，和dm.ini中的PORT_NUM一致
  MAL_DW_PORT                = 3567    #实例本地的守护进程监听TCP连接的端口
  MAL_INST_DW_PORT            = 4567  #实例监听守护进程TCP连接的端口

[MAL_INST1]
  MAL_INST_NAME             = GRP1_RT_DSC02 
  MAL_HOST                  = 192.168.0.142
  MAL_PORT                  = 8339 
  MAL_INST_HOST             = 192.168.1.142
  MAL_INST_PORT             = 8346 
  MAL_DW_PORT                = 3568
  MAL_INST_DW_PORT            = 4568 

[MAL_INST2]
  MAL_INST_NAME             = GRP1_RT_02
  MAL_HOST                  = 192.168.0.143
  MAL_PORT                  = 8738
  MAL_INST_HOST             = 192.168.1.143
  MAL_INST_PORT             = 9344
  MAL_DW_PORT                = 3569
  MAL_INST_DW_PORT            = 4569
```

#### 7.13.2.4 配置 dmarch.ini

手动配置备库的 dmarch.ini 文件，配置本地归档与实时归档。

```
[ARCHIVE_LOCAL1]
    ARCH_TYPE            = LOCAL
    ARCH_DEST            = /dm/data/EP01/DAMENG/arch
    ARCH_FILE_SIZE        = 1024
    ARCH_SPACE_LIMIT    = 0

[ARCHIVE_REALTIME1]
    ARCH_TYPE            = REALTIME
    ARCH_DEST            = GRP1_RT_DSC01/GRP1_RT_DSC02
```

#### 7.13.2.5 配置 dmwatcher.ini

配置 GRP1\_RT\_02 的 dmwatcher.ini 文件。

```
[GRP1]
   DW_TYPE                 = GLOBAL
   DW_MODE                 = MANUAL
   DW_ERROR_TIME           = 60
   INST_RECOVER_TIME       = 60
   INST_ERROR_TIME         = 35
   INST_INI                = /dm/data/GRP1_RT_02/dm.ini
   INST_OGUID              = 1000
   INST_STARTUP_CMD        = /dm/bin/dmserver
   INST_AUTO_RESTART       = 0 #对单节点，如果需要打开自动拉起功能，将此配置修改为1即可
   RLOG_SEND_THRESHOLD     = 0
   RLOG_APPLY_THRESHOLD    = 0
```

#### 7.13.2.6 启动备库

以 Mount 方式启动备库。

```
./dmserver /dm/data/DAMENG/dm.ini mount
```

> **注意**
> 
> 一定要以Mount方式启动数据库实例，否则系统启动时会重构回滚表空间，生成Redo日志；并且，启动后应用可能连接到数据库实例进行操作，破坏主备库的数据一致性。数据守护配置结束后，守护进程会自动Open数据库。

#### 7.13.2.7 设置 OGUID

启动命令行工具 DIsql，登录备库 GRP1\_RT\_02，设置 OGUID 值为 1000。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);
SQL>SP_SET_OGUID(1000);
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);
```

> **注意**
> 
> 系统通过OGUID值确定一个守护进程组，由用户保证OGUID值的唯一性，并确保数据守护系统中，数据库、守护进程和监视器配置相同的OGUID值。

#### 7.13.2.8 修改数据库模式

启动命令行工具 DIsql，登录备库 GRP1\_RT\_02 修改数据库为 STANDBY 模式。

```
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 1);           --第1步
SQL>ALTER DATABASE STANDBY;                                    --第2步 
SQL>SP_SET_PARA_VALUE(1, 'ALTER_MODE_STATUS', 0);            --第3步
```

### 7.13.3 配置监视器

本小节示例守护进程配置的是手动切换模式，因此这里配置普通监视器即可。

编辑 dmmonitor.ini 文件，放在/dm/data 目录下:

```
MON_LOG_PATH                = /dm/data/log
MON_LOG_INTERVAL            = 60
MON_LOG_FILE_SIZE            = 64
MON_LOG_SPACE_LIMIT            = 0
MON_DW_CONFIRM                = 0

[GRP1]
MON_INST_OGUID                = 1000
MON_DW_IP                    = 192.168.0.141:3567/192.168.0.142:3568
MON_DW_IP                    = 192.168.0.143:3569
```

### 7.13.4 启动主备库的守护进程及监视器

启动 DMDSC 主库的所有守护进程：

```
./dmwatcher /dm/data/DSC/DSC01/dmwatcher.ini
./dmwatcher /dm/data/DSC/DSC02/dmwatcher.ini
```

启动备库的守护进程：

```
./dmwatcher /dm/data/DAMENG/dmwatcher.ini
```

启动监视器：

```
./dmmonitor path=/dm/data/dmmonitor.ini
```

监视器提供一系列命令，支持当前守护系统状态查看以及故障处理，可输入 help 命令，查看各种命令使用说明，结合实际情况选择使用。

至此 normal 模式的 DSC 成功切换为 DSC 主备集群，在搭建步骤和各项配置都正确的情况下，在监视器上执行 show 命令，可以监控到所有实例都处于 Open 状态，所有守护进程也都处于 Open 状态，即为正常运行状态。