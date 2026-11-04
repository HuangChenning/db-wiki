---
title: "35.4.3 Server Metrics"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/telemetry-metrics-meter-metrics.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 35.4.3 Server Metrics

The following server metrics are registered by default:

The maximum number of metric instruments which can be created is set by [`performance_schema_max_metric_classes`](performance-schema-system-variables.md).

#### mysql.stats Metrics

**Table 35.3 mysql.stats Metrics**

| Name | Source Variable | OTEL Type | Description |
| --- | --- | --- | --- |
| `aborted_clients` | [`Aborted_clients`](server-status-variables.md) | `ASYNC COUNTER` | The number of connections that were aborted because the client died without closing the connection properly |
| `aborted_connects` | [`Aborted_connects`](server-status-variables.md) | `ASYNC COUNTER` | The number of failed attempts to connect to the MySQL server |
| `acl_cache_items_count` | [`Acl_cache_items_count`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of cached privilege objects |
| `binlog_cache.disk_use` | [`Binlog_cache_disk_use`](server-status-variables.md) | `ASYNC COUNTER` | The number of transactions that used the temporary binary log cache but that exceeded the value of binlog\_cache\_size and used a temporary file to store statements from the transaction |
| `binlog_cache.use` | [`Binlog_cache_use`](server-status-variables.md) | `ASYNC COUNTER` | The number of transactions that used the binary log cache. |
| `binlog_stmt_cache_disk_use` | [`Binlog_stmt_cache_disk_use`](server-status-variables.md) | `ASYNC COUNTER` | The number of nontransaction statements that used the binary log statement cache but that exceeded the value of binlog\_stmt\_cache\_size and used a temporary file to store those statements. |
| `binlog_stmt_cache_use` | [`Binlog_stmt_cache_use`](server-status-variables.md) | `ASYNC COUNTER` | The number of nontransactional statements that used the binary log statement cache |
| `bytes_received` | [`Bytes_received`](server-status-variables.md) | `ASYNC COUNTER` | The number of bytes received from all clients |
| `bytes_sent` | [`Bytes_sent`](server-status-variables.md) | `ASYNC COUNTER` | The number of bytes sent to all clients |
| `created.tmp_disk_tables` | [`Created_tmp_disk_tables`](server-status-variables.md) | `ASYNC COUNTER` | The number of internal on-disk temporary tables created by the server while executing statements |
| `created.tmp_files` | [`Created_tmp_files`](server-status-variables.md) | `ASYNC COUNTER` | How many temporary files mysqld has created |
| `created.tmp_tables` | [`Created_tmp_tables`](server-status-variables.md) | `ASYNC COUNTER` | The number of internal temporary tables created by the server while executing statements |
| `error_log.buffered_bytes` | [`Error_log_buffered_bytes`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of bytes currently used in the Performance Schema error\_log table |
| `error_log.buffered_events` | [`Error_log_buffered_events`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of events currently present in the Performance Schema error\_log table |
| `error_log.expired_events` | [`Error_log_expired_events`](server-status-variables.md) | `ASYNC COUNTER` | The number of events discarded from the Performance Schema error\_log table to make room for new events |
| `flush_commands` | [`Flush_commands`](server-status-variables.md) | `ASYNC COUNTER` | The number of times the server flushes tables |
| `global_connection_memory` | [`Global_connection_memory`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The memory used by all user connections to the server |
| `locked_connects` | [`Locked_connects`](server-status-variables.md) | `ASYNC COUNTER` | The number of attempts to connect to locked user accounts |
| `max_execution_time_exceeded` | [`Max_execution_time_exceeded`](server-status-variables.md) | `ASYNC COUNTER` | The number of SELECT statements for which the execution timeout was exceeded |
| `max_execution_time_set` | [`Max_execution_time_set`](server-status-variables.md) | `ASYNC COUNTER` | The number of SELECT statements for which a nonzero execution timeout was set |
| `max_execution_time_set_failed` | [`Max_execution_time_set_failed`](server-status-variables.md) | `ASYNC COUNTER` | The number of `SELECT` statements for which the attempt to set an execution timeout failed |
| `max_used_connections` | [`Max_used_connections`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The maximum number of connections that have been in use simultaneously since the server started |
| `ongoing_anonymous_transaction_count` | [`Ongoing_anonymous_transaction_count`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Shows the number of ongoing transactions which have been marked as anonymous |
| `open_files` | [`Open_files`](server-status-variables.md) | `ASYNC COUNTER` | The number of files that are open. This count includes regular files opened by the server. |
| `open_streams` | [`Open_streams`](server-status-variables.md) | `ASYNC COUNTER` | The number of streams that are open, used mainly for logging |
| `open_table_definitions` | [`Open_table_definitions`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of cached table definitions |
| `open_tables` | [`Open_tables`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of tables that are open. |
| `opened_files` | [`Opened_files`](server-status-variables.md) | `ASYNC COUNTER` | The number of files that have been opened with `my_open()`. |
| `opened_table_definitions` | [`Opened_table_definitions`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of table definitions that have been cached. |
| `opened_tables` | [`Opened_tables`](server-status-variables.md) | `ASYNC COUNTER` | The number of tables that have been opened |
| `prepared_stmt_count` | [`Prepared_stmt_count`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The current number of prepared statements |
| `queries` | [`Queries`](server-status-variables.md) | `ASYNC COUNTER` | The number of statements executed by the server, including ones executed within stored programs. It does not count `COM_PING` or `COM_STATISTICS` commands. |
| `questions` | [`Questions`](server-status-variables.md) | `ASYNC COUNTER` | The number of statements executed by the server. This includes only statements sent to the server by clients and not statements executed within stored programs. |
| `replica_open_temp_tables` | [`Replica_open_temp_tables`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Number of temporary tables that the replication SQL thread currently has open. |
| `secondary_engine_execution_count` | [`Secondary_engine_execution_count`](https://dev.mysql.com/doc/heatwave/en/heatwave-status-variables.html#statvar_Secondary_engine_execution_count) | `ASYNC COUNTER` | The number of queries offloaded to a secondary engine |
| `select_full_join` | [`Select_full_join`](server-status-variables.md) | `ASYNC COUNTER` | The number of joins that perform table scans because they do not use indexes |
| `select_full_range_join` | [`Select_full_range_join`](server-status-variables.md) | `ASYNC COUNTER` | The number of joins that used a range search on a reference table |
| `select_range` | [`Select_range`](server-status-variables.md) | `ASYNC COUNTER` | The number of joins that used ranges on the first table |
| `select_range_check` | [`Select_range_check`](server-status-variables.md) | `ASYNC COUNTER` | The number of joins without keys that check for key usage after each row |
| `select_scan` | [`Select_scan`](server-status-variables.md) | `ASYNC COUNTER` | The number of joins that did a full scan of the first table |
| `slow_launch_threads` | [`Slow_launch_threads`](server-status-variables.md) | `ASYNC COUNTER` | The number of threads that have taken more than slow\_launch\_time seconds to create. |
| `slow_queries` | [`Slow_queries`](server-status-variables.md) | `ASYNC COUNTER` | The number of queries that have taken more than long\_query\_time seconds |
| `sort_merge_passes` | [`Sort_merge_passes`](server-status-variables.md) | `ASYNC COUNTER` | The number of merge passes that the sort algorithm has had to do |
| `sort_range` | [`Sort_range`](server-status-variables.md) | `ASYNC COUNTER` | The number of sorts that were done using ranges |
| `sort_rows` | [`Sort_rows`](server-status-variables.md) | `ASYNC COUNTER` | The number of sorted rows. |
| `sort_scan` | [`Sort_scan`](server-status-variables.md) | `ASYNC COUNTER` | The number of sorts that were done by scanning the table. |
| `table_locks_immediate` | [`Table_locks_immediate`](server-status-variables.md) | `ASYNC COUNTER` | The number of times that a request for a table lock could be granted immediately |
| `table_locks_waited` | [`Table_locks_waited`](server-status-variables.md) | `ASYNC COUNTER` | The number of times that a request for a table lock could not be granted immediately and a wait was needed. |
| `table_open_cache_hits` | [`Table_open_cache_hits`](server-status-variables.md) | `ASYNC COUNTER` | The number of hits for open tables cache lookups. |
| `table_open_cache_misses` | [`Table_open_cache_misses`](server-status-variables.md) | `ASYNC COUNTER` | The number of misses for open tables cache lookups. |
| `table_open_cache_overflows` | [`Table_open_cache_overflows`](server-status-variables.md) | `ASYNC COUNTER` | The number of overflows for the open tables cache. |
| `tc_log_page_waits` | [`Tc_log_page_waits`](server-status-variables.md) | `ASYNC COUNTER` | For the memory-mapped implementation of the recovery log, this variable increments each time the server was not able to commit a transaction and had to wait for a free page in the log. |
| `threads_cached` | [`Threads_cached`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of threads in the thread cache. |
| `threads_connected` | [`Threads_connected`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of currently open connections |
| `threads_created` | [`Threads_created`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of threads created to handle connections. |
| `threads_running` | [`Threads_running`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of threads that are not sleeping. |
| `uptime` | [`Uptime`](server-status-variables.md) | `ASYNC COUNTER` | The number of seconds that the server has been up. |

#### mysql.stats.com Metrics

The `mysql.stats.com` metrics correspond to the ``Com_*`xxx`*`` statement counter variables. See [Section 7.1.10, “Server Status Variables”](server-status-variables.md) and [Com\_xxx](server-status-variables.md) for more information.

The `mysql.stats.com` metrics are named for those variables, without the `Com_` prefix. For example, the `select` metric corresponds to the `Com_select` statement counter variable.

These metrics are of OTEL Type `ASYNC           COUNTER` and record the number of times (INTEGER) the corresponding command statement has been executed.

#### mysql.stats.connection Metrics

The `mysql.stats.connection` metrics correspond to the `Connections` and ``Connection_*`XXX`*`` status variables.

**Table 35.4 mysql.stats.connection Metrics**

| Name | Source Variable | OTEL Type | Description |
| --- | --- | --- | --- |
| `total` | [`Connections`](server-status-variables.md) | `ASYNC COUNTER` | Cumulative count of total connections created. |
| `errors_accept` | [`Connection_errors_accept`](server-status-variables.md) | `ASYNC COUNTER` | The number of errors that occurred during calls to `accept()` on the listening port. |
| `errors_internal` | [`Connection_errors_internal`](server-status-variables.md) | `ASYNC COUNTER` | The number of connections refused due to internal errors in the server, such as failure to start a new thread or an out-of-memory condition. |
| `errors_max_connections` | [`Connection_errors_max_connections`](server-status-variables.md) | `ASYNC COUNTER` | The number of connections refused because the server max\_connections limit was reached. |
| `errors_peer_address` | [`Connection_errors_peer_address`](server-status-variables.md) | `ASYNC COUNTER` | The number of errors that occurred while searching for connecting client IP addresses. |
| `errors_select` | [`Connection_errors_select`](server-status-variables.md) | `ASYNC COUNTER` | The number of errors that occurred during calls to select() or poll() on the listening port. |
| `errors_tcpwrap` | [`Connection_errors_tcpwrap`](server-status-variables.md) | `ASYNC COUNTER` | The number of connections refused by the `libwrap` library. |

#### mysql.perf\_schema Metrics

The `mysql.perf_schema` correspond to the ``Performance_schema_*`XXX`*`` status variables. See [Section 29.7, “Performance Schema Status Monitoring”](performance-schema-status-monitoring.md).

**Table 35.5 mysql.perf\_schema Metrics**

| Name | Source Variable | OTEL Type | Description |
| --- | --- | --- | --- |
| `accounts_lost` | [`Performance_schema_accounts_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of times a row could not be added to the accounts table because it was full. |
| `cond_classes_lost` | [`Performance_schema_cond_classes_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many condition instruments could not be loaded. |
| `cond_instances_lost` | [`Performance_schema_cond_instances_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many condition instrument instances could not be created. |
| `digest_lost` | [`Performance_schema_digest_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of digest instances that could not be instrumented in the [`events_statements_summary_by_digest`](performance-schema-statement-summary-tables.md) table. |
| `file_classes_lost` | [`Performance_schema_file_classes_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many file instruments could not be loaded. |
| `file_handles_lost` | [`Performance_schema_file_handles_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many file instrument instances could not be opened. |
| `file_instances_lost` | [`Performance_schema_file_instances_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many file instrument instances could not be created. |
| `hosts_lost` | [`Performance_schema_hosts_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of times a row could not be added to the hosts table because it was full. |
| `index_stat_lost` | [`Performance_schema_index_stat_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of indexes for which statistics were lost. |
| `locker_lost` | [`Performance_schema_locker_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many events are lost or not recorded. |
| `memory_classes_lost` | [`Performance_schema_memory_classes_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of times a memory instrument could not be loaded. |
| `metadata_lock_lost` | [`Performance_schema_metadata_lock_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of metadata locks that could not be instrumented in the [`metadata_locks`](performance-schema-metadata-locks-table.md) table. |
| `meter_lost` | [`Performance_schema_meter_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many meter instruments could not be loaded. |
| `metric_lost` | [`Performance_schema_metric_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many metric instruments could not be loaded. |
| `mutex_classes_lost` | [`Performance_schema_mutex_classes_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many mutex instruments could not be loaded. |
| `mutex_instances_lost` | [`Performance_schema_mutex_instances_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many mutex instrument instances could not be created. |
| `nested_statement_lost` | [`Performance_schema_nested_statement_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of stored program statements for which statistics were lost. |
| `prepared_statements_lost` | [`Performance_schema_prepared_statements_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of prepared statements that could not be instrumented in the [`prepared_statements_instances`](performance-schema-prepared-statements-instances-table.md) table. |
| `program_lost` | [`Performance_schema_program_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of stored programs for which statistics were lost. |
| `rwlock_classes_lost` | [`Performance_schema_rwlock_classes_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many rwlock instruments could not be loaded. |
| `rwlock_instances_lost` | [`Performance_schema_rwlock_instances_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many rwlock instrument instances could not be created. |
| `session_connect_attrs_longest_seen` | [`Performance_schema_session_connect_attrs_longest_seen`](performance-schema-status-variables.md) | `ASYNC COUNTER` | Longest seen connection attribute received. |
| `session_connect_attrs_lost` | [`Performance_schema_session_connect_attrs_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of connections for which connection attribute truncation has occurred |
| `socket_classes_lost` | [`Performance_schema_socket_classes_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many socket instruments could not be loaded. |
| `socket_instances_lost` | [`Performance_schema_socket_instances_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many socket instrument instances could not be created. |
| `stage_classes_lost` | [`Performance_schema_stage_classes_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many stage instruments could not be loaded. |
| `statement_classes_lost` | [`Performance_schema_statement_classes_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many statement instruments could not be loaded. |
| `table_handles_lost` | [`Performance_schema_table_handles_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many table instrument instances could not be opened. |
| `table_instances_lost` | [`Performance_schema_table_instances_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many table instrument instances could not be created. |
| `table_lock_stat_lost` | [`Performance_schema_table_lock_stat_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of tables for which lock statistics were lost. |
| `thread_classes_lost` | [`Performance_schema_thread_classes_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | How many thread instruments could not be loaded. |
| `thread_instances_lost` | [`Performance_schema_thread_instances_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of thread instances that could not be instrumented in the [`threads`](performance-schema-threads-table.md) table. |
| `users_lost` | [`Performance_schema_users_lost`](performance-schema-status-variables.md) | `ASYNC COUNTER` | The number of times a row could not be added to the [`users`](performance-schema-users-table.md) table because it was full. |

#### mysql.stats.handler Metrics

The `mysql.stats.handler` metrics correspond to the ``Handler_*`XXX`*`` status variables.

**Table 35.6 mysql.perf\_schema Metrics**

| Name | Source Variable | OTEL Type | Description |
| --- | --- | --- | --- |
| `commit` | [`Handler_commit`](server-status-variables.md) | `ASYNC COUNTER` | The number of internal COMMIT statements. |
| `delete` | [`Handler_delete`](server-status-variables.md) | `ASYNC COUNTER` | The number of times that rows have been deleted from tables |
| `discover` | [`Handler_discover`](mysql-cluster-options-variables.md) | `ASYNC COUNTER` | The number of times that tables have been discovered. |
| `external_lock` | [`Handler_external_lock`](server-status-variables.md) | `ASYNC COUNTER` | The server increments this variable for each call to its external\_lock() function, which generally occurs at the beginning and end of access to a table instance. |
| `mrr_init` | [`Handler_mrr_init`](server-status-variables.md) | `ASYNC COUNTER` | The number of times the server uses a storage engine's own Multi-Range Read implementation for table access. |
| `prepare` | [`Handler_prepare`](server-status-variables.md) | `ASYNC COUNTER` | A counter for the prepare phase of two-phase commit operations. |
| `read_first` | [`Handler_read_first`](server-status-variables.md) | `ASYNC COUNTER` | The number of times the first entry in an index was read. |
| `read_key` | [`Handler_read_key`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests to read a row based on a key. |
| `read_last` | [`Handler_read_last`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests to read the last key in an index. |
| `read_next` | [`Handler_read_next`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests to read the next row in key order. |
| `read_prev` | [`Handler_read_prev`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests to read the previous row in key order. |
| `read_rnd` | [`Handler_read_rnd`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests to read a row based on a fixed position. |
| `read_rnd_next` | [`Handler_read_rnd_next`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests to read the next row in the data file. |
| `rollback` | [`Handler_rollback`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests for a storage engine to perform a rollback operation. |
| `savepoint` | [`Handler_savepoint`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests for a storage engine to place a savepoint. |
| `savepoint_rollback` | [`Handler_savepoint_rollback`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests for a storage engine to roll back to a savepoint. |
| `update` | [`Handler_update`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests to update a row in a table. |
| `write` | [`Handler_write`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests to insert a row in a table. |

#### mysql.stats.myisam Metrics

**Table 35.7 mysql.perf\_schema Metrics**

| Name | Source Variable | OTEL Type | Description |
| --- | --- | --- | --- |
| `key_blocks_not_flushed` | [`Key_blocks_not_flushed`](server-status-variables.md) | `ASYNC COUNTER` | The number of key blocks in the MyISAM key cache that have changed but have not yet been flushed to disk. |
| `key_blocks_unused` | [`Key_blocks_unused`](server-status-variables.md) | `ASYNC COUNTER` | The number of unused blocks in the MyISAM key cache. |
| `key_blocks_used` | [`Key_blocks_used`](server-status-variables.md) | `ASYNC COUNTER` | The number of used blocks in the MyISAM key cache. |
| `key_read_requests` | [`Key_read_requests`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests to read a key block from the MyISAM key cache. |
| `key_reads` | [`Key_reads`](server-status-variables.md) | `ASYNC COUNTER` | The number of physical reads of a key block from disk into the MyISAM key cache. |
| `key_write_requests` | [`Key_write_requests`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests to write a key block to the MyISAM key cache. |
| `key_writes` | [`Key_writes`](server-status-variables.md) | `ASYNC COUNTER` | The number of physical writes of a key block from the MyISAM key cache to disk. |

#### mysql.stats.ssl Metrics

**Table 35.8 mysql.stats.ssl Metrics**

| Name | Source Variable | OTEL Type | Description |
| --- | --- | --- | --- |
| `client_connects` | [`Ssl_client_connects`](server-status-variables.md) | `ASYNC COUNTER` | The number of SSL connection attempts to an SSL-enabled replication source server. |
| `connect_renegotiates` | [`Ssl_connect_renegotiates`](server-status-variables.md) | `ASYNC COUNTER` | The number of negotiates needed to establish the connection to an SSL-enabled replication source server. |
| `finished_accepts` | [`Ssl_finished_accepts`](server-status-variables.md) | `ASYNC COUNTER` | The number of successful SSL connections to the server. |
| `finished_connects` | [`Ssl_finished_connects`](server-status-variables.md) | `ASYNC COUNTER` | The number of successful replica connections to an SSL-enabled replication source server. |
| `session_cache_hits` | [`Ssl_session_cache_hits`](server-status-variables.md) | `ASYNC COUNTER` | The number of SSL session cache hits. |
| `session_cache_misses` | [`Ssl_session_cache_misses`](server-status-variables.md) | `ASYNC COUNTER` | The number of SSL session cache misses. |
| `session_cache_overflows` | [`Ssl_session_cache_overflows`](server-status-variables.md) | `ASYNC COUNTER` | The number of SSL session cache overflows. |
| `session_cache_size` | [`Ssl_session_cache_size`](server-status-variables.md) | `ASYNC COUNTER` | The SSL session cache size. |
| `session_cache_timeouts` | [`Ssl_session_cache_timeouts`](server-status-variables.md) | `ASYNC COUNTER` | The number of SSL session cache timeouts. |
| `used_session_cache_entries` | [`Ssl_used_session_cache_entries`](server-status-variables.md) | `ASYNC COUNTER` | How many SSL session cache entries were used. |
| `accept_renegotiates` | [`Ssl_accept_renegotiates`](server-status-variables.md) | `ASYNC COUNTER` | The number of negotiates needed to establish the connection. |
| `accepts` | [`Ssl_accepts`](server-status-variables.md) | `ASYNC COUNTER` | The number of accepted SSL connections. |
| `callback_cache_hits` | [`Ssl_callback_cache_hits`](server-status-variables.md) | `ASYNC COUNTER` | The number of callback cache hits. |

#### mysql.inno Metrics

**Table 35.9 mysql.inno Metrics**

| Name | Source Variable | OTEL Type | Description |
| --- | --- | --- | --- |
| `dblwr_pages_written` | [`Innodb_dblwr_pages_written`](server-status-variables.md) | `ASYNC COUNTER` | Number of pages that have been written for doublewrite operations |
| `dblwr_writes` | [`Innodb_dblwr_writes`](server-status-variables.md) | `ASYNC COUNTER` | Number of doublewrite operations that have been performed |
| `redo_log_logical_size` | [`Innodb_redo_log_logical_size`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | LSN range size in bytes containing in-use redo log data. |
| `redo_log_physical_size` | [`Innodb_redo_log_physical_size`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Disk space in bytes currently consumed by all redo log files on disk, excluding spare redo log files |
| `redo_log_capacity_resized` | [`Innodb_redo_log_capacity_resized`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Redo log capacity in bytes for all redo log files, after the last completed capacity resize operation |
| `log_waits` | [`Innodb_log_waits`](server-status-variables.md) | `ASYNC COUNTER` | Number of log waits due to small log buffer |
| `log_write_requests` | [`Innodb_log_write_requests`](server-status-variables.md) | `ASYNC COUNTER` | Number of log write requests |
| `log_writes` | [`Innodb_log_writes`](server-status-variables.md) | `ASYNC COUNTER` | The number of physical writes to the InnoDB redo log file |
| `os_log_fsyncs` | [`Innodb_os_log_fsyncs`](server-status-variables.md) | `ASYNC COUNTER` | Number of fsync log writes. |
| `os_log_pending_fsyncs` | [`Innodb_os_log_pending_fsyncs`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Number of pending fsync writes. |
| `os_log_pending_writes` | [`Innodb_os_log_pending_writes`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Number of pending log file writes. |
| `os_log_written` | [`Innodb_os_log_written`](server-status-variables.md) | `ASYNC COUNTER` | Bytes of log written. |
| `page_size` | [`Innodb_page_size`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | InnoDB page size in bytes. |
| `pages_created` | [`Innodb_pages_created`](server-status-variables.md) | `ASYNC COUNTER` | Number of pages created |
| `pages_read` | [`Innodb_pages_read`](server-status-variables.md) | `ASYNC COUNTER` | Number of pages read. |
| `pages_written` | [`Innodb_pages_written`](server-status-variables.md) | `ASYNC COUNTER` | Number of pages written. |
| `row_lock_current_waits` | [`Innodb_row_lock_current_waits`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Number of row locks currently being waited for. |
| `row_lock_time` | [`Innodb_row_lock_time`](server-status-variables.md) | `ASYNC COUNTER` | Time spent in acquiring row locks, in milliseconds |
| `row_lock_time_avg` | [`Innodb_row_lock_time_avg`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The average time to acquire a row lock, in milliseconds |
| `row_lock_time_max` | [`Innodb_row_lock_time_max`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The maximum time to acquire a row lock, in milliseconds. |
| `row_lock_waits` | [`Innodb_row_lock_waits`](server-status-variables.md) | `ASYNC COUNTER` | Number of times a row lock had to be waited for. |
| `rows_deleted` | [`Innodb_rows_deleted`](server-status-variables.md) | `ASYNC COUNTER` | The number of rows inserted into InnoDB tables. |
| `rows_read` | [`Innodb_rows_read`](server-status-variables.md) | `ASYNC COUNTER` | The number of rows read from InnoDB tables |
| `rows_updated` | [`Innodb_rows_updated`](server-status-variables.md) | `ASYNC COUNTER` | The number of rows updated in InnoDB tables. |
| `system_rows_deleted` | [`Innodb_system_rows_deleted`](server-status-variables.md) | `ASYNC COUNTER` | Number of rows deleted from InnoDB tables belonging to system-created schemas. |
| `system_rows_inserted` | [`Innodb_system_rows_inserted`](server-status-variables.md) | `ASYNC COUNTER` | Number of rows inserted into InnoDB tables belonging to system-created schemas |
| `system_rows_read` | [`Innodb_system_rows_read`](server-status-variables.md) | `ASYNC COUNTER` | Number of rows read from InnoDB tables belonging to system-created schemas. |
| `system_rows_updated` | [`Innodb_system_rows_updated`](server-status-variables.md) | `ASYNC COUNTER` | Number of rows updated in InnoDB tables belonging to system-created schemas. |
| `num_open_files` | [`Innodb_num_open_files`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Number of files currently open. |
| `truncated_status_writes` | [`Innodb_truncated_status_writes`](server-status-variables.md) | `ASYNC COUNTER` | Number of times output from the [`SHOW                   ENGINE INNODB STATUS`](show-engine.md) statement has been truncated. |
| `undo_tablespaces_total` | [`Innodb_undo_tablespaces_total`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Total number of undo tablespaces. |
| `undo_tablespaces_explicit` | [`Innodb_undo_tablespaces_explicit`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Number of user-created undo tablespaces. |
| `undo_tablespaces_active` | [`Innodb_undo_tablespaces_active`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Number of active undo tablespaces, including implicit and explicit tablespaces |

#### mysql.inno.buffer\_pool Metrics

**Table 35.10 mysql.inno.buffer\_pool Metrics**

| Name | Source Variable | OTEL Type | Description |
| --- | --- | --- | --- |
| `pages_data` | [`Innodb_buffer_pool_pages_data`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Buffer pages containing data. |
| `bytes_data` | [`Innodb_buffer_pool_bytes_data`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Buffer bytes containing data. |
| `pages_dirty` | [`Innodb_buffer_pool_pages_dirty`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Buffer pages currently dirty. |
| `bytes_dirty` | [`Innodb_buffer_pool_bytes_dirty`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Buffer bytes currently dirty |
| `pages_flushed` | [`Innodb_buffer_pool_pages_flushed`](server-status-variables.md) | `ASYNC COUNTER` | The number of requests to flush pages from the InnoDB buffer pool. |
| `pages_free` | [`Innodb_buffer_pool_pages_free`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Buffer pages currently free. |
| `pages_misc` | [`Innodb_buffer_pool_pages_misc`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Buffer pages for misc use such as row locks or the adaptive hash index. |
| `pages_total` | [`Innodb_buffer_pool_pages_total`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Total buffer pool size in pages. |
| `read_ahead_rnd` | [`Innodb_buffer_pool_read_ahead_rnd`](server-status-variables.md) | `ASYNC COUNTER` | The number of 'random' read-aheads initiated by InnoDB. |
| `read_ahead` | [`Innodb_buffer_pool_read_ahead`](server-status-variables.md) | `ASYNC COUNTER` | Number of pages read as read ahead. |
| `read_ahead_evicted` | [`Innodb_buffer_pool_read_ahead_evicted`](server-status-variables.md) | `ASYNC COUNTER` | Read-ahead pages evicted without being accessed. |
| `read_requests` | [`Innodb_buffer_pool_read_requests`](server-status-variables.md) | `ASYNC COUNTER` | Number of logical read requests. |
| `reads` | [`Innodb_buffer_pool_reads`](server-status-variables.md) | `ASYNC COUNTER` | Number of reads directly from disk. |
| `wait_free` | [`Innodb_buffer_pool_wait_free`](server-status-variables.md) | `ASYNC COUNTER` | Number of times waited for free buffer. |
| `write_requests` | [`Innodb_buffer_pool_write_requests`](server-status-variables.md) | `ASYNC COUNTER` | Number of write requests. |

#### mysql.inno.data Metrics

**Table 35.11 mysql.inno.data Metrics**

| Name | Source Variable | OTEL Type | Description |
| --- | --- | --- | --- |
| `fsyncs` | [`Innodb_data_fsyncs`](server-status-variables.md) | `ASYNC COUNTER` | Number of `fsync()` calls. |
| `pending_fsyncs` | [`Innodb_data_pending_fsyncs`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | Number of pending fsync operations. |
| `pending_reads` | [`Innodb_data_pending_reads`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The current number of pending reads |
| `pending_writes` | [`Innodb_data_pending_writes`](server-status-variables.md) | `ASYNC GAUGE COUNTER` | The current number of pending writes. |
| `read` | [`Innodb_data_read`](server-status-variables.md) | `ASYNC COUNTER` | Amount of data read in bytes. |
| `reads` | [`Innodb_data_reads`](server-status-variables.md) | `ASYNC COUNTER` | Number of reads initiated. |
| `writes` | [`Innodb_data_writes`](server-status-variables.md) | `ASYNC COUNTER` | Number of writes initiated. |
| `written` | [`Innodb_data_written`](server-status-variables.md) | `ASYNC COUNTER` | Amount of data written in bytes. |

#### mysql.x Metrics

**Table 35.12 mysql.x Metrics**

| Name | Source Variable | OTEL Type | Description |
| --- | --- | --- | --- |
| `aborted_clients` | [`Mysqlx_aborted_clients`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of clients that were disconnected because of an input or output error. |
| `bytes_received` | [`Mysqlx_bytes_received`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The total number of bytes received through the network, measured before decompression. |
| `bytes_received_compressed_payload` | [`Mysqlx_bytes_received_compressed_payload`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of bytes received as compressed message payloads, measured before decompression. |
| `bytes_received_uncompressed_frame` | [`Mysqlx_bytes_received_uncompressed_frame`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of bytes received as compressed message payloads, measured after decompression. |
| `bytes_sent` | [`Mysqlx_bytes_sent`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The total number of bytes sent through the network. |
| `bytes_sent_compressed_payload` | [`Mysqlx_bytes_sent_compressed_payload`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of bytes sent as compressed message payloads, measured after compression. |
| `bytes_sent_uncompressed_frame` | [`Mysqlx_bytes_sent_uncompressed_frame`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of bytes sent as compressed message payloads, measured before compression. |
| `connection_accept_errors` | [`Mysqlx_connection_accept_errors`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of connections which have caused accept errors. |
| `connection_errors` | [`Mysqlx_connection_errors`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of connections which have caused errors. |
| `connections_accepted` | [`Mysqlx_connections_accepted`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of connections which have been accepted. |
| `connections_closed` | [`Mysqlx_connections_closed`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of connections which have been closed. |
| `connections_rejected` | [`Mysqlx_connections_rejected`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of connections which have been rejected. |
| `crud_create_view` | [`Mysqlx_crud_create_view`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of create view requests received. |
| `crud_delete` | [`Mysqlx_crud_delete`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of delete requests received. |
| `crud_drop_view` | [`Mysqlx_crud_drop_view`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of drop view requests received. |
| `crud_find` | [`Mysqlx_crud_find`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of find requests received. |
| `crud_insert` | [`Mysqlx_crud_insert`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of insert requests received. |
| `crud_modify_view` | [`Mysqlx_crud_modify_view`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of modify view requests received. |
| `crud_update` | [`Mysqlx_crud_update`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of update requests received. |
| `cursor_close` | [`Mysqlx_cursor_close`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of cursor-close messages received. |
| `cursor_fetch` | [`Mysqlx_cursor_fetch`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of cursor-fetch messages received. |
| `cursor_open` | [`Mysqlx_cursor_open`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of cursor-open messages received. |
| `errors_sent` | [`Mysqlx_errors_sent`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of errors sent to clients. |
| `errors_unknown_message_type` | [`Mysqlx_errors_unknown_message_type`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of unknown message types that have been received. |
| `expect_close` | [`Mysqlx_expect_close`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of expectation blocks closed. |
| `expect_open` | [`Mysqlx_expect_open`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of expectation blocks opened. |
| `init_error` | [`Mysqlx_init_error`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of errors during initialisation. |
| `messages_sent` | [`Mysqlx_messages_sent`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The total number of messages of all types sent to clients. |
| `notice_global_sent` | [`Mysqlx_notice_global_sent`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of global notifications sent to clients. |
| `notice_other_sent` | [`Mysqlx_notice_other_sent`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of other types of notices sent back to clients. |
| `notice_warning_sent` | [`Mysqlx_notice_warning_sent`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of warning notices sent back to clients. |
| `notified_by_group_replication` | [`Mysqlx_notified_by_group_replication`](x-plugin-status-variables.md) | `ASYNC COUNTER` | Number of Group Replication notifications sent to clients. |
| `prep_deallocate` | [`Mysqlx_prep_deallocate`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of prepared-statement-deallocate messages received. |
| `prep_execute` | [`Mysqlx_prep_execute`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of prepared-statement-execute messages received. |
| `prep_prepare` | [`Mysqlx_prep_prepare`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of prepared-statement messages received. |
| `rows_sent` | [`Mysqlx_rows_sent`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of rows sent back to clients. |
| `sessions` | [`Mysqlx_sessions`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of sessions that have been opened. |
| `sessions_accepted` | [`Mysqlx_sessions_accepted`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of session attempts which have been accepted. |
| `sessions_closed` | [`Mysqlx_sessions_closed`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of sessions that have been closed. |
| `sessions_fatal_error` | [`Mysqlx_sessions_fatal_error`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of sessions that have closed with a fatal error. |
| `sessions_killed` | [`Mysqlx_sessions_killed`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of sessions which have been killed. |
| `sessions_rejected` | [`Mysqlx_sessions_rejected`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of session attempts which have been rejected. |
| `ssl_accepts` | [`Mysqlx_ssl_accepts`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of accepted SSL connections. |
| `ssl_finished_accepts` | [`Mysqlx_ssl_finished_accepts`](x-plugin-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of successful SSL connections to the server. |
| `worker_threads` | [`Mysqlx_worker_threads`](x-plugin-status-variables.md) | `ASYNC GAUGE COUNTER` | The number of worker threads available. |
| `worker_threads_active` | [`Mysqlx_worker_threads_active`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of worker threads currently used. |

#### mysql.x.stmt Metrics

**Table 35.13 mysql.x.stmt Metrics**

| Name | Source Variable | OTEL Type | Description |
| --- | --- | --- | --- |
| `create_collection` | [`Mysqlx_stmt_create_collection`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of create collection statements received. |
| `create_collection_index` | [`Mysqlx_stmt_create_collection_index`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of create collection index statements received. |
| `disable_notices` | [`Mysqlx_stmt_disable_notices`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of disable notice statements received. |
| `drop_collection` | [`Mysqlx_stmt_drop_collection`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of drop collection statements received. |
| `drop_collection_index` | [`Mysqlx_stmt_drop_collection_index`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of drop collection index statements received. |
| `enable_notices` | [`Mysqlx_stmt_enable_notices`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of enable notice statements received. |
| `ensure_collection` | [`Mysqlx_stmt_ensure_collection`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of ensure collection statements received. |
| `execute_mysqlx` | [`Mysqlx_stmt_execute_mysqlx`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of StmtExecute messages received with namespace set to mysqlx. |
| `execute_sql` | [`Mysqlx_stmt_execute_sql`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of StmtExecute requests received for the SQL namespace. |
| `get_collection_options` | [`Mysqlx_stmt_get_collection_options`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of get collection object statements received. |
| `kill_client` | [`Mysqlx_stmt_kill_client`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of kill client statements received. |
| `list_clients` | [`Mysqlx_stmt_list_clients`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of list client statements received. |
| `list_notices` | [`Mysqlx_stmt_list_notices`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of list notice statements received. |
| `list_objects` | [`Mysqlx_stmt_list_objects`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of list object statements received. |
| `modify_collection_options` | [`Mysqlx_stmt_modify_collection_options`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of modify collection options statements received. |
| `ping` | [`Mysqlx_stmt_ping`](x-plugin-status-variables.md) | `ASYNC COUNTER` | The number of ping statements received. |