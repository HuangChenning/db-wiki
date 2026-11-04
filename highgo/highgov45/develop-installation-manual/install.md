---
title: "概述"
book: "HGDB-SEE V4.5.8 安装手册"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/develop/install.html"
tags:
  - highgo
  - highgo-v45
  - develop-installation-manual
---

## HGDB-SEE V4.5.8 安装手册

## 前言

### 文档说明

本文档适用于瀚高安全版数据库系统V4.5.8（以下简称HGDB-SEE V4.5.8）安装过程。

### 环境说明

演示环境如下:

CPU：x86\_64（虚拟机）

操作系统：Red Hat Enterprise Linux Server release 7.1 (Maipo)

数据库介质：hgdb-see-4.5.8-fe4791c.x86\_64.rpm

## 安装前准备

### 最小硬件需求

安装之前需要确保服务器符合瀚高数据库要求的最低配置，见下表。

|  |  |
| --- | --- |
| 硬盘 | 最小1GB，生产环境建议单独挂载 > 2000GB 的磁盘存放数据 |
| 物理内存 | 最小1GB，生产环境建议 > 8GB |
| 交换内存 | 可以不配置，生产环境建议配置，与内存对应关系详见下表 |

### 操作系统版本检查

> cat /etc/os-release

确保为符合的操作系统。

### CPU 型号检查

> grep model /proc/cpuinfo

确保为符合架构的CPU。

### 操作系统内存空间检查

要验证系统是否满足HGDB-SEE V4.5.8的最低要求，以root用户身份登录并运行以下命令。

查看可用RAM和交换空间大小，运行以下命令：

> df -h
> 
> free -h
> 
> grep MemTotal /proc/meminfo
> 
> grep SwapTotal /proc/meminfo

内存及对应swap建议值参照下表。

| **MemTotal** | **SwapTotal** |
| --- | --- |
| <=8G | 2~4G |
| 8~16G | 4~8G |
| 16~64G | 8~32G |
| \>=64G | 32G |

确保满足数据库最小安装需求。

### 磁盘大小检查

> df -h

确保满足数据库最小安装需求。

### 数据库安装包完整性检查

> md5sum hgdb-see-4.5.8-fe4791c.x86\_64.rpm

返回结果需要与瀚高数据库安装包md5检验码文件中的序号一致，确保上传至服务器的数据库安装包完整，未被损坏。

### 系统内核参数检查

检查内核参数，确保瀚高数据库运行在最优环境下。如下为内核参数修改参考值，可通过编辑/etc/sysctl.conf文件修改参数：

```bash
vi /etc/sysctl.conf
kernel.shmall= 2097152    
// shmall根据实际page_size设置，等于物理内存(B)/page_size。使用getconf PAGE_SIZE命令获取page_size的值，一般为4096B
kernel.shmmax= 4294967295  
// shmmax根据实际物理内存设置，物理内存(B)的1/2
kernel.shmmni= 4096
kernel.sem= 250 32000 100 128
fs.file-max= 6815744
net.ipv4.ip_local_port_range= 9000 65500
net.core.rmem_default= 262144
```

运行如下命令使参数生效：

> /sbin/sysctl -p

运行如下命令使参数net.ipv4.ip\_local\_port\_range生效：

> /etc/rc.d/init.d/network restart

### 防火墙设置

关闭防火墙或者开放端口：

1. 关闭防火墙

> systemctl stop firewalld.service
> 
> systemctl disable firewalld.service

2. 开放数据库使用端口

> firewall-cmd –add-port=5866/tcp #临时添加5866端口
> 
> firewall-cmd –permanent –add-port=5866/tcp #永久添加5866端口
> 
> firewall-cmd –reload #重载生效

验证命令：

> firewall-cmd –list-ports | grep 5866 #查看是否开放5866端口

### 时区和时间检查

安装前对系统时间和时区进行检查，不正确的情况可以通过如下命令修改。

```bash
//检查时区 
timedatectl
 //修改时区为上海 
timedatectl set-timezone Asia/Shanghai 
//修改时间
date -s "20220222 10:26:00"
```

## 数据库安装

### rpm包安装

安全版数据库rpm格式的介质需使用root用户安装和维护数据库。

（1）使用root用户安装rpm包：

```bash
[root@hgdb ~]# rpm -ivh hgdb-see-4.5.8-fe4791c.x86_64.rpm 
准备中...                          ################################# [100%]
正在升级/安装...
   1:hgdb-see-4.5.8-fe4791c           ################################# [100%]
Created symlink from /etc/systemd/system/multi-user.target.wants/hgdb-see-4.5.8.service to /usr/lib/systemd/system/hgdb-see-4.5.8.service.
Created symlink from /etc/systemd/system/graphical.target.wants/hgdb-see-4.5.8.service to /usr/lib/systemd/system/hgdb-see-4.5.8.service.
Created symlink from /etc/systemd/system/multi-user.target.wants/hgproxy.service to /usr/lib/systemd/system/hgproxy.service.
Created symlink from /etc/systemd/system/graphical.target.wants/hgproxy.service to /usr/lib/systemd/system/hgproxy.service.
```

安装完毕后，会在/opt/highgo下生成如下安装目录：

```bash
[root@hgdb ~]# cd /opt/highgo/
[root@hgdb highgo]# ls
dbha  hgdbconfiguration  hgdb-see-4.5.8  hgproxy
```

（2）环境变量生效

数据库安装完毕后会在/opt/highgo/hgdb-see-4.5.8/etc目录下生成一个名为hgdbenv.sample的环境变量示例文件，内容如下所示：

```bash
export HG_BASE=/opt/highgo
export HGDB_HOME=/opt/highgo/hgdb-see-4.5.8
export PGPORT=5866
export PGDATABASE=highgo
export PATH=$HGDB_HOME/bin:$PATH
export PGDATA=$HGDB_HOME/data
```

您可根据需要修改该示例文件，并使其生效。会话级别的生效命令如下：

> \[root@hgdb etc\]# source hgdbenv.sample

也可将该命令加入系统环境变量文件中，如.bash\_profile。

（3）初始化并配置数据库

在etc目录下有一个配置脚本laststep.sh，使用该脚本可快速进行数据库配置。

```bash
[root@ hgdb etc]# ./laststep.sh 
是否按照默认值初始化一个数据库实例？（yes/no/exit）（默认yes）yes
initdb -A sm3 -e sm4 -c echo 12345678 -D /opt/highgo/hgdb-see-4.5.8/data --pwfile=/opt/highgo/hgdb-see-4.5.8/etc/default_passwd
The files belonging to this database system will be owned by user "root".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.UTF-8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.
Data encryption using sm4 is enabled.

creating directory /opt/highgo/hgdb-see-4.5.8/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... PRC
creating configuration files ... ok
running bootstrap script ... 2022-05-05 13:23:55.450 CST [25261] LOG:  Switchover the SSHA Role. Current is NONE
ok
performing post-bootstrap initialization ... 2022-05-05 13:23:56.475 CST [25272] LOG:  data encryption performed by sm4
2022-05-05 13:23:56.484 CST [25272] LOG:  Switchover the SSHA Role. Current is NONE

ok
syncing data to disk ... ok

Success. You can now start the database server using:

    hg_sslkeygen.sh /opt/highgo/hgdb-see-4.5.8/data
    pg_ctl -D /opt/highgo/hgdb-see-4.5.8/data -l logfile start
/opt/highgo/hgdb-see-4.5.8/bin/hg_sslkeygen.sh /opt/highgo/hgdb-see-4.5.8/data
Setting the ssl configuration to /opt/highgo/hgdb-see-4.5.8/data
Generating RSA private key, 2048 bit long modulus
............+++
.............................................................................................................................................................+++
e is 65537 (0x10001)
pg_ctl start -D /opt/highgo/hgdb-see-4.5.8/data
waiting for server to start....2022-05-05 13:24:15.002 CST [25296] LOG:  data encryption performed by sm4
2022-05-05 13:24:15.614 CST [25296] LOG:  starting HighGo Security Enterprise Edition Database System 4.5.8 on x86_64,build on 20220419
2022-05-05 13:24:15.615 CST [25296] LOG:  listening on IPv6 address "::1", port 5866
2022-05-05 13:24:15.615 CST [25296] LOG:  listening on IPv4 address "127.0.0.1", port 5866
2022-05-05 13:24:15.738 CST [25296] LOG:  listening on Unix socket "/tmp/.s.PGSQL.5866"
2022-05-05 13:24:15.798 CST [25296] LOG:  This is a trial HighGo Security Enterprise Edition Database, valid until 2022-06-04 23:59:59. Pre-sale service hotline: 400-708-8006. Online technical support platform: https://support.highgo.com/.
2022-05-05 13:24:15.808 CST [25298] LOG:  database system was shut down at 2022-05-05 13:24:08 CST
2022-05-05 13:24:15.811 CST [25298] LOG:  Switchover the SSHA Role. Current is NONE
2022-05-05 13:24:15.827 CST [25296] LOG:  database system is ready to accept connections
 done
server started
psql -U syssso -d highgo -f secure_param.sql
NOTICE:  
-------------------------------------------
Login User: syssso 
Login time: 2022-05-05 13:24:17.054059+08 
Login Address: [local] 
Last Login Status: SUCCESS 
Login Failures: 0 
Valied Until: 2022-05-12 13:23:56+08 
-------------------------------------------

        set_secure_param         
---------------------------------
 set configuration successfully.
(1 row)

        set_secure_param         
---------------------------------
 set configuration successfully.
(1 row)

        set_secure_param         
---------------------------------
 set configuration successfully.
(1 row)

        set_secure_param         
---------------------------------
 set configuration successfully.
(1 row)

        set_secure_param         
---------------------------------
 set configuration successfully.
(1 row)

psql -U syssao -d highgo -f audit_param.sql
NOTICE:  
-------------------------------------------
Login User: syssao 
Login time: 2022-05-05 13:24:17.098228+08 
Login Address: [local] 
Last Login Status: SUCCESS 
Login Failures: 0 
Valied Until: 2022-05-12 13:23:56+08 
-------------------------------------------

         set_audit_param         
---------------------------------
 set configuration successfully.
(1 row)

pg_ctl restart  -D /opt/highgo/hgdb-see-4.5.8/data
2022-05-05 13:24:17.230 CST [25296] LOG:  received fast shutdown request
waiting for server to shut down....2022-05-05 13:24:17.241 CST [25296] LOG:  aborting any active transactions
2022-05-05 13:24:17.250 CST [25296] LOG:  background worker "logical replication launcher" (PID 25304) exited with exit code 1
2022-05-05 13:24:17.250 CST [25299] LOG:  shutting down
2022-05-05 13:24:17.620 CST [25296] LOG:  database system is shut down
 done
server stopped
waiting for server to start....2022-05-05 13:24:17.666 CST [25321] LOG:  data encryption performed by sm4
2022-05-05 13:24:17.676 CST [25321] LOG:  starting HighGo Security Enterprise Edition Database System 4.5.8 on x86_64,build on 20220419
2022-05-05 13:24:17.676 CST [25321] LOG:  listening on IPv4 address "0.0.0.0", port 5866
2022-05-05 13:24:17.676 CST [25321] LOG:  listening on IPv6 address "::", port 5866
2022-05-05 13:24:17.694 CST [25321] LOG:  listening on Unix socket "/tmp/.s.PGSQL.5866"
2022-05-05 13:24:17.789 CST [25321] LOG:  redirecting log output to logging collector process
2022-05-05 13:24:17.789 CST [25321] HINT:  Future log output will appear in directory "hgdb_log".
 done
server started
```

也可使用配置助手工具使用图形界面对数据库进行配置。详见配置助手使用文档。

### deb包安装

debian系的操作系统需要使用deb格式的介质安装数据库。与rpm包相比，仅安装命令不同：

> dpkg -i hgdb-see-4.5.8-fe4791c.x86\_64.deb

## 启停数据库

1. 通过服务启动。

> \[root@hgdb ~\]$ systemctl start hgdb-see-4.5.8.service

2. 通过服务停止。

> \[root@hgdb ~\]$ systemctl stop hgdb-see-4.5.8.service

3. 通过数据库命令启动。

> \[root@hgdb ~\]$ pg\_ctl start -D /opt/highgo/hgdb-see-4.5.8/data

4. 通过数据库命令停止。

> \[root@hgdb ~\]$ pg\_ctl stop -D /opt/highgo/hgdb-see-4.5.8/data

## 卸载数据库

### rpm包卸载

卸载前请使用pg\_ctl stop或systemctl 命令关闭数据库服务。

使用rpm命令卸载数据库。为保证数据安全性，卸载后data目录不会被删除，请根据需要手动删除。

卸载命令：

> \[root@hgdb ~\]# rpm -e hgdb-see-4.5.8

### deb包卸载

卸载前请使用pg\_ctl stop或systemctl 命令关闭数据库服务。

使用dpkg命令卸载数据库。为保证数据安全性，卸载后data目录不会被删除，请根据需要手动删除。

卸载命令：

> \[root@hgdb ~\]# dpkg -r hgdb-see-4.5.8

## 数据库目录结构

如下为数据库安装后生成的目录结构：

| 目录名 | 注释 |
| --- | --- |
| dbha | 存放瀚高高可用集群的配置文件和可执行文件。 |
| hgdbconfiguration | 存放运行配置助手工具所需的问题。 |
| hgdb-see-4.5.8 | 存放数据库相关目录。 |
| bin | 存放数据库相关的可执行文件 |
| conf | 存放数据库相关的配置文件 |
| etc | 存放驱动文件、环境变量示例文件、一键配置脚本等数据库相关的外围文件 |
| include | 存放数据库的头文件 |
| lib | 存放数据库相关的库文件 |
| REVISION | 存放数据库安装包的版本号（内部使用） |
| share | 存放文档、扩展等 |
| hgproxy | 存放读写分离工具相关的可执行文件和库文件等。 |

初始化数据库后，会生成数据目录，例如“/opt/highgo/hgdb-see-4.5.8/data” ，其中包含众多子目录和文件。

不同版本包含的目录及名称略有不同。下表对数据目录中子目录和文件的用途进行说明。

| 目录名 | 注释 |
| --- | --- |
| base | 包含数据库用户所创建的各个数据库。 |
| bct | hg\_rman的块跟踪机制，主要用于增量备份。 |
| global | 一些共享系统表的目录，包含集群范围的各个表和相关视图。 |
| hgdb\_log | 包含数据库日志，目录名可自定义。 |
| log | 包含数据库日志文件。 |
| pg\_commit\_ts | 事务提交时间戳。 |
| pg\_dynshmem | 动态共享内存子系统。 |
| pg\_logical | 逻辑解码状态数据。 |
| pg\_multixact | 多事务状态数据。 |
| pg\_notify | 监听/通知状态。 |
| pg\_replslot | 复制槽数据。 |
| pg\_serial | 提交的可序列化事务的信息。 |
| pg\_snapshots | 导出的快照。 |
| pg\_stat | 统计子系统的永久文件。 |
| pg\_stat\_tmp | 统计子系统的临时文件。 |
| pg\_subtrans | 子事务状态数据。 |
| pg\_tblspc | 表空间符号链接。 |
| pg\_twophase | 准备事务的状态文件。 |
| pg\_wal | WAL (Write Ahead Log/REDO) 文件。 |
| pg\_xact | 事务提交状态数据。 |
| hgaudit/hg\_audit | 审计日志目录。 |
| current\_logfiles | 由日志采集器写入的日志文件。 |
| hgdb.lic | 数据库使用期限控制文件。 |
| pg\_hba.conf | 是数据库判断客户端/应用程序能否正常访问数据库的唯一依据，认证配置文件。 |
| pg\_ident.conf | 映射配置文件。 |
| PG\_VERSION | 内核的版本号。 |
| postgresql.auto.conf | 通过ALTER SYSTEM修改的参数(新功能,优先级更高)。 |
| postgresql.conf | 数据库实例的主配置文件，基本上所有的配置参数都在此文件中。 |
| postmaster.opts | 该文件记录服务器最后一次启动时使用的命令行参数。 |
| postmaster.pid | 锁文件，记录当前主进程ID(PID)以及集集数据目录路径、主服务开始时间戳、端口号、UNIX域套接字目录路径(Windows上的空)、第一个有效的侦听地址(IP地址或\*，或如果不在TCP上侦听空)，以及共享内存段ID(TH)。 |
| audit\_param.conf | 审计配置文件。 |
| secure\_param.conf | 安全配置文件。 |
| server.crt | 服务端证书。 |
| server.key | 私钥证书。 |
| root.crt | 根证书。 |