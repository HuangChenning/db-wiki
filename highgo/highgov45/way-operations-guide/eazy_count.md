---
title: "8、简单方便的获取所有表的条数"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/eazy_count.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 简单方便的获取所有表的条数

## 1、文档用途

我们知道oracle里有一个系统表存的rownum。本文旨在介绍在HG数据库中简单方便的获取所有表的条数的方法。

## 2、详细信息

通过如下sql：

```
select relname as 表名, reltuples as 条数 from pg_class where relkind = 'r' and relnamespace = (select oid from pg_namespace where nspname='highgo') order by 条数 desc;
```

效果如下：

```
highgo=# select relname as 表名, reltuples as 条数 from pg_class where relkind = 'r' and relnamespace = (select oid from pg_namespace where nspname='highgo') order by 条数 desc;

   表名    | 条数 

-------------+--------

 t1          |      0

 aaa         |      0

 b           |      0

 test1       |      0

 t           |      0

 d1          |      0

 d2          |      0

 product     |      0

 addressbook |      5

(9 rows)
```

在很多情况下这个值是一个参考值，想更新此值可以通过如下命令：

```
highgo=# select * from t1;

 a | b 

---+---

 3 | a

(1 row)

highgo=# analyze t1;

ANALYZE
```

效果如下：

```
highgo=# select relname as 表名, reltuples as 条数 from pg_class where relkind = 'r' and relnamespace = (select oid from pg_namespace where nspname='highgo') order by 条数 desc;

   表名    | 条数 

-------------+--------

 t1          |      1

 aaa         |      0

 b           |      0

 test1       |      0

 t           |      0

 d1          |      0

 d2          |      0

 product     |      0

 addressbook |      5

(9 rows)
```