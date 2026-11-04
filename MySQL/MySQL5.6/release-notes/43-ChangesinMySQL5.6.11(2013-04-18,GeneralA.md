---
title: "Changes in MySQL 5.6.11 (2013-04-18, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=131"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

A known limitation of this release:Note If you have `InnoDB` tables with full-text search indexes and you are upgrading from MySQL 5.6.10 to a MySQL version up to and including MySQL 5.6.18, the server will fail to start after the upgrade (Bug#72079). This bug is fixed in MySQL 5.6.19.

As a workaround, remove full-text search indexes prior to upgrading and rebuild full-text search indexes after the upgrade is completed.

- Deprecation and Removal Notes
- RPM Notes
- Functionality Added or Changed
- Bugs Fixed

> Deprecation and Removal Notes

- The only supported value for the `innodb_mirrored_log_groups` system variable is 1, so this

variable is now deprecated. Setting it to 1 at startup results in a warning. Setting it to a value other than 1 at startup results in an error and the server exits. This variable will be removed in a future release. (WL#6808)

> RPM Notes

- It was not possible to upgrade a community RPM to a commercial RPM using `rpm -uvh` or `yum`

`localupdate`. To deal with this, the RPM spec file has been updated in MySQL 5.6.11, which has the following consequences:

## MySQL 5.6 Release Notes

- For a non-upgrade installation (no existing MySQL version installed), it possible to install MySQL using

```
yum.
```

- For upgrades, it is necessary to clean up any earlier MySQL installations. In effect, the update is

performed by removing the old installations and installing the new one.

Additional details follow.

For a non-upgrade installation of MySQL 5.6.11, it is possible to install using `yum`:

```
shell> yum install MySQL-server-NEWVERSION.glibc23.i386.rpm
```

For upgrades to MySQL 5.6.11, the upgrade is performed by removing the old installation and installing the new one. To do this, use the following procedure:

1. Remove the existing 5.6.X installation. `OLDVERSION` is the version to remove.

```
shell> rpm -e MySQL-server-OLDVERSION.glibc23.i386.rpm
```

Repeat this step for all installed MySQL RPMs.

2. Install the new version. `NEWVERSION` is the version to install.

```
shell> rpm -ivh MySQL-server-NEWVERSION.glibc23.i386.rpm
```

Alternatively, the removal and installation can be done using `yum`:

```
shell> yum remove MySQL-server-OLDVERSION.glibc23.i386.rpm
shell> yum install MySQL-server-NEWVERSION.glibc23.i386.rpm
```

(Bug #16445097, Bug #16445125, Bug #16587285)

> Functionality Added or Changed

- Replication: The functions `GTID_SUBTRACT()` and `GTID_SUBSET()` were formerly available in

`libmysqld` only when it was built with replication support. Now these functions are always available when using this library, regardless of how it was built.

- MySQL no longer uses the default OpenSSL compression. (Bug #16235681)
- There is now a distinct error code (`ER_MUST_CHANGE_PASSWORD_LOGIN`) for the error sent by the

server to a client authenticating with an expired password. (Bug #16102943)

- `mysql_config_editor` now supports `--port` and `--socket` options for specifying TCP/IP port

number and Unix socket file name. (Bug #15851247)

- `mysqlcheck` has a new `--skip-database` option. The option value is the name of a database (case

sensitive) for which checks should be skipped.

`mysql_upgrade` adds this option to `mysqlcheck` commands that it generates to upgrade the system tables in the `mysql` database before tables in other databases: It upgrades the `mysql` database, then all databases except the `mysql` database. This avoids problems that can occur if user tables are upgraded before the system tables. (Bug #14697538, Bug #68163, Bug #16216384)

> Bugs Fixed

- Incompatible Change; Partitioning: Changes in the `KEY` partitioning hashing functions used with

numeric, date and time, `ENUM`, and `SET` columns in MySQL 5.5 makes tables using partitioning or

## MySQL 5.6 Release Notes

subpartitioning by `KEY` on any of the affected column types and created on a MySQL 5.5 or later server incompatible with a MySQL 5.1 server. This is because the partition IDs as calculated by a MySQL 5.5 or later server almost certainly differ from those calculated by a MySQL 5.1 server for the same table definition and data as a result of the changes in these functions.

The principal changes in the `KEY` partitioning implementation in MySQL 5.5 resulting in this issue were as follows: 1. The hash function used for numeric and date and time columns changed from binary to character-based. 2. The base used for hashing of `ENUM` and `SET` columns changed from `latin1 ci`characters to binary.

The fix involves adding the capability in MySQL 5.5 and later to choose which type of hashing to use for `KEY` partitioning, which is implemented with a new `ALGORITHM` extension to the `PARTITION BY``KEY` option for `CREATE TABLE` and `ALTER TABLE`. Specifying `PARTITION BY KEY ALGORITHM=1``([columns])` causes the server to use the hashing functions as implemented in MySQL 5.1; using`ALGORITHM=2` causes the server to use the hashing functions from MySQL 5.5 and later. `ALGORITHM=2`is the default. Using the appropriate value for `ALGORITHM`, you can perform any of the following tasks:

- Create `KEY` partitioned tables in MySQL 5.5 and later that are compatible with MySQL 5.1, using

```
CREATE TABLE ... PARTITION BY KEY ALGORITHM=1 (...).
```

- Downgrade `KEY` partitioned tables that were created in MySQL 5.5 or later to become compatible with

MySQL 5.1, using `ALTER TABLE ... PARTITION BY KEY ALGORITHM=1 (...)`.

- Upgrade `KEY` partitioned tables originally created in MySQL 5.1 to use hashing as in MySQL 5.5 and

```
later, using ALTER TABLE ... PARTITION BY KEY ALGORITHM=2 (...).
```

Important: After such tables are upgraded, they cannot be used any longer with MySQL 5.1 unless they are first downgraded again using `ALTER TABLE ... PARTITION BY KEY ALGORITHM=1``(...)` on a MySQL server supporting this option.

This syntax is not backward compatible, and causes errors in older versions of the MySQL server.

When generating `CREATE TABLE ... PARTITION BY KEY` statements, `mysqldump` brackets any occurrence of `ALGORITHM=1` or `ALGORITHM=2` in conditional comments such that it is ignored by a MySQL server whose version is not at least 5.5.31. An additional consideration for upgrades is that MySQL 5.6 servers prior to MySQL 5.6.11 do not ignore the `ALGORITHM` option in such statements when generated by a MySQL 5.5 server, due to the that the conditional comments refer to version 5.5.31; in this case, you must edit the dump manually and remove or comment out the option wherever it occurs before attempting to load it into a MySQL 5.6.10 or earlier MySQL 5.6 server. This is not an issue for dumps generated by MySQL 5.6.11 or later version of `mysqldump`, where the version used in such comments is 5.6.11. For more information, see ALTER TABLE Partition Operations.

As part of this fix, a spurious assertion by `InnoDB` that a deleted row had previously been read, causing the server to assert on delete of a row that the row was in the wrong partition, was also removed. (Bug#14521864, Bug #66462, Bug #16093958, Bug #16274455)References: See also: Bug #11759782.

- Incompatible Change: For debug builds, creating an InnoDB table in strict SQL mode that violated the

maximum key length limit caused the server to exit.

A behavior change in consequence of this bug fix: In strict SQL mode, a key length limit violation now results in a error (and the table is not created), rather than a warning and truncation of the key to the maximum key length. This applies to all storage engines. (Bug #16035659)

## MySQL 5.6 Release Notes

- Important Change; Replication

Important This fix was reverted in MySQL 5.6.12. See Changes in MySQL 5.6.12(2013-06-03, General Availability).

Executing a statement that performs an implicit commit but whose changes are not logged when`gtid_next` is set to any value other than `AUTOMATIC` is not permitted. Now in such cases, the statement fails with an error. This includes the statements in the following list:

```
- CHANGE MASTER TO
- START SLAVE
- STOP SLAVE
- REPAIR TABLE
- OPTIMIZE TABLE
- ANALYZE TABLE
- CHECK TABLE
- CREATE SERVER
- ALTER SERVER
- DROP SERVER
- CACHE INDEX
- LOAD INDEX INTO CACHE
- FLUSH
- RESET
```

(Bug #16062608)References: See also: Bug #16484323.

- Important Change; Replication: The version number reported by `mysqlbinlog` `--version` has been

increased to 3.4. (Bug #15894381, Bug #67643)

- Important Note; Replication: Using row-based logging to replicate from a table to a same-named view

led to a failure on the slave. Now, when using row-based logging, the target object type is checked prior to performing any DML, and an error is given if the target on the slave is not actually a table.

Note It remains possible to replicate from a table to a same-named view using statement-based logging.

(Bug #11752707, Bug #43975)

## MySQL 5.6 Release Notes

- Performance; InnoDB: Switching the MySQL table used by the InnoDB memcached interface (using

the `@@` notation), was made more efficient, by reading cached information about the cache policy to use for each table. This optimization lets you frequently switch between tables during a session that uses the memcached interface, without incurring I/O overhead from examining table metadata each time. (Bug#16206654)

- Performance; InnoDB: Performance was improved for operations on tables with many rows that were

deleted but not yet purged. The speedup applies mainly to workloads that perform bulk deletes, or updates to the primary key columns, and where the system is busy enough to experience purge lag.

(Bug #16138582, Bug #68069)

- Performance; InnoDB: The `DROP TABLE` statement for a table using compression could be slower than

necessary, causing a stall for several seconds. MySQL was unnecessarily decompressing pages in the buffer pool related to the table as part of the `DROP` operation. (Bug #16067973)

- Performance; InnoDB: The I/O routines used when the AIO subsystem were made more efficient, to

merge consecutive I/O requests into a single operation. This fix solves a performance issue introduced during the 5.6 development cycle. (Bug #16043841, Bug #67973)

- InnoDB: When `ADD PRIMARY KEY` columns are reordered in an `ALTER TABLE` statement (for

example: `ALTER TABLE t1 ADD PRIMARY KEY(a,b), CHANGE a a INT AFTER b`), the log apply for `UPDATE` operations failed to find rows. (Bug #16586355)

- InnoDB: `ALTER TABLE` operations on `InnoDB` tables that added a `PRIMARY KEY` using a column prefix

could produce an incorrect result. (Bug #16544336)

- InnoDB: For `ALTER TABLE` operations on `InnoDB` tables that required a table-copying operation,

other transactions on the table might fail during the copy. However, if such a transaction issued a partial rollback, the rollback was treated as a full rollback. (Bug #16544143)

- InnoDB: When parsing a delimited search string such as “abc-def” in a full-text search, `InnoDB` now

uses the same word delimiters as `MyISAM`. (Bug #16419661)

- InnoDB: Naming inconsistencies were addressed for InnoDB `PERFORMANCE_SCHEMA` key declarations.

(Bug #16414044)

- InnoDB: Status values in the `innodb_ft_config` table would not update. The `innodb_ft_config`

is intended for internal configuration and should not be used for statistical information purposes.

To avoid confusion, column values that are intended for internal use have been removed from the`innodb_ft_config` table. This fix also removes the `innodb_ft_config` table and other internal full text search-related tables that were unintentionally exposed. (Bug #16409494, Bug #68502)

- InnoDB: Crash recovery failed with a `!recv_no_log_write` assertion when reading a page. (Bug

#16405422)

- InnoDB: This fix disables a condition for extra splitting of clustered index leaf pages, on compressed

tables. Extra page splitting was only done to reserve space for future updates, so that future page splits could be avoided. (Bug #16401801)

- InnoDB: For `InnoDB` tables, if a `PRIMARY KEY` on a `VARCHAR` column (or prefix) was empty, index

page compression could fail. (Bug #16400920)

- InnoDB: The `InnoDB` page-splitting algorithm could recurse excessively. (Bug #16345265)
- InnoDB: Improper testing of compatibility between the referencing and referenced during `ALTER`

`TABLE ... ADD FOREIGN` key could cause a server exit. (Bug #16330036)

- InnoDB: Importing a tablespace with the configuration file present would not import the data file. This

problem would occur when all pages are not flushed from the buffer pool after a table is altered using the

## MySQL 5.6 Release Notes

copy and rename approach. This fix ensures that all pages are flushed from the buffer pool when a table is altered using the copy and rename approach. (Bug #16318052)

- InnoDB: Rollback did not include changes made to temporary tables by read-only transactions. (Bug

#16310467)

- InnoDB: When using `ALTER TABLE` to set an `AUTO_INCREMENT` column value to a user-

specified value, InnoDB would set the `AUTO_INCREMENT` value to the user-specified value even when the `AUTO_INCREMENT` value is greater than the user-specified value. This fix ensures that the `AUTO_INCREMENT` value is set to the maximum of the user-specified value and MAX(auto_increment_column)+1, which is the expected behaviour. (Bug #16310273)

- InnoDB: `RENAME TABLE` would result in a hang due to a MySQL mutex acquisition deadlock. (Bug

#16305265)

- InnoDB: For debug builds, `InnoDB` status exporting was subject to a race condition that could cause a

server exit. (Bug #16292043)

- InnoDB: With `innodb_api_enable_mdl=OFF`, an `ALTER TABLE` operation on an `InnoDB` table that

required a table copy could cause a server exit. (Bug #16287411)

- InnoDB: An assertion failure would occur in `heap->magic_n == MEM_BLOCK_MAGIC_N` due to a

race condition that appeared when `row_merge_read_clustered_index()` returned an error. (Bug#16275237)

- InnoDB: InnoDB now aborts execution on Windows by calling the `abort()` function directly, as it does

on other platforms. (Bug #16263506)

- InnoDB: This fix removes an unnecessary debug assertion related to page_hash locks which only

affects debug builds. The debug assertion is no longer valid and should have been removed when hash_lock array was introduced in MySQL 5.6. (Bug #16263167)

- InnoDB: Internal read operations could be misclassified as synchronous when they were actually

asynchronous. When the I/O requests returned sooner than expected, threads could be scheduled inefficiently. This issue mainly affected read-ahead requests, and thus had relatively little impact on I/O performed by user queries. (Bug #16249505, Bug #68197)

- InnoDB: The `lock_validate` function, which is only present in debug builds, acquired and released

mutexes to avoid hogging them. This behavior introduced a window wherein changes to the hash table could occur while code traversed the same set of data. This fix updates `lock_validate` logic to collect all records for which locks must be validated, releases mutexes, and runs a loop to validate record locks.

(Bug #16235056)

- InnoDB: `ALTER TABLE` functions would perform a check to see if InnoDB is in read-only mode

(`srv_read_only_mode=true`). If InnoDB was in read-only mode, the check would return a successful status and do nothing else. This fix replaces `srv_read_only_mode` check conditions with debug assertions. (Bug #16227539)

- InnoDB: When the InnoDB buffer pool is almost filled with 4KB compressed pages, inserting into 16KB

compact tables would cause 8KB `pages_free` to increase, which could potentially slow or stall inserts.

(Bug #16223169)

- InnoDB: This fix updates InnoDB code in `ha_innodb.cc` and `handler0alter.cc` to use

`TABLE::key_info` instead of both `TABLE::key_info` and `TABLE_SHARE::key_info`. (Bug#16215361)

- InnoDB: When InnoDB locking code was revised, a call to register lock waits was inadvertently

removed. This fix adds the call back to the InnoDB locking code. (Bug #16208201)

## MySQL 5.6 Release Notes

- InnoDB: If the MySQL server halted at a precise moment when a purge operation was being applied

from the change buffer, the operation could be incorrectly performed again during the next restart. A workaround was to set the configuration option `innodb_change_buffering=changes`, to turn off change buffering for purge operations. (Bug #16183892, Bug #14636528)

- InnoDB: The InnoDB `memcached` plugin could encounter a serious error under a heavy load, such as

produced by benchmark runs. (Bug #16182660, Bug #68096)

- InnoDB: A direct call to the `trx_start_if_not_started_xa_low()` function would cause a debug

assertion. (Bug #16178995)

- InnoDB: In the case of LOCK WAIT for an insert in a foreign key table, `InnoDB` could report a false

dictionary-changed error and cause the insert to fail rather than being retried. (Bug #16174255)

- InnoDB: An in-place `ALTER TABLE` on an `InnoDB` table could fail to delete the statistics for the old

primary key from the `mysql.innodb_index_stats` table. (Bug #16170451)

- InnoDB: In some cases, deadlock detection did not work, resulting in sessions hanging waiting for a

lock-wait timeout. (Bug #16169638)

- InnoDB: Arithmetic underflow during page compression for `CREATE TABLE` on an `InnoDB` table could

cause a server exit. (Bug #16089381)

- InnoDB: For debug builds, online `ALTER TABLE` operations for `InnoDB` tables could cause a server exit

during table rebuilding. (Bug #16063835)

- InnoDB: In some cases, the `InnoDB` purge coordinator did not use all available purge threads, resulting

in suboptimal purge activity. (Bug #16037372)

- InnoDB: On systems that cannot handle unaligned memory access, depending on the stack frame

alignment, a `SIGBUS` error could occur during startup. This issue was observed on Solaris 64-bit systems. (Bug #16021177)

- InnoDB: `ALTER TABLE` for `InnoDB` tables was not fully atomic. (Bug #15989081)
- InnoDB: When `innodb_mirrored_log_groups` was set to a value other than the default 1, the

MySQL server encountered a serious error during startup while loading the InnoDB memcached plugin.

In earlier releases, the server would refuse to start (but not display an error) when this setting was changed. This fix cleans up the error handling for unsupported values of this configuration option. (Bug#15907954, Bug #67670)

- InnoDB: The `innodb_sync_array_size` variable was incorrectly allowed to be configured at runtime.

As documented, `innodb_sync_array_size` must be configured when the MySQL instance is starting up, and cannot be changed afterward. This fix changes `innodb_sync_array_size` to a non-dynamic variable, as intended. (Bug #14629979)

- InnoDB: An error at the filesystem level, such as too many open files, could cause an unhandled error

during an `ALTER TABLE` operation. The error could be accompanied by Valgrind warnings, and by this assertion message:

```
Assertion `! is_set()' failed.
mysqld got signal 6 ;
```

(Bug #14628410, Bug #16000909)

- InnoDB: The server could exit during an attempt by `InnoDB` to reorganize or compress a compressed

secondary index page. (Bug #14606334)

## MySQL 5.6 Release Notes

- InnoDB: A DML operation performed while a `RENAME TABLE` operation waits for pending I/O operations

on the tablespace to complete would result in a deadlock. (Bug #14556349)

- InnoDB: A `RENAME TABLE` statement could stall for several minutes before timing out. This issue could

occurred for a table using compression, with change buffering enabled. (Bug #14556349)

- InnoDB: If the server was started with the `skip-innodb` option, or `InnoDB` otherwise failed to start,

query any of these Information Schema tables would cause a severe error:

```
- INNODB_BUFFER_PAGE
- INNODB_BUFFER_PAGE_LRU
- INNODB_BUFFER_POOL_STATS
```

(Bug #14144290)

- InnoDB: Online DDL had a restriction that prevented renaming a column and adding a foreign key

involving that column in a single `ALTER TABLE` statement. Now, this combination of operations is allowed in a single statement. (Bug #14105491)

- InnoDB: When printing out long semaphore wait diagnostics, `sync_array_cell_print()` ran into

a segmentation violation (SEGV) caused by a race condition. This fix addresses the race condition by allowing the cell to be freed while it is being printed. (Bug #13997024)

- InnoDB: The value of the `innodb_version` variable was not updated consistently for all server

releases for the InnoDB Plugin in MySQL 5.1, and the integrated `InnoDB` component in MySQL 5.5, 5.6,and higher. Since `InnoDB` and MySQL Server development cycles are fully integrated and synchronized,now the value returned by the `innodb_version` variable is the same as for the `version` variable. (Bug#13463493, Bug #63435)

- InnoDB: Attempting to replace the default `InnoDB` full-text search (FTS) stopword list by creating an

`InnoDB` table with the same structure as `INFORMATION_SCHEMA.INNODB_FT_DEFAULT_STOPWORD`would result in an error. `SHOW CREATE TABLE` revealed that the new `InnoDB` table was created with`CHARSET=utf8`. The `InnoDB` FTS stopword table validity check only supported latin1. This fix extends the validity check for all supported character sets. (Bug #68450, Bug #16373868)

- InnoDB: This fix removes left-over prototype code for `srv_parse_log_group_home_dirs`, and

related header comments. (Bug #68133, Bug #16198764)

- InnoDB: Killing a query caused an InnoDB assertion failure when the same table (cursor) instance

was used again. This is the result of a regression error introduced by the fix for Bug#14704286. The fix introduced a check to handle kill signals for long running queries but the cursor was not restored to the proper state. (Bug #68051, Bug #16088883)

- InnoDB: On startup, InnoDB reported a message on 64-bit Linux and 64-bit Windows systems stating

that the CPU does not support crc32 instructions. On Windows, InnoDB does not use crc32 instructions even if supported by the CPU. This fix revises the wording of the message and implements a check for availability of crc32 instructions. (Bug #68035, Bug #16075806)

- InnoDB: The length of internally generated foreign key names was not checked. If internally generated

foreign key names were over the 64 character limit, this resulted in invalid DDL from `SHOW CREATE``TABLE`. This fix checks the length of internally generated foreign key names and reports an error message if the limit is exceeded. (Bug #44541, Bug #11753153)

- Partitioning: `ALGORITHM = INPLACE`, which was disallowed in MySQL 5.6.10 for DDL statements

operating on partitioned tables, can once again be used with such statements. (Bug #16216513)

## MySQL 5.6 Release Notes

References: See also: Bug #14760210.

- Partitioning: A query on a table partitioned by range and using `TO_DAYS()` as a partitioing function

always included the first partition of the table when pruning. This happened regardless of the range employed in the `BETWEEN` clause of such a query. (Bug #15843818, Bug #49754)

- Partitioning: Execution of `ALTER TABLE ... DROP PARTITION` against a view caused the server to

crash, rather than fail with an error as expected. (Bug #14653504)

- Partitioning: A query result was not sorted if both `DISTINCT` and `ORDER BY` were used and the

underlying table was partitioned. (Bug #14058167)

- Partitioning: Inserting any number of rows into an `ARCHIVE` table that used more than 1000 partitions

and then attempting to drop the table caused the MySQL Server to fail. (Bug #13819630, Bug #64580)

- Replication: When using GTIDs and binary log auto-positioning, the master had to scan all binary logs

whenever the slave reconnected (due to reasons such as I/O thread failure or a change of master)before it could send any events to slave. Now, the master starts from the oldest binary log that contains any GTID not found on the slave. (Bug #16340322, Bug #68386)

- Replication: When the server version of the master was greater than or equal to 10, replication to a

slave having a lower server version failed. (Bug #16237051, Bug #68187)

- Replication: When replicating to a MySQL 5.6 master to an older slave, Error 1193

(`ER_UNKNOWN_SYSTEM_VARIABLE`) was logged with a message such as `Unknown system`

```
variable 'SERVER_UUID' on master, maybe it is a *VERY OLD MASTER*. This message
```

has been improved to include more information, similar to this one: `Unknown system variable`

```
'SERVER_UUID' on master. A probable cause is that the variable is not
supported on the master (version: 5.5.31), even though it is on the slave
```

`(version: 5.6.11)`. (Bug #16216404, Bug #68164)

- Replication: When MTS is on and transactions are being applied, the slave coordinator would hang

when encountering a checksum error on a transaction event. This was due to a deadlock situation in which the coordinator assumed a normal stop while a worker waited for the coordinator to dispatch more events. For debug builds, the problem appeared as an assertion failure, which was due to the coordinator not setting `thd->is_error()` when encountering an error. (Bug #16210351)

- Replication: A zero-length name for a user variable (such as @``) was incorrectly considered to be a

sign of data or network corruption when reading from the binary log. (Bug #16200555, Bug #68135)

- Replication: `mysqlbinlog` can connect to a remote server and read its binary logs. In MySQL 5.6 and

later, this tool can also wait for the server to generate and send additional events, in practice behaving like a slave connecting to a master. In cases where the server sent a heartbeat, `mysqlbinlog` was unable to handle it properly. As a consequence, `mysqlbinlog` failed at this point, without reading any more events from the server. To fix this problem, `mysqlbinlog` now ignores any binary log events of type `HEARTBEAT_LOG_EVENT` that it receives. (Bug #16104206)

- Replication: `STOP SLAVE` could cause a deadlock when issued concurrently with a statement

such as `SHOW STATUS` that retrieved the values for one or more of the status variables

```
Slave_retried_transactions, Slave_heartbeat_period, Slave_received_heartbeats,
```

`Slave_last_heartbeat`, or `Slave_running`. (Bug #16088188, Bug #67545)References: See also: Bug #16088114.

- Replication: Backtick (`) characters were not always handled correctly in internally generated SQL

statements, which could sometimes lead to errors on the slave. (Bug #16084594, Bug #68045)

## MySQL 5.6 Release Notes

References: This issue is a regression of: Bug #14548159, Bug #66550.

- Replication: In order to provision or to restore a server using GTIDs, it is possible to set `gtid_purged`

to a given GTID set listing the transactions that were imported. This operation requires that the global`gtid_executed` and `gtid_purged` server system variables are empty. (This is done in order to avoid the possibility of overriding server-generated GTIDs.)The error message `GTID_PURGED can only be set when GTID_EXECUTED is empty` that was raised when this requirement was not met could be confusing or misleading because it did not specify the scope of the affected variables. To prevent this from happening, error messages that refer to variables relating to GTIDs now specify the scope of any such variables when they do so. (Bug#16084426, Bug #68038)

- Replication: The session-level value for `gtid_next` was incorrectly reset on the slave for all rollbacks,

which meant that GTIDs could be lost for multi-statement transactions, causing the slave to stop with an`ER_GTID_NEXT_TYPE_UNDEFINED_GROUP` error. Now this is done only when a complete transaction is being rolled back, or when `autocommit` is enabled. (Bug #16084206)

- Replication: Using the `--replicate-*` options (see Replica Server Options and Variables) could in

some cases lead to a memory leak on the slave. (Bug #16056813, Bug #67983)

- Replication: In some cases, when the slave could not recognize the server version of the master, this

could cause the slave to fail. (Bug #16056365)

- Replication: In certain cases, the dump thread could send a heartbeat out of synchronisation with

format description events. One of the effects of this issue what that, after provisioning a new server from a backup data directory and setting `--gtid-mode=ON` and enabling autopositioning (see CHANGE MASTER TO Statement), replication failed to start, with the error `Read invalid event from``master...`. The same problem could also cause GTID-based replication to fail due to skipped events following a unplanned shutdown of the master. (Bug #16051857)

- Replication: Table IDs used in replication were defined as type `ulong` on the master and `uint` on the

slave. In addition, the maximum value for table IDs in binary log events is 6 bytes (281474976710655).

This combination of factors led to the following issues:

- Data could be lost on the slave when a table was assigned an ID greater than `uint`.
- Table IDs greater than 281474976710655 were written to the binary log as 281474976710655.
- This led to a stopped slave when the slave encountered two tables having the same table ID.

To fix these problems, IDs are now defined by both master and slave as type `ulonglong` but constrained to a range of 0 to 281474976710655, restarting from 0 when it exceeds this value. (Bug#14801955, Bug #67352)

- Replication: Internal objects used for relay log information were only partially deleted before freeing

their memory. (Bug #14677824)

- Replication: It was possible in certain cases—immediately after detecting an EOF in the dump thread

read event loop, and before deciding whether to change to a new binary log file—for new events to be written to the binary log before this decision was made. If log rotation occurred at this time, any events that occurred following EOF detection were dropped, resulting in loss of data. Now in such cases, steps are taken to make sure that all events are processed before allowing the log rotation to take place. (Bug#13545447, Bug #67929)References: See also: Bug #16016886.

## MySQL 5.6 Release Notes

- Replication: If the disk becomes full while writing to the binary log, the server hangs until space is freed

up manually. It was possible after this was done for the MySQL server to fail, due to an internal status value being set when not needed. Now in such cases, rather than trying to set this status, a warning is written in the error log instead. (Bug #11753923, Bug #45449)

- Microsoft Windows: A server started with `--shared-memory` to support shared-memory connections

could crash when receiving requests from multiple threads. (Bug #13934876)

- Solaris: `mysql_install_db` did not work in Solaris 10 sparse root zones. (Bug #68117, Bug

#16197860)

- `InnoDB` now reports row and table locks to the thread pool plugin. Deadlocks within a thread group

could occur otherwise. (Bug #16448639)

- Failure to handle a full-text search wildcard properly could cause the server to exit. (Bug #16446108)
- `SHOW ENGINE PERFORMANCE_SCHEMA STATUS` could report incorrect memory-allocation values when

the correct values exceeded 4GB. (Bug #16414644)

- The server could exit if a prepared statement attempted to create a table using the name of an existing

view while an SQL handler was opened. (Bug #16385711)

- Performance Schema statement tokenization overhead was reduced. (Bug #16382260)
- A long database name in a `GRANT` statement could cause the server to exit. (Bug #16372927)
- On Linux, a race condition involving `epoll()` could cause the thread pool plugin to miss events. This

was most likely on systems with greater than 16 cores. (Bug #16367483)

- Some aggregate queries attempted to allocate excessive memory. (Bug #16343992)
- For debug builds, an assertion could be raised if a statement failed with autocommit enabled just before

an `XA START` statement was issued. (Bug #16341673)

- Very small `join_buffer_size` values could cause an assertion to be raised. (Bug #16328373)
- The `BUILD-CMAKE` file in MySQL distributions was updated with the correct URL for `CMake` information.

(Bug #16328024)

- The optimizer's attempt to remove redundant subquery clauses raised an assertion when executing a

prepared statement with a subquery in the `ON` clause of a join in a subquery. (Bug #16318585)References: This issue is a regression of: Bug #15875919.

- Incorrect results were returned if a query contained a subquery in an `IN` clause which contained an `XOR`

operation in the `WHERE` clause. (Bug #16311231)

- A Valgrind failure could occur if a `CREATE USER` statement was logged to the general query log and the

`old_passwords` system variable was set to 2. (Bug #16300620)

- For debug builds, checking of password constraints could raise an assertion for statements that updated

passwords. (Bug #16289303)

- Conversion of numeric values to `BIT` could yield unexpected results. (Bug #16271540)
- Fixed warnings when compiling with XCode 4.6. Fixed warnings when compiling when the

`_XOPEN_SOURCE` or `isoctal` macro was already defined in the environment. (Bug #16265300, Bug#60911, Bug #12407384)

## MySQL 5.6 Release Notes

- In the range optimizer, an index merge failure could cause a server exit. (Bug #16241773)
- For upgrade operations, RPM packages produced unnecessary errors about being unable to access

`.err` files. (Bug #16235828)

- Queries using range predicates that were evaluated using the LooseScan semijoin strategy could return

duplicate rows. (Bug #16221623)References: This issue is a regression of: Bug #14728469.

- Certain legal `HAVING` clauses were rejected as invalid. (Bug #16221433)
- yaSSL did not perform proper padding checks, but instead examined only the last byte of cleartext and

used it to determine how many bytes to remove. (Bug #16218104)

- The Performance Schema could return incorrect values for the `PROCESSLIST_INFO` column of the

`threads` table. (Bug #16215165)

- A full-text query using Boolean mode could return zero results in some cases where the search term was

a quoted phrase:

- If the quoted phrase was preceded by a + sign. For example, this combination of a Boolean + operator

and a phrase would return zero results:

```
WHERE MATCH(content) AGAINST('+"required term due to plus sign"' IN BOOLEAN MODE)
```

- If the quoted phrase contained any stopwords. For example, the stopword "the" inside the phrase

caused the query to return zero results:

```
WHERE MATCH(content) AGAINST('"stopword inside the phrase"' IN BOOLEAN MODE)
```

(Bug #16206253, Bug #68150)

- `mysql_config --libs` displayed incorrect output. (Bug #16200717)
- Invocation of the range optimizer for a `NULL` select caused the server to exit. (Bug #16192219)
- If, in a `SELECT`, the `HAVING` clause contained a function call which itself contained an alias to a selected

expression, the server could sometimes exit. (Bug #16165981)

- For debug builds, the server could exit due to incorrect calculation of applicable indexes for a join that

involved `const` tables. (Bug #16165832)

- A bug in range optimization sometimes led to incorrect condition calculation for index merge union. This

could lead to missing rows. (Bug #16164031, Bug #68194, Bug #16229746)

```
- For a CREATE TABLE (... col_name TIMESTAMP DEFAULT CURRENT_TIMESTAMP ...) ...
```

`SELECT` statement for which the `SELECT` did not provide a value for the `TIMESTAMP` column, that column was set to '0000-00-00 00:00:00', not the current timestamp. (Bug #16163936)

- Using `GROUP BY WITH ROLLUP` in a prepared statement could cause the server to exit. (Bug

#16163596)

- With the thread pool plugin enabled, large numbers of connections could lead to a Valgrind panic or

failure of clients to be able to connect. (Bug #16088658, Bug #16196591)

- Performance Schema instrumentation was missing for slave worker threads. (Bug #16083949)

## MySQL 5.6 Release Notes

- The server executed `EXPLAIN FORMAT=JSON` for some malformed queries improperly. (Bug

#16078557)

- With statement-based binary logging, dropping a `TEMPORARY` `InnoDB` table could cause a segmentation

fault. (Bug #16076275)

- Setting the `slave_rows_search_algorithms` system variable to an inappropriate value could cause

the server to exit. (Bug #16074161)

- `SET PASSWORD` and `GRANT ... IDENTIFIED BY` have no effect on the password of a user who

is authenticated using an authentication plugin that accesses passwords stored externally to the mysql.user table. But attempts to change the password of such a user produced no warning, leading to the impression that the password had been changed when it was not. Now MySQL issues an`ER_SET_PASSWORD_AUTH_PLUGIN` warning to indicate that the attempt was ignored. (Bug #16072004)

- Directory name manipulation could result in stack overflow on OS X and Windows. (Bug #16066243)
- The initial `test` database contained a `dummy.bak` file that prevented `DROP DATABASE` from working.

This file is no longer included. Also, a `db.opt` file is now included that contains these lines:

```
default-character-set=latin1
default-collation=latin1_swedish_ci
```

(Bug #16062056)

- Issuing a `PREPARE` statement using certain combinations of stored functions and user variables caused

the server to exit. (Bug #16056537)

- Setting a system variable to `DEFAULT` could cause the server to exit. (Bug #16044655)
- For debug builds, if the server was started with binary logging disabled, executing `SHOW RELAYLOG`

`EVENTS` from within a stored procedure raised an assertion. (Bug #16043173)

- The query parser leaked memory for some syntax errors. (Bug #16040022)
- During shutdown, the server could attempt to lock an uninitialized mutex. (Bug #16016493)
- The `--default-authentication-plugin` option permitted invalid plugin values, and did not always

set the `old_passwords` system variable to a value appropriate for the named plugin. (Bug #16014394)

- The `--character-set-server` option could set connection character set system variables to values

such as `ucs2` that are not permitted. (Bug #15985752, Bug #23303391)

- Under some circumstances, `mysql --secure-auth` permitted passwords to be sent to the server

using the old (pre-4.1) hashing format. (Bug #15977433)

- When a partition is missing, code in `ha_innodb.cc` would retry 10 times and sleep for a microsecond

each time while holding `LOCK_open`. The retry logic for partitioned tables was introduced as a fix for Bug#33349 but did not include a test case to validate it. This fix removes the retry logic for partitioned tables. If the problem reported in Bug#33349 reappears, a different solution will be explored. (Bug#15973904)

- Joins of exactly 32 tables and containing a `HAVING` clause returned an empty result. (Bug #15972635)
- A `mysys` library string-formatting routine could mishandle width specifiers. (Bug #15960005)
- Table creation operations added entries to the `file_instances` Performance Schema table, but these

were not always removed for table drop operations. (Bug #15927620)

## MySQL 5.6 Release Notes

- With index condition pushdown enabled, queries for which the pushed-down condition contained no

columns in the used index could be slow. (Bug #15896009)

- A query with an `EXISTS/IN/ALL/ANY` subquery with an `ORDER BY` clause ordering by an outer column

of type `BLOB` that is not in the select list caused an assertion to fire. (Bug #15875919)References: See also: Bug #14728142.

- In special cases, the optimizer did not consider indexes that were applicable to query processing,

resulting in potentially suboptimal execution and incorrect `EXPLAIN` output. (Bug #15849135, Bug#16094171)

- Creating an `InnoDB` table with a `FULLTEXT` index could encounter a serious error if the table name

contained nonalphanumeric characters. (Bug #14835178, Bug #16036699)

- Enabling the query cache during high client contention could cause the server to exit. (Bug #14727815)
- The MSI Installer installed MySQL in “per-user” mode, which could result in conflicts or failure to detect

an existing installation if two users installed MySQL on the same machine. Now the MSI Installer uses“per-machine” installation mode. (Bug #14711808)

- The server sometimes failed to respect `MAX_CONNECTIONS_PER_HOUR` limits on user connections. (Bug

#14627287)

- The optimizer could return incorrect results after transforming an `IN` subquery with aggregate functions

to an `EXISTS` subquery. (Bug #14586710)

- `SET PASSWORD` for anonymous users did not work correctly. (Bug #14561102)
- When a client program loses the connection to the MySQL server or if the server begins a shutdown

after the client has executed `mysql_stmt_prepare()`, the next `mysql_stmt_prepare()` returns an error (as expected) but subsequent `mysql_stmt_execute()` calls crash the client. (Bug #14553380)

- Previously, if multiple `--login-path` options were given, `mysql_config_editor` ignored all but the

last one. Now multiple `--login-path` options result in an error. (Bug #14551712)

- `SHOW COLUMNS` on a view defined as a `UNION` of `Geometry` columns could cause the server to exit.

(Bug #14362617)

```
- The sha256_password_private_key_path and sha256_password_public_key_path system
```

variables indicate key files for the `sha256_password` authentication plugin, but the server failed to properly check whether the key files were valid. Now in the event that either key file is invalid, the server logs an error and exits. (Bug #14360513)

- `SET var_name = VALUES(col_name)` could cause the server to exit. This syntax is now prohibited

because in `SET` context there is no column name and the statement returns `ER_BAD_FIELD_ERROR`.

(Bug #14211565)

- The `COM_CHANGE_USER` command in the client/server protocol did not properly use the character set

number in the command packet, leading to incorrect character set conversion of other values in the packet. (Bug #14163155)

- Invoking the `FORMAT()` function with a locale and a very large number could cause the server to exit.

(Bug #14040155)

- yaSSL rejected some valid server SSL certificates. (Bug #13777928)
- Certain plugin-related conditions can make a user account unusable:

## MySQL 5.6 Release Notes

- The account requires an authentication plugin that is not loaded.
- The account requires the `sha256_password` authentication plugin but the server was started with

neither SSL nor RSA enabled as required by this plugin.

The server now checks those conditions by default and produces warnings for unusable accounts. This checking slows down server initialization and `FLUSH PRIVILEGES`, so it is made optional by means of the new `validate_user_plugins` system variable. This variable is enabled by default, but if you do not require the additional checking, you can disable it at startup to avoid the performance decrement.

(Bug #13010061, Bug #14506305)

- Passing an unknown time zone specification to `CONVERT_TZ()` resulted in a memory leak. (Bug

#12347040)

- The obsolete `linuxthreads.txt` and `glibc-2.2.5.patch` files in the `Docs` directory of MySQL

distributions have been removed. (Bug #11766326)

- `mysql_install_db` did not escape `'_'` in the host name for statements written to the grant tables.

(Bug #11746817)

- With `explicit_defaults_for_timestamp` enabled, inserting `NULL` into a `TIMESTAMP NOT NULL`

column now produces an error (as it already did for other `NOT NULL` data types), instead of inserting the current timestamp. (Bug #68472, Bug #16394472)

- Handling of `SQL_CALC_FOUND_ROWS` in combination with `ORDER BY` and `LIMIT` could lead to incorrect

results for `FOUND_ROWS()`. (Bug #68458, Bug #16383173)

- If `INET6_NTOA()` or `INET6_ATON()` returned `NULL` for a row in a result set, following rows also

returned `NULL`. (Bug #68454, Bug #16373973)

- A statement with an aggregated, nongrouped outer query and an aggregated, nongrouped subquery in

the `SELECT` list could return incorrect results. (Bug #68372, Bug #16325175)

- Adding an `ORDER BY` clause following an `IN` subquery could cause duplicate rows to be returned. (Bug

#68330, Bug #16308085)

- If the server was started with `--skip-grant-tables`, `ALTER USER ... PASSWORD EXPIRE`

caused the server to exit. (Bug #68300, Bug #16295905)

- Configuring with `-DWITH_SSL=/path/to/openssl` resulted in link errors due to selection of the

incorrect `libcrypto`. (Bug #68277, Bug #16284051)

- If `mysql` is built with the bundled `libedit` library, the library is built as static code, to avoid linking to

a different dynamic version at runtime. Dynamic linking could result in use of a different, incompatible version and a segmentation fault. (Bug #68231, Bug #16296509)

- Some table I/O performed by the server when calling a storage engine were missing from the statistics

collected by the Performance Schema. (Bug #68180, Bug #16222630)

- The Perl version of `mysql_install_db` mishandled some error messages. (Bug #68118, Bug

#16197542)

- For arguments with fractional seconds greater than six decimals, `SEC_TO_TIME()` truncated, rather

than rounding as it should have. (Bug #68061, Bug #16093024)

- Queries with many values in a `IN()` clause were slow due to inclusion of debugging code in non-

debugging builds. (Bug #68046, Bug #16078212)

## MySQL 5.6 Release Notes

References: See also: Bug #58731, Bug #11765737.

```
- ALTER TABLE tbl_name ADD COLUMN col_name TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```

`ON UPDATE CURRENT_TIMESTAMP` inserted `0000-00-00 00:00:00` rather than the current timestamp if the alteration was done in place rather than by making a table copy. (Bug #68040, Bug#16076089)

- `mysqld_safe` used the nonportable `-e` test construct. (Bug #67976, Bug #16046140)
- Nonspatial indexes only support exact-match lookups for spatial columns, but the optimizer incorrectly

used `range` access in some cases, leading to incorrect results. (Bug #67889, Bug #15993693)

- For `EXPLAIN DELETE` and `EXPLAIN UPDATE` the `possible_keys` column listed all indexes, not just

the applicable indexes. (Bug #67830, Bug #15972078)

- MySQL failed to build if configured with `WITH_LIBWRAP` enabled. (Bug #67018, Bug #16342793)
- `CMake` did not check whether the system `zlib` had certain functions required for MySQL, resulting in

build errors. Now it checks and falls back to the bundled `zlib` if the functions are missing. (Bug #65856,Bug #14300733)

- If a dump file contained a view with one character set and collation defined on a view with a different

character set and collation, attempts to restore the dump file failed with an “illegal mix of collations” error.

(Bug #65382, Bug #14117025)

- If the server was started without a `--datadir` option, `SHOW VARIABLES` could show an empty value for

the `datadir` system variable. (Bug #60995, Bug #12546953)

- For debug builds, some queries with `SELECT ... FROM DUAL` nested subqueries raised an assertion.

(Bug #60305, Bug #11827369)

```
- The --log-slow-admin-statements and --log-slow-slave-statements
```

command options now are exposed at runtime as the `log_slow_admin_statements` and`log_slow_slave_statements` system variables. Their values can be examined using `SHOW``VARIABLES`. The variables are dynamic, so their values can be set at runtime. (The options were actually replaced by the system variables, but as system variables can be set at server startup, no option functionality is lost.) (Bug #59860, Bug #11766693)

- `UNION ALL` on `BLOB` columns could produce incorrect results. (Bug #50136, Bug #11758009)
- An out-of-memory condition could occur while handling an out-of-memory error, leading to recursion in

error handling. (Bug #49514, Bug #11757464)

- The `REPLACE()` function produced incorrect results when a user variable was supplied as an argument

and the operation was performed on multiple rows. (Bug #49271, Bug #11757250)

- `UNION` type conversion could incorrectly turn unsigned values into signed values. (Bug #49003, Bug

#11757005)

- Setting `max_connections` to a value less than the current number of open connections caused the

server to exit. (Bug #44100, Bug #11752803)

- The optimizer used Loose Index Scan for some queries for which this access method is inapplicable.

(Bug #42785, Bug #11751794)

- View access in low memory conditions could raise a debugging assertion. (Bug #39307, Bug

#11749556)

## MySQL 5.6 Release Notes
