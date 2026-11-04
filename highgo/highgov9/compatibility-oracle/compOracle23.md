---
title: CURSOR
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle23.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## CURSOR

## 说明

### 隐式游标

隐式游标是一个会话级别的游标，由PL/SQL构建和管理，当运行一个SELECT或DML语句时，默认打开一个隐式游标，不能控制隐式游标，但可以从其属性中获得相关信息。

隐式游标的属性语法称之为SQLattribute,因此隐式游标也称作SQL游标。SQLattribute通常指向最近运行的SELECT或DML语句，如果没有该语句运行，则值为NULL。

隐式游标当其关联的语句运行完后将会关闭，然而其属性值在另一个SELECT或DML语句运行前仍然可用。

要保存当前隐式游标属性值以供以后使用，需要将其分配给局部变量，否则，其他操作（如子程序调用）可能会在测试属性之前更改属性的值。

其中各个参数选项如下所示：

- %ISOPE

隐式游标是否打开，bool值，总是false。

- %FOUND

存在以下情况：

- 如果没有SELECT或DML语句执行返回NULL
- 如果最近的SELECT和DML语句返回一行或多行返回true
- 如果最近的SELECT 和DML语句没有返回行返回false
- %NOTFOUND

存在以下情况：

- 如果没有SELECT或DML语句执行返回NULL
- 如果最近的SELECT和DML语句返回一行或多行返回false
- 如果最近的SELECT和DML语句没有返回行则返回true
- %ROWCOUNT

存在以下情况：

- 如果没有SELECT 或DML语句执行返回NULL
- 如果有SELECT或DML语句执行则返回当前被获取的行数

### 显式游标

一个显示游标是一个会话级别的游标，它由用户来构建和管理，可以声明和定义一个显示游标，给显示游标一个名字并将其和一个查询关联，你可以用如下方式处理该查询的结果。

- 使用open语句打开显示游标，使用fetch语句获取查询中的行，以及使用close关闭显示游标
- 在FOR LOOP语句中使用显示游标

### 游标变量及操作

要创建一个游标变量，可以以预定义类型SYS\_REFCURSOR定义变量或者定义一个REF CURSOR类型，然后以该类型定义变量。

游标变量限制：

- 不能在包规范中定义游标变量
- 集合中或数据库的列中不能存储游标变量的值
- 不能使用比较运算符测试游标变量是否相等、不相等或无效
- 在服务器端到服务器远程过程调用（RPC）中使用游标变量会导致错误

#### OPEN FOR操作

在定义好游标变量后，可以使用OPEN FOR语句来打开它，在重新打开游标变量之前，不需要关闭它，在你重新打开游标变量之后，之前和它关联的查询将会丢失。

#### FETCH操作

当打开一个游标变量后，可以使用FETCH语句来从结果集中获取行数据。

#### 给游标变量赋值

可以将一个PL/SQL游标变量的值赋值给另一个PL/SQL 游标变量或者host 游标变量。

### 命名游标属性

显示游标和游标变量都有一个名字与其关联，因此统称命名游标，每个命名游标都有四个属性，这些属性返回关于执行DML或SLEECT操作的信息。

- Named\_cursor
- Explicit\_cursor：显示游标的名字
- Cursor\_parameter：游标类型的参数名字
- Cursor\_variable：游标变量的名字
- :host\_cursor\_variable：主机变量

其中Named\_cursor\_attribute包括如下：

- %ISOPEN

如果cursor被打开，则返回TRUE，否则返回FALSE。

- %FOUND

存在如下值：

- 游标没打开，则报INVALID\_CURSOR异常
- 游标打开了，但没有进行FETCH，NULL
- 最近的FETCH 返回行了，TRUE
- 最近的FETCH没有返回一行，FALSE
- %NOTFOUND

存在如下值：

- 游标没打开，抛出INVALID\_CURSOR异常
- 游标打开，没有FETCH操作，NULL
- 最近的FETCH返回行数据，FALSE
- 最近的FETCH没有返回行数据，TRUE
- %ROWCOUNT

存在如下值：

- 游标没有打开，抛出INVALID\_CURSOR异常
- 游标已经打开，当前fetch出来的行数的值

## 示例

\-- 创建一个示例表并插入一些数据

CREATE TABLE employees (

employee\_id NUMBER PRIMARY KEY,

first\_name VARCHAR2(50),

last\_name VARCHAR2(50),

salary NUMBER

);

INSERT INTO employees (employee\_id, first\_name, last\_name, salary) VALUES (1, ‘John’, ‘Doe’, 60000);

INSERT INTO employees (employee\_id, first\_name, last\_name, salary) VALUES (2, ‘Jane’, ‘Smith’, 75000);

INSERT INTO employees (employee\_id, first\_name, last\_name, salary) VALUES (3, ‘Alice’, ‘Johnson’, 90000);

INSERT INTO employees (employee\_id, first\_name, last\_name, salary) VALUES (4, ‘Bob’, ‘Brown’, 50000);

DECLARE CURSOR emp\_cursor IS SELECT employee\_id, first\_name, last\_name, salary FROM employees where employee\_id=1;

emp\_record emp\_cursor%ROWTYPE;

BEGIN

OPEN emp\_cursor;

LOOP

FETCH emp\_cursor INTO emp\_record;

EXIT WHEN emp\_cursor%NOTFOUND;

raise notice ‘ID: %, Name: % %, Salary: %’, emp\_record.employee\_id,emp\_record.first\_name,emp\_record.last\_name,emp\_record.salary;

END LOOP;

CLOSE emp\_cursor;

END;

/