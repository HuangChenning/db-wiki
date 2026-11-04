---
title: "Changes in MySQL 5.6.27 (2015-09-30, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=46"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> Security Notes

- yaSSL was upgraded to version 2.3.8.

Upgrading from older versions fixes a connection-failure issue when used with the thread pool plugin.

(Bug #20774956, Bug #21888925)

> Functionality Added or Changed

- InnoDB: The new `innodb_numa_interleave` read-only configuration option allows you to

enable the NUMA interleave memory policy for allocation of the `InnoDB` buffer pool. When`innodb_numa_interleave` is enabled, the NUMA memory policy is set to `MPOL_INTERLEAVE` for the `mysqld` process. After the `InnoDB` buffer pool is allocated, the `NUMA` memory policy is set back to`MPOL_DEFAULT`. This option is only available on NUMA-enabled Linux systems.

Thanks to Stewart Smith for the patch. (Bug #18871046, Bug #72811)

- RPM `.spec` files were updated so that MySQL Server builds from source RPM packages will include

the proper files to take advantage of operating system NUMA capabilities. This introduces a runtime dependency on `libnuma.so.1`. RPM and `yum` detect this and refuse to install if that library is not installed. (Bug #21775221)

> Bugs Fixed

- InnoDB; Microsoft Windows: Setting `lower_case_table_names=0` on a case-insensitive file system

could result in a hang condition when running an `INSERT INTO ... SELECT ... FROM tbl_name`

## MySQL 5.6 Release Notes

operation with the wrong `tbl_name` lettercase. An error message is now printed and the server exits when attempting to start the server with `--lower_case_table_names=0` on a case-insensitive file system. (Bug #20198490, Bug #75185)

- InnoDB: Reloading a table that was evicted while empty caused an `AUTO_INCREMENT` value to be

reset. (Bug #21454472, Bug #77743)

- InnoDB: Memory allocation sanity checks were added to the `memcached` code. (Bug #21288106)
- InnoDB: A `memcached` `flush_all` command raised an assertion. A function that starts a transaction

was called from within assertion code. (Bug #21239299, Bug #75199)

- InnoDB: A data corruption occurred on ARM64. GCC builtins did not issue the correct fences when

setting or unsetting the lock word. (Bug #21102971, Bug #76135)

- InnoDB: Server shutdown was delayed waiting for the purge thread to exit. To avoid this problem, the

number of calls to `trx_purge()` was reduced, and the `trx_purge()` batch size was reduced to 20.

(Bug #21040050)

- InnoDB: In `READ COMMITTED` mode, a `REPLACE` operation on a unique secondary index resulted in a

constraint violation. Thanks to Alexey Kopytov for the patch. (Bug #21025880, Bug #76927)

- InnoDB: The `IBUF_BITMAP_FREE` bit indicated that there was more free space in the leaf page than

was actually available. (Bug #20796566)

- InnoDB: The server failed to start with an `innodb_force_recovery` setting greater than 3. `InnoDB`

was set to read-only mode before redo logs were applied.

`DROP TABLE` is now supported with an `innodb_force_recovery` setting greater than 3. (Bug#19779113)

- InnoDB: The `trx_sys_read_pertable_file_format_id()` function reported the wrong file format.

(Bug #19206671)

- Packaging; OS X: Using `user=mysql` during installation on OS X did not allow the `mysql` database

to be installed. To fix this problem, OS X packages now use the `--no-defaults` option when creating this database. This also means that having a `my.cnf` file on the system no longer affects the installation.

(Bug #21364902)

- Partitioning: `CREATE TABLE` statements that used an invalid function in a subpartitioning expression

did not always fail gracefully as expected. (Bug #20310212)

- Partitioning: Error handling for failed partitioning-related `ALTER TABLE` operations against non-

partitioned tables was not performed correctly (Bug #20284744)

- Partitioning: `ALTER TABLE` when executed from a stored procedure did not always work correctly with

tables partitioned by `RANGE`. (Bug #77333, Bug #16613004, Bug #21246891)

- Replication: Repeatedly checking for `ERR_LOCK_WAIT_TIMEOUT` (as done, for example by repeatedly

executing `SHOW SLAVE STATUS`) during a prolonged write lock on a table led to an assert. (Bug#21095969)

- Replication: If statement based logging was in use, when updating multiple tables in a single statement,

a single transaction could be logged as two different transactions. This was due to the binary logging process not properly identifying statements which were operating over transactional tables. The fix ensures that they are correctly identified, even if such statements do not change the contents of the tables. (Bug #16621582, Bug #21349028)

## MySQL 5.6 Release Notes

- Replication: When the dump thread was killed while dumping an inactive binary log, some events in this

log could be skipped and thus not replicated. (Bug #78337, Bug #21816399)References: See also: Bug #74607, Bug #19975697.

- Replication: Under certain circumstances it was possible for `Retrieved_Gtid_Set` on the slave to

contain gaps while no gaps appeared in `Executed_Gtid_Set` or the slave's binary logs. This could happen when slave rotated the relay log in such a way that the last event of this log contained the record which set `gtid_next`, and was then restarted after reading GTIDs from the following log. Following the restart, `Retrieved_Gtid_Set` contained GTIDs which were executed incorrectly as well as spurious or"phantom" gaps.

TYhe fix for this problem adds a GTID to `Retrieved_Gtid_Set` before writing the event to the relay log, rather than after. If for some reason writing to relay log fails, the GTID is removed from`Retrieved_Gtid_Set`. (Bug #76959, Bug #21046372)References: See also: Bug #17943188.

- Replication: `SAVEPOINT` and `ROLLBACK TO SAVEPOINT` within a trigger led to an assertion. (Bug

#76727, Bug #20901025)

- Replication: While a `SHOW BINLOG EVENTS` statement was executing, any parallel transaction was

blocked. The fix ensures that the `SHOW BINLOG EVENTS` process now only acquires a lock for the duration of calculating the file's end position, therefore parallel transactions are not blocked for long durations. (Bug #76618, Bug #20928790)

- Replication: If a `CREATE VIEW` statement failed, it was being incorrectly written to the binary log even

though it did not result in the creation of a partial view. The fix ensures that such statements are not recorded in the binary log. Additionally it was found that when a statement which had failed on a master was received by a slave with an expected error, if the statement was skipped on the slave, for example due to a replication filter, the expected error was being compared with the actual error that happened on the slave. The fix ensures that if a statement with an expected error is received by a slave, if the statement has not been filtered, only then is it compared with the actual error that happened on the slave. (Bug #76493, Bug #20797764)

- Replication: The action specified for `binlog_error_action` was not always honored correctly after a

hardware failure occurred during log rotation. (Bug #76379, Bug #20805298)

- Replication: Modifying the `master_info_repository` or `relay_log_info_repository` inside a

transaction and later rolling back that transaction left the repository in an unusable state. We fix this by preventing any modification of these repositories inside a transaction. (Bug #74950, Bug #20074353)

- Replication: When `relay_log_recovery` is set, the error log entry that reports the new recovery

positions has been extended to also report the old relay log positions. (Bug #74089, Bug #21305976)

- Replication: When a master with `--binlog_checksum=none` and `--gtid-mode=ON` was

replicating to a slave with `--binlog_checksum=crc32`, restarting the slave's SQL thread caused an `Event crc check` error. This was due to the `Format_description_log_event` from the master not being correctly found in existing relay logs after restarting the slave's SQL thread.

The fix ensures that the `Previous_gtids_log_event` is correctly skipped and that the correct`Format_description_log_event` is found in existing relay logs after restarting the slave's SQL thread. (Bug #73806, Bug #20644100, Bug #76746, Bug #20909880)

- Replication: When using `relay_log_info_repository=TABLE`, the

`mysql.slave_relay_log_info` table is updated when a transaction is committed or when a flush is performed explicitly, such as during relay log rotation. If a transaction that uses any nontransactional tables (for example `MyISAM` tables) is split across multiple relay logs, it is partially committed on relay

## MySQL 5.6 Release Notes

log flush. When `gtid_mode=ON`, this caused the same GTID to be used for the remaining portion of the transaction, which raised an `ER_GTID_NEXT_TYPE_UNDEFINED_GROUP` error.

We fix this issue by postponing in such cases the update of the relay log information repository that normally occurs on relay log rotation until the commit for the transaction in question has been executed.

This issue did not affect tables using transactional storage engines such as `InnoDB`. (Bug #68525, Bug#16418100)References: See also: Bug #21630907, Bug #76974.

- The `CMake` checks for NUMA availability could cause compilation problems on platforms without NUMA

support. (Bug #21774859)

- Certain subqueries as arguments to `PROCEDURE ANALYSE()` could cause a server exit. (Bug

#21350175)

- An assertion could be raised due to incorrect error handling if a `SELECT ... FOR UPDATE` subquery

resulted in deadlock and caused a rollback. (Bug #21096444)

- Selecting the result of an `INSERT()` function call to which input was passed as a hexidecimal string

could expose more information than was passed to the function. (Bug #21056907)

- The updatable property of a view is set during view creation. If the underlying table was dropped and re-

created as a nonupdatable one, the updatable property of the original view was not revised accordingly.

This could cause a server exit for attempts to insert or replace into the view is made. (This problem was specific to views with multiple tables/views and did not occur with update statements.) (Bug #21039264)

- Servers linked against yaSSL and compiled with GCC 4.8.2 could fail to respond correctly to connection

attempts until several seconds after startup. (Bug #21025377)

- For tables with subpartitions, the server could exit due to incorrect error handling during partition pruning

if the partition could be identified but not the subpartition. (Bug #20909518)

- `DELETE` could check privileges for the wrong database when table aliases were used. (Bug #20777016)
- Within a trigger, use of a cursor that accessed `OLD` or `NEW` values from a row could cause a server exit.

(Bug #20760261)

- Long path name values for some options could lead to stack overflow. (Bug #20376760)
- MySQL sometimes produced no warning when it was unable to interpret a character in a given character

set. (Bug #20238729)

- On Windows, the `validate_password` plugin could cause a server exit during the dictionary check.

(Bug #18636874)

- On Windows, setting `query_cache_min_res_unit` to too large a value could result in a value of 0

and a subsequent server exit. (Bug #18487951)

- `EXPLAIN` of statements containing `GROUP_CONCAT()` could cause a server exit. (Bug #17865675)
- On Windows, heap corruption in the audit log plugin caused server startup failure. (Bug #14700102)
- RPM installation scripts failed if configuration files contained multiple `datadir` lines. Now the last

`datadir` line is used. (Bug #77878, Bug #21527467)

- For wait events, the Performance Schema uses the `CYCLE` timer by default, but failed to fall back to a

different timer if `CYCLE` was unavailable. (Bug #77577, Bug #21374104)

## MySQL 5.6 Release Notes

- Updating `VARCHAR` and `TEXT` columns in the same `UPDATE` statement could produce incorrect results.

When a `VARCHAR` column was assigned to a `TEXT` column and the `VARCHAR` column was then set to a different value, the `TEXT` column's result contained the `VARCHAR` column's new value. (Bug #77135, Bug#21143080)

- If an `INFORMATION_SCHEMA` query that performed a table-open operation encountered a corrupt

table and attempted to repair it, a deadlock could occur, resulting in an aborted transaction without an appropriate error being reported. Such queries now do not attempt table repair. (Bug #76912, Bug#21021848)

- `mysqladmin -u root -p` could exit with a segmentation fault. (Bug #76538, Bug #20802751)
- `mysqlimport --use-threads` did not actually use multiple threads. (Bug #76480, Bug #20772273)
- The optimizer sometimes generates an index for a derived table (subquery in the `FROM` clause). If this

occurred for a statement executed within a stored program, a memory leak could occur. (Bug #76349,Bug #20728894)

- For OS X 10.9 packages, the `version_compile_os` system variable indicated 10.8. (Bug #75581, Bug

#20400501)

- The optimizer could incorrectly assume an out-of-memory condition while optimizing a range scan for the

`OR` operator, resulting in overestimation of the number of qualifying rows. (Bug #75248, Bug #20229614)

- On platforms where the `char` is unsigned, the server was unable to parse collation definitions that

included non-7-bit ASCII characters. Affected platforms include ARM and PowerPC. Thanks to Alexey Kopytov for the patch. (Bug #74891, Bug #20928289, Bug #21682439)

- The `events_statements_history` Performance Schema table could have an `ERRORS` column value

of 0 when other columns indicated there were errors. (Bug #74614, Bug #19929832)

- View creation from a `UNION` failed with a duplicate-column error if a `SELECT` statement in the `UNION`

other than the first used the same column name multiple times. (Bug #74539, Bug #19886430)

- Empty XML elements having the form `<element/>` were not handled correctly by the `LOAD XML`

statement. (Bug #67542, Bug #16171518)
