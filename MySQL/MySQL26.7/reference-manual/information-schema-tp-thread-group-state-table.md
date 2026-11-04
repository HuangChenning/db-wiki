---
title: "MySQL :: MySQL 26.7 Reference Manual :: 28.5.2 The INFORMATION_SCHEMA TP_THREAD_GROUP_STATE Table"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/information-schema-tp-thread-group-state-table.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 28.5.2 The INFORMATION\_SCHEMA TP\_THREAD\_GROUP\_STATE Table

The `INFORMATION_SCHEMA` thread pool tables are deprecated, and subject to removal in a future version of MySQL. You should use the versions available as Performance Schema tables insted. See [Section 29.12.16, “Performance Schema Thread Pool Tables”](performance-schema-thread-pool-tables.md). Applications should transition away from the old tables to the new tables. For example, if an application uses this query:

```sql
SELECT * FROM INFORMATION_SCHEMA.TP_THREAD_GROUP_STATE;
```

The application should use this query instead:

```sql
SELECT * FROM performance_schema.tp_thread_group_state;
```

The `TP_THREAD_GROUP_STATE` table has one row per thread group in the thread pool. Each row provides information about the current state of a group.

For descriptions of the columns in the `INFORMATION_SCHEMA` `TP_THREAD_GROUP_STATE` table, see [Section 29.12.16.2, “The tp\_thread\_group\_state Table”](performance-schema-tp-thread-group-state-table.md). The Performance Schema [`tp_thread_group_state`](performance-schema-tp-thread-group-state-table.md) table has equivalent columns.