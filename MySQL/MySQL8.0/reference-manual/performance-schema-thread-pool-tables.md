---
title: "29.12.16 Performance Schema Thread Pool Tables"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-thread-pool-tables.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 29.12.16 Performance Schema Thread Pool Tables

Note

The Performance Schema tables described here are available as of MySQL 8.0.14. Prior to MySQL 8.0.14, use the corresponding `INFORMATION_SCHEMA` tables instead; see [Section 28.5, “INFORMATION\_SCHEMA Thread Pool Tables”](thread-pool-information-schema-tables.md).

The following sections describe the Performance Schema tables associated with the thread pool plugin (see [Section 7.6.3, “MySQL Enterprise Thread Pool”](thread-pool.md)). They provide information about thread pool operation:

- [`tp_thread_group_state`](performance-schema-tp-thread-group-state-table.md): Information about thread pool thread group states.
- [`tp_thread_group_stats`](performance-schema-tp-thread-group-stats-table.md): Thread group statistics.
- [`tp_thread_state`](performance-schema-tp-thread-state-table.md): Information about thread pool thread states.

Rows in these tables represent snapshots in time. In the case of [`tp_thread_state`](performance-schema-tp-thread-state-table.md), all rows for a thread group comprise a snapshot in time. Thus, the MySQL server holds the mutex of the thread group while producing the snapshot. But it does not hold mutexes on all thread groups at the same time, to prevent a statement against [`tp_thread_state`](performance-schema-tp-thread-state-table.md) from blocking the entire MySQL server.

The Performance Schema thread pool tables are implemented by the thread pool plugin and are loaded and unloaded when that plugin is loaded and unloaded (see [Section 7.6.3.2, “Thread Pool Installation”](thread-pool-installation.md)). No special configuration step for the tables is needed. However, the tables depend on the thread pool plugin being enabled. If the thread pool plugin is loaded but disabled, the tables are not created.