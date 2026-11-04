---
title: "PLSQL数据类型"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle24.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## PLSQL数据类型

## %TYPE

### 说明

%TYPE支持以下两种定义形式，scalar\_variable\_name和db\_table\_or\_view\_name. column\_name，表示常规变量名和表/视图名.列名：

1、常规变量名：scalar\_variable\_name%TYPE

2、表或视图的列：db\_table\_or\_view\_name. column\_name %TYPE

### 示例

highgo=# create table t1(unique1 int);

CREATE TABLE

highgo=# insert into t1 select generate\_series(1,100);

INSERT 0 100

highgo=# create or replace procedure p1(id int)

highgo-# as

highgo-# curs1 CURSOR FOR SELECT \* FROM t1;

highgo-# curs2 refcursor;

highgo-# curs3 CURSOR (key integer) FOR SELECT \* FROM t1 WHERE unique1 = key;

highgo-# curs4 curs1%TYPE;

highgo-# curs5 curs2%TYPE;

highgo-# curs6 curs3%TYPE;

highgo-# BEGIN

highgo-# OPEN curs1;

highgo-# CLOSE curs1;

highgo-# END;

highgo-# /

CREATE PROCEDURE

highgo=# call p1(1);

Call completed.

highgo=# \\df+ p1

List of functions

Schema | Name | Result data type | Argument data types | Type | Volatility | Parallel | Owner | Security | Access privileges | Language | Source code

| Description

\-——-+——+——————+———————+——+————+———-+————+———-+——————-+———-+————————————————————–

\-———+————-

public | p1 | | IN id integer | proc | volatile | unsafe | highgo| definer | | plisql | curs1 CURSOR FOR SELECT \* FROM t1;

+|

| | | | | | | | | | | curs2 refcursor;

+|

| | | | | | | | | | | curs3 CURSOR (key integer) FOR SELECT \* FROM t1 WHERE uniqu

e1 = key;+|

| | | | | | | | | | | curs4 curs1%TYPE;

+|

| | | | | | | | | | | curs5 curs2%TYPE;

+|

| | | | | | | | | | | curs6 curs3%TYPE;

+|

| | | | | | | | | | | BEGIN

+|

| | | | | | | | | | | OPEN curs1;

+|

| | | | | | | | | | | CLOSE curs1;

+|

| | | | | | | | | | | END

|

(1 row)

## %ROWTYPE

### 说明

支持表名%ROWTYPE或视图名%ROWTYPE作为函数或存储过程参数类型和函数返回值类型。

%ROWTYPE声明的变量不会继承引用表的初始值或约束。

注意事项：

支持查询列赋值给一个%ROWTYPE变量，例如：SELECT \* INTO %rowtype声明的变量 FROM *table*; 需要注意的是：如果查询的列数少于或多于%rowtype声明的变量成员个数，默认情况下不报错。只有set plisql.extra\_errors = ‘all’; 才会报错。

### 示例

highgo=# create table tb1(id int,name varchar(5));

CREATE TABLE

highgo=# insert into tb1 values(1,’sam’);

INSERT 0 1

highgo=# insert into tb1 values(2,’amy’);

INSERT 0 1

highgo=# declare

highgo-# var1 tb1%rowtype;

highgo-# begin

highgo-# select id,name into var1 from tb1 where id=2;

highgo-# raise notice ‘id:%,name:%’,var1.id,var1.name;

highgo-# end;

highgo-# /

NOTICE: id:2,name:amy

PL/iSQL procedure successfully completed.

#当源和目标的字段不匹配，则提示错误信息

highgo=# set plisql.extra\_errors = ‘all’; –设置参数

SET

highgo=# declare

highgo-# var1 tb1%rowtype;

highgo-# begin

highgo-# select id into var1 from tb1 where id=2;

highgo-# end;

highgo-# /

ERROR: Return rowtype or query do not match

背景: PL/iSQL function inline\_code\_block line 4 at SQL statement

## RECORD

### 说明

RECORD类型是一个局部类型，只在声明它的块中使用。如果定义在独立的或包子程序中，RECORD类型存储在数据库中。

定义在包规范中的RECORD类型是公共的，可以在包外通过package\_name.type\_name引用RECORD类型。因为它存储在数据库中直到通过DROP PACKAGE语句删除包。

### 示例

CREATE TABLE employees ( employee\_id NUMBER, first\_name VARCHAR2(50), last\_name VARCHAR2(50), salary NUMBER );

INSERT INTO employees (employee\_id, first\_name, last\_name, salary) VALUES (1, ‘John’, ‘Doe’, 50000);

INSERT INTO employees (employee\_id, first\_name, last\_name, salary) VALUES (2, ‘Jane’, ‘Smith’, 55000);

INSERT INTO employees (employee\_id, first\_name, last\_name, salary) VALUES (3, ‘Alice’, ‘Johnson’, 60000);

DECLARE

\-- 定义一个 RECORD 类型

TYPE employee\_record IS RECORD (

employee\_id NUMBER,

first\_name VARCHAR2(50),

last\_name VARCHAR2(50),

salary NUMBER

);

\-- 声明一个该类型的变量

emp employee\_record;

BEGIN

\-- 从 employees 表中选择一行

SELECT employee\_id, first\_name, last\_name, salary

INTO emp

FROM employees

WHERE employee\_id = 1;

\-- 打印结果

raise notice ‘Employee ID:% ‘, emp.employee\_id;

raise notice ‘First Name: %’, emp.first\_name;

raise notice ‘Last Name: %’, emp.last\_name;

raise notice ‘Salary: %’, emp.salary;

END;

/

\--输出结果

NOTICE: Employee ID:1

NOTICE: First Name: John

NOTICE: Last Name: Doe

NOTICE: Salary: 50000

PL/iSQL procedure successfully completed.