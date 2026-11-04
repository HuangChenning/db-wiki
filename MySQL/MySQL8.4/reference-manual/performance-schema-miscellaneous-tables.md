---
title: "29.12.22 Performance Schema Miscellaneous Tables"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/performance-schema-miscellaneous-tables.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 29.12.22 Performance Schema Miscellaneous Tables

The following sections describe tables that do not fall into the table categories discussed in the preceding sections:

- [`component_scheduler_tasks`](performance-schema-component-scheduler-tasks-table.md): The current status of each scheduled task.
- [`error_log`](performance-schema-error-log-table.md): The most recent events written to the error log.
- [`host_cache`](performance-schema-host-cache-table.md): Information from the internal host cache.
- [`innodb_redo_log_files`](performance-schema-innodb-redo-log-files-table.md): Information about InnoDB redo log files.
- [`log_status`](performance-schema-log-status-table.md): Information about server logs for backup purposes.
- [`performance_timers`](performance-schema-performance-timers-table.md): Which event timers are available.
- [`processlist`](performance-schema-processlist-table.md): Information about server processes.
- [`threads`](performance-schema-threads-table.md): Information about server threads.
- [`tls_channel_status`](performance-schema-tls-channel-status-table.md): TLS context properties for connection interfaces.
- [`user_defined_functions`](performance-schema-user-defined-functions-table.md): Loadable functions registered by a component, plugin, or [`CREATE             FUNCTION`](create-function-loadable.md) statement.