---
title: CREATE PACKAGE BODY
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-PACKAGE-BODY.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Package bodies are defined using PL/SQL. Therefore, this section provides some general information but refers to [*Oracle Database PL/SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=LNPLS01372) for details of syntax and semantics.

Use the `CREATE` `PACKAGE` `BODY` statement to create the body of a stored **package**, which is an encapsulated collection of related procedures, stored functions, and other program objects stored together in the database. The **package body** defines these objects. The **package** **specification**, defined in an earlier `CREATE` `PACKAGE` statement, declares these objects.

Packages are an alternative to creating procedures and functions as standalone schema objects.

**See Also:**

- [CREATE FUNCTION](CREATE-FUNCTION.md) and [CREATE PROCEDURE](CREATE-PROCEDURE.md) for information on creating standalone functions and procedures
- [CREATE PACKAGE](CREATE-PACKAGE.md) for a discussion of packages, including how to create packages
- [ALTER PACKAGE](ALTER-PACKAGE.md) for information on modifying a package
- [DROP PACKAGE](DROP-PACKAGE.md) for information on removing a package from the database

## Prerequisites

To create or replace a package in your own schema, you must have the `CREATE` `PROCEDURE` system privilege. To create or replace a package in another user’s schema, you must have the `CREATE` `ANY` `PROCEDURE` system privilege. In both cases, the package body must be created in the same schema as the package.

To embed a `CREATE` `PACKAGE` `BODY` statement inside an Oracle Database precompiler program, you must terminate the statement with the keyword `END-EXEC` followed by the embedded SQL statement terminator for the specific language.

**See Also:** [*Oracle Database PL/SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=LNPLS01372)

## Syntax

Package bodies are defined using PL/SQL. Therefore, the syntax diagram in this book shows only the SQL keywords. Refer to [*Oracle Database PL/SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=LNPLS01372) for the PL/SQL syntax, semantics, and examples.

## create\_package\_body::=

[Description of the illustration create\_package\_body.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/create_package_body.html)

(*plsql\_package\_body\_source*: See [*Oracle Database PL/SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=LNPLS2181).)

## Semantics

## OR REPLACE

Specify `OR` `REPLACE` to re-create the package body if it already exists. Use this clause to change the body of an existing package without dropping, re-creating, and regranting object privileges previously granted on it. If you change a package body, then Oracle Database recompiles it.

Users who had previously been granted privileges on a redefined package can still access the package without being regranted the privileges.

**See Also:** [ALTER PACKAGE](ALTER-PACKAGE.md) for information on recompiling package bodies

## IF NOT EXISTS

Specifying `IF NOT EXISTS` has the following effects:

- If the package body does not exist, a new one is created at the end of the statement.
- If the package body exists, it is detected and a new one is not created.

You can only specify `OR REPLACE` or `IF NOT EXISTS` in a statement at a time. Using both `OR REPLACE` with `IF NOT EXISTS` in the very same statement results in an error.

You cannot specify `IF EXISTS` with `CREATE` statements.

**Note:** You can use `IF [NOT] EXISTS` only from Release 19.28 and up.

## \[ EDITIONABLE | NONEDITIONABLE \]

If you do not specify this clause, then the package body inherits `EDITIONABLE` or `NONEDITIONABLE` from the package specification. If you do specify this clause, then it must match that of the package specification.