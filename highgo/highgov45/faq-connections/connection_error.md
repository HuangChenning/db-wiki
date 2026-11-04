---
title: "8、客户端连接数据库报错：ERROR XX000 missing chunk number x for toast value x in pg_toast_x"
book: "连接使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/connection_error.html"
tags:
  - highgo
  - highgo-v45
  - faq-connections
---

## 客户端连接数据库报错：ERROR: XX000: missing chunk number x for toast value x in pg\_toast\_x

## 1、问题描述

使用客户端工具连接某数据库的表时，出现如下所示报错：

```
ERROR: XX000:missing chunk number 0 for toast value 30982 in pg_toast_2619
```

## 2、问题原因

某张表关联的toast表的data发生损坏。

## 3、解决方案

toast是The OverSized Attribute Storage Technique(超尺寸字段存储技术)的缩写，是超长字段在HighgoDB的一种存储方式。当某表中的超长字段的时候，那这个表会有与之相关联的Toast表。根据toast表的命名规则，假设存在表test的oid为2867，那么如果存在与之相关联的toast表，toast表名为pg\_toast\_2867。

### (1）通过toast的表名pg\_toast\_2619查询出哪张表出现了问题：

```
highgo=# select 2619::regclass;
   regclass
--------------
 pg_statistic
(1 row)
 
highgo=#  select relname,relfilenode,reltoastrelid from pg_class where relname='pg_statistic';
   relname    | relfilenode | reltoastrelid
--------------+-------------+---------------
 pg_statistic |        2619 |          2840
(1 row)
```

### (2） 找到该表后做一下简单的修复：

```
REINDEX table pg_toast.pg_toast_2619;
REINDEX table pg_statistic;
VACUUM ANALYZE pg_statistic;
```

### (3） 定位该表中损坏的数据行。

执行如下函数：

```
DO $$
declare
    v_rec record;
BEGIN
   for v_rec in SELECT * FROM pg_statistic loop
           raise notice 'Parameter is: %', v_rec.ctid;
      raise notice 'Parameter is: %', v_rec;
   end loop;
END;
$$
LANGUAGE plpgsql;
NOTICE:  00000: Parameter is: (46,9)
ERROR:  XX000: missing chunk number 0 for toast value 30982 in pg_toast_2619
CONTEXT:  PL/pgSQL function inline_code_block line 7 at RAISE
```

### (4） 将第3步中定位的记录删除:

```
delete from pg_statistic where ctid ='(46,9)';
```