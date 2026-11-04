---
title: SUBTYPE
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle29.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## SUBTYPE

SUBTYPE  
是一种强大的特性，允许开发者基于现有数据类型定义新的子类型，并可以为这些子类型添加约束条件（如范围、精度等）。这种特性在数据建模和程序设计中具有显著优势，例如：

- 增强数据一致性：通过为数据类型添加约束，确保数据符合业务规则。
- 提高代码可读性：使用自定义的子类型可以更清晰地表达代码意图。
- 简化数据类型管理：允许基于现有类型派生新类型，减少重复定义。

说明：

该功能在V9.0.5及以后的版本中支持。

## 使用SUBTYPE类型

### 说明

SUBTYPE  
类型可以使用标量类型、复合类型、record类型和subtype类型作为基类型。可以用在存储过程、函数、匿名块、包中使用，也可以作为参数和返回值类型使用。

语法：

SUBTYPE subtype\_name IS base\_type

### 示例

#### 匿名块中使用subtype

示例1：在匿名块中定义subtype类型并使用

DECLARE

SUBTYPE typ1 IS integer;

val1 typ1:= 123;

BEGIN

raise notice 'val1: %', val1;

END;

/

示例2：在匿名块中定义基于数组和subtype类型的subtype类型并使用

DECLARE

SUBTYPE my\_subtype1 IS int\[\];

SUBTYPE my\_subtype2 IS my\_subtype1;

val1 my\_subtype2;

BEGIN

val1:= ARRAY\[1,2,3,4,5\];

raise notice 'val1: %', val1\[2\];

END;

/

示例3：在匿名块中定义基于复合类型的subtype类型并使用

CREATE TYPE rec\_type AS (id INTEGER, name VARCHAR(30));

DECLARE

SUBTYPE typ1 IS rec\_type;

val1 typ1;

BEGIN

val1.id:= 101;

val1.name:= 'John';

raise notice 'val1: %', val1;

END;

/

#### 存储过程中使用subtype

示例：在存储过程中定义subtype类型并使用

CREATE OR REPLACE PROCEDURE pr1 AS

SUBTYPE typ1 IS integer;

val1 typ1:= 123;

BEGIN

raise notice 'val1: %', val1;

END;

/

CALL pr1();

#### 函数中使用subtype

示例：在函数中定义subtype类型并作为参数和返回值使用

CREATE OR REPLACE FUNCTION func1 RETURN INTEGER AS

SUBTYPE typ1 IS integer;

val1 typ1:= 123;

val2 typ1;

FUNCTION test\_func1(p1 typ1) RETURN typ1 AS

BEGIN

RETURN p1;

END;

BEGIN

val2:= test\_func1(val1);

raise notice 'val2: %', val2;

RETURN 1;

END;

/

SELECT func1() FROM DUAL;

#### 包中使用subtype

示例：在包中定义subtype类型并使用

CREATE OR REPLACE PACKAGE my\_package AS

SUBTYPE age IS INTEGER;

PROCEDURE display\_employee\_info(p\_age IN age);

FUNCTION get\_default\_age RETURN age;

END my\_package;

CREATE OR REPLACE PACKAGE BODY my\_package AS

PROCEDURE display\_employee\_info(p\_age IN age) IS

BEGIN

raise notice 'Age: %', p\_age;

END display\_employee\_info;

FUNCTION get\_default\_age RETURN age IS

BEGIN

RETURN 30;

END get\_default\_age;

END my\_package;

DECLARE

v\_age my\_package.age:= 45;

BEGIN

my\_package.display\_employee\_info(p\_age => v\_age);

raise notice 'Default age: %', my\_package.get\_default\_age();

END;

/

#### 使用record作为基类型

示例：使用record作为基类型

DECLARE

TYPE rec\_type IS RECORD (id INTEGER, name VARCHAR2(30));

SUBTYPE my\_subtype1 IS rec\_type;

SUBTYPE my\_subtype2 IS my\_subtype1;

val1 my\_subtype1;

val2 my\_subtype2;

BEGIN

val1.id:= 100;

val1.name:= 'John';

raise notice 'val1: %', val1;

val2.id:= 100;

val2.name:= 'John';

raise notice 'val2: %', val2;

END;

/

#### 使用cursor和rowtype作为基类型

示例：使用cursor和rowtype作为基类型

CREATE TABLE employees(id INTGER, name VARCHAR2(30));

INSERT INTO employees VALUES(100, 'John');

DECLARE

TYPE empcurtyp IS REF CURSOR RETURN employees%ROWTYPE;

SUBTYPE my\_subtype1 IS empcurtyp;

SUBTYPE my\_subtype2 IS my\_subtype1;

SUBTYPE my\_subtype3 IS employees%ROWTYPE;

SUBTYPE my\_subtype4 IS my\_subtype3;

cursor1 my\_subtype1;

cursor2 my\_subtype2;

val1 my\_subtype3;

val2 my\_subtype4;

BEGIN

OPEN cursor1 FOR SELECT \* FROM employees;

FETCH cursor1 INTO val1;

raise info 'al1: %', val1;

CLOSE cursor1;

OPEN cursor2 FOR SELECT \* FROM employees;

FETCH cursor2 INTO val2;

raise info 'val2: %', val2;

CLOSE cursor2;

END;

/

## SUBTYPE类型支持约束

定义subtype类型支持添加多种约束，包括非空约束，长度约束和范围约束。

### 非空约束

语法：

SUBTYPE subtype\_name IS base\_type \[ NOT NULL \]

示例：

DECLARE

SUBTYPE typ1 IS INTEGER NOT NULL;

val1 typ1:= 123;

val2 typ1; --err

BEGIN

val2:= val1;

raise notice 'val2: %', val2;

val2:= NULL; --err

END;

/

因为将val2设置为null，所以上述语句会报错：

variable "val2" must have a default value, since it's declared NOT  
NULL

### 长度约束

语法：

SUBTYPE subtype\_name IS base\_type \[ precision \[, scale \]\] \[ NOT  
NULL \]

示例：

DECLARE

SUBTYPE str\_subtype IS VARCHAR2(10);

v\_str1 str\_subtype(5):= 'Hello';

v\_str2 str\_subtype;

BEGIN

v\_str1:= 'HelloOK'; --err

v\_str2:= 'HelloOK';

raise notice 'v\_str1: %', v\_str1;

END;

/

因为 v\_str1的值超过了设定长度，所以上述语句会报错：

ERROR: value too long for type varchar2(5 byte)

### 范围约束

目前仅支持对INTEGER类型使用范围约束。

语法：

SUBTYPE subtype\_name IS base\_type

\[ RANGE low\_value.. high\_value \] \[ NOT NULL \]

示例：

DECLARE

SUBTYPE typ1 IS INTEGER RANGE 0..9;

SUBTYPE typ2 IS INTEGER RANGE 10..99;

SUBTYPE typ3 IS INTEGER RANGE 0..99;

val1 typ1:= 4;

val2 typ2:= 35;

val3 typ3;

BEGIN

raise notice 'val1: %', val1;

val3:= val1;

val1:= val2; --err

val2:= val1; --err

END;

/

因为val1 和val2的值超过了设置的范围，所以上述语句会报错：

ERROR: numeric or value error