---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/exception-declaration.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Exception Declaration

An exception declaration declares the name of a user-defined exception.

You can use the `EXCEPTION_INIT` pragma to assign this name to an internally defined exception.

Topics

Syntax

exception\_declaration::=

![exception_declaration](img/exception_declaration.gif)

> ```
> exception EXCEPTION;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2026, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

exception\_declaration

exception

Name of the exception that you are declaring.

Restriction on exception

You can use `exception` only in an `EXCEPTION_INIT` pragma, `RAISE` statement, `RAISE_APPLICATION_ERROR` invocation, or exception handler.

Caution:

Oracle recommends against using a predefined exception name for `exception`. For details, see " [Redeclared Predefined Exceptions](redeclared-predefined-exceptions.md) ". For a list of predefined exception names, see [Table 11-3](predefined-exceptions.md).

Examples