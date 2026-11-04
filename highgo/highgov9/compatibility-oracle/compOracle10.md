---
title: "嵌套子程序"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle10.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 嵌套子程序

## 说明

### 函数

1. function\_declaration

声明一个函数，但不定义，稍后需要在相同的模块，子过程、或包中去定义。

1. function\_heading

函数头部，包括函数名称、参数列表

- Function\_name: 函数名称
- Return datatype: 返回类型，可以是任何的PL/SQL 类型
1. function\_definition

定义一个之前被声明的函数，或者声明定义一个函数

- declare\_section: 函数内部的变量声明与定义
- body: 函数体
1. 函数属性:

Deterministic, pipelined, parallel\_enable, result\_cache

### 存储过程

1. procedure\_declaration:

声明一个存储过程，但不定义，稍后需要在相同模块，子过程、包中去定义。

1. procedure\_heading

Procedure: 存储过程的名字

Procedure\_propertis: 存储过程属性，每一个属性只能出现一次，无顺序要求，嵌套存储过程中不支持。

1. procedure\_definition

定义一个之前被声明的存储过程，或者声明与定义一个存储过程

Declare\_section: 存储过程中的变量声明

Body:过程体

1. call\_spec

将c程序的名字，参数类型以及返回值映射到SQL端，该语句只能出现在SQL端的子过程，包规范和包体中，类型的规范和类型体中，不允许出现在PL/SQL块中，因此在嵌套函数中不支持。

## 示例

create table tb1(id int);

#外层为匿名块，内层为存储过程，执行语句

declare

procedure test\_inlineproc(id integer) is

begin

insert into tb1 values(id);

end;

begin

call test\_inlineproc(1);

end;

/

#外层为匿名块，内层为函数，执行语句

declare

mds integer;

function infunc(id integer) return integer is

begin

insert into tb1 values(id);

return id;

end;

begin

mds:=infunc(2);

end;

/