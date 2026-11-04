---
title: "Changes in MySQL 5.6.4 (2011-12-20, Milestone 7)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=230"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Note This is a milestone release, for use at your own risk. Upgrades between milestone releases (or from a milestone release to a GA release) are not supported.

Significant development changes take place in milestone releases and you may encounter compatibility issues, such as data format changes that require attention in addition to the usual procedure of running `mysql_upgrade`. For example, you may find it necessary to dump your data with `mysqldump` before the upgrade and reload it afterward. (Making a backup before the upgrade is a prudent precaution in any case.)

- Condition Handler Changes
- Fractional Seconds Handling
- InnoDB Notes
- Optimizer Notes
- Performance Schema Notes
- Functionality Added or Changed
- Bugs Fixed

> Condition Handler Changes

- Incompatible Change: MySQL now supports the `GET DIAGNOSTICS` statement. `GET DIAGNOSTICS`

provides applications a standardized way to obtain information from the diagnostics area, such as whether the previous SQL statement produced an exception and what it was. See GET DIAGNOSTICS Statement.

In addition, several deficiencies in condition handler processing rules were corrected so that MySQL behavior is more like standard SQL:

- Block scope is used in determining which handler to select. Previously, a stored program was treated

as having a single scope for handler selection.

- Condition precedence is more accurately resolved.
- Diagnostics area clearing has changed. Bug #55843 caused handled conditions to be cleared from the

diagnostics area before activating the handler. This made condition information unavailable within the handler. Now condition information is available within the handler, which can inspect it with the `GET``DIAGNOSTICS` statement. The condition information is cleared when the handler exits, if it has not already been cleared during handler execution.

- Previously, handlers were activated as soon as a condition occurred. Now they are not activated until

the statement in which the condition occurred finishes execution, at which point the most appropriate handler is chosen. This can make a difference for statements that raise multiple conditions, if a condition raised later during statement execution has higher precedence than an earlier condition and there are handlers in the same scope for both conditions. Previously, the handler for the first condition raised would be chosen, even if it had a lower precedence than other handlers. Now the handler for

## MySQL 5.6 Release Notes

the condition with the highest precedence is chosen, even if it is not the first condition raised by the statement.

- Issues that caused the server to exit due to incorrect handler call stack processing were fixed.

The work just described involved several condition-handler bug fixes:

- The `RETURN` statement did not clear the diagnostics area as it should have. Now the diagnostics area

is cleared before executing `RETURN`. This prevents a condition in a nested function call from incorrectly propagating to an outer scope. It also means there is no way to return an SQL warning from a stored function. This change is not backward compatible, but the resulting behavior is more like standard SQL.

- When an SQL `HANDLER` was activated, the handled condition was immediately removed from the

diagnostics area. Consequently, any SQL diagnostic statement executed in the handler was unable to examine the condition that activated the handler. Now condition information is available within the handler.

- If multiple handlers existed at the same level within a stored program, the wrong one could be chosen.

Now the handler for the highest precedence condition is chosen.

- If an error occurred in a context where different handlers were present at different levels of nesting, an

outer handler could be chosen rather than the innermost one.

For more information, see Scope Rules for Handlers. (Bug #12951117, Bug #38806, Bug #11749343,Bug #55852, Bug #11763171, Bug #61392, Bug #12652873, Bug #11660, Bug #11745196, Bug #48637,Bug #11756690, WL #2111, WL #5986)

> Fractional Seconds Handling

- Incompatible Change: MySQL now permits fractional seconds for `TIME`, `DATETIME`, and `TIMESTAMP`

values, with up to microseconds (6 digits) precision. To define a column that includes a fractional seconds part, use the syntax `type_name(fsp)`, where `type_name` is `TIME`, `DATETIME`, or`TIMESTAMP`, and `fsp` is the fractional seconds precision. For example:

```
CREATE TABLE t1 (t TIME(3), dt DATETIME(6));
```

The `fsp` value, if given, must be in the range 0 to 6. A value of 0 signifies that there is no fractional part.

If omitted, the default precision is 0. (This differs from the standard SQL default of 6, for compatibility with previous MySQL versions.)The following items summarize the implications of this change. See also Fractional Seconds in Time Values.

- For `TIME`, `DATETIME`, and `TIMESTAMP` columns, the encoding and storage requirements in new

tables differ from such columns in tables created previously because these types now include a fractional seconds part. This can affect the output of statements that depend on the row format, such

```
as CHECKSUM TABLE.
```

- Due to these changes in encoding and storage requirements for MySQL's `DATETIME` and `TIMESTAMP`

types, importing pre-MySQL 5.6.4 `InnoDB` tables using `ALTER TABLE ... IMPORT TABLESPACE`that contain `DATETIME` and `TIMESTAMP` types into MySQL 5.6.4 (or later) requires a workaround procedure which is described in the “Server Changes” section of Changes in MySQL 5.6 .

- Syntax for temporal literals now produces temporal values: `DATE 'str'`, `TIME 'str'`, and

`TIMESTAMP 'str'`, and the ODBC-syntax equivalents. The resulting value includes a trailing

## MySQL 5.6 Release Notes

fractional seconds part if specified. Previously, the temporal type keyword was ignored and these constructs produced the string value. See Standard SQL and ODBC Date and Time Literals

- Functions that take temporal arguments accept values with fractional seconds. Return values from

temporal functions include fractional seconds as appropriate.

- Three `INFORMATION_SCHEMA` tables, `COLUMNS`, `PARAMETERS`, and `ROUTINES`, now have a

`DATETIME_PRECISION` column. Its value is the fractional seconds precision for `TIME`, `DATETIME`,and `TIMESTAMP` columns, and `NULL` for other data types.

- The C API accommodates fractional seconds as follows:
- In the `MYSQL_FIELD` column metadata structure, the `decimals` member indicates the fractional

seconds precision for `TIME`, `DATETIME`, and `TIMESTAMP` columns. Clients can determine whether a result set temporal column has a fractional seconds part by checking for a nonzero `decimals`value in the corresponding `MYSQL_FIELD` structure. Previously, the `decimals` member indicated the precision for numeric columns and was zero otherwise.

- In the `MYSQL_TIME` structure used for the binary protocol, the `second_part` member indicates the

microseconds part for `TIME`, `DATETIME`, and `TIMESTAMP` columns. Previously, the `second_part`member was unused.

In some cases, previously accepted syntax may produce different results. The following items indicate where existing code may need to be changed to avoid problems:

- Some expressions produce results that differ from previous results. Examples: The `timestamp`

system variable returns a value that includes a microseconds fractional part rather than an integer value. Functions that return a result that includes the current time (such as `CURTIME()`, `SYSDATE()`,or `UTC_TIMESTAMP()`) interpret an argument as an `fsp` value and the return value includes a fractional seconds part of that many digits. Previously, these functions permitted an argument but ignored it.

- `TIME` values are converted to `DATETIME` by adding the time to the current date. (This means that

the date part of the result differs from the current date if the time value is outside the range from`'00:00:00'` to `'23:59:59'`.) Previously, conversion of `TIME` values to `DATETIME` was unreliable.

See Conversion Between Date and Time Types.

- `TIMESTAMP(N)` was permitted in old MySQL versions, but N was a display width rather than fractional

seconds precision. Support for this behavior was removed in MySQL 5.5.3, so applications that are reasonably up to date should not be subject to this issue. Otherwise, code must be rewritten.

Note There may be problems replicating from a master server that understands fractional seconds to an older slave that does not:

- For `CREATE TABLE` statements containing columns that have an `fsp` value

greater than 0, replication will fail due to parser errors.

- Statements that use temporal data types with an `fsp` value of 0 will work for

with statement-based logging but not row-based logging. In the latter case, the

## MySQL 5.6 Release Notes

data types have binary formats and type codes on the master that differ from those on the slave.

- Some expression results will differ on master and slave. For example,

expressions that involve the `timestamp` system variable or functions that return the current time have different results, as described earlier.

(Bug #8523, Bug #11745064, WL #946)

> InnoDB Notes

- MySQL now supports `FULLTEXT` indexes for `InnoDB` tables. The core syntax is very similar to

the `FULLTEXT` capability from earlier releases, with the `CREATE TABLE` and `CREATE INDEX`statements, and `MATCH() AGAINST()` clause in the `SELECT` statement. The new @ operator allows proximity searches for terms that are near each other in the document. The detailed search processing is controlled by a new set of configuration options: `innodb_ft_enable_stopword`,

```
innodb_ft_server_stopword_table, innodb_ft_user_stopword_table,
innodb_ft_cache_size, innodb_ft_min_token_size, and innodb_ft_max_token_size.
```

You can monitor the workings of the `InnoDB` full-text search system by querying new

```
INFORMATION_SCHEMA tables: innodb_ft_default_stopword, innodb_ft_index_table,
innodb_ft_index_cache, innodb_ft_config, innodb_ft_deleted, and
```

`innodb_ft_being_deleted`. (WL #5538)

> Optimizer Notes

- These query optimizer improvements were implemented:
- The optimizer detects and optimizes away these useless query parts within `IN`/`ALL`/`SOME`/`EXISTS`

subqueries:

```
- DISTINCT
```

- `GROUP BY`, if there is no `HAVING` clause and no aggregate functions
- `ORDER BY`, which has no effect because `LIMIT` is not supported in these subqueries

(WL #5953)

> Performance Schema Notes

- The Performance Schema has these additions:
- The Performance Schema now permits instrument and consumer configuration at server

startup, which previously was possible only at runtime using `UPDATE` statements for the`setup_instruments` and `setup_consumers` tables. This change was made because configuration at runtime is too late to disable instruments that have already been initialized during server startup. For example, the `wait/sync/mutex/sql/LOCK_open` mutex is initialized once during server startup, so attempts to disable the corresponding instrument at runtime have no effect.

To control an instrument at server startup, use an option of this form:

```
--performance-schema-instrument='instrument_name=value'
```

Here, `instrument_name` is an instrument name such as `wait/sync/mutex/sql/LOCK_open`,and `value` is one of these values:

- `off`, `false`, or 0: Disable the instrument

## MySQL 5.6 Release Notes

- `on`, `true`, or 1: Enable and time the instrument
- `counted`: Enable and count (rather than time) the instrument

Each `--performance-schema-instrument` option can specify only one instrument name, but multiple instances of the option can be given to configure multiple instruments. In addition, patterns are permitted in instrument names to configure instruments that match the pattern. To configure all condition synchronization instruments as enabled and counted, use this option:

```
--performance-schema-instrument='wait/synch/cond/%=counted'
```

To disable all instruments, use this option:

```
--performance-schema-instrument='%=off'
```

Longer instrument name strings take precedence over shorter pattern names, regardless of order. For information about specifying patterns to select instruments, see Naming Instruments or Consumers for Filtering Operations.

An unrecognized instrument name is ignored. It is possible that a plugin installed later may create the instrument, at which time the name is recognized and configured.

To control a consumer at server startup, use an option of this form:

```
--performance-schema-consumer_consumer_name=value
```

Here, `consumer_name` is a consumer name such as `events_waits_history`, and `value` is one of these values:

- `off`, `false`, or 0: Do not collect events for the consumer
- `on`, `true`, or 1: Collect events for the consumer

For example, to enable the `events_waits_history` consumer, use this option:

```
--performance-schema-consumer-events-waits-history=on
```

The permitted consumer names can be found by examining the `setup_consumers` table. Patterns are not permitted.

Along with the preceding changes to permit configuration at server startup, the default instrument and consumer configuration has changed. Previously, all instruments and consumers were enabled by default. Now, instruments are disabled except the statement, I/O, and idle instruments. Consumers

## MySQL 5.6 Release Notes

are disabled except the global, thread, and current-statement consumers. These changes produce a default configuration with a low overhead.

- Tables that have an `EVENT_ID` column now also have an `END_EVENT_ID` column to support

determination of nested event relationships:

```
- events_waits_current, events_waits_history, events_waits_history_long
- events_stages_current, events_stages_history, events_stages_history_long
- events_statements_current, events_statements_history,
events_statements_history_long
```

As before, `EVENT_ID` is populated with the thread current event counter when an event starts. In addition, `END_EVENT_ID` is `NULL` until the event ends, at which point it is set to the new thread current event counter. This permits the relationship “event B is included in event A” to be determined using the following expression, without having to follow each inclusion relationship using `NESTING_EVENT_ID`:

```
A.EVENT_ID <= B.EVENT_ID AND B.END_EVENT_ID <= A.END_EVENT_ID
```

- The Performance Schema aggregates file I/O operations in two places, the

`events_waits_summary_xxx` tables and the `file_summary_xxx` tables. It was possible to join the `events_waits_summary_global_by_event_name` table to the`file_summary_by_event_name` by using the `EVENT_NAME` column. However, it was not possible to do the same with the `events_waits_summary_by_instance` and `file_summary_by_instance`tables because the former uses `OBJECT_INSTANCE_BEGIN` as the instance identifier and the latter uses `FILE_NAME`. This means that it was possible to obtain both file I/O latency and usage per file, but not to correctly correlate latency to usage when there was more than one form of file (such as multiple redo logs, table files, and so forth).

To address this issue, the `file_summary_by_instance` table now has an`OBJECT_INSTANCE_BEGIN` column. In addition, both `file_summary_by_instance` and`file_summary_by_event_name` have additional aggregation columns (such as timer wait information), which in many cases makes it possible to obtain the desired summary information without need for a join at all.

If you upgrade to this MySQL release from an earlier version, you must run `mysql_upgrade` (and restart the server) to incorporate these changes into the `performance_schema` database.

For more information, see MySQL Performance Schema. (WL #5863, WL #5908, WL #5461)

> Functionality Added or Changed

- Performance; InnoDB: New optimizations apply to read-only `InnoDB` transactions. See Optimizing

InnoDB Read-Only Transactions for details. The new optimizations make autocommit more applicable to `InnoDB` queries than before, as a way to signal that a transaction is read-only because it is a single-statement `SELECT`. (WL #6046)

- Performance; InnoDB: You can now set the `InnoDB` page size for uncompressed tables to 8KB

or 4KB, as an alternative to the default 16KB. This setting is controlled by the `innodb_page_size`configuration option. You specify the size when creating the MySQL instance. All `InnoDB` tablespaces within an instance share the same page size. Smaller page sizes can help to avoid redundant or inefficient I/O for certain combinations of workload and storage devices, particularly SSD devices with small block sizes. (WL #5756)

## MySQL 5.6 Release Notes

- Replication: Previously, replication slaves could connect to the master server only through master

accounts that use native authentication. Now replication slaves can also connect through master accounts that use nonnative authentication if the required client-side plugin is installed on the slave side in the directory named by the slave `plugin_dir` system variable. (Bug #12897501)

- The optimizer trace capability now tracks temporary tables created by the server during statement

execution. (Bug #13400713)

- Performance of metadata locking operations on Windows XP systems was improved by instituting a

cache for metadata lock objects. This permits the server to avoid expensive operations for creation and destruction of synchronization objects on XP. A new system variable, `metadata_locks_cache_size`,permits control over the size of the cache. The default size is 1024. (Bug #12695572)

- Upgrading from an `Advanced GPL` RPM package to an `Advanced` RPM package did not work. Now

on Linux it is possible to use `rpm -U` to replace any installed MySQL product by any other of the same release family. It is not necessary to remove the old produce with `rpm -e` first. (Bug #11886309)

- The `make_win_bin_dist` script is no longer used and has been removed from MySQL distributions

and the manual. (Bug #58241)

- `MEMORY` table creation time is now available in the `CREATE_TIME` column of the

`INFORMATION_SCHEMA.TABLES` table and the `Create_time` column of `SHOW TABLE STATUS` output.

(Bug #51655, Bug #11759349)

- Previously, MySQL servers from 5.1 and up refused to open `ARCHIVE` tables created in 5.0 because

opening them caused a server crash. The server now can open 5.0 `ARCHIVE` tables, and `REPAIR``TABLE` updates them to the format used in 5.6. However, the recommended upgrade procedure is still to dump 5.0 `ARCHIVE` tables before upgrading and reload them after upgrading. (Bug #48633, Bug#11756687)

- Error messages that referred only to an error code now also include the corresponding error description.

(Bug #48348, Bug #11756433)

- The MySQL code base was changed to permit use of the C++ Standard Library and to enable

exceptions and runtime type information (RTTI). This change has the following implications:

- Libraries and executables depend on some C++ standard library. On Linux, this has not been the case

previously. On Solaris, the default dependency has changed from the default library to `libstlport`,which is now included with binary distributions for users whose system does not have it.

- The `-fno-rtti` and `-fno-exceptions` options are no longer used to build plugins, such as storage

engines. Users who write their own plugins should omit these options if they were using tem.

- C++ users who compile from source should set `CXX` to a C++ compiler rather than a C compiler. For

example, use `g++` rather than `gcc`. This includes the server as well as client programs.

- `mysql_config` now has a `--cxxflags` option. This is like the `--cflags` option, but produces flags

appropriate for a C++ compiler rather than a C compiler.

- Loadable functions can be written in C++ using standard library features.

(WL #5825)

> Bugs Fixed

- Security Enhancement; Replication: The `START SLAVE` statement now accepts `USER` and `PASSWORD`

options. By default, MySQL native authentication is used, and the user name and password are stored

## MySQL 5.6 Release Notes

in the `master.info` repository. This behavior can be overridden by additionally specifying the name(`DEFAULT_AUTH`) and location (`PLUGIN_DIR`) of an authentication plugin when issuing `START SLAVE`. .

As part of this change, warnings are now issued in the following cases:

```
1. If START SLAVE USER="..." PASSWORD="..." or CHANGE MASTER TO
```

`MASTER_USER="..." MASTER_PASSWORD="..."` is executed using an unencrypted connection,the warning message `Sending passwords in plain text without SSL/TLS is``extremely insecure` is generated (`ER_INSECURE_PLAIN_TEXT`).

2. If the user name and password are stored in or read from the `master.info` repository in the course

of executing `CHANGE MASTER TO`, a warning message is printed out to the error log: `Storing`

```
MySQL user name or password information in the master.info repository is
not secure and is therefore not recommended (ER_INSECURE_CHANGE_MASTER).
```

Note The text of a running `START SLAVE` statement, including values for `USER` and`PASSWORD`, can be seen in the output of a concurrent `SHOW PROCESSLIST`statement. The complete text of a `CHANGE MASTER TO` statement is also visible

```
to SHOW PROCESSLIST.
```

See also Pluggable Authentication. (Bug #13083642, WL #4143)

- Incompatible Change; Replication: The statements in the following list are now marked as unsafe for

statement-based replication. This is due to the fact that each of these statements depends on the results of a `SELECT` statement whose order cannot always be determined. When using `STATEMENT` logging mode, a warning is issued in the binary log for any of these statements; when using `MIXED` logging mode, the statement is logged using the row-based format.

```
- INSERT ... SELECT ... ON DUPLICATE KEY UPDATE
- REPLACE ... SELECT
- CREATE TABLE ... IGNORE SELECT
- CREATE TABLE ... REPLACE SELECT
- INSERT IGNORE ... SELECT
- UPDATE IGNORE
```

When upgrading, you should note the use of these statements in your applications, keeping in mind that a statement that inserts or replaces rows obtained from a `SELECT` can take up many times as much space in the binary log when logged using row-based format than when only the statement itself is logged. Depending on the number and size of the rows selected and inserted (or replaced) by any such statements, the difference in size of the binary log after the logging of these statements is switched from statement-based to row-based can potentially be several orders of magnitude. See Advantages and Disadvantages of Statement-Based and Row-Based Replication. (Bug #11758262, Bug #50439)

- Incompatible Change: Previously, “Aborted connection” errors were written to the error log based on

the session value of `log_warnings`, which permitted users with minimal privileges to cause many messages to be written to the log unless restricted by the `MAX_CONNECTIONS_PER_HOUR` resource limit. Now this logging is based on the global `log_warnings` variable. There are no remaining uses of the session `log_warnings` variable, so it has been removed and the variable now has only a global value. (Bug #53466, Bug #11761014)

## MySQL 5.6 Release Notes

- Important Change; InnoDB: If an `ALTER TABLE` statement failed for an `InnoDB` table due to an error

code from an underlying file-renaming system call, `InnoDB` could lose track of the `.ibd` file for the table.

This issue only occurred when the `innodb_file_per_table` configuration option was enabled, and when the low-level error persisted through thousands of retry attempts. In MySQL 5.1, this issue applied to the InnoDB Plugin but not the built-in InnoDB storage engine.

For example, if you encounter an error like the following:

```
mysql> ALTER TABLE sb2 ADD COLUMN d2 INT;
ERROR 1025 (HY000): Error on rename of './sbtest/#sql-1eb9_1' to
'./sbtest/sb2' (errno: -1)
```

you might be able to access the `#sql*` table by copying an `.frm` file from a table with an identical schema. The table name to use for the `.frm` filewould be `sbtest.#mysql50##sql-1eb9_1` in the preceding example. (Bug #12884631, Bug #62146)

- Important Change; Replication: Setting an empty user in a `CHANGE MASTER TO` statement caused

an invalid internal result and is no longer permitted. Trying to use `MASTER_USER=''` or setting`MASTER_PASSWORD` while leaving `MASTER_USER` unset causes the statement to fail with an error. (Bug#13427949)

- Performance; InnoDB: The process of deallocating the `InnoDB` Adaptive Hash Index was made faster,

during shutdown or when turning off the AHI with the statement:

```
SET GLOBAL innodb_adaptive_hash_index=OFF;
```

(Bug #13006367, Bug #62487)

- Performance; InnoDB: This fix improves the performance of instrumentation code for `InnoDB` buffer

pool operations. (Bug #12950803, Bug #62294)

- Performance; InnoDB: This fix improved the efficiency and concurrency of freeing pages in the `InnoDB`

buffer pool when performing a `DROP TABLE` for an `InnoDB` table when the `innodb_file_per_table`option is enabled.

This change is most noticeable for systems with large buffer pools. During the drop operation, one traversal of the buffer pool memory structure is changed from the LRU list (the entire buffer pool) to the flush list (a much smaller structure). The LRU scanning is reduced, but not entirely eliminated. The buffer pool mutex is also released periodically, so that if the drop operation takes significant time, other threads can proceed concurrently. (Bug #11759044, Bug #51325)

- InnoDB: An internal deadlock could occur within `InnoDB`, on a server doing a substantial amount of

change buffering for DML operations, particularly `DELETE` statements. (Bug #13340047)

- InnoDB: Fixed a compilation problem that affected the `InnoDB` source code with `gcc` 4.6.1. The

affected `InnoDB` source file was `btr/btr0cur.c`. (Bug #13116045)

- InnoDB: Querying the `INFORMATION_SCHEMA.INNODB_SYS_TABLESTATS` table could cause the

server to halt with an assertion error, in debug builds only. (Bug #12960058)

- InnoDB: Valgrind errors when building with the settings `innodb_checksum_algorithm=innodb` and

`innodb_checksum_algorithm=crc32` were fixed. (Bug #12939557)

- InnoDB: Unused functions were removed from the internal `InnoDB` code related to mini-transactions, to

clarify the logic. (Bug #12626794, Bug #61240)

- InnoDB: Lookups using secondary indexes could give incorrect matches under a specific set of

conditions. The conditions involve an index defined on a column prefix, for a BLOB or other long column

## MySQL 5.6 Release Notes

stored outside the index page, with a table using the Barracuda file format. (Bug #12601439, Bug#12543666)

- InnoDB: An `UPDATE` statement for an `InnoDB` table could hang. The issue affects tables using the

Barracuda file format and having multiple indexes on column prefixes. The size of an undo log record could exceed the page size, even though the total size of the column prefixes was less than the page size (usually 16KB). In MySQL 5.5 and higher, this error is now reported using the new code`ER_UNDO_RECORD_TOO_BIG`. In MySQL 5.1 with the InnoDB Plugin, this error is reported using the existing code `ER_TOO_BIG_ROWSIZE`. (Bug #12547647)

- InnoDB: This fix corrects cases where the MySQL server could hang or abort with a `long semaphore`

`wait` message. (This is a different issue than when these symptoms occurred during a `CHECK TABLE`statement.) (Bug #11766591, Bug #59733)

- InnoDB: Issuing `INSERT...ON DUPLICATE KEY` statements for `InnoDB` tables from concurrent

threads could cause a deadlock, particularly with the `INSERT...ON DUPLICATE KEY UPDATE` form.

The problem could also be triggered by issuing multiple `INSERT IGNORE` statements. The fix avoids deadlocks caused by the same row being accessed by more than one transaction. Deadlocks could still occur when multiple rows are inserted and updated simultaneously by different transactions in inconsistent order; those types of deadlocks require the standard error handling on the application side,of re-trying the transaction. (Bug #11759688, Bug #52020, Bug #12842206)

- Partitioning: `CHECKSUM TABLE` returned 0 for a partitioned table unless the statement was used with

the `EXTENDED` option. (Bug #11933226, Bug #60681)

- Partitioning: Error 1214 (`ER_TABLE_CANT_HANDLE_FT`), given when trying to use a `FULLTEXT`

index with a partitioned table, displayed the misleading text `The used table type doesn't``support FULLTEXT indexes` was misleading and has been replaced with Error 1752(`ER_FULLTEXT_NOT_SUPPORTED_WITH_PARTITIONING`) which shows the more accurate `FULLTEXT``index is not supported for partitioned tables`. (Bug #11763825, Bug #56590)

- Partitioning: Using `ALTER TABLE` to remove partitioning from a valid `MyISAM` table could corrupt it.

(Bug #52599, Bug #11760213)

- Replication: The value set for the `slave_parallel_workers` system variable was not always

honored correctly; in such cases a random value was used. (Bug #13334470)

- Replication: Execution of `LOAD DATA` on a `MyISAM` table having an after-insert trigger which wrote into

an `InnoDB` table caused multithreaded statement-based replication to abort with error 1742 (`Cannot``execute the current event group in the parallel mode`). (Bug #12982188)

- Replication: Several warnings and informational messages were revised for typographic errors and

clarity. (Bug #12947248, Bug #12978113)

- Replication: When a statement containing a large number of rows to be applied on a slave table that

does not contain a primary key, a considerable amount of time can be needed to find and change all the rows that are to be changed. The current fix helps diagnose this issue by printing a message to the error log if the execution time for a given statement replicated using row-based replication takes more than 60 seconds. `log_warnings` must be greater than 1 for this message to be printed to the error log. (Bug#11760927, Bug #53375)

- Replication: `mysqlbinlog` `--hexdump` printed the last row of the hex dump incorrectly, in two ways:
1. If the length of the last row was eight bytes, the end of the previous row was copied to the end of the

last row, padding the last row to full length.

2. If the length of the last row was less than sixteen bytes, its textual representation was not aligned

with that of previous rows.

## MySQL 5.6 Release Notes

(Bug #11747887, Bug #34386)

- Replication: A replication master could send damaged events to slaves after the binary log disk on the

master became full. To correct this issue, only complete events are now pushed by the master dump thread to the slave I/O thread. In addition, the error text that the master sends to the slave when an incomplete event is found now states that the incomplete event may have been caused by running out of disk space on the master, and provides coordinates of the first and the last event bytes read. (Bug#11747416, Bug #32228)References: See also: Bug #64035, Bug #13593869.

- Replication: `--replicate-rewrite-db=from_name->to_name` did not work correctly when the

name of the source database (`from_name`) consisted of only a single character. (Bug #34332, Bug#11747866)

- An incorrect `InnoDB` assertion could cause the server to halt. This issue only affected debug builds.

The assertion referenced the source file `btr0pcur.ic` and the variable `cursor->pos_state`. (Bug#13358468)

- A derived table with more than 64 columns caused a server crash. (Bug #13354889)
- With `InnoDB` change buffering enabled and `innodb_page_size` set to an 8K or 4K page size, an

`UPDATE` statement could fail if a column being updated contained a value longer than 1/8th of the page size. (Bug #13336585)

- Writes to the slow log involved a call to `thd->current_utime()` even if no log entries ended up being

written, unnecessarily reducing performance. (Bug #13326965)

- Rounding `DBL_MAX` returned `DBL_MAX`, not 'inf'. (Bug #13261955)
- For materialized temporary tables, a missing key length check could cause incorrect query results. (Bug

#13261277)

- Access privileges were checked for each stored program instruction, even if the instruction used no

tables, resulting in reduced performance. (Bug #13251277)

- The error message for `ER_EVENT_CANNOT_ALTER_IN_THE_PAST` was incorrect. (Bug #13247871)
- During the table-opening process, memory was allocated and later freed that was needed view loading,

even for statements that did not use views. These unnecessary allocation and free operations are no longer done. (Bug #13116518)

- Subqueries with `OUTER JOIN` could return incorrect results if the subquery referred to a column from

another `SELECT`. (Bug #13068506)

- Writes to `MyISAM` temporary tables could include uninitialized data, which could contain sensitive

information. Now only bytes containing initialized data are copied, which also improves performance.

(Bug #12997905)

- The Performance Schema nested some network I/O events within the wrong statement. (Bug

#12981100)

- `mysql_plugin` mishandled the `--plugin-ini`, `--mysqld`, and `--my-print-defaults` options

under some circumstances. (Bug #12968815)

- `mysql_plugin` returned the wrong error code from failed server bootstrap execution. (Bug #12968567)

## MySQL 5.6 Release Notes

- Internal conversion of zero to binary and back could yield a result with incorrect precision. (Bug

#12911710)

- Valgrind warnings generated by `filesort` operations were fixed. (Bug #12856915)
- An `IN`-to-`EXISTS` subquery transformation could yield incorrect results if the outer value list contained

`NULL`. (Bug #12838171)

- With index condition pushdown enabled, `STRAIGHT_JOIN` queries could produce incorrect results. (Bug

#12822678, Bug #12724899)

- The result of `ROUND()` was incorrect for certain numbers. (Bug #12744991)
- A warning resulting from use of `SPACE()` referred to `REPEAT()` in the warning message. (Bug

#12735829)

- `IN` and `EXISTS` subqueries with `DISTINCT` and `ORDER BY` could return incorrect results. (Bug

#12709738)

- A memory leak occurred due to failure to clean up after `QUICK_INDEX_MERGE_SELECT/Unique`. (Bug

#12694872, Bug #14542543)

- Several improvements were made to the `libedit` library bundled with MySQL distributions, and that is

available for all platforms that MySQL supports except Windows.

- Navigation keys did not work for UTF-8 input.
- Word navigation and delete operations did not work for UTF-8 input with Cyrillic characters.
- Nonlatin characters were corrupted in overwrite mode for UTF-8 input.
- Long queries caused the statement history file to become corrupted.
- The Alt key caused history operations to fail.

(Bug #12605400, Bug #12613725, Bug #12618092, Bug #12624155, Bug #12617651, Bug #12605388)

- `SELECT SQL_BUFFER_RESULT` query results included too many rows if a `GROUP BY` clause was

optimized away. (Bug #12578908)

- `decimal_round()` could cause a server exit when processing long numeric strings. (Bug #12563865)
- `mysqldump` `--all-databases` did not dump the replication log tables. (They could be dumped only by

naming them explicitly when invoking `mysqldump`, and using the `--master-data` option.)As a result of the fix for this problem, it is now possible to execute statements requiring read locks on the replication log tables at any time, while any statements requiring a write lock on either or both of these tables are disallowed whenever replication is in progress. For more information, see Relay Log and Replication Metadata Repositories. (Bug #12402875, Bug #60902)

- The client-server protocol now has the client send authentication data as length-

encoded strings so that data longer than 256 bytes can be sent. This is done using the`CLIENT_PLUGIN_AUTH_LENENC_CLIENT_DATA` client capability. (Bug #11878962)

- `mysqld_safe` did not properly check for an already running instance of `mysqld`. (Bug #11878394)
- `SUM(DISTINCT)` incorrectly converted `DATE`, `DATETIME`, `TIME`, and `TIMESTAMP` arguments to `YEAR`.

(Bug #73543, Bug #19427648)

## MySQL 5.6 Release Notes

- If index condition pushdown access was chosen and then abandoned, some variables were not cleared,

leading to incorrect query results. (Bug #62533)

- The `CMake` configuration checks did not properly test whether the C compiler supports the `inline`

keyword. (Bug #61708, Bug #12711108)

- For a `lower_case_table_names` value of 1 or 2 and a database having a mixed-case name, calling

a stored function using a fully qualified name including the database name failed. (Bug #60347, Bug#11840395)

- `mysql_upgrade` did not upgrade the system tables or create the `mysql_upgrade_info` file when run

with the `--write-binlog` or `--skip-write-binlog` option. (Bug #60223, Bug #11827359)

- A multiple-table `UPDATE` statement required the `UPDATE` privilege on a view which was only read if the

view was processed using the merge algorithm. (Bug #59957, Bug #11766767)

- When a join operation contained a view, the optimizer sometimes failed to associate the view's `WHERE`

clause with the first table or view in a join when it was possible to do so, resulting in a less efficient query. (Bug #59696, Bug #11766559)

- An assertion was raised when selecting from a view that selects from a view that used a loadable

function that had been deleted. (Bug #59546, Bug #11766440)

- The help message for `mysql_install_db` did not indicate that it supports the `--defaults-file`, `--`

`defaults-extra-file` and `--no-defaults` options. (Bug #58898, Bug #11765888)

- `mysql_install_db` printed the `--skip-grant-tables` server option as `--skip-grant` in one of

its error messages. (Bug #58534, Bug #11765553)

- An assertion designed to detect zero-length sort keys also was raised when the entire key set fit in

memory. (Bug #58200, Bug #11765254)

- During optimization, `ZEROFILL` values may be converted to string constants. However, `CASE`

expressions did not handle switching data types after the planning stage, leading to `CASE` finding a null pointer instead of its argument. (Bug #57135, Bug #11764313)

- If a plugin was uninstalled, thread local variables for plugin variables of string type with wth

`PLUGIN_VAR_MEMALLOC` flag were not freed. (Bug #56652, Bug #11763882)

- Deadlock could occur when these four things happened at the same time: 1) An old dump thread was

waiting for the binary log to grow. 2) The slave server that replicates from the old dump thread tried to reconnect. During reconnection, the new dump thread tried to kill the old dump thread. 3) A `KILL`statement tried to kill the old dump thread. 4) An `INSERT` statement caused a binary log rotation. (Bug#56299, Bug #11763573)

- `myisampack` could create corrupt `FULLTEXT` indexes when compressing tables. (Bug #53646, Bug

#11761180)

- The `SQL_BIG_RESULT` modifier could change the results for queries that included a `GROUP BY` clause.

(Bug #53534, Bug #11761078)

- `ARCHIVE` tables with `NULL` columns could cause server crashes or become corrupt under concurrent

load. (Bug #51252, Bug #11758979)

- `InnoDB` used incorrect identifier quoting style in an error message that resulted in an error if a user

followed the suggestion in the message. (Bug #49556, Bug #11757503)

- `OPTIMIZE TABLE` could corrupt `MyISAM` tables if `myisam_use_mmap` was enabled. (Bug #49030, Bug

#11757032)

## MySQL 5.6 Release Notes

- Concurrent access to `ARCHIVE` tables could cause corruption. (Bug #42784, Bug #11751793)
- A query that selected a `GROUP_CONCAT()` function result could return different values depending on

whether an `ORDER BY` of the function result was present. (Bug #41090, Bug #11750518)

- A linking problem prevented the `FEDERATED` storage engine plugin from loading. (Bug #40942, Bug

#11750417)

- Subqueries could return incorrect results when materialization was enabled. (Bug #40037, Bug

#11749901, Bug #12705660, Bug #12908058)

- For debug builds, an assertion could be raised for `ALTER` statements that performed a `RENAME`

operation. This occurred for storage engine handlertons that exposed the `HTON_FLUSH_AFTER_RENAME`flag. (Bug #38028, Bug #11749050)

- The estimate of space required for `filesort` operations could be too high, resulting in inefficient

initialization. (Bug #37359, Bug #11748783)

- An `ALTER TABLE` that included an `ADD ... AFTER` operation to add a new column after a column

that had been modified earlier in the statement failed to find the existing column. (Bug #34972, Bug#11748057)

- For `FEDERATED` tables, loss of connection to the remote table during some insert operations could cause

a server crash. (Bug #34660, Bug #11747970)

- For some queries, the `index_merge` access method was used even when more expensive then `ref`

access. (Bug #32254, Bug #11747423)

- Collation for the `SPACE()` function was determined by the parse time value of the

`collation_connection` system variable (instead of the runtime value), which could give unexpected results from prepared statements, triggers, and stored procedures. (Bug #23637, Bug #11746123)
