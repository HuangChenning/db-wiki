---
title: Basic LOOP Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/basic_loop_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

With each iteration of the basic `LOOP` statement, its statements run and control returns to the top of the loop. The `LOOP` statement ends when a statement inside the loop transfers control outside the loop or raises an exception.

Topics

Syntax

basic\_loop\_statement::=

![basic_loop_statement](img/basic_loop_statement.gif)

> ```
> LOOP statement... END LOOP [ label ] ;
> ```
>
> [Copyright © 1996, 2014, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  
  

See ["statement::="](block.md).

Semantics

statement

To prevent an infinite loop, at least one statement must transfer control outside the loop. The statements that can transfer control outside the loop are:

- ["CONTINUE Statement"](continue_statement.md) (when it transfers control to the next iteration of an enclosing labeled loop)
- ["EXIT Statement"](exit_statement.md)
- ["GOTO Statement"](goto_statement.md)
- ["RAISE Statement"](raise_statement.md)

label

A label that identifies `basic_loop_statement` (see ["statement::="](block.md) and ["label"](block.md)). `CONTINUE`, `EXIT`, and `GOTO` statements can reference this label.

Labels improve readability, especially when `LOOP` statements are nested, but only if you ensure that the label ine the `END` `LOOP` statement matches a label at the beginning of the same `LOOP` statement (the compiler does not check).

Examples

- [Example 1-2, "Processing Query Result Rows One at a Time"](overview.md)
- [Example 4-9, "Basic LOOP Statement with EXIT Statement"](controlstatements.md)
- [Example 4-10, "Basic LOOP Statement with EXIT WHEN Statement"](controlstatements.md)
- [Example 4-11, "Nested, Labeled Basic LOOP Statements with EXIT WHEN Statements"](controlstatements.md)
- [Example 4-13, "CONTINUE Statement in Basic LOOP Statement"](controlstatements.md)
- [Example 4-14, "CONTINUE WHEN Statement in Basic LOOP Statement"](controlstatements.md)