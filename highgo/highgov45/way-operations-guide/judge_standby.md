---
title: "1、 判断流复制主备角色的方法"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/judge_standby.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 判断流复制主备角色的方法

HighGo Database进行流复制维护操作之前首先要知道当前数据库的角色，测试环境为一主一备，如何判断数据库角色？

提供以下4种方法进行判断：

## 1、通过 pg\_controldata 命令查看数据库的控制信息，Database cluster state 字段信息可判断是主库还是备库。

主库返回 in production：

```
[highgo@localhost ~]$ pg_controldata |grep cluster
Database cluster state:    in production
```

备库返回 in archive recovery：

```
[highgo@localhost ~]$ pg_controldata |grep cluster
Database cluster state:    in archive recovery
```

## 2、通过进程查看，ps -ef | grep wal | grep -v grep。

显示 wal sender …streaming 进程表示当前数据库为主库：

```
[highgo@localhost ~]$ ps -ef | grep wal | grep -v grep
highgo 10625    10239    0  07:03 ?  00:00:00  postgres:  wal writer process 
highgo 14540    10239    0 10:00  ? 00:00:00 postgres: wal  sender process repuser 192.168.168.168(63146) streaming 0/100991F8
```

显示 wal receiver …streaming 进程表示当前数据库为备库：

```
[highgo@localhost ~]$ ps -ef | grep wal | grep -v grep
highgo        18692    18687    0 10:00 ?    00:00:00 postgres: wal receiver process    streaming 0/100991F8
```

## 3、通过查看数据字典表 pg\_stat\_replication。

进入psql 客户端，输入select \* from pg\_stat\_replication;

主库在表中能查到记录：

```
highgo=# select * from pg_stat_replication;
  pid  | usesysid | usename  | application_name | client_addr | client_hostname | client_port |         backend_start         | backend_xmin |   state   |  sent_lsn  | write_lsn  | flush_lsn  | replay_lsn | write_lag | flush_lag | replay_lag | sync_priority | sync_state |          reply_time 
-------+----------+----------+------------------+-------------+-----------------+-------------+-------------------------------+--------------+----
-------+------------+------------+------------+------------+-----------+-----------+------------+---------------+------------+------------------------
 29612 |       10 | postgres | walreceiver      |             |                 |          -1 | 2021-12-22 15:13:09.966562+08 |              | streaming | 1/1676EE18 | 1/1676EE18 | 1/1676EE18 | 1/1676EE18 |           |           |            |             1 | sync       | 2022-02-16 14:33:20.844851+08
```

备库在表中无记录：

```
highgo=# select * from pg_stat_replication;
  pid  | usesysid | usename  | application_name | client_addr | client_hostname | client_port | backend_start | backend_xmin | state |  sent_lsn  | write_lsn  | flush_lsn  | replay_lsn | write_lag | flush_lag | replay_lag | sync_priority | sync_state |  reply_time
-------+----------+----------+------------------+-------------+-----------------+-------------+-------------------------------+--------------+----
-------+------------+------------+------------+------------+-----------+-----------+------------+---------------+------------+--------------------
```

## 4、通过系统函数 pg\_is\_in\_recovery()判断。

进入 psql 客户端，输入 select pg\_is\_in\_recovery();主库返回 f：

```
highgo=# select pg_is_in_recovery(); 
pg_is_in_recovery
-------------------
f
(1 row)

备库返回 t：
highgo=# select pg_is_in_recovery(); 
pg_is_in_recovery
-------------------
t
(1 row)
```