---
title: WHILE LOOP Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/while_loop_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `WHILE` `LOOP` statement runs one or more statements while a condition is `TRUE`. The `WHILE` `LOOP` statement ends when the condition becomes `FALSE` or `NULL`, or when a statement inside the loop transfers control outside the loop or raises an exception.

Topics

Semantics

boolean\_expression

Expression whose value is `TRUE`, `FALSE`, or `NULL`.

`boolean_expression` is evaluated at the beginning of each iteration of the loop. If its value is `TRUE`, the statements after `LOOP` run. Otherwise, control transfers to the statement after the `WHILE` `LOOP` statement.

statement

To prevent an infinite loop, at least one statement must change the value of `boolean_expression` to `FALSE` or `NULL`, transfer control outside the loop, or raise an exception. The statements that can transfer control outside the loop are:

- ["CONTINUE Statement"](continue_statement.md) (when it transfers control to the next iteration of an enclosing labeled loop)
- ["EXIT Statement"](exit_statement.md)
- ["GOTO Statement"](goto_statement.md)
- ["RAISE Statement"](raise_statement.md)

label

Label that identifies `while_loop_statement` (see ["statement::="](block.md) and ["label"](block.md)). `CONTINUE`, `EXIT`, and `GOTO` statements can reference this label.

Labels improve readability, especially when `LOOP` statements are nested, but only if you ensure that the label in the `END` `LOOP` statement matches a label at the beginning of the same `LOOP` statement (the compiler does not check).

Examples

- [Example 4-28, "WHILE LOOP Statements"](controlstatements.md)

Related Topics

In this chapter:

- ["Basic LOOP Statement"](basic_loop_statement.md)
- ["CONTINUE Statement"](continue_statement.md)
- ["Cursor FOR LOOP Statement"](cursor_for_loop_statement.md)
- ["EXIT Statement"](exit_statement.md)
- ["Explicit Cursor Declaration and Definition"](explicit_cursor.md)
- ["FETCH Statement"](fetch_statement.md)
- ["FOR LOOP Statement"](for_loop_statement.md)
- ["FORALL Statement"](forall_statement.md)
- ["OPEN Statement"](open_statement.md)

In other chapters:

- ["WHILE LOOP Statement"](controlstatements.md)