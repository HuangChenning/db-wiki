---
title: "14、hghac集群主备数据不一致"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/hghac.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## hghac集群主备数据不一致

## 1、问题描述

hghac集群中主备库数据不一致，存在较大数据差异。

## 2、问题原因

用户修改数据库中流复制相关用户密码后，未修改hghac.yml中的对应的用户密码，也未检查流复制备库连接字符串中的用户密码是否正确，导致流复制断开，集群数据不一致。

## 3、解决方案

查看集群状态主库正常，两个备库均存在数据差异，猜测备库与主库连接已断开。

```
[root@test-hghac-0 /]# /opt/HighGo/tools/hghac/hghactl  list
+ Cluster: test-hghac (6969050704707002401) --+---------+----+-----------+
| Member       | Host               | Role    | State   | TL | Lag in MB |
+--------------+--------------------+---------+---------+----+-----------+
| test-hghac-0 | 10.233.103.89:5866 | Replica | running |    |     689.0 |
| test-hghac-1 | 10.233.105.48:5866 | Replica | running |    |     945.0 |
| test-hghac-2 | 10.233.92.57:5866  | Leader  | running |  6 |           |
+--------------+--------------------+---------+---------+----+-----------+
```

wal进程已停止，检查数据库日志发现如下大量报错：

```
2021-06-28 00:00:14.254 CST,"a_replication","",2328,"127.0.0.1:46089",60d8a08e.918,2,"authentication",2021-06-28 00:00:14 CST,3/47794,0,FATAL,22023,"Too many invalid attempts. Please contact the syssso user to unlock",,,,,,,,,""
2021-06-28 16:13:59.633 CST,"a_rewind","highgo",23226,"10.233.103.85:50824",60d984c7.5aba,2,"authentication",2021-06-28 16:13:59 CST,5/13199,0,FATAL,22023,"Too many invalid attempts. Please contact the syssso user to unlock",,,,,,,,,""
```

登录test-hghac-2服务器，对被锁定的用户进行解锁：

```
[root@test-hghac-2 /]# psql highgo sysdba
Password for user sysdba:
NOTICE:
-------------------------------------------
Login User: sysdba
Login time: 2021-06-30 09:48:10.725705+08
Login Address: [local]
Last Login Status: FAILED
Login Failures: 1
Valied Until: 2022-06-08 15:28:25+08
-------------------------------------------
psql (4.5.6)
Type "help" for help.
highgo=# select user_unlock('a_replication');
highgo=# select user_unlock('a_rewind');
```

解锁完成后，a\_replication用户立刻再次被锁。

与客户沟通后得知客户修改过a\_replication、a\_rewind用户密码，但未修改hghac.yml 以及流复制连接字符串中的用户密码，导致流复制断开主备数据不一致。  
修改流复制相关用户的密码并修改hghac.yml文件以及流复制连接字符串中的信息。

```
[root@test-hghac-2 ]# psql highgo syssso
highgo=> alter user  a_rewind  encrypted password  'test@123';
ALTER ROLE
highgo=> alter user a_replication encrypted password  'test@123';
ALTER ROLE
highgo=> \q
登陆test-hghac-1 以及test-hghac-0 服务器，确认/root/pgpass 中的密码正确后重启备库。
[root@test-hghac-1 ]# cat postgresql.conf |grep primary_conninfo
primary_conninfo = 'user=a_replication passfile=/root/pgpass host=10.10.10.89 port=5866 sslmode=prefer application_name=test-hghac-1'
```

重新启动备库后检查数据库日志以及集群状态：

```
FATAL,XX000,"highest timeline 6 of the primary is behind recovery timeline 7",,,,,,,,,""
[root@test-hghac-0 /]# /opt/HighGo/tools/hghac/hghactl  list
+ Cluster: test-hghac (6969050704707002401) --+---------+----+-----------+
| Member       | Host               | Role    | State   | TL | Lag in MB |
+--------------+--------------------+---------+---------+----+-----------+
| test-hghac-0 | 10.233.103.89:5866 | Replica | crashed |    |   unknown |
| test-hghac-1 | 10.233.105.48:5866 | Replica | stoppped|    |   unknown |
| test-hghac-2 | 10.233.92.57:5866  | Leader  | running |  6 |           |
+--------------+--------------------+---------+---------+----+-----------+
```

因为时间线问题无法将备库加入集群，只能重新初始化集群备库：

```
[root@test-hghac-1 /]# /opt/HighGo/tools/hghac/hghactl  reinit  test-hghac test-hghac-1
[root@test-hghac-0 /]# /opt/HighGo/tools/hghac/hghactl  reinit  test-hghac test-hghac-0
```

完成后查看数据库集群状态：

```
[root@test-hghac-0 /]# /opt/HighGo/tools/hghac/hghactl  list
+ Cluster: test-hghac (6969050704707002401) --+---------+----+-----------+
| Member       | Host               | Role    | State   | TL | Lag in MB |
+--------------+--------------------+---------+---------+----+-----------+
| test-hghac-0 | 10.233.103.89:5866 | Leader  | running |  8 |           |
| test-hghac-1 | 10.233.105.48:5866 | Replica | running |  8 |       0.0 |
| test-hghac-2 | 10.233.92.57:5866  | Replica | running |  8 |       0.0 |
+--------------+--------------------+---------+---------+----+-----------+
```

集群状态正常，处理完成。