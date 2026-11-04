---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/DROP-FUNCTION-statement.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## DROP FUNCTION Statement

The `DROP` `FUNCTION` statement drops a standalone function from the database.

Note:

Do not use this statement to drop a function that is part of a package. Instead, either drop the entire package using the " [DROP PACKAGE Statement](DROP-PACKAGE-statement.md) " or redefine the package without the function using the " [CREATE PACKAGE Statement](CREATE-PACKAGE-statement.md) " with the `OR` `REPLACE` clause.

Topics

Prerequisites

The function must be in your schema or you must have the `DROP` `ANY` `PROCEDURE` system privilege.

Syntax

drop\_function::=

![drop_function](img/drop_function.gif)

> ```
> DROP FUNCTION [ IF EXISTS ] [ schema. ] function_name ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2026, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

drop\_function

IF EXISTS

Drops the function if it exists. If no such function exists, the statement is ignored without error.

schema

Name of the schema containing the function. Default: your schema.

function\_name

Name of the function to be dropped.

The database invalidates any local objects that depend on, or invoke, the dropped function. If you subsequently reference one of these objects, then the database tries to recompile the object and returns an error if you have not re-created the dropped function.

If any statistics types are associated with the function, then the database disassociates the statistics types with the `FORCE` option and drops any user-defined statistics collected with the statistics type.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01106) for information about the `ASSOCIATE` `STATISTICS` statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01507) for information about the `DISASSOCIATE` `STATISTICS` statement

Example

Example 14-32 Dropping a Function

This statement drops the function `SecondMax` in the sample schema `oe` and invalidates all objects that depend upon `SecondMax`:

```
DROP FUNCTION IF EXISTS oe.SecondMax;
```

If `SecondMax` does not already exist in the schema, this statement is ignored without error. Note that the output message is the same whether or not the function exists (in this case, `Function dropped.`).

See Also:

" [Example 14-15](CREATE-FUNCTION-statement.md) " for information about creating the `SecondMax` function