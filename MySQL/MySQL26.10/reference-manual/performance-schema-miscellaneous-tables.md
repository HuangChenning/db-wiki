---
title: "MySQL :: MySQL 26.10 Reference Manual :: 29.12.23 Performance Schema Miscellaneous Tables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/performance-schema-miscellaneous-tables.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 29.12.23 Performance Schema Miscellaneous Tables

The following sections describe tables that do not fall into the table categories discussed in the preceding sections:

- [`component_scheduler_tasks`](performance-schema-component-scheduler-tasks-table.md): The current status of each scheduled task.
- [`connection_control_failed_login_attempts`](performance-schema-connection-control-failed-login-attempts-table.md): The current number of consecutive failed connection attempts per account.
- [`error_log`](performance-schema-error-log-table.md): The most recent events written to the error log.
- [`host_cache`](performance-schema-host-cache-table.md): Information from the internal host cache.
- [`innodb_redo_log_files`](performance-schema-innodb-redo-log-files-table.md): Information about InnoDB redo log files.
- [`log_status`](performance-schema-log-status-table.md): Information about server logs for backup purposes.
- [`mysql_option`](performance-schema-mysql-option-table.md): Information about features available in the MySQL Server.
- [`performance_timers`](performance-schema-performance-timers-table.md): Which event timers are available.
- [`processlist`](performance-schema-processlist-table.md): Information about server processes.
- [`threads`](performance-schema-threads-table.md): Information about server threads.
- [`tls_channel_status`](performance-schema-tls-channel-status-table.md): TLS context properties for connection interfaces.
- [`user_defined_functions`](performance-schema-user-defined-functions-table.md): Loadable functions registered by a component, plugin, or [`CREATE             FUNCTION`](create-function-loadable.md) statement.