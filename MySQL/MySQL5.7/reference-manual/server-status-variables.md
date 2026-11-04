---
title: "5.1.9 Server Status Variables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/server-status-variables.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 5.1.9 Server Status Variables

The MySQL server maintains many status variables that provide information about its operation. You can view these variables and their values by using the `SHOW [GLOBAL | SESSION]       STATUS` statement (see [Section 13.7.5.35, “SHOW STATUS Statement”](show-status.md)). The optional `GLOBAL` keyword aggregates the values over all connections, and `SESSION` shows the values for the current connection.

```
mysql> SHOW GLOBAL STATUS;
+-----------------------------------+------------+
| Variable_name                     | Value      |
+-----------------------------------+------------+
| Aborted_clients                   | 0          |
| Aborted_connects                  | 0          |
| Bytes_received                    | 155372598  |
| Bytes_sent                        | 1176560426 |
...
| Connections                       | 30023      |
| Created_tmp_disk_tables           | 0          |
| Created_tmp_files                 | 3          |
| Created_tmp_tables                | 2          |
...
| Threads_created                   | 217        |
| Threads_running                   | 88         |
| Uptime                            | 1389872    |
+-----------------------------------+------------+
```

Many status variables are reset to 0 by the [`FLUSH STATUS`](flush.md) statement.

This section provides a description of each status variable. For a status variable summary, see [Section 5.1.5, “Server Status Variable Reference”](server-status-variable-reference.md). For information about status variables specific to NDB Cluster, see [Section 21.4.3.9.3, “NDB Cluster Status Variables”](mysql-cluster-options-variables.md).

The status variables have the meanings shown in the following list.

- `Aborted_clients`
	The number of connections that were aborted because the client died without closing the connection properly. See [Section B.3.2.9, “Communication Errors and Aborted Connections”](communication-errors.md).
- `Aborted_connects`
	The number of failed attempts to connect to the MySQL server. See [Section B.3.2.9, “Communication Errors and Aborted Connections”](communication-errors.md).
	For additional connection-related information, check the ``Connection_errors_*`xxx`*`` status variables and the [`host_cache`](performance-schema-host-cache-table.md) table.
	As of MySQL 5.7.3, `Aborted_connects` is not visible in the embedded server because for that server it is not updated and is not meaningful.
- `Binlog_cache_disk_use`
	The number of transactions that used the temporary binary log cache but that exceeded the value of [`binlog_cache_size`](replication-options-binary-log.md) and used a temporary file to store statements from the transaction.
	The number of nontransactional statements that caused the binary log transaction cache to be written to disk is tracked separately in the `Binlog_stmt_cache_disk_use` status variable.
- `Binlog_cache_use`
	The number of transactions that used the binary log cache.
- `Binlog_stmt_cache_disk_use`
	The number of nontransaction statements that used the binary log statement cache but that exceeded the value of [`binlog_stmt_cache_size`](replication-options-binary-log.md) and used a temporary file to store those statements.
- `Binlog_stmt_cache_use`
	The number of nontransactional statements that used the binary log statement cache.
- `Bytes_received`
	The number of bytes received from all clients.
- `Bytes_sent`
	The number of bytes sent to all clients.
- ``Com_*`xxx`*``
	The ``Com_*`xxx`*`` statement counter variables indicate the number of times each *`xxx`* statement has been executed. There is one status variable for each type of statement. For example, `Com_delete` and `Com_update` count [`DELETE`](delete.md) and [`UPDATE`](update.md) statements, respectively. `Com_delete_multi` and `Com_update_multi` are similar but apply to [`DELETE`](delete.md) and [`UPDATE`](update.md) statements that use multiple-table syntax.
	If a query result is returned from query cache, the server increments the `Qcache_hits` status variable, not `Com_select`. See [Section 8.10.3.4, “Query Cache Status and Maintenance”](query-cache-status-and-maintenance.md).
	All ``Com_stmt_*`xxx`*`` variables are increased even if a prepared statement argument is unknown or an error occurred during execution. In other words, their values correspond to the number of requests issued, not to the number of requests successfully completed. For example, because status variables are initialized for each server startup and do not persist across restarts, the `Com_shutdown` variable that tracks [`SHUTDOWN`](shutdown.md) statements normally has a value of zero, but can be nonzero if [`SHUTDOWN`](shutdown.md) statements were executed but failed.
	The ``Com_stmt_*`xxx`*`` status variables are as follows:
	- `Com_stmt_prepare`
	- `Com_stmt_execute`
	- `Com_stmt_fetch`
	- `Com_stmt_send_long_data`
	- `Com_stmt_reset`
	- `Com_stmt_close`
	Those variables stand for prepared statement commands. Their names refer to the ``COM_*`xxx`*`` command set used in the network layer. In other words, their values increase whenever prepared statement API calls such as **mysql\_stmt\_prepare()**, **mysql\_stmt\_execute()**, and so forth are executed. However, `Com_stmt_prepare`, `Com_stmt_execute` and `Com_stmt_close` also increase for [`PREPARE`](prepare.md), [`EXECUTE`](execute.md), or [`DEALLOCATE PREPARE`](deallocate-prepare.md), respectively. Additionally, the values of the older statement counter variables `Com_prepare_sql`, `Com_execute_sql`, and `Com_dealloc_sql` increase for the [`PREPARE`](prepare.md), [`EXECUTE`](execute.md), and [`DEALLOCATE PREPARE`](deallocate-prepare.md) statements. `Com_stmt_fetch` stands for the total number of network round-trips issued when fetching from cursors.
	`Com_stmt_reprepare` indicates the number of times statements were automatically reprepared by the server after metadata changes to tables or views referred to by the statement. A reprepare operation increments `Com_stmt_reprepare`, and also `Com_stmt_prepare`.
	`Com_explain_other` indicates the number of [`EXPLAIN FOR           CONNECTION`](explain.md) statements executed. See [Section 8.8.4, “Obtaining Execution Plan Information for a Named Connection”](explain-for-connection.md).
	`Com_change_repl_filter` indicates the number of [`CHANGE REPLICATION FILTER`](change-replication-filter.md) statements executed.
- `Compression`
	Whether the client connection uses compression in the client/server protocol.
- ``Connection_errors_*`xxx`*``
	These variables provide information about errors that occur during the client connection process. They are global only and represent error counts aggregated across connections from all hosts. These variables track errors not accounted for by the host cache (see [Section 5.1.11.2, “DNS Lookups and the Host Cache”](host-cache.md)), such as errors that are not associated with TCP connections, occur very early in the connection process (even before an IP address is known), or are not specific to any particular IP address (such as out-of-memory conditions).
	As of MySQL 5.7.3, the ``Connection_errors_*`xxx`*`` status variables are not visible in the embedded server because for that server they are not updated and are not meaningful.
	- `Connection_errors_accept`
		The number of errors that occurred during calls to `accept()` on the listening port.
	- `Connection_errors_internal`
		The number of connections refused due to internal errors in the server, such as failure to start a new thread or an out-of-memory condition.
	- `Connection_errors_max_connections`
		The number of connections refused because the server [`max_connections`](server-system-variables.md) limit was reached.
	- `Connection_errors_peer_address`
		The number of errors that occurred while searching for connecting client IP addresses.
	- `Connection_errors_select`
		The number of errors that occurred during calls to `select()` or `poll()` on the listening port. (Failure of this operation does not necessarily means a client connection was rejected.)
	- `Connection_errors_tcpwrap`
		The number of connections refused by the `libwrap` library.
- `Connections`
	The number of connection attempts (successful or not) to the MySQL server.
- `Created_tmp_disk_tables`
	The number of internal on-disk temporary tables created by the server while executing statements.
	You can compare the number of internal on-disk temporary tables created to the total number of internal temporary tables created by comparing `Created_tmp_disk_tables` and `Created_tmp_tables` values.
	See also [Section 8.4.4, “Internal Temporary Table Use in MySQL”](internal-temporary-tables.md).
- `Created_tmp_files`
	How many temporary files [**mysqld**](mysqld.md) has created.
- `Created_tmp_tables`
	The number of internal temporary tables created by the server while executing statements.
	You can compare the number of internal on-disk temporary tables created to the total number of internal temporary tables created by comparing `Created_tmp_disk_tables` and `Created_tmp_tables` values.
	See also [Section 8.4.4, “Internal Temporary Table Use in MySQL”](internal-temporary-tables.md).
	Each invocation of the [`SHOW           STATUS`](show-status.md) statement uses an internal temporary table and increments the global `Created_tmp_tables` value.
- `Delayed_errors`
	This status variable is deprecated (because `DELAYED` inserts are not supported); expect it to be removed in a future release.
- `Delayed_insert_threads`
	This status variable is deprecated (because `DELAYED` inserts are not supported); expect it to be removed in a future release.
- `Delayed_writes`
	This status variable is deprecated (because `DELAYED` inserts are not supported); expect it to be removed in a future release.
- `Flush_commands`
	The number of times the server flushes tables, whether because a user executed a [`FLUSH TABLES`](flush.md) statement or due to internal server operation. It is also incremented by receipt of a `COM_REFRESH` packet. This is in contrast to `Com_flush`, which indicates how many `FLUSH` statements have been executed, whether [`FLUSH           TABLES`](flush.md), [`FLUSH LOGS`](flush.md), and so forth.
- `group_replication_primary_member`
	Shows the primary member's UUID when the group is operating in single-primary mode. If the group is operating in multi-primary mode, shows an empty string.
- `Handler_commit`
	The number of internal [`COMMIT`](commit.md) statements.
- `Handler_delete`
	The number of times that rows have been deleted from tables.
- `Handler_external_lock`
	The server increments this variable for each call to its `external_lock()` function, which generally occurs at the beginning and end of access to a table instance. There might be differences among storage engines. This variable can be used, for example, to discover for a statement that accesses a partitioned table how many partitions were pruned before locking occurred: Check how much the counter increased for the statement, subtract 2 (2 calls for the table itself), then divide by 2 to get the number of partitions locked.
- `Handler_mrr_init`
	The number of times the server uses a storage engine's own Multi-Range Read implementation for table access.
- `Handler_prepare`
	A counter for the prepare phase of two-phase commit operations.
- `Handler_read_first`
	The number of times the first entry in an index was read. If this value is high, it suggests that the server is doing a lot of full index scans (for example, `SELECT col1 FROM           foo`, assuming that `col1` is indexed).
- `Handler_read_key`
	The number of requests to read a row based on a key. If this value is high, it is a good indication that your tables are properly indexed for your queries.
- `Handler_read_last`
	The number of requests to read the last key in an index. With `ORDER BY`, the server issues a first-key request followed by several next-key requests, whereas with `ORDER BY DESC`, the server issues a last-key request followed by several previous-key requests.
- `Handler_read_next`
	The number of requests to read the next row in key order. This value is incremented if you are querying an index column with a range constraint or if you are doing an index scan.
- `Handler_read_prev`
	The number of requests to read the previous row in key order. This read method is mainly used to optimize `ORDER BY           ... DESC`.
- `Handler_read_rnd`
	The number of requests to read a row based on a fixed position. This value is high if you are doing a lot of queries that require sorting of the result. You probably have a lot of queries that require MySQL to scan entire tables or you have joins that do not use keys properly.
- `Handler_read_rnd_next`
	The number of requests to read the next row in the data file. This value is high if you are doing a lot of table scans. Generally this suggests that your tables are not properly indexed or that your queries are not written to take advantage of the indexes you have.
- `Handler_rollback`
	The number of requests for a storage engine to perform a rollback operation.
- `Handler_savepoint`
	The number of requests for a storage engine to place a savepoint.
- `Handler_savepoint_rollback`
	The number of requests for a storage engine to roll back to a savepoint.
- `Handler_update`
	The number of requests to update a row in a table.
- `Handler_write`
	The number of requests to insert a row in a table.
- `Innodb_available_undo_logs`
	Note
	The `Innodb_available_undo_logs` status variable is deprecated as of MySQL 5.7.19; expect it to be removed in a future release.
	The total number of available `InnoDB` [rollback segments](glossary.md). Supplements the [`innodb_rollback_segments`](innodb-parameters.md) system variable, which defines the number of active rollback segments.
	One rollback segment always resides in the system tablespace, and 32 rollback segments are reserved for use by temporary tables and are hosted in the temporary tablespace (`ibtmp1`). See [Section 14.6.7, “Undo Logs”](innodb-undo-logs.md).
	If you initiate a MySQL instance with 32 or fewer rollback segments, `InnoDB` still assigns one rollback segment to the system tablespace and 32 rollback segments to the temporary tablespace. In this case, `Innodb_available_undo_logs` reports 33 available rollback segments even though the instance was initialized with a lesser [`innodb_rollback_segments`](innodb-parameters.md) value.
- `Innodb_buffer_pool_dump_status`
	The progress of an operation to record the [pages](glossary.md) held in the `InnoDB` [buffer pool](glossary.md), triggered by the setting of `innodb_buffer_pool_dump_at_shutdown` or `innodb_buffer_pool_dump_now`.
	For related information and examples, see [Section 14.8.3.6, “Saving and Restoring the Buffer Pool State”](innodb-preload-buffer-pool.md).
- `Innodb_buffer_pool_load_status`
	The progress of an operation to [warm up](glossary.md) the `InnoDB` [buffer pool](glossary.md) by reading in a set of [pages](glossary.md) corresponding to an earlier point in time, triggered by the setting of [`innodb_buffer_pool_load_at_startup`](innodb-parameters.md) or [`innodb_buffer_pool_load_now`](innodb-parameters.md). If the operation introduces too much overhead, you can cancel it by setting [`innodb_buffer_pool_load_abort`](innodb-parameters.md).
	For related information and examples, see [Section 14.8.3.6, “Saving and Restoring the Buffer Pool State”](innodb-preload-buffer-pool.md).
- `Innodb_buffer_pool_bytes_data`
	The total number of bytes in the `InnoDB` [buffer pool](glossary.md) containing data. The number includes both [dirty](glossary.md) and clean pages. For more accurate memory usage calculations than with `Innodb_buffer_pool_pages_data`, when [compressed](glossary.md) tables cause the buffer pool to hold pages of different sizes.
- `Innodb_buffer_pool_pages_data`
	The number of [pages](glossary.md) in the `InnoDB` [buffer pool](glossary.md) containing data. The number includes both [dirty](glossary.md) and clean pages. When using [compressed tables](glossary.md), the reported `Innodb_buffer_pool_pages_data` value may be larger than `Innodb_buffer_pool_pages_total` (Bug #59550).
- `Innodb_buffer_pool_bytes_dirty`
	The total current number of bytes held in [dirty pages](glossary.md) in the `InnoDB` [buffer pool](glossary.md). For more accurate memory usage calculations than with `Innodb_buffer_pool_pages_dirty`, when [compressed](glossary.md) tables cause the buffer pool to hold pages of different sizes.
- `Innodb_buffer_pool_pages_dirty`
	The current number of [dirty pages](glossary.md) in the `InnoDB` [buffer pool](glossary.md).
- `Innodb_buffer_pool_pages_flushed`
	The number of requests to [flush](glossary.md) [pages](glossary.md) from the `InnoDB` [buffer pool](glossary.md).
- `Innodb_buffer_pool_pages_free`
	The number of free [pages](glossary.md) in the `InnoDB` [buffer pool](glossary.md).
- `Innodb_buffer_pool_pages_latched`
	The number of latched [pages](glossary.md) in the `InnoDB` [buffer pool](glossary.md). These are pages currently being read or written, or that cannot be [flushed](glossary.md) or removed for some other reason. Calculation of this variable is expensive, so it is available only when the `UNIV_DEBUG` system is defined at server build time.
- `Innodb_buffer_pool_pages_misc`
	The number of [pages](glossary.md) in the `InnoDB` [buffer pool](glossary.md) that are busy because they have been allocated for administrative overhead, such as [row locks](glossary.md) or the [adaptive hash index](glossary.md). This value can also be calculated as `Innodb_buffer_pool_pages_total` − `Innodb_buffer_pool_pages_free` − `Innodb_buffer_pool_pages_data`. When using [compressed tables](glossary.md), `Innodb_buffer_pool_pages_misc` may report an out-of-bounds value (Bug #59550).
- `Innodb_buffer_pool_pages_total`
	The total size of the `InnoDB` [buffer pool](glossary.md), in [pages](glossary.md). When using [compressed tables](glossary.md), the reported `Innodb_buffer_pool_pages_data` value may be larger than `Innodb_buffer_pool_pages_total` (Bug #59550)
- `Innodb_buffer_pool_read_ahead`
	The number of [pages](glossary.md) read into the `InnoDB` [buffer pool](glossary.md) by the [read-ahead](glossary.md) background thread.
- `Innodb_buffer_pool_read_ahead_evicted`
	The number of [pages](glossary.md) read into the `InnoDB` [buffer pool](glossary.md) by the [read-ahead](glossary.md) background thread that were subsequently [evicted](glossary.md) without having been accessed by queries.
- `Innodb_buffer_pool_read_ahead_rnd`
	The number of “random” read-aheads initiated by `InnoDB`. This happens when a query scans a large portion of a table but in random order.
- `Innodb_buffer_pool_read_requests`
	The number of logical read requests.
- `Innodb_buffer_pool_reads`
	The number of logical reads that `InnoDB` could not satisfy from the [buffer pool](glossary.md), and had to read directly from disk.
- `Innodb_buffer_pool_resize_status`
	The status of an operation to resize the `InnoDB` [buffer pool](glossary.md) dynamically, triggered by setting the [`innodb_buffer_pool_size`](innodb-parameters.md) parameter dynamically. The [`innodb_buffer_pool_size`](innodb-parameters.md) parameter is dynamic, which allows you to resize the buffer pool without restarting the server. See [Configuring InnoDB Buffer Pool Size Online](innodb-buffer-pool-resize.md) for related information.
- `Innodb_buffer_pool_wait_free`
	Normally, writes to the `InnoDB` [buffer pool](glossary.md) happen in the background. When `InnoDB` needs to read or create a [page](glossary.md) and no clean pages are available, `InnoDB` flushes some [dirty pages](glossary.md) first and waits for that operation to finish. This counter counts instances of these waits. If [`innodb_buffer_pool_size`](innodb-parameters.md) has been set properly, this value should be small.
- `Innodb_buffer_pool_write_requests`
	The number of writes done to the `InnoDB` [buffer pool](glossary.md).
- `Innodb_data_fsyncs`
	The number of `fsync()` operations so far. The frequency of `fsync()` calls is influenced by the setting of the [`innodb_flush_method`](innodb-parameters.md) configuration option.
- `Innodb_data_pending_fsyncs`
	The current number of pending `fsync()` operations. The frequency of `fsync()` calls is influenced by the setting of the [`innodb_flush_method`](innodb-parameters.md) configuration option.
- `Innodb_data_pending_reads`
	The current number of pending reads.
- `Innodb_data_pending_writes`
	The current number of pending writes.
- `Innodb_data_read`
	The amount of data read since the server was started (in bytes).
- `Innodb_data_reads`
	The total number of data reads (OS file reads).
- `Innodb_data_writes`
	The total number of data writes.
- `Innodb_data_written`
	The amount of data written so far, in bytes.
- `Innodb_dblwr_pages_written`
	The number of [pages](glossary.md) that have been written to the [doublewrite buffer](glossary.md). See [Section 14.12.1, “InnoDB Disk I/O”](innodb-disk-io.md).
- `Innodb_dblwr_writes`
	The number of doublewrite operations that have been performed. See [Section 14.12.1, “InnoDB Disk I/O”](innodb-disk-io.md).
- `Innodb_have_atomic_builtins`
	Indicates whether the server was built with [atomic instructions](glossary.md).
- `Innodb_log_waits`
	The number of times that the [log buffer](glossary.md) was too small and a [wait](glossary.md) was required for it to be [flushed](glossary.md) before continuing.
- `Innodb_log_write_requests`
	The number of write requests for the `InnoDB` [redo log](glossary.md).
- `Innodb_log_writes`
	The number of physical writes to the `InnoDB` [redo log](glossary.md) file.
- `Innodb_num_open_files`
	The number of files `InnoDB` currently holds open.
- `Innodb_os_log_fsyncs`
	The number of `fsync()` writes done to the `InnoDB` [redo log](glossary.md) files.
- `Innodb_os_log_pending_fsyncs`
	The number of pending `fsync()` operations for the `InnoDB` [redo log](glossary.md) files.
- `Innodb_os_log_pending_writes`
	The number of pending writes to the `InnoDB` [redo log](glossary.md) files.
- `Innodb_os_log_written`
	The number of bytes written to the `InnoDB` [redo log](glossary.md) files.
- `Innodb_page_size`
	`InnoDB` page size (default 16KB). Many values are counted in pages; the page size enables them to be easily converted to bytes.
- `Innodb_pages_created`
	The number of pages created by operations on `InnoDB` tables.
- `Innodb_pages_read`
	The number of pages read from the `InnoDB` buffer pool by operations on `InnoDB` tables.
- `Innodb_pages_written`
	The number of pages written by operations on `InnoDB` tables.
- `Innodb_row_lock_current_waits`
	The number of [row locks](glossary.md) currently being waited for by operations on `InnoDB` tables.
- `Innodb_row_lock_time`
	The total time spent in acquiring [row locks](glossary.md) for `InnoDB` tables, in milliseconds.
- `Innodb_row_lock_time_avg`
	The average time to acquire a [row lock](glossary.md) for `InnoDB` tables, in milliseconds.
- `Innodb_row_lock_time_max`
	The maximum time to acquire a [row lock](glossary.md) for `InnoDB` tables, in milliseconds.
- `Innodb_row_lock_waits`
	The number of times operations on `InnoDB` tables had to wait for a [row lock](glossary.md).
- `Innodb_rows_deleted`
	The number of rows deleted from `InnoDB` tables.
- `Innodb_rows_inserted`
	The number of rows inserted into `InnoDB` tables.
- `Innodb_rows_read`
	The number of rows read from `InnoDB` tables.
- `Innodb_rows_updated`
	The estimated number of rows updated in `InnoDB` tables.
	Note
	This value is not meant to be 100% accurate. For an accurate (but more expensive) result, use [`ROW_COUNT()`](information-functions.md).
- `Innodb_truncated_status_writes`
	The number of times output from the `SHOW ENGINE           INNODB STATUS` statement has been truncated.
- `Key_blocks_not_flushed`
	The number of key blocks in the `MyISAM` key cache that have changed but have not yet been flushed to disk.
- `Key_blocks_unused`
	The number of unused blocks in the `MyISAM` key cache. You can use this value to determine how much of the key cache is in use; see the discussion of [`key_buffer_size`](server-system-variables.md) in [Section 5.1.7, “Server System Variables”](server-system-variables.md).
- `Key_blocks_used`
	The number of used blocks in the `MyISAM` key cache. This value is a high-water mark that indicates the maximum number of blocks that have ever been in use at one time.
- `Key_read_requests`
	The number of requests to read a key block from the `MyISAM` key cache.
- `Key_reads`
	The number of physical reads of a key block from disk into the `MyISAM` key cache. If `Key_reads` is large, then your [`key_buffer_size`](server-system-variables.md) value is probably too small. The cache miss rate can be calculated as `Key_reads` / `Key_read_requests`.
- `Key_write_requests`
	The number of requests to write a key block to the `MyISAM` key cache.
- `Key_writes`
	The number of physical writes of a key block from the `MyISAM` key cache to disk.
- `Last_query_cost`
	The total cost of the last compiled query as computed by the query optimizer. This is useful for comparing the cost of different query plans for the same query. The default value of 0 means that no query has been compiled yet. The default value is 0. `Last_query_cost` has session scope.
	`Last_query_cost` can be computed accurately only for simple, “flat” queries, but not for complex queries such as those containing subqueries or [`UNION`](union.md). For the latter, the value is set to 0.
- `Last_query_partial_plans`
	The number of iterations the query optimizer made in execution plan construction for the previous query.
	`Last_query_partial_plans` has session scope.
- `Locked_connects`
	The number of attempts to connect to locked user accounts. For information about account locking and unlocking, see [Section 6.2.15, “Account Locking”](account-locking.md).
- `Max_execution_time_exceeded`
	The number of [`SELECT`](select.md) statements for which the execution timeout was exceeded.
- `Max_execution_time_set`
	The number of [`SELECT`](select.md) statements for which a nonzero execution timeout was set. This includes statements that include a nonzero [`MAX_EXECUTION_TIME`](optimizer-hints.md) optimizer hint, and statements that include no such hint but execute while the timeout indicated by the [`max_execution_time`](server-system-variables.md) system variable is nonzero.
- `Max_execution_time_set_failed`
	The number of [`SELECT`](select.md) statements for which the attempt to set an execution timeout failed.
- `Max_used_connections`
	The maximum number of connections that have been in use simultaneously since the server started.
- `Max_used_connections_time`
	The time at which `Max_used_connections` reached its current value.
- `Not_flushed_delayed_rows`
	This status variable is deprecated (because `DELAYED` inserts are not supported); expect it to be removed in a future release.
- `mecab_charset`
	The character set currently used by the MeCab full-text parser plugin. For related information, see [Section 12.9.9, “MeCab Full-Text Parser Plugin”](fulltext-search-mecab.md).
- `Ongoing_anonymous_transaction_count`
	Shows the number of ongoing transactions which have been marked as anonymous. This can be used to ensure that no further transactions are waiting to be processed.
- `Ongoing_anonymous_gtid_violating_transaction_count`
	This status variable is only available in debug builds. Shows the number of ongoing transactions which use [`gtid_next=ANONYMOUS`](replication-options-gtids.md) and that violate GTID consistency.
- `Ongoing_automatic_gtid_violating_transaction_count`
	This status variable is only available in debug builds. Shows the number of ongoing transactions which use [`gtid_next=AUTOMATIC`](replication-options-gtids.md) and that violate GTID consistency.
- `Open_files`
	The number of files that are open. This count includes regular files opened by the server. It does not include other types of files such as sockets or pipes. Also, the count does not include files that storage engines open using their own internal functions rather than asking the server level to do so.
- `Open_streams`
	The number of streams that are open (used mainly for logging).
- `Open_table_definitions`
	The number of cached `.frm` files.
- `Open_tables`
	The number of tables that are open.
- `Opened_files`
	The number of files that have been opened with `my_open()` (a `mysys` library function). Parts of the server that open files without using this function do not increment the count.
- `Opened_table_definitions`
	The number of `.frm` files that have been cached.
- `Opened_tables`
	The number of tables that have been opened. If `Opened_tables` is big, your [`table_open_cache`](server-system-variables.md) value is probably too small.
- ``Performance_schema_*`xxx`*``
	Performance Schema status variables are listed in [Section 25.16, “Performance Schema Status Variables”](performance-schema-status-variables.md). These variables provide information about instrumentation that could not be loaded or created due to memory constraints.
- `Prepared_stmt_count`
	The current number of prepared statements. (The maximum number of statements is given by the [`max_prepared_stmt_count`](server-system-variables.md) system variable.)
- `Qcache_free_blocks`
	The number of free memory blocks in the query cache.
	Note
	The query cache is deprecated as of MySQL 5.7.20, and is removed in MySQL 8.0. Deprecation includes `Qcache_free_blocks`.
- `Qcache_free_memory`
	The amount of free memory for the query cache.
	Note
	The query cache is deprecated as of MySQL 5.7.20, and is removed in MySQL 8.0. Deprecation includes `Qcache_free_memory`.
- `Qcache_hits`
	The number of query cache hits.
	The discussion at the beginning of this section indicates how to relate this statement-counting status variable to other such variables.
	Note
	The query cache is deprecated as of MySQL 5.7.20, and is removed in MySQL 8.0. Deprecation includes `Qcache_hits`.
- `Qcache_inserts`
	The number of queries added to the query cache.
	Note
	The query cache is deprecated as of MySQL 5.7.20, and is removed in MySQL 8.0. Deprecation includes `Qcache_inserts`.
- `Qcache_lowmem_prunes`
	The number of queries that were deleted from the query cache because of low memory.
	Note
	The query cache is deprecated as of MySQL 5.7.20, and is removed in MySQL 8.0. Deprecation includes `Qcache_lowmem_prunes`.
- `Qcache_not_cached`
	The number of noncached queries (not cacheable, or not cached due to the [`query_cache_type`](server-system-variables.md) setting).
	Note
	The query cache is deprecated as of MySQL 5.7.20, and is removed in MySQL 8.0. Deprecation includes `Qcache_not_cached`.
- `Qcache_queries_in_cache`
	The number of queries registered in the query cache.
	Note
	The query cache is deprecated as of MySQL 5.7.20, and is removed in MySQL 8.0. Deprecation includes `Qcache_queries_in_cache`.
- `Qcache_total_blocks`
	The total number of blocks in the query cache.
	Note
	The query cache is deprecated as of MySQL 5.7.20, and is removed in MySQL 8.0. Deprecation includes `Qcache_total_blocks`.
- `Queries`
	The number of statements executed by the server. This variable includes statements executed within stored programs, unlike the `Questions` variable. It does not count `COM_PING` or `COM_STATISTICS` commands.
	The discussion at the beginning of this section indicates how to relate this statement-counting status variable to other such variables.
- `Questions`
	The number of statements executed by the server. This includes only statements sent to the server by clients and not statements executed within stored programs, unlike the `Queries` variable. This variable does not count `COM_PING`, `COM_STATISTICS`, `COM_STMT_PREPARE`, `COM_STMT_CLOSE`, or `COM_STMT_RESET` commands.
	The discussion at the beginning of this section indicates how to relate this statement-counting status variable to other such variables.
- `Rpl_semi_sync_master_clients`
	The number of semisynchronous replicas.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_net_avg_wait_time`
	The average time in microseconds the source waited for a replica reply. This variable is deprecated, always `0`; expect it to be in a future version.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_net_wait_time`
	The total time in microseconds the source waited for replica replies. This variable is deprecated, and is always `0`; expect it to be removed in a future version.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_net_waits`
	The total number of times the source waited for replica replies.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_no_times`
	The number of times the source turned off semisynchronous replication.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_no_tx`
	The number of commits that were not acknowledged successfully by a replica.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_status`
	Whether semisynchronous replication currently is operational on the source. The value is `ON` if the plugin has been enabled and a commit acknowledgment has occurred. It is `OFF` if the plugin is not enabled or the source has fallen back to asynchronous replication due to commit acknowledgment timeout.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_timefunc_failures`
	The number of times the source failed when calling time functions such as `gettimeofday()`.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_tx_avg_wait_time`
	The average time in microseconds the source waited for each transaction.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_tx_wait_time`
	The total time in microseconds the source waited for transactions.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_tx_waits`
	The total number of times the source waited for transactions.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_wait_pos_backtraverse`
	The total number of times the source waited for an event with binary coordinates lower than events waited for previously. This can occur when the order in which transactions start waiting for a reply is different from the order in which their binary log events are written.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_wait_sessions`
	The number of sessions currently waiting for replica replies.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_master_yes_tx`
	The number of commits that were acknowledged successfully by a replica.
	This variable is available only if the source-side semisynchronous replication plugin is installed.
- `Rpl_semi_sync_slave_status`
	Whether semisynchronous replication currently is operational on the replica. This is `ON` if the plugin has been enabled and the replica I/O thread is running, `OFF` otherwise.
	This variable is available only if the replica-side semisynchronous replication plugin is installed.
- `Rsa_public_key`
	This variable is available if MySQL was compiled using OpenSSL (see [Section 6.3.4, “SSL Library-Dependent Capabilities”](ssl-libraries.md)). Its value is the public key used by the `sha256_password` authentication plugin for RSA key pair-based password exchange. The value is nonempty only if the server successfully initializes the private and public keys in the files named by the [`sha256_password_private_key_path`](server-system-variables.md) and [`sha256_password_public_key_path`](server-system-variables.md) system variables. The value of `Rsa_public_key` comes from the latter file.
	For information about `sha256_password`, see [Section 6.4.1.5, “SHA-256 Pluggable Authentication”](sha256-pluggable-authentication.md).
- `Select_full_join`
	The number of joins that perform table scans because they do not use indexes. If this value is not 0, you should carefully check the indexes of your tables.
- `Select_full_range_join`
	The number of joins that used a range search on a reference table.
- `Select_range`
	The number of joins that used ranges on the first table. This is normally not a critical issue even if the value is quite large.
- `Select_range_check`
	The number of joins without keys that check for key usage after each row. If this is not 0, you should carefully check the indexes of your tables.
- `Select_scan`
	The number of joins that did a full scan of the first table.
- `Slave_heartbeat_period`
	Shows the replication heartbeat interval (in seconds) on a replication replica.
	This variable is affected by the value of the [`show_compatibility_56`](server-system-variables.md) system variable. For details, see [Effect of show\_compatibility\_56 on Slave Status Variables](server-system-variables.md).
	Note
	This variable only shows the status of the default replication channel. To monitor any replication channel, use the `HEARTBEAT_INTERVAL` column in the [`replication_connection_configuration`](performance-schema-replication-connection-configuration-table.md) table for the replication channel. `Slave_heartbeat_period` is deprecated and is removed in MySQL 8.0.
- `Slave_last_heartbeat`
	Shows when the most recent heartbeat signal was received by a replica, as a [`TIMESTAMP`](datetime.md) value.
	This variable is affected by the value of the [`show_compatibility_56`](server-system-variables.md) system variable. For details, see [Effect of show\_compatibility\_56 on Slave Status Variables](server-system-variables.md).
	Note
	This variable only shows the status of the default replication channel. To monitor any replication channel, use the `LAST_HEARTBEAT_TIMESTAMP` column in the [`replication_connection_status`](performance-schema-replication-connection-status-table.md) table for the replication channel. `Slave_last_heartbeat` is deprecated and is removed in MySQL 8.0.
- `Slave_open_temp_tables`
	The number of temporary tables that the replica SQL thread currently has open. If the value is greater than zero, it is not safe to shut down the replica; see [Section 16.4.1.29, “Replication and Temporary Tables”](replication-features-temptables.md). This variable reports the total count of open temporary tables for *all* replication channels.
- `Slave_received_heartbeats`
	This counter increments with each replication heartbeat received by a replication replica since the last time that the replica was restarted or reset, or a [`CHANGE MASTER TO`](change-master-to.md) statement was issued.
	This variable is affected by the value of the [`show_compatibility_56`](server-system-variables.md) system variable. For details, see [Effect of show\_compatibility\_56 on Slave Status Variables](server-system-variables.md).
	Note
	This variable only shows the status of the default replication channel. To monitor any replication channel, use the `COUNT_RECEIVED_HEARTBEATS` column in the [`replication_connection_status`](performance-schema-replication-connection-status-table.md) table for the replication channel. `Slave_received_heartbeats` is deprecated and is removed in MySQL 8.0.
- `Slave_retried_transactions`
	The total number of times since startup that the replication replica SQL thread has retried transactions.
	This variable is affected by the value of the [`show_compatibility_56`](server-system-variables.md) system variable. For details, see [Effect of show\_compatibility\_56 on Slave Status Variables](server-system-variables.md).
	Note
	This variable only shows the status of the default replication channel. To monitor any replication channel, use the `COUNT_TRANSACTIONS_RETRIES` column in the [`replication_applier_status`](performance-schema-replication-applier-status-table.md) table for the replication channel. `Slave_retried_transactions` is deprecated and is removed in MySQL 8.0.
- `Slave_rows_last_search_algorithm_used`
	The search algorithm that was most recently used by this replica to locate rows for row-based replication. The result shows whether the replica used indexes, a table scan, or hashing as the search algorithm for the last transaction executed on any channel.
	The method used depends on the setting for the [`slave_rows_search_algorithms`](replication-options-replica.md) system variable, and the keys that are available on the relevant table.
	This variable is available only for debug builds of MySQL.
- `Slave_running`
	This is `ON` if this server is a replica that is connected to a replication source, and both the I/O and SQL threads are running; otherwise, it is `OFF`.
	This variable is affected by the value of the [`show_compatibility_56`](server-system-variables.md) system variable. For details, see [Effect of show\_compatibility\_56 on Slave Status Variables](server-system-variables.md).
	Note
	This variable only shows the status of the default replication channel. To monitor any replication channel, use the `SERVICE_STATE` column in the [`replication_applier_status`](performance-schema-replication-applier-status-table.md) or [`replication_connection_status`](performance-schema-replication-connection-status-table.md) tables of the replication channel. `Slave_running` is deprecated and is removed in MySQL 8.0.
- `Slow_launch_threads`
	The number of threads that have taken more than [`slow_launch_time`](server-system-variables.md) seconds to create.
	This variable is not meaningful in the embedded server (`libmysqld`) and as of MySQL 5.7.2 is no longer visible within the embedded server.
- `Slow_queries`
	The number of queries that have taken more than [`long_query_time`](server-system-variables.md) seconds. This counter increments regardless of whether the slow query log is enabled. For information about that log, see [Section 5.4.5, “The Slow Query Log”](slow-query-log.md).
- `Sort_merge_passes`
	The number of merge passes that the sort algorithm has had to do. If this value is large, you should consider increasing the value of the [`sort_buffer_size`](server-system-variables.md) system variable.
- `Sort_range`
	The number of sorts that were done using ranges.
- `Sort_rows`
	The number of sorted rows.
- `Sort_scan`
	The number of sorts that were done by scanning the table.
- `Ssl_accept_renegotiates`
	The number of negotiates needed to establish the connection.
- `Ssl_accepts`
	The number of accepted SSL connections.
- `Ssl_callback_cache_hits`
	The number of callback cache hits.
- `Ssl_cipher`
	The current encryption cipher (empty for unencrypted connections).
- `Ssl_cipher_list`
	The list of possible SSL ciphers (empty for non-SSL connections).
- `Ssl_client_connects`
	The number of SSL connection attempts to an SSL-enabled source.
- `Ssl_connect_renegotiates`
	The number of negotiates needed to establish the connection to an SSL-enabled source.
- `Ssl_ctx_verify_depth`
	The SSL context verification depth (how many certificates in the chain are tested).
- `Ssl_ctx_verify_mode`
	The SSL context verification mode.
- `Ssl_default_timeout`
	The default SSL timeout.
- `Ssl_finished_accepts`
	The number of successful SSL connections to the server.
- `Ssl_finished_connects`
	The number of successful replica connections to an SSL-enabled source.
- `Ssl_server_not_after`
	The last date for which the SSL certificate is valid. To check SSL certificate expiration information, use this statement:
	```
	mysql> SHOW STATUS LIKE 'Ssl_server_not%';
	+-----------------------+--------------------------+
	| Variable_name         | Value                    |
	+-----------------------+--------------------------+
	| Ssl_server_not_after  | Apr 28 14:16:39 2025 GMT |
	| Ssl_server_not_before | May  1 14:16:39 2015 GMT |
	+-----------------------+--------------------------+
	```
- `Ssl_server_not_before`
	The first date for which the SSL certificate is valid.
- `Ssl_session_cache_hits`
	The number of SSL session cache hits.
- `Ssl_session_cache_misses`
	The number of SSL session cache misses.
- `Ssl_session_cache_mode`
	The SSL session cache mode.
- `Ssl_session_cache_overflows`
	The number of SSL session cache overflows.
- `Ssl_session_cache_size`
	The SSL session cache size.
- `Ssl_session_cache_timeouts`
	The number of SSL session cache timeouts.
- `Ssl_sessions_reused`
	This is equal to 0 if TLS was not used in the current MySQL session, or if a TLS session has not been reused; otherwise it is equal to 1.
	`Ssl_sessions_reused` has session scope.
- `Ssl_used_session_cache_entries`
	How many SSL session cache entries were used.
- `Ssl_verify_depth`
	The verification depth for replication SSL connections.
- `Ssl_verify_mode`
	The verification mode used by the server for a connection that uses SSL. The value is a bitmask; bits are defined in the `openssl/ssl.h` header file:
	```
	# define SSL_VERIFY_NONE                 0x00
	# define SSL_VERIFY_PEER                 0x01
	# define SSL_VERIFY_FAIL_IF_NO_PEER_CERT 0x02
	# define SSL_VERIFY_CLIENT_ONCE          0x04
	```
	`SSL_VERIFY_PEER` indicates that the server asks for a client certificate. If the client supplies one, the server performs verification and proceeds only if verification is successful. `SSL_VERIFY_CLIENT_ONCE` indicates that a request for the client certificate is done only in the initial handshake.
- `Ssl_version`
	The SSL protocol version of the connection (for example, TLSv1). If the connection is not encrypted, the value is empty.
- `Table_locks_immediate`
	The number of times that a request for a table lock could be granted immediately.
- `Table_locks_waited`
	The number of times that a request for a table lock could not be granted immediately and a wait was needed. If this is high and you have performance problems, you should first optimize your queries, and then either split your table or tables or use replication.
- `Table_open_cache_hits`
	The number of hits for open tables cache lookups.
- `Table_open_cache_misses`
	The number of misses for open tables cache lookups.
- `Table_open_cache_overflows`
	The number of overflows for the open tables cache. This is the number of times, after a table is opened or closed, a cache instance has an unused entry and the size of the instance is larger than [`table_open_cache`](server-system-variables.md) / [`table_open_cache_instances`](server-system-variables.md).
- `Tc_log_max_pages_used`
	For the memory-mapped implementation of the log that is used by [**mysqld**](mysqld.md) when it acts as the transaction coordinator for recovery of internal XA transactions, this variable indicates the largest number of pages used for the log since the server started. If the product of `Tc_log_max_pages_used` and `Tc_log_page_size` is always significantly less than the log size, the size is larger than necessary and can be reduced. (The size is set by the [`--log-tc-size`](server-options.md) option. This variable is unused: It is unneeded for binary log-based recovery, and the memory-mapped recovery log method is not used unless the number of storage engines that are capable of two-phase commit and that support XA transactions is greater than one. (`InnoDB` is the only applicable engine.)
- `Tc_log_page_size`
	The page size used for the memory-mapped implementation of the XA recovery log. The default value is determined using `getpagesize()`. This variable is unused for the same reasons as described for `Tc_log_max_pages_used`.
- `Tc_log_page_waits`
	For the memory-mapped implementation of the recovery log, this variable increments each time the server was not able to commit a transaction and had to wait for a free page in the log. If this value is large, you might want to increase the log size (with the [`--log-tc-size`](server-options.md) option). For binary log-based recovery, this variable increments each time the binary log cannot be closed because there are two-phase commits in progress. (The close operation waits until all such transactions are finished.)
- `Threads_cached`
	The number of threads in the thread cache.
	This variable is not meaningful in the embedded server (`libmysqld`) and as of MySQL 5.7.2 is no longer visible within the embedded server.
- `Threads_connected`
	The number of currently open connections.
- `Threads_created`
	The number of threads created to handle connections. If `Threads_created` is big, you may want to increase the [`thread_cache_size`](server-system-variables.md) value. The cache miss rate can be calculated as `Threads_created` / `Connections`.
- `Threads_running`
	The number of threads that are not sleeping.
- `Uptime`
	The number of seconds that the server has been up.
- `Uptime_since_flush_status`
	The number of seconds since the most recent `FLUSH           STATUS` statement.