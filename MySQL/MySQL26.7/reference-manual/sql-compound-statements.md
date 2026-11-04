---
title: "MySQL :: MySQL 26.7 Reference Manual :: 15.6 Compound Statement Syntax"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/sql-compound-statements.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 15.6 Compound Statement Syntax

This section describes the syntax for the [`BEGIN ... END`](begin-end.md) compound statement and other statements that can be used in the body of stored programs: Stored procedures and functions, triggers, and events. These objects are defined in terms of SQL code that is stored on the server for later invocation (see [Chapter 27, *Stored Objects*](stored-objects.md)).

A compound statement is a block that can contain other blocks; declarations for variables, condition handlers, and cursors; and flow control constructs such as loops and conditional tests.