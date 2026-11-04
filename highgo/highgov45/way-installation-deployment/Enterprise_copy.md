---
title: "6、HGDB企业版V6逻辑复制搭建"
book: "安装实施类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/Enterprise_copy.html"
tags:
  - highgo
  - highgo-v45
  - way-installation-deployment
---

## HGDB企业版V6逻辑复制搭建

## 一、逻辑复制搭建

### 1、发布端修改数据库运行参数

```
highgo=# alter system set listen_addresses='*';
highgo=# alter system set wal_level='logical';
highgo=# alter system set max_replication_slots=30;
highgo=# alter system set max_wal_senders=40;
highgo=# alter system set max_logical_replication_workers=40;
highgo=# alter system set max_sync_workers_per_subscription=10;
highgo=# alter user postgres with password'postgres';
```

### 2、发布端修改pg\_hba.conf文件，增加以下内容

```
host   all              all    0.0.0.0/0    md5
host replication      all    0.0.0.0/0   md5
```

### 3、发布端重启数据库，使修改后的配置参数生效

```
pg_ctl start
```

### 4、发布端创建用于逻辑复制同步的表，并插入测试数据

```
highgo=# create table test1(id int primary key,txt text);
highgo=# insert into  test1 values(1,'a');
highgo=# insert into  test1 values(2,'b');
highgo=# create table test2(id int primary key,txt text);
highgo=# insert into  test2 values(1,'a');
highgo=# insert into  test2 values(2,'b');
```

### 5、发布节点创建逻辑复制用户

```
highgo=# create user logicalrep replication login encrypted password 'Logical@123';
```

### 6、将发布表的相关权限授权给发布用户。

```
highgo=# grant usage on schema public to logicalrep;
highgo=# grant select on all tables in schema public to logicalrep;
highgo=# alter default privileges in schema public grant select on tables to logicalrep ;
```

### 7、发布节点创建发布

```
highgo=# create publication pub1 for table public.test1,public.test2;
highgo=# select * from pg_publication;  #查询发布详情
```

### 8、订阅端修改数据库运行参数

```
highgo=# alter system set listen_addresses='*';
highgo=# alter system set max_replication_slots=30;
highgo=# alter system set max_wal_senders=40;
highgo=# alter system set max_logical_replication_workers=40;
highgo=# alter system set max_sync_workers_per_subscription=10;
```

### 9、订阅端导出导入发布表的表结构

```
pg_dump -h 192.168.80.251 -d postgres -U postgres -s -t test1 -t test2 -f createtable.sql
psql -f createtable.sql
```

### 11、订阅端创建订阅（必须为超级用户创建订阅）

```
highgo=# create subscription sub1 connection 'host=192.168.230.51 port=5866 dbname=highgo user=logicalrep password=Logical@123' publication pub1;
```

### 12、订阅端查询同步状态

```
highgo=# select * from test1;
 id | txt
----+-----
  1 | a
  2 | b
(2 rows)
highgo=# select * from test2;
 id | txt
----+-----
  1 | a
  2 | b
(2 rows)
```

### 13、插入数据测试

```
##发布端新插入数据
highgo=# insert into test1 values(3,'c');
INSERT 0 1
highgo=# select * from test1;
 id | txt
----+-----
  1 | a
  2 | b
  3 | c
(3 rows)

##订阅端查询数据是否同步
highgo=# select * from test1;  
 id | txt
----+-----
  1 | a
  2 | b
  3 | c
(3 rows)

通过查询同步表内的数据可验证逻辑复制搭建完成。
```

## 二、逻辑复制相关查询

### 1、发布端

```
select * from pg_publication;        ##查询数据库内发布信息
select * from pg_stat_replication;    ##查询流复制相关信息
select * from pg_publication_tables;  ##查询已经发布的表的信息
```

### 2、订阅端

```
select * from pg_subscription;       ##查询订阅信息
select * from pg_subscription_rel;   ##查询每张表的同步状态
select * from pg_replication_origin_status;
```

## 三、逻辑复制注意事项

不支持DDL复制(ALTER TABLE/CREATE TABLE)

不支持TEMPRORARY表和UNLOGGED表复制

不支持Sequences复制（ serial/bigserial/identity）

不支持TRUNCATE操作复制  
不支持大对象复制

不支持视图、物化视图、外部表复制被复制的表上最好有主键约束；如果没有，必须执行：ALTER TABLE reptest REPLICA IDENTITY FULL;

注：订阅端的复制表是可修改的，复制表一旦修改，发布者和订阅者会数据不一致，进而打破复制。