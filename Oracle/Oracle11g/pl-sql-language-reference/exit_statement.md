---
title: EXIT Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/exit_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `EXIT` statement exits the current iteration of a loop, either conditionally or unconditionally, and transfers control to the end of either the current loop or an enclosing labeled loop.

Restriction on EXIT Statement

An `EXIT` statement must be inside a `LOOP` statement.

Topics

Semantics

label

Name that identifies either the current loop or an enclosing loop (see ["Basic LOOP Statement"](basic_loop_statement.md)).

Without `label`, the `EXIT` statement transfers control to the next iteration of the current loop. With `label`, the `EXIT` statement transfers control to the next iteration of the loop that `label` identifies.

WHEN boolean\_expression

Without this clause, the `EXIT` statement exits the current iteration of the loop unconditionally. With this clause, the `EXIT` statement exits the current iteration of the loop if and only if the value of `boolean_expression` is `TRUE`.

Examples

- [Example 4-9, "Basic LOOP Statement with EXIT Statement"](controlstatements.md)
- [Example 4-10, "Basic LOOP Statement with EXIT WHEN Statement"](controlstatements.md)
- [Example 4-11, "Nested, Labeled Basic LOOP Statements with EXIT WHEN Statements"](controlstatements.md)
- [Example 4-25, "EXIT WHEN Statement in FOR LOOP Statement"](controlstatements.md)
- [Example 4-26, "EXIT WHEN Statement in Inner FOR LOOP Statement"](controlstatements.md)