---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/CLOSE-statement.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `CLOSE` statement closes a named cursor, freeing its resources for reuse.

After closing an explicit cursor, you can reopen it with the `OPEN` statement. You must close an explicit cursor before reopening it.

After closing a cursor variable, you can reopen it with the `OPEN` `FOR` statement. You need not close a cursor variable before reopening it.

Topics

Syntax

close\_statement::=

![close_statement](img/close_statement.gif)

> ```
> CLOSE { cursor | cursor_variable | :host_cursor_variable } ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

close\_statement

cursor

Name of an open explicit cursor.

cursor\_variable

Name of an open cursor variable.

:host\_cursor\_variable

Name of a cursor variable declared in a PL/SQL host environment and passed to PL/SQL as a bind variable. Do not put space between the colon (:) and `host_cursor_variable`.

Examples

- [Example 7-6](static-sql.md), "FETCH Statements Inside LOOP Statements"