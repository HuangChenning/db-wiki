---
title: DROP PACKAGE
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8025.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Packages are defined using PL/SQL. Refer to [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/drop_package.htm#LNPLS99992) for complete information on creating, altering, and dropping packages.

Use the `DROP` `PACKAGE` statement to remove a stored package from the database. This statement drops the body and specification of a package.

Note:

Do not use this statement to remove a single object from a package. Instead, re-create the package without the object using the `CREATE` `PACKAGE` and `CREATE` `PACKAGE` `BODY` statements with the `OR` `REPLACE` clause.

Prerequisites

The package must be in your own schema or you must have the `DROP` `ANY` `PROCEDURE` system privilege.

Syntax

drop\_package::=

![drop_package](img/drop_package.gif)

> ```
> DROP PACKAGE [ BODY ] [ schema. ] package ;
> ```
  

Semantics

BODY

Specify `BODY` to drop only the body of the package. If you omit this clause, then Oracle Database drops both the body and specification of the package.

When you drop only the body of a package but not its specification, the database does not invalidate dependent objects. However, you cannot call one of the procedures or stored functions declared in the package specification until you re-create the package body.

schema

Specify the schema containing the package. If you omit `schema`, then the database assumes the package is in your own schema.

package

Specify the name of the package to be dropped.

Oracle Database invalidates any local objects that depend on the package specification. If you subsequently reference one of these objects, then the database tries to recompile the object and returns an error if you have not re-created the dropped package.

If any statistics types are associated with the package, then the database disassociates the statistics types with the `FORCE` clause and drops any user-defined statistics collected with the statistics types.

See Also:

[ASSOCIATE STATISTICS](statements_4006.md) and [DISASSOCIATE STATISTICS](statements_8006.md)

Examples

Dropping a Package: Example The following statement drops the specification and body of the `emp_mgmt` package, invalidating all objects that depend on the specification. See [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/create_package_body.htm#LNPLS01381) for the example that creates this package.

```
DROP PACKAGE emp_mgmt;
```