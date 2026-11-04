---
title: CASE Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/case_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `CASE` statement chooses from a sequence of conditions and runs a corresponding statement.

The simple `CASE` statement evaluates a single expression and compares it to several potential values.

The searched `CASE` statement evaluates multiple Boolean expressions and chooses the first one whose value is `TRUE`.

Topics

Semantics

simple\_case\_statement

selector

Expression whose value is evaluated once and used to select one of several alternatives. `selector` can have any PL/SQL data type except `BLOB`, `BFILE`, or a user-defined type.

WHEN selector\_value THEN statement

`selector_value` can be an expression of any PL/SQL type except `BLOB`, `BFILE`, or a user-defined type.

The `selector_value` s are evaluated sequentially. If the value of a `selector_value` equals the value of `selector`, then the `statement` associated with that `selector_value` runs, and the `CASE` statement ends. Subsequent `selector_value` s are not evaluated.

Caution:

A `statement` can modify the database and invoke nondeterministic functions. There is no fall-through mechanism, as there is in the C `switch` statement.

ELSE statement \[statement \]...

The `statement` s run if and only if no `selector_value` has the same value as `selector`.

Without the `ELSE` clause, if no `selector_value` has the same value as `selector`, the system raises the predefined exception `CASE_NOT_FOUND`.

label

A label that identifies the statement (see ["statement::="](block.md) and ["label"](block.md)).

searched\_case\_statement

WHEN boolean\_expression THEN statement

The `boolean_expression` s are evaluated sequentially. If the value of a `boolean_expression` is `TRUE`, the `statement` associated with that `boolean_expression` runs, and the `CASE` statement ends. Subsequent `boolean_expression` s are not evaluated.

Caution:

A `statement` can modify the database and invoke nondeterministic functions. There is no fall-through mechanism, as there is in the C `switch` statement.

ELSE statement \[statement \]...

The `statement` s run if and only if no `boolean_expression` has the value `TRUE`.

Without the `ELSE` clause, if no `boolean_expression` has the value `TRUE`, the system raises the predefined exception `CASE_NOT_FOUND`.

label

A label that identifies the statement (see ["statement::="](block.md) and ["label"](block.md)).

Related Topics

In this chapter:

- ["IF Statement"](if_statement.md)

In other chapters:

- ["CASE Expressions"](fundamentals.md)
- ["Conditional Selection Statements"](controlstatements.md)
- ["Simple CASE Statement"](controlstatements.md)
- ["Searched CASE Statement"](controlstatements.md)

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions116.htm#SQLRF00681) for information about the `NULLIF` function
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions030.htm#SQLRF00617) for information about the `COALESCE` function