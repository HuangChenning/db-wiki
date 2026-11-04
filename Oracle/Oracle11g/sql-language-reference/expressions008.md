---
title: Function Expressions
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/expressions008.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

You can use any built-in SQL function or user-defined function as an expression. Some valid built-in function expressions are:

```
LENGTH('BLAKE') 
ROUND(1234.567*43) 
SYSDATE
```

See Also:

["About SQL Functions"](functions001.md) ' and ["Aggregate Functions"](functions003.md) for information on built-in functions

A user-defined function expression specifies a call to:

- A function in an Oracle-supplied package (see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/intro.htm#ARPLS001))
- A function in a user-defined package or type or in a standalone user-defined function (see ["About User-Defined Functions"](functions256.md))
- A user-defined function or operator (see [CREATE OPERATOR](statements_6004.md), [CREATE FUNCTION](statements_5011.md), and [Oracle Database Data Cartridge Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/operators.htm#ADDCI2100))

Some valid user-defined function expressions are:

```
circle_area(radius)
payroll.tax_rate(empno)
hr.employees.comm_pct@remote(dependents, empno)
DBMS_LOB.getlength(column_name)
my_function(a_column)
```

In a user-defined function being used as an expression, positional, named, and mixed notation are supported. For example, all of the following notations are correct:

```
CALL my_function(arg1 => 3, arg2 => 4) ...
```
```
CALL my_function(3, 4) ...

CALL my_function(3, arg2 => 4) ...
```

Restriction on User-Defined Function Expressions You cannot pass arguments of object type or `XMLType` to remote functions and procedures.