---
title: "16、HGDB表空间迁移"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HGDB_tableq.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## HGDB表空间迁移

## 1、 LINUX下的表空间迁移

### 1.1 、创建表空间

```
highgo=# create tablespace tbs_data location '/data/t_tbs';
CREATE TABLESPACE
查看表空间
highgo=# \db+
                                   List of tablespaces
    Name    | Owner  |  Location   | Access privileges | Options |  Size   | Description
------------+--------+-------------+-------------------+---------+---------+-------------
pg_default | highgo |             |                   |         | 996 MB  |
pg_global  | highgo |             |                   |         | 464 kB  |
tbs_data   | highgo | /data/t_tbs |                   |         | 0 bytes |
(3 rows)
```

### 1.2 、创建模拟数据

方式1：在新表空间创建新对象

```
highgo=# create database test owner htest  TABLESPACE = 'tbs_data';
CREATE DATABASE
```

方式2：将旧的数据对象迁移至新表空间

举例：alter database TEST set tablespace tbs\_data;  
注意：如果是集群环境，则只需要在主库中进行就行了，从库会自动同步。需要注意的事，迁移过程中，TEST库是会加上全局锁的，无法读写。所以在实际中需要协调出业务空闲时间。

查看新表空间下的数据库

```
highgo=# \l+ test
                                             List of databases
Name | Owner | Encoding |  Collate   |   Ctype    | Access privileges |  Size   | Tablespace | Description
------+-------+----------+------------+------------+-------------------+---------+------------+-------------
test | htest | UTF8     | zh_CN.utf8 | zh_CN.utf8 |                   | 7449 kB | tbs_data   |
(1 row)
```

在TEST库中创建识别表bz\_test1;

```
test=# create table bz_test1 (a integer,b integer,c integer ,d integer);
CREATE TABLE
test=# insert into bz_test1 select (random()*(10^5))::integer,(random()*(10^5))::integer,(random()*(10^5))::integer from generate_series(1,1000) ;
INSERT 0 1000
test=#
test=# \dt
         List of relations
Schema |   Name   | Type  | Owner
--------+----------+-------+-------
public | bz_test1 | table | htest
(1 row)

test=# select * from bz_test1 limit 5;
   a   |   b   |   c   | d
-------+-------+-------+---
45394 | 47760 | 27691 |
11743 |  8785 | 19327 |
59565 | 49539 |  1585 |
55315 | 60471 | 39387 |
66894 | 23568 | 54289 |
(5 rows)
```

### 1.3 表空间迁移

查看tbs\_data物理文件状态

```
[highgo@tqz data]$ ll pg_tblspc/
total 0
lrwxrwxrwx. 1 highgo highgo 11 Jul 28 10:22 16557 -> /data/t_tbs
```

迁移DATA目录

此时如果迁移DATA目录，则需要：

方式1（离线迁移）：

关闭数据库复制data目录和表空间目录/data/t\_tbs至目标位置，注意如果t\_tbs目录不存放在$PGDATA/pg\_tblspc/下则需创建软连接到该目录下，例如：

```
[highgo@tqz ~]$ cp -rf  /data/highgo/4.7.7/data /home/highgo/test_c/

pg_ctl start -D /home/highgo/test_c/data/   t_tbs目录未移动位置，软连接仍然生效，直接启动数据库即可
```

如果移动t\_tbs目录

```
[highgo@tqz data]$ mv /data/t_tbs  /home/highgo/
[highgo@tqz data]$ ll pg_tblspc/
total 0
lrwxrwxrwx. 1 highgo highgo 11 Jul 28 10:52 16557 -> 已丢失
```

此时注意：缺少tbs\_data表空间并不意味着不可以登录数据库，除了TEST库不可用外，其余可正常登陆使用。

```
highgo=# \c test htest
FATAL:  3D000: database "test" does not exist
DETAIL:  The database subdirectory "pg_tblspc/16557/PG_9.5_201510051/16558" is missing.
Previous connection kept
```

将表空间新目录路径链接到pg\_tblspc下

```
[highgo@tqz data]$ ln -s /home/highgo/t_tbs  /home/highgo/test_c/data/pg_tblspc/16557
```

启动数据库并查询表的一致性

```
test=# \dt
         List of relations
Schema |   Name   | Type  | Owner
--------+----------+-------+-------
public | bz_test1 | table | htest
(1 row)

test=# select * from bz_test1 limit 5;
   a   |   b   |   c   | d
-------+-------+-------+---
45394 | 47760 | 27691 |
11743 |  8785 | 19327 |
59555 | 49539 |  1585 |
55315 | 60471 | 39387 |
66894 | 23568 | 54289 |
(5 rows)
```

至此整个DATA目录迁移完成。

方式2（在线迁移）：

通过pg\_basebackup命令来在线迁移

\-T, –tablespace-mapping （重新指定tablespace新路径）

举例：

```
[highgo@tqz data]$ pg_basebackup -U highgo -h127.0.0.1 -T /home/highgo/t_tbs=/data/t_tbs  -x -D /home/highgo/test_c/data2
Password:
NOTICE:  00000: pg_stop_backup complete, all required WAL segments have been archived

[highgo@tqz data]$ ll /data/
total 0
drwxr-xr-x. 5 highgo highgo 52 Dec 24  2019 highgo
drwx------. 3 highgo highgo 30 Jul 28 13:46 t_tbs
```

查看迁移后的状态

```
[highgo@tqz data2]$ pg_ctl start -D /home/highgo/test_c/data2
[highgo@tqz data2]$ psql -d test -U htest
test=# select * from bz_test1 limit 5;
   a   |   b   |   c   | d
-------+-------+-------+---
45394 | 47760 | 27691 |
11743 |  8785 | 19327 |
59565 | 49539 |  1585 |
55315 | 60471 | 39387 |
66894 | 23568 | 54289 |
(5 rows)
```

## 2 、WINDOWS下的表空间迁移

Windows下瀚高数据库的表空间迁移方式参考Linux表空间迁移（建议使用方式2）

注意事项：

### 2.1 关于WINDOWS下目录软链接

mklink /J 目标文件（夹） 源文件（夹）

```
使用示例： mklink /J  D:\target-dir  E:\src-dir
```

### 2.2关于数据库服务注册

迁移DATA目录完成后需要重新注册数据库服务

例如：

```
注销服务：pg_ctl unregister -N hgdb-se4.7.7-1
添加服务：pg_ctl register -N hgdb-se4.7.7 -U "NT AUTHORITY\NetworkService" -D "D:\HighGo DataBase\data" -s
```