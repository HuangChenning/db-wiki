---
title: "6、search_path 的使用说明"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/search_path.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## search\_path 的使用说明

在 HGDB 中,想要查看数据库中有什么数据表或者视图,一般会在连接数据库后使用元命令\\d进行查询,而元命令\\d的搜索范围会限定在这个 search\_path 模式搜索路径参数中。

## 1、search\_path 参数默认是 “$user”, public 两个值。

```
highgo=# show search_path; 
   search_path   
-----------------
 "$user", public
(1 row)
```

$user 是指和当前用户的用户名相同的模式,public 就是数据库自带的 public 模式

## 2、在数据库中创建测试模式和数据表进行测试:

```
highgo=# create schema test_schema ;
CREATE SCHEMA
highgo=# create table test_table_public (id int );
CREATE TABLE
highgo=# create table test_schema.test_table_test_schema (id int );
CREATE TABLE
```

## 3、在默认的 search\_path 参数下使用元命令 \\d 查询表是不能把刚建立的表完全查询出来

```
highgo=# \d
                 List of relations
 Schema |           Name           | Type  | Owner  
--------+--------------------------+-------+--------
 public | pg_stat_statements       | view  | highgo
 public | pg_wait_sampling_current | view  | highgo
 public | pg_wait_sampling_history | view  | highgo
 public | pg_wait_sampling_profile | view  | highgo
 public | test_table_public        | table | highgo
(19 rows)
```

## 4、无法查询出来表 test\_table\_test\_schema,原因是数据库搜索是按照模式搜索路径中所列出来的模式进行搜索

将模式搜索路径参数进行暂时性修改:

```
highgo=# set search_path TO public,test_schema;
SET
或者
highgo=# set search_path = public,test_schema;
SET
highgo=# show search_path ;
     search_path     
---------------------
 public, test_schema
(1 row)
```

## 5、再次进行查询:

```
highgo=# \d
                    List of relations
   Schema    |           Name           | Type  | Owner  
-------------+--------------------------+-------+--------
public      | pg_wait_sampling_current | view  | highgo
public      | pg_wait_sampling_history | view  | highgo
public      | pg_wait_sampling_profile | view  | highgo
public      | test_table_public        | table | highgo
test_schema | test_table_test_schema   | table | highgo
```

但是上述修改方式是暂时性修改,只会在本次会话生效,如果断开了数据库连接,再次使用 psql 连接进去数据库,search\_path 参数又会变回默认值

## 6、search\_path 参数是存在于 postgresql.conf 配置文件中的,如果想要永久生效则可以直接修改 postgresql.conf 配置文件:

```
[highgo@localhost ~]$ vi $PGDATA/postgresql.conf

#search_path = '"$user", public'        # schema names
```

## 7、去掉注释符号,将 search\_path 参数的值修改为需要的值即可,不需要重启数据库生效

```
[highgo@localhost ~]$ pg_ctl reload
server signaled
highgo=# show search_path ;
         search_path         
-----------------------------
 "$user", public,test_schema
(1 row)
```