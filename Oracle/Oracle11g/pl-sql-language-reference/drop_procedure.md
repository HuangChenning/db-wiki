---
title: DROP PROCEDURE Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/drop_procedure.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `DROP` `PROCEDURE` statement drops a standalone procedure from the database.

Note:

Do not use this statement to remove a procedure that is part of a package. Instead, either drop the entire package using the ["DROP PACKAGE Statement"](drop_package.md), or redefine the package without the procedure using the ["CREATE PACKAGE Statement"](create_package.md) with the `OR` `REPLACE` clause.

Topics

Prerequisites

The procedure must be in your schema or you must have the `DROP` `ANY` `PROCEDURE` system privilege.

Syntax

drop\_procedure::=

![drop_procedure](img/drop_procedure.gif)

> ```
> DROP PROCEDURE [ schema. ] procedure ;
> ```
>
> [Copyright © 1996, 2014, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

Semantics

schema

Name of the schema containing the procedure. Default: your schema.

procedure

Name of the procedure to be dropped.

When you drop a procedure, the database invalidates any local objects that depend upon the dropped procedure. If you subsequently reference one of these objects, then the database tries to recompile the object and returns an error message if you have not re-created the dropped procedure.

Example

Dropping a Procedure: Example This statement drops the procedure `remove_emp` owned by the user `hr` and invalidates all objects that depend upon `remove_emp`:

```
DROP PROCEDURE hr.remove_emp;
```