---
title: "28.5.3 The INFORMATION_SCHEMA TP_THREAD_GROUP_STATS Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/information-schema-tp-thread-group-stats-table.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 28.5.3 The INFORMATION\_SCHEMA TP\_THREAD\_GROUP\_STATS Table

As of MySQL 8.0.14, the thread pool `INFORMATION_SCHEMA` tables are also available as Performance Schema tables. (See [Section 29.12.16, “Performance Schema Thread Pool Tables”](performance-schema-thread-pool-tables.md).) The `INFORMATION_SCHEMA` tables are deprecated; expect them to be removed in a future version of MySQL. Applications should transition away from the old tables to the new tables. For example, if an application uses this query:

```
SELECT * FROM INFORMATION_SCHEMA.TP_THREAD_GROUP_STATS;
```

The application should use this query instead:

```
SELECT * FROM performance_schema.tp_thread_group_stats;
```

The `TP_THREAD_GROUP_STATS` table reports statistics per thread group. There is one row per group.

For descriptions of the columns in the `INFORMATION_SCHEMA` `TP_THREAD_GROUP_STATS` table, see [Section 29.12.16.2, “The tp\_thread\_group\_stats Table”](performance-schema-tp-thread-group-stats-table.md). The Performance Schema [`tp_thread_group_stats`](performance-schema-tp-thread-group-stats-table.md) table has equivalent columns.