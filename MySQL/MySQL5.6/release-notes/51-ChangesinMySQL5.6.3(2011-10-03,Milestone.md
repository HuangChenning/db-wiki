---
title: "Changes in MySQL 5.6.3 (2011-10-03, Milestone 6)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=243"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Note This is a milestone release, for use at your own risk. Upgrades between milestone releases (or from a milestone release to a GA release) are not supported.

Significant development changes take place in milestone releases and you may encounter compatibility issues, such as data format changes that require attention in addition to the usual procedure of running `mysql_upgrade`. For example, you may find it necessary to dump your data with `mysqldump` before the upgrade and reload it afterward. (Making a backup before the upgrade is a prudent precaution in any case.)

- Parallel Event Execution (Multithreaded Slave)
- Optimizer Notes
- Performance Schema Notes
- Security Notes
- Functionality Added or Changed
- Bugs Fixed

## MySQL 5.6 Release Notes

> Parallel Event Execution (Multithreaded Slave)

- Replication: MySQL replication now supports a multithreaded slave executing replication events

from the master across different databases in parallel, which can result in significant improvements in application throughput when certain conditions are met. The optimum case is that the data be partitioned per database, and that updates within a given database occur in the same order relative to one another as they do on the master. However, transactions do not need to be coordinated between different databases.

The `slave_parallel_workers` server system variable (added in this release) sets the number of slave worker threads for executing replication events in parallel. When parallel execution is enabled,the slave SQL thread acts as the coordinator for the slave worker threads, among which transactions are distributed on a per-database basis. This means that a worker thread on the slave can process successive transactions on a given database without waiting for updates on other databases to complete.

Due to the fact that transactions on different databases can occur in a different order on the slave than on the master, checking for the most recently executed transaction does not guarantee that all previous transactions from the master have been executed on the slave. This has implications for logging and recovery when using a multithreaded slave. For information about how to interpret binary logging information when using multithreading on the slave, see SHOW SLAVE STATUS Statement.

(WL #5569)

> Optimizer Notes

- These query optimizer improvements were implemented:
- The `EXPLAIN` statement now provides execution plan information for `DELETE`, `INSERT`, `REPLACE`,

and `UPDATE` statements. Previously, `EXPLAIN` provided information only for `SELECT` statements.

- The optimizer more efficiently handles subqueries in the `FROM` clause (that is, derived tables):
- Materialization of subqueries in the `FROM` clause is postponed until their contents are needed

during query execution, which improves performance. Delay of materialization may even enable the optimizer to avoid it entirely. Consider a query that joins the result of a subquery in the `FROM` clause to another table: If the optimizer processes that other table first and finds that it returns no rows, the join need not be carried out further and the optimizer need not materialize the subquery at all.

Previously, subqueries in the `FROM` clause were materialized for `EXPLAIN SELECT` statements.

This resulted in partial `SELECT` execution, even though the purpose of `EXPLAIN` is to obtain query plan information, not to execute the query. This materialization no longer occurs, so `EXPLAIN` is faster for such queries.

- During query execution, the optimizer may add an index to a derived table to speed up row retrieval

from it.

For more information, see Optimizing Derived Tables.

- A Batched Key Access (BKA) join algorithm is now available that uses both index access to the joined

table and a join buffer. The BKA algorithm supports inner join and outer join operations, including nested outer joins. Benefits of BKA include improved join performance due to more efficient table scanning.

Two flags have been added to the `optimizer_switch` system variable (`block_nested_loop`and `batched_key_access`). These flags control how the optimizer uses the Block Nested-Loop

## MySQL 5.6 Release Notes

and Batched Key Access join algorithms. Previously, the `optimizer_join_cache_level` system variable was used for join buffer control; this variable has been removed.

For more information, see Block Nested-Loop and Batched Key Access Joins.

- The optimizer now has a tracing capability. This will be of use to optimizer developers, and also to

users who file bugs against the optimizer and want to provide more information that will help resolve the bug. The interface is provided by a set of `optimizer_trace_xxx` system variables and the`INFORMATION_SCHEMA.OPTIMIZER_TRACE` table, but is subject to change. For details, see MySQL Internals: Tracing the Optimizer.

(Bug #44802, Bug #11753371, Bug #14295, Bug #11745379, Bug #27975, Bug #11746677, WL #4897,WL #5274, WL #5285)

> Performance Schema Notes

- The Performance Schema has these additions:
- The Performance Schema now instruments stages and statements. Stages are steps during

the statement-execution process, such as parsing a statement, opening a table, or performing a`filesort` operation. Stages correspond to the thread states displayed by `SHOW PROCESSLIST` or that are visible in the `INFORMATION_SCHEMA.PROCESSLIST` table. Stages begin and end when state values change.

Within the event hierarchy, wait events nest within stage events, which nest within statement events. To reflect this nesting in wait-event tables such as `events_waits_current`, the`NESTING_EVENT_ID` column now can be non-`NULL` to indicate the `EVENT_ID` value of the event within which an event is nested, and `NESTING_EVENT_TYPE` is a new column indicating the type of the nesting event.

The `setup_instruments` table now contains instruments with names that begin with `stage` and`statement`. Corresponding to these instruments, the `setup_timers` table now contains rows with`NAME` values of `stage` and `statement` that indicate the unit for stage and statement event timing.

The default unit for each is `NANOSECOND`.

These new tables store stage and statement events:

- `events_stages_current`: Current stage events
- `events_stages_history`: The most recent stage events for each thread
- `events_stages_history_long`: The most recent stage events overall
- `events_statements_current`: Current statement events
- `events_statements_history`: The most recent statement events for each thread
- `events_statements_history_long`: The most recent statement events overall

The `setup_consumers` table now contains consumer values with names corresponding to those table names. These consumers may be used to filter collection of stage and statement events.

There are also summary tables that provide aggregated stage and statement information.

Application developers can use statement instrumentation to see in detail the statements generated by an application, and how these statements are executed by the server. Stage instrumentation can

## MySQL 5.6 Release Notes

be used to focus on particular parts of statements. This information may be useful to change how an application issues queries against the database, to minimize the application footprint on the server,and to improve application performance and scalability.

For more information, see Performance Schema Stage Event Tables, Stage Summary Tables,Performance Schema Statement Event Tables, and Statement Summary Tables.

- The Performance Schema now provides statistics about connections to the server. When a client

connects, it does so under a particular user name and from a particular host. The Performance Schema tracks connections per account (user name plus host name) and separately per user name and per host name, using these tables:

- `accounts`: Connection statistics per client account
- `hosts`: Connection statistics per client host name
- `users`: Connection statistics per client user name

There are also summary tables that provide aggregated connection information.

It is good security practice to define a dedicated account per application, so that an application is given privileges to perform only those actions that it needs during its operation. This also facilitates monitoring because the information in the connection tables can be used by application developers to see load statistics per application when deploying several applications against a given database server.

For more information, see Performance Schema Connection Tables.

- Previously, the `setup_objects` table could be used only to specify by inclusion which objects

to instrument. There was no way to explicitly disable object instrumentation, such as to configure instrumention for all tables except those in a particular database. Now the `setup_objects` table includes an `ENABLED` column that indicates whether to instrument matching objects. This feature improves the `setup_objects` table usability because it permits exclusion patterns.

The default table contents now include a row that disables instrumentation for tables in the `mysql`database, which is a change from the previous default object instrumentation. This change is chosen assuming that end users want to instrument application objects, not internal server tables. The change reduces the default Performance Schema overhead because I/O and locks on `mysql` tables are not instrumented.

The table also includes rows that disable instrumentation for tables in the `INFORMATION_SCHEMA` and`performance_schema` databases. This is not a change in behavior because those tables were not instrumented before, but these rows make the full object instrumentation defaults explicit.

- The Performance Schema now instruments sockets. This enables monitoring of network

communication to and from the server. Information collected includes network activity such as socket instances, socket operations, and number of bytes transmitted and received.

The `setup_instruments` table now contains instruments with names that begin with `wait/io/``socket`. There is also an `idle` instrument used for idle events when a socket is waiting for the next request from the client. Corresponding to the latter instrument, the `setup_timers` table now

## MySQL 5.6 Release Notes

contains a row with a `NAME` value of `idle` that indicates the unit for idle event timing. The default unit

```
is MICROSECOND.
```

These new tables contain socket information:

- `socket_instances`: A real-time snapshot of the active connections to the MySQL server
- `socket_summary_by_instance`: Aggregate timer and byte count statistics generated by the

`wait/io/socket/*` instruments for all socket I/O operations, per socket instance

- `socket_summary_by_event_name`: Aggregate timer and byte count statistics generated by the

`wait/io/socket/*` instruments for all socket I/O operations, per socket instrument The information in the socket tables can be used by application developers, particularly those developing web-based applications, to assess the volume of network traffic directly attributable to queries generated by their application. This can be particularly useful during development of applications intended for large-scale implementations.

For more information, see The socket_instances Table, and Socket Summary Tables.

As a consequence of these changes, the `Opening table` thread state has been removed. The`Opening tables` state remains and can be used instead. (See General Thread States.)If you upgrade to this MySQL release from an earlier version, you must run `mysql_upgrade` (and restart the server) to incorporate these changes into the `performance_schema` database. (WL #4813,WL #2515, WL #5342)

> Security Notes

- For temporary tables created with the `CREATE TEMPORARY TABLE` statement, the privilege model has

changed.

Previously, the `CREATE TEMPORARY TABLES` privilege enabled users to create temporary tables with the `CREATE TEMPORARY TABLE` statement. However, other operations on a temporary table, such as `INSERT`, `UPDATE`, or `SELECT`, required additional privileges for those operations for the database containing the temporary table, or for the nontemporary table of the same name.

To keep privileges for temporary and nontemporary tables separate, a common workaround for this situation was to create a database dedicated to the use of temporary tables. Then for that database,a user could be granted the `CREATE TEMPORARY TABLES` privilege, along with any other privileges required for temporary table operations done by that user.

Now, the `CREATE TEMPORARY TABLES` privilege enables users to create temporary tables with `CREATE``TEMPORARY TABLE`, as before. However, after a session has created a temporary table, the server performs no further privilege checks on the table. The creating session can perform any operation on the table, such as `DROP TABLE`, `INSERT`, `UPDATE`, or `SELECT`.

One implication of this change is that a session can manipulate its temporary tables even if the current user has no privilege to create them. Suppose that the current user does not have the `CREATE``TEMPORARY TABLES` privilege but is able to execute a `DEFINER`-context stored procedure that executes with the privileges of a user who does have `CREATE TEMPORARY TABLES` and that creates a temporary table. While the procedure executes, the session uses the privileges of the defining user. After the procedure returns, the effective privileges revert to those of the current user, which can still see the temporary table and perform any operation on it. (Bug #27480, Bug #11746602)

## MySQL 5.6 Release Notes

- Statement logging has been modified so that passwords do not appear in plain text for the following

statements:

```
CREATE USER ... IDENTIFIED BY ...
GRANT ... IDENTIFIED BY ...
SET PASSWORD ...
```

Passwords in those statements are rewritten not to appear literally in statement text, for the general query log, slow query log, and binary log. Rewriting does not apply to other statements.

For the general query log, password rewriting can be suppressed by starting the server with the `--log-``raw` option. This option may be useful for diagnostic purposes, to see the exact text of statements as received by the server, but for security reasons is not recommended for production use.

One change you will notice is that statements that cannot be parsed (due, for example, to syntax errors)are no longer written to the general query log because they cannot be known to be password free. Use cases that require logging of all statements including those with errors should use the `--log-raw`option, bearing in mind that this also bypasses password writing. (WL #5706)

> Functionality Added or Changed

- Incompatible Change: In the audit plugin interface, the `event_class` member was removed from the

`mysql_event_general` structure and the calling sequence for the notification function was changed.

Originally, the second argument was a pointer to the event structure. The function now receives this information as two arguments: an event class number and a pointer to the event. Corresponding to these changes, `MYSQL_AUDIT_INTERFACE_VERSION` was increased to `0x0300`.

The `plugin_audit.h` header file, and the `NULL_AUDIT` example plugin in the `plugin/audit_null`directory were modified per these changes. See Writing Audit Plugins.

- Important Change; Replication: The `RESET SLAVE` statement has been extended with an `ALL`

keyword. In addition to deleting the `master.info`, `relay-log.info`, and all relay log files, `RESET``SLAVE ALL` also clears all connection information otherwise held in memory following execution of`RESET SLAVE`. (Bug #11809016, Bug #11763210)

- Performance; InnoDB: At shutdown, MySQL can record the pages that are cached in the

`InnoDB` buffer pool, then reload those same pages upon restart. This technique can help to quickly reach consistent throughput after a restart, without a lengthy warmup period. This preload capability uses a compact save format and background I/O to minimize overhead on the MySQL server. The basic dump/restore capability is enabled through the configuration options

```
innodb_buffer_pool_dump_at_shutdown and innodb_buffer_pool_load_at_startup.
```

Related configuration options such as `innodb_buffer_pool_dump_now` and`innodb_buffer_pool_load_now` offer extra flexibility for advanced users to configure the MySQL server for different workloads. See Saving and Restoring the Buffer Pool State for details. (Bug#11765816, Bug #58819, WL #5712)

- Performance; InnoDB: When `innodb_file_per_table` is enabled, each `InnoDB` table is created

in its own tablespace file (`.ibd` file). As data inside the table grows, the `.ibd` file is extended, which is an I/O operation that may create a bottleneck for busy systems with many `InnoDB` tables. For `InnoDB`tables that are stored inside the system tablespace, the extension operation happens less frequently, as space freed by `DELETE` or `TRUNCATE` operations within one table can be reused by another table.

MySQL 5.6 improves concurrency for extending `InnoDB` tablespace files (`.ibd` files), so that multiple`.ibd` files can be extended simultaneously without blocking read or write operations performed by other threads. (Bug #11763692, Bug #56433, WL #5654)

## MySQL 5.6 Release Notes

- Performance; InnoDB: You can improve the efficiency of the `InnoDB` checksum feature by specifying

the configuration option `innodb_checksum_algorithm=crc32`, which turns on a faster checksum algorithm. This option replaces the `innodb_checksums` option. Data written using the old checksum algorithm (option value `innodb`) is fully upward-compatible; tablespaces modified using the new checksum algorithm (option value `crc32`) cannot be downgraded to an earlier version of MySQL that does not support the `innodb_checksum_algorithm` option. (Bug #11757757, Bug #49852, WL#5652)

- Performance; InnoDB: The code that detects deadlocks in `InnoDB` transactions has been modified to

use a fixed-size work area rather than a recursive algorithm. The resulting detection operation is faster as a result. You do not need to do anything to take advantage of this enhancement.

Under both the old and new detection mechanisms, you might encounter a `search too deep` error that is not a true deadlock, but requires you to re-try the transaction the same way as with a deadlock.

(WL #5915)

- Performance; InnoDB: The `InnoDB` thread-scheduling code has been enhanced to work better with

greater than 16 threads. Where possible, atomic instructions are used. You control this feature by setting the configuration option `innodb_thread_concurrency` to a nonzero value, and adjusting the value of`innodb_adaptive_max_sleep_delay`. See Configuring Thread Concurrency for InnoDB for details.

(WL #5758)

- Performance; InnoDB: Work continues to offload flush operations from the `InnoDB` main thread,

doing them in the `page_cleaner` thread instead. The latest changes to the buffer pool flushing algorithms can improve performance for some I/O-bound workloads, particularly in configurations with multiple buffer pool instances. You control this feature by adjusting the settings for the`innodb_lru_scan_depth` and `innodb_flush_neighbors` configuration options. To find the optimal settings, test each combination of the above settings with both the Adaptive Hash Index and the Doublewrite Buffer turned on and off. See Configuring Buffer Pool Flushing for more details. (WL #5580)

- Performance; InnoDB: This feature optionally moves the `InnoDB` undo log out of the system

tablespace into one or more separate tablespaces. The I/O patterns for the undo log make these new tablespaces good candidates to move to SSD storage, while keeping the system tablespace on hard disk storage. This feature is controlled by the configuration options

```
innodb_undo_directory, innodb_undo_tablespaces, and innodb_undo_logs (formerly
```

known as `innodb_rollback_segments`). Users cannot drop the separate tablespaces created to hold`InnoDB` undo logs, or the individual segments inside those tablespaces.

MySQL instances configured this way are not downward-compatible; older versions of MySQL cannot access the undo logs that reside in their own tablespace.

For details, see Undo Tablespaces. (WL #5535)

- InnoDB: `InnoDB` now permits concurrent reads while creating a secondary index. (Bug #11853126)

References: See also: Bug #11751388, Bug #11784056, Bug #11815600.

- InnoDB: The `InnoDB` redo log files now have a maximum combined size of 512GB, increased from

4GB. You can specify the larger values through the `innodb_log_file_size` option.

There is no special upgrade process or file format to take advantage of this enhancement. The bytes that record the extra size information were already reserved in the `InnoDB` system tablespace. However, if you develop applications that interact with the `InnoDB` logical sequence number (LSN) value, change your code to use guaranteed 64-bit variables to store and compare LSN values, rather than 32-bit variables. (Bug #11765780, Bug #58779, WL #5739)

## MySQL 5.6 Release Notes

- InnoDB: `InnoDB` tables can now be created with character sets whose collation ID is greater than 255.

For example, the following `InnoDB` table can now be created, where formerly the collation ID of 359 was beyond the range supported by `InnoDB`.

```
mysql> show collation like 'ucs2_vn_ci';
+------------+---------+-----+---------+----------+---------+
| Collation  | Charset | Id  | Default | Compiled | Sortlen |
+------------+---------+-----+---------+----------+---------+
| ucs2_vn_ci | ucs2    | 359 |         |          |       8 |
+------------+---------+-----+---------+----------+---------+
1 row in set (0.00 sec)
mysql> CREATE TABLE two_byte_collation (c1 char(1) CHARACTER SET UCS2 COLLATE UCS2_VN_CI)
-> ENGINE = INNODB;
Query OK, 0 rows affected (0.16 sec)
```

This capability opens up `InnoDB` tables for use with a range of user-defined character sets. MySQL predefined character sets have previously been limited to a maximum of 255, and now that restriction is lifted. See Choosing a Collation ID for more information. (WL #5557)

- Replication: MySQL 5.6.1 added timestamps to the error messages shown in the `Last_IO_Error`

and `Last_SQL_Error` columns of the output of `SHOW SLAVE STATUS`. Now these timestamps are shown in separate columns of their own, named `Last_IO_Error_Timestamp` and`Last_SQL_Error_Timestamp`, respectively. (Bug #11765599, Bug #58584)References: See also: Bug #43535, Bug #11752361.

- Replication: `BEGIN`, `COMMIT`, and `ROLLBACK` statements are now cached along with the statements

instead of being written when the cache is flushed to the binary log. This change does not affect DDL statements—which are written into the statement cache, then immediately flushed—or Incident events(which, along with Rotate events, are still written directly to the binary log). (WL #4832)References: See also: Bug #57275, Bug #11764443.

- Microsoft Windows: The Windows installer now creates an item in the MySQL menu named `MySQL`

`command line client - Unicode`. This item invokes the `mysql` client with properties set to communicate through the console to the MySQL server using Unicode. It passes the `--default-``character-set=utf8` option to `mysql` and sets the font to the `Lucida Console` Unicode-compatible font. See Unicode Support on Windows. (WL #5826)

- Following `EXPLAIN EXTENDED`, a change has been made to the transformed query displayed by `SHOW`

`WARNINGS`. Each `SELECT` part now is preceded by the `id` value from the associated `EXPLAIN` output row. This makes it easier to see the correspondence between those rows and parts of the transformed query. For example, this query:

```
EXPLAIN EXTENDED SELECT 36 FROM DUAL
```

results in:

```
/* select#1 */ select 36 from dual
```

And this query:

```
EXPLAIN EXTENDED SELECT a FROM t
WHERE a IN (SELECT b FROM u UNION SELECT c from v)
```

results in:

```
/* select#1 */ select a from t where a in (/* select#2 */
select b from u union /* select#3 */ select c from v);
```

## MySQL 5.6 Release Notes

(Bug #13035597)

- Several memory allocation calls were eliminated, resulting in improved performance. (Bug #12552221)
- `CMake` configuration support on Linux now provides a boolean `ENABLE_GCOV` option to control whether

to include support for `gcov`. (Bug #12549572)

- Previously, Performance Schema instrumentation for both the binary log and the relay log used these

instruments:

```
wait/io/file/sql/binlog
wait/io/file/sql/binlog_index
wait/synch/mutex/sql/MYSQL_BIN_LOG::LOCK_index
wait/synch/cond/sql/MYSQL_BIN_LOG::update_cond
```

Now instrumentation for the relay log uses these instruments, which makes it possible to distinguish binary log and relay log events:

```
wait/io/file/sql/relaylog
wait/io/file/sql/relaylog_index
wait/synch/mutex/sql/MYSQL_RELAY_LOG::LOCK_index
wait/synch/cond/sql/MYSQL_RELAY_LOG::update_cond
```

(Bug #59658, Bug #11766528)

- A new server option, `--plugin-load-add`, complements the `--plugin-load` option. `--plugin-`

`load-add` adds a plugin or plugins to the set of plugins to be loaded at startup. The argument format is the same as for `--plugin-load`. `--plugin-load-add` can be used to avoid specifying a large set of plugins as a single long unwieldy `--plugin-load` argument.

`--plugin-load-add` can be given in the absence of `--plugin-load`, but any instance of `--``plugin-load-add` that appears before `--plugin-load`. has no effect because `--plugin-load`resets the set of plugins to load.

This change affects the output of `mysqld --verbose --help` in that a value for `plugin-load` is no longer printed. (Bug #59026, Bug #11766001)

- When invoked with the `--auto-generate-sql` option, `mysqlslap` dropped the schema specified with

the `--create-schema` option at the end of the test run, which may have been unexpected by the user.

`mysqlslap` now has a `--no-drop` option that prevents any schema created during the test run from being dropped. (Bug #58090, Bug #11765157)

- The server now exposes SSL certificate expiration dates through the `Ssl_server_not_before`

and `Ssl_server_not_after` status variables. Both variables have values in ANSI time format (for example, Sep 12 16:22:06 2013 GMT), or are blank for non-SSL connections. (Bug #57648, Bug#11764778)

- Previously, `TEMPORARY` tables created with `CREATE TEMPORARY TABLES` used the default storage

engine unless the definition included an explicit `ENGINE` option. (The default engine is the value of the `default_storage_engine` system variable.) Since MySQL 5.5.5, when the default storage engine was changed from the nontransactional `MyISAM` engine to the transactional `InnoDB` engine,`TEMPORARY` tables have incurred the overhead of transactional processing.

To permit the default storage engine for `TEMPORARY` tables to be set independently of the default engine for permanent tables, the server now supports a `default_tmp_storage_engine` system variable.

For example, to create `TEMPORARY` tables as nontransactional tables by default, start the server with`--default_tmp_storage_engine=MyISAM`. The storage engine for `TEMPORARY` tables can still be

## MySQL 5.6 Release Notes

specified on an individual basis by including an `ENGINE` option in table definitions. (Bug #49232, Bug#11757216)

- Previously, for MySQL binaries linked against OpenSSL, if an SSL key file supplied to the MySQL server

or a MySQL client program (using the `--ssl-key` option) was protected by a passphrase, the program would prompt the user for the passphrase. This is now also the case for MySQL binaries linked against yaSSL. (Bug #44559, Bug #11753167)

- The `mysql` client program now has a `--binary-mode` option that helps when processing

`mysqlbinlog` output that may contain `BLOB` values. By default, `mysql` translates `\r\n` in statement strings to `\n` and interprets `\0` as the statement terminator. `--binary-mode` disables both features. It also disables all `mysql` commands except `charset` and `delimiter` in noninteractive mode (for input piped to `mysql` or loaded using the `source` command). (Bug #33048, Bug #11747577)

- MySQL binaries linked against OpenSSL (but not yaSSL) now support certificate revocation lists for SSL

connections:

- The MySQL server supports the `ssl_crl` and `ssl_crlpath` system variables, which indicate the

revocation list file or directory containing such files.

- MySQL client programs that support SSL recognize `--ssl-crl` and `--ssl-crlpath` options for

specifying a revocation list file or directory containing such files.

- The `CHANGE MASTER TO` statement has `MASTER_SSL_CRL` and `MASTER_SSL_CRLPATH` options

for specifying revocation list information to use when the slave connects to the master. The`mysql.slave_master_info` file has two more rows to store the values of these options. The `SHOW``SLAVE STATUS` statement has two more columns to display the values of these options.

The `mysql_options()` C API function has `MYSQL_OPT_SSL_CRL` and `MYSQL_OPT_SSL_CRLPATH`options for specifying revocation list information to use when the client connects to the master. In addition, `mysql_options()` now also supports `MYSQL_OPT_SSL_CA`, `MYSQL_OPT_SSL_CAPATH`,

```
MYSQL_OPT_SSL_CERT, MYSQL_OPT_SSL_CIPHER, and MYSQL_OPT_SSL_KEY options for
```

specifying other SSL parameters.

(Bug #31224, Bug #11747191)

- `mysqld` now has an `--ignore-db-dir` option that tells the server to ignore a given name for purposes

of the `SHOW DATABASES` statement or `INFORMATION_SCHEMA` tables. For example, if a MySQL configuration locates the data directory at the root of a file system on Unix, the system might create a`lost+found` directory there that the server should ignore. Starting the server with `--ignore-db-``dir=lost+found` causes that name not to be listed as a database.

To specify more than one name, use this option multiple times, once for each name. Specifying the option with an empty value (that is, as `--ignore-db-dir=`) resets the directory list to the empty list.

Instances of this option given at server startup are used to set the `ignore_db_dirs` system variable.

In addition to directories named by `--ignore-db-dir`, directories having a name that begins with a period are ignored. (Bug #22615, Bug #11746029)

- Client programs now display more information for SSL errors to aid in diagnosis and debugging of

connection problems. (Bug #21287, Bug #11745920)

- Some plugins operate in such a matter that they should be loaded at server startup, and not loaded or

unloaded at runtime. The plugin API now supports marking plugins this way. The `st_mysql_plugin`structure now has a `flags` member, which can be set to the OR of the applicable flags. The`PLUGIN_OPT_NO_INSTALL` flag indicates that the plugin cannot be loaded at runtime with the `INSTALL`

## MySQL 5.6 Release Notes

`PLUGIN` statement. This is appropriate for plugins that must be loaded at server startup with the `--``plugin-load` option. The `PLUGIN_OPT_NO_UNINSTALL` flag indicates that the plugin cannot be unloaded at runtime with the `UNINSTALL PLUGIN` statement.

The new member changes the interface, so the plugin interface version,`MYSQL_PLUGIN_INTERFACE_VERSION`, has been incremented from `0x0102` to `0x0103`. Plugins that require access to the new member must be recompiled to use version `0x0103` or higher. (WL #5973)

- A new utility, `mysql_plugin`, enables MySQL administrators to manage which plugins a MySQL server

loads. It provides an alternative to manually specifying the `--plugin-load` option at server startup or using the `INSTALL PLUGIN` and `UNINSTALL PLUGIN` statements at runtime. See mysql_plugin —Configure MySQL Server Plugins. (WL #5710)

- The following items are deprecated and will be removed in a future MySQL release. Where alternatives

are shown, applications should be updated to use them.

- The `innodb_table_monitor` table. Similar information can be obtained from `InnoDB`

`INFORMATION_SCHEMA` tables. See INFORMATION_SCHEMA InnoDB Tables.

- The `innodb_locks_unsafe_for_binlog` system variable.
- The `innodb_stats_sample_pages` system variable. Use

```
innodb_stats_transient_sample_pages instead.
```

- The `innodb_use_sys_malloc` and the `innodb_additional_mem_pool_size` system variables.

(WL #5533)

- The undocumented `--all` option for `perror` has been removed. Also, `perror` no longer displays

messages for BDB error codes. (WL #5914)

- MySQL now includes support for manipulating IPv6 network addresses and for validating IPv4 and IPv6

addresses:

- The `INET6_ATON()` and `INET6_NTOA()` functions convert between string and numeric forms of IPv6

addresses. Because numeric-format IPv6 addresses require more bytes than the largest integer type,the representation uses the `VARBINARY` data type.

- The `IS_IPV4()` and `IS_IPV6()` functions test whether a string value represents a valid IPv4 or IPv6

address. The `IS_IPV4_COMPAT()` and `IS_IPV4_MAPPED()` functions test whether a numeric-format value represents a valid IPv4-compatible or IPv4-mapped address.

- No changes were made to the `INET_ATON()` or `INET_NTOA()` functions that manipulate IPv4

addresses.

`IS_IPV4()` is more strict than `INET_ATON()` about what constitutes a valid IPv4 address, so it may be useful for applications that need to perform strong checks against invalid values. Alternatively, use`INET6_ATON()` to convert IPv4 addresses to internal form and check for a `NULL` result (which indicates an invalid address). `INET6_ATON()` is equally strong as `IS_IPV4()` about checking IPv4 addresses.

(WL #5787)

- The `max_allowed_packet` system variable now controls the maximum size of parameter values that

can be sent with the `mysql_stmt_send_long_data()` C API function.

- The `NULL_AUDIT` example plugin in the `plugin/audit_null` directory has been updated to count

instances of events in the `MYSQL_AUDIT_CONNECTION_CLASS` event class. See Writing Audit Plugins.

## MySQL 5.6 Release Notes

> Bugs Fixed

- Security Fix: A security bug was fixed. (Bug #59533)
- Incompatible Change: For socket I/O, an optimization for the case when the server used alarms for

timeouts could cause a slowdown when socket timeouts were used instead.

The fix for this issue results in several changes:

- Previously, timeouts applied to entire packet-level send or receive operations. Now timeouts apply to

individual I/O operations at a finer level, such as sending 10 bytes of a given packet.

- The handling of packets larger than `max_allowed_packet` has changed. Previously, if an

application sent a packet bigger than the maximum permitted size, or if the server failed to allocate a buffer sufficiently large to hold the packet, the server kept reading the packet until its end, then skipped it and returned an `ER_NET_PACKET_TOO_LARGE` error. Now the server disconnects the session if it cannot handle such large packets.

- On Windows, the default value for the `MYSQL_OPT_CONNECT_TIMEOUT` option to `mysql_options()`

is no longer 20 seconds. Now the default is no timeout (infinite), the same as on other platforms.

- Building and running MySQL on POSIX systems now requires support for `poll()` and `O_NONBLOCK`.

These should be available on any modern POSIX system.

(Bug #54790, Bug #36225, Bug #11762221, Bug #51244, Bug #11758972)

- Incompatible Change: The `mysql_affected_rows()` C API function returned 3 (instead of 2) for

`INSERT ... ON DUPLICATE KEY UPDATE` statements where there was a duplicated key value.

Now the affected-rows value per row is 1 if the row is inserted as a new row, 2 if an existing row is updated, and 0 if an existing row is set to its current values. If you specify the `CLIENT_FOUND_ROWS`flag to `mysql_real_connect()` when connecting to `mysqld`, the affected-rows value is 1 (not 0) if an existing row is set to its current values. (Bug #46675, Bug #11754979)

- Incompatible Change: Handling of a date-related assertion was modified. A consequence of this

change is that several functions become more strict when passed a `DATE()` function value as their argument and reject incomplete dates with a day part of zero. These functions are affected:

```
CONVERT_TZ(), DATE_ADD(), DATE_SUB(), DAYOFYEAR(), LAST_DAY(), TIMESTAMPDIFF(),
TO_DAYS(), TO_SECONDS(), WEEK(), WEEKDAY(), WEEKOFYEAR(), YEARWEEK().
```

It was later determined that stricter handling is unnecessary for `LAST_DAY()`, which was reverted to permit a zero day part in MySQL 5.6.5.

References: See also: Bug #13458237.

- Performance; InnoDB: This fix improves the performance of operations on `VARCHAR(N)` columns in

`InnoDB` tables, where N is declared as a large value but the actual string values in the table are short.

(Bug #12835650)

- Performance; InnoDB: The mechanism that `InnoDB` uses to detect if the MySQL server is idle was

made more accurate, to avoid slowdown due to flush operations that normally occur when no other activity is taking place. The mechanism now considers that the server is not idle if there are pending read requests for the `InnoDB` buffer pool. (Bug #11766123, Bug #59163)

## MySQL 5.6 Release Notes

- InnoDB; Replication: Trying to update a column, previously set to `NULL`, of an `InnoDB` table with no

primary key caused replication to fail on the slave with `Can't find record in 'table'`.

Note This issue was inadvertently reintroduced in MySQL 5.6.6, and fixed again in MySQL 5.6.12.

(Bug #11766865, Bug #60091)References: See also: Bug #16566658.

- InnoDB: The `DATA_LENGTH` column in the `INFORMATION_SCHEMA.TABLES` table now correctly reports

the on-disk sizes of tablespaces for `InnoDB` compressed tables. (Bug #12770537)

- InnoDB: A failed `CREATE INDEX` operation for an `InnoDB` table could result in some memory being

allocated but not freed. This memory leak could affect tables created with the `ROW_FORMAT=DYNAMIC` or`ROW_FORMAT=COMPRESSED` setting. (Bug #12699505)

- InnoDB: With the configuration settings `innodb_file_per_table=1` and

`innodb_file_format=Barracuda`, inserting a column value greater than half the page size, and including that column in a secondary index, could cause a crash when that column value was updated.

(Bug #12637786)

- InnoDB: The underlying tables to support the `InnoDB` persistent statistics feature were renamed and

moved into the `mysql` database. `innodb.table_stats` became `mysql.innodb_table_stats`, and`innodb.index_stats` became `mysql.innodb_index_stats`. (Bug #12604399)

- InnoDB: The server could halt if `InnoDB` interpreted a very heavy I/O load for 15 minutes or more as

an indication that the server was hung. This change fixes the logic that measures how long `InnoDB`threads were waiting, which formerly could produce false positives. (Bug #11877216, Bug #11755413,Bug #47183)

- InnoDB: With the setting `lower_case_table_names=2`, inserts into `InnoDB` tables covered by

foreign key constraints could fail after a server restart. (Bug #11831040, Bug #60196, Bug #60909)

- InnoDB: If the MySQL Server crashed immediately after creating an `InnoDB` table, attempting to access

the table after restart could cause another crash. The issue could occur if the server halted after `InnoDB`created the primary index for the table, but before the index definition was recorded in the MySQL metadata. (Bug #11766824, Bug #60042)

- InnoDB: If the server crashed while an XA transaction was prepared but not yet committed, the

transaction could remain in the system after restart, and cause a subsequent shutdown to hang. (Bug#11766513, Bug #59641)

- InnoDB: The MySQL server could hang during `CREATE TABLE`, `OPTIMIZE TABLE`, or `ALTER TABLE`

or other DDL operation that performs a table copy for an `InnoDB` table, if such operations were performed by multiple sessions simultaneously. The error was reported as:

```
InnoDB: Error: semaphore wait has lasted > 600 seconds
```

(Bug #11760042, Bug #52409)

- InnoDB: With the setting `lower_case_table_names=2`, inserts into `InnoDB` tables covered by

foreign key constraints could fail after a server restart. This is a similar problem to the foreign key error in Bug #11831040 / Bug #60196 / Bug #60909, but with a different root cause and occurring on OS X.

## MySQL 5.6 Release Notes

- Partitioning: The internal `get_partition_set()` function did not take into account the possibility that

a key specification could be `NULL` in some cases. (Bug #12380149)

- Partitioning: When executing a row-ordered retrieval index merge, the partitioning handler used

memory from that allocated for the table, rather than that allocated to the query, causing table object memory not to be freed until the table was closed. (Bug #11766249, Bug #59316)

- Partitioning: Attempting to use `ALTER TABLE ... EXCHANGE PARTITION` to exchange a view with

a (nonexistent) partition of a table that was not partitioned caused the server to crash. (Bug #11766232,Bug #60039)

- Partitioning: Auto-increment columns of partitioned tables were checked even when they were not

being written to. In debug builds, this could lead to a server crash. (Bug #11765667, Bug #58655)

- Partitioning: The `UNIX_TIMESTAMP()` function was not treated as a monotonic function for purposes

of partition pruning. (Bug #11746819, Bug #28928)

- Partitioning: A problem with a previous fix for poor performance of `INSERT ON DUPLICATE KEY`

`UPDATE` statements on tables having many partitions caused the handler function for reading a row from a specific index to fail to store the ID of the partition last used. This caused some statements to fail with`Can't find record` errors. (Bug #59297, Bug #11766232)References: This issue is a regression of: Bug #52455.

- Replication: A mistake in thread cleanup could cause a replication master to crash. (Bug #12578441)
- Replication: When using row-based replication and attribute promotion or demotion (see Replication of

Columns Having Different Data Types), memory allocated internally for conversion of `BLOB` columns was not freed afterwards. (Bug #12558519)

- Replication: A memory leak could occur when re-creating a missing master info repository, because a

new I/O cache used for a reference to the repository was re-created when the repository was re-created,but the previous cache was never removed. (Bug #12557307)

- Replication: A race condition could occur between a user thread and the SQL thread when both tried to

read the same memory before its value was safely set. This issue has now been corrected.

In addition, internal functions relating to creation of and appending to log events, when storing data, used memory local to the functions which was freed when the functions returned. As part of the fix for this problem, the output of `SHOW SLAVE STATUS` has been modified such that it no longer refers to files or file names in the accompanying status message, but rather contains one of the messages `Making`

```
temporary file (append) before replaying LOAD DATA INFILE or Making temporary
```

`file (create) before replaying LOAD DATA INFILE`. (Bug #12416611)

- Replication: The name of the `Ssl_verify_server_cert` column in the

`mysql.slave_master_info` table was misspelled as `Ssl_verify_servert_cert`. (Bug#12407446, Bug #60988)

- Replication: When `mysqlbinlog` was invoked using `--base64-output=decode-row` and `--`

`start-position=pos`, (where `pos` is a point in the binary log past the format description log event), a spurious error of the type shown here was generated:

```
malformed binlog: it does not contain any Format_description_log_event...
```

However, since there is nothing unsafe about not printing the format description log event, the error has been removed for this case. (Bug #12354268)

## MySQL 5.6 Release Notes

- Replication: A failed `CREATE USER` statement was mistakenly written to the binary log. (Bug

#11827392, Bug #60082)

- Replication: It is no longer possible to change the storage engine used by the

`mysql.slave_master_info` and `mysql.slave_relay_log_info` tables while replication is running. This means that, to make replication crash-safe, you must make sure that both of these tables use a transactional storage engine before starting replication.

For more information, see Relay Log and Replication Metadata Repositories, and Options for Logging Replica Status to Tables. (Bug #11765887, Bug #58897)

- Replication: A transaction was written to the binary log even when it did not update any

nontransactional tables. (Bug #11763471, Bug #56184)References: See also: Bug #11763126, Bug #55789.

- Replication: `mysqlbinlog` using the `--raw` option did not function correctly with binary logs from

MySQL Server versions 5.0.3 and earlier. (Bug #11763265, Bug #55956)

- Replication: Retrying a transaction on the slave could insert extra data into nontransactional tables.

(Bug #11763126, Bug #55789)References: See also: Bug #11763471, Bug #56184.

- Replication: Typographical errors appeared in the text of several replication error messages. (The word

“position” was misspelled as “postion”.) (Bug #11762616, Bug #55229)

- Replication: Temporary deadlocks in the slave SQL thread could cause unnecessary `Deadlock`

`found when trying to get lock; try restarting transaction` error messages to be logged on the slave.

Now in such cases, only a warning is logged unless `slave_transaction_retries` has been exceeded by the number of such warnings for a given transaction. (Bug #11748510, Bug #36524)

- Replication: When a slave requested a binary log file which did not exist on the master, the slave

continued to request the file regardless. This caused the slave's error log to be flooded with low-level`EE_FILENOTFOUND` errors (error code 29) from the master. (Bug #11745939, Bug #21437)

- Replication: If a `LOAD DATA` statement—replicated using statement-based replication—featured a `SET`

clause, the name-value pairs were regenerated using a method (`Item::print()`) intended primarily for generating output for statements such as `EXPLAIN EXTENDED`, and which cannot be relied on to return valid SQL. This could in certain cases lead to a crash on the slave.

To fix this problem, the server now names each value in its original, user-supplied form, and uses that to create `LOAD DATA` statements for statement-based replication. (Bug #60580, Bug #11902767)References: See also: Bug #34283, Bug #11752526, Bug #43746.

- Replication: Error 1590 (`ER_SLAVE_INCIDENT`) caused the slave to stop even when it was started with

`--slave-skip-errors=1590`. (Bug #59889, Bug #11768580, Bug #11799671)

- Replication: Using the `--server-id` option with `mysqlbinlog` could cause format description log

events to be filtered from the binary log, leaving `mysqlbinlog` unable to read the remainder of the log.

Now such events are always read without regard to the value of this option.

As part of the fix for this problem, `mysqlbinlog` now also reads rotate log events without regard to the value of `--server-id`. (Bug #59530, Bug #11766427)

## MySQL 5.6 Release Notes

- Replication: A failed `DROP DATABASE` statement could break statement-based replication. (Bug

#58381, Bug #11765416)

- Replication: Processing of corrupted table map events could cause the server to crash. This was

especially likely if the events mapped different tables to the same identifier, such as could happen due to Bug #56226.

Now, before applying a table map event, the server checks whether the table has already been mapped with different settings, and if so, an error is raised and the slave SQL thread stops. If it has been mapped with the same settings, or if the table is set to be ignored by filtering rules, there is no change in behavior: the event is skipped and IDs are not checked. (Bug #44360, Bug #11753004)References: See also: Bug #56226, Bug #11763509.

- OS X: Compilation failed on OS X 10.7 (Lion) with a warning: `Implicit declaration of`

`function 'pthread_init'` (Bug #12779790)

- Microsoft Windows: Adding support for Windows authentication to `libmysqlclient` introduced a link

dependency on the system Secur32 library. The Microsoft Visual C++ link information now pulls in this library automatically. (Bug #12612143)

- Microsoft Windows: On Windows, the server rejected client connections if no DNS server was

available. (Bug #12325375)

- Microsoft Windows: On Windows, the `authentication_string` column recently added to the

`mysql.user` table caused the Configuration Wizard to fail. (Bug #59038, Bug #11766011)

- The Performance Schema caused a bottleneck for `LOCK_open`. (Bug #12993572)
- `mysqld_safe` ignored any value of `plugin_dir` specified in `my.cnf` files. (Bug #12925024)
- The metadata locking subsystem added too much overhead for `INFORMATION_SCHEMA` queries that

were processed by opening only `.frm` or `.TRG` files and had to scan many tables. For example, `SELECT``COUNT(*) FROM INFORMATION_SCHEMA.TRIGGERS` was affected. (Bug #12828477)

- The result for `ANY` subqueries with nested joins could be missing rows. (Bug #12795555)
- With profiling disabled or not compiled in, `set_thd_proc_info()` unnecessarily checked file name

lengths. (Bug #12756017)References: This issue is a regression of: Bug #59273.

- Compiling the server with maintainer mode enabled failed for `gcc` 4.6 or higher. (Bug #12727287)
- For prepared statements, an `OK` could be sent to the client if the prepare failed due to being killed. (Bug

#12661349)

- Some Valgrind warnings were corrected:
- For the `SUBSTRING()`, `LEFT()`, `RIGHT()`, `LPAD()`, `RPAD()`, and `REPEAT()` functions, a missing

`NULL` value check was corrected.

- For the `LIKE` operator, an attempt to use an uninitialized string buffer in the case of an empty wildcard

was corrected.

(Bug #12634989, Bug #59851, Bug #11766684)

- For debug builds, a field-type check raised an assertion if the type was `MYSQL_TYPE_NULL`. (Bug

#12620084)

## MySQL 5.6 Release Notes

- With index condition pushdown enabled, a crash could occur due to an invalid end-of-range value. (Bug

#12601961)

- The option-parsing code for empty strings leaked memory. (Bug #12589928)
- The server could fail to free allocated memory when `INSERT DELAYED` was used with binary logging

enabled. (Bug #12538873)

- A `DBUG_ASSERT` added by Bug #11792200 was overly aggressive in raising assertions. (Bug

#12537160)References: See also: Bug #11792200.

- In some cases, memory allocated for `Query_tables_list::sroutines()` was not freed properly.

(Bug #12429877)

- After the fix for Bug #11889186, `MAKEDATE()` arguments with a year part greater than 9999 raised an

assertion. (Bug #12403504)References: This issue is a regression of: Bug #11889186.

- An assertion could be raised due to a missing `NULL` value check in

`Item_func_round::fix_length_and_dec()`. (Bug #12392636)

- Assignments to `NEW.var_name` within triggers, where `var_name` had a `BLOB` or `TEXT` type, were not

properly handled and produced incorrect results. (Bug #12362125)

- An assertion could be raised if Index Condition Pushdown code pushed down an index condition

containing a subquery. (Bug #12355958)

- `XA COMMIT` could fail to clean up the error state if it discovered that the current XA transaction had to be

rolled back. Consequently, the next XA transaction could raise an assertion when it checked for proper cleanup of the previous transaction. (Bug #12352846)

- An assertion could be raised during two-phase commits if the binary log was used as the transaction

coordinator log. (Bug #12346411)

- `InnoDB` could add temporary index information to `INFORMATION_SCHEMA`, which could raise an

assertion. (Bug #12340873)

- `mysql_list_fields()` returned incorrect character set information for character columns of views.

(Bug #12337762)

- A too-strict assertion could cause a server crash. (Bug #12321461)
- `mysql_upgrade` did not properly upgrade the `authentication_string` column of the `mysql.user`

table. (Bug #11936829)

- The optimizer sometimes chose a forward index scan followed by a filesort to reverse the order rather

than scanning the index in reverse order. (Bug #11882131)

- Previously, an inappropriate error message was produced if a multiple-table update for an `InnoDB`

table with a clustered primary key would update a table through multiple aliases, and perform an update that may physically move the row in at least one of these aliases. Now the error message is: `Primary`

```
key/partition key update is not permitted since the table is updated both as
```

`'tbl_name1' and 'tbl_name2'` (Bug #11882110)References: See also: Bug #11764529.

## MySQL 5.6 Release Notes

- With index condition pushdown enabled, queries that used `STRAIGHT_JOIN` on data that included `NULL`

values could return incorrect results. (Bug #11873324)

- `InnoDB` invoked some `zlib` functions without proper initialization. (Bug #11849231)
- Division of large numbers could cause stack corruption. (Bug #11792200)
- Corrected a condition that produced an `InnoDB` message in the error log, `unlock row could not`

`find a 3 mode lock on the record`. This situation could occur with a combination of a subquery and a `FOR UPDATE` clause under the `READ UNCOMMITTED` isolation level. The fix also improves the debuggability of such messages by including the original SQL statements that caused them. (Bug#11766322, Bug #59410)

- With Valgrind enabled, `InnoDB` semaphore wait timeouts were too low and could expire. (Bug

#11765460)

- `CHECK TABLE` and `REPAIR TABLE` failed to find problems with `MERGE` tables that had underlying tables

missing or with the wrong storage engine. Issues were reported only for the first underlying table. (Bug#11754210)

- `(5 DIV 2)` and `(5.0 DIV 2)` produced different results (2 versus 3) because the result of the latter

expression was not truncated before conversion to integer. This differed from the behavior in MySQL 5.0 and 5.1. Now both expressions produce 2. (Bug #61676, Bug #12711164)

- The server failed to compile if partitioning support was disabled. (Bug #61625, Bug #12694147)
- `ALTER TABLE {MODIFY|CHANGE} ... FIRST` did nothing except rename columns if the old and new

versions of the table had exactly the same structure with respect to column data types. As a result, the mapping of column name to column data was incorrect. The same thing happened for `ALTER TABLE``DROP COLUMN ... ADD COLUMN` statements intended to produce a new version of the table with exactly the same structure as the old version. (Bug #61493, Bug #12652385)

- Incorrect handling of metadata locking for `FLUSH TABLES WITH READ LOCK` for statements requiring

prelocking caused two problems:

- Execution of any data-changing statement that required prelocking (that is, involved a stored

function or trigger) as part of a transaction slowed down somewhat all subsequent statements in the transaction. Performance in a transaction that periodically involved such statements gradually degraded over time.

- Execution of any data-changing statement that required prelocking as part of a transaction prevented

a concurrent `FLUSH TABLES WITH READ LOCK` from proceeding until the end of the transaction rather than at the end of the particular statement.

(Bug #61401, Bug #12641342)

- A problem introduced in MySQL 5.5.11 caused very old (MySQL 4.0) clients to be unable to connect to

the server. (Bug #61222, Bug #12563279)

- The fractional part of the “Queries per second” value could be displayed incorrectly in MySQL status

output (for example, in the output from `mysqladmin status` or the `mysql` `STATUS` command). (Bug#61205, Bug #12565712)

- The `mysql-log-rotate` script was updated because it referred to deprecated MySQL options. (Bug

#61038, Bug #12546842)

- Using `CREATE EVENT IF NOT EXISTS` for an event that already existed and was enabled caused

multiple instances of the event to run. (Bug #61005, Bug #12546938)

## MySQL 5.6 Release Notes

- If a statement ended with mismatched quotes, the server accepted the statement and interpreted

whatever was after the initial quote as a text string. (Bug #60993, Bug #12546960)

- `LOAD DATA` incorrectly parsed relative data file path names that ascended more than three levels in the

file system and as a consequence was unable to find the file. (Bug #60987, Bug #12403662)

- Fixed “shift count greater than width of type” compilation warnings. (Bug #60908, Bug #12402772)

References: See also: Bug #12561303.

- Table I/O for the `table_io_waits_summary_by_index_usage` Performance Schema table was

counted as using no index for `UPDATE` and `DELETE` statements, even when an index was used. (Bug#60905, Bug #12370950)

- An internal client macro reference was removed from the `client_plugin.h` header file. This reference

made the file unusable. (Bug #60746, Bug #12325444)

- Comparison of a `DATETIME` stored program variable and `NOW()` resulted in “Illegal mix of collations

error” when `character_set_connection` was set to `utf8`. (Bug #60625, Bug #11926811)

- Selecting from a view for which the definition included a `HAVING` clause failed with an error:

```
1356: View '...' references invalid table(s) or column(s)
or function(s) or definer/invoker of view lack rights to use them
```

(Bug #60295, Bug #11829681)

- `CREATE TABLE` syntax permits specification of a `STORAGE {DEFAULT|DISK|MEMORY}` option.

However, this value was not written to the `.frm` file, so that a subsequent `CREATE TABLE ... LIKE`for the table did not include that option.

Also, `ALTER TABLE` of a table that had a tablespace incorrectly destroyed the tablespace. (Bug #60111,Bug #11766883, Bug #34047, Bug #11747789)

- The `mysql_load_plugin()` C API function did not clear the previous error. (Bug #60075, Bug

#11766854)

- For repeated invocation of some stored procedures, the server consumed memory that it did not release

until the connection terminated. (Bug #60025, Bug #11848763)

- The server permitted `max_allowed_packet` to be set lower than `net_buffer_length`, which does

not make sense because `max_allowed_packet` is the upper limit on `net_buffer_length` values.

Now a warning occurs and the value remains unchanged. (Bug #59959, Bug #11766769)

- The server did not check for certain invalid out of order sequences of XA statements, and these

sequences raised an assertion. (Bug #59936, Bug #11766752, Bug #12348348)

- Index condition pushdown code accessed an uninitialized variable. (Bug #59843, Bug #11766678)
- For unknown users, the native password plugin reported incorrectly that no password had been specified

even when it had. (Bug #59792, Bug #11766641)

- `SELECT DISTINCT` with a deterministic stored function in the `WHERE` clause could produce incorrect

results. (Bug #59736, Bug #11766594)

- Setting `optimizer_join_cache_level` to 3 or greater raised an assertion for some queries. (Bug

#59651, Bug #11766522)

## MySQL 5.6 Release Notes

- Previously, Performance Schema table columns that held byte counts were `BIGINT UNSIGNED`. These

were changed to `BIGINT` (signed). This makes it easier to perform calculations that compute differences between columns. (Bug #59631, Bug #11766504)

- A missing variable initialization for `Item_func_set_user_var` objects could raise an assertion. (Bug

#59527, Bug #11766424)

- For some queries, the optimizer performed range analysis too many times for the same index. (Bug

#59415, Bug #11766327)

- With the conversion from GNU autotools to `CMake` for configuring MySQL, the `USE_SYMDIR`

preprocessor symbol was omitted. This caused failure of symbolic links (described at Using Symbolic Links). (Bug #59408, Bug #11766320)

- An incorrect `max_length` value for `YEAR` values could be used in temporary result tables for `UNION`,

leading to incorrect results. (Bug #59343, Bug #11766270)

- In `Item_func_in::fix_length_and_dec()`, a Valgrind warning for uninitialized values was

corrected. (Bug #59270, Bug #11766212)

- An invalid pathname argument for the `--defaults-extra-file` option of MySQL programs caused a

program crash. (Bug #59234, Bug #11766184)

- In `Item_func_month::val_str()`, a Valgrind warning for a too-late `NULL` value check was

corrected. (Bug #59166, Bug #11766126)

- In `Item::get_date`, a Valgrind warning for a missing `NULL` value check was corrected. (Bug #59164,

Bug #11766124)

- In `extract_date_time()`, a Valgrind warning for a missing end-of-string check was corrected. (Bug

#59151, Bug #11766112)

- Some tables were not instrumented by the Performance Schema even though they were listed in the

`setup_objects` table. (Bug #59150, Bug #11766111)

- In string context, the `MIN()` and `MAX()` functions did not take into account the unsignedness of a

`BIGINT UNSIGNED` argument. (Bug #59132, Bug #11766094)

- In `Item_func::val_decimal`, a Valgrind warning for a missing `NULL` value check was corrected.

(Bug #59125, Bug #11766087)

- In `ROUND()` calculations, a Valgrind warning for uninitialized memory was corrected. (Bug #58937, Bug

#11765923)References: This issue is a regression of: Bug #33143.

- The range created by the optimizer when OR-ing two conditions could be incorrect, causing incorrect

query results. (Bug #58834, Bug #11765831)

- Valgrind warnings caused by comparing index values to an uninitialized field were corrected. (Bug

#58705, Bug #11765713)

- As a side effect of optimizing `condition AND TRUE` or `condition OR FALSE`, MySQL for certain

subqueries forgot that the columns used by the condition needed to be read, which raised an assertion in debug builds. (Bug #58690, Bug #11765699)

- `CREATE TRIGGER` and `DROP TRIGGER` can change the prelocking list of stored routines, but the routine

cache did not detect such changes, resulting in routine execution with an inaccurate locking list. (Bug#58674, Bug #11765684)

## MySQL 5.6 Release Notes

- In `Item_func_str_to_date::val_str`, a Valgrind warning for an uninitialized variable was

corrected. (Bug #58154, Bug #11765216)

- The code for `PROCEDURE ANALYSE()` had a missing `DBUG_RETURN` statement, which could cause a

server crash in debug builds. (Bug #58140, Bug #11765202)

- `LOAD DATA` errors could leak I/O cache memory. (Bug #58072, Bug #11765141)
- For `LOAD DATA`, multibyte character sequences could be pushed onto a stack too small to

accommodate them. (Bug #58069, Bug #11765139)

- The embedded server crashed when `argc = 0`. (Bug #57931, Bug #12561297)
- An assertion could be raised in `Item_func_int_val::fix_num_length_and_dec()` due to

overflow for geometry functions. (Bug #57900, Bug #11764994)

- An assertion was raised if a statement tried to upgrade a metadata lock while there was an active `FLUSH`

`TABLE tbl_list WITH READ LOCK` statement. Now if a statement tries to upgrade a metadata lock in this situation, the server returns an `ER_TABLE_NOT_LOCKED_FOR_WRITE` error to the client. (Bug#57649, Bug #11764779)

- The optimizer sometimes requested ordered access from a storage engine when ordered access was

not required. (Bug #57601, Bug #11764737)

- An embedded client aborted rather than issuing an error message if it issued a `TEE` command (`\T`

`file_name`) and the directory containing the file did not exist. This occurred because the wrong error handler was called. (Bug #57491, Bug #11764633)

- `ALTER EVENT` could change the event status. (Bug #57156, Bug #11764334)
- For an outer join with a `NOT IN` subquery in the `WHERE` clause, a null left operand to the `NOT IN`

returned was treated differently than a literal `NULL` operand. (Bug #56881, Bug #11764086)

- Threads blocked in the `waiting for table metadata` state were not visible in

`performance_schema.THREADS` or `SHOW PROFILE`. (Bug #56475, Bug #11763728)

- With prepared statements, the server could attempt to send result set metadata after the table had been

closed. (Bug #56115, Bug #11763413)

- Table objects associated with one session's optimizer structures could be closed after being passed

to another session, prematurely ending the second session's table or index scan. (Bug #56080, Bug#11763382)

- In some cases, `SHOW WARNINGS` returned an empty result when the previous statement failed. (Bug

#55847, Bug #11763166)

- A handled condition (error or warning) could be shown as not handled at the end of the statement. (Bug

#55843, Bug #11763162)References: This issue is a regression of: Bug #23032.

- In debug builds, `Field_new_decimal::store_value()` was subject to buffer overflows. (Bug

#55436, Bug #11762799)

- For an `InnoDB` table, dropping and adding an index in a single `ALTER TABLE` statement could fail. (Bug

#54927, Bug #11762345)

- For a client connected using SSL, the `Ssl_cipher_list` status variable was empty and did not show

the possible cipher types. (Bug #52596, Bug #11760210)

## MySQL 5.6 Release Notes

- The `mysql` client sometimes did not properly close sessions terminated by the user with Control+C.

(Bug #52515, Bug #11760134)

- `CREATE TABLE ... LIKE` for a `MyISAM` table definition that included an `DATA DIRECTORY` or `INDEX`

`DIRECTORY` table option failed, instead of creating a table with those options omitted as documented.

(Bug #52354, Bug #11759990)

- Spatial operations on certain corner cases could cause a server crash: Polygons with zero-point

linerings; polygons with touching linerings. (Bug #51979, Bug #11759650, Bug #47429, Bug #11755628)

- Attempts to grant the `EXECUTE` or `ALTER ROUTINE` privilege for a nonexistent stored procedure

returned success instead of an error. (Bug #51401, Bug #11759114)

- With `lower_case_table_names=2`, resolution of objects qualified by database names could fail. (Bug

#50924, Bug #11758687)

- `CREATE TABLE` without an `ENGINE` option determined the default engine at parse rather than execution

time. This led to incorrect results if the statement was executed within a stored program and the default engine had been changed in the meantime. (Bug #50614, Bug #11758414)

- On Linux, the `mysql` client built using the bundled `libedit` did not read `~/.editrc`. (Bug #49967,

Bug #11757855)

- For some statements such as `DESCRIBE` or `SHOW`, views with too many columns produced errors. (Bug

#49437, Bug #11757397)

- The optimizer sometimes incorrectly processed `HAVING` clauses for queries that did not also have an

`ORDER BY` clause. (Bug #48916, Bug #11756928)

- `PROCEDURE ANALYSE()` could leak memory for `NULL` results, and could return incorrect results if used

with a `LIMIT` clause. (Bug #48137, Bug #11756242)

- A race condition between loading a stored routine using the name qualified by the database name

and dropping that database resulted in a spurious error message: `The table mysql.proc is``missing, corrupt, or contains bad data` (Bug #47870, Bug #11756013)

- When used to upgrade tables, `mysqlcheck` (and `mysql_upgrade`, which invokes `mysqlcheck`)

did not upgrade some tables for which table repair was found to be necessary. In particular, it failed to upgrade `InnoDB` tables that needed repair, leaving them in a nonupgraded state. This occurred because:

- `mysqlcheck --check-upgrade ---auto-repair` checks for tables that are incompatible

with the current version of MySQL. It does this by issuing the `CHECK TABLE ... FOR UPGRADE`statement and examining the result.

- For any table found to be incompatible, `mysqlcheck` issues a `REPAIR TABLE` statement. But this

fails for storage engines such as `InnoDB` that do not support the repair operation. Consequently, the table remained unchanged.

To fix the problem, the following changes were made to `CHECK TABLE ... FOR UPGRADE` and`mysqlcheck`. Because `mysql_upgrade` invokes `mysqlcheck`, these changes also fix the problem for

```
mysql_upgrade.
```

- `CHECK TABLE ... FOR UPGRADE` returns a different error if a table needs repair but its storage

engine does not support `REPAIR TABLE`:Previous:

## MySQL 5.6 Release Notes

```
Error: ER_TABLE_NEEDS_UPGRADE
Table upgrade required. Please do "REPAIR TABLE `tbl_name`" or
dump/reload to fix it!
```

Now:

```
Error: ER_TABLE_NEEDS_REBUILD
Table rebuild required. Please do "ALTER TABLE `tbl_name` FORCE" or
dump/reload to fix it!
```

- `mysqlcheck` recognizes the new error and issues an `ALTER TABLE ... FORCE` statement. The

`FORCE` option for `ALTER TABLE` was recognized but did nothing; now it is implemented and acts as a“null” alter operation that rebuilds the table.

(Bug #47205, Bug #11755431)

- On some platforms, the `Incorrect value: xxx for column yyy at row zzz` error produced

by `LOAD DATA` could have an incorrect value of `zzz`. (Bug #46895, Bug #11755168)

- Upgrades using an RPM package recreated the `test` database, which is undesirable when the DBA had

removed it. (Bug #45415, Bug #11753896)

- In MySQL 5.1 and up, if a table had triggers that used syntax supported in 5.0 but not 5.1, the table

became unavailable. Now the table is marked as having broken triggers. These should be dropped and recreated manually. (Bug #45235, Bug #11753738)

- An attempt to install nonexistent files during installation was corrected. (Bug #43247, Bug #11752142)
- Some status variables rolled over to zero after reaching the maximum 32-bit value. They have been

changed to 64-bit values. (Bug #42698, Bug #11751727)

- `SHOW EVENTS` did not always show events from the correct database. (Bug #41907, Bug #11751148)
- For queries with many `eq_ref` joins, the optimizer took excessive time to develop an execution plan.

(Bug #41740, Bug #11751026, Bug #58225, Bug #11765274)

- On FreeBSD 64-bit builds of the embedded server, exceptions were not prevented from propagating into

the embedded application. (Bug #38965, Bug #11749418)

- With `DISTINCT`, `CONCAT(col_name,...)` returned incorrect results when the arguments to

`CONCAT()` were columns with an integer data type declared with a display width narrower than the values in the column. (For example, if an `INT(1)` column contained 1111.) (Bug #4082)
