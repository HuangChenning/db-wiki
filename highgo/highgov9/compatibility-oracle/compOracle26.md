---
title: "CALL调用"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle26.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## CALL调用

## 说明

瀚高数据库管理系统V9.0中的CALL语句支持调用单独的函数存储过程，也可以是在包或对象类型中的函数和存储过程。CALL调用函数增加INTO子句语法，插入的目标是一个host variable。

绑定变量在CALL语句中可以是一个输入绑定变量或输出绑定变量，取决于使用方式，如用在参数中依据参数的IN、OUT、INOUT模式，IN模式参数对应的是输入绑定变量、OUT/ INOUT参数是输出绑定变量，函数调用的INTO子句中引用的绑定变量是输出绑定变量。CALL调用函数和存储过程的参数或INTO子句中引用绑定变量。

## 示例

\--call into

highgo=# create or replace function f\_defs(a number default 1314)

highgo-# return number

highgo-# is

highgo-# begin

highgo-# raise notice ‘%’, a;

highgo-# return a;

highgo-# end;

highgo-# /

CREATE FUNCTION

highgo=# variable x number

highgo=# call f\_defs() into:x;

NOTICE: 1314

Call completed.

highgo=# print x

X

\-—–

1314

\--call调用包

highgo=# create table tb1(c1 int);

CREATE TABLE

highgo=# create or replace package pkg is

highgo-# var1 integer;

highgo-# procedure test\_p;

highgo-# end;

highgo-# /

CREATE PACKAGE

highgo=# create or replace package body pkg is

highgo-# procedure test\_p is

highgo-# begin

highgo-# insert into tb1 values(1);

highgo-# end;

highgo-# begin

highgo-# var1:= 2;

highgo-# end;

highgo-# /

CREATE PACKAGE BODY

highgo=# call pkg.test\_p();

Call completed.

highgo=# select \* from tb1;

c1

\-—

1

(1 row)

## 限制

1、CALL调用无参或全取默认值的函数/存储过程不能省略空括号。

2、CALL调用的函数参数数量取决于configure时的指定的大小，受block\_size的限制。最大值依赖block\_size大小，8kb最大600个，16kb最大1200个，32kb最大2400个。

3、CALL语句中OUT参数对应的绑定变量支持对精度和数据类型的验证，即超出精度可能报错也可能截断，规则如下：

首先绑定变量只有字符类型允许指定精度，因此对于精度溢出的情景只需要考虑字符类型的绑定变量即可。假设一个声明为字符类型的绑定变量的精度在接收函数或存储过程OUT参数或返回值时一定会溢出，那么当溢出时是选择报错还是选择截断输出字符串，规则如下：

- 当绑定变量数据类型与OUT参数/返回值的数据类型相同时，采用截断策略。
- 当绑定变量数据类型与OUT参数/返回值的数据类型不同时，采用报错策略。
- 输出绑定变量不允许被重复绑定。