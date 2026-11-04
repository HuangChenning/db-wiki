---
title: "PSQL兼容SQLPLIS"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle27.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## PSQL兼容SQL\*PLUS

## 说明

### 兼容SQL\*PLUS的var\[iable\]命令

#### 定义绑定变量

使用VARIABLE创建绑定变量，指定绑定变量的数据类型，可选的给绑定变量一个初始值。支持的数据类型如下：

- NUMBER
- CHAR
- CHAR (n \[CHAR | BYTE\])
- NCHAR
- NCHAR (n)
- VARCHAR2 (n \[CHAR | BYTE\])
- NVARCHAR2 (n)
- BINARY\_FLOAT
- BINARY\_DOUBLE

支持的数据类型中只有字符类型可以指定typmod值，同时受nls\_length\_semantics参数影响。

CHAR或NCHAR类型长度的范围是1 ~~2000，varchar2或nvarchar2的长度是1~~ 32767，否则提示错误。

语法：

VAR\[IABLE\] \[variable \[type \[=value\]\]\]

#### 绑定变量赋值

使用VARIABLE直接给某个绑定变量赋值。

语法：

VAR\[IABLE\] variable =value

#### 显示绑定变量特征

使用VARIABLE加变量名来显示某个绑定变量的特性，VARIABLE什么也不跟表示打印所有绑定变量的特性信息。注意，这不是打印变量的值，只是显示绑定变量的名称和类型属性。VARIABLE后面要么没有绑定变量名字，要么只能有一个绑定变量名字，即不能选择显示某几个把绑定变量的特性，只能是显示一个或所有。

语法：

VAR\[IABLE\] \[variable\]

#### 示例

\--number类型

highgo=# variable x number;

highgo=# exec:x:=3.14;

PL/iSQL procedure successfully completed.

highgo=# print x;

X

\-—–

3.14

\--varchar2类型

highgo=# variable y varchar2(20) = ‘highgo database’

highgo=# print y;

Y

\-—————-

highgo database

\--修改x

highgo=# variable x = 3.16

highgo=# print x

X

\-—–

3.16

\--打印所有变量

highgo=# variable

variable x

datatype NUMBER

variable y

datatype VARCHAR2(20)

### 兼容SQL\*PLUS的print命令

使用PRINT加变量名称列表来打印某几个绑定变量的值，如果PRINT忽略变量名列表，则打印所有绑定变量的值。

语法：

PRINT \[variable …\]

#### 示例

\--打印单个变量

highgo=# print x

X

\-—–

3.16

\--打印多个变量

highgo=# print x y

X

\-—–

3.16

Y

\-—————-

highgo database

\--打印所有变量

highgo=# print

X

\-—–

3.16

Y

\-—————-

highgo database

### 兼容SQL\*PLUS的exec\[ute\]命令

执行一个单个的PL/SQL语句，EXECUTE 命令通常按如下方式使用。

语法：

EXEC\[UTE\] statement

此处statement 表示一个PL/SQL语句。

例子：

如果变量:n已经由下面定义：

VARIABLE n NUMBER

以下 EXECUTE 命令为绑定变量 n 赋值：

EXECUTE:n:= 1

PL/SQL procedure successfully completed.

### 兼容SQL\*PLUS的系统变量

#### SERVEROUTPUT

该功能在V9.0.5及以后的版本中支持。

兼容Oracle中的系统变量SERVEROUTPUT，用于控制是否在屏幕上显示由 PL/iSQL 程序或存储过程通过 DBMS\_OUTPUT.PUT\_LINE 过程输出的文本。DBMS\_OUTPUT行长度限制为32767字节。OFF表示不显示DBMS\_OUTPUT.PUT\_LINE的输出，ON表示显示输出。

语法：

```
SET SERVEROUT[PUT] {ON | OFF}
```

说明：

- 设置为ON：启用DBMS\_OUTPUT系统包功能，并且在客户端中显示输出。如果仅执行DBMS\_OUTPUT.ENABLE，而客户端没有设置 SET SERVEROUTPUT ON，将看不到任何输出内容。
- 设置为OFF：禁用DBMS\_OUTPUT系统包功能。清除缓存。

以下是一个简单的示例。

在psql中执行以下语句，结果显示如下：

```
BEGIN

 DBMS_OUTPUT.PUT_LINE('Task is complete');

END;

/

--输出：

PL/iSQL procedure successfully completed.
```

设置SERVEROUTPUT的值，put\_line中的内容会打印到屏幕中：

```
--设置变量值

set SERVEROUTPUT on;

--执行语句

BEGIN

 DBMS_OUTPUT.PUT_LINE('Task is complete');

END;

/

--输出：

Task is complete

PL/iSQL procedure successfully completed.
```