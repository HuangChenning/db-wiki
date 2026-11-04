---
title: "17.12.7 Online DDL Failure Conditions"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/innodb-online-ddl-failure-conditions.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 17.12.7 Online DDL Failure Conditions

The failure of an online DDL operation is typically due to one of the following conditions:

- An `ALGORITHM` clause specifies an algorithm that is not compatible with the particular type of DDL operation or storage engine.
- A `LOCK` clause specifies a low degree of locking (`SHARED` or `NONE`) that is not compatible with the particular type of DDL operation.
- A timeout occurs while waiting for an [exclusive lock](glossary.md) on the table, which may be needed briefly during the initial and final phases of the DDL operation.
- The [`tmpdir`](server-system-variables.md) or [`innodb_tmpdir`](innodb-parameters.md) file system runs out of disk space, while MySQL writes temporary sort files on disk during index creation. For more information, see [Section 17.12.3, “Online DDL Space Requirements”](innodb-online-ddl-space-requirements.md).
- The operation takes a long time and concurrent DML modifies the table so much that the size of the temporary online log exceeds the value of the [`innodb_online_alter_log_max_size`](innodb-parameters.md) configuration option. This condition causes a `DB_ONLINE_LOG_TOO_BIG` error.
- Concurrent DML makes changes to the table that are allowed with the original table definition, but not with the new one. The operation only fails at the very end, when MySQL tries to apply all the changes from concurrent DML statements. For example, you might insert duplicate values into a column while a unique index is being created, or you might insert `NULL` values into a column while creating a [primary key](glossary.md) index on that column. The changes made by the concurrent DML take precedence, and the [`ALTER TABLE`](alter-table.md) operation is effectively [rolled back](glossary.md).