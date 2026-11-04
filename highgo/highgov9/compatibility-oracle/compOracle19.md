---
title: "伪列"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle19.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 伪列

## ROWID

### 说明

Rowid显示为 (tableOid, seqno)，其中tableOid 为表的OID。seqno是一个唯一的序列值。Rowid数据类型是一个复合类型其包含两个属性rowoid, rowno，rowoid对应Rowid列的tableOid, rowno对应Rowid列的seqno。

### 示例

1、全局生效，影响全局创建的表均带有rowid：

set ivorysql.default\_with\_rowids to on; #开启rowid相关的guc参数

highgo=# create table t2 (a int, b int);

CREATE TABLE

highgo=# insert into t2 values(20, 3);

INSERT 0 1

highgo=# insert into t2 values(5, 7);

INSERT 0 1

highgo=# insert into t2 values(4, 9);

INSERT 0 1

#如果不指定rowid，则不显示

highgo=# select \* from t2;

a | b

\-—+—

20 | 3

5 | 7

4 | 9

(3 行记录)

#采用如下两种方式查询数据

#1、直接查询rowid

highgo=# select rowid, \* from t2;

rowid | a | b

\-———-+—-+—

(16409,1) | 20 | 3

(16409,2) | 5 | 7

(16409,3) | 4 | 9

(3 行记录)

#2、通过指定rowid查询

highgo=# select rowid, \* from t2 where rowid = ‘(16409,1)’;

rowid | a | b

\-———-+—-+—

(16409,1) | 20 | 3

(1 行记录)

highgo=# drop table t2;

DROP TABLE

2、仅操作单表生效：

highgo=# create table t2 (a int, b int) with rowid;

CREATE TABLE

highgo=# insert into t2 values(20, 3);

INSERT 0 1

highgo=# insert into t2 values(5, 7);

INSERT 0 1

highgo=# insert into t2 values(4, 9);

INSERT 0 1

highgo=# select rowid, \* from t2;

rowid | a | b

\-———-+—-+—

(16417,1) | 20 | 3

(16417,2) | 5 | 7

(16417,3) | 4 | 9

(3 行记录)

highgo=# select rowid, \* from t2 where rowid = ‘(16417,2)’;

rowid | a | b

\-———-+—+—

(16417,2) | 5 | 7

(1 行记录)

highgo=# drop table t2;

DROP TABLE

## ROWNUM

### 说明

当查询返回结果集后，结果集中的每一行记录都有一个ROWNUM列，该列返回一个数字，指示从表或一组连接的行中选择行的顺序。第一行的ROWNUM为1，第二行为2，依此类推。

支持Select、Update、Delete、Merge等操作。

### 示例

highgo=# create table members(id int,name varchar2(10));

CREATE TABLE

highgo=#

highgo=#

highgo=# insert into members values(1,’成员1’);

INSERT 0 1

highgo=# insert into members values(2,’成员2’);

INSERT 0 1

highgo=# insert into members values(3,’成员3’);

INSERT 0 1

\--select操作

highgo=# select \* from members where rownum < 3;

id | name

\-—+——-

1 | 成员1

2 | 成员2

(2 rows)

\--update操作

highgo=# alter table members add depno int;

ALTER TABLE

highgo=# update members set depno=rownum;

UPDATE 3

highgo=# select \* from members;

id | name | depno

\-—+——-+——-

1 | 成员1 | 1

2 | 成员2 | 2

3 | 成员3 | 3

(3 rows)

\--delete操作

highgo=# delete from members where rownum < 2;

DELETE 1

highgo=# select \* from members;

id | name | depno

\-—+——-+——-

2 | 成员2 | 2

3 | 成员3 | 3

(2 rows)