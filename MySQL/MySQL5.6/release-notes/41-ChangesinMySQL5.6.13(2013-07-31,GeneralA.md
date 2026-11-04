---
title: "Changes in MySQL 5.6.13 (2013-07-31, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=111"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Known limitations of this release:Note On Microsoft Windows, MySQL Installer does not upgrade MySQL Enterprise Backup (MEB) 3.8.1 to 3.8.2 (latest version). A workaround is to uninstall MEB 3.8.1 and then install MEB 3.8.2 (latest version) with MySQL Installer.

Note If you have `InnoDB` tables with full-text search indexes and you are upgrading from MySQL 5.6.10 to a MySQL version up to and including MySQL 5.6.18, the server will fail to start after the upgrade (Bug#72079). This bug is fixed in MySQL 5.6.19.

As a workaround, remove full-text search indexes prior to upgrading and rebuild full-text search indexes after the upgrade is completed.

- Deprecation and Removal Notes
- Functionality Added or Changed
- Bugs Fixed

> Deprecation and Removal Notes

- Previously, program options could be specified in full or as any unambiguous prefix. For example, the

`--compress` option could be given to `mysqldump` as `--compr`, but not as `--comp` because the latter is ambiguous. Option prefixes now are deprecated. They can cause problems when new options are implemented for programs. A prefix that is currently unambiguous might become ambiguous in the future. If an unambiguous prefix is given, a warning now occurs to provide feedback. For example:

```
Warning: Using unique option prefix compr instead of compress is
deprecated and will be removed in a future release. Please use the
full name instead.
```

## MySQL 5.6 Release Notes

Option prefixes are no longer supported in MySQL 5.7; only full options are accepted. (Bug #16996656,WL #6978)

> Functionality Added or Changed

- Incompatible Change: Previously, the Performance Schema statement instrumentation did not

include statements executed on a slave replication server. To address this, a new abstract instrument,`statement/rpl/relay_log`, has been added to the `setup_instruments` table. This instrument is used during the early stages of replicated statement classification before the exact statement type is known.

In addition, the `statement/com/` abstract statement instrument was renamed to `statement/com/`

```
new_packet.
```

Applications that refer to the old instrument names must be updated with the new names. For more information about the use of abstract instruments in statement classification, see Performance Schema Statement Event Tables. (Bug #16750433, Bug #17271055)

- Important Change; Replication: By default, when promoting integers from a smaller type on the

master to a larger type on the slave (for example, from a `SMALLINT` column on the master to a `BIGINT`column on the slave), the promoted values are treated as though they are signed. Now in such cases it is possible to modify or override this behavior using one or both of `ALL_SIGNED`, `ALL_UNSIGNED`in the set of values specified for the `slave_type_conversions` server system variable. For more information, see Row-based replication: attribute promotion and demotion, as well as the description of the variable. (Bug #15831300)

- The C API `libmysqlclient` shared-library `.so` files now have version 18.1.0 (up from version 18.0.0

used in MySQL 5.5). 18.1.0 can be used as a replacement for 18.0.0. (Bug #16809055, Bug #59106,Bug #12407476)

- In batch mode, `mysql` formatted result status messages such as “"Query OK, 1 row affected"” but did

not print them. Now these messages are not formatted. (Bug #69486, Bug #16971432)

> Bugs Fixed

- Incompatible Change: It is possible for a column `DEFAULT` value to be valid for the `sql_mode` value at

table-creation time but invalid for the `sql_mode` value when rows are inserted or updated. Example:

```
SET sql_mode = '';
CREATE TABLE t (d DATE DEFAULT 0);
SET sql_mode = 'NO_ZERO_DATE,STRICT_ALL_TABLES';
INSERT INTO t (d) VALUES(DEFAULT);
```

In this case, 0 should be accepted for the `CREATE TABLE` but rejected for the `INSERT`. However,previously the server did not evaluate `DEFAULT` values used for inserts or updates against the current`sql_mode`. In the example, the `INSERT` succeeds and inserts `'0000-00-00'` into the `DATE` column.

The server now applies the proper `sql_mode` checks to generate a warning or error at insert or update time.

A resulting incompatibility for replication if you use statement-based logging(`binlog_format=STATEMENT`) is that if a slave is upgraded, a nonupgraded master will execute the preceding example without error, whereas the `INSERT` will fail on the slave and replication will stop.

To deal with this, stop all new statements on the master and wait until the slaves catch up. Then upgrade the slaves followed by the master. Alternatively, if you cannot stop new statements, temporarily change

## MySQL 5.6 Release Notes

to row-based logging on the master (`binlog_format=ROW`) and wait until all slaves have processed all binary logs produced up to the point of this change. Then upgrade the slaves followed by the master and change the master back to statement-based logging. (Bug #68041, Bug #16078943)

- Important Change; Performance; InnoDB: `InnoDB` failed to open a tablespace that has multiple

data files. This removes the known limitation that was in MySQL Server 5.6.12. (Bug #17033706, Bug#69623)

- Performance; InnoDB: A code regression introduced in MySQL 5.6 negatively impacted `DROP TABLE`

and `ALTER TABLE` performance. This could cause a performance drop between MySQL Server 5.5.x and 5.6.x. (Bug #16864741, Bug #69316)

- Performance; InnoDB: When `innodb_thread_concurrency` is set to a nonzero value, there was

a possibility that all `innodb_concurrency_tickets` would be released after each row was read,resulting in a concurrency check after each read. This could impact performance of all queries. One symptom could be higher system CPU usage. We strongly recommend that you upgrade to MySQL Server 5.6.13 if you use this setting. This could cause a performance drop between MySQL Server 5.5.x and 5.6.x. (Bug #68869, Bug #16622478)

- InnoDB: A full-text search using the IN BOOLEAN MODE modifier would result in an assertion failure.

(Bug #16927092)References: This issue is a regression of: Bug #16516193.

- InnoDB: When `CHECK TABLE` found a secondary index that contained the wrong number of entries, it

would report an error but not mark the index as corrupt. `CHECK TABLE` now marks the index as corrupt when this error is encountered, but only the index is marked as corrupt, not the table. As a result, only the index becomes unusable until it is dropped and rebuilt. The table is unaffected. (Bug #16914007)

- InnoDB: `InnoDB` would attempt to gather statistics on partially created indexes. (Bug #16907783)
- InnoDB: The server would crash during a `memcached` set operation. The failure was due to a padded

length value for a utf8 `CHAR` column. During a `memcached` update operation, a field from an old tuple would be copied with a data length that was less than the padded utf8 `CHAR` column value. This fix ensures that old tuples are not copied. Instead, a new tuple is created each time. (Bug #16875543)

- InnoDB: The two `INFORMATION_SCHEMA` tables for the InnoDB buffer pool could show an invalid page

type for read-fixed blocks. This fix will show the unknown page type for blocks that are I/O-fixed for reading. (Bug #16859867)

- InnoDB: Removed invalid compilation warning messages that appeared when compiling the `InnoDB`

memcached plugin. (Bug #16816824)

- InnoDB: A memory leak would occur when inserting or replacing a row in a full-text search index on a

table with more than 96 columns. (Bug #16809167)

- InnoDB: During an insert buffer merge, InnoDB would invoke

`lock_rec_restore_from_page_infimum()` on a potentially invalid record pointer. (Bug#16806366)

- InnoDB: The `innodb_rwlock_x_spin_waits` item in the

`INFORMATION_SCHEMA.INNODB_METRICS` table would show the same value as the`innodb_rwlock_x_os_waits` item. (Bug #16798175)

- InnoDB: In debug builds, an assertion could occur in `OPT_CHECK_ORDER_BY` when using binary directly

in a search string, as binary may include `NULL` bytes and other non-meaningful characters. This fix will remove non-meaningful characters before the search is run. (Bug #16766016)

## MySQL 5.6 Release Notes

- InnoDB: Valgrind testing returned memory leak errors which resulted from a regression introduced by

the fix for Bug #11753153. The `dict_create_add_foreign_to_dictionary` function would call`pars_info_create` but failed to call `pars_info_free`. (Bug #16754901)

- InnoDB: The `page_zip_validate()` consistency check failed after compressing a page, in

`page_zip_compress()`. This problem was caused by `page_zip_decompress()`, which failed to set`heap_no` correctly when a record contained no user data bytes. A record with no user data bytes occurs when, for example, a primary key is an empty string and all secondary index fields are NULL or an empty string. (Bug #16736929)

- InnoDB: Some characters in the identifier for a foreign key constraint are modified during table exports.

(Bug #16722314, Bug #69062)

- InnoDB: Stale `InnoDB` memcached connections would result in a memory leak. (Bug #16707516, Bug

#68530)

- InnoDB: A race condition would occur between `ALTER TABLE ... ADD KEY` and `INSERT` statements,

resulting in an “Unable to Purge a Record” error. (Bug #16628233)

- InnoDB: Very large `InnoDB` full-text search (FTS) results could consume an excessive amount of

memory. This bug fix reduces memory consumption for FTS results and introduces a new configuration parameter, `innodb_ft_result_cache_limit`, which places a default size limit of 2000000000 bytes on the `InnoDB` FTS query result cache. `innodb_ft_result_cache_limit` has an unlimited maximum value and can be set dynamically. (Bug #16625973)

- InnoDB: During a transaction commit, `prepare_commit_mutex` is acquired to preserve the commit

order. If the commit operation failed, the transaction would be rolled back but the mutex would not be released. Subsequent insert operations would not be able to acquire the same mutex. This fix frees`prepare_commit_mutex` during `innobase_rollback`. (Bug #16513588)

- InnoDB: When the InnoDB shutdown mode (`innodb_fast_shutdown`) is set to 2 and the master

thread enters the flush loop, the thread would not be able to exit under some circumstances. This could lead to a shutdown hang. (Bug #16411457)

- InnoDB: Restarting InnoDB in read-only mode and running a workload would occasionally return a

`global_segment < os_aio_n_segments` assertion. (Bug #16362046)

- InnoDB: While printing a UTF-8 table name, `InnoDB` would truncate the table name, resulting in an

incomplete buffer and subsequent Valgrind error. This bug fix also addresses an incorrect debugging error message. (Bug #16066351)

- InnoDB: Attempting to create a table while in `innodb_read_only` mode resulted in the following error:

```
ERROR 1015 (HY000): Can't lock file (errno: 165 - Table is read only). (Bug
```

#15963619)

- InnoDB: Creating numerous tables, each with a full-text search index, could result in excessive memory

consumption. This bug fix adds a new configuration parameter, `innodb_ft_total_cache_size`,which defines a global memory limit for full-text search indexes. If the global limit is reached by an index operation, a force sync is triggered. (Bug #14834698, Bug #16817453)

- InnoDB: In the error log, a full-text search index would be reported missing from the data dictionary

during a `TRUNCATE TABLE` operation. After restarting `mysqld`, the following `InnoDB` error would be

```
reported: “InnoDB: Error: trying to load index idx13 for table test/g1 but the
```

`index tree has been freed.`.” (Bug #12429565)References: See also: Bug #17402002.

## MySQL 5.6 Release Notes

- InnoDB: The `row_check_index_for_mysql` method, which checks for NULL fields during an index

scan or `CHECK TABLE` operation, would iterate unnecessarily. Thanks to Po-Chun Chang for the patch to correct this issue. (Bug #69377, Bug #16896647)

- InnoDB: When running an `InnoDB` full-text search in boolean mode, prefixing an asterisk (*) to a search

string (`'*string'`) would result in an error whereas for `MyISAM`, a prefixed asterisk would be ignored.

To ensure compatibility between `InnoDB` and `MyISAM`, `InnoDB` now handles a prefixed asterisk in the same way as `MyISAM`. (Bug #68948, Bug #16660607)

- InnoDB: Successive deletes in descending key order would lead to under-filled `InnoDB` index pages.

When an `InnoDB` index page is under-filled, it is merged with the left or right sibling node. The check performed to determine if a sibling node is available for merging was not functioning correctly. (Bug#68501, Bug #16417635)

- InnoDB: Setting `foreign_key_checks=0` and running `ALTER TABLE` to change the character set

of foreign key columns for a database with multiple tables with foreign key constraints would leave the database in an inconsistent state. Subsequent `ALTER TABLE` operations (using the `COPY` algorithm)with `foreign_key_checks=1` would fail due to the detected inconsistency. Reversion of the partially executed `ALTER TABLE` operation would also fail, resulting in the loss of the table being altered. When running the same `ALTER TABLE` operation with a `RENAME` clause, the inconsistency would not be detected but if the `ALTER TABLE` operation failed for some other reason, reversion of the partially executed `ALTER TABLE` failed with the same result.

The bug fix temporarily disables `foreign_key_checks` while the previous table definition is restored.

(Bug #65701, Bug #14227431)

- InnoDB: Creating a table with a comment or default textual value containing an apostrophe that is

escaped with a backslash would sometimes cause the InnoDB storage engine to omit foreign key definitions. (Bug #61656, Bug #12762377)

- InnoDB: The `pthread_mutex`, `commit_threads_m`, which was initialized but never used, has been

removed from the code base. (Bug #60225, Bug #11829813)

- Partitioning: When upgrading to MySQL 5.5.31 or higher, a message is written into the output of

`mysql_upgrade` when encountering a partitioned table for which the `ALGORITHM` option is required to maintain binary compatibility with the original; the message includes the `ALTER TABLE` statement required to make the change. For such a table having a sufficiently large number of partitions, the message was truncated with an error before the complete `ALTER TABLE` statement could be written.

(Bug #16589511)

- Partitioning: When a range was specified in the `WHERE` condition of a query against a table partitioned

by range, and the specified range was entirely within one of the partitions, the next partition was also checked for rows although it should have been pruned away.

Suppose we have a range-partitioned table t created using the following SQL statement:

```
CREATE TABLE t  (
id INT AUTO_INCREMENT,
dt DATETIME,
PRIMARY KEY (dt,id),
UNIQUE KEY (id,dt)
)
PARTITION BY RANGE  COLUMNS(dt) (
PARTITION p0 VALUES LESS THAN ('2013-01-01'),
PARTITION p1 VALUES LESS THAN ('2013-01-15'),
PARTITION p2 VALUES LESS THAN ('2013-02-01'),
PARTITION p3 VALUES LESS THAN ('2013-02-15'),
PARTITION pmax VALUES LESS THAN (MAXVALUE)
);
```

## MySQL 5.6 Release Notes

An example of a query that exhibited this issue when run against t is shown here:

```
SELECT COUNT(*) FROM t
WHERE dt >= '2013-02-01' AND dt < '2013-02-15';
```

In this case, partition `pmax` was checked, even though the range given in the `WHERE` clause lay entirely within partition `p3`. (Bug #16447483)

- Partitioning: When dropping a partitioned table, the table's `.par` file was deleted first, before the table

definition or data. This meant that, if the server failed during the drop operation, the table could be left in an inconsistent state in which it could neither be accessed nor dropped.

The fix for this problem makes the following changes:

- Now, when dropping a partitioned table, the table's `.par` file is not removed until all table data has

been deleted.

- When executing `DROP TABLE` of a partitioned table, in the event that its `.par` file is determined to be

missing, the table's `.frm` file is now immediately deleted, in effect forcing the drop to complete.

(Bug #13548704, Bug #63884)

- Replication: The condition leading to the issue fixed in Bug #16579083 continued to raise an error even

though the condition itself no longer cause the issue to occur. (Bug #16931177, Bug #69369)References: See also: Bug #16271657, Bug #16491597, Bug #68251, Bug #68569. This issue is a regression of: Bug #16579083.

- Replication: When `rpl_semi_sync_master_timeout` was set to an extremely large value,

semisynchronous replication became very slow, especially when many sessions were working in parallel. It was discovered that the code to calculate this timeout was inside the wait loop itself, with the result that an increase in the value of `rpl_semi_sync_master_timeout` caused repeated iterations.

This fix improves the method used to calculate wakeup times, and moves it outside of the wait loop, so that it is executed one time only. (Bug #16878043, Bug #69341)

- Replication: It was possible to cause a deadlock after issuing `FLUSH TABLES WITH READ LOCK` by

issuing `STOP SLAVE` in a new connection to the slave, then issuing `SHOW SLAVE STATUS` using the original connection.

The fix for this includes the addition of the `rpl_stop_slave_timeout` system variable, to control the time in seconds to wait for slave to stop after issuing `STOP SLAVE` before returning a warning. (Bug#16856735)

- Replication: Some expressions employing variables were not handled correctly by `LOAD DATA`. (Bug

#16753869)

- Replication: In some circumstances, the message in the `Last_Error` column from the output of `SHOW`

`SLAVE STATUS` referred to `GTID_NEXT_LIST` although this variable is not currently implemented (the name is reserved for possible future use). Now in such cases the error message no longer refers to this variable. (Bug #16742886, Bug #69096)References: See also: Bug #16715809, Bug #69045.

- Replication: Linker errors occurred if the header file `log_event.h` was included in an application

containing multiple source files, because the file `rpl_tblmap.cc` was included in `log_event.h`.

This fix moves the inclusion of `rpl_tblmap.cc` into the source files that use `log_event.h`. (Bug#16607258)

## MySQL 5.6 Release Notes

- Replication: The error displayed by `SHOW SLAVE STATUS` when a worker thread fails to apply an event

contained no event coordinate information. The GTID for the event's group was also not shown. Now in such cases, the text shown for `Last_SQL_Error` is prefixed with the (physical) master binary log coordinates, as well as the value of `gtid_next` when this has been set. (Bug #16594095)

- Replication: The warning issued when specifying `MASTER_USER` or `MASTER_PASSWORD` with `CHANGE`

`MASTER TO` was unclear for a number of reasons, and has been changed to read, `Storing MySQL`

```
user name or password information in the master info repository is not secure
and is therefore not recommended. Please consider using the USER and PASSWORD
connection options for START SLAVE; see 'START SLAVE Syntax' in the MySQL
```

`Manual for more information.` (Bug #16460123, Bug #16461303, Bug #68602, Bug #68599)

- Replication: After a transaction was skipped due to its GTID already having been logged, all remaining

executed transactions were incorrectly skipped until `gtid_next` was pointed to a different GTID.

To avoid this incorrect behavior, all transactions—even those that have been skipped—are marked as undefined when they are commited or rolled back, so that an error is thrown whenever a second transaction is executed following the same `SET @@SESSION.gtid_next` statement. (Bug #16223835)

- Replication: After the client thread on a slave performed a `FLUSH TABLES WITH READ LOCK` and

was followed by some updates on the master, the slave hung when executing `SHOW SLAVE STATUS`.

(Bug #68460, Bug #16387720)

- The optimizer failed to check a function return value for an area calculation, leading to a server exit. (Bug

#23280059)

- Reads from message buffers for closed connections could occur. (Bug #17003702)
- The server could exit while using a cursor to fetch rows from a `UNION` query. (Bug #16983143)
- `Sql_condition::set_subclass_origin()` could perform an out-of-bounds read. (Bug #16969091)
- The range optimizer incorrectly assumed that any geometry function on a spatial index returned rows in

ROWID order, which could result in incorrect query results. (Bug #16960800)

- Initialization of `keycache_*` variables (see Multiple Key Caches) during server startup could write to

incorrect memory. (Bug #16945503)

- For debug builds, improper use of `SAFE_MUTEX` within `dbug.c` caused different code areas to have

different ideas about size and contents of a mutex. This could result in out-of-bounds memory writes.

(Bug #16945343)

- The Performance Schema could spawn a thread using incorrect instrumentation information. (Bug

#16939689)

- The server did excessive locking on the `LOCK_active_mi` and `active_mi->rli->data_lock`

mutexes for any `SHOW STATUS LIKE 'pattern'` statement, even when the pattern did not match status variables that use those mutexes (`Slave_heartbeat_period`, `Slave_last_heartbeat`,

```
Slave_received_heartbeats, Slave_retried_transactions, Slave_running). Now
```

attempts to show those variables do not lock those mutexes. This might result is slightly stale data, but better performance. (Bug #16904035)

- Full-text phrase search in `InnoDB` tables could read incorrect memory. (Bug #16885178)
- It was not possible to keep several major versions of MySQL in the same `yum` repository. (Bug

#16878042)

- `INSERT ... ON DUPLICATE KEY UPDATE` could cause a server exit if a column with no default value

was set to `DEFAULT`. (Bug #16756402)

## MySQL 5.6 Release Notes

References: This issue is a regression of: Bug #14789787.

- In a prepared statement or stored routine, if the `HAVING` clause of a subquery referenced some column

of the GROUP BY of the parent query, the server could exit. (Bug #16739050)

- Compiling failed with `-DMY_ATOMIC_MODE_RWLOCKS=1` or on platforms on which MySQL did not

support lockless atomic operations (such as ARM). (Bug #16736461)

- The code base was modified to account for new warning checks introduced by `gcc` 4.8. (Bug

#16729109)

- The runtime `open_files_limit` system variable did not show the actual number of file descriptors

the `mysqld` process could have, but instead the number that was requested after adjusting the value specified at startup. (Bug #16657588)

- The server could make the wrong decision about whether an account password was expired. (Bug

#16604641)

- Some rows for a session could be missing sporadically from the `session_connect_attrs`

Performance Schema table while the session was executing a workload. (Bug #16576980)

- Upgrading from community SLES RPM packages to commercial packages for the same MySQL version

failed with conflict errors. (Bug #16545296)

- If the optimizer was using a Loose Index Scan, the server could exit while attempting to create a

temporary table. (Bug #16436567)

- Incorrect results or a server exit could be caused by a reference to an aggregated expression inside a

nested subquery, where the aggregated expression was evaluated in a query block more than two levels outer to the reference. (Bug #16436383)

- Unlike `MyISAM`, `InnoDB` does not support boolean full-text searches on nonindexed columns, but this

restriction was not enforced, resulting in queries that returned incorrect results. (Bug #16434374)

- A full-text search syntax error failed to print to standard output. (Bug #16429688, Bug #16765397)
- A server exit could occur for queries of the form `SELECT (SELECT 1 FROM t1) IN (SELECT a`

`FROM t1)` when attempting to evaluate the constant left-hand argument to the `IN` subquery predicate.

(Bug #16369522)

- An assertion could be raised when creating a index on a prefix of a `TINYBLOB` or `GEOMETRY` column in

an `InnoDB` column. (Bug #16368875, Bug #18776592, Bug #17665767)

- In debug builds, failure in the range optimizer for an `ER_LOCK_DEADLOCK` or `ER_LOCK_WAIT_TIMEOUT`

error could go undetected and cause an assertion to be raised when a response was sent to the client.

In release builds, this problem manifested as clients receiving an `OK` for a statement that had failed. (Bug#16366994, Bug #16247110)

- Transforming some subqueries that select temporal or `BIGINT` types or to a semijoin caused a server

exit on the second execution of prepared statements or stored programs. (Bug #16319671)

- The server could exit in `do_copy_not_null()` due to an improper `NULL`-value check. (Bug

#16316564)

- No warning was generated if a duplicate index existed after dropping a column associated with a

multiple-column index. (Bug #16315351)

- `SELECT DISTINCT` with `WITH ROLLUP` could result in a `Duplicate entry 'NULL' for key`

`'<auto_key>'` error. (Bug #16314835)

## MySQL 5.6 Release Notes

- The usual failed-login attempt accounting was not applied to failed `COM_CHANGE_USER` commands. (Bug

#16241992, Bug #17357535)

- A user variable referenced during execution of a prepared statement is set to memory that is freed at the

end of execution. A second execution of the statement could result in Valgrind warnings when accessing this memory. (Bug #16119355)

- Misoptimization of left expressions in prepared statements could cause a server exit. (Bug #16095534)
- The optimizer trace could print ranges for key parts that were not usable for range access. (Bug

#14615536)

- Passwords in statements were not obfuscated before being written to the audit log. (Bug #14536456)
- When running a query on `INFORMATION_SCHEMA.INNODB_BUFFER_PAGE` that requested

`table_name` and `index_name` values, query results would include index pages without `table_name`or `index_name` values. (Bug #14529666)

- Several `COM_xxx` commands in the client-server protocol did not have length checks for incoming

network packets, which could result in various problems for malformed input. (Bug #14525642)

- With the thread pool plugin in use, normal connection termination caused the `Aborted_clients` status

variable to be incremented. (Bug #14081240)

- On Windows, command-line options of the form `--opt_name="opt_value"` worked but

`--opt_name='opt_value'` did not.

On all platforms, for Performance Schema options of the form `--``performance_schema_instrument="instrument=value"`, invalid instrument names now are rejected. (Bug #13955232)

- MySQL Installer, if run in custom install or change mode, offered installation options that had no effect.

(Bug #12928601)

- Incorrect results could be returned from queries that used several `aggr_func(DISTINCT)` functions

(where `aggr_func()` is an aggregate function such as `COUNT()`) when these referred to different columns of the same composite key. (Bug #12328597)

- RPM packages did not provide lowercase tags for their contents. For example, a server RPM indicated

that it provided `MySQL-server`, but not `mysql-server`. (Bug #69830, Bug #17211588)

- When selecting a union of an empty result set (created with `WHERE 1=0` or `WHERE FALSE`) with a

derived table, incorrect filtering was applied to the derived table. (Bug #69471, Bug #16961803)References: This issue is a regression of: Bug #15848521.

- For queries with `ORDER BY ... LIMIT`, the optimizer could choose a nonordering index for table

access. (Bug #69410, Bug #16916596)

- When an internal buffer was too small for the workload, the Performance Schema could spend a lot

of time in an internal spin loop attempting to allocate a memory buffer, and fail. (Bug #69382, Bug#16945618)

- In the absence of `SQL_CALC_FOUND_ROWS` in the preceding query, `FOUND_ROWS()` should return the

number of rows in the result set, but this did not always happen if the query contained `ORDER BY`. (Bug#69271, Bug #16827872)

- Full-text search on `InnoDB` tables failed on searches for words containing apostrophes. (Bug #69216,

Bug #16801781)

## MySQL 5.6 Release Notes

- If an `UPDATE` containing a subquery caused a deadlock inside `InnoDB`, the deadlock was not properly

handled by the SQL layer. The SQL layer then tried to unlock the row after `InnoDB` rolled back the transaction, raising an assertion inside `InnoDB`. (Bug #69127, Bug #16757869)

- Some `LEFT JOIN` queries with `GROUP BY` could return incorrect results. (Bug #68897, Bug #16620047)

References: This issue is a regression of: Bug #11760517.

- Comparison of a `DATETIME` value and a string did not work correctly for the `utf8_unicode_ci`

collation. (Bug #68795, Bug #16567381)

- Full-text search on `InnoDB` tables failed on searches for literal phrases combined with + or - operators.

(Bug #68720, Bug #16516193)

- Optimizations that used extended secondary keys (see Use of Index Extensions) worked only for

`InnoDB`, even for storage engines with the requisite underlying capabilities. (Bug #68469, Bug#16391678)

- `mysql_install_db` incorrectly tried to create the `mysql.innodb_table_stats` and

`mysql.innodb_index_stats` tables if `InnoDB` was not available. (Bug #68438, Bug #16369955)

- `mysqldump` assumed the existence of the `general_log` and `slow_log` tables in the `mysql` database.

It failed if invoked to dump tables from an older server where these tables do not exist. (Bug #65670,Bug #14236170)

- Attempts to build from a source RPM package could fail because the build process attempted to refer to

a `pb2user` that might not exist. (Bug #64641, Bug #13865797, Bug #69339, Bug #16874980)

- If one session had any metadata lock on a table, another session attempting `CREATE TABLE [IF`

`NOT EXISTS]` for the same table would hang. This occurred due to an attempt in the second session to acquire an exclusive metadata lock on the table before checking whether the table already existed.

An exclusive metadata lock is not compatible with any other metadata locks, so the session hung for the lock timeout period if another session had the table locked.

Now the server attempts to acquire a shared metadata lock on the table first to check whether it exists,then upgrade to an exclusive lock if it does not. If the table does exist, an error occurs for `CREATE``TABLE` and a warning for `CREATE TABLE IF NOT EXISTS`. (Bug #63144, Bug #13418638)

- `sql-common/client_plugin.c` contained a nonportable use of a `va_list` parameter. (Bug #62769,

Bug #13252623)

- Unoptimized versions of the `xxxkorr()` macros in `my_global.h` were used on 64-bit x86 processors.

(Bug #61179, Bug #12565703)

- A typo in `cmake/dtrace.cmake` prevented DTrace support from being enabled by -

`DENABLE_DTRACE-on`. (Bug #60743, Bug #12325449)

- Boolean plugin system variables did not behave well on machines where `char` is unsigned; some code

attempted to assign a negative value to these. (Bug #59905, Bug #11864205)

- With `big_tables` enabled, queries that used `COUNT(DISTINCT)` on a simple join with a constant

equality condition on a non-duplicate key returned incorrect results. (Bug #52582, Bug #11760197)References: See also: Bug #18853696.
