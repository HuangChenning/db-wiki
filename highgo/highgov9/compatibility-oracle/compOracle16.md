---
title: "虚拟列"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle16.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 虚拟列

## 说明

当查询时，虚拟列看起来像普通表列，是一个表达式，在运行时计算，不存储在数据库中，不能更新虚拟列的值。

在使用虚拟列时，只需要根据指定的语法就能创建包含有虚拟列的表。语法图仅展示虚拟列相关语法内容：

## 示例

1. 虚拟列使用

#创建测试表

highgo=# CREATE TABLE vtest1 (a int PRIMARY KEY, b int GENERATED ALWAYS AS (a \* 2));

CREATE TABLE

highgo=# insert into vtest1 (a) values (1);

INSERT 0 1

#不允许给虚拟列插入值

highgo=# insert into vtest1(a,b) values (1,2);

错误: INSERT operation disallowed on virtual columns

#不允许更新虚拟列值

highgo=# update vtest1 set b = 3 where a = 1;

错误: UPDATE operation disallowed on virtual columns

highgo=# update vtest1 set a = 2 where b = 2;

UPDATE 1

highgo=# delete from vtest1 where b = 4;

DELETE 1

highgo=# SELECT \* FROM vtest1;

a | b

\-–+—

(0 行记录)

highgo=# DROP TABLE vtest1;

DROP TABLE

修改虚拟列

highgo=# create table t1 (id number,product varchar2(50),price number(10,2),price\_with\_tax int generated always as (round(price\*1.2,2)) virtual);

CREATE TABLE

highgo=# insert into t1 (id, product, price) values (1, ‘computer’, 1500);

INSERT 0 1

highgo=# insert into t1 (id, product, price) values (2, ‘bike’, 1000);

INSERT 0 1

highgo=# select \* from t1;

id | product | price | price\_with\_tax

\-—+———-+———+—————-

1 | computer | 1500.00 | 1800

2 | bike | 1000.00 | 1200

(2 行记录)

#更新虚拟列

highgo=# alter table t1 modify (price\_with\_tax int as (round(price\*1.3,2)));

ALTER TABLE

highgo=# select \* from t1;

id | product | price | price\_with\_tax

\-—+———-+———+—————-

1 | computer | 1500.00 | 1950

2 | bike | 1000.00 | 1300

(2 行记录)

#删除虚拟列后，增加虚拟列

highgo=# alter table t1 drop column price\_with\_tax;

ALTER TABLE

highgo=# alter table t1 add (price\_with\_tax int as (round(price\*1.5,2)));

ALTER TABLE

highgo=# select \* from t1;

id | product | price | price\_with\_tax

\-—+———-+———+—————-

1 | computer | 1500.00 | 2250

2 | bike | 1000.00 | 1500

(2 行记录)

highgo=# drop table t1;

DROP TABLE