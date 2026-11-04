---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.6.5 Flow Control Statements"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/flow-control-statements.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.6.5 Flow Control Statements

MySQL supports the [`IF`](if.md), [`CASE`](case.md), [`ITERATE`](iterate.md), [`LEAVE`](leave.md) [`LOOP`](loop.md), [`WHILE`](while.md), and [`REPEAT`](repeat.md) constructs for flow control within stored programs. It also supports [`RETURN`](return.md) within stored functions.

Many of these constructs contain other statements, as indicated by the grammar specifications in the following sections. Such constructs may be nested. For example, an [`IF`](if.md) statement might contain a [`WHILE`](while.md) loop, which itself contains a [`CASE`](case.md) statement.

MySQL does not support `FOR` loops.