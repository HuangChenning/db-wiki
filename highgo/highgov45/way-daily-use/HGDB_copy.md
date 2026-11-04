---
title: "17、HGDB两表间数据复制语句介绍"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HGDB_copy.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## HGDB两表间数据复制语句介绍

在HGDB中的SELECT INTO和INSERT INTO SELECT两种表复制语句都可以用来复制表与表之间的数据。

## 1、INSERT INTO FROM语句

语句形式为：

```
Insert into Table2(field1,field2,…) select value1,value2,… from Table1
```

要求目标表Table2必须存在，由于目标表Table2已经存在，所以我们除了插入源表Table1的字段外，还可以插入常量。示例如下：

```
highgo=# insert into test1 select id,note from test;
错误:  42P01: 关系 "test1" 不存在
第1行insert into test1 select id,note from test;
                 ^
highgo=# create table test1(id integer,note character varying);
CREATE TABLE
highgo=# insert into test1 select id,note from test;
INSERT 0 6
highgo=# select * from test1;
 id |   note
----+-----------
  1 | abcdefgh
  2 | abcdxyzh
  3 | 123defgh
  4 | ab_cdefgh
  5 | ab%cdxyzh
  6 | abcdhadsw
(6 行记录)
```

## 2、SELECT INTO FROM语句

语句形式为：

```
SELECT vale1, value2 into Table2 from Table1
```

要求目标table2不存在，在插入时会自动创建表Table2，并将Table1中指定字段数据复制到Table2中。

```
highgo=# \d
                 关联列表 
    架构模式    |  名称  |  类型  | 拥有者
----------------+--------+--------+--------
 oracle_catalog | dual   | 视图   | highgo
 public         | people | 数据表 | highgo
 public         | test   | 数据表 | highgo
 public         | test1  | 数据表 | highgo
(4 行记录)
highgo=# select id,note into test2 from test;
SELECT 6
highgo=# \d
                 关联列表   
    架构模式    |  名称  |  类型  | 拥有者
----------------+--------+--------+--------
 oracle_catalog | dual   | 视图   | highgo
 public         | people | 数据表 | highgo
 public         | test   | 数据表 | highgo
 public         | test1  | 数据表 | highgo
 public         | test2  | 数据表 | highgo
(5 行记录)
highgo=# select id,note into test2 from test;
错误:  42P07: 关系 "test2" 已经存在
```