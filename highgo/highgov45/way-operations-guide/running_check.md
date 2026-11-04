---
title: "14、数据库服务是否运行及运行状态的检查方法"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/running_check.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 数据库服务是否运行及运行状态的检查方法

## 一、单机版数据库的运行状态查看

### 1、通过数据库自带的操作系统命令 pg\_ctl 查看数据库运行状态

```
# 数据库正常运行显示如下:

[highgo@localhost ~]$ pg_ctl status 

pg_ctl: server is running (PID: 7482)

/opt/HighGoDB-5.6.4/bin/postgres "-D" "/opt/HighGoDB-5.6.4/data"

# 数据库关闭状态显示如下:

[highgo@localhost ~]$ pg_ctl status 

pg_ctl: no server running
```

### 2、通过数据库自带的操作系统命令 pg\_controldata 查看数据库运行状态

```
# 数据库正常运行显示如下:

[highgo@localhost ~]$ pg_controldata 

...

Database cluster state:        in production

..

# 数据库关闭状态显示如下:

[highgo@localhost ~]$ pg_controldata 

...

Database cluster state:        shut down

...
```

### 3、通过后台进程看数据库运行状态

```
# 正常运行的数据库会存在如下进程

[highgo@localhost ~]$ ps -ef | grep -v grep | grep postgres 

highgo   8002   1 0 10:41 pts/0  00:00:00 /opt/HighGoDB-5.6.4/bin/postgres

highgo   8007  8002 0 10:41 ?    00:00:00 postgres: logger process  

highgo   8009  8002 0 10:41 ?    00:00:00 postgres: checkpointer process 

highgo   8010  8002 0 10:41 ?    00:00:00 postgres: writer process  

highgo   8011  8002 0 10:41 ?    00:00:00 postgres: wal writer process  

highgo   8012  8002 0 10:41 ?    00:00:00 postgres: autovacuum launcher process 

highgo   8013  8002 0 10:41 ?    00:00:00 postgres: archiver process  

highgo   8014  8002 0 10:41 ?    00:00:00 postgres: stats collector process 

highgo   8015  8002 0 10:41 ?    00:00:00 postgres: bgworker: pg_wait_sampling collector 

highgo   8017  8002 0 10:41 ?    00:00:00 postgres: bgworker: performance diagnosis collector 

highgo   8018  8002 0 10:41 ?    00:00:00 postgres: bgworker: hg_job_scheduler 

highgo   8019  8002 0 10:41 ?    00:00:00 postgres: bgworker: logical replication launcher
```

ps：(1)显示内容第一列代表数据库在哪个用户底下运行，上方显示数据库运行在highgo用户底下。

(2)显示内容第一行代表数据库运行的主进程。

### 4、通过文件系统查看数据库是否处于运行状态

```
# 数据库处于运行状态时会存在下列文件:

[highgo@localhost data]$ ls -lrth | grep postmaster.pid

-rw------- 1 highgo highgo  82 Jul 23 10:41 postmaster.pid

# 数据库处于关闭状态时:

[highgo@localhost data]$ ls -lrth | grep postmaster
```

ps: (1)运行上方命令需要进到数据库data目录，命令：cd $PGDATA

(2)但是如果数据库由于异常宕机，可能会存在残留进程，所以不能仅凭这一条来判定数据库处于正常运行状态

(3)如果查看数据库处于运行状态，但是连接不到数据库，查看进程存在很少，有可能是数据库异常宕机，此时需要删除掉数据目录中的 postmaster.pid 文件并重启数据库

## 二、主备流复制数据库运行状态的查询

1、通过数据库自带的操作系统命令 pg\_ctl 查看数据库运行状态

```
# 数据库正常运行显示如下:

[highgo@localhost ~]$ pg_ctl status 

pg_ctl: server is running (PID: 7465)

/opt/HighGoDB-5.6.4/bin/postgres "-D" "/opt/HighGoDB-5.6.4/data"

# 数据库关闭状态显示如下:

[highgo@localhost ~]$ pg_ctl status 

pg_ctl: no server running
```

### 2、通过数据库自带的操作系统命令 pg\_controldata 查看数据库运行状态

```
# 流复制**主库**正常运行时:

[highgo@node1 ~]$ pg_controldata

pg_control version number:      1002

Catalog version number:        201707211

Database system identifier:      6837288046332662480

**Database cluster state:        in production**

...

# 流复制**主库**处于关闭状态时:

[highgo@node1 ~]$ pg_controldata

pg_control version number:      1002

Catalog version number:        201707211

Database system identifier:      6837288046332662480

**Database cluster state:        shut down**

...

# 流复制**备库**正常运行时:

[highgo@node2 ~]$ pg_controldata

pg_control version number:      1002

Catalog version number:        201707211

Database system identifier:      6837288046332662480

**Database cluster state:        in archive recovery**

...

# 流复制**备库**处于关闭状态时:

[highgo@node2 ~]$ pg_controldata

pg_control version number:      1002

Catalog version number:        201707211

Database system identifier:      6837288046332662480

**Database cluster state:        shut down in recovery**

...
```

### 3、通过后台进程看数据库运行状态

```
# 流复制**主库**正常运行时:

[highgo@node1 ~]$ ps -ef | grep postgres 

highgo   8038   1 0 11:07 pts/0  00:00:00 /opt/HighGoDB-5.6.4/bin/postgres

highgo   8043  8038 0 11:07 ?    00:00:00 postgres: logger process  

highgo   8045  8038 0 11:07 ?    00:00:00 postgres: checkpointer process 

highgo   8046  8038 0 11:07 ?    00:00:00 postgres: writer process  

highgo   8047  8038 0 11:07 ?    00:00:00 postgres: wal writer process  

highgo   8048  8038 0 11:07 ?    00:00:00 postgres: autovacuum launcher process 

highgo   8049  8038 0 11:07 ?    00:00:00 postgres: archiver process  

highgo   8050  8038 0 11:07 ?    00:00:00 postgres: stats collector process 

highgo   8051  8038 0 11:07 ?    00:00:00 postgres: bgworker: pg_wait_sampling collector 

highgo   8053  8038 0 11:07 ?    00:00:00 postgres: bgworker: performance diagnosis collector 

highgo   8054  8038 0 11:07 ?    00:00:00 postgres: bgworker: logical replication launcher 

**highgo   8055  8038 0 11:07 ?    00:00:00 postgres: wal sender process hgreplica 192.168.179.161(35068) streaming 0/4A000098**

# 流复制**备库**正常运行时:

[highgo@node2 ~]$ ps -ef | grep postgres 

highgo   8004   1 1 11:07 pts/0  00:00:00 /opt/HighGoDB-5.6.4/bin/postgres

highgo   8009  8004 0 11:07 ?    00:00:00 postgres: logger process  

highgo   8010  8004 0 11:07 ?    00:00:00 postgres: startup process  recovering 00000001000000000000004A

highgo   8011  8004 0 11:07 ?    00:00:00 postgres: checkpointer process 

highgo   8012  8004 0 11:07 ?    00:00:00 postgres: writer process  

highgo   8013  8004 0 11:07 ?    00:00:00 postgres: stats collector process 

highgo   8014  8004 0 11:07 ?    00:00:00 postgres: bgworker: pg_wait_sampling collector 

**highgo   8015  8004 1 11:07 ?    00:00:00 postgres: wal receiver process  streaming 0/4A000098**
```

从上述加粗的内容可以看到，主备库的 wal 进程是有区别的，流复制中主库会向备库发送 wal 日志，所以主库存在 wal sender 进程，备库则会有 wal receiver 进程

ps:

（1）也可以直接进行 wal 进程的查看来进行主备库的区分

```
# 流复制主库显示如下: 

[highgo@node1 ~]$ ps -ef | grep wal 

highgo   8047  8038 0 11:07 ?    00:00:00 postgres: wal writer process  

highgo   8055  8038 0 11:07 ?    00:00:00 postgres: wal sender process hgreplica 192.168.179.161(35068) streaming 0/4A00C5B8

# 流复制备库显示如下: 

[highgo@node2 ~]$ ps -ef | grep wal 

highgo   8015  8004 0 11:07 ?    00:00:00 postgres: wal receiver process  streaming 0/4A00C5B8
```

（2）另外，如果存在级联备库（向流复制备库请求 wal ），则流复制备库上也会存在 wal sender 进程

### 4、通过文件系统查看数据库的运行状态

（1）数据库是否处于运行状态:

```
# 数据库处于运行状态时会存在下列文件:

[highgo@localhost data]$ ls -lrth | grep postmaster.pid

-rw------- 1 highgo highgo  82 Jul 23 10:41 postmaster.pid

# 数据库处于关闭状态时:

[highgo@localhost data]$ ls -lrth | grep postmaster
```

（2）主备库的差别

```
# 备库存在 recovery.conf 文件

[highgo@node2 data]$ ls -lrth | grep recovery

-rw-rw-r-- 1 highgo highgo 375 Jun 17 10:12 recovery.conf

# 如果主备流复制已经做过至少一次主备切换，主库上会存在 recovery.done 文件

[highgo@node2 data]$ ls -lrth | grep recovery

-rw-rw-r-- 1 highgo highgo 375 Jun 15 10:12 recovery.done
```