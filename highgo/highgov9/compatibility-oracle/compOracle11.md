---
title: PACKAGE
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle11.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## PACKAGE

## 说明

Package是一组相关过程、函数、变量、常量、类型和游标等PL/SQL程序设计元素的组合。包具有面向对象设计的特点，是对这些PL/SQL程序设计元素的封装。

(1)声明或定义：包定义部分是创建包的规范说明，声明包内数据类型、变量、常量、游标等元素。

这部分也是为使用者提供了透明的接口。

(2)包体:包体是包定义部分的具体实现。

(3)将有联系的对象打成包,方便使用。

(4)包中对象包括储存过程,函数,游标,自定义类型和变量,可以在PL/SQL块中应用这些对象。

### 创建包

使用CREATE PACKAGE语句创建或替换一个包的规范，包是相关的存储过程、函数、和其他程序对象的集合，在数据库中作为一个单元存储。包规范声明这些对象，在包体中定义这些对象。

- OR REPLACE:

如果包存在，则重建一个包，并重新编译，在包重定义之前被授予包上的权限的用户仍然可以访问包，而不需要重新授权。

如果任何基于函数的索引依赖该包，则数据库会标记该索引disabled。

- \[EDITIONABLE|NONEDITIONABLE\]

标记该package对象是否是可编辑的，目前该功能仅支持语法，默认是EDITIONABLE。

- Schema

包所在的模式名字。

- Sharing\_clause

该子句指明包使用什么样的共享属性，仅仅支持在application root环境下创建对象。

- METADATA 共享数据字典，但数据对每个容器是不同的，
- NONE 该对象不是共享的，只能被application root访问

如果没有指定该子句，则由初始化参数DEFAULT\_SHARING决定，如果该参数没有值，则默认是METADATA。

目前仅支持语法。

- Default collation clause

字符串排序集，仅支持语法。

- invoker\_rights\_clause

指定包中函数、存储过程以及包规范中声明的显示游标的AUTHID，目前仅支持语法。

- accessible\_by\_clause

指定可以调用该包的每个访问器，目前仅支持语法。

- item\_list\_1

定义包中的类型、声明游标和子过程，每个声明必须在包中有其定义。除了空格外，包规范中声明与包体中定义需要严格字符一致。不允许有PRAGMA AUTONOMOUS\_TRANSACTION出现，具体内容由普通函数声明部分决定，这部分内容俗称包的公有对象，外部可以通过包名.xxx来引用或赋值。

### 创建包体

需要有与CREATE PACKAGE一样的权限，且要求包体与包规范在同一个模式下，且包规范必须存在，该语句定义包规范中声明的对象。

当包规范中有cursor或子过程时，那么必须拥有一个包体去定义它，否则包体是可选的。

- OR REPLACE

如果包体已存在，则重建包体并重新编译包体。

在包体重定义之前被授予包体上权限的用户仍然可以访问包，而不需要重新授权。

- \[EDITIONABLE|NONEDITIONABLE\]

如果没有指定这个属性，则从包规范中继承，如果设置了，则需和包规范一致。

- declare\_section

包含包规范中声明的游标和子程序的定义，对应的子程序的声明和定义的头部除空白外，必须完全匹配。

在包体中还可以声明并定义只能被包内引用的私有对象。

此处不能出现PRAGMA AUTONOMOUS\_TRANSACTION.

- initialize\_section

初始化变量，以及一些一次性设置的步骤。

### 更新包或包体

ALTER PACKAGE语句显示地重新编译包规范、包体或两个都重新编译。显示的重新编译消除了运行时的隐式重编译，阻止了相关运行时的编译错误和性能消耗。

由于包中的所有对象是作为一个单元进行存储的，所以ALTER PACKAGE会对包中的所有对象进行重新编译，不能使用ALTER PROCEDURE或ALTER FUNCTION语句来编译包中的某个存储过程或函数。

此语句不会改变已存在的包的声明或定义，如果想要重新声明或重新定义一个包，需要使用含OR REPLACE子句的CREATE PACKAGE或CREATE PACKAGE BODY语句。

- COMPILE

重新编译PL/SQL单元，无论它是有效和无效的

首先，如果该单元依赖的任何对象无效，数据库将重新编译它们。数据库还会使依赖于该单元的任何本地对象失效。如果数据库成功重新编译单元，则该单元将变为有效，否则数据库将返回错误，并且该单元标记仍然无效。

在重新编译期间，数据库会丢弃所有持久的编译器开关设置，并从会话中重新检索它们，并在编译后存储它们。要避免此过程，请指定REUSE SETTINGS.

- DEBUG

具有与PLSQL\_OPTIMIZE\_LEVEL=1 相同效果，指示PL/SQL编译器生成和存储由PL/SQL调试器使用的代码，仅支持语法。

- SPECIFICATION

只重新编译包规范，不管包规范有效或无效，在修改包规范后，可以通过重新编译包规范来查看是否有编译错误。

当重新编译一个包规范时，数据库会将所有依赖此包规范的本地对象失效，比如调用包中存储过程或函数的子过程。包体也依赖它的包规范，如果在随后引用这些依赖对象时没有提前重新编译这些依赖对象，则数据库会在运行时，重新编译这些依赖对象。

- BODY

只重新编译包体，不管包体是否有效。在修改了包体之后，可以通过此语句重新编译包体，重新编译包体不会导致那些依赖包规范的对象失效。

当重新编译包体时，如果包体依赖的对象失效，则数据库首先重新编译包体依赖的失效对象，如果重新编译包体成功，则包体变为有效。

- PACKAGE

重新编译包规范和包体，不管他们是否有效，重新编译包规范和包体，会导致失效和重新编译依赖此包的对象。

- REUSE SETTINGS

防止数据库丢弃并重新获取编译器开关设置。使用此子句保留现有设置，并使用它们来重新编译此语句中其他地方未指定值的任何参数，只支持语法。

- Compiler\_parameters\_clause

指定PL/SQL的编译参数的值，这些值存储在每个PL/SQL单元的数据字典中，仅支持其语法。

### 删除包或包体

DROP PACKAGE 语句删除数据库中的一个存储包。这个语句会同时删除包体和包规范。不能使用此语句删除包中的一个单独对象。

- BODY

只删除包体，如果没有这个子句，则数据库会将包规范和包体都删除。

如果只删除包体，不删除包规范，则数据库不会将依赖包的本地对象失效。

但是在重建包体之前，不能再调用包规范中声明的存储过程或函数。

- 数据库会失效依赖包规范的本地对象。如果随后引用这些本地对象时，数据库重新编译本地对象，如果被删除的包没有被重建，则返回一个错误。
- 如果任何统计类型与包关联，则数据库将使用FORCE子句来断开统计数据类型与包的关联，并删除使用统计类型收集的任何用户定义的统计信息。

### DISCARD PACKAGE

该功能是为兼容PG的DISCARD功能做的，目前PG支持DISCARD SEQUENCE、DISCARD TEMP、DISCARD PLAN等用来删除当前session的序列、临时表以及计划等缓存，并且DISCARD ALL支持删除本session的PORTAL、临时表、计划、序列等临时存储

支持DISCARD PACKAGE语法，并且在DISCARD ALL中调用函数删除本session的PACKAGE缓存。

## 示例

1\. 创建并查看包规范

create package pkg is

var1 integer;

function test\_f(id integer) return integer;

end;

/

create or replace package body pkg is

function test\_f(id integer) return integer is

begin

return id+5;

end;

begin

end;

/

2.查看包规范

\\dk pkg

3.调用函数

select pkg.test\_f(100) from dual;

4.替换包体内容

create or replace package body pkg is

function test\_f(id integer) return integer is

begin

return id+15;

end;

begin

end;

/

5.调用函数

select pkg.test\_f(100) from dual;

6.删除包

drop package pkg;

7.释放资源

discard package;