---
title: CONTINUE Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/continue_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `CONTINUE` statement exits the current iteration of a loop, either conditionally or unconditionally, and transfers control to the next iteration of either the current loop or an enclosing labeled loop.

If a `CONTINUE` statement exits a cursor `FOR` loop prematurely (for example, to exit an inner loop and transfer control to the next iteration of an outer loop), the cursor closes (in this context, `CONTINUE` works like `GOTO`).

Note:

As of Oracle Database 11g Release 1, `CONTINUE` is a PL/SQL keyword. If your program invokes a subprogram named `CONTINUE`, you get a warning.

Restrictions on CONTINUE Statement

- A `CONTINUE` statement must be inside a `LOOP` statement.
- A `CONTINUE` statement cannot cross a subprogram or method boundary.

Topics

- Syntax
- Semantics
- Examples
- Related Topics

Semantics

label

Name that identifies either the current loop or an enclosing loop (see ["Basic LOOP Statement"](basic_loop_statement.md)).

Without `label`, the `CONTINUE` statement transfers control to the next iteration of the current loop. With `label`, the `CONTINUE` statement transfers control to the next iteration of the loop that `label` identifies.

WHEN boolean\_expression

Without this clause, the `CONTINUE` statement exits the current iteration of the loop unconditionally. With this clause, the `CONTINUE` statement exits the current iteration of the loop if and only if the value of `boolean_expression` is `TRUE`.

Related Topics

In this chapter:

- ["Basic LOOP Statement"](basic_loop_statement.md)
- ["Cursor FOR LOOP Statement"](cursor_for_loop_statement.md)
- ["EXIT Statement"](exit_statement.md)
- ["Expression"](expression.md)
- ["FOR LOOP Statement"](for_loop_statement.md)
- ["WHILE LOOP Statement"](while_loop_statement.md)

In other chapters:

- ["LOOP Statements"](controlstatements.md)
- ["CONTINUE Statement"](controlstatements.md)
- ["CONTINUE WHEN Statement"](controlstatements.md)