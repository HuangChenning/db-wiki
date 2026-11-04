---
title: "4、HighGo Database删除表中的重复数据"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/delete_repeat.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## HighGo Database删除表中的重复数据

## 1、文档用途

本文适用于提供在HighGo Database中，没有主键及唯一索引的情况下，如何清理重复数据。

本文中提供的删除方法不会判断数据的有效性，实际环境中，如数据保留有要求，需谨慎使用。

## 2、详细信息

创建测试用表

```
highgo=# create table test(id int,name varchar);

CREATE TABLE

highgo=#
```

插入测试数据

```
highgo=# insert into test values(1,'hgdb1');

INSERT 0 1

highgo=# insert into test values(2,'highgo1');

INSERT 0 1

highgo=# insert into test values(2,'highgo2');

INSERT 0 1

highgo=# insert into test values(3,'hgdb1');

INSERT 0 1

highgo=# insert into test values(3,'hgdb2');

INSERT 0 1

highgo=# insert into test values(3,'hgdb3');

INSERT 0 1

highgo=#
```

查看重复值的情况

```
highgo=# select id, count(*) from test group by id having count(*) > 1;

 id | count 

----+-------

  3 |     3

  2 |     2

(2 rows)
```

ctid类似oracle中的rowid，可以标记唯一数据，如下所示

```
highgo=# select ctid, * from test;

 ctid  | id |  name   

-------+----+---------

 (0,1) |  1 | hgdb1

 (0,2) |  2 | highgo1

 (0,3) |  2 | highgo2

 (0,4) |  3 | hgdb1

 (0,5) |  3 | hgdb2

 (0,6) |  3 | hgdb3

(6 rows)
```

查询出重复数据

```
highgo=# select * from test where ctid not in (select max(ctid) from test group by id);

 id |  name   

----+---------

  2 | highgo1

  3 | hgdb1

  3 | hgdb2

(3 rows)
```

删除重复数据

```
highgo=# delete from test where ctid not in (select max(ctid) from test group by id);

DELETE 3

highgo=# select * from test;

 id |  name   

----+---------

  1 | hgdb1

  2 | highgo2

  3 | hgdb3

(3 rows)
```

其他的写法

```
highgo=# delete from test a where a.ctid <>(select max(b.ctid) from test b where a.id = b.id);

DELETE 3

highgo=# 

highgo=# select * from test;

 id |  name   

----+---------

  1 | hgdb1

  2 | highgo2

  3 | hgdb3

(3 rows)
```