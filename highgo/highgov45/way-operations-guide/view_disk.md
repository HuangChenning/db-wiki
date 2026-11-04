---
title: "24、查看数据库占用磁盘空间的方法"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/view_disk.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 查看数据库占用磁盘空间的方法

## 一、通过系统函数查找

通过系统函数查询数据库大小得到的结果仅为数据库、模式、表等各类逻辑数据对象占用大小，不包含WAL日志、审计日志、数据库运行日志等其他部分。

### 1、查看全部数据库大小之和

```
highgo=# select sum(pg_database_size(datname)) from pg_database;
   sum   
--------------------------
 33227060
(1 row)
highgo=#
highgo=#
highgo=# select pg_size_pretty(sum(pg_database_size(datname))) from pg_database;
 pg_size_pretty
---------------------------
 32 MB
(1 row)
highgo=# select  sum(pg_database_size(datname)) /1024/1024 as "SIZE M" from pg_database;
      SIZE
---------------------------
 31.6877937316894531
(1 row)
```

注：函数pg\_database\_size()得到的结果单位为字节，函数pg\_size\_pretty()得到的结果单位是数据库认为便于观看单位，结果不是非常准确，存在四舍五入。

### 2、查看某几个数据库大小之和，使用过程中将函数内的参数填写对应数据库名称即可。

```
highgo=# select sum(pg_database_size(pg_database.datname))/1024/1024 as "SIZE M" from pg_database where datname in('highgo','template0'); 
total_size
------------
   16744602
(1 row)

highgo=# select pg_size_pretty(sum(pg_database_size(pg_database.datname))) as total_size from pg_database where datname in('highgo','template0'); 
total_size
------------
 16 MB
(1 row)
highgo=# select sum(pg_database_size(pg_database.datname))/1024/1024 as "SIZE M" from pg_database where datname in('highgo','template0');
       SIZE       
---------------------
 15.9688968658447266
(1 row)
```

### 3、查看单个数据库大小明细，使用过程中将函数内的参数填写为对应数据库名称即可。

```
highgo=# SELECT pg_database_size('highgo');
 pg_database_size
------------------
          8576663

(1 row)
highgo=# SELECT pg_size_pretty(pg_database_size('highgo'));

 pg_size_pretty
----------------
 8376 kB
(1 row)
highgo=# SELECT pg_database_size('highgo')/1024/1024 as "SIZE M";

 SIZE
--------
   8
(1 row)
```

### 4、查看数据库集群内各数据库大小明细

```
highgo=# select datname,pg_size_pretty(pg_database_size(datname)) from pg_database;
  datname  | pg_size_pretty
-----------+----------------
 highgo    | 8376 kB
 template1 | 7977 kB
 template0 | 7977 kB
 test      | 8120 kB
(4 rows)
```

## 二、通过查看数据库对应目录大小确定磁盘使用空间

### 1、数据集簇占用大小，包含WAL日志、数据库运行日志等。

如果用户手动创建过表空间，此种情况下还需要统计该表空间所在目录的大小，表空间的路径可通过元命令\\db查看确定。

```
[highgo@host1 base]$ cd $PGDATA
[highgo@host1 data]$ du -sh
49M
```

注：windows环境下找到对应文件夹，鼠标右键查看大小即可。

### 2、数据库各类逻辑对象大小之和，不包含WAL日志、数据库运行日志等，只需查看base、global两个文件夹大小。

如果用户手动创建过表空间，此种情况下还需要统计该表空间所在目录的大小，表空间的路径可通过元命令\\db查看确定。

```
[highgo@host1 data]$ du -sk base global  
32616 base
584 global
[highgo@host1 data]$ du -sm base global 
32 base
1 global
```

注：windows环境下找到对应文件夹，鼠标右键查看大小即可。

### 3、单个数据库大小确定。首先查询数据库oid，通过oid确定数据库存放路径，查看该文件夹大小即可，默认存放路径为$PGDATA/base/oid。

如果数据库使用的是用户自建的表空间，则数据库存放路径为$PGDATA/pg\_tblspc/oid

```
highgo=# select datname,oid from pg_database;
  datname  |  oid 
-----------+-------
 highgo    | 13864
 template1 |     1
 template0 | 13863
 test      | 16444
 tbltest   | 16451
(5 rows)

[highgo@host1 16451]$ cd $PGDATA/base/16444
[highgo@host1 16444]$ du -sm
8 
[highgo@host1 16444]$ du -sk
8140
```

注：windows环境下找到对应文件夹，鼠标右键查看大小即可。