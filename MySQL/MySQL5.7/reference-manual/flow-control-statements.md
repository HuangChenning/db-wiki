---
title: "13.6.5 Flow Control Statements"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/flow-control-statements.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.6.5 Flow Control Statements

MySQL supports the [`IF`](if.md), [`CASE`](case.md), [`ITERATE`](iterate.md), [`LEAVE`](leave.md) [`LOOP`](loop.md), [`WHILE`](while.md), and [`REPEAT`](repeat.md) constructs for flow control within stored programs. It also supports [`RETURN`](return.md) within stored functions.

Many of these constructs contain other statements, as indicated by the grammar specifications in the following sections. Such constructs may be nested. For example, an [`IF`](if.md) statement might contain a [`WHILE`](while.md) loop, which itself contains a [`CASE`](case.md) statement.

MySQL does not support `FOR` loops.