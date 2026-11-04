---
title: "19.2.5 How Servers Evaluate Replication Filtering Rules"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/replication-rules.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 19.2.5 How Servers Evaluate Replication Filtering Rules

If a replication source server does not write a statement to its binary log, the statement is not replicated. If the server does log the statement, the statement is sent to all replicas and each replica determines whether to execute it or ignore it.

On the source, you can control which databases to log changes for by using the [`--binlog-do-db`](replication-options-binary-log.md) and [`--binlog-ignore-db`](replication-options-binary-log.md) options to control binary logging. For a description of the rules that servers use in evaluating these options, see [Section 19.2.5.1, “Evaluation of Database-Level Replication and Binary Logging Options”](replication-rules-db-options.md). You should not use these options to control which databases and tables are replicated. Instead, use filtering on the replica to control the events that are executed on the replica.

On the replica side, decisions about whether to execute or ignore statements received from the source are made according to the `--replicate-*` options that the replica was started with. (See [Section 19.1.6, “Replication and Binary Logging Options and Variables”](replication-options.md).) The filters governed by these options can also be set dynamically using the `CHANGE REPLICATION FILTER` statement. The rules governing such filters are the same whether they are created on startup using `--replicate-*` options or while the replica server is running by `CHANGE REPLICATION       FILTER`. Note that replication filters cannot be used on Group Replication-specific channels on a MySQL server instance that is configured for Group Replication, because filtering transactions on some servers would make the group unable to reach agreement on a consistent state.

In the simplest case, when there are no `--replicate-*` options, the replica executes all statements that it receives from the source. Otherwise, the result depends on the particular options given.

Database-level options ([`--replicate-do-db`](replication-options-replica.md), [`--replicate-ignore-db`](replication-options-replica.md)) are checked first; see [Section 19.2.5.1, “Evaluation of Database-Level Replication and Binary Logging Options”](replication-rules-db-options.md), for a description of this process. If no database-level options are used, option checking proceeds to any table-level options that may be in use (see [Section 19.2.5.2, “Evaluation of Table-Level Replication Options”](replication-rules-table-options.md), for a discussion of these). If one or more database-level options are used but none are matched, the statement is not replicated.

For statements affecting databases only (that is, [`CREATE DATABASE`](create-database.md), [`DROP DATABASE`](drop-database.md), and [`ALTER DATABASE`](alter-database.md)), database-level options always take precedence over any [`--replicate-wild-do-table`](replication-options-replica.md) options. In other words, for such statements, [`--replicate-wild-do-table`](replication-options-replica.md) options are checked if and only if there are no database-level options that apply.

To make it easier to determine what effect a given set of options has, it is recommended that you avoid mixing `do-*` and `ignore-*` options, or options containing wildcards with options which do not.

If any [`--replicate-rewrite-db`](replication-options-replica.md) options were specified, they are applied before the `--replicate-*` filtering rules are tested.

Note

All replication filtering options follow the same rules for case sensitivity that apply to names of databases and tables elsewhere in the MySQL server, including the effects of the [`lower_case_table_names`](server-system-variables.md) system variable.

Filtering rules are applied before performing any privilege checks; if a transaction is filtered out, no privilege check is performed for that transaction, and thus no error can be raised by it. See [Section 19.5.1.29, “Replica Errors During Replication”](replication-features-errors.md), for more information.