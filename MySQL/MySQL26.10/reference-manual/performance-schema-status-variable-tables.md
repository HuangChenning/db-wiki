---
title: "MySQL :: MySQL 26.10 Reference Manual :: 29.12.15 Performance Schema Status Variable Tables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/performance-schema-status-variable-tables.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 29.12.15 Performance Schema Status Variable Tables

The MySQL server maintains many status variables that provide information about its operation (see [Section 7.1.10, “Server Status Variables”](server-status-variables.md)). Status variable information is available in these Performance Schema tables:

- `global_status`: Global status variables. An application that wants only global values should use this table.
- `session_status`: Status variables for the current session. An application that wants all status variable values for its own session should use this table. It includes the session variables for its session, as well as the values of global variables that have no session counterpart.
- `status_by_thread`: Session status variables for each active session. An application that wants to know the session variable values for specific sessions should use this table. It includes session variables only, identified by thread ID.

There are also summary tables that provide status variable information aggregated by account, host name, and user name. See [Section 29.12.20.12, “Status Variable Summary Tables”](performance-schema-status-variable-summary-tables.md).

The session variable tables (`session_status`, `status_by_thread`) contain information only for active sessions, not terminated sessions.

The Performance Schema collects statistics for global status variables only for threads for which the `INSTRUMENTED` value is `YES` in the [`threads`](performance-schema-threads-table.md) table. Statistics for session status variables are always collected, regardless of the `INSTRUMENTED` value.

The Performance Schema does not collect statistics for ``Com_*`xxx`*`` status variables in the status variable tables. To obtain global and per-session statement execution counts, use the [`events_statements_summary_global_by_event_name`](performance-schema-statement-summary-tables.md) and [`events_statements_summary_by_thread_by_event_name`](performance-schema-statement-summary-tables.md) tables, respectively. For example:

```sql
SELECT EVENT_NAME, COUNT_STAR
FROM performance_schema.events_statements_summary_global_by_event_name
WHERE EVENT_NAME LIKE 'statement/sql/%';
```

The `global_status` and `session_status` tables have these columns:

- `VARIABLE_NAME`
	The status variable name.
- `VARIABLE_VALUE`
	The status variable value. For `global_status`, this column contains the global value. For `session_status`, this column contains the variable value for the current session.

The `global_status` and `session_status` tables have these indexes:

- Primary key on (`VARIABLE_NAME`)

The `status_by_thread` table contains the status of each active thread. It has these columns:

- `THREAD_ID`
	The thread identifier of the session in which the status variable is defined.
- `VARIABLE_NAME`
	The status variable name.
- `VARIABLE_VALUE`
	The session variable value for the session named by the `THREAD_ID` column.

The `status_by_thread` table has these indexes:

- Primary key on (`THREAD_ID`, `VARIABLE_NAME`)

The `status_by_thread` table contains status variable information only about foreground threads. If the [`performance_schema_max_thread_instances`](performance-schema-system-variables.md) system variable is not autoscaled (signified by a value of −1) and the maximum permitted number of instrumented thread objects is not greater than the number of background threads, the table is empty.

The Performance Schema supports [`TRUNCATE         TABLE`](truncate-table.md) for status variable tables as follows:

- `global_status`: Resets thread, account, host, and user status. Resets global status variables except those that the server never resets.
- `session_status`: Not supported.
- `status_by_thread`: Aggregates status for all threads to the global status and account status, then resets thread status. If account statistics are not collected, the session status is added to host and user status, if host and user status are collected.
	Account, host, and user statistics are not collected if the [`performance_schema_accounts_size`](performance-schema-system-variables.md), [`performance_schema_hosts_size`](performance-schema-system-variables.md), and [`performance_schema_users_size`](performance-schema-system-variables.md) system variables, respectively, are set to 0.

[`FLUSH STATUS`](flush.md) adds the session status from all active sessions to the global status variables, resets the status of all active sessions, and resets account, host, and user status values aggregated from disconnected sessions.