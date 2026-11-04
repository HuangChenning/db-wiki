---
title: DROP PACKAGE Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/drop_package.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `DROP` `PACKAGE` statement drops a stored package from the database. This statement drops the body and specification of a package.

Note:

Do not use this statement to drop a single object from a package. Instead, re-create the package without the object using the ["CREATE PACKAGE Statement"](create_package.md) and ["CREATE PACKAGE BODY Statement"](create_package_body.md) with the `OR` `REPLACE` clause.

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
> [Copyright © 1996, 2014, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

Semantics

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

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_4006.htm#SQLRF01106) for information about the `ASSOCIATE` `STATISTICS` statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8006.htm#SQLRF01507) for information about the `DISASSOCIATE` `STATISTICS` statement

Example

Dropping a Package: Example This statement drops the specification and body of the `emp_mgmt` package, which was created in ["Creating a Package Body: Example"](create_package_body.md), invalidating all objects that depend on the specification:

```
DROP PACKAGE emp_mgmt;
```