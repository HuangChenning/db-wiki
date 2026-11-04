---
title: "MySQL :: MySQL 26.7 Reference Manual :: 27.3.6 JavaScript SQL API"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/srjs-sql-api.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 27.3.6 JavaScript SQL API

This section provides reference information for the SQL and result set API supported by JavaScript stored routines in the MLE Component.

The API supports the top-level objects listed here:

- [`Column`](srjsapi-column.md): Result set column metadata.
- [`PreparedStatement`](srjsapi-preparedstatement.md): Handler for execution of prepared statements.
- [`Row`](srjsapi-row.md): Row in a result set.
- [`Session`](srjsapi-session.md): MySQL user session. For information about `Session` transactional methods such as [`startTransaction()`](srjsapi-transactions.md), [`commit()`](srjsapi-transactions.md), and [`rollback()`](srjsapi-transactions.md), see [Section 27.3.6.11, “JavaScript Transaction API”](srjsapi-transactions.md).
- [`SqlExecute`](srjsapi-sqlexecute.md): Handler for execution of (simple) SQL statements. Its [`execute()`](srjsapi-sqlexecute.md) method executes an SQL statement.
- [`SqlResult`](srjsapi-sqlresult.md): Result set returned by an SQL statement.
- [`Warning`](srjsapi-warning.md): Warning raised by statement execution.

The SQL API can be used only within JavaScript stored procedures, and cannot be used within JavaScript stored functions.