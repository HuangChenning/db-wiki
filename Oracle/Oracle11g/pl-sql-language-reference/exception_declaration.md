---
title: Exception Declaration
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/exception_declaration.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

An exception declaration declares the name of a user-defined exception. You can use the `EXCEPTION_INIT` pragma to assign this name to an internally defined exception.

Topics

Syntax

exception\_declaration::=

  
[Description of the illustration exception\_declaration.gif](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/img_text/exception_declaration.htm)  

Semantics

exception

Name of the exception that you are declaring.

Restriction on exception

You can use `exception` only in an `EXCEPTION_INIT` pragma, `RAISE` statement, `RAISE_APPLICATION_ERROR` invocation, or exception handler.

Caution:

Oracle recommends against using a predefined exception name for `exception`. For details, see ["Redeclared Predefined Exceptions"](errors.md). For a list of predefined exception names, see [Table 11-3](errors.md).