---
title: "25.12.10 Performance Schema User-Defined Variable Tables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/performance-schema-user-variable-tables.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 25.12.10 Performance Schema User-Defined Variable Tables

The Performance Schema provides a `user_variables_by_thread` table that exposes user-defined variables. These are variables defined within a specific session and include a `@` character preceding the name; see [Section 9.4, “User-Defined Variables”](user-variables.md).

The `user_variables_by_thread` table has these columns:

- `THREAD_ID`
	The thread identifier of the session in which the variable is defined.
- `VARIABLE_NAME`
	The variable name, without the leading `@` character.
- `VARIABLE_VALUE`
	The variable value.

[`TRUNCATE TABLE`](truncate-table.md) is not permitted for the `user_variables_by_thread` table.