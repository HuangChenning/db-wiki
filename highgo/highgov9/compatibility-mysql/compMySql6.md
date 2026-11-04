---
title: "大小写兼容"
book: "MySQL兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compMySql6.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-mysql
---

## 大小写兼容

在PG中大小写是不敏感的，而MySQL则大小写敏感。为了兼容MySQL的大小写，瀚高数据库管理系统V9.0采用了两个GUC参数：

- mysql.enable\_case\_switch：大小写的总开关。在开启该参数的情况下，MySQL大小写开启，关闭的情况下，MySQL大小写关闭，保持PG原生的功能不变；
- lower\_case\_table\_names：MySQL大小写参数。该参数决定使用哪种大小写方式。

## 功能

以下是MySQL大小写兼容的主要功能：

| lower\_case\_table\_names表名 | 0 | 1 | 2 |
| --- | --- | --- | --- |
| 库名1、MySQL对应的为pg的模式名。2、真正的库名不受参数控制，创建的名字是什么，存储和使用时都应该是什么。) | 存储：输入什么就是什么，可同名。 使用：严格区分大小写。 | 存储：转为小写，不能有同名的。 使用：不区分大小写。 | 存储：输入什么就是什么，linux可同名，Windows不可同名。 使用：linux严格区分大小写，Windows不区分大小写。 |
| 模式名(在MySQL中与库一致) | 存储：输入什么就是什么，可同名。 使用：严格区分大小写。 | 存储：转为小写，不能有同名的。 使用：不区分大小写。 | 存储：输入什么就是什么，linux可同名Windows不可同名。 使用：linux严格区分大小写，Windows不区分大小写。 |
| 表/视图名/别名/SEQ | 存储：输入什么就是什么，可同名。 使用：严格区分大小写。 | 存储：转为小写，不能有同名的 使用：不区分大小写。 | 存储：输入什么就是什么，linux可同名Windows不可同名。 使用：linux严格区分大小写，Windows不区分大小写。 |
| 列名 | 存储：输入什么就是什么，不能有同名的。使用：不区分大小写。 | 存储：输入什么就是什么，不能有同名的。 使用：不区分大小写。 | 存储：输入什么就是什么，不能有同名的。 使用：不区分大小写。 |
| 用户名 | 存储：输入什么就是什么，可同名。 使用：严格区分大小写。 | 存储：输入什么就是什么，可同名。 使用：严格区分大小写。 | 存储：输入什么就是什么，可同名。 使用：严格区分大小写。 |
| 函数/过程 | 存储：输入什么就是什么，不可同名。 使用：不区分大小写。 | 存储：输入什么就是什么，不可同名。 使用：不区分大小写。 | 存储：输入什么就是什么，不可同名。 使用：不区分大小写。 |
| LANGUAGE | 使用：转小写。 | 使用：转小写。 | 使用：转小写。 |

## 示例

highgo=# show mysql.enable\_case\_switch;

mysql.enable\_case\_switch

\--------------------------

on

(1 row)

highgo=# show lower\_case\_table\_names;

lower\_case\_table\_names

\------------------------

0

(1 row)

highgo=# create database DB;

CREATE SCHEMA

highgo=# create database Db;

CREATE SCHEMA

highgo=# create database dB;

CREATE SCHEMA

highgo=# create database db;

CREATE SCHEMA

highgo=# use DB;

SET

highgo=# create table t1(c binary);

CREATE TABLE

highgo=# \\d

List of relations

Schema | Name | Type | Owner

\--------+------+-------+--------

DB | t1 | table | highgo

(1 row)

highgo=# use Db;

SET

highgo=# \\d

Did not find any relations.