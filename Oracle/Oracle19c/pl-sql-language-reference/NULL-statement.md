---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/NULL-statement.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## NULL Statement

The `NULL` statement is a ''no-op" (no operation)—it only passes control to the next statement.

Note:

The `NULL` statement and the `BOOLEAN` value `NULL` are not related.

Topics

Syntax

null\_statement::=

![null_statement](img/null_statement.gif)

> ```
> NULL ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2026, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Examples

- [Example 4-31](sequential-control-statements.md), "GOTO Statement Goes to Labeled NULL Statement"
- [Example 4-34](sequential-control-statements.md), "NULL Statement Showing No Action"
- [Example 4-35](sequential-control-statements.md), "NULL Statement as Placeholder During Subprogram Creation"