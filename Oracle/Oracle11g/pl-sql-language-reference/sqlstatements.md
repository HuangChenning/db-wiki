---
title: SQL Statements for Stored PL/SQL Units
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/sqlstatements.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

## 14 SQL Statements for Stored PL/SQL Units

This chapter explains how to use the SQL statements that create, change, and drop stored PL/SQL units.

For instructions for reading the syntax diagrams in this chapter, see [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/ap_syntx.htm#SQLRF018).

CREATE \[OR REPLACE\] Statements

Each of these SQL statements creates a PL/SQL unit at schema level and stores it in the database:

- [CREATE FUNCTION Statement](create_function.md)
- [CREATE LIBRARY Statement](create_library.md)
- [CREATE PACKAGE Statement](create_package.md)
- [CREATE PACKAGE BODY Statement](create_package_body.md)
- [CREATE PROCEDURE Statement](create_procedure.md)
- [CREATE TRIGGER Statement](create_trigger.md)
- [CREATE TYPE Statement](create_type.md)
- [CREATE TYPE BODY Statement](create_type_body.md)

Each of these `CREATE` statements has an optional `OR` `REPLACE` clause. Specify `OR` `REPLACE` to re-create an existing PL/SQL unit—that is, to change its declaration or definition without dropping it, re-creating it, and regranting object privileges previously granted on it. If you redefine a PL/SQL unit, the database recompiles it.

Caution:

A `CREATE` `OR` `REPLACE` statement does not issue a warning before replacing the existing PL/SQL unit.

None of these `CREATE` statements can appear in a PL/SQL block.

ALTER Statements

To recompile an existing PL/SQL unit without re-creating it (without changing its declaration or definition), use one of these SQL statements:

- [ALTER FUNCTION Statement](alter_function.md)
- [ALTER LIBRARY Statement](alter_library.md)
- [ALTER PACKAGE Statement](alter_package.md)
- [ALTER PROCEDURE Statement](alter_procedure.md)
- [ALTER TRIGGER Statement](alter_trigger.md)
- [ALTER TYPE Statement](alter_type.md)

Reasons to use an `ALTER` statement are:

- To explicitly recompile a stored unit that has become invalid, thus eliminating the need for implicit runtime recompilation and preventing associated runtime compilation errors and performance overhead.
- To recompile a unit with different compilation parameters.
	For information about compilation parameters, see ["PL/SQL Units and Compilation Parameters"](overview.md).
- To enable or disable a trigger.

The `ALTER` `TYPE` statement has additional uses. For details, see ["ALTER TYPE Statement"](alter_type.md).

DROP Statements

To drop an existing PL/SQL unit from the database, use one of these SQL statements:

- [DROP FUNCTION Statement](drop_function.md)
- [DROP LIBRARY Statement](drop_library.md)
- [DROP PACKAGE Statement](drop_package.md)
- [DROP PROCEDURE Statement](drop_procedure.md)
- [DROP TRIGGER Statement](drop_trigger.md)
- [DROP TYPE Statement](drop_type.md)
- [DROP TYPE BODY Statement](drop_type_body.md)