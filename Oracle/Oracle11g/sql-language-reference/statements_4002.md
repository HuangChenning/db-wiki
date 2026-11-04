---
title: ALTER TYPE
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_4002.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Object types are defined using PL/SQL. Therefore, this section provides some general information but refers to [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/alter_type.htm#LNPLS99995) for details of syntax and semantics.

Use the `ALTER` `TYPE` statement to add or drop member attributes or methods. You can change the existing properties (`FINAL` or `INSTANTIABLE`) of an object type, and you can modify the scalar attributes of the type.

You can also use this statement to recompile the specification or body of the type or to change the specification of an object type by adding new object member subprogram specifications.

Prerequisites

The object type must be in your own schema and you must have `CREATE` `TYPE` or `CREATE` `ANY` `TYPE` system privilege, or you must have `ALTER` `ANY` `TYPE` system privileges.

Syntax

alter\_type::=

![alter_type](img/alter_type.gif)

> ```
> ALTER TYPE [ schema. ]type alter_type_clauses
> ```
  
  

(`alter_type_clauses`: See [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/alter_type.htm#LNPLS99995) for the syntax of this clause.)

Semantics

schema

Specify the schema that contains the type. If you omit `schema`, then Oracle Database assumes the type is in your current schema.

type

Specify the name of an object type, a nested table type, or a varray type.

Restriction on type\_name You cannot evolve an editioned object type. The `ALTER` `TYPE` statement fails with ORA-22348 if either of the following is true:

- The type is an editioned object type and the `ALTER` `TYPE` statement has no `compile_type_clause`. You can use the `ALTER` `TYPE` statement to recompile an editioned object type, but not for any other purpose.
- The type has a dependent that is an editioned object type and the `ALTER` `TYPE` statement has a `CASCADE` clause.

Refer to Oracle Database PL/SQL Language Reference for more information on the [`compile_type_clause`](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/alter_type.htm#LNPLS1441) and the [`CASCADE`](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/alter_type.htm#LNPLS1482) clause.

alter\_type\_clauses

See [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/alter_type.htm#LNPLS99995) for the syntax and semantics of this clause and for complete information on creating and compiling object types.