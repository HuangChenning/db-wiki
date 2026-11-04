---
title: "Changes in MySQL 5.6.9 (2012-12-11, Release Candidate)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=157"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Deprecation and Removal Notes
- Installation Notes
- Functionality Added or Changed
- Bugs Fixed

> Deprecation and Removal Notes

- Microsoft Windows: Windows Vista, Windows Server 2008, and newer support native symbolic linking

using the `mklink` command. This makes the MySQL Server implementation of database symbolic links using `.sym` files redundant, so that mechanism is now deprecated and will be removed in a future MySQL release. See Using Symbolic Links for Databases on Windows. (WL #6561)

> Installation Notes

- The `--random-passwords` option for `mysql_install_db` is now supported for MySQL install

operations (not upgrades) using Solaris PKG packages.

## MySQL 5.6 Release Notes

> Functionality Added or Changed

- Incompatible Change; Replication: A number of variable and other names relating to GTID-based

replication have been changed, with a view to making these names more appropriate and meaningful.

The old names are no longer supported.

The features so renamed are shown in the following list:

- The `disable_gtid_unsafe_statements` system variable has been renamed

```
enforce_gtid_consistency.
```

- The `gtid_done` server system variable has been renamed `gtid_executed`.

The `gtid_lost` server system variable has been renamed `gtid_purged`; in addition, this variable is no longer read-only.

- The `SQL_THREAD_WAIT_AFTER_GTIDS()` function has been renamed

```
WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS().
```

For more information, see Replication with Global Transaction Identifiers, and Global Transaction ID Options and Variables. (Bug #14775984)

- For client connections restrictd by the server because the client account password is expired, the server

now permits `SET PASSWORD` only if the account named in the statement matches the account used by the client. (Bug #14807074)References: See also: Bug #14698309.

- The server now provides thread information (for `SHOW PROCESSLIST`) to indicate the progress of in-

place `ALTER TABLE` operations:

```
- preparing for alter table
```

The server is preparing to execute an in-place `ALTER TABLE`.

```
- altering table
```

The server is in the process of executing an in-place `ALTER TABLE`.

```
- committing alter table to storage engine
```

The server has finished an in-place `ALTER TABLE` and is committing the result.

(Bug #14790408)

- `InnoDB` automatically extends each secondary index by appending the primary key columns to it.

Previously, the optimizer did not take into account the primary key columns of the extended secondary index when determining how and whether to use that index. Now the optimizer takes the primary key columns into account, which can result in more efficient query execution plans and better performance.

The optimizer can use extended secondary keys for `ref`, `range`, and `index_merge` index access, for Loose Index Scan, for join and sorting optimization, and for `MIN()`/`MAX()` optimization.

The new `use_index_extensions` flag of the `optimizer_switch` system variable permits control over whether the optimizer takes the primary key columns into account when determining how to use an`InnoDB` table's secondary indexes. By default, `use_index_extensions` is enabled. To check whether disabling use of index extensions will improve performance, use this statement:

## MySQL 5.6 Release Notes

```
SET optimizer_switch = 'use_index_extensions=off';
```

For more information, see Use of Index Extensions. (Bug #62025, Bug #12814559, Bug #56714, Bug#11763940, WL #6266)

- `mysqld` now writes dates to the error log in ISO (`YYYY-MM-DD hh:mm:ss`) format. It also includes its

process ID following the date. Thanks to Davi Arnaut for the patch. (Bug #56240, Bug #11763523)

> Bugs Fixed

- Incompatible Change: The `THREAD_ID` column in Performance Schema tables was widened from `INT`

to `BIGINT` to accommodate 64-bit values.

Note As a consequence of this change, the `PROCESSLIST_ID` column of the `threads`table is now `NULL` for background threads. Previously, the value was 0 for background threads.

If you upgrade to this MySQL release from an earlier version, you must run `mysql_upgrade` (and restart the server) to incorporate this change to the `performance_schema` database. (Bug #14664453)

- Incompatible Change: `LAST_INSERT_ID(expr)` did not work for `expr` values greater than the largest

signed `BIGINT` value. Such arguments now are accepted, with some consequences for compatibility with previous versions:

- `LAST_INSERT_ID()` now returns a `BIGINT UNSIGNED` value, not a `BIGINT` (signed) value.
- `LAST_INSERT_ID(expr)` now returns an unsigned integer value, not a signed integer value.
- For `AUTO_INCREMENT` columns, negative values are no longer supported.

(Bug #20964, Bug #11745891)

- Incompatible Change: Connection ID (thread ID) values greater than 32 bits can occur on some

systems (such as busy or long-running 64-bit systems), causing these problems:

- Connection IDs written to the general query log and slow query log were incorrect. This was true for

logging to both files and tables.

- The `CONNECTION_ID()` function could return a value with a data type too small for values larger than

32 bits.

- The `mysql_thread_id()` and `mysql_kill()` C API functions did not handle ID values

larger than 32 bits. This could result in killing the wrong thread; for example, if you invoked

```
mysql_kill(mysql_thread_id()).
```

Connection IDs now are permitted to be 64-bit values when the server supports them (when built with 64-bit data types), which has these effects:

- Connection IDs are logged correctly to the general query log and slow query log.

Note This change involves a modification to the log tables, so after upgrading to this release, you must run mysql_upgrade and restart the server.

## MySQL 5.6 Release Notes

- `CONNECTION_ID()` returns a data type appropriate for values larger than 32 bits.
- `mysql_thread_id()` is unchanged; the client/server protocal has only 4 bytes for the ID value. This

function returns an incorrect (truncated) value for connection IDs larger than 32 bits and should be avoided.

`mysql_kill()` still cannot handle values larger than 32 bits, but to guard against killing the wrong thread now returns an error in these cases:

- If given an ID larger than 32 bits, `mysql_kill()` returns a `CR_INVALID_CONN_HANDLE` error.
- After the server's internal thread ID counter reaches a value larger than 32 bits, it returns an

`ER_DATA_OUT_OF_RANGE` error for any `mysql_kill()` invocation and `mysql_kill()` fails.

To avoid problems with `mysql_thread_id()` and `mysql_kill()`, do not use them. To get the connection ID, execute a `SELECT CONNECTION_ID()` query and retrieve the result. To kill a thread,execute a `KILL` statement.

(Bug #19806, Bug #11745768, Bug #65715, Bug #14236124, Bug #44728, Bug #11753308)

- Important Change; InnoDB: A DML statement using the index merge access method could lock many

rows from the table, even when those rows were not part of the final result set. This fix reduces the excessive locking by releasing the locks of unmatched rows. This optimization affects only transactions with isolation level equal to or less strict than `READ COMMITTED`; it does not apply to transactions using`REPEATABLE READ` or `SERIALIZABLE` isolation level. (Bug #14226171)

- Important Change; Replication: Statements involving the Performance Schema tables should not

be written to the binary log, because the content of these tables is applicable only to a given MySQL Server instance, and may differ greatly between different servers in a replication topology. The database administrator should be able to configure (`INSERT`, `UPDATE`, or `DELETE`) or flush (`TRUNCATE TABLE`)performance schema tables on a single server without affecting others. However, when using replication with GTIDs enabled (see Replication with Global Transaction Identifiers), warnings about unsafe statements updating Performance Schema tables were elevated to errors, preventing the use of`performance_schema` and GTIDs together.

Similar problems were encountered with replication and system logging tables when GTIDs were enabled.

This fix introduces the concept of a nonreplicated or local table. Now when MySQL replication encounters a table that is marked as local, updates to this table are ignored.

This fix defines as local the following tables, which are no longer replicated:

- All tables in the `performance_schema` database

```
- mysql.general_log
- mysql.slow_log
- mysql.slave_relay_log_info
- mysql.slave_master_info
```

## MySQL 5.6 Release Notes

```
- mysql.slave_worker_info
```

Before this fix, statements using the `performance_schema` and other tables just listed were handled by being marked as unsafe for replication, which caused warnings during execution; the statements were nonetheless written to the binary log, regardless of the logging format in effect.

Existing replication behavior for tables in the `INFORMATION_SCHEMA` database is not changed by this fix.

For more information, see MySQL Performance Schema. See also MySQL Server Logs, and Replication Metadata Repositories. For information about general and slow query log tables, see Selecting General Query Log and Slow Query Log Output Destinations. (Bug #14741537)

- Important Change; Replication: Because running the server with GTIDs enabled prevented changes

to nontransactional tables, programs such as `mysql_upgrade` and `mysql_install_db` were unable to operate on system tables that used the MyISAM storage engine and therefore could not function correctly. Now, when running with `--enforce-gtid-consistency` (required whenever `--gtid-``mode=ON`), the server allows single statements on nontransactional tables. (Bug #14722659)

- Important Change; Replication: Formerly, the value of the `Seconds_Behind_Master` column

in the output of `SHOW SLAVE STATUS` was always set to `NULL` whenever the SQL thread or the I/O thread was stopped. Now, this column is set to `NULL` only if the SQL thread is not running, or if the I/O thread is not running following a check to determine whether or not the SQL thread has processed all of the relay log. (If the SQL thread has finished processing and the I/O thread is running,`Seconds_Behind_Master` is 0.) (Bug #12946333)

- Performance; InnoDB: The timing values for low-level `InnoDB` read operations were adjusted for

better performance with fast storage devices, such as SSD. This enhancement primarily affects read operations for `BLOB` columns in compressed tables. (Bug #13702112, Bug #64258)

- InnoDB; Partitioning: Previously, when attempting to optimize one or more partitions of a partitioned

table that used a storage engine that does not support partition-level `OPTIMIZE`, such as `InnoDB`,

```
MySQL reported Table does not support optimize, doing recreate + analyze
```

`instead`, then re-created the entire table, but did not actually analyze it. Now in such cases, the

```
warning message is, Table does not support optimize on partitions. All partitions
```

`will be rebuilt and analyzed.` In addition, the entire table is analyzed after first being rebuilt.

(Bug #11751825, Bug #42822)

- InnoDB: The server could halt with an error when two kinds of operations happened simultaneously:
- A `ROLLBACK` of an inserted row that contained off-page columns.
- An online DDL operation involving a table of `ROW_FORMAT=DYNAMIC` or `ROW_FORMAT=COMPRESSED`

(that is, using the Barracuda file format) that rebuilt the table. For example, `ADD/DROP COLUMN`, `ADD``PRIMARY KEY`, change `ROW_FORMAT`.

(Bug #14842014)

- InnoDB: If the server crashed while rows were inserted into a table with a `FULLTEXT` index but before

the transaction was committed, an error could occur during the next startup:

```
InnoDB: Assertion failure in thread thread_num in file dict0dict.cc line 1019
```

(Bug #14826779)

- InnoDB: The server could halt with an error when accessing an `InnoDB` table containing a `FULLTEXT`

index through the `HANDLER` statement. (Bug #14788710)

## MySQL 5.6 Release Notes

- InnoDB: A timeout error could occur on Windows systems when doing `ALTER TABLE` statements with

the `DISCARD TABLESPACE` or `IMPORT TABLESPACE` clauses, due to a temporary tablespace file remaining in the file system. (Bug #14776799)

- InnoDB: `InnoDB` tables with `FULLTEXT` indexes could allocate memory for thread handles that was

never released, possibly leading to resource issues on Windows systems. (Bug #14759163)

- InnoDB: The server could halt with an assertion error for an `ANALYZE TABLE` operation, depending on

the structure of the table and its indexes:

```
InnoDB: Assertion failure in thread thread_num in file dict0dict.ic line 447
InnoDB: Failing assertion: pos < table->n_def
```

(Bug #14755452)

- InnoDB: During an online DDL operation that copies the table, the secondary index of the table could

become corrupted. (Bug #14753701)

- InnoDB: An online DDL operation for an `InnoDB` table incorrectly reported an empty value (`''`) instead

of the correct key value when it reported a duplicate key error for a unique index using an index prefix.

(Bug #14729221)

- InnoDB: If the server crashed after an online DDL `CREATE INDEX` operation, an error could occur while

rolling back incomplete transactions on the next startup:

```
InnoDB: error in sec index entry del undo in
...
InnoDB: Assertion failure in thread thread_num in file row0umod.cc line 559
```

(Bug #14707452)

- InnoDB: This fix improves the error handling when an `ALTER TABLE` operation adds a column beyond

the maximum number allowed for an `InnoDB` table. It also raises the maximum number of columns for an `InnoDB` table from 1000 to 1020. (Bug #14705287)

- InnoDB: This fix makes MySQL more responsive to `KILL QUERY` statements when the query is

accessing an `InnoDB` table. (Bug #14704286)

- InnoDB: If the server crashed at a precise moment during an `ALTER TABLE` operation that rebuilt the

clustered index for an `InnoDB` table, the original table could be inaccessible afterward. An example of such an operation is `ALTER TABLE ... ADD PRIMARY KEY` The fix preserves the original table if the server halts during this operation. You might still need to rename the `.ibd` file manually to restore the original table contents: in MySQL 5.6 and higher, rename from `#sql-ib$new_table_id.ibd` to`table_name.ibd` within the database directory; prior to MySQL 5.6, the temporary file to rename is`table_name#1` or `#2`. (Bug #14669848)

- InnoDB: During an online DDL operation that rebuilt the table, a `CHECK TABLE` statement could report a

count mismatch for all secondary indexes. (Bug #14606472)

- InnoDB: After a `FULLTEXT` index was created and dropped from an `InnoDB` table, further `ALTER`

`TABLE` operations to add, drop, and rename columns could cause a serious error. Regression of bug#13972248. (Bug #14504337)

- InnoDB: If an `ALTER TABLE` statement failed while attempting to create a `FULLTEXT` index for an

`InnoDB` table, the server could halt with an assertion error while dropping the incomplete index. (Bug#14504174)

- InnoDB: During shutdown, with the `innodb_purge_threads` configuration option set greater than 1,

the server could halt prematurely with this error:

## MySQL 5.6 Release Notes

```
mysqld got signal 11
```

A workaround was to increase `innodb_log_file_size` and set `innodb_purge_threads=1`.

The fix was backported to MySQL 5.5 and 5.1, although those versions do not have the`innodb_purge_threads` configuration option so the error was unlikely to occur. (Bug #14234028)

- InnoDB: The server could halt with an error under some combinations of concurrent operations:

```
InnoDB: unknown error code 20
```

This issue originated during the 5.6 development cycle. It affected only transactions using the `READ``COMMITTED` and`READ UNCOMMITTED` isolation levels. (Bug #13641662, Bug #12424846)

- InnoDB: This fix improves the error message when a foreign key constraint cannot be created. Instead

of referring to an inability to create a table with an auto-generated name, the message clearly states the error:

```
ERROR 1215 (HY000): Cannot add foreign key constraint
```

Issuing a subsequent `SHOW WARNINGS` statement provides additional detail about any secondary indexes that are required. (Bug #11745444, Bug #15324)

- Replication: If a table to be replicated had a `FULLTEXT` index, this index was not ruled out when

selecting the type of scan to be used in finding the next row, even though it cannot be used to find the correct one. The row applier subsequently tried unsuccessfully to employ an index scan, causing replication to fail. Now in such cases, indexes which do not provide for sequential access (such as`FULLTEXT`) are not considered when determining whether to use a table, index, or hash scan for this purpose. (Bug #14843764)

- Replication: Given a stored routine R in which the `GTID_SUBTRACT()` function was invoked: Once

`GTID_SUBTRACT()` returned `NULL` when called inside R, it continued to return `NULL` every time it was called within R, for the remainder of the client session. (Bug #14838575)

- Replication: When using the GTID-aware master-slave protocol, the slave I/O thread used the wrong

position. When using GTIDs, the position is not normally used, but as a special case, the position was used in addition to the GTID when the slave reconnected to the same master (even though this was not necessary). This problem is fixed by making the GTID-aware master-slave protocol not use positions at all any longer. (Bug #14828028)

- Replication: `MySQL Enterprise Backup`, `mysqldump`, and `mysqlhotcopy` could not be used with

a GTID-enabled MySQL Server, because they were unable to restore the server's GTID state and so could not restore from any point in the binary log other than the very beginning.

As part of the fix for this problem, the `gtid_purged` system variable (formerly named `gtid_lost`) is no longer read-only; now it is possible to add GTIDs to it when `gtid_executed` (formerly `gtid_done`)is empty. (Bug #14787808)

- Replication: Restarting replication after the first binary log file was purged resulted in the error `Got`

```
fatal error 1236 from master when reading data from binary log: 'The slave
is connecting using CHANGE MASTER TO MASTER_AUTO_POSITION = 1, but the master
has purged binary logs containing GTIDs that the slave requires.' This led GTID-
```

based replication to fail. (Bug #14756691)

- Solaris: Installation using Solaris packages ran `mysql_install_db` during upgrade operations (this

should occur only for new installations). (Bug #14747671, Bug #16534721)

- `mysql_install_db` failed to honor the `--user` option. (Bug #15866735)

## MySQL 5.6 Release Notes

- The optimizer could allocate insufficient memory when determining subquery execution strategies,

causing the server to exit. (Bug #14846866)

- The optimizer could raise an assertion when evaluating a range test against an `IS NOT NULL` condition.

(Bug #14843705)

- `init_io_cache()` used `memset()` to clear a mutex but passed the wrong mutex size. (Bug

#14838882)

- Creating an `InnoDB` table with a `FULLTEXT` index could encounter a serious error if the table name

contained nonalphanumeric characters. (Bug #14835178, Bug #16036699)

- Out-of-bounds reads could occur within `filename_to_tablename()`. (Bug #14834378)
- When a backup is taken using `mysqldump` on a server with global transaction IDs (GTIDs) enabled, the

dump file did not contain any GTID information. This eventually results in replicating the transactions from the beginning of history when the backup is used to bring up a slave.

To enable control over GTID information written to the dump file, `mysqldump` now has a `--set-gtid-``purged` option that indicates whether to add a `SET` `@@GLOBAL.gtid_purged` statement to the output.

The following table shows the permitted option values. The default value is `AUTO`.

Value Meaning`OFF` Add no `SET` statement to the output.

`ON` Add a `SET` statement to the output. An error occurs if GTIDs are not enabled on the server.

`AUTO` Add a `SET` statement to the output if GTIDs are enabled on the server.

(Bug #14832472)

- With `LOCK TABLES` in effect, `CREATE TABLE IF NOT EXISTS ... LIKE` could raise an assertion.

(Bug #14788976)

- An assertion could be raised executing `INSERT`, `UPDATE`, or `DELETE` after implicitly starting a `READ`

`ONLY` transaction in `LOCK TABLES` mode. (Bug #14788540)

- A query with a union and a join could crash the parser. (Bug #14786792, Bug #16076289)
- Attempting to read a `utf16` file with `LOAD DATA` raised an assertion. (Bug #14786470)
- The automatic key generation part of derived table handling did not handle properly columns specified as

part of the `VALUES()` clause and caused an assertion to be raised. (Bug #14786324)

- Invalid memory reads could occur for queries that selected from a zero-length table name. (Bug

#14780820)

- `SHOW PROCESSLIST` output was not sorted in `Id` order. (Bug #14771006)
- For some `SELECT` statements, `EXPLAIN` could cause the server to exit. (Bug #14761894)
- Attempting to create an auto-increment column in an `InnoDB` table with a `NULL` type attribute could

cause a serious error. (Bug #14758479)

- A memory leak occurred for attempts to use `ALTER TABLE` to set a default value for a tiny, medium, or

long `BLOB` or `TEXT` column. (Bug #14756206)

## MySQL 5.6 Release Notes

- An assertion was raised if `ALTER TABLE` was used to rename a column to same name as an existing

column while also reordering the renamed column using `AFTER` or `FIRST`. (Bug #14756089)

- An assertion could be raised if semijoin materialization was used to evaluate a `NOT IN` subquery. (Bug

#14751858)

- After issuing `ALTER TABLE ... DISCARD TABLESPACE`, an online DDL operation for the same table

could fail on Windows systems with an error: `Got error 11 from storage engine`. An `ALTER``TABLE` statement with the `ALGORITHM=INPLACE` clause could also create an empty .ibd file, making the tablespace no longer “discarded”. (Bug #14735917)

- For some continuation handler nestings, continuation could occur at the wrong location. (Bug

#14724836)

- Starting the server with `bind_address` and then setting `host_cache_size` to 0 could result in the

server stopping for certain kinds of client connections. (Bug #14689561)

- For `UPDATE` statements, `EXPLAIN` showed the total key length in the `key_len` column rather than the

length of the used key parts. (Bug #14682438)

- With index condition pushdown enabled, the optimizer could produce incorrect results for derived tables.

(Bug #14640176)

- `SHOW PROFILE` could be used to cause excessive server memory consumption. (Bug #14629232)
- The optimizer could incorrectly use a nonspatial index to optimize spatial operations, causing an

assertion to be raised. (Bug #14600994)

- Several problems with `mysql_config_editor` were fixed:
- There was no error message for write errors to the configuration file.
- The `--all` option is not supported for the `remove` command, but there was no warning message for

attempts to use `remove --all`.

- The `--all` option is not supported for the `set` command, but there was no warning message for

attempts to use `set --all`.

In addition, the `--user`, `--password`, and `--host` options now are supported for the `remove`command. When present, the `remove` command removes only the requested values from the login path.

If none of them is given, `remove` removes the entire `client` login path. For example, this command removes only the `user` value from the `client` login path rather than the entire `client` login path:

```
mysql_config_editor remove --login-path=client --user
```

(Bug #14505672, Bug #14545989, Bug #14545999)

- A `LIKE` pattern with too many `'%'` wildcards could cause a segmentation fault. (Bug #14303860)
- Previously, the `events_statements_summary_by_digest` Performance Schema table was a

summary grouped by the `DIGEST` column alone. Now this table contains a `SCHEMA_NAME` column and the digest summary is grouped by the `SCHEMA_NAME` and `DIGEST` columns.

If you upgrade to this MySQL release from an earlier version, you must run `mysql_upgrade` (and restart the server) to incorporate this change into the `performance_schema` database. (Bug#14075527)

- Query rewriting to scrub passwords for logging was done even if none of the associated logs were

enabled. Also, `CREATE SERVER` and `ALTER SERVER` are now rewritten as necessary. (Bug #14073554)

## MySQL 5.6 Release Notes

- `CREATE TABLE ... SELECT` could create a table with a column of type `NULL`, which when accessed

caused a server exit. (Bug #14021323, Bug #23280699)

- `CHECK TABLE` and `REPAIR TABLE` could crash if a `MyISAM` table had a corrupt key (`.MYI`) file. Now

the server produces an error. (Bug #13556441)

- `CHECK TABLE` and `REPAIR TABLE` could crash if a `MyISAM` table had a corrupt key (`.MYI`) file. Now

the server produces an error. (Bug #13556107, Bug #13556000)

- A “buffer too small” error message from the `myisamchk` command referred to the

`myisam_sort_buffer_size` configuration option, when it should have referred to

```
sort_buffer_size.
```

`myisamchk` now has a `myisam_sort_buffer_size` variable available as an alternative name to`sort_buffer_size`. `myisam_sort_buffer_size` is preferable to `sort_buffer_size` because its name corresponds to the `myisam_sort_buffer_size` server system variable that has a similar meaning. `sort_buffer_size` should be considered deprecated. (Bug #11754894, Bug #46578)

- The `host_cache` Performance Schema table displayed some lines multiple times. This was not an

issue with the host cache itself, only with the table that provides information about the cache contents.

(Bug #67236, Bug #14764890)

- On OS X, reinitializing the query cache could cause the server to exit. Thanks to Davi Arnaut for the

patch. (Bug #67156, Bug #14741880)

- The server failed to use the query cache for queries in which a database or table name contained special

characters and the table storage engine was `InnoDB`. (Bug #64821, Bug #13919851)

- `mysqld_safe` ignored the value of the `UMASK` environment variable, leading to behavior different from

`mysqld` with respect to the access mode of created files. Now `mysqld_safe` (and `mysqld_multi`)attempt to approximate the same behavior as `mysqld`. (Bug #57406, Bug #11764559)

- For dumps of the `mysql` database, `mysqldump` skipped the `event` table unless the `--events` option

was given. This no longer occurs. To skip the `event` table if that is desired, use the `--ignore-table`option instead (Bug #55587, Bug #11762933)

- For `MEMORY` tables with `HASH` indexes, `DELETE` sometimes failed to delete all applicable rows. (Bug

#51763, Bug #11759445)

- On OS X, `KILL` could sometimes be unreliable. (Bug #37780, Bug #11748945)
