---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/sql-statements-for-stored-plsql-units.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

This chapter explains how to use the SQL statements that create, change, and drop stored PL/SQL units.

CREATE \[ OR REPLACE \] Statements

Each of these SQL statements creates a PL/SQL unit at schema level and stores it in the database:

- [CREATE FUNCTION Statement](CREATE-FUNCTION-statement.md)
- [CREATE LIBRARY Statement](CREATE-LIBRARY-statement.md)
- [CREATE PACKAGE Statement](CREATE-PACKAGE-statement.md)
- [CREATE PACKAGE BODY Statement](CREATE-PACKAGE-BODY-statement.md)
- [CREATE PROCEDURE Statement](CREATE-PROCEDURE-statement.md)
- [CREATE TRIGGER Statement](CREATE-TRIGGER-statement.md)
- [CREATE TYPE Statement](CREATE-TYPE-statement.md)
- [CREATE TYPE BODY Statement](CREATE-TYPE-BODY-statement.md)

Each of these `CREATE` statements has an optional `OR` `REPLACE` clause. Specify `OR` `REPLACE` to re-create an existing PL/SQL unit—that is, to change its declaration or definition without dropping it, re-creating it, and regranting object privileges previously granted on it. If you redefine a PL/SQL unit, the database recompiles it.

Caution:

A `CREATE` `OR` `REPLACE` statement does not issue a warning before replacing the existing PL/SQL unit.

None of these `CREATE` statements can appear in a PL/SQL block.

ALTER Statements

To recompile an existing PL/SQL unit without re-creating it (without changing its declaration or definition), use one of these SQL statements:

- [ALTER FUNCTION Statement](ALTER-FUNCTION-statement.md)
- [ALTER LIBRARY Statement](ALTER-LIBRARY-statement.md)
- [ALTER PACKAGE Statement](ALTER-PACKAGE-statement.md)
- [ALTER PROCEDURE Statement](ALTER-PROCEDURE-statement.md)
- [ALTER TRIGGER Statement](ALTER-TRIGGER-statement.md)
- [ALTER TYPE Statement](ALTER-TYPE-statement.md)

Reasons to use an `ALTER` statement are:

- To explicitly recompile a stored unit that has become invalid, thus eliminating the need for implicit runtime recompilation and preventing associated runtime compilation errors and performance overhead.
- To recompile a stored unit with different compilation parameters.
- To enable or disable a trigger.
- To specify the `EDITIONABLE` or `NONEDITIONABLE` property of a stored unit whose schema object type is not yet editionable in its schema.

The `ALTER` `TYPE` statement has additional uses.

DROP Statements

To drop an existing PL/SQL unit from the database, use one of these SQL statements:

- [DROP FUNCTION Statement](DROP-FUNCTION-statement.md)
- [DROP LIBRARY Statement](DROP-LIBRARY-statement.md)
- [DROP PACKAGE Statement](DROP-PACKAGE-statement.md)
- [DROP PROCEDURE Statement](DROP-PROCEDURE-statement.md)
- [DROP TRIGGER Statement](DROP-TRIGGER-statement.md)
- [DROP TYPE Statement](DROP-TYPE-statement.md)
- [DROP TYPE BODY Statement](DROP-TYPE-BODY-statement.md)

Related Topics

- For instructions for reading the syntax diagrams in this chapter, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF018).
- For information about editioned and noneditioned objects, see [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=ADFNS99923).
- For information about compilation parameters, see " [PL/SQL Units and Compilation Parameters](overview.md) ".