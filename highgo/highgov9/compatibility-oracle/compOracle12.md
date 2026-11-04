---
title: "全局临时表"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle12.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 全局临时表

## 说明

在数据库中临时表在需要缓存（临时保留）结果集的应用程序中很有用，临时表保存仅在事务或会话期间存在的数据。全局临时表是临时表中的一种类型，它是存储在磁盘上的永久数据库对象，全局临时表的元数据对多个用户及其会话可见，但其内容对会话而言是本地的。

使用 CREATE GLOBAL TEMPORARY TABLE 语句创建全局临时表，ON COMMIT子句指示表中的数据是特定于事务（默认）还是特定于会话，其含义如下：

| **ON COMMIT 选项** | **描述** |
| --- | --- |
| DELETE ROWS | 这创建了一个全局性的临时表，是针对事务的。当事务第一次插入全局临时表时，会话就被绑定到该表。绑定在事务结束后就消失了。数据库在每次提交后都会截断该表（删除所有行） |
| PRESERVE ROWS | 这将创建一个全局临时表，该表是针对会话的。在会话中第一次插入表时，会话会被绑定到全局临时表上。这种绑定在会话结束时或在会话中对表发出TRUNCATE时消失。当你终止会话时，数据库会截断该表 |

第一次创建临时表时，它的元数据存储在数据字典中，但没有为表数据分配空间。在对表执行第一个 DML 操作时为表段分配空间。临时表定义以与常规表定义相同的方式持久存在，但表段和表包含的任何数据都是特定于会话或特定于事务的数据。可以使用 ON COMMIT 子句指定表段和数据是会话特定的还是事务特定的。

通过对表执行 INSERT 操作，会话将绑定到临时表。使用 TRUNCATE 语句或在会话终止时，或者对于特定于事务的临时表，通过发出 COMMIT 或 ROLLBACK 语句，会话将解除绑定到临时表。

## 示例

\--会话临时表示例

\--session1

highgo=# create global temporary table tmp (d number) on commit preserve rows;

CREATE TABLE

highgo=# insert into tmp values (1);

INSERT 0 1

highgo=# select \* from tmp;

d

\-–

1

(1 row)

highgo=# select \* from tmp;

d

\-–

1

(1 row)

highgo=#

\--session2

highgo=# insert into tmp values (100);

INSERT 0 1

highgo=# select \* from tmp;

d

\-—-

100

(1 row)

\--事务临时表

\--当事务提交后，数据不保留

highgo=# create GLOBAL TEMPORARY table foo2(

highgo(# bar int,

highgo(# name varchar(100)

highgo(# ) ON COMMIT DELETE ROWS;

CREATE TABLE

highgo=# begin;

BEGIN

highgo=\*# insert into foo2 values(1,’highgo’);

INSERT 0 1

highgo=\*# select \* from foo2;

bar | name

\-—-+——–

1 | highgo

(1 row)

highgo=\*# end;

COMMIT

highgo=# select \* from foo2;

bar | name

\-—-+——

(0 rows)

## 限制

- 全局临时表上不能指定任何外键约束（foreign key constraints）
- 全局临时表不能包含嵌套表的列
- 全局临时表不支持并行UPDATE、DELETE和MERGE
- 全局临时表不能包含 INVISIBLE列
- 全局临时表不支持并行操作