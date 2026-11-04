---
title: IF Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/if_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `IF` statement either runs or skips a sequence of one or more statements, depending on the value of a `BOOLEAN` expression.

Topics

Semantics

boolean\_expression

Expression whose value is `TRUE`, `FALSE`, or `NULL`.

The first `boolean_expression` is always evaluated. Each other `boolean_expression` is evaluated only if the values of the preceding expressions are `FALSE`.

If a `boolean_expression` is evaluated and its value is `TRUE`, the statements after the corresponding `THEN` run. The succeeding expressions are not evaluated, and the statements associated with them do not run.

ELSE

If no `boolean_expression` has the value `TRUE`, the statements after `ELSE` run.