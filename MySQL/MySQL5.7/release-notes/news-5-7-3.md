---
title: "43 Changes in MySQL 5.7.3 (2013-12-03, Milestone 13)"
book: MySQL 5.7 Release Notes
version: "5.7"
source: "https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-3.html"
tags:
  - mysql
  - mysql-5.7
  - release-notes
---

MySQL 5.7 Release Notes

Note

This is a milestone release, for use at your own risk. Upgrades between milestone releases (or from a milestone release to a GA release) are not supported. Significant development changes take place in milestone releases and you may encounter compatibility issues, such as data format changes that require attention in addition to the usual procedure of running **mysql\_upgrade**. For example, you may find it necessary to dump your data with **mysqldump** before the upgrade and reload it afterward. (Making a backup before the upgrade is a prudent precaution in any case.)

### Audit Log Notes

- MySQL 5.7 changed audit log file output to a new format that has better compatibility with Oracle Audit Vault. It is now possible to select either the old or new format using the new [`audit_log_format`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/audit-log-reference.html#sysvar_audit_log_format) system variable, which has permitted values of `OLD` and `NEW` (default `NEW`). For details about each format, see [Audit Log File Formats](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/audit-log-file-formats.html).
	If you change the value of [`audit_log_format`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/audit-log-reference.html#sysvar_audit_log_format), use this procedure to avoid writing log entries in one format to an existing log file that contains entries in a different format:
	1. Stop the server.
	2. Rename the current audit log file manually.
	3. Restart the server with the new value of [`audit_log_format`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/audit-log-reference.html#sysvar_audit_log_format). The audit log plugin will create a new log file, which will contain log entries in the selected format.
	(WL #7076)

### Compilation Notes

- **CMake** configuration for the `Clang` compiler sets more appropriate flags for building on Linux. Specifically, `-g         -fno-omit-frame-pointer -fno-strict-aliasing` is now added. (Bug #17633291)
- Work was done to clean up the source code base, including: Removing unneeded **CMake** checks; removing unused macros from source files; reorganizing header files to reduce the number of dependencies and make them more modular, removing function declarations without definitions, replacing locally written functions with equivalent functions from industry-standard libraries.

### Full-Text Search Notes

- **Important Change; InnoDB:** `InnoDB` now supports external full-text parser plugins. In order to support `InnoDB` full-text parser plugins that are called in boolean mode, a new “ `position` ” member has been added to the `MYSQL_FTPARSER__BOOLEAN_INFO` structure. If you plan to use an existing full-text parser plugin that is called in boolean mode with MySQL 5.7.3 or later, you must add support for the new “ `position` ” member, which is described in [Writing Full-Text Parser Plugins](https://dev.mysql.com/doc/extending-mysql/5.7/en/writing-full-text-plugins.html). Altering a `MyISAM` table with a full-text parser plugin to use `InnoDB` is also supported. For additional information about full-text parser plugins, see [Full-Text Parser Plugins](https://dev.mysql.com/doc/extending-mysql/5.7/en/plugin-types.html#full-text-plugin-type). (WL #6943)

### Optimizer Notes

- The server no longer uses a temporary table for [`UNION`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/union.html) statements that meet certain qualifications. Instead, it retains from temporary table creation only the data structures necessary to perform result column typecasting. The table is not fully instantiated and no rows are written to or read from it; rows are sent directly to the client. The result is reduced memory and disk requirements, and smaller delay before the first row is sent to the client because the server need not wait until the last query block is executed. [`EXPLAIN`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/explain.html) and optimizer trace output will change: The `UNION RESULT` query block will not be present because that block is the part that reads from the temporary table.
	The conditions that qualify a `UNION` for evaluation without a temporary table are:
	- The union is `UNION ALL`, not `UNION` or `UNION             DISTINCT`.
	- There is no global `ORDER BY` clause.
	- The union is not the top-level query block of an `{INSERT | REPLACE} ... SELECT ...` statement.
	(Bug #50674, Bug #11758470, WL #1763)
- The optimizer now is able to apply the range scan access method to queries of this form:
	```
	SELECT ... FROM t1 WHERE ( col_1, col_2 ) IN (( 'a', 'b' ), ( 'c', 'd' ));
	```
	Previously, for range scans to be used it was necessary for the query to be written as:
	```
	SELECT ... FROM t1 WHERE ( col_1 = 'a' AND col_2 = 'b' )
	OR ( col_1 = 'c' AND col_2 = 'd' );
	```
	For the optimizer to use a range scan, queries must satisfy these conditions:
	- Only [`IN()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/comparison-operators.html#operator_in) predicates are used, not [`NOT IN()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/comparison-operators.html#operator_not-in).
	- On the left side of the [`IN()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/comparison-operators.html#operator_in) predicate, the row constructor contains only column references.
	- On the right side of the [`IN()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/comparison-operators.html#operator_in) predicate, row constructors contain only runtime constants, which are either literals or local column references that are bound to constants during execution.
	- On the right side of the [`IN()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/comparison-operators.html#operator_in) predicate, there is more than one row constructor.
	[`EXPLAIN`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/explain.html) output for applicable queries changes from full table scan or index scan to range scan. Changes are also visible by checking the values of the [`Handler_read_first`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-status-variables.html#statvar_Handler_read_first), [`Handler_read_key`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-status-variables.html#statvar_Handler_read_key), and [`Handler_read_next`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-status-variables.html#statvar_Handler_read_next) status variables. (Bug #31188, Bug #11747186, WL #7019)
- The modified `filesort` algorithm now includes an additional optimization designed to enable more tuples to fit into the sort buffer: For additional columns of type `CHAR` or `VARCHAR`, or any nullable fixed-size data type, the values are packed. For example, without packing, a `VARCHAR(255)` column value containing only 3 characters takes 255 characters in the sort buffer. With packing, the value requires only 3 characters plus a two-byte length indicator.
	For data containing packable strings shorter than the maximum column length or many `NULL` values, more records fit into the sort buffer. This improves in-memory sorting of the sort buffer and performance of disk-based merge sorting of the temporary file.
	In edge cases, packing may be disadvantageous: If packable strings are the maximum column length or there are few `NULL` values, the space required for the length indicators reduces the number of records that fit into the sort buffer and sorting is slower in memory and on disk.
	Packing is not applicable if the filesort uses a priority queue for sorting, as is the case when an `ORDER BY ...         LIMIT` optimization is applied (see [LIMIT Query Optimization](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/limit-optimization.html)).
	If a `filesort` is done, optimizer trace output includes a `filesort_summary` block. For example:
	```
	"filesort_summary": {
	  "rows": 100,
	  "examined_rows": 100,
	  "number_of_tmp_files": 0,
	  "sort_buffer_size": 25192,
	  "sort_mode": "<sort_key, packed_additional_fields>"
	}
	```
	The `sort_mode` value provides information about the algorithm used and the contents of the sort buffer:
	```
	<sort_key, rowid>: sort using row pointers
	<sort_key, additional_fields>: sort using additional fields
	<sort_key, packed_additional_fields>: sort using packed additional fields
	```
	For additional information about the `filesort` algorithm, see [ORDER BY Optimization](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/order-by-optimization.html). For information about the optimizer trace, see [MySQL Internals: Tracing the Optimizer](https://dev.mysql.com/doc/internals/en/optimizer-tracing.html). (WL #1509)

### Packaging Notes

- Previously, MySQL Server distributions included the MySQL Reference Manual in Info format (the Docs/mysql.info file). Because the license for the manual restricts redistribution, its inclusion in Community packages caused problems for downstream redistributors, such as those who create Linux distributions. Community distributions of MySQL Server no longer include the mysql.info file, to make the repackaging and redistribution process easier (for example, the source tarball and its checksum can be used directly). This change applies to all source and binary Community packaging formats. Commercial (Enterprise) distributions are unchanged.
	For those who wish to continue using the MySQL Reference Manual in Info format, we have made it available at [https://dev.mysql.com/doc/](https://dev.mysql.com/doc/).

### Performance Schema Notes

- The Performance Schema now instruments transactions. The information collected includes quantitative and qualitative data including transaction duration, transaction counts, and frequency of various transaction attributes such as isolation level and access modes. This information is collected in tables that contain current and recent transaction events, and is aggregated in summary tables across several dimensions, including user, account, and thread (client connection).
	These new tables store transaction events:
	- [`events_transactions_current`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-events-transactions-current-table.html): Current transaction events
	- [`events_transactions_history`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-events-transactions-history-table.html): The most recent transaction events for each thread
	- [`events_transactions_history_long`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-events-transactions-history-long-table.html): The most recent transaction events overall
	There are also summary tables that provide aggregated transaction information.
	Within the event hierarchy, wait events nest within stage events, which nest within statement events, which nest within transactions. To reflect this, the `NESTING_EVENT_TYPE` column, in those tables that have it, permits a new value, `TRANSACTION`, in addition to the existing values `STATEMENT`, `STAGE`, and `WAIT`.
	To permit control over configuration of transaction event collection, these changes were made to Performance Schema setup tables:
	- The [`setup_instruments`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-setup-instruments-table.html) table contains a new instrument named `transaction`. This instrument is disabled by default.
	- The [`setup_consumers`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-setup-consumers-table.html) table contains new consumer values with names corresponding to the current and recent transaction event table names. These consumers may be used to filter collection of transaction events. Only `events_transactions_current` is enabled by default.
	- The [`setup_timers`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-setup-timers-table.html) table contains a new row with a `NAME` value of `transaction` that indicates the unit for transaction event timing. The default unit is `NANOSECOND`.
	For more information, see [Performance Schema Transaction Tables](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-transaction-tables.html), and [Transaction Summary Tables](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-transaction-summary-tables.html).
	If you upgrade to this MySQL release from an earlier version, you must run **mysql\_upgrade** (and restart the server) to incorporate these changes into the `performance_schema` database. (WL #5864)
- The Performance Schema now exposes metadata lock information:
	- Locks that have been granted (shows which sessions own which current metadata locks)
	- Locks that have been requested but not yet granted (shows which sessions are waiting for which metadata locks).
	- Lock requests that have been killed by the deadlock detector or timed out and are waiting for the requesting session's lock request to be discarded
	This information enables you to understand metadata lock dependencies between sessions. You can see not only which lock a session is waiting for, but which session currently holds that lock.
	The Performance Schema now also exposes table lock information that shows which table handles the server has open, how they are locked, and by which sessions.
	These specific changes were implemented:
	- The [`metadata_locks`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-metadata-locks-table.html) and [`table_handles`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-table-handles-table.html) tables list current locks and lock requests for metadata locks and table locks.
	- The [`setup_instruments`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-setup-instruments-table.html) table now has a `wait/lock/metadata/sql/mdl` instrument for metadata locks. This instrument is disabled by default.
	- The [`performance_schema_max_metadata_locks`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-system-variables.html#sysvar_performance_schema_max_metadata_locks) system variable configures the maximum number of metadata locks tracked in the [`metadata_locks`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-metadata-locks-table.html) table. For [`table_handles`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-table-handles-table.html), the size is configured by the existing [`performance_schema_max_table_handles`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-system-variables.html#sysvar_performance_schema_max_table_handles) system variable.
	- The [`Performance_schema_metadata_lock_lost`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-status-variables.html#statvar_Performance_schema_metadata_lock_lost) status variable indicates the number of times a metadata lock could not be recorded. For [`table_handles`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-table-handles-table.html), tables that are opened but cannot be instrumented are counted by the existing [`Performance_schema_table_handles_lost`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-status-variables.html#statvar_Performance_schema_table_handles_lost) status variable.
	For more information, see [Performance Schema Lock Tables](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-lock-tables.html).
	If you upgrade to this MySQL release from an earlier version, you must run **mysql\_upgrade** (and restart the server) to incorporate these changes into the `performance_schema` database. (WL #5879)

### Security Notes

- **Incompatible Change:** Previously, the [`--ssl`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/connection-options.html#option_general_ssl) option has been treated as advisory: When given, an encrypted connection was permitted but not required. Also, several other ``--ssl-*`xxx`*`` options implied `--ssl`. Because of this, the option was usually not used explicitly as `--ssl`, but in its negated form as `--ssl=0`, which prevents use of encryption. This was true on both the client and server sides, and true for any synonyms of `--ssl` (`--ssl=1`, `--enable-ssl`) or `--ssl=0` (`--skip-ssl`, `--disable-ssl`).
	Now the meaning of `--ssl` has changed *on the client-side only*. (There are no secure-connection changes on the server side.)
	When given on the client side as `--ssl` (or a synonym), the option is no longer advisory but prescriptive. Given a server enabled to support encrypted connections, a client program can require an encrypted connection by specifying only the [`--ssl`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/connection-options.html#option_general_ssl) option. (Previously, it was necessary for the client to specify either the [`--ssl-ca`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/connection-options.html#option_general_ssl-ca) option, or all three of the [`--ssl-ca`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/connection-options.html#option_general_ssl-ca), [`--ssl-key`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/connection-options.html#option_general_ssl-key), and [`--ssl-cert`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/connection-options.html#option_general_ssl-cert) options.) The connection attempt fails if an encrypted connection cannot be established. This is an incompatible change in the sense that MySQL client commands that use `--ssl` now will fail unless an encrypted connection can be established. On the other hand, for a successful connection attempt, the connection is guaranteed to be secure. Previously, there was no such guarantee.
	In addition, other ``--ssl-*`xxx`*`` options on the client side no longer imply `--ssl` and are advisory in the absence of [`--ssl`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/connection-options.html#option_general_ssl): The client attempts to connect using encryption but falls back to an unencrypted connection if an encrypted connection cannot be established.
	There is no change in the meaning of `--ssl=0` (and its synonyms) to prevent use of encryption and override other ``--ssl-*`xxx`*`` options.
	A new `MYSQL_OPT_SSL_ENFORCE` option is available for the [`mysql_options()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-options.html) C API function to indicate whether to require the connection to use encryption. If enabled, it has the same effect as specifying `--ssl` on the command line: If an encrypted connection cannot be established, the connection attempt fails.
	For more information, see [Command Options for Encrypted Connections](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/connection-options.html#encrypted-connection-options), and [mysql\_options()](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-options.html).
	The `MASTER_SSL=1` option for the [`CHANGE MASTER TO`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/change-master-to.html) statement has changed as well, analogous to the change in the meaning of `--ssl`. That is, when given, the slave connection to the master must use encryption or the connection attempt fails. (Bug #11744828, WL #6791)

### Functionality Added or Changed

- **Incompatible Change:** Several statement instruments in the [`setup_instruments`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-setup-instruments-table.html) table are used by the Performance Schema during the early stages of statement classification before the exact statement type is known. These instruments were renamed to more clearly reflect their “abstract” nature:
	| Old Instrument Name | New Instrument Name |
	| --- | --- |
	| `statement/com/` | `statement/abstract/new_packet` |
	| `statement/com/Query` | `statement/abstract/Query` |
	| `statement/rpl/relay_log` | `statement/abstract/relay_log` |
	In addition, statistics for abstract instruments are no longer collected in the following tables, because no such instrument is ever used as the final classification for a statement:
	```
	events_statements_summary_by_thread_by_event_name
	events_statements_summary_by_account_by_event_name
	events_statements_summary_by_user_by_event_name
	events_statements_summary_by_host_by_event_name
	events_statements_summary_global_by_event_name
	```
	Applications that refer to the old instrument names must be updated with the new names. For more information about the use of abstract instruments in statement classification, see [Performance Schema Statement Event Tables](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-statement-tables.html). (Bug #16750433, Bug #17271055)
- **Incompatible Change:** The [`EXPLAIN`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/explain.html) statement has been changed so that the effects of the `EXTENDED` and `PARTITIONS` keywords are always enabled. `EXTENDED` and `PARTITIONS` are still recognized, but are superfluous and have been deprecated. They will be removed from [`EXPLAIN`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/explain.html) syntax in a future MySQL release.
	[`EXPLAIN`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/explain.html) output differs as follows as a result of this change:
	- The filtered and partitions columns appear in [`EXPLAIN`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/explain.html) output regardless of whether the `EXTENDED` and `PARTITIONS` keywords are specified. This is an incompatible change for applications that expect to identify column information by position rather than by name, and such applications will need adjustment.
	- [`SHOW WARNINGS`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/show-warnings.html) immediately following `EXPLAIN` shows additional execution plan information regardless of whether the `EXTENDED` keyword is specified. (An additional deprecation warning is included if the statement includes the `EXTENDED` or `PARTITIONS` keyword.)
	(WL #7027)
- **Performance; InnoDB:** The `log_write_up_to` function, which writes to redo log files up to a certain log sequence number (LSN) and optionally flushes writes to disk, has been refactored to improve performance for workloads with heavy `log_sys::mutex` contention and where [`innodb_flush_log_at_trx_commit=2`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/innodb-parameters.html#sysvar_innodb_flush_log_at_trx_commit). (WL #7050)
- **Performance:** The `LOCK_thread_count` mutex protected several independent internal server structures and variables, and was a bottleneck, particularly affecting server performance in the circumstance when many clients were connecting and disconnecting at once. This mutex was decomposed into more specific mutexes and atomic operations to alleviate the bottleneck and improve performance.
	As part of this work, the following status variables are no longer visible in the embedded server because for that server they were not updated and were not meaningful: [`Aborted_connects`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-status-variables.html#statvar_Aborted_connects), [`Connection_errors_accept`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-status-variables.html#statvar_Connection_errors_accept), [`Connection_errors_internal`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-status-variables.html#statvar_Connection_errors_internal), [`Connection_errors_max_connections`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-status-variables.html#statvar_Connection_errors_max_connections), [`Connection_errors_peer_address`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-status-variables.html#statvar_Connection_errors_peer_address), [`Connection_errors_select`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-status-variables.html#statvar_Connection_errors_select), [`Connection_errors_tcpwrap`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-status-variables.html#statvar_Connection_errors_tcpwrap). (WL #7260)
- **InnoDB:** The `InnoDB` **memcached** plugin now supports inserts and reads on mapped `InnoDB` tables that have an `INTEGER` defined as the primary key. (Bug #17315083, Bug #17203937)
- **Replication:** Replication filtering rules can now be set dynamically on the slave using the SQL statement [`CHANGE         REPLICATION FILTER`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/change-replication-filter.html) introduced in this release. This statement has the same effect as starting the slave **mysqld** with one or more of the options [`--replicate-do-db`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-replica.html#option_mysqld_replicate-do-db), [`--replicate-ignore-db`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-replica.html#option_mysqld_replicate-ignore-db), [`--replicate-do-table`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-replica.html#option_mysqld_replicate-do-table), [`--replicate-ignore-table`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-replica.html#option_mysqld_replicate-ignore-table), [`--replicate-wild-do-table`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-replica.html#option_mysqld_replicate-wild-do-table), [`--replicate-wild-ignore-table`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-replica.html#option_mysqld_replicate-wild-ignore-table), and [`--replicate-rewrite-db`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-replica.html#option_mysqld_replicate-rewrite-db).
	For example, issuing the statement `CHANGE REPLICATION         FILTER REPLICATE_DO_TABLE = (d1.t2)` is equivalent to starting the slave **mysqld** with `--replicate-do-table='d1.t2'`.
	[`CHANGE REPLICATION FILTER`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/change-replication-filter.html) differs from the server options in that, to take effect, the statement requires only that the slave SQL thread be stopped beforehand and restarted afterwards, using [`STOP SLAVE         SQL_THREAD`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/stop-slave.html) and [`START SLAVE         SQL_THREAD`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/start-slave.html), respectively.
	This statement leaves any existing replication filtering rules unchanged; to unset all filters of a given type, set the filter to an empty list, as shown in this example:
	```
	CHANGE REPLICATION FILTER REPLICATE_DO_DB = ();
	```
	You can list multiple replication filtering rules in the same statement, separated by commas. When multiple instances of the *same* rule are found, only the last instance is used.
	For more information, see [CHANGE REPLICATION FILTER Statement](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/change-replication-filter.html); see also [How Servers Evaluate Replication Filtering Rules](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-rules.html). (Bug #15877941, Bug #11752237, Bug #67362, Bug #43366, WL #7057)
- **Replication:** Previously, with semisynchronous replication enabled, the master waited for a single slave acknowledgment per transaction before proceeding. A new system variable, [`rpl_semi_sync_master_wait_for_slave_count`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-source.html#sysvar_rpl_semi_sync_master_wait_for_slave_count), enables the number of slave acknowledgments required per transaction to be configured. The minimum (and default) value is 1. The maximum is 65,536. Performance is best for small values of this variable. (WL #7169)
- **Microsoft Windows:** The implementation of condition variables specific to Windows XP and Windows Server 2003 was removed from the source code because MySQL is not supported on those platforms as of MySQL 5.6. (Bug #17332056)
- The Performance Schema now instruments the read/write lock `Delegate::lock`, which is used for the following classes:
	```
	Trans_delegate
	Binlog_storage_delegate
	Binlog_transmit_delegate
	Binlog_relay_IO_delegate
	```
	A different instrument name is used for each subclass, to have distinct statistics for distinct uses. The instruments are visible in the `schema.setup_instruments` table and have these names:
	```
	wait/synch/rwlock/sql/Trans_delegate::lock
	wait/synch/rwlock/sql/Binlog_storage_delegate::lock
	wait/synch/rwlock/sql/Binlog_transmit_delegate::lock
	wait/synch/rwlock/sql/Binlog_relay_IO_delegate::lock
	```
	(Bug #17590161, Bug #70577)
- Some dependencies between client-side plugin header files were removed:
	- The `MYSQL_PLUGIN_EXPORT` macro required by plugin declarations is now declared directly in `mysql/client_plugin.h` instead of getting the definition from `mysql/plugin.h`. That macro was the only thing required by client-side plugins and declared in server-side header `mysql/plugin.h`, so including `mysql/client_plugin.h` in an application no longer requires the application to also include `mysql/plugin.h`.
	- `mysql/plugin_trace.h` no longer uses `C_MODE_START` or `C_MODE_END`. Consequently, including `mysql/plugin_trace.h` in an application no longer requires the application to also include `my_global.h`.
	Applications might require `mysql/plugin.h` or `my_global.h` for other reasons, of course. (Bug #17582168)
- Overhead for Performance Schema instrumentation associated with thread creation was reduced. (Bug #17539520)
- It is now possible to enable the Performance Schema but exclude certain parts of the instrumentation. For example, to enable the Performance Schema but exclude stage and statement instrumentation, do this:
	```
	shell> cmake . -DWITH_PERFSCHEMA_STORAGE_ENGINE=1 \
	        -DDISABLE_PSI_STAGE=1 \
	        -DDISABLE_PSI_STATEMENT=1
	```
	For more information, see the descriptions of the ``DISABLE_PSI_*`XXX`*`` **CMake** options in [MySQL Source-Configuration Options](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/source-configuration-options.html). (Bug #17478068)
- A new **CMake** option, [`WITH_ASAN`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/source-configuration-options.html#option_cmake_with_asan), permits enabling AddressSanitizer for compilers that support it. (Bug #17435338)
- Several compilation warnings were fixed that occurred when compiling without debugging enabled. (Bug #17332094)
- A new [`ER_ENGINE_OUT_OF_MEMORY`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_engine_out_of_memory) error code is available for use by storage engines to report out-of-memory conditions. (Bug #16807964)
- Overhead for deprecation warnings was reduced. (Bug #70402, Bug #17497869)
- For [`GRANT`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/grant.html) statements, [`ER_SP_DOES_NOT_EXIST`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_sp_does_not_exist) errors for nonexistent stored procedures and functions now specify `PROCEDURE does not exist` or `FUNCTION         does not exist` rather than the less-specific `PROCEDURE or FUNCTION does not exist`. (Bug #69628, Bug #17036976)
- The hash function used for metadata locking was modified to reduce overhead. (Bug #68487, Bug #16396598)
- Because there are new API functions ([`mysql_get_option()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-get-option.html), [`mysql_reset_connection()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-reset-connection.html)), the library ABI version is now 18.2. Shared library names now include 18.2 where appropriate.
- A new [`mysql_get_option()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-get-option.html) C API function is available that returns the current value of applicable `mysql_options()` options. See [mysql\_get\_option()](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-get-option.html). (WL #6791)
- When a connection is returned to the thread pool plugin, the connection thread context must be cleaned up. Previously, this was done using `COM_CHANGE_USER` (which is like the [`mysql_change_user()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-change-user.html) C API function). However, that operation reauthenticates, which is unnecessary network roundtrip overhead in this context.
	Now it is possible for client connection state to be reset in a more lightweight manner without causing reauthentication. The API is exposed publicly through these changes:
	- A new `COM_RESET_CONNECTION` protocol command (defined in `mysql_com.h`)
	- A new [`mysql_reset_connection()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-reset-connection.html) C API function
	- A new `resetconnection` command for the **mysql** client
	Resetting a connection has effects similar to [`mysql_change_user()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-change-user.html) or an auto-reconnect except that the connection is not closed and reopened, and reauthentication is not done. See [mysql\_change\_user()](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-change-user.html)) and see [Automatic Reconnection Control](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/c-api-auto-reconnect.html)).
	For more information, see [mysql\_reset\_connection()](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-reset-connection.html) and [mysql — The MySQL Command-Line Client](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysql.html). (WL #6797)

### Bugs Fixed

- **Incompatible Change:** For logging to the `general_log` and `slow_log` tables in the `mysql` database, log lines containing multiple character sets were not always handled correctly. The `general_log.argument` and `slow_log.sql_text` columns now have been changed from [`MEDIUMTEXT`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/blob.html) to [`MEDIUMBLOB`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/blob.html). Consequently, no character set transformation is done for logging to tables now, which aligns it with logging to files.
	If you upgrade to this MySQL release from an earlier version, you must run **mysql\_upgrade** (and restart the server) to incorporate these changes into the `mysql` system database. (Bug #14575847)
- **Important Change; Replication:** `START SLAVE UNTIL SQL_AFTER_GTIDS` did not cause the slave to stop until the next GTID event was received following execution of the transaction having the indicated GTID, which could cause issues in the case when the next GTID event is delayed, or does not exist. Now the slave stops after completing the transaction with that GTID. (Bug #14767986)
- **Important Change; Replication:** It was possible to start the server with binary logging enabled but no server ID specified; in such cases, the server would set [`server_id`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options.html#sysvar_server_id) to 1 (rather than 0) while slaves remained unable to connect.
	Now [`server_id`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options.html#sysvar_server_id) must be set when starting the server with binary logging enabled, otherwise the server is unable to start. If [`--server-id=0`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options.html#sysvar_server_id) is used, this value is no longer changed by the server; in this case, updates are written to the binary log, but slaves are unable to connect. Using [`--server-id`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options.html#sysvar_server_id) without specifying a value has the same effect as setting it explicitly to 0. (Bug #11763963, Bug #56739)
- **InnoDB; Replication:** The `InnoDB` **mecached** plugin would update a record before inserting to the binary log, which would cause slave server replication to stop. The insert should occur before the update. (Bug #17358875)
- **InnoDB:** When new indexes are added by an [`ALTER         TABLE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/alter-table.html) operation, instead of only saving table-level statistics and statistics for the new indexes, `InnoDB` would save statistics for the entire table, including the table's other indexes. This behavior slowed [`ALTER TABLE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/alter-table.html) performance. (Bug #17848838, Bug #16511145)
- **InnoDB:** A regression introduced by the fix for Bug#17371537 resulted a memory leak for **memcached** insert operations. (Bug #17738935)
	References: See also: Bug #17371537.
- **InnoDB:** Fault-tolerant code found in the log apply code for `InnoDB` [`ALTER TABLE ... IN         PLACE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/alter-table.html) could result in data corruption. (Bug #17625063, Bug #17512497)
- **InnoDB:** The `trx->error_key_num` field was not initialized in the error injection code found in `storage/innobase/handler/handler0alter.cc`. The `error_key_num` field is usually 0 but can be a non zero value if the memory buffer of a DDL transaction object is reused. (Bug #17624926)
- **InnoDB:** Databases names beginning with a digit would cause a full-text search (FTS) parser error. (Bug #17607956)
	References: See also: Bug #17161372.
- **InnoDB:** An [`ALTER TABLE ...         CHANGE [COLUMN]`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/alter-table.html) operation would result in an `rbt_empty(index_cache->words)` assertion. (Bug #17536995)
- **InnoDB:** `buf_flush_event` would be created at flush thread startup instead of server startup. Also, `buf_flush_event` would be signaled when `InnoDB` is started in read-only mode. (Bug #17516062)
- **InnoDB:** [`CHECK TABLE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/check-table.html) would ignore the `QUICK` option. (Bug #17513737)
- **InnoDB:** An excessive amount of memory would be consumed when querying [`INFORMATION_SCHEMA.INNODB_FT_INDEX_TABLE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/information-schema-innodb-ft-index-table-table.html). The problem would occur for very large full-text search indexes. (Bug #17483582, Bug #70329)
- **InnoDB:** Running [`SHOW ENGINE         INNODB STATUS`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/show-engine.html) on one connection thread and killing that thread by running a [`KILL CONNECTION`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/kill.html) statement from a different connection thread would result in a severe error. (Bug #17474166)
- **InnoDB:** In debug builds, test case failures would occur due to `ibuf_contract_ext` performing merges and `dict_stats_update` returning evicted pages back into the buffer pool while `ibuf_change_buffering_debug` is enabled. (Bug #17446090)
- **InnoDB:** `InnoDB` failed to return an error when attempting to run a query after discarding the tablespace. (Bug #17431533)
- **InnoDB:** A severe error would occur after discarding a tablespace. (Bug #17430207)
- **InnoDB:** Data in the `OPERATION` column of `performance_schema.events_waits_current` table was incorrect due to a code regression introduced in MySQL 5.7.2. (Bug #17429480)
- **InnoDB:** During a [`TRUNCATE TABLE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/truncate-table.html) operation, InnoDB: Trying to TRUNCATE a missing index of table... warnings would be printed to the error log. These warnings should not be printed when the index is a full-text search (FTS) index. (Bug #17402002, Bug #70226)
	References: See also: Bug #12429565.
- **InnoDB:** During parallel full-text search (FTS) index creation, a scanner thread reads in documents and passes them to the tokenizer. The tokenizer frees documents from memory when tokenization is complete. When tokenizing documents with a large amount of text, the tokenizer thread would not keep pace with the scanner thread. As a result, memory would not be freed fast enough and the “tokenization pending list” would grow in size. (Bug #17384979)
- **InnoDB:** `row_scan_index_for_mysql` would allocate a buffer size of `UNIV_PAGE_SIZE` for `row_search_for_mysql`. When the record length was greater than `UNIV_PAGE_SIZE`, a Valgrind error would occur. (Bug #17378106)
- **InnoDB:** `trx_create` and `trx_free` would be called for every **memcached** `get` request. (Bug #17371537, Bug #70172)
- **InnoDB:** A full-text search (FTS) `BOOLEAN MODE` query with an invalid character in the query string could result in a memory access violation failure. (Bug #17350055)
- **InnoDB:** An assertion would be raised when the database initialization thread encountered other threads performing buffer pool flushing. (Bug #17349975)
- **InnoDB:** Full-text index creation on a large table failed due to insufficient temporary table space and result in a misleading “incorrect key file” error. (Bug #17339606)
- **InnoDB:** The `UNIV_BLOB_DEBUG` compile-time debug flag, which is not often used and is limited by its inability to work across crash recovery, has been removed in order to simplify code refactoring. (Bug #17338452)
- **InnoDB:** The `UNIV_SEARCH_DEBUG` compile-time debug check, which has never reported a failure, has been removed along with all references to it. (Bug #17338432)
- **InnoDB:** `trx_sys_t::ro_trx_list` has been removed. Adding and removing transactions from the `ro_trx_list` can be costly, and placing transactions on the list by default is no longer necessary after mutex related optimizations implemented in MySQL 5.7.2. User transactions are still placed on the `trx_t::mysql_trx_list`. Currently, background read-only transactions are not placed on any list. (Bug #17332300)
- **InnoDB:** When [`innodb_file_per_table`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/innodb-parameters.html#sysvar_innodb_file_per_table) is set to `OFF`, replication failed with error code 1880 when truncating tables. For tables that reside in the shared tablespace, the truncate log file name used during the truncate action was not unique. The error is due to a MySQL 5.7.2 code regression related to Bug #14174004. (Bug #17327409)
- **InnoDB:** When `InnoDB` is retrieving rows and a [`KILL QUERY`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/kill.html) statement is issued, `InnoDB` would return false errors. (Bug #16950658)
- **InnoDB:** In `btr_validate_level` there are checks to ensure that all B-tree pages are marked when allocated. The checks failed on the change buffer because the allocation of change buffer pages is handled differently than other B-tree pages. (Bug #16884217)
- **InnoDB:** The hardcoded size for the `srv_max_n_threads` variable was insufficient. The variable setting is now configured based on the maximum number of connection threads and `InnoDB` background threads. (Bug #16884077)
- **InnoDB:** InnoDB would set `UNIV_WORD_SIZE` to 4 for both Windows 32-bit and 64-bit systems. With this patch, `UNIV_WORD_SIZE` is set to 8 on 64-bit Windows systems. This patch also removes `UNIV_WORD_ALIGNMENT`, which is no longer used. (Bug #16774645)
- **InnoDB:** A `SELECT COUNT(*)` query would take a long time to complete when run concurrently with a [`LOAD DATA`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/load-data.html) operation. The `mtr_memo_contains` function, which determines if an object is part of a memo in a mini transaction, contained a nested loop that caused the query to run slowly. (Bug #16764240, Bug #69141)
- **InnoDB:** When the change buffer is enabled, `InnoDB` failed to write a transaction log record when merging a record from the insert buffer to a secondary index page if the insert was performed as an “update-in-place”. (Bug #16752251, Bug #69122)
- **InnoDB:** Due to a regression in MySQL 5.6, creating or dropping tables with [`innodb_force_recovery`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/innodb-parameters.html#sysvar_innodb_force_recovery) set to `3` (`SRV_FORCE_NO_TRX_UNDO`) failed. Additionally, this bug fix includes a code modification that sets `InnoDB` to read-only when [`innodb_force_recovery`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/innodb-parameters.html#sysvar_innodb_force_recovery) is set to a value greater than `3` (`SRV_FORCE_NO_TRX_UNDO`). (Bug #16631778, Bug #69892)
- **InnoDB:** An `InnoDB` **memcached** configuration error message contained an incorrect file name. The error message stated, Please create config table containers in database innodb\_memcache by running innodb\_config.sql. error 31. The correct file name is `innodb_memcached_config.sql`. Also, the “error 31” portion of the error message has been translated to its text equivalent, which is “Table not found”. (Bug #16498810, Bug #68684)
- **InnoDB:** In `mutex_spin_wait()`, the `sync_array_reserve_cell` function could fail to find an empty slot on systems with sync wait arrays that are small in size, resulting in an error. (Bug #16245498)
- **InnoDB:** When `index_read_map` is called for an exact search and fails to return a record due to non-matching search criteria, the cursor would be positioned on the next record after the searched key. A subsequent call to `index_next         ` would return the next record instead of returning the previous non-matching row, thereby skipping a record. (Bug #14621190, Bug #15965874, Bug #17314241, Bug #70038, Bug #17413093, Bug #12860669, Bug #60220, Bug #17565888)
- **InnoDB:** An implicit rollback caused the server to halt when restarting with an [`innodb_force_recovery`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/innodb-parameters.html#sysvar_innodb_force_recovery) value of 3 or greater. This bug was addressed by the combination of fixes for Bug #16310467 and Bug #17253499. (Bug #14178835)
	References: See also: Bug #16310467, Bug #17253499.
- **InnoDB:** An infinite loop could occur in `buf_page_get_gen` when handling compressed-only pages. (Bug #12560151, Bug #61132)
- **InnoDB:** `InnoDB` would attempt to free [`BLOB`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/blob.html) pages already marked as free. (Bug #11762662, Bug #55284)
- **InnoDB:** Converting a table with a large number of columns from [`MyISAM`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/myisam-storage-engine.html) to [`InnoDB`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/innodb-storage-engine.html) would cause an assertion due to insufficient log buffer space. Instead of asserting, `InnoDB` now attempts to increase log buffer size automatically if the redo log size is too large. (Bug #11758196, Bug #50366)
- **Partitioning:** The storage engine was set incorrectly during a rebuild of a partition; the table storage engine was ignored and the default storage engine used instead. Thus, in MySQL 5.1, it was possible for `REBUILD PARTITION` to change the partition storage engine from [`InnoDB`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/innodb-storage-engine.html) to [`MyISAM`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/myisam-storage-engine.html), and for the reverse (rebuilding partitions of `MyISAM` tables causing the partitions to use `InnoDB`) to occurin MySQL 5.5 and later. Now, when rebuilding partitions, the storage engine actually used by the table is checked and used by the handler for the rebuild operation, so that the partition storage engine is not inadvertently changed. (Bug #17559867)
- **Partitioning:** Index condition pushdown did not work with partitioned tables. (Bug #17306882, Bug #70001)
- **Partitioning:** After disabling the parent table's indexes with [`ALTER TABLE ...         DISABLE KEYS`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/alter-table.html), rebuilding any of its partitions enabled the indexes on those partitions, leading [`MyISAM`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/myisam-storage-engine.html) to fail with an error when the optimizer tried to use one of the affected indexes.
	Now in such cases, we check for disabled indexes on the table before rebuilding any of its partitions. If the indexes have been disabled, then we disable them on the partition following the rebuild. (Bug #16051817)
- **Replication:** When GTID-based replication was used with an intra-schema multithreaded slave, transactions were assigned to the first worker thread only. (Bug #17590616, Bug #70536)
- **Replication:** The `WORKER_ID` column of the `replication_execute_status_by_worker` table did not use the internal `id` column values from the `mysql.slave_worker_info` table, as expected. (Bug #17514406, Bug #70426)
- **Replication:** The `THREAD_ID` column values shown in the `performance_schema.replication_execute_status_by_worker` table used the same thread IDs shown in the output from [`SHOW PROCESSLIST`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/show-processlist.html), rather than those used by other `performance_schema` tables. (Bug #17440991, Bug #70423)
	References: See also: Bug #17473308, Bug #17526982.
- **Replication:** The final argument in the `SET` clause of a [`LOAD DATA ...         SET`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/load-data.html) statement was repeated in the binary log. (Bug #17429677, Bug #70277)
- **Replication:** When an error encountered by the dump thread while reading events from the active binary log file was a temporary error, so that the dump thread tried to read the event, it was possible for the dump thread to seek the wrong position, which could cause one or more events to be resent. To prevent this, the thread's position is obtained after each correct read of an event.
	In addition, with this fix, only binary logs that are not closed normally are marked as possibly being corrupted.
	Finally, two warnings are added; these are now returned when a dump thread encounters a temporary error. (Bug #17402313)
- **Replication:** Setting [`rpl_semi_sync_master_enabled`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-source.html#sysvar_rpl_semi_sync_master_enabled) while the master was waiting for a reply from the slave could in some cases cause the master to fail. (Bug #17327454, Bug #70045)
- **Replication:** When stopping the I/O thread, it was possible with a very large transaction (equivalent to a binary log size greater than 100MB) that the thread did not receive the transaction to the end. When reconnecting with `MASTER_AUTO_POSITION=1` it then tried to fetch changes from the next transaction, which could lead to loss of the incomplete transaction and its data. (Bug #17280176, Bug #69943)
- **Replication:** Trying to set [`CHANGE MASTER         TO ... MASTER_AUTO_POSITION = 0`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/change-master-to.html) failed with error 1777 ([`ER_AUTO_POSITION_REQUIRES_GTID_MODE_ON`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_auto_position_requires_gtid_mode_on)). (Bug #17277744)
- **Replication:** No error was written to the log file when writing an incident event to the binary log. This meant that the user was not alerted that a slave server will later be stopped by the incident event. To prevent this from happening, error messages are now written in the log file for all incidents written to the binary log. (Bug #17258782)
- **Replication:** The value of [`LAST_INSERT_ID()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/information-functions.html#function_last-insert-id) was not correctly replicated when filtering rules were used on the slave. (Bug #17234370, Bug #69861)
- **Replication:** [`RESET SLAVE         ALL`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/reset-slave.html) reset only the host, port, user, password, and log positions. Now it resets all connection parameters. (Bug #17185647)
- **Replication:** An internal function used for storing GTID values could sometimes try to handle them as strings of the wrong length. (Bug #17032712, Bug #69618)
- **Replication:** During row-based replication with [`binlog_row_image`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-binary-log.html#sysvar_binlog_row_image) set to `MINIMAL`, updating only some columns of a table having 9 or more columns caused **mysqlbinlog** to fail when it was used with the [`--verbose`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysqlbinlog.html#option_mysqlbinlog_verbose) option. (Bug #16960133)
- **Replication:** When a master with semisynchronous replication enabled was shut down, the master failed to wait for either a semisyncnronous `ACK` or timeout before completing the shutdown. This prevented semisynchronous replication from reverting to asynchronous replication and allowed open transactions to complete on the master, which resulted in missing events on the slave.
	To fix this problem, dump threads are now stopped last during shutdown, after the client is told to stop, so that, if the dump thread has pending events from active clients, they can be sent to the slave. (Bug #16775543)
- **Replication:** Issuing a [`GRANT`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/grant.html) statement with invalid parameters caused the master to write `LOST_EVENTS` events into its binary logs, causing replication to stop. Now such cases, if one or more grants or revocations of privileges are successful, an incident is written to the log; otherwise, only a warning is logged. (Bug #16629195, Bug #68892)
- **Replication:** [`START SLAVE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/start-slave.html) failed when the server was started with [`master_info_repository=TABLE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-replica.html#sysvar_master_info_repository) and [`relay_log_info_repository=TABLE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-replica.html#sysvar_relay_log_info_repository) and with [`autocommit=0`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-system-variables.html#sysvar_autocommit), together with [`--skip-slave-start`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-replica.html#option_mysqld_skip-slave-start).
	A workaround for previous versions of MySQL is to restart the slave **mysqld** without the `--skip-slave-start` option. (Bug #16533802)
- **Replication:** A number of unneeded initializations of objects that were used but not actually needed for reading the relay log info log were removed. (Bug #16291602)
- **Replication:** **mysqlbinlog** now supports the same command-line options relating to SSL as **mysql**, **mysqladmin**, and other MySQL client programs. See [Command Options for Encrypted Connections](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/connection-options.html#encrypted-connection-options), for more information. (Bug #11751199, Bug #41975)
- **Replication:** Previous versions of **mysqlbinlog** did not correctly accept the `ssl-ca` option in an option file. This fix ensures that this option can be correctly used. In earlier versions a work around is to use the `loose-ssl-ca` option. (Bug #74864, Bug #20032654)
- For debug builds, an error occurring during [`DELETE IGNORE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/delete.html) could raise an assertion. (Bug #17720294)
- [`UNION ALL`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/union.html) statements for which one [`SELECT`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/select.html) returned zero rows could result in an incorrect [`FOUND_ROWS()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/information-functions.html#function_found-rows) value. (Bug #17708480)
- Enabling Index Merge optimizer switches and setting a small [`sort_buffer_size`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-system-variables.html#sysvar_sort_buffer_size) value could lead to a server exit. (Bug #17617945)
- Some license and documentation files were missing from Windows MSI packages. (Bug #17584523)
- [`UNION ALL`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/union.html) queries for which the last [`SELECT`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/select.html) selected an aggregate value from an empty table resulted in an incorrect [`FOUND_ROWS()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/information-functions.html#function_found-rows) value. (Bug #17580869)
- Semijoin materialization strategy was not used for `VARCHAR` columns longer than 512 bytes, resulting in use of a less-efficient strategy and worse query performance. (The limit in characters rather than bytes depends on the column character set; 170 characters for `utf8`, for example.) (Bug #17566396)
- Disconnect processing overhead was reduced for sessions that have no outstanding prepared statements. Previously, a global mutex was acquired to handle these, but there is no need to do so in the absence of such statements. (Bug #17560986)
- The optimizer did not consider a clustered primary key as a covering index unless all columns required for a query were in the primary key definition. This incorrectly raised the calculated cost of using the index and caused it not to be used in some cases when it would be more efficient than the index otherwise chosen. (Bug #17560636)
- Selecting from the [`session_connect_attrs`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-session-connect-attrs-table.html) Performance Schema table under high load could cause a server exit. (Bug #17542370)
- The Performance Schema had a race condition adding and deleting stored procedure entries that could raise an assertion. (Bug #17529279)
- [`DROP TRIGGER`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/drop-trigger.html) succeeded even with the [`read_only`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-system-variables.html#sysvar_read_only) system variable enabled. (Bug #17503460)
- An incorrect result could be produced by a simple [`COUNT(DISTINCT)`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/aggregate-functions.html#function_count) query on a table that contains a large number of distinct values. This was more likely when [`tmp_table_size`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-system-variables.html#sysvar_tmp_table_size) or [`max_heap_table_size`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-system-variables.html#sysvar_max_heap_table_size) were set to small values. (Bug #17500866)
- Performance Schema memory instrumentation overhead was reduced.
	Memory allocated internally by the Performance Schema was not reported by the memory instrumentation. This was corrected, and there is now a `memory/performance_schema/internal_buffers` instrument (disabled by default) that can be enabled to obtain this information. (Bug #17493868)
- Stored programs were not listed in the [`objects_summary_global_by_type`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-objects-summary-global-by-type-table.html) Performance Schema table. (Bug #17472833)
- `my_print_stacktrace()` printed a Reference Manual URL that pointed to the 5.1 manual. It now is parameterized for the current server series. (Bug #17465503)
- In debug builds, [`SHOW PROCEDURE         CODE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/show-procedure-code.html) raised an assertion. (Bug #17434385)
- Compilation failures under Visual Studio 2012 were corrected. (Bug #17430236)
- For JSON-format [`EXPLAIN`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/explain.html) statements, materialized views were incorrectly labeled as `optimized_away_subqueries` rather than as `materialized_from_subquery`. (Bug #17428655)
- [`KILL`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/kill.html) with an invalid thread ID value could raise an assertion. (Bug #17420682)
- An assertion was raised if a statement tried to set an exception condition in a diagnostics area which already contained an exception or completion condition. This could occur if a failed stored program tried to transfer its exception condition to the diagnostics area of its caller that already contained a condition. (Bug #17400687)
- In the Performance Schema memory instrumentation, statistics collected for memory-free operations could be under-evaluated, leading to the appearance of a memory leak. (Bug #17400029)
- Compiling without the Performance Schema resulted in unresolved symbols. (Bug #17399658)
- Some warnings produced by **mysql\_install\_db** referred to the now-deprecated [`log_warnings`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-system-variables.html#sysvar_log_warnings) system variable. These have been updated to refer to [`log_error_verbosity`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-system-variables.html#sysvar_log_error_verbosity) instead. (Bug #17363350)
- An assertion was raised if `SET PASSWORD` was used for an account that has been manually deleted from the `mysql.user` table but still present in memory. (Bug #17359329)
- Savepoints could not be used successfully following an [`ER_LOCK_DEADLOCK`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_lock_deadlock) error (or [`ER_LOCK_WAIT_TIMEOUT`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_lock_wait_timeout) error, if [`innodb_rollback_on_timeout`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/innodb-parameters.html#sysvar_innodb_rollback_on_timeout) was enabled). (Bug #17356954)
	References: This issue is a regression of: Bug #14188793.
- The `CLIENT_CONNECT_WITH_DB` flag was improperly handled in the C client library. This could lead to a malformed packet sent to the server. (Bug #17351732)
- Upgrades using RPM packages failed if the MySQL server was running due to failure to ignore the `mysqld_safe.pid` file created by **mysqld\_safe**. (Bug #17343851)
- The [`mysql_real_connect()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-real-connect.html) C API function could leak memory if it failed. (Bug #17337684)
- The `filesort` implementation sometimes failed to allocate enough buffer space, leading to a server exit. (Bug #17326567)
- Cost comparison for [`ref`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/explain-output.html#jointype_ref) access could be inaccurate. (Bug #17303649)
- The [`mysql_options()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-options.html) C API function could leak memory if called more than once with the `MYSQL_SET_CLIENT_IP` option. (Bug #17297012)
- The [`CONV()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mathematical-functions.html#function_conv) function could call `abs(INT_MIN)`, which is undefined, and cause a server exit. (Bug #17296644)
- An error array in the SSL code was missing a comma, leading to implicit concatenation of adjacent messages and a resulting off-by-one error in the relationship between error numbers and messages. (Bug #17294150)
- Full-text search on `InnoDB` tables failed on searches that used the `+` boolean operator. (Bug #17280122)
- For single-threaded workloads, the optimizer recognizes some special cases for which it can avoid function calls and enhance performance. (Bug #17234723)
- The `my_load_path()` function could in some cases calculate a path value incorrectly. (Bug #17204851)
- Temporary table columns were marked as temporarily nullable without taking into account the presence of triggers for the table. This could lead to `NOT NULL` columns being updated to `NULL` by a multiple-table [`UPDATE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/update.html) statement. (Bug #17055378)
- In debug builds, an assert could be raised if a statement was killed while executing a trigger. (Bug #17049537)
- Within a stored program, comparison of the value of a scalar subquery with an `IN` clause resulted in an error for the first execution and raised an assertion for the second execution. (Bug #17029399)
- Information was not transferred between two optimizer modules because there were duplicate variables for the same information. This could lead to suboptimal query execution plans and incorrect query results. (Bug #16982071, Bug #70021, Bug #17310161)
- JSON-format [`EXPLAIN`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/explain.html) statements could leak memory. (Bug #16970785)
- Queries with `ROLLUP` and an inner subquery with a reference to an outer field could raise an assertion. (Bug #16967281)
- [`GRANT`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/grant.html) without an `IDENTIFIED BY` clause resulted in an error even for existing users. (Bug #16938568)
- [`GROUP_CONCAT()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/aggregate-functions.html#function_group-concat) with an invalid separator could cause a server exit. (Bug #16870783)
- For partitioned tables, queries could return different results depending on whether Index Merge was used. (Bug #16862316)
	References: See also: Bug #17648468, Bug #176588348, Bug #18167648.
- **mysqltest\_embedded** does not work with the `--ps-protocol` option, so it now issues a warning if that option is given. (Bug #16817580)
- An internal `InnoDB` string routine could write past the end of a buffer. (Bug #16765410)
- GIS intersection-related code was missing a return value check, leading to a loop in nondebug builds and a raised assertion in debug builds. (Bug #16659166)
- For debug builds, when the optimizer removed an `Item_ref` pointing to a subquery, it caused a server exit. (Bug #16509874)
	References: This issue is a regression of: Bug #16318585.
- It is no longer possible to expire the password for anonymous-user accounts because an anonymous user cannot execute [`SET PASSWORD`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/set-password.html) to reset the account password. (Bug #16483619)
- On Windows, a MySQL client program that simply used `#include <mysql.h>` could not be compiled due to missing Windows declarations in that file. The same program would compile on other platforms. (Bug #16409270)
	References: See also: Bug #17514554.
- `HANDLER READ` could cause a server exit due to wrongly considering columns as constant. (Bug #16386136)
- Using the binary client/server protocol, the second execution of a prepared statement for a query with parameters in the `LIMIT` clause raised an assertion. (Bug #16346241)
- Very long database names in queries could cause the server to exit. (Bug #15912213, Bug #16900358)
- Memory allocated for the Performance Schema was not freed at server shutdown. (Bug #14771682)
- If an [`INSTALL PLUGIN`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/install-plugin.html) statement contained invalid UTF-8 characters in the shared library name, it caused the server to hang (or to raise an assertion in debug builds). (Bug #14653594, Bug #23080148, Bug #27167197)
- Standalone Windows MSI packages did not have the `ALLUSERS` property set. They now set `ALLUSERS=1`. For earlier MSI packages in this MySQL series, a workaround is to use the following command:
	```
	C:\> msiexec /i msi_installer_name ALLUSERS=1
	```
	(Bug #14647206)
- Deadlocks involving metadata locks and `InnoDB` deadlocks were both reported as an [`ER_LOCK_DEADLOCK`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_lock_deadlock) error, but only `InnoDB` deadlocks rolled back the transaction. Now both deadlocks roll back the transaction. (Bug #14188793)
- Columns in a `PRIMARY KEY` must be `NOT         NULL`, but if declared explicitly as `NULL` produced no error. Now an error occurs. For example, a statement such as [`CREATE TABLE t (i         INT NULL PRIMARY KEY)`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/create-table.html) is rejected. The same occurs for similar [`ALTER TABLE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/alter-table.html) statements. (Bug #13995622, Bug #66987, Bug #15967545, Bug #16545198)
- Some `.pdb` files were missing from Windows Zip archive distributions. (Bug #13878021)
- Several issues identified by the Coverity static analysis tool were fixed. Thanks to Jan Staněk and Honza Horak for the patches. (Bug #70591, Bug #17590095)
- Setting [`host_cache_size`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-system-variables.html#sysvar_host_cache_size) at startup had no effect. (Bug #70552, Bug #17576516)
- MySQL did not compile on OS X 10.9 (Mavericks). (Bug #70542, Bug #17647863)
- For [``EXPLAIN FOR         CONNECTION *`connection_id`*``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/explain.html), the parser did not permit *`connection_id`* values larger than the maximum signed [`BIGINT`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/integer-types.html) value. The maximum unsigned value now is permitted. (Bug #70533, Bug #17564492)
- [`EXPLAIN FOR         CONNECTION`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/explain.html) reported no error if the connection ID belonged to no connection thread. (Bug #70532, Bug #17564493)
- In some cases, range conditions over indexes defined on column prefixes returned incomplete result sets. (For example, ``SELECT ... WHERE 'abcdef1' <         *`col_name`* AND         *`col_name`* < 'abcdef9'``, where the index on *`col_name`* indexed only the first 6 characters.) (Bug #70341, Bug #17458273)
- `InnoDB` full-text searches failed to find records within transactions that included savepoints. (Bug #70333, Bug #17458835)
- Incorrect reference counting in the range optimizer module resulted in potential for missing or duplicate rows in the query result set. (Bug #70236, Bug #17405466)
- If asked to upgrade a server that was running without `InnoDB` enabled, **mysql\_upgrade** issued complaints about `InnoDB` tables not existing (tables that will not exist unless `InnoDB` is available). (Bug #70152, Bug #17361912)
- With the thread pool plugin enabled, the `PROCESSLIST_USER` and `PROCESSLIST_HOST` columns of the [`threads`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/performance-schema-threads-table.html) Performance Schema table were always `NULL` for client sessions. Also, for the main thread, those columns were not `NULL` but set to a user account.
	Note
	As part of the bug fix implementation, Performance Schema instrumentation for the thread pool plugin was changed to use `thread_pool`, not `sql`.
	(Bug #70028, Bug #17310065, Bug #17049691)
- Performance Schema instrumentation overhead was reduced for frequent connect/disconnect operations. (Bug #70018, Bug #17310878)
- Full-text search on `InnoDB` tables failed on searches for words containing apostrophes when using boolean operators.
	The [`innodb_ft_max_token_size`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/innodb-parameters.html#sysvar_innodb_ft_max_token_size) maximum value was incorrectly defined as 252, which is the maximum byte length. The maximum [`innodb_ft_max_token_size`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/innodb-parameters.html#sysvar_innodb_ft_max_token_size) value is now 84, which is the maximum character length. (Bug #69932, Bug #17276125)
- [`COUNT(DISTINCT)`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/aggregate-functions.html#function_count) should not count `NULL` values, but they were counted when the optimizer used Loose Index Scan. (Bug #69841, Bug #17222452)
- `InnoDB` deadlock caused transaction rollback but did not release metadata locks, blocking concurrent DDL on the transaction tables until the connection that got the deadlock issued an explicit `COMMIT` or `ROLLBACK`. (Bug #69668, Bug #17054007)
- In debug builds, static initialization code could call DBUG functions before the DBUG subsystem was initialized. (Bug #69653, Bug #17063675)
- Reads of `Geometry` values within a stored program could read already-freed memory and produce incorrect results. (Bug #69517, Bug #16985214)
- Specifying the same directory with multiple instances of [`--ignore-db-dir`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_ignore-db-dir) caused a server exit. (Bug #69441, Bug #16944177)
- For queries that qualify to be written to the slow query log, the check whether the log is enabled now occurs earlier, reducing overhead.
	Also, when [`log_throttle_queries_not_using_indexes`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-system-variables.html#sysvar_log_throttle_queries_not_using_indexes) is specified at server startup, a value is now required. Previously, it was incorrectly treated as optional. (Bug #69420, Bug #16924125)
- Some `INSERT INTO ... SELECT ... FROM` statements were slow unless the [`tmp_table_size`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-system-variables.html#sysvar_tmp_table_size) and [`max_heap_table_size`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-system-variables.html#sysvar_max_heap_table_size) system variables were set large enough to permit the temporary table used for query processing to be stored in the `MEMORY` storage engine. (Bug #69368, Bug #16894092)
- Missing `va_end()` calls were added to logging and UCS2 code. Thanks to Jan Staněk for the patch. (Bug #68896, Bug #16725769)
- [`ER_TRUNCATED_WRONG_VALUE`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_truncated_wrong_value) (truncated value) errors for `DECIMAL` values failed to show the erroneous input value. (Bug #68745, Bug #16552002)
- For queries of the form ``UPDATE ... WHERE         *`unique_key`* ORDER BY ... LIMIT         ...``, incorrect rows could be updated. Unique keys permit multiple `NULL` values, but the optimizer did not always consider all of them. (Bug #68656, Bug #16482467)
- Within a stored function or trigger, occurrence of an [`ER_LOCK_WAIT_TIMEOUT`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_lock_wait_timeout) error caused failure to execute a condition handler. (Bug #67947, Bug #16041903)
- With a `NULL` literal in a particular parameter position, [`IFNULL()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/flow-control-functions.html#function_ifnull), [`COALESCE()`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/comparison-operators.html#function_coalesce), and [`CASE`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/flow-control-functions.html#operator_case) returned a signed value when they should return an unsigned value. (Bug #65976, Bug #14359340)
- The server uses the ethernet hardware address for UUID generation, but made assumptions about the names of ethernet devices rather than querying the system for their names. Thanks to Honza Horak for the patch. (Bug #63055, Bug #13548252)
- Host names in grant tables are stored in lowercase, but **mysql\_install\_db** could fail to observe this convention, leading to accounts that could not be dropped with [`DROP USER`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/drop-user.html). (Bug #62255, Bug #12917164, Bug #62254, Bug #12917151)
- If one connection changed its default database and simultaneously another connection executed `SHOW         PROCESSLIST`, the second connection could access invalid memory when attempting to display the first connection's default database. memory. (Bug #58198, Bug #11765252)
- At server shutdown, a race condition between the main thread and the shutdown thread could cause server failure. (Bug #56666, Bug #11763896)
- Fixed a potential problem with the MySQL string function `strmov()`. Its behavior with respect to overlap of source and destination previously depended on native support for `stpcpy()`. (Bug #48864, Bug #17429539)
- For a column declared as a `PRIMARY KEY`, the MySQL sometimes unnecessarily added a `DEFAULT` clause. For example, for `CREATE TABLE t (a INT, PRIMARY         KEY(a))`, a `DEFAULT 0` clause was added, whereas with `CREATE TABLE t (a INT PRIMARY         KEY)`, it was not. (Bug #36723, Bug #11748566)
- Views containing ``ORDER BY         *`integer`*`` could result in errors at view evaluation time. Consider these view definitions, which use `ORDER BY` with an ordinal number:
	```
	CREATE VIEW v1 AS SELECT x, y, z FROM t ORDER BY 2;
	CREATE VIEW v2 AS SELECT x, 1, z FROM t ORDER BY 2;
	```
	In the first case, `ORDER BY 2` refers to a named column `y`. In the second case, it refers to a constant 1. For queries that select from either view fewer than 2 columns (the number named in the `ORDER         BY` clause), an error occurred if the server evaluated the view using the MERGE algorithm. Examples:
	```
	mysql> SELECT x FROM v1;
	ERROR 1054 (42S22): Unknown column '2' in 'order clause'
	mysql> SELECT x FROM v2;
	ERROR 1054 (42S22): Unknown column '2' in 'order clause'
	```
	To handle view definitions like this, the server now writes them differently into the `.frm` file that stores the view definition. This difference is visible with [`SHOW CREATE VIEW`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/show-create-view.html). Previously, the `.frm` file contained this for the `ORDER BY 2` clause:
	```
	For v1: ORDER BY 2
	For v2: ORDER BY 2
	```
	Now, the `.frm` file contains this:
	```
	For v1: ORDER BY \`t\`.\`y\`
	For v2: ORDER BY ''
	```
	That is, for `v1`, 2 is replaced by a reference to the name of the column referred to. For `v2`, 2 is replaced by a constant string expression (ordering by a constant has no effect, so ordering by any constant will do).
	If you experience view-evaluation errors such as just described, drop and recreate the view so that the `.frm` file contains the updated view representation. Alternatively, for views like `v2` that order by a constant value, drop and recreate the view with no `ORDER         BY` clause. (Bug #28695, Bug #11746789)
- Killing a query that is performing a `filesort` operation resulted in an [`ER_SERVER_SHUTDOWN`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_server_shutdown) (Server shutdown in progess) error. (Bug #18256, Bug #11745656)