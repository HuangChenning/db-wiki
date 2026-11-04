---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-control-statements.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## 4 PL/SQL Control Statements

PL/SQL has three categories of control statements: conditional selection statements, loop statements and sequential control statements.

PL/SQL categories of control statements are:

- Conditional selection statements, which run different statements for different data values.
	The conditional selection statements are `IF` and `CASE`.
- Loop statements, which run the same statements with a series of different data values.
	The loop statements are the basic `LOOP`, `FOR` `LOOP`, and `WHILE` `LOOP`.
	The `EXIT` statement transfers control to the end of a loop. The `CONTINUE` statement exits the current iteration of a loop and transfers control to the next iteration. Both `EXIT` and `CONTINUE` have an optional `WHEN` clause, where you can specify a condition.
- Sequential control statements, which are not crucial to PL/SQL programming.
	The sequential control statements are `GOTO`, which goes to a specified statement, and `NULL`, which does nothing.

Topics