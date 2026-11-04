---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/FOR-LOOP-statement.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## FOR LOOP Statement

With each iteration of the `FOR` `LOOP` statement, its statements run, its index is either incremented or decremented, and control returns to the top of the loop. The `FOR` `LOOP` statement ends when its index reaches a specified value, or when a statement inside the loop transfers control outside the loop or raises an exception.

Topics

Syntax

for\_loop\_statement::=

![for_loop_statement](img/for_loop_statement.gif)

> ```
> [ FOR index IN [ REVERSE ] lower_bound .. upper_bound
>     LOOP statement... END LOOP [ label ] ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2026, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([statement::=](block.md))

Semantics

for\_loop\_statement

index

Name for the implicitly declared integer variable that is local to the `FOR` `LOOP` statement. Statements outside the loop cannot reference `index`. Statements inside the loop can reference `index`, but cannot change its value. After the `FOR` `LOOP` statement runs, `index` is undefined.

See Also:

" [FOR LOOP Index](loop-statements.md) "

\[ REVERSE \] lower\_bound.. upper\_bound

`lower_bound` and `upper_bound` must evaluate to numbers (see " [Lower Bound and Upper Bound](loop-statements.md) "). PL/SQL evaluates `lower_bound` and `upper_bound` once, when the `FOR` `LOOP` statement is entered, and stores them as temporary `PLS_INTEGER` values, rounding them to the nearest integer if necessary.

If `lower_bound` equals `upper_bound`, the `statements` run only once.

If `lower_bound` does not equal `upper_bound` when the `FOR` `LOOP` statement begins to run, then:

- If `REVERSE` is omitted:
	If `lower_bound` is greater than `upper_bound`, the `statements` do not run, and control transfers to the statement after the `FOR` `LOOP` statement.
	Otherwise, `lower_bound` is assigned to `index`, the `statements` run, and control returns to the top of the loop, where `index` is compared to `upper_bound`. If `index` is less than `upper_bound`, `index` is incremented by one, the `statements` run again, and control returns to the top of the loop. When `index` is greater than `upper_bound`, control transfers to the statement after the `FOR` `LOOP` statement.
- If `REVERSE` is specified:
	If `upper_bound` is less than `lower_bound`, the `statements` do not run, and control transfers to the statement after the `FOR` `LOOP` statement.
	Otherwise, `upper_bound` is assigned to `index`, the `statements` run, and control returns to the top of the loop, where `index` is compared to `lower_bound`. If `index` is greater than `lower_bound`, `index` is decremented by one, the `statements` run again, and control returns to the top of the loop. When `index` is less than `lower_bound`, control transfers to the statement after the `FOR` `LOOP` statement.

label

A label that identifies `for_loop_statement` (see " [statement::=](block.md) " and " [label](block.md) "). `CONTINUE`, `EXIT`, and `GOTO` statements can reference this label.

Labels improve readability, especially when `LOOP` statements are nested, but only if you ensure that the label in the `END` `LOOP` statement matches a label at the beginning of the same `LOOP` statement (the compiler does not check).

Examples

- [Example 4-15](loop-statements.md), "FOR LOOP Statements"
- [Example 4-16](loop-statements.md), "Reverse FOR LOOP Statements"
- [Example 4-17](loop-statements.md), "Simulating STEP Clause in FOR LOOP Statement"
- [Example 4-19](loop-statements.md), "Outside Statement References FOR LOOP Statement Index"
- [Example 4-20](loop-statements.md), "FOR LOOP Statement Index with Same Name as Variable"
- [Example 4-21](loop-statements.md), "FOR LOOP Statement References Variable with Same Name as Index"
- [Example 4-22](loop-statements.md), "Nested FOR LOOP Statements with Same Index Name"
- [Example 4-23](loop-statements.md), "FOR LOOP Statement Bounds"
- [Example 4-24](loop-statements.md), "Specifying FOR LOOP Statement Bounds at Run Time"

Related Topics

In this chapter:

- " [Basic LOOP Statement](basic-LOOP-statement.md) "
- " [CONTINUE Statement](CONTINUE-statement.md) "
- " [Cursor FOR LOOP Statement](cursor-FOR-LOOP-statement.md) "
- " [EXIT Statement](EXIT-statement.md) "
- " [FETCH Statement](FETCH-statement.md) "
- " [FORALL Statement](FORALL-statement.md) "
- " [OPEN Statement](OPEN-statement.md) "
- " [WHILE LOOP Statement](WHILE-LOOP-statement.md) "

In other chapters:

- " [FOR LOOP Statement](loop-statements.md) "