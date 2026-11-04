---
title: ALTER FUNCTION
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ALTER-FUNCTION.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Functions are defined using PL/SQL. Therefore, this section provides some general information but refers to [*Oracle Database PL/SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=LNPLS99999) for details of syntax and semantics.

Use the `ALTER` `FUNCTION` statement to recompile an invalid standalone stored function. Explicit recompilation eliminates the need for implicit run-time recompilation and prevents associated run-time compilation errors and performance overhead.

This statement does not change the declaration or definition of an existing function. To redeclare or redefine a function, use the `CREATE` `FUNCTION` statement with the `OR` `REPLACE` clause. See [CREATE FUNCTION](CREATE-FUNCTION.md).

## Prerequisites

The function must be in your own schema or you must have `ALTER` `ANY` `PROCEDURE` system privilege.

## Syntax

## alter\_function::=

[Description of the illustration alter\_function.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/alter_function.html)

(*function\_compile\_clause*: See [*Oracle Database PL/SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=LNPLS1872) for the syntax of this clause.)

## Semantics

## IF EXISTS

Specify `IF EXISTS` to alter an existing function.

**Note:** You can only use `IF EXISTS` from Release 19.28 and up.

## schema

Specify the schema containing the function. If you omit *schema*, then Oracle Database assumes the function is in your own schema.

## function\_name

Specify the name of the function to be recompiled.

## function\_compile\_clause

See [*Oracle Database PL/SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=LNPLS1872) for the syntax and semantics of this clause and for complete information on creating and compiling functions.

## EDITIONABLE | NONEDITIONABLE

Use these clauses to specify whether the function becomes an editioned or noneditioned object if editioning is later enabled for the schema object type `FUNCTION` in *schema*. The default is `EDITIONABLE`. For information about altering editioned and noneditioned objects, see [*Oracle Database Development Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=ADFNS1287).