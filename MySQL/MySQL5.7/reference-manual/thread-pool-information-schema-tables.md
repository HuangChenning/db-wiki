---
title: "24.5 INFORMATION_SCHEMA Thread Pool Tables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/thread-pool-information-schema-tables.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

The following sections describe the `INFORMATION_SCHEMA` tables associated with the thread pool plugin (see [Section 5.5.3, “MySQL Enterprise Thread Pool”](thread-pool.md)). They provide information about thread pool operation:

Rows in these tables represent snapshots in time. In the case of [`TP_THREAD_STATE`](information-schema-tp-thread-state-table.md), all rows for a thread group comprise a snapshot in time. Thus, the MySQL server holds the mutex of the thread group while producing the snapshot. But it does not hold mutexes on all thread groups at the same time, to prevent a statement against [`TP_THREAD_STATE`](information-schema-tp-thread-state-table.md) from blocking the entire MySQL server.

The thread pool `INFORMATION_SCHEMA` tables are implemented by individual plugins and the decision whether to load one can be made independently of the others (see [Section 5.5.3.2, “Thread Pool Installation”](thread-pool-installation.md)). However, the content of all the tables depends on the thread pool plugin being enabled. If a table plugin is enabled but the thread pool plugin is not, the table becomes visible and can be accessed, but is empty.