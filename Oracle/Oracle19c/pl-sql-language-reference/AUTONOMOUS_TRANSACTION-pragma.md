---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/AUTONOMOUS_TRANSACTION-pragma.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## AUTONOMOUS\_TRANSACTION Pragma

The `AUTONOMOUS_TRANSACTION` pragma marks a routine as autonomous; that is, independent of the main transaction.

In this context, a routine is one of these:

- Schema-level (not nested) anonymous PL/SQL block
- Standalone, package, or nested subprogram
- Method of an ADT
- Noncompound trigger

Topics

Syntax

autonomous\_trans\_pragma::=

![autonomous_trans_pragma](img/autonomous_trans_pragma.gif)

> ```
> PRAGMA AUTONOMOUS_TRANSACTION ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2026, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Examples

- [Example 6-43](autonomous-transactions.md), "Declaring Autonomous Function in Package"
- [Example 6-44](autonomous-transactions.md), "Declaring Autonomous Standalone Procedure"
- [Example 6-45](autonomous-transactions.md), "Declaring Autonomous PL/SQL Block"
- [Example 6-46](autonomous-transactions.md), "Autonomous Trigger Logs INSERT Statements"
- [Example 6-47](autonomous-transactions.md), "Autonomous Trigger Uses Native Dynamic SQL for DDL"
- [Example 6-48](autonomous-transactions.md), "Invoking Autonomous Function"