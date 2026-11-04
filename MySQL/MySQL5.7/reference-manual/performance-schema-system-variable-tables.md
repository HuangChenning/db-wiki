---
title: "25.12.13 Performance Schema System Variable Tables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/performance-schema-system-variable-tables.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 25.12.13 Performance Schema System Variable Tables

Note

The value of the [`show_compatibility_56`](server-system-variables.md) system variable affects the information available from the tables described here. For details, see the description of that variable in [Section 5.1.7, “Server System Variables”](server-system-variables.md).

The MySQL server maintains many system variables that indicate how it is configured (see [Section 5.1.7, “Server System Variables”](server-system-variables.md)). System variable information is available in these Performance Schema tables:

- `global_variables`: Global system variables. An application that wants only global values should use this table.
- `session_variables`: System variables for the current session. An application that wants all system variable values for its own session should use this table. It includes the session variables for its session, as well as the values of global variables that have no session counterpart.
- `variables_by_thread`: Session system variables for each active session. An application that wants to know the session variable values for specific sessions should use this table. It includes session variables only, identified by thread ID.

The session variable tables (`session_variables`, `variables_by_thread`) contain information only for active sessions, not terminated sessions.

The `global_variables` and `session_variables` tables have these columns:

- `VARIABLE_NAME`
	The system variable name.
- `VARIABLE_VALUE`
	The system variable value. For `global_variables`, this column contains the global value. For `session_variables`, this column contains the variable value in effect for the current session.

The `variables_by_thread` table has these columns:

- `THREAD_ID`
	The thread identifier of the session in which the system variable is defined.
- `VARIABLE_NAME`
	The system variable name.
- `VARIABLE_VALUE`
	The session variable value for the session named by the `THREAD_ID` column.

The `variables_by_thread` table contains system variable information only about foreground threads. If not all threads are instrumented by the Performance Schema, this table may miss some rows. In this case, the [`Performance_schema_thread_instances_lost`](performance-schema-status-variables.md) status variable is greater than zero.

[`TRUNCATE TABLE`](truncate-table.md) is not supported for Performance Schema system variable tables.