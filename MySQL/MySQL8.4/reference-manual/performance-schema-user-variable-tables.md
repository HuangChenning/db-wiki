---
title: "29.12.10 Performance Schema User-Defined Variable Tables"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/performance-schema-user-variable-tables.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 29.12.10 Performance Schema User-Defined Variable Tables

The Performance Schema provides a `user_variables_by_thread` table that exposes user-defined variables. These are variables defined within a specific session and include a `@` character preceding the name; see [Section 11.4, “User-Defined Variables”](user-variables.md).

The `user_variables_by_thread` table has these columns:

- `THREAD_ID`
	The thread identifier of the session in which the variable is defined.
- `VARIABLE_NAME`
	The variable name, without the leading `@` character.
- `VARIABLE_VALUE`
	The variable value.

The `user_variables_by_thread` table has these indexes:

- Primary key on (`THREAD_ID`, `VARIABLE_NAME`)

[`TRUNCATE TABLE`](truncate-table.md) is not permitted for the `user_variables_by_thread` table.