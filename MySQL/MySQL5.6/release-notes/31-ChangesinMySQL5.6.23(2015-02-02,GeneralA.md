---
title: "Changes in MySQL 5.6.23 (2015-02-02, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=63"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> Security Notes

- The linked OpenSSL library for the MySQL Commercial Server has been updated from version 1.0.1j

to version 1.0.1k. Issues fixed in the new version are described at http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #20375530)

- yaSSL was upgraded to version 2.3.7. (Bug #19695101, Bug #20201864)

> Functionality Added or Changed

- SSL 2.0 and SSL 3.0 protocols are now explicitly disabled because they provide weak encryption. (Bug

#19820550)References: See also: Bug #19921150.

- The valid date range of the SSL certificates in `mysql-test/std_data` has been extended to the year
2029. (Bug #18366947)

> Bugs Fixed

- InnoDB: A tablespace export operation set the purge state to `PURGE_STATE_STOP`, but the purge

thread did not check the purge state until the current purge operation was completed. In the case of a large history list, the tablespace export operation was delayed, waiting for the current purge operation to finish. The purge state is now checked with every purge batch. (Bug #20266847, Bug #75298)

- InnoDB: An `ALTER TABLE ... ADD INDEX` operation raised an assertion due to assertion code that

did not allow an online index status of `ONLINE_INDEX_ABORTED_DROPPED`. The assertion code was relaxed. (Bug #20198726)

- InnoDB: An error occurred when the `push_warning_printf` function was invoked during

server recovery. This function was previously used to print a warning message to the client. Also,`current_thd` was NULL when the server was restarted. (Bug #20144839)

## MySQL 5.6 Release Notes

- InnoDB: The `INNODB_METRICS` `adaptive_hash_searches_btree` counter failed to report counter

data. (Bug #20080942, Bug #74511)

- InnoDB: An `ALTER TABLE` operation that changed the name of a foreign key column resulted in a

failure when reloading the foreign key constraint. The previous column name remained in the data dictionary cache instead of being evicted. (Bug #20031243)

- InnoDB: With `foreign_key_checks` disabled, an assertion was raised when adding a foreign key

constraint on a renamed column that was part of a previous foreign key constraint. (Bug #20029625)

- InnoDB: Error messages regarding a size limitation on `BLOB` or `TEXT` data inserted in a single

transaction were revised. (Bug #19975322)

- InnoDB: DML operations on a table with full-text search indexes raised an invalid assertion. (Bug

#19905246)References: This issue is a regression of: Bug #19314480.

- InnoDB: A multiple-table delete operation caused the server to halt. (Bug #19815702)
- InnoDB: A `FLUSH TABLES` operation raised an assertion. (Bug #19803418)
- InnoDB: With change buffering enabled, a buffered sequence of operations that should not have been

buffered resulted in an `Unable to purge a record` error. (Bug #19528825, Bug #73767)

- InnoDB: On non-Windows platforms, `os-file_pread` and `os_file_pwrite` functions return -1 when

an error occurs. This value was printed in an error message as the number of bytes read or written.

Instead of printing the -1 value in the error message, a separate error message indicating a system call failure is now printed. Thanks to David Bennett for the patch. (Bug #19315210, Bug #73365)

- InnoDB: A slow shutdown (`innodb_fast_shutdown=0`) after crash recovery raised an assertion. Slow

shutdown did not wait for background rollback operations to finish before proceeding. (Bug #16862810)

- InnoDB: The integer column value was handled incorrectly for the `memcached` `incr` and `decr`

commands. (Bug #69415, Bug #20083106, Bug #74874, Bug #20044123)

- Partitioning: A failed `ALTER TABLE ... TRUNCATE PARTITION` statement or a failed `TRUNCATE`

`TABLE` statement against a partitioned table sometimes left inconsistent metadata in the table cache;

subsequent SQL statements reusing this metadata failed, and could in some cases also lead to a failure of the server. (Bug #74292, Bug #19786861)

- Replication: If a client thread on a slave executed `FLUSH TABLES WITH READ LOCK` while the

master executed a DML, executing `SHOW SLAVE STATUS` in the same client became blocked, causing a deadlock. The fix ensures that the read lock is only held during the period that the relay log is being updated and the deadlock is avoided. (Bug #19843808)

- Replication: Ignorable log events were introduced in MySQL 5.6, but were found to not be functioning

correctly. This has now been fixed. (Bug #74683, Bug #19949915)

- Replication: When an XA transaction was active, executing an internal rollback, for example using

the `BINLOG` statement, resulted in an assertion. The fix ensures that a rollback happens only for a slave when a transaction spans multiple binary log files. Rollback does not happen now if the Format_description comes from the `BINLOG` statement being executed in the MySQL client. (Bug#74597, Bug #19928622)

- Replication: In normal usage, it is not possible for a slave to have more GTIDs than the master. But in

certain situations, such as after a hardware failure or incorrectly cleared `gtid_purged`, the master's binary log could be truncated. This fix ensures that in such a situation, the master now detects that the

## MySQL 5.6 Release Notes

slave has transactions with GTIDs which are not on the master. An error is now generated on the slave and the I/O thread is stopped with an error. The master's dump thread is also stopped. This prevents data inconsistencies during replication. (Bug #72635, Bug #18789758)

- Replication: When using `SHOW SLAVE STATUS` to monitor replication performance,

`Seconds_Behind_Master` sometimes displayed unexpected lag behind the master. This was caused by `Previous_gtids` log events being written to the slave's relay log with a timestamp behind the master, and then being used to calculate the `Seconds_Behind_Master`. This fix ensures that events generated on the slave that are added to the relay log and are not used when calculating`Seconds_Behind_Master`. (Bug #72376, Bug #18622657)

- On Ubuntu 14.10, MySQL install operations could fail to reload AppArmor. (Bug #20092641)
- `EXPLAIN` within an XA transaction could raise an assertion. (Bug #19941492)
- Unlocking a temporary table after locking and truncating it could cause a server exit. (Bug #19786309)
- The Enterprise Encryption plugin could mishandle string arguments. (Bug #19688008, Bug #20730103)
- Binary log files created by streaming the binary log from a remote server with `mysqlbinlog` were given

an access mode more permissive than the original files. (Bug #19649868)

- If the `audit_log` plugin encountered a disk-full error, the server would exit.

Now, if the file system to which the audit log is being written fills up, a “disk full” error is written to the error log. Audit logging continues until the audit log buffer is full. If free disk space has not been made available by the time the buffer fills, client sessions will hang, and stopping the server at the time of client sessions hanging will result in audit log corruption. To avoid this if client sessions are hung, ensure that free space is available on the audit logging file system before stopping the server. (Bug #19411485)

- For failure to create a temporary table due to being out of file descriptors, the server exited rather than

returning an error. (Bug #18948649)

- For some queries that contained a derived table (subquery in the `FROM` clause), delay of materialization

resulted in a suboptimal execution plan due to a less accurate row-count estimate. (Bug #18607971)

- For `UPDATE` and `DELETE` statements, the server could exit after attempting to access an uninitialized

data structure. (Bug #18036143)

- Starting the server with `start service` or `mysqld_safe` could result in failure to use the correct

plugin directory. (Bug #17619241)

- `FLUSH TABLES` on a `FEDERATED` table failed if the table had been idle longer than the `wait_timeout`

time plus the TCP keepalive time. (Bug #17599258)

- Selecting all columns from `INFORMATION_SCHEMA.TABLES` did not reopen tables if they were in the

table cache, but selecting a subset of those columns under the same conditions did reopen tables. (Bug#16869534)

- If `my_write()` encountered a disk-full condition, it could return an incorrect error value. (Bug

#16078792, Bug #19984788)

- A malformed data packet could cause the server to exit. (Bug #10063897)
- `InnoDB` boolean full-text searches incorrectly handled + combined with parentheses; for example,

`+word1 +(>word2 <word3)`. (Bug #74845, Bug #20028323)

- MySQL failed to compile with GCC 4.9.1 in debug mode. (Bug #74710, Bug #19974500)

## MySQL 5.6 Release Notes

- For debug builds, the server could exit due to an optimizer failure to allocate enough memory for group

references. (Bug #74447, Bug #19855522)

- The server no longer logs the following warnings because they are uninformative: Client failed to provide

its character set. '`charset`' will be used as client character set. (Bug #72543, Bug #18708334)

- A file created for an internal temporary table could cause problems if the file was orphaned for some

reason and the file name was reused for later queries. (Bug #32917, Bug #11747548)
