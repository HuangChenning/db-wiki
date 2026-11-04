---
title: "匿名块"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle9.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 匿名块

## 说明

PL/SQL(Procedural Language/SQL)过程性SQL语言，通过增加了过程性控制结构有效的扩充了SQL的功能。PL/SQL中的基本単位是“块” (block)。所有的 PL/SQL程序都是由“块”构成的，这些块可以顺序出现，也可以相互进行嵌套。

“块”（block）分为两种：命名块和匿名块。

PL/SQL 块由关键字 DECLARE、BEGIN、EXCEPTION 和 END 定义。这些关键字将“块”（block）分为声明部分、可执行部分和异常处理部分。声明和异常部分是可选的，只有可执行部分是必须有的。

匿名块（anonymous block）是没有名字的PL/SQL块。以DECLARE或BEGIN开始，每次提交都被编译。因为匿名块没有名称，所以不能在数据库中存储并且不能直接从其他PL/SQL块中调用。

命名块：包括 [存储过程](https://so.csdn.net/so/search?q=%E5%AD%98%E5%82%A8%E8%BF%87%E7%A8%8B&spm=1001.2101.3001.7020%22%20%5Ct%20%22_blank) 、函数、包和触发器。命名块可以在数据库中存储并在适当的时候调用。

### PLSQL\_BLOCK

#### LABEL

block的标签。

可以为一个block定义多个标签，多个标签可以重名。

如果有嵌套的block，每个block标签可以重名。

同在一个block的子block可以重名。

#### DECLARE

开始Block的声明部分。

#### DECLARE\_SECTION

包含局部声明，这些局部变量只存在于这个block，对于block的子block或相邻的其他block块不可见。

声明部分限制

1. create\_package、create\_package\_body、或 compound\_trigger\_block语句中的declare\_section不能包含PRAGMA AUTONOMOUS\_TRANSACTION。
2. trigger\_body或 tps\_body中的declare\_section不能声明LOGN或LONG RAW类型的变量。

#### BODY

##### BEGIN

开始block的执行部分。包含执行语句。

##### EXCEPTION

Block的异常处理部分。

##### END

表示block结束。

## 示例

create table tb\_log\_block(num int);

declare

v\_word varchar2(20);

n\_len number;

begin

v\_word:= ‘highgo’;

select length(v\_word) into n\_len from dual;

insert into tb\_log\_block(num) values(n\_len);

end;

/