---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/RAISE-statement.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `RAISE` statement explicitly raises an exception.

Outside an exception handler, you must specify the exception name. Inside an exception handler, if you omit the exception name, the `RAISE` statement reraises the current exception.

Topics

Syntax

raise\_statement::=

![raise_statement](img/raise_statement.gif)

> ```
> RAISE [ exception ] ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

exception

Name of an exception, either predefined (see [Table 12-3](plsql-error-handling.md)) or user-declared (see " [Exception Declaration](exception-declaration.md) ").

`exception` is optional only in an exception handler, where the default is the current exception (see " [Reraising Current Exception with RAISE Statement](plsql-error-handling.md) ").

Examples