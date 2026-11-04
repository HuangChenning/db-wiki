---
title: GOTO Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/goto_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `GOTO` statement transfers control to a labeled block or statement.

If a `GOTO` statement exits a cursor `FOR` `LOOP` statement prematurely, the cursor closes.

Restrictions on GOTO Statement

- A `GOTO` statement cannot transfer control into an `IF` statement, `CASE` statement, `LOOP` statement, or sub-block.
- A `GOTO` statement cannot transfer control from one `IF` statement clause to another, or from one `CASE` statement `WHEN` clause to another.
- A `GOTO` statement cannot transfer control out of a subprogram.
- A `GOTO` statement cannot transfer control into an exception handler.
- A `GOTO` statement cannot transfer control from an exception handler back into the current block (but it can transfer control from an exception handler into an enclosing block).

Topics

Syntax

goto\_statement::=

  
[Description of the illustration goto\_statement.gif](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/img_text/goto_statement.htm)  

Semantics

label

Identifies either a block or a statement (see ["plsql\_block::="](block.md), ["statement::="](block.md), and ["label"](block.md)).

If `label` is not in the current block, then the `GOTO` statement transfers control to the first enclosing block in which `label` appears.