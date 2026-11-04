---
title: "MySQL :: MySQL 26.10 Reference Manual :: 28.5.4 The INFORMATION_SCHEMA TP_THREAD_STATE Table"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/information-schema-tp-thread-state-table.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 28.5.4 The INFORMATION\_SCHEMA TP\_THREAD\_STATE Table

The `INFORMATION_SCHEMA` thread pool tables are deprecated, and subject to removal in a future version of MySQL. You should use the versions available as Performance Schema tables instead. See [Section 29.12.16, “Performance Schema Thread Pool Tables”](performance-schema-thread-pool-tables.md). Applications should transition away from the old tables to the new tables. For example, if an application uses this query:

```sql
SELECT * FROM INFORMATION_SCHEMA.TP_THREAD_STATE;
```

The application should use this query instead:

```sql
SELECT * FROM performance_schema.tp_thread_state;
```

The `TP_THREAD_STATE` table has one row per thread created by the thread pool to handle connections.

For descriptions of the columns in the `INFORMATION_SCHEMA` `TP_THREAD_STATE` table, see [Section 29.12.16.4, “The tp\_thread\_state Table”](performance-schema-tp-thread-state-table.md). The Performance Schema [`tp_thread_state`](performance-schema-tp-thread-state-table.md) table has equivalent columns.