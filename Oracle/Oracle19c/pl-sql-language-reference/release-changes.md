---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/release-changes.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Changes in This Release for Oracle Database PL/SQL Language Reference

Changes to Oracle Database PL/SQL Language Reference are described for each release.

This preface contains:

- Changes in Release 19c for Oracle Database PL/SQL Language Reference
- Changes in Release 18c for Oracle Database PL/SQL Language Reference

### Changes in Oracle Database Release 19c

Starting from Oracle Database 19c, if a polymorphic table function and its implementation methods are defined in the same package, then the USING clause is optional.

See Also:

- [PIPELINED Clause](PIPELINED-clause.md) for more information on polymorphic table function, syntax and semantics

#### SQL Macros

You can create SQL macros (SQM) to factor out common SQL expressions and statements into reusable, parameterized constructs that can be used in other SQL statements.

Starting with Oracle Database release 19c, version 19.7, SQL table macros are supported. SQL table macros are expressions, typically used in a `FROM` clause, to act as a sort of polymorphic (parameterized) views.

SQL table macros increase developer productivity, simplify collaborative development, and improve code quality.

#### IF \[NOT\] EXISTS Syntax Support

Starting with Oracle Database 19c, Release Update 19.28, the clauses `IF NOT EXISTS` and `IF EXISTS` are supported by `CREATE`, `ALTER`, and `DROP` DDL statements. They are used to suppress potential errors otherwise raised by the existence or non-existence of a given object, allowing you to write idempotent DDL scripts.

The `IF NOT EXISTS` clause is supported by the `CREATE` DDL statement to prevent errors from being thrown if an object with the given name already exists. If the object does already exist, the command is ignored and the original object remains unchanged.

On the flip side, the `IF EXISTS` clause suppresses errors when used with `ALTER` and `DROP` DDL statements. In the case that no object by the given name exists, the command is ignored and no object is affected by `ALTER` or `DROP`.

The use or exclusion of the clause provides you more control depending on whether you need to know if an object exists before executing a DDL statement. With this flexibility, you can determine whether you would rather have the statement ignored or have an error raised in the event the object exists (or doesn't exist).

Note:

`IF NOT EXISTS` cannot be used in combination with `OR REPLACE` in commands using the `CREATE` DDL statement.

See Also:

- " [SQL Statements for Stored PL/SQL Units](sql-statements-for-stored-plsql-units.md) " for information about the semantics used to implement `IF [NOT] EXISTS` with different object types
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADFNS-GUID-3818B089-D99D-437C-862F-CBD276BDA3F1) for more information about using the `IF [NOT] EXISTS` clause

Example - CREATE PROCEDURE with IF NOT EXISTS

Executing this statement one time results in the creation of procedure `hello`, assuming a procedure by the same name does not already exist in your schema.

```
CREATE PROCEDURE IF NOT EXISTS hello AS
BEGIN
  DBMS_OUTPUT.PUT_LINE('Hello there');
END;
/
```

Executing the statement additional times, even with an altered procedure body, results in no error. The original body remains unchanged.

```
CREATE PROCEDURE IF NOT EXISTS hello AS
BEGIN
  DBMS_OUTPUT.PUT_LINE('Second hello');
END;
/
```

Note:

The same output message will be displayed, in this case `Procedure created`, regardless of whether the command is ignored or executed. This ensures that you can write DDL scripts that are idempotent. The same holds true for `ALTER`, `CREATE`, and `DROP` statements.

The procedure text is the same before and after the second statement is executed.

```
SELECT TEXT FROM USER_SOURCE WHERE NAME='HELLO';
```
```
TEXT
-------------------------------------------
procedure            hello
AS BEGIN
DBMS_OUTPUT.PUT_LINE('Hello there');
END;
```

### Changes in Oracle Database Release 18c

For Oracle Database 18c, Oracle Database PL/SQL Language Reference documents these new features.

New Features

#### Non-Persistance Support for Object Types

This feature enables you to mark abstract data types used in programs for processing only, for storage only, or for mixed use.

Instances of non-persistable types cannot persist on disk.

See Also:

- `CREATE` `TYPE` statement [\[NOT\] PERSISTABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/CREATE-TYPE-statement.html#GUID-389D603D-FBD0-452A-8414-240BBBC57034__NOTPERSISTABLE-DC9DEF8B) clause for more information about the syntax and semantics

#### Polymorphic Table Functions

A polymorphic table function (PTF) is a new type of table function whose return type is determined by the arguments passed into the PTF.

A table function is a function that returns a collection of rows and that can be called from the `FROM` clause of a SQL query block.

The new polymorphic table function (PTF) provides an efficient and scalable framework to extend the analytical capabilities of the Oracle Database. A query writer is able to call these functions without knowing the details of the implementation of the PTF and the PTF doesn't need to know about the details or how the function is being executed (e.g. in serial or parallel) or whether the input rows are partitioned or ordered.

Therefore, a PTF is useful when SQL developers and database administrators want to provide generic extensions which work for arbitrary input tables or queries.

See [Overview of Polymorphic Table Functions](overview-polymorphic-table-functions.md) for more information.

#### Qualified Expressions

Aggregates and their necessary adjunct, qualified expressions, improve program clarity and programmer productivity.

Through Oracle Database 12c release 2, it was possible to supply the value of a non-scalar datatype with an expression, for example by using the type constructor for a nested table. Starting with Oracle Database Release 18c, any PL/SQL value can be provided by an expression (for example for a record or for an associative array) like a constructor provides an abstract datatype value. In PL/SQL, we use the terms "qualified expression" and "aggregate" rather than the SQL term "type constructor", but the functionality is the same.

See [Qualified Expressions Overview](qualified-expressions-overview.md) and [qualified\_expression::=](expression.md) for more information about the syntax and semantics.

### Deprecated Features

The following features are deprecated in this release, and may be desupported in a future release.

The command ` ALTER TYPE`... `INVALIDATE` is deprecated. Use the `CASCADE` clause instead.

The `REPLACE` clause of `ALTER TYPE` is deprecated. Use the `alter_method_spec` clause instead. Alternatively, you can recreate the type using the `CREATE OR REPLACE TYPE` statement.

For the syntax and semantics, see [ALTER TYPE Statement](ALTER-TYPE-statement.md)

Starting with Oracle Database 12c release 1 (12.1), the compilation parameter PLSQL\_DEBUG is deprecated.

To compile PL/SQL units for debugging, specify PLSQL\_OPTIMIZE\_LEVEL=1.

For information about compilation parameters, see [PL/SQL Units and Compilation Parameters](architecture-pl-sql.md).

### Desupported Features

No features in PL/SQL Language Reference have been desupported for 19c.

Note:

Oracle Database Advanced Queuing continues to be enhanced and is independent of Oracle Streams, which is desupported in Oracle Database 19c.

See Also:

- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=UPGRD-GUID-E121B993-1845-405A-B4BA-047BAC00626E) for more information about desupported features in Oracle Database 19c