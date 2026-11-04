---
title: "MySQL :: MySQL 26.10 Reference Manual :: 29.12.16 Performance Schema Thread Pool Tables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/performance-schema-thread-pool-tables.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 29.12.16 Performance Schema Thread Pool Tables

The following sections describe the Performance Schema tables associated with the thread pool plugin (see [Section 7.6.3, “MySQL Thread Pool”](thread-pool.md)). They provide information about thread pool operation:

Rows in these tables represent snapshots in time. In the case of [`tp_thread_state`](performance-schema-tp-thread-state-table.md), all rows for a thread group comprise a snapshot in time. Thus, the MySQL server holds the mutex of the thread group while producing the snapshot. But it does not hold mutexes on all thread groups at the same time, to prevent a statement against [`tp_thread_state`](performance-schema-tp-thread-state-table.md) from blocking the entire MySQL server.

The Performance Schema thread pool tables are implemented by the thread pool plugin and are loaded and unloaded when that plugin is loaded and unloaded (see [Section 7.6.3.2, “Thread Pool Installation”](thread-pool-installation.md)). No special configuration step for the tables is needed. However, the tables depend on the thread pool plugin being enabled. If the thread pool plugin is loaded but disabled, the tables are not created.