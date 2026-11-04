---
title: "28.5 INFORMATION_SCHEMA Thread Pool Tables"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/thread-pool-information-schema-tables.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

The `INFORMATION_SCHEMA` thread pool tables are deprecated, and subject to removal in a future version of MySQL. Accessing any of these tables produces a warning; you should use the versions available as Performance Schema tables instead. See [Section 29.12.16, “Performance Schema Thread Pool Tables”](performance-schema-thread-pool-tables.md). Applications should transition away from the old tables to the new tables. For example, if an application uses this query:

```
SELECT * FROM INFORMATION_SCHEMA.TP_THREAD_STATE;
```

The application should use this query instead:

```
SELECT * FROM performance_schema.tp_thread_state;
```

The following sections describe the `INFORMATION_SCHEMA` tables associated with the thread pool plugin (see [Section 7.6.3, “MySQL Enterprise Thread Pool”](thread-pool.md)). They provide information about thread pool operation:

- [`TP_THREAD_GROUP_STATE`](information-schema-tp-thread-group-state-table.md): Information about thread pool thread group states
- [`TP_THREAD_GROUP_STATS`](information-schema-tp-thread-group-stats-table.md): Thread group statistics
- [`TP_THREAD_STATE`](information-schema-tp-thread-state-table.md): Information about thread pool thread states

Rows in these tables represent snapshots in time. In the case of `TP_THREAD_STATE`, all rows for a thread group comprise a snapshot in time. Thus, the MySQL server holds the mutex of the thread group while producing the snapshot. But it does not hold mutexes on all thread groups at the same time, to prevent a statement against `TP_THREAD_STATE` from blocking the entire MySQL server.

The `INFORMATION_SCHEMA` thread pool tables are implemented by individual plugins and the decision whether to load one can be made independently of the others (see [Section 7.6.3.2, “Thread Pool Installation”](thread-pool-installation.md)). However, the content of all the tables depends on the thread pool plugin being enabled. If a table plugin is enabled but the thread pool plugin is not, the table becomes visible and can be accessed but is empty.