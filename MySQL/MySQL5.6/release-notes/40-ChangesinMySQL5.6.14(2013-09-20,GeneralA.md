---
title: "Changes in MySQL 5.6.14 (2013-09-20, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=105"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

A known limitation of this release:Note If you have `InnoDB` tables with full-text search indexes and you are upgrading from MySQL 5.6.10 to a MySQL version up to and including MySQL 5.6.18, the server will fail to start after the upgrade (Bug#72079). This bug is fixed in MySQL 5.6.19.

As a workaround, remove full-text search indexes prior to upgrading and rebuild full-text search indexes after the upgrade is completed.

- Audit Log Notes
- Functionality Added or Changed
- Bugs Fixed

## MySQL 5.6 Release Notes

> Audit Log Notes

- MySQL 5.7 changed audit log file output to a new format that has better compatibility with Oracle Audit

Vault. This format has been backported to MySQL 5.6 and it is possible to select either the old or new format using the new `audit_log_format` system variable, which has permitted values of `OLD` and `NEW`(default `OLD`). For details about each format, see Audit Log File Formats.

In addition, when the audit log plugin rotates the audit log file, it uses a different file name format. For a log file named `audit.log`, the plugin previously renamed the file to `audit.log.TIMESTAMP`. The plugin now renames the file to `audit.log.TIMESTAMP.xml` to indicate that it is an XML file.

If you change the value of `audit_log_format`, use this procedure to avoid writing log entries in one format to an existing log file that contains entries in a different format:

1. Stop the server.
2. Rename the current audit log file manually.
3. Restart the server with the new value of `audit_log_format`. The audit log plugin will create a new

log file, which will contain log entries in the selected format.

The API for writing audit plugins has also changed. The `mysql_event_general` structure has new members to represent client host name and IP address, command class, and external user. For more information, see Writing Audit Plugins. (WL #7076)

> Functionality Added or Changed

- Incompatible Change: In MySQL 5.6.13, the `statement/com/` abstract statement instrument in the

`setup_instruments` Performance Schema table was renamed to `statement/com/new_packet`.

That change has been reverted.

Applications that refer to the old instrument name must be updated with the new name. For more information about the use of abstract instruments in statement classification, see Performance Schema Statement Event Tables. (Bug #16750433, Bug #17271055)

- InnoDB: The `InnoDB` `memcached` plugin now supports inserts and reads on mapped `InnoDB` tables

that have an `INTEGER` defined as the primary key. (Bug #17315083, Bug #17203937)

> Bugs Fixed

- Important Change; Replication: `START SLAVE UNTIL SQL_AFTER_GTIDS` did not cause the slave

to stop until the next GTID event was received following execution of the transaction having the indicated GTID, which could cause issues in the case when the next GTID event is delayed, or does not exist.

Now the slave stops after completing the transaction with that GTID. (Bug #14767986)

- InnoDB; Partitioning: Following any query on the `INFORMATION_SCHEMA.PARTITIONS`

table, `InnoDB` index statistics as shown in the output of statements such as `SELECT` `* FROM``INFORMATION_SCHEMA.STATISTICS` were read from the last partition, instead of from the partition containing the greatest number of rows. (Bug #11766851, Bug #60071)References: See also: Bug #16882435, Bug #69179.

- InnoDB: When logging the delete-marking of a record during online `ALTER TABLE...ADD PRIMARY`

`KEY`, `InnoDB` writes the transaction ID to the log as it was before the deletion or delete-marking of the record. When doing this, `InnoDB` would overwrite the `DB_TRX_ID` field in the original table, which could result in locking issues. (Bug #17316731)

## MySQL 5.6 Release Notes

- InnoDB: The `row_sel_sec_rec_is_for_clust_rec` function would incorrectly prepare to compare

a NULL column prefix in a secondary index with a non-NULL column in a clustered index. (Bug#17312846)

- InnoDB: An assertion would be raised in `fil_node_open_file` due to a missing `.ibd` file. Instead of

asserting, `InnoDB` should return false and the caller of `fil_node_open_file` should handle the return message. (Bug #17305626, Bug #70007)

- InnoDB: An incorrect purge would occur when rolling back an update to a delete-marked record. (Bug

#17302896)

- InnoDB: The assertion `ut_ad(oldest_lsn <= cur_lsn)` in file `buf0flu.cc` failed because the

current max LSN would be retrieved from the buffer pool before the oldest LSN. (Bug #17252421)

- InnoDB: `InnoDB` `memcached` `add` and `set` operations would perform more slowly than SQL `INSERT`

operations. (Bug #17214191)

- InnoDB: As commented in `log0log.h`, `old_lsn` and `old_buf_free` should only be compiled when

`UNIV_LOG_DEBUG` is enabled. (Bug #17160270, Bug #69724)

- InnoDB: Adding a foreign key with a constraint name that included the string “_ibfk_” caused `InnoDB`

to create a duplicate constraint with a generated internal name. The generated internal name could also collide with an existing user-defined constraint of the same name, causing a duplicate key error. (Bug#17076737, Bug #69693, Bug #17076718, Bug #69707)

- InnoDB: The `ha_innobase::clone` function would incorrectly assert that a thread cannot clone a

table handler that is used by another thread, and that the original table handler and the cloned table handler must belong to the same transaction. The incorrect assertions have been removed. (Bug#17001980)

- InnoDB: A regression introduced in the fix for Bug #14606334 would cause crashes on startup during

crash recovery. (Bug #16996584)

- InnoDB: Rolling back an `INSERT` after a failed `BLOB` write would result in an assertion failure. The

assertion has been modified to allow NULL `BLOB` pointers if an error occurs during a `BLOB` write. (Bug#16971045)

- InnoDB: When dropping all indexes on a column with multiple indexes, `InnoDB` failed to block a `DROP`

`INDEX` operation when a foreign key constraint requires an index. (Bug #16896810)

- InnoDB: An assertion failure would occur in file `row0log.cc` on `ROW_FORMAT=REDUNDANT` tables that

contained an unexpected but valid data directory flag. (Bug #16863098)

- InnoDB: A regression introduced with the fix for Bug #11762038 would cause `InnoDB` to raise an

incorrect error message. The message stated that, “InnoDB cannot delete/update rows with cascading foreign key constraints that exceed max depth of 20”. The error message would occur when killing connections reading from `InnoDB` tables that did not have foreign key constraints. (Bug #16710923)References: This issue is a regression of: Bug #11762038.

- InnoDB: In debug builds, an assertion failure would occur if `innodb_log_group_home_dir`

does not exist. Instead of an assertion, `InnoDB` now aborts with an error message if`innodb_log_group_home_dir` does not exist. (Bug #16691130, Bug #69000)

- InnoDB: For the Barracuda file format and beyond, the externally stored prefix would be read even

though the prefix is already stored locally in memory. (Bug #16569640)

- InnoDB: When changing the shared tablespace file name using `innodb_data_file_path` and

leaving the current log files in place, `InnoDB` would create a new tablespace file and overwrite the

## MySQL 5.6 Release Notes

log files resulting in a mismatch between the data dictionary and tables on disk. This bug fix ensures that `InnoDB` does not create a new tablespace if there are inconsistent system tablespaces, undo tablespaces, or redo log files. (Bug #16418661)

- InnoDB: Persistent statistics would be disabled unnecessarily when running in read-only mode. When

running in read-only mode, fetching statistics from disk does not involve any modification of on-disk data except for when `ANALYZE TABLE` is run. This fix enables persistent statistics for read-only mode. (Bug#16083211)

- InnoDB: The documentation incorrectly stated that `START TRANSACTION WITH CONSISTENT`

`SNAPSHOT` provides a consistent snapshot only if the current isolation level is `REPEATABLE READ` or

```
SERIALIZABLE. START TRANSACTION WITH CONSISTENT SNAPSHOT only works with REPEATABLE
```

`READ`. All other isolation levels are ignored. The documentation has been revised and a warning is now generated whenever the `WITH CONSISTENT SNAPSHOT` clause is ignored. (Bug #14017206, Bug#65146)

- InnoDB: The `srv_master_thread` background thread, which monitors server activity and performs

activities such as page flushing when the server is inactive or in a shutdown state, runs on a one second delay loop. `srv_master_thread` failed to check if the server is in a shutdown state before sleeping.

(Bug #13417564, Bug #63276)

- InnoDB: An infinite loop could occur in `buf_page_get_gen` when handling compressed-only pages.

(Bug #12560151, Bug #61132)

- Partitioning: Creating a table `t1` using `CREATE TABLE ... PARTITION BY LIST ...`

`PARTITION ... VALUES IN (NULL)`, then attempting to execute `CREATE TABLE ... LIKE t1`caused the server to fail. (Bug #16860588)

- Replication: The server attempted to perform an internal truncatation of the `slave_worker_info`

table while resetting it, even though this is a DDL operation and should not be used conccurrently with DML operations. To prevent this from happening, the reset now performs sequential row deletion in place of the truncation operation. (Bug #17286858, Bug #69898)

- Replication: When the `--relay-log-info-file` option was used together with

`slave_parallel_workers` set to a value greater than 1, `mysqld` failed to start. (Bug #17160671)

- Replication: The commit error caused by the failure of binary log rotation failure generated an incident

event in the binary log file and interrupted the user session with error messages which did not mention that the slave server would be stopped later when the incident event was replayed.

Now, when encountering binary log rotation failure, a more helpful error message is instead written to the log, alerting the user to investigate in a timely manner. (Bug #17016017)

- Replication: It was possible in `CHANGE MASTER TO` statements to set the `MASTER_DELAY` option

greater than the supported maximum value (231 − 1). In addition, the error resulting from setting`MASTER_DELAY` to a value greater than 232 was not handled correctly. (Bug #16820156, Bug#16960315, Bug #69249, Bug #69469)

- Replication: When a master with semisynchronous replication enabled was shut down, the master

failed to wait for either a semisyncnronous `ACK` or timeout before completing the shutdown. This prevented semisynchronous replication from reverting to asynchronous replication and allowed open transactions to complete on the master, which resulted in missing events on the slave.

To fix this problem, dump threads are now stopped last during shutdown, after the client is told to stop,so that, if the dump thread has pending events from active clients, they can be sent to the slave. (Bug#16775543)

## MySQL 5.6 Release Notes

- Replication: A session attachment error during group commit causes the rollback of the transaction (as

intended), but the transaction in which this happened was still written to the binary log and replicated to the slave. Thus, such an error could lead to a mismatched master and slave.

Now when this error occurs, an incident event is written in the binary log which causes replication to stop, and notifies the user that redundant events may exist in the binary log. An additional error is also now reported to the client, indicating that the ongoing transaction has been rolled back. (Bug#16579083)

- Replication: `START SLAVE` failed when the server was started with

```
master_info_repository=TABLE and relay_log_info_repository=TABLE and with
```

`autocommit=0`, together with `--skip-slave-start`.

A workaround for previous versions of MySQL is to restart the slave `mysqld` without the `--skip-``slave-start` option. (Bug #16533802)

- Replication: A slave using row-based replication was unable to read the rows containing columns of

type `MYSQL_TYPE_DECIMAL` properly (old-style decimal, used prior to MySQL 5.0.3). Now the slave throws an error if it receives this type of data. You can convert the old-style `DECIMAL` format to the binary format used in current MySQL releases with `ALTER TABLE`; see Upgrading from MySQL 4.1 to

5.0, for more information. (Bug #16416302)

- Replication: `DROP TEMP TABLE IF EXISTS` statements could lead to failures in applying the

binary log during point-in-time recovery operations. This is due to the fact that, when using row-based replication, the server appends `IF EXISTS` to any `DROP TEMPORARY TABLE` statements written to the binary log, and that the slave SQL thread does not check * wildcard filter rules for `DROP TEMPORARY``TABLE IF EXISTS`. If `--log-slave-updates` was also enabled on the slave, such a statement was preceded by a `USE` statement. If the database referred by the `USE` statement did not exist, the statement failed, and stopped replication.

Now, when writing `DROP TEMPORARY TABLE IF EXISTS` into the binary log, no `USE` statement is written, and the table name in the `DROP TEMPORARY TABLE` statement is a fully qualified table name.

(Bug #16290902)

- Savepoints could not be used successfully following an `ER_LOCK_DEADLOCK` error (or

`ER_LOCK_WAIT_TIMEOUT` error, if `innodb_rollback_on_timeout` was enabled). (Bug #17356954)References: This issue is a regression of: Bug #14188793.

- The `mysql_real_connect()` C API function could leak memory if it failed. (Bug #17337684)
- Full-text search on `InnoDB` tables failed on searches that used the + boolean operator. (Bug

#17280122)

- For single-threaded workloads, the optimizer recognizes some special cases for which it can avoid

function calls and enhance performance. (Bug #17234723)

- `AES_ENCRYPT()` and `AES_DECRYPT()` failed to work correctly when MySQL was built with an

`AES_KEY_LENGTH` value of 192 or 256. (Bug #17170207)

- `SELECT * from performance_schema.events_statements_current` could raise an assertion

due to a race condition under load. (Bug #17164720)

- `InnoDB` full-text searches failed in databases whose names began with a digit. (Bug #17161372)
- A successful connection failed to reset the per-IP address counter used to count successive connection

failures. This could possibly cause a host to be blocked, when the `max_connect_errors` limit was reached. (Bug #17156507)

## MySQL 5.6 Release Notes

- With the thread pool plugin enabled and SSL in use, an error in one connection might affect other

connections, causing them to experience a lost connection. (Bug #17087862)

- Under load, truncating the `accounts` Performance Schema table could cause a server exit. (Bug

#17084615)

- Within a stored program, comparison of the value of a scalar subquery with an `IN` clause resulted in an

error for the first execution and raised an assertion for the second execution. (Bug #17029399)

- The `my_strtoll10()` function could incorrectly convert some long string-format numbers to numeric

values and fail to set the overflow flag. (Bug #16997513)

- A race condition in the thread pool plugin could cause status variables such as `Aborted_connects` not

to be incremented and permitting concurrent kills to happen for the same thread ID. (Bug #16959022)

- For partitioned tables, queries could return different results depending on whether Index Merge was

used. (Bug #16862316)References: See also: Bug #17648468, Bug #176588348, Bug #18167648.

- Excessive memory consumption was observed for multiple execution of a stored procedure under these

circumstances: 1) The stored procedure had an SQL statement that failed during validation. 2) The stored procedure had an SQL statement that required repreparation. (Bug #16857395)

- For some statements, memory leaks could result when the optimizer removed unneeded subquery

clauses. (Bug #16807641)References: This issue is a regression of: Bug #15875919.

- Password rewriting in the general query log now also applies to prepared statements. (Bug #16732621)
- Within a stored procedure, repeated execution of a prepared `CREATE TABLE` statement for a table with

partitions could cause a server exit. (Bug #16614004)

- For debug builds, when the optimizer removed an `Item_ref` pointing to a subquery, it caused a server

exit. (Bug #16509874)References: This issue is a regression of: Bug #16318585.

- If the primary key for the `mysql.proc` system table was removed (an unsupported and not-

recommended operation), the server exited for subsequent stored procedure invocation. Similar problems could occur for other system tables. Now an error occurs instead. (Bug #16373054)

- Deadlocks involving metadata locks and `InnoDB` deadlocks were both reported as an

`ER_LOCK_DEADLOCK` error, but only `InnoDB` deadlocks rolled back the transaction. Now both deadlocks roll back the transaction. (Bug #14188793)

- Metadata returned for a prepared `SELECT` statement that had outer joins could indicate that columns

containing `NULL` values were `NOT NULL`. (Bug #12818811)

- For queries that accessed an `INFORMATION_SCHEMA` table in a subquery, an attempt to lock a mutex

that had already been locked could cause a server crash. (Bug #11765744)

- Full-text search on `InnoDB` tables failed on searches for words containing apostrophes when using

boolean operators.

The `innodb_ft_max_token_size` maximum value was incorrectly defined as 252, which is the maximum byte length. The maximum `innodb_ft_max_token_size` value is now 84, which is the maximum character length. (Bug #69932, Bug #17276125)

## MySQL 5.6 Release Notes

- `InnoDB` deadlock caused transaction rollback but did not release metadata locks, blocking concurrent

DDL on the transaction tables until the connection that got the deadlock issued an explicit `COMMIT` or`ROLLBACK`. (Bug #69668, Bug #17054007)

- The `libmysql.dll` library was missing several symbols: `my_init`, `mysql_client_find_plugin`,

```
mysql_client_register_plugin, mysql_load_plugin, mysql_load_plugin_v,
```

`mysql_options4`, and `mysql_plugin_options`. (Bug #69204, Bug #16797982, Bug #62394)

- `mysqldump` wrote `SET` statements as `SET OPTION`, which failed when reloaded because the

deprecated `OPTION` keyword has been removed from `SET` syntax. (Bug #67507, Bug #15844882)

- For failure to create a new thread for the event scheduler, event execution, or new connection, no

message was written to the error log. This could lead to the impression that the event scheduler was running normally when it was not. (Bug #67191, Bug #14749800, Bug #16865959)

- If one connection changed its default database and simultaneously another connection executed `SHOW`

`PROCESSLIST`, the second connection could access invalid memory when attempting to display the first connection's default database. memory. (Bug #58198, Bug #11765252)

- For better robustness against stack overflow, the server now accounts for the size of the guard area

when making thread stack size requests. (Bug #35019, Bug #11748074)
