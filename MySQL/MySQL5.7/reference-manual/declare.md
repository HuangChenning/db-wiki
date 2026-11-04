---
title: "13.6.3 DECLARE Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/declare.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.6.3 DECLARE Statement

The `DECLARE` statement is used to define various items local to a program:

- Local variables. See [Section 13.6.4, “Variables in Stored Programs”](stored-program-variables.md).
- Conditions and handlers. See [Section 13.6.7, “Condition Handling”](condition-handling.md).
- Cursors. See [Section 13.6.6, “Cursors”](cursors.md).

`DECLARE` is permitted only inside a [`BEGIN ... END`](begin-end.md) compound statement and must be at its start, before any other statements.

Declarations must follow a certain order. Cursor declarations must appear before handler declarations. Variable and condition declarations must appear before cursor or handler declarations.