---
title: "Changes in MySQL 5.6.21 (2014-09-23, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=70"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

## MySQL 5.6 Release Notes

- Deprecation and Removal Notes
- MySQL Enterprise Notes
- Functionality Added or Changed
- Bugs Fixed

> Deprecation and Removal Notes

- The `thread_concurrency` system variable is deprecated, but no warning resulted from setting it at

server startup. (Bug #17873011)

- The `--skip-innodb` option is now deprecated and its use results in a warning. It will be removed in a

future MySQL version. This also applies to its synonyms (`--innodb=OFF`, `--disable-innodb`, and so forth). (WL #7976)

> MySQL Enterprise Notes

- MySQL Enterprise Edition now includes a set of encryption functions based on the OpenSSL library

that expose OpenSSL capabilities at the SQL level. These functions enable Enterprise applications to perform the following operations:

- Implement added data protection using public-key asymmetric cryptography
- Create public and private keys and digital signatures
- Perform asymmetric encryption and decryption
- Use cryptographic hashing for digital signing and data verification and validation

For more information, see MySQL Enterprise Encryption. (WL #7717)

> Functionality Added or Changed

- Replication: The new variable `simplified_binlog_gtid_recovery` can be used to change the

way binary log files are searched for previous GTIDs during recovery, speeding up the process when a large number of binary log files exist. (Bug #69097, Bug #16741603, Bug #74071, Bug #19686914)

- Internally, spatial data types such as `Geometry` are represented as `BLOB` values, so when invoked with

the `--hex-blob` option, `mysqldump` now displays spatial values in hex. (Bug #43544, Bug #11752369)

> Bugs Fixed

- InnoDB; Partitioning: Large numbers of partitioned `InnoDB` tables could consume much more memory

when used in MySQL 5.6 or 5.7 than the memory used by the same tables used in previous releases of the MySQL Server. (Bug #17780517, Bug #70641)References: This issue is a regression of: Bug #11764622, Bug #57480.

- InnoDB: An `ALTER TABLE ... ADD FOREIGN KEY` operation could cause a serious error. (Bug

#19471516, Bug #73650)

- InnoDB: In debug builds, an `INSERT` operation affecting compressed tables would raise a sync-related

assertion. (Bug #19295893)

## MySQL 5.6 Release Notes

- InnoDB: Retrieval of multiple values with a single `get` command would return incorrect results instead of

an error message. The `InnoDB` `memcached` plugin does not currently support retrieval of multiple values with a single `get` command. (Bug #19172212, Bug #72453)

- InnoDB: Attempting to perform operations on a timed out key would cause the `memcached` daemon to

crash and restart. (Bug #19172013, Bug #72586)

- InnoDB: With a transaction isolation level less than or equal to `READ COMMITTED`, gap locks were not

taken when scanning a unique secondary index to check for duplicates. As a result, duplicate check logic failed allowing duplicate key values in the unique secondary index. (Bug #19140907)References: This issue is a regression of: Bug #16133801.

- InnoDB: During recovery, a segmentation fault would occur when marking a table as corrupt. (Bug

#18942294)References: This issue is a regression of: Bug #11830883.

- InnoDB: A failed in-place `ALTER TABLE` operation would leave behind nonunique temporary file names

in the data dictionary preventing future `ALTER TABLE` operations on the same table due to temporary file name conflicts. To avoid this problem, temporary file names are made unique by appending a static global number that is initialized to a random distributed 32-bit number using `ut_time()` and`ut_crc32()`. The number is then incremented atomically for each assigned temporary file name.

Previously, temporary files were named using the format `#sql-ibtid`, where `tid` is the table ID.

Temporary files are now named using the format `#sql-ibtid-inc`, where `tid` is the table ID and `inc`is the incremented number. (Bug #18734396, Bug #72594)

- InnoDB: In rare cases, the purge process would attempt to delete a secondary index record that was not

marked for deletion, resulting in an inconsistent secondary index. (Bug #18631496)

- InnoDB: `srv_active_wake_master_thread()` was called directly in `innobase_commit` and

`innobase_prepare`, waking up the master thread and incrementing `srv_activity_count`.

`srv_active_wake_master_thread()` should only be called after committing write transactions, not after read-only transactions or rollbacks. This patch also replaces some calls to`srv_active_wake_master_thread()` with calls to `ib_wake_master_thread()`. (Bug #18477009,Bug #72137)

- InnoDB: An in-place `ALTER TABLE` operation on a table with a broken foreign key constraint could raise

an assertion. (Bug #16869435)

- InnoDB: Inserting a record into an `InnoDB` table with a key that falls between the maximum key of a full

page and the minimum key of the “next” page could result in unnecessary page splits and under-filled pages. If the insert point is at the end of a page, `InnoDB` now attempts to insert to the next page before splitting the page. (Bug #15923864, Bug #67718)

- Replication: After the fix for Bug #16861624, killing a multithreaded slave worker which was waiting for

a commit lock caused a debug assertion to fail. This fix ensures that such a situation can not occur. (Bug#19311260)

- Replication: When committing a transaction, a flag is now used to check whether a thread has been

created, rather than checking the thread itself, which uses more resources, particularly when running the server with `master_info_repository=TABLE`. (Bug #18684222)References: See also: Bug #17967378.

- Replication: When using GTIDs with `MASTER_AUTO_POSITION` enabled, if an I/O thread was restarted

it failed with an `ER_GTID_NEXT_TYPE_UNDEFINED_GROUP` error due to a partial transaction not being

## MySQL 5.6 Release Notes

correctly rolled back before resuming the I/O thread. This fix ensures that the partial transaction is correctly rolled back. (Bug #18472603)

- Replication: When `mysqlbinlog` processed multiple binary log files into a single output file,

this file was not in a useful state for point-in-time recovery, when it failed with the error, `When`

```
@@SESSION.GTID_NEXT is set to a GTID, you must explicitly set it to a
different value after a COMMIT or ROLLBACK. Please check GTID_NEXT variable
manual page for detailed explanation. Current @@SESSION.GTID_NEXT is 'xyz'.
```

When `mysqlbinlog` processes a binary log containing GTIDs, it outputs `SET` `gtid_next` statements,but `gtid_next` is set to undefined whenever a commit occurs; this left `gtid_next` undefined when the server had finished processing the output from `mysqlbinlog`. When the next binary log file started with one or more anonymous statements or transactions, the combination of gtid_next being left undefined at the end of the first binary log and the second binary log containing anonymous transactions to the error described previously (Error 1837, `ER_GTID_NEXT_TYPE_UNDEFINED_GROUP`).

To fix this issue, now, whenever `mysqlbinlog` encounters this situation, it inserts `SET gtid_next =``AUTOMATIC` if required to avoid leaving the previous binary log with `gtid_next` undefined.

In addition, as a result of this fix, `mysqlbinlog` no longer outputs session variable information for every binary log; now, this value is printed only once unless it changes. (Bug #18258933, Bug #71695)

- Replication: When the I/O thread reconnected to a master using GTIDs and multithreaded slaves while

in the middle of a transaction, it failed to abort the transaction, leaving a partial transaction in the relay log, and then retrieving the same transaction again. This occurred when performing a rotation of the relay log. Now when reconnecting, the server checks before rotating the log in such cases, and waits first for any ongoing transaction to complete. (Bug #17326020)

- Replication: The `CLIENT_REMEMBER_OPTIONS` flag for compressed slave connections is no longer

reset and all options are retained. This restores functionality of all options to compressed slave connections. (Bug #72901, Bug #18923691, Bug #73324, Bug #19244772)

- Replication: When using row-based replication, setting a slave's `slave_rows_search_algorithms`

variable to `HASH_SCAN` caused an `ER_KEY_NOT_FOUND` error even though that record existed in the storage layer. This fix ensures that the unique key for each record is correctly maintained and such a situation does not occur. (Bug #72788, Bug #18860225)

- Replication: When using row-based replication, running a long transaction involving a large number

of events could trigger an Out of Memory (OOM) error if the slave's table structure was not compatible with the master's table structure. Such an incompatible situation could occur if the table on the slave had been manually changed, or when replicating between different MySQL versions that have different data types. This OOM error was caused because the virtual temporary tables created for the row conversion were not being freed until the end of the transaction, which was a problem when replicating large numbers of events.

Starting with this version, such virtual tables are correctly freed during the conversion process. (Bug#72610, Bug #18770469)References: See also: Bug #19692387.

- Replication: The error messages generated when a duplicate server UUID causes issues during

replication have been improved. The slave error now identifies the duplicate server UUID and the master error identifies the zombie thread that has been killed. (Bug #72578, Bug #18731211)

- Replication: When an event group was spanned across multiple relay log files, a slave could incorrectly

identify GTID-header group boundaries. This meant that when a transaction was retried, or if the SQL thread was stopped in the middle of a transaction after some rotates, the `Gtid_log_event` was being

## MySQL 5.6 Release Notes

silently skipped on the slave, and the transaction was logged with the slave's GTID. This problem also impacted on using `START SLAVE UNTIL MASTER_LOG_POS = log_pos;` with GTIDs enabled.

If `log_pos` was in the middle of a transaction, the `Gtid_log_event` was not correctly detected as the beginning of the transaction and replication stopped before this event. With this fix, threads correctly detect that they are part of a group, and this is used to check if a `Gtid_log_event` is part of a transaction. (Bug #72313, Bug #18652178, Bug #18306199)

- Replication: On a master that is using semisynchronous replication, where

```
rpl_semi_sync_master_wait_no_slave is enabled and rpl_semi_sync_master_timeout is
```

set to long timeout, killing the I/O thread could cause the server to hang on shutdown. This fix ensures that if the dump thread finds that there no semisynchronous slaves connected to the master, the setting of `rpl_semi_sync_master_wait_no_slave` is ignored and the shutdown proceeds correctly. (Bug#71047, Bug #17879675)

- Replication: When using semisynchronous replication, if the binary log position was changed to a future

position on a slave then an assertion error was generated on the master. This fix ensures that in such a situation the future position is correctly acknowledged and an error is instead generated on the slave.

(Bug #70327, Bug #17453826)

- Replication: When an SQL thread which was waiting for a commit lock was killed and restarted

it caused a transaction to be skipped on slave. This fix ensures that thread positions are correctly persisted and transactions resume at the correct position. (Bug #69873, Bug #17450876)

- With DTrace support enabled, certain other compilation options could cause the build to fail. (Bug

#19506247)

- yaSSL client code did not validate the encryption size or session ID length, which could cause the client

to exit. (Bug #19463277, Bug #19463565)

- yaSSL could fail preauthorization if the client supplied inaccurate buffer lengths. (Bug #19370676, Bug

#19355577)

- Competition between threads could lead to timeout failure trying to rotate the audit log file. (Bug

#19184973)

- `LPAD()` and `RPAD()` could cause a server exit if the pad string argument was not well formed. (Bug

#18935421)

- The optimizer could create a zero-length column for a temporary table, causing a server exit. (Bug

#18928848)

- `MOD` for very small decimal right-hand arguments could cause a server exit. (Bug #18469276)
- The client library now includes a call to `X509_verify_cert_error_string()` in the SSL certificate

verification code, to be more robust in detecting invalid certificates. (Bug #18384260)

- If the left-hand-side of an `IN` predicate was a scalar subquery but returned no row, the server could exit.

(Bug #18223655, Bug #18447874)

- Sending a `SIGQUIT` or `SIGINT` signal to `mysql` could result in a `glibc`  double free or corruption error.

(Bug #17297324)

- RPM Bundle `tar` file distributions did not include the shared compatibility library RPM. (Bug #74611,

Bug #19909411)

- On EL7, installation of MySQL from RPM packages could fail if `postfix` had previously been installed

using `yum`. (Bug #73507, Bug #19392051, Bug #19392149)

## MySQL 5.6 Release Notes

- The query cache was not invalidated for a table when a `CASCADE DELETE` or `CASCADE UPDATE`

referential constraint was specified and the database name or table name contained special characters.

(Bug #72547, Bug #18710853)

- `mysql_upgrade` could fail if the `mysql.user` table contained multiple accounts with the same user

name and host name where the host name differed in lettercase. This is still not permitted, but now`mysql_upgrade` prints a more informative error message to indicate the nature of the problem:

```
ERROR 1644 (45000): Multiple accounts exist for user_name, host_name
that differ only in Host lettercase; remove all except one of them
```

(Bug #72066, Bug #18415196)

- A simultaneous `OPTIMIZE TABLE` and online `ALTER TABLE` on the same `InnoDB` table could result in

deadlock. (Bug #71433, Bug #18110156)

- Invalid memory access could occur when using prepared statements if a `mysql` client connection was

lost after statement preparation was complete and there was at least one statement that was in initialized state but not prepared yet. (Bug #70429, Bug #17512527)

- If the general query log or slow query log file was set to a FIFO or socket file, and the file reader

went away, the server stopped executing statements. Now the server detects such files, logs an error message, and continues with the appropriate log disabled. (Bug #67088, Bug #14757009)

- `LIKE` matches failed for code points of HALF WIDTH KATAKANA in the `sjis` and `cp932` character

sets. (Bug #47641, Bug #11755818)
