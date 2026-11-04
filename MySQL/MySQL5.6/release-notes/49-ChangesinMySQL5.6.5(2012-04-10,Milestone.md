---
title: "Changes in MySQL 5.6.5 (2012-04-10, Milestone 8)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=214"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Note This is a milestone release, for use at your own risk. Upgrades between milestone releases (or from a milestone release to a GA release) are not supported.

Significant development changes take place in milestone releases and you may encounter compatibility issues, such as data format changes that require attention in addition to the usual procedure of running `mysql_upgrade`. For example, you may find it necessary to dump your data with `mysqldump` before the upgrade and reload it afterward. (Making a backup before the upgrade is a prudent precaution in any case.)Beginning with MySQL 5.6.5, Oracle no longer provides binaries for OS X 10.5. This aligns with Apple no longer providing updates or support for this platform.

- Data Type Notes
- Replication with GTIDs
- Host Cache Notes
- Optimizer Notes
- Performance Schema Notes
- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> Data Type Notes

- Previously, at most one `TIMESTAMP` column per table could be automatically initialized or updated to the

current date and time. This restriction has been lifted. Any `TIMESTAMP` column definition can have any combination of `DEFAULT CURRENT_TIMESTAMP` and `ON UPDATE CURRENT_TIMESTAMP` clauses. In addition, these clauses now can be used with `DATETIME` column definitions. For more information, see Automatic Initialization and Updating for TIMESTAMP and DATETIME. (WL #5874)

> Replication with GTIDs

- Important Change; Replication: This release introduces global transaction identifiers (GTIDs) for

MySQL Replication. A GTID is a unique identifier that is assigned to each transaction as it is committed;

this identifier is unique on the MySQL Server where the transaction originated, as well as across all MySQL Servers in a given replication setup. Because GTID-based replication depends on tracking transactions, it cannot be employed with tables that employ a nontransactional storage engine such as`MyISAM`; thus, it is currently supported only with `InnoDB` tables.

Because each transaction is uniquely identified, it is not necessary when using GTIDs to specify positions in the master's binary log when starting a new slave or failing over to a new master. This is reflected in the addition of a new `MASTER_AUTO_POSITION` option for the `CHANGE MASTER TO`

## MySQL 5.6 Release Notes

statement which takes the place of the `MASTER_LOG_FILE` and `MASTER_LOG_POS` options when executing this statement to prepare a MySQL Server to act as a replication slave.

To enable GTIDs on a MySQL Server, the server must be started with the options `--gtid-mode=ON`

```
--disable-gtid-unsafe-statements --log-bin --log-slave-updates. These options are
```

needed whether the server acts as a replication master or as a replication slave; the `--gtid-mode` and`--disable-gtid-unsafe-statements` options are new in this release. Once the master and slave have each been started with these options, it is necessary only to issue a `CHANGE MASTER TO ...``MASTER_AUTO_POSITION=1` followed by `START SLAVE` on the slave to start replication.

A number of new server system variables have also been added for monitoring GTID usage. For more information about these options and variables, see Global Transaction ID Options and Variables.

As part of these changes, three new `mysqlbinlog` options—`--include-gtids`, `--exclude-gtids`,and `--skip-gtids`—have been added for reading binary logs produced when the server participates in replication with GTIDs.

Important Due to an issue discovered just prior to release, you cannot import a dump made using `mysqldump` from a MySQL 5.5 server to a MySQL 5.6.5 server and then use `mysqlupgrade` on the MySQL 5.6.5 server while GTIDs are enabled; doing so makes it impossible to connect to the server normally following the upgrade.

Instead, you should import the dump and run `mysqlupgrade` while the MySQL

5.6.5 server is running with `--gtid-mode=OFF`, then restart it with `--gtid-``mode=ON`. (Bug #13833710) (`mysqlupgrade` can be executed when the server is running with `--gtid-mode` set either to `OFF`, or to `ON`.)For additional information about GTIDs and setting up GTID-based replication, see Replication with Global Transaction Identifiers. (WL #3584)

> Host Cache Notes

- MySQL now provides improved access to the host cache, which contains client IP address and host

name information and is used to avoid DNS lookups, as well as more information about the causes of errors that occur when clients connect to the server. These changes have been implemented:

- A new Performance Schema `host_cache` table exposes the contents of the host cache so that it

can be examined using `SELECT` statements. Access to host cache contents makes it possible to answer questions such as how many hosts are cached, what kinds of connection errors are occurring for which hosts, or how close host error counts are to reaching the `max_connect_errors` system variable limit. The Performance Schema must be enabled or this table is empty.

If you upgrade to this MySQL release from an earlier version, you must run `mysql_upgrade` (and restart the server) to incorporate this change into the `performance_schema` database.

- The host cache has additional counters to track errors that do apply to specific IP addresses.
- The host cache size now is configurable using the `host_cache_size` system variable. This variable

also controls the maximum size of the `host_cache` table because that table is the cache visible representation. Setting the size to 0 disables the host cache. This is similar to disabling the cache by starting the server with `--skip-host-cache`, but using `host_cache_size` is more flexible because it can also be used to resize, enable, and disable the host cache at runtime, not just at server startup. If you start the server with `--skip-host-cache`, the host cache cannot be re-enabled at runtime.

## MySQL 5.6 Release Notes

- New `Connection_errors_xxx` status variables provide information about connection errors that do

not apply to specific client IP addresses.

For more information, see DNS Lookups and the Host Cache, and The host_cache Table. (Bug #22821,Bug #24906, Bug #45817, Bug #59404, Bug #11746048, Bug #11746269, Bug #11754244, Bug#11766316, WL #5259)

> Optimizer Notes

- Reporting of how to sort a result set in `EXPLAIN` has been improved for some statements. This sorting

decision could be reported incorrectly, causing `Using filesort` or `Using temporary` to be reported when they should not have been or vice versa. This could occur for statements that included index hints,that had the form `SELECT SQL_BIG_RESULT ... GROUP BY`, that used `SQL_CALC_FOUND_ROWS`with `LIMIT`, or that used `GROUP BY`, `ORDER BY`, and `LIMIT`. (Bug #11744768, Bug #1560, WL #5558)

- These query optimizer improvements were implemented:
- The `EXPLAIN` statement now can produce output in JSON format. To select this, use `EXPLAIN`

`FORMAT = JSON explainable_stmt` syntax. With `FORMAT = JSON`, the output includes regular`EXPLAIN` information, as well as extended and partition information.

Traditional `EXPLAIN` output has also changed so that empty columns contain `NULL` rather the empty string. In addition, `UNION RESULT` rows have `Using filesort` in the `Extra` column because a temporary table is used to buffer `UNION` results.

To work for both Optimizer Trace and JSON-format `EXPLAIN` output, the `end_marker` parameter for the `optimizer_trace` system variable has been moved to a separate `end_markers_in_json`system variable. This is an incompatible change to the `optimizer_trace` variable. For more information, see MySQL Internals: Tracing the Optimizer.

- The optimizer tries to find the best query execution plan by beginning with the most promising table

and recursively adding to the plan the most promising of the remaining tables. Partial execution plans with a higher cost than an already found plan are pruned. The optimizer now attempts to improve the order in which it adds tables to the plan, resulting in a reduction of the number of partial plans considered.

Queries that are likely to have improved performance are joins of many tables, where most tables use`eq_ref` or `ref` join types (as indicated by `EXPLAIN` output).

A new status variable, `Last_query_partial_plans`, counts the number of iterations the optimizer makes in execution plan construction for the previous query.

- The optimizer uses semijoin and materialization strategies to optimize subquery execution. See

Optimizing Subqueries with Semijoin Transformations, and Optimizing Subqueries with Materialization.

In addition, the Batched Key Access (BKA) Join and Block Nested-Loop (BNL) Join algorithms used for inner join and outer join operations have been extended to support semijoin operations. For more information, see Block Nested-Loop and Batched Key Access Joins.

Several flags have been added to the `optimizer_switch` system variable to enable control over semijoin and subquery materialization strategies. The `semijoin` flag controls whether semijoins are used. If it is set to `on`, the `firstmatch` and `loosescan` flags enable finer control over the permitted semijoin strategies. The `materialization` flag controls whether subquery materialization is used. If`semijoin` and `materialization` are both `on`, semijoins also use materialization where applicable.

These flags are `on` by default. See Switchable Optimizations.

## MySQL 5.6 Release Notes

- For expressions such as `col_name IN(values)` that compare a column to a list of values, the

optimizer previously made row estimates using index dives for each value in the list. This becomes inefficient as the number of values becomes large. The optimizer now can make row estimates for such expressions using index statistics instead, which is less accurate but quicker for a large number of values. The point at which the optimizer switches from index dives to index statistics is configurable using the new `eq_range_index_dive_limit` system variable. For more information, see Equality Range Optimization of Many-Valued Comparisons.

(WL #5729, WL #5855, WL #5957, WL #6158)

> Performance Schema Notes

- The Performance Schema has these additions:
- The Performance Schema now has a `host_cache` table that exposes the contents of the host

cache so that it can be examined using `SELECT` statements. See Host Cache Notes elsewhere in this changelog.

- The Performance Schema now maintains statement digest information. This normalizes and groups

statements with the same “signature” and permits questions to be answered about the types of statements the server is executing and how often they occur.

- A `statement_digest` consumer in the `setup_consumers` table controls whether the

Performance Schema maintains digest information.

- The statement event tables (`events_statements_current`, `events_statements_history`,

and `events_statements_history_long`) have `DIGEST` and `DIGEST_TEXT` columns that contain digest MD5 values and the corresponding normalized statement text strings.

- A `events_statements_summary_by_digest` table provides aggregated statement digest

information.

For more information, see The host_cache Table, Performance Schema Statement Event Tables, and Statement Summary Tables.

If you upgrade to this MySQL release from an earlier version, you must run `mysql_upgrade` (and restart the server) to incorporate these changes into the `performance_schema` database. (WL #5767)

> Security Notes

- Passwords stored in the older hash format used before MySQL 4.1 are less secure than passwords

that use the native password hashing method and should be avoided. Pre-4.1 passwords and the`mysql_old_password` authentication plugin are now deprecated. To prevent connections using accounts that have pre-4.1 password hashes, the `secure_auth` system variable is now enabled by default. (To permit connections for accounts that have such password hashes, start the server with `--``secure_auth=0`.) (Bug #13586336)

- MySQL client programs now issue a warning if a password is given on the command line that this can be

insecure.

> Functionality Added or Changed

- Incompatible Change: The obsolete `OPTION` modifier for the `SET` statement has been removed. (WL

#5185, WL #6311)

## MySQL 5.6 Release Notes

- InnoDB: `--ignore-builtin-innodb` is now ignored if used. (Bug #13586262)
- OS X; Microsoft Windows: A new `CMake` option, `MYSQL_PROJECT_NAME`, can be set on Windows or

OS X to be used in the project name. (Bug #13551687)

- Microsoft Windows: A new server option, `--slow-start-timeout`, controls the Windows service

control manager's service start timeout. The value is the maximum number of milliseconds that the service control manager waits before trying to kill the MySQL service during startup. The default value is 15000 (15 seconds). If the MySQL service takes too long to start, you may need to increase this value. A value of 0 means there is no timeout. (Bug #45546, Bug #11754011)

- The `MySQL-shared-compat` RPM package enables users of Red Hat-provided `mysql-*-5.1` RPM

packages to migrate to Oracle-provided `MySQL-*-5.5` packages. `MySQL-shared-compat` now replaces the Red Hat `mysql-libs` package by replacing `libmysqlclient.so` files of the latter package, thus satisfying dependencies of other packages on `mysql-libs`. This change affects only users of Red Hat (or Red Hat-compatible) RPM packages. Nothing is different for users of Oracle RPM packages. (Bug #13867506)

- Temporary tables for `INFORMATION_SCHEMA` queries now use dynamic `MyISAM` row format if they

contain sufficiently large `VARCHAR` columns, resulting in space savings. (Bug #13627632)

- As of MySQL 5.5.3, the `LOW_PRIORITY` modifier for `LOCK TABLES ... LOW_PRIORITY WRITE` has

no effect. This modifier is now deprecated. Its use should be avoided and now produces a warning. Use`LOCK TABLES ... WRITE` instead. (Bug #13586314)

- If the `log_queries_not_using_indexes` system variable is enabled, slow queries that do not use

indexes are written to the slow query log. In this case, it is now possible to put a logging rate limit on these queries by setting the new `log_throttle_queries_not_using_indexes` system variable,so that the slow query log does not grow too quickly. By default, this variable is 0, which means there is no limit. Positive values impose a per-minute limit on logging of queries that do not use indexes. The first such query opens a 60-second window within which the server logs queries up to the given limit,then suppresses additional queries. If there are suppressed queries when the window ends, the server logs a summary that indicates how many there were and the aggregate time spent in them. The next 60-second window begins when the server logs the next query that does not use indexes. (Bug #55323,Bug #11762697)

- Several subquery performance issues were resolved through the implementation of semijoin subquery

optimization strategies. See Optimizing Subqueries with Semijoin Transformations. (Bug #47914, Bug#11756048, Bug #58660, Bug #11765671, Bug #10815, Bug #11745162, Bug #9021, Bug #13519134,Bug #48763, Bug #11756798, Bug #25130, Bug #11746289)

- The `mysql` client now supports an `--init-command=str` option. The option value is an SQL

statement to execute after connecting to the server. If auto-reconnect is enabled, the statement is executed again after reconnection occurs. (Bug #45634, Bug #11754087)

- New `utf8_general_mysql500_ci` and `ucs2_general_mysql500_ci` collations have been

added that preserve the behavior of `utf8_general_ci` and `ucs2_general_ci` from versions of MySQL previous to 5.1.24. Bug #27877 corrected an error in the original collations but introduced an incompatibility for columns that contain German `'ß'` LATIN SMALL LETTER SHARP S. (As a result of the fix, that character compares equal to characters with which it previously compared different.) A symptom of the problem after upgrading to MySQL 5.1.24 or newer from a version older than 5.1.24 is that `CHECK TABLE` produces this error:

```
Table upgrade required.
```

## MySQL 5.6 Release Notes

```
Please do "REPAIR TABLE `t`" or dump/reload to fix it!
```

Unfortunately, `REPAIR TABLE` could not fix the problem. The new collations permit older tables created before MySQL 5.1.24 to be upgraded to current versions of MySQL.

To convert an affected table after a binary upgrade that leaves the table files in place, alter the table to use the new collation. Suppose that the table `t1` contains one or more problematic `utf8` columns. To convert the table at the table level, use a statement like this:

```
ALTER TABLE t1
CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci;
```

To apply the change on a column-specific basis, use a statement like this (be sure to repeat the column definition as originally specified except for the `COLLATE` clause):

```
ALTER TABLE t1
MODIFY c1 CHAR(N) CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci;
```

To upgrade the table using a dump and reload procedure, dump the table using `mysqldump`, modify the`CREATE TABLE` statement in the dump file to use the new collation, and reload the table.

After making the appropriate changes, `CHECK TABLE` should report no error. (Bug #43593, Bug#11752408)References: See also: Bug #27877.

- The `SET TRANSACTION` and `START TRANSACTION` statements now support `READ WRITE` and `READ`

`ONLY` modifiers to set the transaction access mode for tables used in transactions. The default mode is read/write, which is the same mode as previously. Read/write mode now may be specified explicitly with the `READ WRITE` modifier. Using `READ ONLY` prohibits table changes and may enable storage engines to make performance improvements that are possible when changes are not permitted.

In addition, the new `--transaction-read-only` option and `tx_read_only` system variable permit the default transaction access mode to be set at server startup and runtime.

For more information, see SET TRANSACTION Statement, and START TRANSACTION, COMMIT, and ROLLBACK Statements. (WL #5968)

- MySQL distributions no longer include the GPL `readline` input-editing library. This results in simpler

maintenance and support, and simplifies licensing considerations.

> Bugs Fixed

- Incompatible Change; Replication: `CHANGE MASTER TO` statements were written into the error log

using quoted numeric values, although the syntax for this statement does not allow such option values to be quoted. This meant that such statements could not be copied from the error log and re-run verbatim.

Now `CHANGE MASTER TO` statements are written to the error log without the extraneous quotation marks, and so are syntactically correct as logged.

- Incompatible Change: A change in MySQL 5.6.3 caused `LAST_DAY()` to be more strict and reject

incomplete dates with a day part of zero. For this function, a nonzero day part is not necessary, so the change has been reverted. (Bug #13458237)

- Important Change; InnoDB: When a row grew in size due to an `UPDATE` operation, other (non-

updated) columns could be moved to off-page storage so that information about the row still fit within the constraints of the `InnoDB` page size. The pointer to the new allocated off-page data was not set up until the pages were allocated and written, potentially leading to lost data if the system crashed while the column was being moved out of the page. The problem was more common with tables using

## MySQL 5.6 Release Notes

`ROW_FORMAT=DYNAMIC` or `ROW_FORMAT=COMPRESSED` along with the Barracuda file format, particularly with the `innodb_file_per_table` setting enabled, because page allocation operations are more common as the `.ibd` tablespace files are extended. Still, the problem could occur with any combination of InnoDB version, file format, and row format.

A related issue was that during such an `UPDATE` operation, or an `INSERT` operation that reused a delete-marked record, other transactions could see invalid data for the affected column, regardless of isolation level.

The fix corrects the order of operations for moving the column data off the original page and replacing it with a pointer. Now if a crash occurs at the precise moment when the column data is being transferred,the transfer will not be re-run during crash recovery.

In MySQL 5.1, this fix applies to the InnoDB Plugin, but not the built-in InnoDB storage engine. (Bug#13721257, Bug #12612184, Bug #12704861)

- Important Change; Partitioning: The query cache did not always function correctly with partitioned

tables in a transactional context. For this reason, the query cache is now disabled for any queries using partitioned tables, and such queries can no longer be cached. For more information, see Restrictions and Limitations on Partitioning. (Bug #11761296, Bug #53775)

- Important Change; Replication: The `CHANGE MASTER TO` statement was not checked for invalid

characters in values for options such as `MASTER_HOST` and `MASTER_USER`. In addition, when the server was restarted, a value containing certain characters was trimmed, causing the loss of its original value. Now such values are validated, and in cases where the value contains invalid characters,including linefeed (`\n` or `0x0A`) characters, the statement fails with an error (`ER_MASTER_INFO`). (Bug#11758581, Bug #50801)

- Important Change; Replication: Moving the binary log file, relay log file, or both files to a new location,

then restarting the server with a new value for `--log-bin`, `--relay-log`, or both, caused the server to abort on start. This was because the entries in the index file overrode the new location. In addition, paths were calculated relative to datadir (rather than to the `--log-bin` or `--relay-log` values).

The fix for this problem means that, when the server reads an entry from the index file, it now checks whether the entry contains a relative path. If it does, the relative part of the path is replaced with the absolute path set using the `--log-bin` or `--relay-log` option. An absolute path remains unchanged;

in such a case, the index must be edited manually to enable the new path or paths to be used. (Bug#11745230, Bug #12133)

- Performance; InnoDB: The optimizer now takes into account `InnoDB` page sizes other than 16KB,

which can be configured with the `innodb_page_size` option when creating a MySQL instance. This change improves the estimates of I/O costs for queries on systems with non-default `InnoDB` page sizes.

(Bug #13623078)

- Performance; InnoDB: Memory allocation for `InnoDB` tables was reorganized to reduce the memory

overhead for large numbers of tables or partitions, avoiding situations where the “resident set size” could grow regardless of `FLUSH TABLES` statements. The problem was most evident for tables with large row size. Some of the memory that was formerly allocated for every open table is now allocated only when the table is modified for the first time. (Bug #11764622, Bug #57480)

- Performance: Temporary `MyISAM` tables (unlike normal `MyISAM` tables) did not use the dynamic row

format when they contained `VARCHAR` columns, resulting in larger temporary files (and more file I/O) than necessary. Dynamic row format now is used, which results in smaller tables that are faster to process.

(Bug #13350136, Bug #78840, Bug #22023218)

- InnoDB: An erroneous assertion could occur, in debug builds only, when creating an index on a column

containing zero-length values (that is, `''`). (Bug #13654923)

## MySQL 5.6 Release Notes

- InnoDB: A DDL operation such as `ALTER TABLE ... ADD COLUMN` could stall, eventually timing out

with an `Error 1005: Can't create table` message referring to `fil_rename_tablespace`.

(Bug #13636122, Bug #62100, Bug #63553)

- InnoDB: If InnoDB was started with `innodb_force_recovery` set to a value of 3 or 4, and there are

transactions to roll back, normal shutdown would hang waiting for those transactions to complete. Now the shutdown happens immediately, without rolling back any transactions, because nonzero values for`innodb_force_recovery` are only appropriate for troubleshooting and diagnostic purposes. (Bug#13628420)

- InnoDB: The MySQL server could hang in some cases if the configuration option

`innodb_use_native_aio` was turned off. (Bug #13619598)

- InnoDB: A Valgrind error was fixed in the function `os_aio_init()`. (Bug #13612811)
- InnoDB: The configuration option `innodb_sort_buf_size` was renamed to

`innodb_sort_buffer_size` for consistency. This work area is used while creating an `InnoDB` index.

(Bug #13610358)

- InnoDB: The server could crash when creating an `InnoDB` temporary table under Linux, if the `$TMPDIR`

setting points to a `tmpfs` filesystem and `innodb_use_native_aio` is enabled, as it is by default in MySQL 5.5.4 and higher. The entry in the error log looked like:

```
101123  2:10:59  InnoDB: Operating system error number 22 in a file operation.
InnoDB: Error number 22 means 'Invalid argument'.
```

The crash occurred because asynchronous I/O is not supported on tmpfs in some Linux kernel versions.

The workaround was to turn off the `innodb_use_native_aio` setting or use a different temporary directory. The fix causes `InnoDB` to turn off the `innodb_use_native_aio` setting automatically if it detects that the temporary file directory does not support asynchronous I/O. (Bug #13593888, Bug#11765450, Bug #58421)

- InnoDB: During startup, the status variable `Innodb_buffer_pool_dump_status` could be empty for

a brief time before being initialized to the correct value `not started`. (Bug #13513676)

- InnoDB: Valgrind errors when referencing the internal function `buf_LRU_scan_and_free_block()`

were fixed. (Bug #13491704)

- InnoDB: The MySQL error log could contain messages like:

```
InnoDB: Ignoring strange row from mysql.innodb_index_stats WHERE ...
```

The fix makes the contents of the `innodb_index_stats` and `innodb_table_stats` tables case-sensitive, to properly distinguish the statistics for tables whose names differ only in lettercase. Other cases were fixed where the wrong name could be selected for an index while retrieving persistent statistics. (Bug #13432465)

- InnoDB: References to C preprocessor symbols and macros `HAVE_purify`,

`UNIV_INIT_MEM_TO_ZERO`, and `UNIV_SET_MEM_TO_ZERO` were removed from the `InnoDB` source code. They were only used in debug builds instrumented for Valgrind. They are replaced by calls to the`UNIV_MEM_INVALID()` macro. (Bug #13418934)

- InnoDB: The MySQL server could halt with an assertion error:

```
InnoDB: Failing assertion: page_get_n_recs(page) > 1
```

Subsequent restarts could fail with the same error. The error occurred during a purge operation involving the `InnoDB` change buffer. The workaround was to set the configuration option`innodb_change_buffering=inserts`. (Bug #13413535, Bug #61104)

## MySQL 5.6 Release Notes

- InnoDB: A discrepancy could arise between the number of available `InnoDB` undo logs and the number

of undo logs that were currently active. Now the `innodb_undo_logs` system variable reports the number of active undo logs, and the new `Innodb_available_undo_logs` status variable reports the total number of undo logs. (Bug #13255225)

- InnoDB: When doing a live downgrade from MySQL 5.6.4 or later, with `innodb_page_size` set to a

value other than 16384, now the earlier MySQL version reports that the page size is incompatible with the older version, rather than crashing or displaying a “corruption” error. (Bug #13116225)

- InnoDB: Certain `CREATE TABLE` statements could fail for `InnoDB` child tables containing

foreign key definitions. This problem affected Windows systems only, with the setting`lower_case_table_names=0`. It was a regression from MySQL bug #55222. (Bug #13083023, Bug#60229)

- InnoDB: If the server crashed during a `TRUNCATE TABLE` or `CREATE INDEX` statement for an `InnoDB`

table, or a `DROP DATABASE` statement for a database containing `InnoDB` tables, an index could be corrupted, causing an error message when accessing the table after restart:

```
InnoDB: Error: trying to load index index_name for table table_name
InnoDB: but the index tree has been freed!
```

In MySQL 5.1, this fix applies to the InnoDB Plugin, but not the built-in InnoDB storage engine. (Bug#12861864, Bug #11766019)

- InnoDB: A DDL operation for an `InnoDB` table could cause a busy MySQL server to halt with an

assertion error:

```
InnoDB: Failing assertion: trx->error_state == DB_SUCCESS
```

The error occurred if the DDL operation was run while all 1023 undo slots were in use by concurrent transactions. This error was less likely to occur in MySQL 5.5 and 5.6, because raising the number of`InnoDB` undo slots increased the number of simultaneous transactions (corresponding to the number of undo slots) from 1K to 128K. (Bug #12739098, Bug #62401)

- InnoDB: `InnoDB` persistent statistics gave less accurate estimates for date columns than for columns

of other data types. The fix changes the way cardinality is estimated for nonunique keys, and avoids situations where identical values could be counted twice if they occurred on different index pages. (Bug#12429443)

- InnoDB: The `innodb_max_purge_lag` variable controls how to delay DML operations when purge

operations are lagging. Previously, if an old consistent read view was detected, DML operations would not be delayed even though the purge lag exceeded the `innodb_max_purge_lag` setting.

Additionally, if the `innodb_max_purge_lag` setting was used, situations could arise in which the DML delay time would continue to increase but not be applied right away due to the presence an old consistent read view. This could result in a lengthy DML delay when the accumulated DML delay time is eventually applied.

This fix caps the DML delay at a maximum value, removes the consistent read check, and revises the DML delay calculation. (Bug #12407434, Bug #60776)

- InnoDB: With 1024 concurrent `InnoDB` transactions running concurrently and the

`innodb_file_per_table` setting enabled, a `CREATE TABLE` operation for an `InnoDB` table could fail.

## MySQL 5.6 Release Notes

The `.ibd` file from the failed `CREATE TABLE` was left behind, preventing the table from being created later, after the load had dropped.

The fix adds error handling to delete the erroneous `.ibd` file. This error was less likely to occur in MySQL 5.5 and 5.6, because raising the number of `InnoDB` undo slots increased the number of simultaneous transactions needed to trigger the bug, from 1K to 128K. (Bug #12400341)

- InnoDB: Improved the accuracy of persistent `InnoDB` statistics for large tables. The estimate of distinct

records could be inaccurate if the index tree was more than 3 levels deep. (Bug #12316365)

- InnoDB: Shutdown could hang with messages like this in the log:

```
Waiting for purge thread  to be suspended
```

After 1 hour, the shutdown times out and `mysqld` quits. This problem is most likely to occur with a high value for `innodb_purge_threads`. (Bug #11765863, Bug #58868, Bug #60939)

- InnoDB: When `DROP TABLE` failed due to all undo slots being in use, the error returned was `Unknown`

`table '...'` rather than the expected `Too many active concurrent transactions`. (Bug#11764724, Bug #57586)References: See also: Bug #11764668, Bug #57529.

- InnoDB: Server startup could produce an error for temporary tables using the `InnoDB` storage engine, if

the path in the `$TMPDIR` variable ended with a / character. The error log would look like:

```
120202 19:21:26  InnoDB: Operating system error number 2 in a file operation.
InnoDB: The error means the system cannot find the path specified.
InnoDB: If you are installing InnoDB, remember that you must create
InnoDB: directories yourself, InnoDB does not create them.
120202 19:21:26  InnoDB: Error: trying to open a table, but could not
InnoDB: open the tablespace file './t/#sql7750_1_0.ibd'!
InnoDB: Have you moved InnoDB .ibd files around without using the
InnoDB: commands DISCARD TABLESPACE and IMPORT TABLESPACE?
InnoDB: It is also possible that this is a temporary table #sql...,
InnoDB: and MySQL removed the .ibd file for this.
```

The workaround for the problem was to create a similar temporary table again, copy its `.frm` file to`tmpdir` under the name mentioned in the error message (for example, `#sql123.frm`) and restart`mysqld` with `tmpdir` set to its normal value without a trailing slash, for example `/var/tmp`. On startup, MySQL would see the `.frm` file and issue `DROP TABLE` for the orphaned temporary table. (Bug#11754376, Bug #45976)

- Partitioning: When creating a view from a `SELECT` statement that used explicit partition selection, the

partition selection portion of the query was ignored. (Bug #13559657)

- Partitioning: Adding a partition to an already existing `LIST`-partitioned table did not work correctly if

the number of items in the new partition was greater than 16. This could happen when trying to add a partition using an `ALTER TABLE ... ADD PARTITION` statement, or an `ALTER TABLE ...``REORGANIZE PARTITION` statement.

This 16-item limit was not apparent when using either `CREATE TABLE ... PARTITION BY LIST` or`ALTER TABLE ... PARTITION BY LIST`. (Bug #13029508, Bug #62505)

- Partitioning: A function internal to the code for finding matching subpartitions represented an unsigned

number as signed, with the result that matching subpartitions were sometimes missed in results of queries. (Bug #12725206, Bug #61765)References: See also: Bug #20257.

## MySQL 5.6 Release Notes

- Partitioning: An `ALTER TABLE ... ADD PARTITION` statement subsequent to `ALTER TABLE ...`

`REORGANIZE PARTITION` failed on a table partitioned by `HASH` or `KEY`. (Bug #11764110, Bug #56909)

- Replication: Executing `mysqlbinlog` with the `--start-position=N` option, where N was equal

either to 0 or to a value greater than the length of the dump file, caused it to crash.

This issue was introduced in MySQL 5.5.18 by the fix for Bug #32228 and Bug #11747416. (Bug#13593869, Bug #64035)References: This issue is a regression of: Bug #32228, Bug #11747416.

- Replication: When starting the server, replication repositories were checked even when the `server_id`

system variable was equal to 0 (the default), in spite of the fact that a valid nonzero value for`server_id` must be supplied for a server that acts as either a master or a slave in MySQL replication.

This could cause problems when trying to perform a live upgrade from MySQL 5.5, although it was possible to work around the issue by starting the server with `--skip-slave-start` (in addition to any other required options).

To avoid this problem, replication repositories are now checked only when the server is started with `--``server-id` using a nonzero value. (Bug #13427444, Bug #13504821)

- Replication: Formerly, the default value shown for the `Port` column in the output of `SHOW SLAVE`

`HOSTS` was 3306 whether the port had been set incorrectly or not set at all. Now, when the slave port is not set, the actual port used by the slave is shown. This change also affects the default shown for the `--``report-port` server option. (Bug #13333431)

- Replication: A race condition could occur when running multiple instances of `mysqld` on a single

machine, when more than slave thread was started at the same time, and each such thread tried to use the same temporary file concurrently. (Bug #12844302, Bug #62055)

- Replication: It was possible on replication slaves where `FEDERATED` tables were in use to get

timeouts on long-running operations, such as Error 1160 `Got an error writing communication``packets`. The `FEDERATED` tables did not need to be replicated for the issue to occur. (Bug #11758931,Bug #51196)References: See also: Bug #12896628, Bug #61790.

- Replication: Statements that wrote to tables with `AUTO_INCREMENT` columns based on an unordered

`SELECT` from another table could lead to the master and the slave going out of sync, as the order in which the rows are retrieved from the table may differ between them. Such statements include any`INSERT ... SELECT`, `REPLACE ... SELECT`, or `CREATE TABLE ... SELECT` statement. Such statements are now marked as unsafe for statement-based replication, which causes the execution of one to throw a warning, and forces the statement to be logged using the row-based format if the logging format is `MIXED`. (Bug #11758263, Bug #50440)

- Replication: On Windows replication slave hosts, `STOP SLAVE` took an excessive length of time to

complete when the master was down. (Bug #11752315, Bug #43460)

- Replication: `mysqlbinlog` `--database=dbname` included all `SET INSERT_ID=n` assignments from

the binary log in its output, even if database `dbname` was never referenced in the binary log. This was due to the fact that `COMMIT` statements were not associated with any database in the binary log. Now in such cases, the current database is tracked so that only those `SET INSERT_ID` assignments that are

## MySQL 5.6 Release Notes

made in the context of changes to tables in database `dbname` are actually printed in the `mysqlbinlog`output. (Bug #11746146, Bug #23894)References: See also: Bug #23890, Bug #46998, Bug #11761686, Bug #54201, Bug #11754117, Bug#45670.

- Microsoft Windows: On Windows, rebuilds in a source distribution failed to create the initial database

due to insufficient cleanup from the previous run or failure to find the proper server executable. (Bug#13431251)

- Microsoft Windows: On Windows, the server incorrectly constructed the full path name of the plugin

binary for `INSTALL PLUGIN` and `CREATE FUNCTION ... SONAME`. (Bug #45549, Bug #11754014)

- `mysqldump` tried to execute `SET` statements as `SET OPTION`, which failed when used against 5.6 or

higher servers because the deprecated `OPTION` keyword has been removed from `SET` syntax. (Bug#13813473)

- The optimizer did not perform constant propagation for views, so a query containing views resulted in a

less efficient execution plan than the corresponding query using only base tables. (Bug #13783777)

- A memory leak could occur for queries containing a subquery that used `GROUP BY` on an outer column.

(Bug #13724099)

- After using an `ALTER TABLE` statement to change the `KEY_BLOCK_SIZE` property for an `InnoDB` table,

for example when switching from an uncompressed to a compressed table, subsequent server restarts could fail with a message like:

```
InnoDB: Error: data file path/ibdata2 uses page size 1024,
InnoDB: but the only supported page size in this release is=16384
```

This issue is a regression introduced in MySQL 5.5.20. (Bug #13698765, Bug #64160)

- In debug builds, a Debug Sync timeout warning was treated as an error, causing an assertion to be

raised. (Bug #13688248)

- `_mi_print_key()` iterated one time too many when there was a `NULL` bit, resulting in Valgrind

warnings. (Bug #13686970)

- Pushing down to `InnoDB` an index condition that called a stored function resulted in a server crash. This

kind of condition is no longer pushed down. (Bug #13655397)

- A `SELECT` from a subquery that returned an empty result could itself fail to return an empty result as

expected. (Bug #13651009, Bug #13650418)

- For debug builds, negative values with a zero integer part and nonzero fractional part (such as -0.1111)

were not detected, so the negative fractional part was later cast to a large unsigned number and raised an assertion. (Bug #13616434)

- If during server startup a signal such as `SIGHUP` was caught prior to full server initialization, the server

could crash. This was due to a race condition between the signal handler thread and the main thread performing server initialization. To prevent this from happening, signal processing is now suspended until full initialization of all server subsystems has been completed successfully. (Bug #13608371, Bug#62311)

- The shared version of `libmysqlclient` did not export these functions for linking by client programs:

`get_tty_password()`, `handle_options()`, `my_print_help()`. (Bug #13604121)

## MySQL 5.6 Release Notes

- An aggregated expression of type `MIN()` or `MAX()` should return `NULL` but could instead return the

empty set if the query was implicitly grouped and there was no `HAVING` clause that evaluates to `FALSE`.

(Bug #13599013)

- Left join queries could be incorrectly converted to inner joins and return erroneous result sets. (Bug

#13595212)

- Date-handling code could raise an assertion attempting to calculate the number of seconds since the

epoch. (Bug #13545236)

- For queries that used a join type of `ref_or_null`, the optimizer could skip the filesort operation and

sort the results incorrectly. (Bug #13531865)

- For some queries, a filesort operation was done even when the result contained only a single row and

needed no sorting. (Bug #13529048)

- The optimizer could return an incorrect select limit in some cases when a query included no explicit

`LIMIT` clause. (Bug #13528826)

- In some cases, the optimizer failed to use a covering index when that was possible and read data rows

instead. (Bug #13514959)

- `SELECT` statements failed for the `EXAMPLE` storage engine. (Bug #13511529)

References: This issue is a regression of: Bug #11746275.

- The Performance Schema instrumentation for stages did not fully honor the `ENABLED` column in the

`schema.setup_instruments` table. (Bug #13509513)

- Converting a string ending with a decimal point (such as `'1.'`) to a floating-point number raised a data

truncation warning. (Bug #13500371)

- Use of an uninitialized `TABLE_SHARE` member could cause a server crash. (Bug #13489996)
- Some outer joins that used views as inner tables did not evaluate conditions correctly. (Bug #13464334)
- A query that used an index on a `CHAR` column referenced in a `BETWEEN` clause could return invalid

results. (Bug #13463488, Bug #63437)

- Expressions that compared a `BIGINT` column with any non-integer constant were performed using

integers rather than decimal or float values, with the result that the constant could be truncated. This could lead to any such comparison that used <, >, `<=`, `>=`, =, `!=`/`<>`, `IN`, or `BETWEEN` yielding false positive or negative results. (Bug #13463415, Bug #11758543, Bug #63502, Bug #50756)

- An application linked against `libmysqld` could crash in debug mode with a `stack smashing`

`detected` error if it tried to connect without specifying the user name. (Bug #13460909)

- Instantiating a derived table for a query with an empty result caused a server crash. (Bug #13457552)
- When the optimizer performed conversion of `DECIMAL` values while evaluating range conditions, it could

produce incorrect results. (Bug #13453382)

- Implicitly grouped queries with a `const` table and no matching rows could return incorrect results. (Bug

#13430588)

- For debug builds, enabling `optimizer_trace` could cause an assertion to be raised. (Bug #13430443)
- Enabling index condition pushdown could cause performance degradation. (Bug #13430436)

## MySQL 5.6 Release Notes

- When a fixed-width row was inserted into a `MyISAM` temporary table, the entire content of the record

buffer was written to the table, including any trailing space contained in `VARCHAR` columns, the issue being that this trailing space could be uninitialized. This problem has been resolved by insuring that only the bytes actually used to store the `VARCHAR` (and none extra) are copied and inserted in such cases.

(Bug #13389854, Bug #79028, Bug #22123583)

- Fractional seconds parts were lost for certain `UNION ALL` queries. (Bug #13375823)
- When merging ranges that effectively resulted in a full index scan, the optimizer did not discard the

range predicate as unneeded. (Bug #13354910)

- When executing `EXPLAIN`, it was assumed that only the default multi-range read implementation could

produce an ordered result; this meant that when a query on a table that used a storage engine providing its own sorted MRR, it was ignored, so that `EXPLAIN` failed to report `Using MRR` even when a multi-range read was used. (Bug #13330645)

- Some multiple-table updates could update a row twice. (Bug #13095459)
- Performance Schema `idle` event timings were not normalized to the same units as wait timings. (Bug

#13018537)

- In MySQL 5.6.3, a number of status variables were changed to `longlong` types so that they would

roll over much later. However, the format string used by `mysqladmin status` to print `Queries per``second` values did not reflect this, causing such values to be misreported. (Bug #12990746)References: See also: Bug #42698. This issue is a regression of: Bug #11751727.

- For debug builds, two assertions could be raised erroneously for `UPDATE` statements. (Bug #12912171)
- When the result of a stored function returning a non-integer type was evaluated for `NULL`, an incorrect

type warning (Warning 1292 `Truncated incorrect INTEGER value`) is generated, although such a test for `NULL` should work with any type. This could cause stored routines not handling the warning correctly to fail.

The issue could be worked around by wrapping the result in an expression, using a function such as`CONCAT()`. (Bug #12872824, Bug #62125)

- When running `mysqldump` with both the `--single-transaction` and `--flush-logs` options, the

flushing of the log performed an implicit `COMMIT` (see Statements That Cause an Implicit Commit),causing more than one transaction to be used and thus breaking consistency. (Bug #12809202, Bug#61854)

- A query that used an aggregate function such as `MAX()` or `MIN()` of an index with `NOT BETWEEN` in the

`WHERE` clause could fail to match rows, thus returning an invalid result. (Bug #12773464, Bug #61925)

- With `ONLY_FULL_GROUP_BY` SQL mode enabled, columns that were not aggregated in the select list or

named in a `GROUP BY` were incorrectly permitted in `ORDER BY`. (Bug #12626418)

- Mishandling of `NO_BACKSLASH_ESCAPES` SQL mode within stored procedures on slave servers could

cause replication failures. (Bug #12601974)

- Passing a user variable as an argument to `GROUP_CONCAT()` could cause a server exit if the variable

value changed during query execution. (Bug #12408412)

- `LOAD INDEX INTO CACHE` could cause a server exit if the index cache was too small. (Bug

#12361113)

## MySQL 5.6 Release Notes

- With `ONLY_FULL_GROUP_BY` SQL mode enabled, a query that uses `GROUP BY` on a column derived

from a subquery in the `FROM` clause failed with a `column isn't in GROUP BY` error, if the query was in a view. (Bug #11923239)

- Attempting to execute `ALTER TABLE` on a temporary `MERGE` table having an underlying temporary table

rendered the `MERGE` table unusable, unless the `ALTER TABLE` specified a new list of underlying tables.

(Bug #11764786, Bug #57657)

- It was possible in the event of successive failures for `mysqld_safe` to restart quickly enough to

consume excessive amounts of CPU. Now, on systems that support the `sleep` and `date` system utilities, `mysqld_safe` checks to see whether it has restarted more than 5 times in the current second,and if so, waits 1 second before attempting another restart. (Bug #11761530, Bug #54035)

- A `HAVING` clause in a query using `MIN()` or `MAX()` was sometimes ignored. (Bug #11760517, Bug

#52935)References: See also: Bug #11758970, Bug #51242, Bug #11759718, Bug #52051.

- When used with the `--xml` option, `mysqldump` `--routines` failed to dump any stored routines,

triggers, or events. (Bug #11760384, Bug #52792)

- If an attempt to initiate a statement failed, the issue could not be reported to the client because it was not

prepared to receive any error messages prior to the execution of any statement. Since the user could not execute any queries, they were simply disconnected without providing a clear error.

After the fix for this issue, the client is prepared for an error as soon as it attempts to initiate a statement,so that the error can be reported prior to disconnecting the user. (Bug #11755281, Bug #47032)

- Previously, `.OLD` files were not included among the files deleted by `DROP DATABASE`. Files with this

extension are now also deleted by the statement. (Bug #11751736, Bug #42708)

- A prepared statement using a view whose definition changed between preparation and execution

continued to use the old definition, which could cause the prepared statement to return incorrect results.

(Bug #11748352, Bug #36002)

- Some debugging information was written to the buffer after a flush, resulting in the information not

appearing until the next flush. (Bug #64048, Bug #13608112)

- Locale information for `FORMAT()` function instances was lost in view definitions. (Bug #63020, Bug

#13344643)

- `mysqlhotcopy` failed for databases containing views. (Bug #62472, Bug #13006947, Bug #12992993)
- The VIO description string was initialized even for connections where it was unneeded. (Bug #62285,

Bug #12951586)

- On Windows, pasting multiple-line input including a CRLF terminator on the last line into the `mysql`

client resulted in the first character of the last line being changed, resulting in erroneous statements.

Handling of newlines in pasted input was also incorrect. (Bug #60901, Bug #12589167, Bug #64104,Bug #13639107)

- The contents of the `shared` and `shared-compat` RPM packages had been changed in versions

5.5.6 and 5.6.1 to avoid the overlap which they traditionally had (and still have in MySQL 5.0 and 5.1).

However, the RPM meta information had not been changed in accordance, and so RPM still assumed a conflict between `shared` and `shared-compat` RPM packages. This has been fixed. (Bug #60855, Bug#12368215)References: See also: Bug #56150.

## MySQL 5.6 Release Notes

- The result of `SUBSTRING_INDEX()` could be missing characters when used as an argument to

conversion functions such as `LOWER()`. (Bug #60166, Bug #11829861)

- `UPDATE IGNORE` returned an incorrect count for number of rows updated when there were duplicate-key

conflicts in a multiple-table update. (Bug #59715, Bug #11766576)

- The optimizer mishandled `STRAIGHT_JOIN` used with nested joins; for example, by not evaluating

tables in the specified order. (Bug #59487, Bug #11766384, Bug #43368, Bug #11752239, Bug #60080,Bug #11766858)

- A subquery involved in a comparison requiring a character set conversion caused an error that resulted

in a server crash. (Bug #59185, Bug #11766143)

- The embedded server crashed when `argc = 0`. (Bug #57931, Bug #12561297)
- If tables were locked by `LOCK TABLES ... READ` in another session, `SET GLOBAL read_only = 1`

failed to complete. (Bug #57612, Bug #11764747)

- Invalid memory reads could occur when `cmp_item_sort_string::store_value()` tried to refer to

a temporary value that could be changed or deleted by other functions. (Bug #57510, Bug #11764651)

- Assigning the result of a subquery to a user variable raised an assertion when the outer query included

`DISTINCT` and `GROUP BY`. (Bug #57196, Bug #11764371)

- For comparisons containing out-of-range constants, the optimizer permitted warnings to leak through to

the client, even though it accounted for the range issue internally. (Bug #56962, Bug #11764155)

- A confusing `CREATE TABLE` error message was improved. (Bug #54963, Bug #11762377)
- The `handle_segfault()` signal-handler code in `mysqld` could itself crash due to calling unsafe

functions. (Bug #54082, Bug #11761576)

- Using `myisamchk` with the sort recover method to repair a table having fixed-width row format could

cause the row pointer size to be reduced, effectively resulting in a smaller maximum data file size. (Bug#48848, Bug #11756869)

- Enabling `myisam_use_mmap` could cause the server to crash. (Bug #48726, Bug #11756764)
- For `MEMORY` tables, a scan of a `HASH` index on a `VARCHAR` column could fail to find some rows if the

index was on a prefix of the column. (Bug #47704, Bug #11755870)

- `myisam_sort_buffer_size` could not be set larger than 4GB on 64-bit systems. (Bug #45702, Bug

#11754145)

- The stored routine cache was subject to a small memory leak that over time or with many routines being

used could result in out-of-memory errors.

The fix for this issue also introduces a new global server system variable `stored_program_cache`which can be used for controlling the size of the stored routine cache. (Bug #44585, Bug #11753187)

- Under some circumstances, the result of `SUBSTRING_INDEX()` incorrectly depended on the contents of

the previous row. (Bug #42404, Bug #11751514)

- Setting an event to `DISABLED` status and with the `ON COMPLETION NOT PRESERVE` attribute caused it

to be dropped at the next server restart. (Bug #37666, Bug #11748899)

- Due to improper locking, concurrent inserts into an `ARCHIVE` table at the same time as repair and check

operations on the table resulted in table corruption. (Bug #37280, Bug #11748748)

## MySQL 5.6 Release Notes

- Stored functions could produce an error message that referred to `ORDER BY` even though the offending

statement within the function had no such clause. (Bug #35410, Bug #11748187)
