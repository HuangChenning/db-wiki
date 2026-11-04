---
title: "MySQL :: MySQL 26.10 Reference Manual :: 25.6.14 NDB API Statistics Counters and Variables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/mysql-cluster-ndb-api-statistics.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 25.6.14 NDB API Statistics Counters and Variables

A number of types of statistical counters relating to actions performed by or affecting [`Ndb`](https://dev.mysql.com/doc/ndbapi/en/ndb-ndb.html) objects are available. Such actions include starting and closing (or aborting) transactions; primary key and unique key operations; table, range, and pruned scans; threads blocked while waiting for the completion of various operations; and data and events sent and received by `NDBCLUSTER`. The counters are incremented inside the NDB kernel whenever NDB API calls are made or data is sent to or received by the data nodes. [**mysqld**](mysqld.md) exposes these counters as system status variables; their values can be read in the output of [`SHOW STATUS`](show-status.md), or by querying the Performance Schema [`session_status`](performance-schema-status-variable-tables.md) or [`global_status`](performance-schema-status-variable-tables.md) table. By comparing the values before and after statements operating on [`NDB`](mysql-cluster.md) tables, you can observe the corresponding actions taken on the API level, and thus the cost of performing the statement.

You can list all of these status variables using the following [`SHOW STATUS`](show-status.md) statement:

```sql
mysql> SHOW STATUS LIKE 'ndb_api%';
+----------------------------------------------+-------------+
| Variable_name                                | Value       |
+----------------------------------------------+-------------+
| Ndb_api_wait_exec_complete_count             | 11          |
| Ndb_api_wait_scan_result_count               | 14          |
| Ndb_api_wait_meta_request_count              | 74          |
| Ndb_api_wait_nanos_count                     | 31453031678 |
| Ndb_api_bytes_sent_count                     | 3336        |
| Ndb_api_bytes_received_count                 | 103568      |
| Ndb_api_trans_start_count                    | 10          |
| Ndb_api_trans_commit_count                   | 2           |
| Ndb_api_trans_abort_count                    | 4           |
| Ndb_api_trans_close_count                    | 10          |
| Ndb_api_pk_op_count                          | 6           |
| Ndb_api_uk_op_count                          | 0           |
| Ndb_api_table_scan_count                     | 3           |
| Ndb_api_range_scan_count                     | 1           |
| Ndb_api_pruned_scan_count                    | 0           |
| Ndb_api_scan_batch_count                     | 3           |
| Ndb_api_read_row_count                       | 11          |
| Ndb_api_trans_local_read_row_count           | 9           |
| Ndb_api_adaptive_send_forced_count           | 5           |
| Ndb_api_adaptive_send_unforced_count         | 11          |
| Ndb_api_adaptive_send_deferred_count         | 0           |
| Ndb_api_event_data_count                     | 0           |
| Ndb_api_event_nondata_count                  | 0           |
| Ndb_api_event_bytes_count                    | 0           |
| Ndb_api_event_data_count_injector            | 0           |
| Ndb_api_event_nondata_count_injector         | 0           |
| Ndb_api_event_bytes_count_injector           | 0           |
| Ndb_api_wait_exec_complete_count_slave       | 0           |
| Ndb_api_wait_scan_result_count_slave         | 0           |
| Ndb_api_wait_meta_request_count_slave        | 0           |
| Ndb_api_wait_nanos_count_slave               | 0           |
| Ndb_api_bytes_sent_count_slave               | 0           |
| Ndb_api_bytes_received_count_slave           | 0           |
| Ndb_api_trans_start_count_slave              | 0           |
| Ndb_api_trans_commit_count_slave             | 0           |
| Ndb_api_trans_abort_count_slave              | 0           |
| Ndb_api_trans_close_count_slave              | 0           |
| Ndb_api_pk_op_count_slave                    | 0           |
| Ndb_api_uk_op_count_slave                    | 0           |
| Ndb_api_table_scan_count_slave               | 0           |
| Ndb_api_range_scan_count_slave               | 0           |
| Ndb_api_pruned_scan_count_slave              | 0           |
| Ndb_api_scan_batch_count_slave               | 0           |
| Ndb_api_read_row_count_slave                 | 0           |
| Ndb_api_trans_local_read_row_count_slave     | 0           |
| Ndb_api_adaptive_send_forced_count_slave     | 0           |
| Ndb_api_adaptive_send_unforced_count_slave   | 0           |
| Ndb_api_adaptive_send_deferred_count_slave   | 0           |
| Ndb_api_wait_exec_complete_count_replica     | 0           |
| Ndb_api_wait_scan_result_count_replica       | 0           |
| Ndb_api_wait_meta_request_count_replica      | 0           |
| Ndb_api_wait_nanos_count_replica             | 0           |
| Ndb_api_bytes_sent_count_replica             | 0           |
| Ndb_api_bytes_received_count_replica         | 0           |
| Ndb_api_trans_start_count_replica            | 0           |
| Ndb_api_trans_commit_count_replica           | 0           |
| Ndb_api_trans_abort_count_replica            | 0           |
| Ndb_api_trans_close_count_replica            | 0           |
| Ndb_api_pk_op_count_replica                  | 0           |
| Ndb_api_uk_op_count_replica                  | 0           |
| Ndb_api_table_scan_count_replica             | 0           |
| Ndb_api_range_scan_count_replica             | 0           |
| Ndb_api_pruned_scan_count_replica            | 0           |
| Ndb_api_scan_batch_count_replica             | 0           |
| Ndb_api_read_row_count_replica               | 0           |
| Ndb_api_trans_local_read_row_count_replica   | 0           |
| Ndb_api_adaptive_send_forced_count_replica   | 0           |
| Ndb_api_adaptive_send_unforced_count_replica | 0           |
| Ndb_api_adaptive_send_deferred_count_replica | 0           |
| Ndb_api_wait_exec_complete_count_session     | 0           |
| Ndb_api_wait_scan_result_count_session       | 3           |
| Ndb_api_wait_meta_request_count_session      | 6           |
| Ndb_api_wait_nanos_count_session             | 2022486     |
| Ndb_api_bytes_sent_count_session             | 268         |
| Ndb_api_bytes_received_count_session         | 10332       |
| Ndb_api_trans_start_count_session            | 1           |
| Ndb_api_trans_commit_count_session           | 0           |
| Ndb_api_trans_abort_count_session            | 0           |
| Ndb_api_trans_close_count_session            | 1           |
| Ndb_api_pk_op_count_session                  | 0           |
| Ndb_api_uk_op_count_session                  | 0           |
| Ndb_api_table_scan_count_session             | 1           |
| Ndb_api_range_scan_count_session             | 0           |
| Ndb_api_pruned_scan_count_session            | 0           |
| Ndb_api_scan_batch_count_session             | 2           |
| Ndb_api_read_row_count_session               | 2           |
| Ndb_api_trans_local_read_row_count_session   | 2           |
| Ndb_api_adaptive_send_forced_count_session   | 1           |
| Ndb_api_adaptive_send_unforced_count_session | 0           |
| Ndb_api_adaptive_send_deferred_count_session | 0           |
+----------------------------------------------+-------------+
90 rows in set (0.00 sec)
```

These status variables are also available from the Performance Schema [`session_status`](performance-schema-status-variable-tables.md) and [`global_status`](performance-schema-status-variable-tables.md) tables, as shown here:

```sql
mysql> SELECT * FROM performance_schema.session_status
    ->   WHERE VARIABLE_NAME LIKE 'ndb_api%';
+----------------------------------------------+----------------+
| VARIABLE_NAME                                | VARIABLE_VALUE |
+----------------------------------------------+----------------+
| Ndb_api_wait_exec_complete_count             | 11             |
| Ndb_api_wait_scan_result_count               | 14             |
| Ndb_api_wait_meta_request_count              | 81             |
| Ndb_api_wait_nanos_count                     | 119485762051   |
| Ndb_api_bytes_sent_count                     | 3476           |
| Ndb_api_bytes_received_count                 | 105372         |
| Ndb_api_trans_start_count                    | 10             |
| Ndb_api_trans_commit_count                   | 2              |
| Ndb_api_trans_abort_count                    | 4              |
| Ndb_api_trans_close_count                    | 10             |
| Ndb_api_pk_op_count                          | 6              |
| Ndb_api_uk_op_count                          | 0              |
| Ndb_api_table_scan_count                     | 3              |
| Ndb_api_range_scan_count                     | 1              |
| Ndb_api_pruned_scan_count                    | 0              |
| Ndb_api_scan_batch_count                     | 3              |
| Ndb_api_read_row_count                       | 11             |
| Ndb_api_trans_local_read_row_count           | 9              |
| Ndb_api_adaptive_send_forced_count           | 5              |
| Ndb_api_adaptive_send_unforced_count         | 11             |
| Ndb_api_adaptive_send_deferred_count         | 0              |
| Ndb_api_event_data_count                     | 0              |
| Ndb_api_event_nondata_count                  | 0              |
| Ndb_api_event_bytes_count                    | 0              |
| Ndb_api_event_data_count_injector            | 0              |
| Ndb_api_event_nondata_count_injector         | 0              |
| Ndb_api_event_bytes_count_injector           | 0              |
| Ndb_api_wait_exec_complete_count_slave       | 0              |
| Ndb_api_wait_scan_result_count_slave         | 0              |
| Ndb_api_wait_meta_request_count_slave        | 0              |
| Ndb_api_wait_nanos_count_slave               | 0              |
| Ndb_api_bytes_sent_count_slave               | 0              |
| Ndb_api_bytes_received_count_slave           | 0              |
| Ndb_api_trans_start_count_slave              | 0              |
| Ndb_api_trans_commit_count_slave             | 0              |
| Ndb_api_trans_abort_count_slave              | 0              |
| Ndb_api_trans_close_count_slave              | 0              |
| Ndb_api_pk_op_count_slave                    | 0              |
| Ndb_api_uk_op_count_slave                    | 0              |
| Ndb_api_table_scan_count_slave               | 0              |
| Ndb_api_range_scan_count_slave               | 0              |
| Ndb_api_pruned_scan_count_slave              | 0              |
| Ndb_api_scan_batch_count_slave               | 0              |
| Ndb_api_read_row_count_slave                 | 0              |
| Ndb_api_trans_local_read_row_count_slave     | 0              |
| Ndb_api_adaptive_send_forced_count_slave     | 0              |
| Ndb_api_adaptive_send_unforced_count_slave   | 0              |
| Ndb_api_adaptive_send_deferred_count_slave   | 0              |
| Ndb_api_wait_exec_complete_count_replica     | 0              |
| Ndb_api_wait_scan_result_count_replica       | 0              |
| Ndb_api_wait_meta_request_count_replica      | 0              |
| Ndb_api_wait_nanos_count_replica             | 0              |
| Ndb_api_bytes_sent_count_replica             | 0              |
| Ndb_api_bytes_received_count_replica         | 0              |
| Ndb_api_trans_start_count_replica            | 0              |
| Ndb_api_trans_commit_count_replica           | 0              |
| Ndb_api_trans_abort_count_replica            | 0              |
| Ndb_api_trans_close_count_replica            | 0              |
| Ndb_api_pk_op_count_replica                  | 0              |
| Ndb_api_uk_op_count_replica                  | 0              |
| Ndb_api_table_scan_count_replica             | 0              |
| Ndb_api_range_scan_count_replica             | 0              |
| Ndb_api_pruned_scan_count_replica            | 0              |
| Ndb_api_scan_batch_count_replica             | 0              |
| Ndb_api_read_row_count_replica               | 0              |
| Ndb_api_trans_local_read_row_count_replica   | 0              |
| Ndb_api_adaptive_send_forced_count_replica   | 0              |
| Ndb_api_adaptive_send_unforced_count_replica | 0              |
| Ndb_api_adaptive_send_deferred_count_replica | 0              |
| Ndb_api_wait_exec_complete_count_session     | 0              |
| Ndb_api_wait_scan_result_count_session       | 3              |
| Ndb_api_wait_meta_request_count_session      | 6              |
| Ndb_api_wait_nanos_count_session             | 2022486        |
| Ndb_api_bytes_sent_count_session             | 268            |
| Ndb_api_bytes_received_count_session         | 10332          |
| Ndb_api_trans_start_count_session            | 1              |
| Ndb_api_trans_commit_count_session           | 0              |
| Ndb_api_trans_abort_count_session            | 0              |
| Ndb_api_trans_close_count_session            | 1              |
| Ndb_api_pk_op_count_session                  | 0              |
| Ndb_api_uk_op_count_session                  | 0              |
| Ndb_api_table_scan_count_session             | 1              |
| Ndb_api_range_scan_count_session             | 0              |
| Ndb_api_pruned_scan_count_session            | 0              |
| Ndb_api_scan_batch_count_session             | 2              |
| Ndb_api_read_row_count_session               | 2              |
| Ndb_api_trans_local_read_row_count_session   | 2              |
| Ndb_api_adaptive_send_forced_count_session   | 1              |
| Ndb_api_adaptive_send_unforced_count_session | 0              |
| Ndb_api_adaptive_send_deferred_count_session | 0              |
+----------------------------------------------+----------------+
90 rows in set (0.00 sec)

mysql> SELECT * FROM performance_schema.global_status
    ->     WHERE VARIABLE_NAME LIKE 'ndb_api%';
+----------------------------------------------+----------------+
| VARIABLE_NAME                                | VARIABLE_VALUE |
+----------------------------------------------+----------------+
| Ndb_api_wait_exec_complete_count             | 11             |
| Ndb_api_wait_scan_result_count               | 14             |
| Ndb_api_wait_meta_request_count              | 88             |
| Ndb_api_wait_nanos_count                     | 159810484729   |
| Ndb_api_bytes_sent_count                     | 3616           |
| Ndb_api_bytes_received_count                 | 107176         |
| Ndb_api_trans_start_count                    | 10             |
| Ndb_api_trans_commit_count                   | 2              |
| Ndb_api_trans_abort_count                    | 4              |
| Ndb_api_trans_close_count                    | 10             |
| Ndb_api_pk_op_count                          | 6              |
| Ndb_api_uk_op_count                          | 0              |
| Ndb_api_table_scan_count                     | 3              |
| Ndb_api_range_scan_count                     | 1              |
| Ndb_api_pruned_scan_count                    | 0              |
| Ndb_api_scan_batch_count                     | 3              |
| Ndb_api_read_row_count                       | 11             |
| Ndb_api_trans_local_read_row_count           | 9              |
| Ndb_api_adaptive_send_forced_count           | 5              |
| Ndb_api_adaptive_send_unforced_count         | 11             |
| Ndb_api_adaptive_send_deferred_count         | 0              |
| Ndb_api_event_data_count                     | 0              |
| Ndb_api_event_nondata_count                  | 0              |
| Ndb_api_event_bytes_count                    | 0              |
| Ndb_api_event_data_count_injector            | 0              |
| Ndb_api_event_nondata_count_injector         | 0              |
| Ndb_api_event_bytes_count_injector           | 0              |
| Ndb_api_wait_exec_complete_count_slave       | 0              |
| Ndb_api_wait_scan_result_count_slave         | 0              |
| Ndb_api_wait_meta_request_count_slave        | 0              |
| Ndb_api_wait_nanos_count_slave               | 0              |
| Ndb_api_bytes_sent_count_slave               | 0              |
| Ndb_api_bytes_received_count_slave           | 0              |
| Ndb_api_trans_start_count_slave              | 0              |
| Ndb_api_trans_commit_count_slave             | 0              |
| Ndb_api_trans_abort_count_slave              | 0              |
| Ndb_api_trans_close_count_slave              | 0              |
| Ndb_api_pk_op_count_slave                    | 0              |
| Ndb_api_uk_op_count_slave                    | 0              |
| Ndb_api_table_scan_count_slave               | 0              |
| Ndb_api_range_scan_count_slave               | 0              |
| Ndb_api_pruned_scan_count_slave              | 0              |
| Ndb_api_scan_batch_count_slave               | 0              |
| Ndb_api_read_row_count_slave                 | 0              |
| Ndb_api_trans_local_read_row_count_slave     | 0              |
| Ndb_api_adaptive_send_forced_count_slave     | 0              |
| Ndb_api_adaptive_send_unforced_count_slave   | 0              |
| Ndb_api_adaptive_send_deferred_count_slave   | 0              |
| Ndb_api_wait_exec_complete_count_replica     | 0              |
| Ndb_api_wait_scan_result_count_replica       | 0              |
| Ndb_api_wait_meta_request_count_replica      | 0              |
| Ndb_api_wait_nanos_count_replica             | 0              |
| Ndb_api_bytes_sent_count_replica             | 0              |
| Ndb_api_bytes_received_count_replica         | 0              |
| Ndb_api_trans_start_count_replica            | 0              |
| Ndb_api_trans_commit_count_replica           | 0              |
| Ndb_api_trans_abort_count_replica            | 0              |
| Ndb_api_trans_close_count_replica            | 0              |
| Ndb_api_pk_op_count_replica                  | 0              |
| Ndb_api_uk_op_count_replica                  | 0              |
| Ndb_api_table_scan_count_replica             | 0              |
| Ndb_api_range_scan_count_replica             | 0              |
| Ndb_api_pruned_scan_count_replica            | 0              |
| Ndb_api_scan_batch_count_replica             | 0              |
| Ndb_api_read_row_count_replica               | 0              |
| Ndb_api_trans_local_read_row_count_replica   | 0              |
| Ndb_api_adaptive_send_forced_count_replica   | 0              |
| Ndb_api_adaptive_send_unforced_count_replica | 0              |
| Ndb_api_adaptive_send_deferred_count_replica | 0              |
| Ndb_api_wait_exec_complete_count_session     | 0              |
| Ndb_api_wait_scan_result_count_session       | 3              |
| Ndb_api_wait_meta_request_count_session      | 6              |
| Ndb_api_wait_nanos_count_session             | 2022486        |
| Ndb_api_bytes_sent_count_session             | 268            |
| Ndb_api_bytes_received_count_session         | 10332          |
| Ndb_api_trans_start_count_session            | 1              |
| Ndb_api_trans_commit_count_session           | 0              |
| Ndb_api_trans_abort_count_session            | 0              |
| Ndb_api_trans_close_count_session            | 1              |
| Ndb_api_pk_op_count_session                  | 0              |
| Ndb_api_uk_op_count_session                  | 0              |
| Ndb_api_table_scan_count_session             | 1              |
| Ndb_api_range_scan_count_session             | 0              |
| Ndb_api_pruned_scan_count_session            | 0              |
| Ndb_api_scan_batch_count_session             | 2              |
| Ndb_api_read_row_count_session               | 2              |
| Ndb_api_trans_local_read_row_count_session   | 2              |
| Ndb_api_adaptive_send_forced_count_session   | 1              |
| Ndb_api_adaptive_send_unforced_count_session | 0              |
| Ndb_api_adaptive_send_deferred_count_session | 0              |
+----------------------------------------------+----------------+
90 rows in set (0.01 sec)
```

Each [`Ndb`](https://dev.mysql.com/doc/ndbapi/en/ndb-ndb.html) object has its own counters. NDB API applications can read the values of the counters for use in optimization or monitoring. For multithreaded clients which use more than one [`Ndb`](https://dev.mysql.com/doc/ndbapi/en/ndb-ndb.html) object concurrently, it is also possible to obtain a summed view of counters from all [`Ndb`](https://dev.mysql.com/doc/ndbapi/en/ndb-ndb.html) objects belonging to a given [`Ndb_cluster_connection`](https://dev.mysql.com/doc/ndbapi/en/ndb-ndb-cluster-connection.html).

Four sets of these counters are exposed. One set applies to the current session only; the other 3 are global. *This is in spite of the fact that their values can be obtained as either session or global status variables in the [**mysql**](mysql.md) client*. This means that specifying the `SESSION` or `GLOBAL` keyword with [`SHOW STATUS`](show-status.md) has no effect on the values reported for NDB API statistics status variables, and the value for each of these variables is the same whether the value is obtained from the equivalent column of the [`session_status`](performance-schema-status-variable-tables.md) or the [`global_status`](performance-schema-status-variable-tables.md) table.

- *Session counters (session specific)*
	Session counters relate to the [`Ndb`](https://dev.mysql.com/doc/ndbapi/en/ndb-ndb.html) objects in use by (only) the current session. Use of such objects by other MySQL clients does not influence these counts.
	In order to minimize confusion with standard MySQL session variables, we refer to the variables that correspond to these NDB API session counters as “ `_session` variables”, with a leading underscore.
- *Replica counters (global)*
	This set of counters relates to the [`Ndb`](https://dev.mysql.com/doc/ndbapi/en/ndb-ndb.html) objects used by the replica SQL thread, if any. If this [**mysqld**](mysqld.md) does not act as a replica, or does not use [`NDB`](mysql-cluster.md) tables, then all of these counts are 0.
	We refer to the related status variables as “ `_replica` variables” (with a leading underscore).
- *Injector counters (global)*
	Injector counters relate to the [`Ndb`](https://dev.mysql.com/doc/ndbapi/en/ndb-ndb.html) object used to listen to cluster events by the binary log injector thread. Even when not writing a binary log, [**mysqld**](mysqld.md) processes attached to an NDB Cluster continue to listen for some events, such as schema changes.
	We refer to the status variables that correspond to NDB API injector counters as “ `_injector` variables” (with a leading underscore).
- *Server (Global) counters (global)*
	This set of counters relates to all [`Ndb`](https://dev.mysql.com/doc/ndbapi/en/ndb-ndb.html) objects currently used by this [**mysqld**](mysqld.md). This includes all MySQL client applications, the replica SQL thread (if any), the binary log injector, and the [`NDB`](mysql-cluster.md) utility thread.
	We refer to the status variables that correspond to these counters as “global variables” or “ [**mysqld**](mysqld.md) -level variables”.

You can obtain values for a particular set of variables by additionally filtering for the substring `session`, `replica`, or `injector` in the variable name (along with the common prefix `Ndb_api`). For `_session` variables, this can be done as shown here:

```sql
mysql> SHOW STATUS LIKE 'ndb_api%session';
+----------------------------------------------+---------+
| Variable_name                                | Value   |
+----------------------------------------------+---------+
| Ndb_api_wait_exec_complete_count_session     | 0       |
| Ndb_api_wait_scan_result_count_session       | 3       |
| Ndb_api_wait_meta_request_count_session      | 6       |
| Ndb_api_wait_nanos_count_session             | 2022486 |
| Ndb_api_bytes_sent_count_session             | 268     |
| Ndb_api_bytes_received_count_session         | 10332   |
| Ndb_api_trans_start_count_session            | 1       |
| Ndb_api_trans_commit_count_session           | 0       |
| Ndb_api_trans_abort_count_session            | 0       |
| Ndb_api_trans_close_count_session            | 1       |
| Ndb_api_pk_op_count_session                  | 0       |
| Ndb_api_uk_op_count_session                  | 0       |
| Ndb_api_table_scan_count_session             | 1       |
| Ndb_api_range_scan_count_session             | 0       |
| Ndb_api_pruned_scan_count_session            | 0       |
| Ndb_api_scan_batch_count_session             | 2       |
| Ndb_api_read_row_count_session               | 2       |
| Ndb_api_trans_local_read_row_count_session   | 2       |
| Ndb_api_adaptive_send_forced_count_session   | 1       |
| Ndb_api_adaptive_send_unforced_count_session | 0       |
| Ndb_api_adaptive_send_deferred_count_session | 0       |
+----------------------------------------------+---------+
21 rows in set (0.00 sec)
```

To obtain a listing of the NDB API [**mysqld**](mysqld.md) -level status variables, filter for variable names beginning with `ndb_api` and ending in `_count`, like this:

```sql
mysql> SELECT * FROM performance_schema.session_status
    ->     WHERE VARIABLE_NAME LIKE 'ndb_api%count';
+------------------------------------+----------------+
| VARIABLE_NAME                      | VARIABLE_VALUE |
+------------------------------------+----------------+
| NDB_API_WAIT_EXEC_COMPLETE_COUNT   | 4              |
| NDB_API_WAIT_SCAN_RESULT_COUNT     | 3              |
| NDB_API_WAIT_META_REQUEST_COUNT    | 28             |
| NDB_API_WAIT_NANOS_COUNT           | 53756398       |
| NDB_API_BYTES_SENT_COUNT           | 1060           |
| NDB_API_BYTES_RECEIVED_COUNT       | 9724           |
| NDB_API_TRANS_START_COUNT          | 3              |
| NDB_API_TRANS_COMMIT_COUNT         | 2              |
| NDB_API_TRANS_ABORT_COUNT          | 0              |
| NDB_API_TRANS_CLOSE_COUNT          | 3              |
| NDB_API_PK_OP_COUNT                | 2              |
| NDB_API_UK_OP_COUNT                | 0              |
| NDB_API_TABLE_SCAN_COUNT           | 1              |
| NDB_API_RANGE_SCAN_COUNT           | 0              |
| NDB_API_PRUNED_SCAN_COUNT          | 0              |
| NDB_API_SCAN_BATCH_COUNT           | 0              |
| NDB_API_READ_ROW_COUNT             | 2              |
| NDB_API_TRANS_LOCAL_READ_ROW_COUNT | 2              |
| NDB_API_EVENT_DATA_COUNT           | 0              |
| NDB_API_EVENT_NONDATA_COUNT        | 0              |
| NDB_API_EVENT_BYTES_COUNT          | 0              |
+------------------------------------+----------------+
21 rows in set (0.09 sec)
```

Not all counters are reflected in all 4 sets of status variables. For the event counters `DataEventsRecvdCount`, `NondataEventsRecvdCount`, and `EventBytesRecvdCount`, only `_injector` and [**mysqld**](mysqld.md) -level NDB API status variables are available:

```sql
mysql> SHOW STATUS LIKE 'ndb_api%event%';
+--------------------------------------+-------+
| Variable_name                        | Value |
+--------------------------------------+-------+
| Ndb_api_event_data_count_injector    | 0     |
| Ndb_api_event_nondata_count_injector | 0     |
| Ndb_api_event_bytes_count_injector   | 0     |
| Ndb_api_event_data_count             | 0     |
| Ndb_api_event_nondata_count          | 0     |
| Ndb_api_event_bytes_count            | 0     |
+--------------------------------------+-------+
6 rows in set (0.00 sec)
```

`_injector` status variables are not implemented for any other NDB API counters, as shown here:

```sql
mysql> SHOW STATUS LIKE 'ndb_api%injector%';
+--------------------------------------+-------+
| Variable_name                        | Value |
+--------------------------------------+-------+
| Ndb_api_event_data_count_injector    | 0     |
| Ndb_api_event_nondata_count_injector | 0     |
| Ndb_api_event_bytes_count_injector   | 0     |
+--------------------------------------+-------+
3 rows in set (0.00 sec)
```

The names of the status variables can easily be associated with the names of the corresponding counters. Each NDB API statistics counter is listed in the following table with a description as well as the names of any MySQL server status variables corresponding to this counter.

**Table 25.39 NDB API statistics counters**

| Counter Name | Description | Status Variables (by statistic type):  - Session - Replica (slave) - Injector - Server |
| --- | --- | --- |
| `WaitExecCompleteCount` | Number of times thread has been blocked while waiting for execution of an operation to complete. Includes all [`execute()`](https://dev.mysql.com/doc/ndbapi/en/ndb-ndbtransaction.html#ndb-ndbtransaction-execute) calls as well as implicit executes for blob operations and auto-increment not visible to clients. | - [`Ndb_api_wait_exec_complete_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_wait_exec_complete_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_wait_exec_complete_count`](mysql-cluster-options-variables.md) |
| `WaitScanResultCount` | Number of times thread has been blocked while waiting for a scan-based signal, such waiting for additional results, or for a scan to close. | - [`Ndb_api_wait_scan_result_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_wait_scan_result_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_wait_scan_result_count`](mysql-cluster-options-variables.md) |
| `WaitMetaRequestCount` | Number of times thread has been blocked waiting for a metadata-based signal; this can occur when waiting for a DDL operation or for an epoch to be started (or ended). | - [`Ndb_api_wait_meta_request_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_wait_meta_request_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_wait_meta_request_count`](mysql-cluster-options-variables.md) |
| `WaitNanosCount` | Total time (in nanoseconds) spent waiting for some type of signal from the data nodes. | - [`Ndb_api_wait_nanos_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_wait_nanos_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_wait_nanos_count`](mysql-cluster-options-variables.md) |
| `BytesSentCount` | Amount of data (in bytes) sent to the data nodes | - [`Ndb_api_bytes_sent_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_bytes_sent_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_bytes_sent_count`](mysql-cluster-options-variables.md) |
| `BytesRecvdCount` | Amount of data (in bytes) received from the data nodes | - [`Ndb_api_bytes_received_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_bytes_received_count_slave`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_bytes_received_count`](mysql-cluster-options-variables.md) |
| `TransStartCount` | Number of transactions started. | - [`Ndb_api_trans_start_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_trans_start_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_trans_start_count`](mysql-cluster-options-variables.md) |
| `TransCommitCount` | Number of transactions committed. | - [`Ndb_api_trans_commit_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_trans_commit_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_trans_commit_count`](mysql-cluster-options-variables.md) |
| `TransAbortCount` | Number of transactions aborted. | - [`Ndb_api_trans_abort_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_trans_abort_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_trans_abort_count`](mysql-cluster-options-variables.md) |
| `TransCloseCount` | Number of transactions aborted. (This value may be greater than the sum of `TransCommitCount` and `TransAbortCount`.) | - [`Ndb_api_trans_close_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_trans_close_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_trans_close_count`](mysql-cluster-options-variables.md) |
| `PkOpCount` | Number of operations based on or using primary keys. This count includes blob-part table operations, implicit unlocking operations, and auto-increment operations, as well as primary key operations normally visible to MySQL clients. | - [`Ndb_api_pk_op_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_pk_op_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_pk_op_count`](mysql-cluster-options-variables.md) |
| `UkOpCount` | Number of operations based on or using unique keys. | - [`Ndb_api_uk_op_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_uk_op_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_uk_op_count`](mysql-cluster-options-variables.md) |
| `TableScanCount` | Number of table scans that have been started. This includes scans of internal tables. | - [`Ndb_api_table_scan_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_table_scan_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_table_scan_count`](mysql-cluster-options-variables.md) |
| `RangeScanCount` | Number of range scans that have been started. | - [`Ndb_api_range_scan_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_range_scan_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_range_scan_count`](mysql-cluster-options-variables.md) |
| `PrunedScanCount` | Number of scans that have been pruned to a single partition. | - [`Ndb_api_pruned_scan_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_pruned_scan_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_pruned_scan_count`](mysql-cluster-options-variables.md) |
| `ScanBatchCount` | Number of batches of rows received. (A batch in this context is a set of scan results from a single fragment.) | - [`Ndb_api_scan_batch_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_scan_batch_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_scan_batch_count`](mysql-cluster-options-variables.md) |
| `ReadRowCount` | Total number of rows that have been read. Includes rows read using primary key, unique key, and scan operations. | - [`Ndb_api_read_row_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_read_row_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_read_row_count`](mysql-cluster-options-variables.md) |
| `TransLocalReadRowCount` | Number of rows read from the data same node on which the transaction was being run. | - [`Ndb_api_trans_local_read_row_count_session`](mysql-cluster-options-variables.md) - [`Ndb_api_trans_local_read_row_count_replica`](mysql-cluster-options-variables.md) - \[none\] - [`Ndb_api_trans_local_read_row_count`](mysql-cluster-options-variables.md) |
| `DataEventsRecvdCount` | Number of row change events received. | - \[none\] - \[none\] - [`Ndb_api_event_data_count_injector`](mysql-cluster-options-variables.md) - [`Ndb_api_event_data_count`](mysql-cluster-options-variables.md) |
| `NondataEventsRecvdCount` | Number of events received, other than row change events. | - \[none\] - \[none\] - [`Ndb_api_event_nondata_count_injector`](mysql-cluster-options-variables.md) - [`Ndb_api_event_nondata_count`](mysql-cluster-options-variables.md) |
| `EventBytesRecvdCount` | Number of bytes of events received. | - \[none\] - \[none\] - [`Ndb_api_event_bytes_count_injector`](mysql-cluster-options-variables.md) - [`Ndb_api_event_bytes_count`](mysql-cluster-options-variables.md) |

To see all counts of committed transactions—that is, all `TransCommitCount` counter status variables—you can filter the results of [`SHOW STATUS`](show-status.md) for the substring `trans_commit_count`, like this:

```sql
mysql> SHOW STATUS LIKE '%trans_commit_count%';
+------------------------------------+-------+
| Variable_name                      | Value |
+------------------------------------+-------+
| Ndb_api_trans_commit_count_session | 1     |
| Ndb_api_trans_commit_count_slave   | 0     |
| Ndb_api_trans_commit_count         | 2     |
+------------------------------------+-------+
3 rows in set (0.00 sec)
```

From this you can determine that 1 transaction has been committed in the current [**mysql**](mysql.md) client session, and 2 transactions have been committed on this [**mysqld**](mysqld.md) since it was last restarted.

You can see how various NDB API counters are incremented by a given SQL statement by comparing the values of the corresponding `_session` status variables immediately before and after performing the statement. In this example, after getting the initial values from [`SHOW       STATUS`](show-status.md), we create in the `test` database an [`NDB`](mysql-cluster.md) table, named `t`, that has a single column:

```sql
mysql> SHOW STATUS LIKE 'ndb_api%session%';
+--------------------------------------------+--------+
| Variable_name                              | Value  |
+--------------------------------------------+--------+
| Ndb_api_wait_exec_complete_count_session   | 2      |
| Ndb_api_wait_scan_result_count_session     | 0      |
| Ndb_api_wait_meta_request_count_session    | 3      |
| Ndb_api_wait_nanos_count_session           | 820705 |
| Ndb_api_bytes_sent_count_session           | 132    |
| Ndb_api_bytes_received_count_session       | 372    |
| Ndb_api_trans_start_count_session          | 1      |
| Ndb_api_trans_commit_count_session         | 1      |
| Ndb_api_trans_abort_count_session          | 0      |
| Ndb_api_trans_close_count_session          | 1      |
| Ndb_api_pk_op_count_session                | 1      |
| Ndb_api_uk_op_count_session                | 0      |
| Ndb_api_table_scan_count_session           | 0      |
| Ndb_api_range_scan_count_session           | 0      |
| Ndb_api_pruned_scan_count_session          | 0      |
| Ndb_api_scan_batch_count_session           | 0      |
| Ndb_api_read_row_count_session             | 1      |
| Ndb_api_trans_local_read_row_count_session | 1      |
+--------------------------------------------+--------+
18 rows in set (0.00 sec)

mysql> USE test;
Database changed
mysql> CREATE TABLE t (c INT) ENGINE NDBCLUSTER;
Query OK, 0 rows affected (0.85 sec)
```

Now you can execute a new [`SHOW       STATUS`](show-status.md) statement and observe the changes, as shown here (with the changed rows highlighted in the output):

```sql
mysql> SHOW STATUS LIKE 'ndb_api%session%';
+--------------------------------------------+-----------+
| Variable_name                              | Value     |
+--------------------------------------------+-----------+
| Ndb_api_wait_exec_complete_count_session   | 8         |
| Ndb_api_wait_scan_result_count_session     | 0         |
| Ndb_api_wait_meta_request_count_session    | 17        |
| Ndb_api_wait_nanos_count_session           | 706871709 |
| Ndb_api_bytes_sent_count_session           | 2376      |
| Ndb_api_bytes_received_count_session       | 3844      |
| Ndb_api_trans_start_count_session          | 4         |
| Ndb_api_trans_commit_count_session         | 4         |
| Ndb_api_trans_abort_count_session          | 0         |
| Ndb_api_trans_close_count_session          | 4         |
| Ndb_api_pk_op_count_session                | 6         |
| Ndb_api_uk_op_count_session                | 0         |
| Ndb_api_table_scan_count_session           | 0         |
| Ndb_api_range_scan_count_session           | 0         |
| Ndb_api_pruned_scan_count_session          | 0         |
| Ndb_api_scan_batch_count_session           | 0         |
| Ndb_api_read_row_count_session             | 2         |
| Ndb_api_trans_local_read_row_count_session | 1         |
+--------------------------------------------+-----------+
18 rows in set (0.00 sec)
```

Similarly, you can see the changes in the NDB API statistics counters caused by inserting a row into `t`: Insert the row, then run the same [`SHOW       STATUS`](show-status.md) statement used in the previous example, as shown here:

```sql
mysql> INSERT INTO t VALUES (100);
Query OK, 1 row affected (0.00 sec)

mysql> SHOW STATUS LIKE 'ndb_api%session%';
+--------------------------------------------+-----------+
| Variable_name                              | Value     |
+--------------------------------------------+-----------+
| Ndb_api_wait_exec_complete_count_session   | 11        |
| Ndb_api_wait_scan_result_count_session     | 6         |
| Ndb_api_wait_meta_request_count_session    | 20        |
| Ndb_api_wait_nanos_count_session           | 707370418 |
| Ndb_api_bytes_sent_count_session           | 2724      |
| Ndb_api_bytes_received_count_session       | 4116      |
| Ndb_api_trans_start_count_session          | 7         |
| Ndb_api_trans_commit_count_session         | 6         |
| Ndb_api_trans_abort_count_session          | 0         |
| Ndb_api_trans_close_count_session          | 7         |
| Ndb_api_pk_op_count_session                | 8         |
| Ndb_api_uk_op_count_session                | 0         |
| Ndb_api_table_scan_count_session           | 1         |
| Ndb_api_range_scan_count_session           | 0         |
| Ndb_api_pruned_scan_count_session          | 0         |
| Ndb_api_scan_batch_count_session           | 0         |
| Ndb_api_read_row_count_session             | 3         |
| Ndb_api_trans_local_read_row_count_session | 2         |
+--------------------------------------------+-----------+
18 rows in set (0.00 sec)
```

We can make a number of observations from these results:

- Although we created `t` with no explicit primary key, 5 primary key operations were performed in doing so (the difference in the “before” and “after” values of [`Ndb_api_pk_op_count_session`](mysql-cluster-options-variables.md), or 6 minus 1). This reflects the creation of the hidden primary key that is a feature of all tables using the [`NDB`](mysql-cluster.md) storage engine.
- By comparing successive values for [`Ndb_api_wait_nanos_count_session`](mysql-cluster-options-variables.md), we can see that the NDB API operations implementing the [`CREATE TABLE`](create-table.md) statement waited much longer (706871709 - 820705 = 706051004 nanoseconds, or approximately 0.7 second) for responses from the data nodes than those executed by the [`INSERT`](insert.md) (707370418 - 706871709 = 498709 ns or roughly.0005 second). The execution times reported for these statements in the [**mysql**](mysql.md) client correlate roughly with these figures.
	On platforms without sufficient (nanosecond) time resolution, small changes in the value of the `WaitNanosCount` NDB API counter due to SQL statements that execute very quickly may not always be visible in the values of [`Ndb_api_wait_nanos_count_session`](mysql-cluster-options-variables.md), [`Ndb_api_wait_nanos_count_replica`](mysql-cluster-options-variables.md), or [`Ndb_api_wait_nanos_count`](mysql-cluster-options-variables.md).
- The [`INSERT`](insert.md) statement incremented both the `ReadRowCount` and `TransLocalReadRowCount` NDB API statistics counters, as reflected by the increased values of [`Ndb_api_read_row_count_session`](mysql-cluster-options-variables.md) and [`Ndb_api_trans_local_read_row_count_session`](mysql-cluster-options-variables.md).