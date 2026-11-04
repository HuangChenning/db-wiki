---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/DROP-PACKAGE-statement.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `DROP` `PACKAGE` statement drops a stored package from the database.

This statement drops the body and specification of a package.

Note:

Do not use this statement to drop a single object from a package. Instead, re-create the package without the object using the " [CREATE PACKAGE Statement](CREATE-PACKAGE-statement.md) " and " [CREATE PACKAGE BODY Statement](CREATE-PACKAGE-BODY-statement.md) " with the `OR` `REPLACE` clause.

Topics

Prerequisites

The package must be in your schema or you must have the `DROP` `ANY` `PROCEDURE` system privilege.

Syntax

drop\_package::=

![drop_package](img/drop_package.gif)

> ```
> DROP PACKAGE [ BODY ] [ schema. ] package ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

drop\_package

BODY

Drops only the body of the package. If you omit this clause, then the database drops both the body and specification of the package.

When you drop only the body of a package but not its specification, the database does not invalidate dependent objects. However, you cannot invoke a procedure or stored function declared in the package specification until you re-create the package body.

schema

Name of the schema containing the package. Default: your schema.

package

Name of the package to be dropped.

The database invalidates any local objects that depend on the package specification. If you subsequently reference one of these objects, then the database tries to recompile the object and returns an error if you have not re-created the dropped package.

If any statistics types are associated with the package, then the database disassociates the statistics types with the `FORCE` clause and drops any user-defined statistics collected with the statistics types.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF01106) for information about the `ASSOCIATE` `STATISTICS` statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF01507) for information about the `DISASSOCIATE` `STATISTICS` statement

Example

Example 15-37 Dropping a Package

This statement drops the specification and body of the `emp_mgmt` package, which was created in " [CREATE PACKAGE BODY Statement](CREATE-PACKAGE-BODY-statement.md) ", invalidating all objects that depend on the specification:

```
DROP PACKAGE emp_mgmt;
```