---
title: "Changes in MySQL 5.6.1 (Not released, Milestone 5)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=278"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Note This is a milestone release, for use at your own risk. Upgrades between milestone releases (or from a milestone release to a GA release) are not supported.

Significant development changes take place in milestone releases and you may encounter compatibility issues, such as data format changes that require attention in addition to the usual procedure of running `mysql_upgrade`. For example, you may find it necessary to dump your data with `mysqldump` before the upgrade and reload it afterward. (Making a backup before the upgrade is a prudent precaution in any case.)

## MySQL 5.6 Release Notes

- Performance Schema Notes
- Functionality Added or Changed
- Bugs Fixed

> Performance Schema Notes

- The Performance Schema has these additions:
- The `setup_consumers` table contents have changed. Previously, the table used a “flat” structure

with a one-to-one correspondence between consumer name and destination table. This has been replaced with a hierarchy of consumer settings that enable progressively finer control of which destinations receive events. The previous `xxx_summary_xxx` consumers no longer exist. Instead,the Performance Schema maintains appropriate summaries automatically for the levels for which settings in the consumer hierarchy are enabled. For example, if only the top-level (global) consumer is enabled, only global summaries are maintained. Others, such as thread-level summaries, are not.

See Pre-Filtering by Consumer. In addition, optimizations have been added to reduce Performance Schema overhead.

- It is now possible to filter events by object using the new `setup_objects` table. Currently, this table

can be used to selectively instrument tables, based on schema names and/or table names. See Pre-Filtering by Object. A new table, `objects_summary_global_by_type`, summarizes events for objects.

- It is now possible to filter events by thread, and the Performance Schema collects more information

for each thread. A new table, `setup_actors`, can be used to selectively instrument user connections, based on the user name and/or host name of each connecting session. The`threads` table, which contains a row for each active server thread, was extended with several new columns. With these additions, the information available in `threads` is like that available from the`INFORMATION_SCHEMA.PROCESSLIST` table or the output from `SHOW PROCESSLIST`. Thus, all three serve to provide information for thread-monitoring purposes. Use of `threads` differs from use of the other two thread information sources in these ways:

- Access to `threads` does not require a mutex and has minimal impact on server performance.

`INFORMATION_SCHEMA.PROCESSLIST` and `SHOW PROCESSLIST` have negative performance consequences because they require a mutex.

- `threads` provides additional information for each thread, such as whether it is a foreground or

background thread, and the location within the server associated with the thread.

- `threads` provides information about background threads. This means that `threads` can be used to

monitor activity the other thread information sources cannot.

- You can control which threads are monitored by setting the `INSTRUMENTED` column or by using the

`setup_actors` table.

For these reasons, DBAs who perform server monitoring using`INFORMATION_SCHEMA.PROCESSLIST` or `SHOW PROCESSLIST` may wish to monitor using `threads`instead.

If you upgrade to this MySQL release from an earlier version, you must run `mysql_upgrade` (and restart the server) to incorporate these changes into the `performance_schema` database.

For more information, see MySQL Performance Schema. (WL #4674, WL #4816)

## MySQL 5.6 Release Notes

> Functionality Added or Changed

- Incompatible Change: The following obsolete constructs have been removed. Where alternatives are

shown, applications should be updated to use them.

- The `--log` server option and the `log` system variable. Instead, use the `general_log` system

variable to enable the general query log and the `general_log_file` system variable to set the general query log file name.

- The `log_slow_queries` system variable. Instead, use the `slow_query_log` system variable to

enable the slow query log and the `slow_query_log_file` system variable to set the slow query log file name.

- The `--one-thread` server option. Use `--thread_handling=no-threads` instead.
- The `--skip-thread-priority` server option.
- The `engine_condition_pushdown` system variable. Use the `engine_condition_pushdown` flag

of the `optimizer_switch` variable instead.

- The `have_csv`, `have_innodb`, `have_ndbcluster`, and `have_partitioning` system variables.

Use `SHOW ENGINES` instead.

- The `sql_big_tables` system variable. Use `big_tables` instead.
- The `sql_low_priority_updates` system variable. Use `low_priority_updates` instead.
- The `sql_max_join_size` system variable. Use `max_join_size` instead.
- The `SLAVE START` and `SLAVE STOP` statements. Use the `START SLAVE` and `STOP SLAVE`

statements instead.

- The `ONE_SHOT` modifier for the `SET` statement.

(WL #5185, WL #6311)

- Important Change; Replication: Replication filtering options such as `--replicate-do-db`, `--`

`replicate-rewrite-db`, and `--replicate-do-table` were not consistent with one another in regard to case sensitivity. Now all `--replicate-*` options follow the same rules for case sensitivity applying to names of databases and tables elsewhere in the MySQL server, including the effects of the`lower_case_table_names` system variable. (Bug #51639, Bug #11759334)

- Important Change; Replication: Added the `MASTER_RETRY_COUNT` option to the `CHANGE MASTER`

`TO` statement, and a corresponding `Master_Retry_Count` column to the output of `SHOW SLAVE``STATUS`. The option sets the value shown in this column. `MASTER_RETRY_COUNT` is intended eventually to replace the older (and now deprecated) `--master-retry-count` server option, and is now the preferred method for setting the maximum number of times that the slave may attempt to reconnect after losing its connection to the master. (Bug #44209, Bug #11752887, Bug #44486, Bug #11753110)

- InnoDB: Setting `innodb_read_ahead_threshold` to 0 disables read-ahead. Prior to 5.6.1, a value

of 0 would trigger a read-ahead upon reading the boundary page of a 64 page extent. (Bug #11763876,Bug #56646)

## MySQL 5.6 Release Notes

- InnoDB: `InnoDB` can now report the total size of the rollback segment, measured in pages. The

value is reported through the `information_schema.innodb_metrics` table, using the counter`trx_rseg_current_size`. You enable and query the counter as follows:

```
mysql> SET GLOBAL innodb_monitor_enable = 'trx_rseg_current_size';
mysql> SELECT name, count, max_count, comment
->     FROM innodb_metrics WHERE name = 'trx_rseg_current_size';
+-----------------------+-------+-----------+----------------------------------------+
| name                  | count | max_count | comment                                |
+-----------------------+-------+-----------+----------------------------------------+
| trx_rseg_current_size |   346 |       346 | Current rollback segment size in pages |
+-----------------------+-------+-----------+----------------------------------------+
```

(Bug #57584)

- Replication: `SHOW SLAVE STATUS` now displays the actual number of retries for each connection

attempt made by the I/O thread. (Bug #56416, Bug #11763675)

- Replication: Added the `Slave_last_heartbeat` status variable, which shows when a replication

slave last received a heartbeat signal. The value is displayed using `TIMESTAMP` format. (Bug #45441)

- Replication: Timestamps have been added to the output of `SHOW SLAVE STATUS` to show when the

most recent I/O and SQL thread errors occurred. The `Last_IO_Error` column is now prefixed with the timestamp for the most recent I/O error, and `Last_SQL_Error` shows the timestamp for the most recent SQL thread error. The timestamp values use the format `YYMMDD hh:mm:ss` in both of these columns. For more information, see SHOW SLAVE STATUS Statement. (Bug #43535, Bug #11752361,Bug #64255, Bug #13726435)

- There is now a `bind_address` system variable containing the value of the `--bind-address` option.

This enables the address to be accessed at runtime. (Bug #44355, Bug #11752999)

- “Unknown table” error messages that included only the table name now include the database name as

well. (Bug #34750, Bug #11747993)

- Previously, `EXPLAIN` output for a large union truncated the `UNION RESULT` row at the end of the list as

follows if the string became too large:

```
<union1,2,3,4,...>
```

To make it easier to understand the union boundaries, truncation now occurs in the middle of the string:

```
<union1,2,3,...,9>
```

(Bug #30597, Bug #11747073)

- The OpenGIS specification defines functions that test the relationship between two geometry values.

MySQL originally implemented these functions such that they used object bounding rectangles and returned the same result as the corresponding MBR-based functions. Corresponding versions are now available that use precise object shapes. These versions are named with an `ST_` prefix. For example,`Contains()` uses object bounding rectangles, whereas `ST_Contains()` uses object shapes. For more information, see Functions That Test Spatial Relations Between Geometry Objects.

There are also now `ST_` aliases for existing spatial functions that were already exact. For example,`ST_IsEmpty()` is an alias for `IsEmpty()`In addition, the `IsSimple()` and `ST_Distance()` spatial functions are now implemented, as well as the set operator functions `ST_Difference()`, `ST_Intersection()`, `ST_SymDifference()`, and`ST_Union()`, (Bug #4249, Bug #11744883, WL #1326)

## MySQL 5.6 Release Notes

- The following items are deprecated and will be removed in a future MySQL release. Where alternatives

are shown, applications should be updated to use them.

- The `thread_concurrency` system variable.
- The `--language` server option. Use the `lc_messages_dir` and `lc_messages` system variables

instead.

- The `--master-retry-count` server option. Use the `MASTER_RETRY_COUNT` option the `CHANGE`

`MASTER TO` statement instead.

(WL #5265)

- Support for adding Unicode collations that are based on the Unicode Collation Algorithm (UCA) has

been improved:

- MySQL now recognizes a larger subset of the LDML syntax that is used to write collation descriptions.

In many cases, it is possible to download a collation definition from the Unicode Common Locale Data Repository and paste the relevant part (that is, the part between the `<rules>` and `</rules>` tags)into the MySQL `Index.xml` file.

- Character representation in LDML rules is more flexible. Any character can be written literally, not

just basic Latin letters. For collations based on UCA 5.2.0, hexadecimal notation can be used for any character, not just BMP characters.

- When problems are found while parsing `Index.xml`, better diagnostics are produced.
- For collations that require tailoring rules, there is no longer a fixed size limit on the tailoring

information.

For more information, see LDML Syntax Supported in MySQL, and Diagnostics During Index.xml Parsing. (WL #5624)

- `TO_BASE64()` and `FROM_BASE64()` functions are now available to perform encoding to and from

base-64 strings. (WL #5510)

## MySQL 5.6 Release Notes

- The Unicode implementation has been extended to include a `utf16le` character set, which corresponds

to the UTF-16LE encoding of the Unicode character set. This is similar to `utf16` (UTF-16) but is little-endian rather than big-endian.

Two `utf16le` collations are available:

- `utf16le_general_ci`: The default collation, case sensitive (similar to `utf16_general_ci`).
- `utf16le_bin`: Case sensitive, with by-codepoint comparison that provides the same order as

```
utf16_bin.
```

There are some limitations on the use of `utf16le`. With the exception of the item regarding user-defined collations, these are the same as the limitations on `ucs2`, `utf16`, and `utf32`.

- `utf16le` cannot be used as a client character set, which means that it also does not work for `SET`

```
NAMES or SET CHARACTER SET.
```

- It is not possible to use `LOAD DATA` to load data files that use `utf16le`.
- `FULLTEXT` indexes cannot be created on a column that uses `utf16le`. However, you can perform `IN`

`BOOLEAN MODE` searches on the column without an index.

- The use of `ENCRYPT()` with `utf16le` is not recommended because the underlying system call

expects a string terminated by a zero byte.

- It is not possible to create user-defined UCA collations for `utf16le` because there is no

`utf16le_unicode_ci` collation, which would serve as the basis for such collations.

(WL #4616)

- Changes to replication in MySQL 5.6 make `mysqlbinlog` output generated by the `--base64-`

`output=ALWAYS` option unusable. `ALWAYS` is now an invalid value for this option. If the option is given without a value, the effect is now the same as `--base64-output=AUTO` rather than `--base64-``output=ALWAYS`. (WL #5625)References: See also: Bug #28760.

- Croatian collations were added for Unicode character sets: `utf8_croatian_ci`, `ucs2_croatian_ci`,

`utf8mb4_croatian_ci`, `utf16_croatian_ci`, and `utf32_croatian_ci`. Thee collations have tailoring for Croatian letters: Č, Ć, Dž, Đ, `Lj`, `Nj`, Š, Ž. They are based on Unicode 4.0. (WL #5476)

- Several changes were made to optimizer-related system variables:
- The `optimizer_switch` system variable has new `engine_condition_pushdown` and

`index_condition_pushdown` flags to control whether storage engine condition pushdown and index condition pushdown optimizations are used. The `engine_condition_pushdown` system variable now is deprecated. For information about condition pushdown, see Engine Condition Pushdown Optimization, and Index Condition Pushdown Optimization.

- The `optimizer_switch` system variable has new `mrr` and `mrr_cost_based` flags to control use

of the Multi-Range Read optimization. The `optimizer_use_mrr` system variable has been removed.

For information about Multi-Range Read, see Multi-Range Read Optimization.

## MySQL 5.6 Release Notes

- The `join_cache_level` system variable has been renamed to `optimizer_join_cache_level`.

This enables a single `SHOW VARIABLES LIKE 'optimizer%'` statement to show more optimizer-related settings.

(WL #5116, WL #5197, WL #5639, WL #5692)

- The Block Nested-Loop (BNL) Join algorithm previously used only for inner joins has been extended and

can be employed for outer join operations, including nested outer joins. For more information, see Block Nested-Loop and Batched Key Access Joins.

In conjunction with this work, a new system variable, `optimizer_join_cache_level`, controls how join buffering is done.

- A `--bind-address` option has been added to a number of MySQL client programs: `mysql`,

```
mysqldump, mysqladmin, mysqlbinlog, mysqlcheck, mysqlimport, and mysqlshow. This is
```

for use on a computer having multiple network interfaces, and enables you to choose which interface is used to connect to the MySQL server.

A corresponding change was made to the `mysql_options()` C API function, which now has a`MYSQL_OPT_BIND` option for specifying the interface. The argument is a host name or IP address(specified as a string). (WL #3126)

> Bugs Fixed

- Incompatible Change; Replication: The behavior of `INSERT DELAYED` statements when using

statement-based replication has changed as follows:Previously, when using `binlog_format=STATEMENT`, a warning was issued in the client when executing `INSERT DELAYED`; now, no warning is issued in such cases.

Previously, when using `binlog_format=STATEMENT`, `INSERT DELAYED` was logged as `INSERT``DELAYED`; now, it is logged as an `INSERT`, without the `DELAYED` option.

However, when `binlog_format=STATEMENT`, `INSERT DELAYED` continues to be executed as`INSERT` (without the `DELAYED` option). The behavior of `INSERT DELAYED` remains unchanged when using `binlog_format=ROW`: `INSERT DELAYED` generates no warnings, is executed as `INSERT``DELAYED`, and is logged using the row-based format.

This change also affects `binlog_format=MIXED`, because `INSERT DELAYED` is no longer considered unsafe. Now, when the logging format is `MIXED`, no switch to row-based logging occurs. This means that the statement is logged as a simple `INSERT` (that is, without the `DELAYED` option), using the statement-based logging format. (Bug #54579, Bug #11762035)References: See also: Bug #56678, Bug #11763907, Bug #57666. This issue is a regression of: Bug#39934, Bug #11749859.

- Incompatible Change; Replication: When determining whether to replicate a `CREATE DATABASE`,

`DROP DATABASE`, or `ALTER DATABASE` statement, database-level options now take precedence over any `--replicate-wild-do-table` options. In other words, when trying to replicate one of these statements, `--replicate-wild-do-table` options are now checked if and only if there are no database-level options that apply to the statement. (Bug #46110, Bug #11754498)

- Incompatible Change: Starvation of `FLUSH TABLES WITH READ LOCK` statements occurred when

there was a constant load of concurrent DML statements in two or more connections. Deadlock occurred when a connection that had some table open through a `HANDLER` statement tried to update data through

## MySQL 5.6 Release Notes

a DML statement while another connection tried to execute `FLUSH TABLES WITH READ LOCK`concurrently.

These problems resulted from the global read lock implementation, which was reimplemented with the following consequences:

- To solve deadlock in event-handling code that was exposed by this patch, the

`LOCK_event_metadata` mutex was replaced with metadata locks on events. As a result, DDL operations on events are now prohibited under `LOCK TABLES`. This is an incompatible change.

- The global read lock (`FLUSH TABLES WITH READ LOCK`) no longer blocks DML and DDL on

temporary tables. Before this patch, server behavior was not consistent in this respect: In some cases,DML/DDL statements on temporary tables were blocked; in others, they were not. Since the main use cases for `FLUSH TABLES WITH READ LOCK` are various forms of backups and temporary tables are not preserved during backups, the server now consistently permits DML/DDL on temporary tables under the global read lock.

- The set of thread states has changed:

```
- Waiting for global metadata lock is replaced by Waiting for global read lock.
```

- Previously, `Waiting for release of readlock` was used to indicate that DML/DDL

statements were waiting for release of a read lock and `Waiting to get readlock` was used to indicate that `FLUSH TABLES WITH READ LOCK` was waiting to acquire a global read lock. Now`Waiting for global read lock` is used for both cases.

- Previously, `Waiting for release of readlock` was used for all statements that caused an

explicit or implicit commit to indicate that they were waiting for release of a read lock and `Waiting`

```
for all running commits to finish was used by FLUSH TABLES WITH READ LOCK.
```

Now `Waiting for commit lock` is used for both cases.

- There are two other new states, `Waiting for trigger metadata lock` and `Waiting for`

```
event metadata lock.
```

(Bug #57006, Bug #11764195, Bug #54673, Bug #11762116)

- Incompatible Change: `CREATE TABLE` statements (including `CREATE TABLE ... LIKE`) are now

prohibited whenever a `LOCK TABLES` statement is in effect.

One consequence of this change is that `CREATE TABLE ... LIKE` makes the same checks as`CREATE TABLE` and does not just copy the `.frm` file. This means that if the current SQL mode is different from the mode in effect when the original table was created, the table definition might be considered invalid for the new mode and the statement will fail. (Bug #42546, Bug #11751609)

- InnoDB; Replication: If the master had `innodb_file_per_table=OFF`,

`innodb_file_format=Antelope` (and `innodb_strict_mode=OFF`), or both, certain `CREATE``TABLE` options, such as `KEY_BLOCK_SIZE`, were ignored. This could permit the master to avoid raising`ER_TOO_BIG_ROWSIZE` errors.

However, the ignored `CREATE TABLE` options were still written into the binary log, so that, if the slave had `innodb_file_per_table=ON` and `innodb_file_format=Barracuda`, it could encounter an

## MySQL 5.6 Release Notes

`ER_TOO_BIG_ROWSIZE` error while executing the record from the log, causing the slave SQL thread to abort and replication to fail.

In the case where the master was running MySQL 5.1 and the slave was MySQL 5.5 (or later), the failure occurred when both master and slave were running with default values for`innodb_file_per_table` and `innodb_file_format`. This could cause problems during upgrades.

To address this issue, the default values for `innodb_file_per_table` and `innodb_file_format`are reverted to the MySQL 5.1 default values—that is, `OFF` and `Antelope`, respectively. (Bug #56318,Bug #11763590)

- InnoDB: If the MySQL Server crashed immediately after creating an `InnoDB` table, the server could

quit with a `signal 11` during the subsequent restart. The issue could occur if the server halted after`InnoDB` created the primary index for the table, but before the index definition was recorded in the MySQL metadata. (Bug #57616)References: This issue is a regression of: Bug #54582.

- InnoDB: With binary logging enabled, `InnoDB` could halt during crash recovery with a message referring

to a transaction ID of 0. (Bug #54901, Bug #11762323)

- Replication: Due to changes made in MySQL 5.5.3, settings made in the `binlog_cache_size`

and `max_binlog_cache_size` server system variables affected both the binary log statement cache (also introduced in that version) and the binary log transactional cache (formerly known simply as the binary log cache). This meant that the resources used as a result of setting either or both of these variables were double the amount expected. To rectify this problem, these variables now affect only the transactional cache. The fix for this issue also introduces two new system variables`binlog_stmt_cache_size` and `max_binlog_stmt_cache_size`, which affect only the binary log statement cache.

In addition, the `Binlog_cache_use` status variable was incremented whenever either cache was used, and `Binlog_cache_disk_use` was incremented whenever the disk space from either cache was used, which caused problems with performance tuning of the statement and transactional caches,because it was not possible to determine which of these was being exceeded when attempting to troubleshoot excessive disk seeks and related problems. This issue is solved by changing the behavior of these two status variables such that they are incremented only in response to usage of the binary log transactional cache, as well as by introducing two new status variables `Binlog_stmt_cache_use` and`Binlog_stmt_cache_disk_use`, which are incremented only by usage of the binary log statement cache.

The behavior of the `max_binlog_cache_size` system variable with regard to active sessions has also been changed to match that of the `binlog_cache_size` system variable: Previously, a change in `max_binlog_cache_size` took effect in existing sessions; now, as with a change in`binlog_cache_size`, a change in `max_binlog_cache_size` takes effect only in sessions begun after the value was changed.

For more information, see System Variables Used with Binary Logging, and Server Status Variables.

(Bug #57275, Bug #11764443)

- Replication: The `Binlog_cache_use` and `Binlog_cache_disk_use status` variables were

incremented twice by a change to a table using a transactional storage engine. (Bug #56343, Bug#11763611)References: This issue is a regression of: Bug #50038.

## MySQL 5.6 Release Notes

- Replication: When `STOP SLAVE` is issued, the slave SQL thread rolls back the current transaction

and stops immediately if the transaction updates only tables which use transactional storage engines.

Previously, this occurred even when the transaction contained `CREATE TEMPORARY TABLE` statements,`DROP TEMPORARY TABLE` statements, or both, although these statements cannot be rolled back.

Because temporary tables persist for the lifetime of a user session (in the case, the replication user),they remain until the slave is stopped or reset. When the transaction is restarted following a subsequent`START SLAVE` statement, the SQL thread aborts with an error that a temporary table to be created (or dropped) already exists (or does not exist, in the latter case).

Following this fix, if an ongoing transaction contains `CREATE TEMPORARY TABLE` statements, `DROP``TEMPORARY TABLE` statements, or both, the SQL thread now waits until the transaction ends, then stops. (Bug #56118, Bug #11763416)

- Replication: When an error occurred in the generation of the name for a new binary log file, the error

was logged but not shown to the user. (Bug #46166)References: See also: Bug #37148, Bug #11748696, Bug #40611, Bug #11750196, Bug #43929, Bug#51019.

- Replication: When `lower_case_table_names` was set to 1 on the slave, but not on the master,

names of databases in replicated statements were not converted, causing replication to fail on slaves using case-sensitive file systems. This occurred for both statement-based and row-based replication.

In addition, when using row-based replication with `lower_case_table_names` set to 1 on the slave only, names of tables were also not converted, also causing replication failure on slaves using case-sensitive file systems. (Bug #37656)

- After setting `collation_connection` to one of the collations for the `ucs2` or `utf16` character sets, it

was not possible to change the collation thereafter. (Bug #65000, Bug #13970475)

- `cmake` `-DBUILD_CONFIG=mysql_release` on Linux previously required `libaio` to be linked in. Now

it is possible to specify `-DIGNORE_AIO_CHECK` to build without `libaio`. (Bug #58955, Bug #11765940)

- A Valgrind failure occurred in `fn_format` when called from `archive_discover`. (Bug #58205, Bug

#11765259)

- Passing a string that was not null-terminated to `UpdateXML()` or `ExtractValue()` caused the server

to fail with an assertion. (Bug #57279, Bug #11764447)

- In bootstrap mode, the server could not execute statements longer than 10,000 characters. (Bug

#55817, Bug #11763139)

- `NULL` values were not grouped properly for some joins containing `GROUP BY`. (Bug #45267, Bug

#11753766)

- A `HAVING` clause could be lost if an index for `ORDER BY` was available, incorrectly permitting additional

rows to be returned. (Bug #45227, Bug #11753730)

- The optimizer could underestimate the memory required for column descriptors during join processing

and cause memory corruption or a server crash. (Bug #42744, Bug #11751763)

- The server returned incorrect results for `WHERE ... OR ... GROUP BY` queries against `InnoDB`

tables. (Bug #37977, Bug #11749031)

- An incorrectly checked `XOR` subquery optimization resulted in an assertion failure. (Bug #37899, Bug

#11748998)

## MySQL 5.6 Release Notes

- A query that could use one index to produce the desired ordering and another index for range access

with index condition pushdown could cause a server crash. (Bug #37851, Bug #11748981)

- With index condition pushdown enabled, `InnoDB` could crash due to a mismatch between what

pushdown code expected to be in a record versus what was actually there. (Bug #36981, Bug#11748647)

- The range optimizer ignored conditions on inner tables in semijoin `IN` subqueries, causing the optimizer

to miss good query execution plans. (Bug #35674, Bug #11748263)

- A server crash or memory overrun could occur with a dependent subquery and joins. (Bug #34799, Bug

#11748009)

- Selecting from a view that referenced the same table in the `FROM` clause and an `IN` clause caused a

server crash. (Bug #33245)

- Deeply nested subqueries could cause stack overflow or a server crash. (Bug #32680, Bug #11747503)
- The server crashed on optimization of queries that compared an indexed `DECIMAL` column with a string

value. (Bug #32262, Bug #11747426)

- The server crashed on optimizations that used the `range checked for each record` access

method. (Bug #32229, Bug #11747417)

- `Contains()` failed for multipolygon geometries. (Bug #32032, Bug #11747370)
- If the optimizer used a Multi-Range Read access method for index lookups, incorrect results could occur

for rows that contained any `BLOB` or `TEXT` data types. (Bug #30622, Bug #11747076)

- Compared to MySQL 5.1, the optimizer failed to use join buffering for certain queries, resulting in slower

performance for those queries. (Bug #30363, Bug #11747028)

- For Multi-Range Read scans used to resolve `LIMIT` queries, failure to close the scan caused file

descriptor leaks for `MyISAM` tables. (Bug #30221, Bug #11746994)

- `SHOW CREATE DATABASE` did not account for the value of the `lower_case_table_names` system

variable. (Bug #21317, Bug #11745926)
