---
title: "Changes in MySQL 5.6.22 (2014-12-01, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=66"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Compilation Notes
- Deprecation and Removal Notes
- Security Notes
- Bugs Fixed

> Compilation Notes

- Noisy compiler warnings on FreeBSD 10 were silenced. (Bug #18790490)
- `CMake` workarounds for older OS X and XCode versions were removed. On OS X, compilation always

uses Clang, even for 32-bit builds.

Compilation on OS X is now supported for OS X 10.8 and up, using XCode 5 and up. Compilation on older versions may work but is unsupported. (Bug #18510941)

- Previously, the `MYSQL_MAINTAINER_MODE` `CMake` option was turned on by default for debug builds

and off for release builds, and `MYSQL_MAINTAINER_MODE` caused `-Werror` to be enabled when building with GCC. This made it cumbersome to enable `-Werror` under certain conditions, such as when compiling with Clang.

Now, `MYSQL_MAINTAINER_MODE` is on by default when compiling debug builds with GCC, and`MYSQL_MAINTAINER_MODE` enbles `-Werror` regardless of whether GCC or Clang is used. Enabling`-Werror` with Clang can be done simply by explicitly setting `-DMYSQL_MAINTAINER_MODE=1` when running `CMake`. In addition, some compilation warnings reported by Clang 3.4 were fixed, making it possible to build the default debug build with `-Werror`. (Bug #18313717)

- Build support was modified to produce the same warnings for Clang as for `gcc`. (Bug #17959689)
- `CMake` configuration for the `Clang` compiler sets more appropriate flags for building on Linux.

Specifically, `-g -fno-omit-frame-pointer -fno-strict-aliasing` is now added. (Bug#17633291)

> Deprecation and Removal Notes

- Replication: The variable `binlogging_impossible_mode` now has an alias named

`binlog_error_action`, which is the preferred name. `binlogging_impossible_mode` is now deprecated. (Bug #19507567)

- Replication: The global scope for the `sql_log_bin` system variable has been deprecated, and this

variable can now be set with session scope only. The statement `SET GLOBAL SQL_LOG_BIN` now produces an error. It remains possible to read the global value of `sql_log_bin`, but doing so produces a warning. You should act now to remove from your applications any dependencies on reading this value; the global scope `sql_log_bin` is removed in MySQL 8.0. (Bug #67433, Bug #15868071)

## MySQL 5.6 Release Notes

- `OLD_PASSWORD()` is deprecated, but no warning was produced when it was invoked. (Bug #73376, Bug

#19285177)

> Security Notes

- yaSSL was upgraded to version 2.3.5. (Bug #19695101, Bug #20201864)
- The linked OpenSSL library for the MySQL Commercial Server has been updated from version 1.0.1h

to version 1.0.1j. Issues fixed in the new version are described at http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #74174, Bug #19717832)

> Bugs Fixed

- InnoDB: An `ALTER TABLE` operation raised an assertion. When a foreign key object was removed from

the dictionary cache, an incorrect foreign key object was removed from the rb-tree. (Bug #19908343)References: This issue is a regression of: Bug #18806829.

- InnoDB: In debug builds, setting the `innodb_limit_optimistic_insert_debug` debug

configuration option to 1 caused an infinite B-tree page split. (Bug #19904003, Bug #74605)

- InnoDB: The `dict_set_corrupted()` function attempted to update the clustered index of the

`SYS_INDEXES` data dictionary table incorrectly. (Bug #19584379)

- InnoDB: Pages with a checksum value of zero were incorrectly treated as empty pages. A page should

only be considered empty if its checksum value and LSN field values are zero. (Bug #19500258, Bug#73689)References: This issue is a regression of: Bug #17335427.

- InnoDB: The `InnoDB` data dictionary was not updated when a `ALTER TABLE ... CHANGE COLUMN`

operation changed the case of the column name. (Bug #19465984)

- InnoDB: A memory access violation caused `fts_optimize_thread` and `mysqld` to terminate. (Bug

#19314480)

- InnoDB: A procedure, called from a function to perform an operation on a temporary table, caused the

server to halt. (Bug #19306524)

- InnoDB: Attempting to shut down the server after starting the server with `innodb_force_recovery=6`

resulted in a hang. (Bug #19265668, Bug #73341)

- InnoDB: A `COMMIT` operation related to full-text search resulted in a segmentation fault. (Bug

#18503734)

- InnoDB: If a database is named using uppercase letters on a MySQL server with

`lower_case_table_names=2` (which is default on OS X), `InnoDB` stores the database name as specified in the `InnoDB` internal system table (`SYS_TABLES`) but stores the name in lowercase on disk.

During crash recovery, the case mismatch resulted in a conflict that marked the tablespace `.ibd` file as missing. The patch for this bug converts database names to lowercase on crash recovery. (Bug#18412598, Bug #72043)

- InnoDB: In debug builds, the `InnoDB` Lock Monitor asserted after a `DROP TABLE` operation, and the

`InnoDB` Monitor encountered an assertion in `buf_page_get_gen`. (Bug #18062698, Bug #71343, Bug#18173184, Bug #68116)

## MySQL 5.6 Release Notes

- InnoDB: A `CREATE TABLE` operation that failed when `innodb_strict_mode` was enabled succeeded

without printing a warning when `innodb_strict_mode` was disabled. (Bug #17852083)

- InnoDB: For explicit cache coherency, a write barrier was added to the head of

`os_thread_create_func()`, and a read barrier was added to assertion code in`rw_lock_free_func()`. (Bug #13364876, Bug #62692, Bug #18870970, Bug #72809)

- InnoDB: The MySQL 5.6.20 patch for Bug #16963396 / MySQL Bug #69477 limited the size

of redo log `BLOB` writes to 10% of the redo log file size. This limitation has been relaxed. Redo log `BLOB` writes are now limited to 10% of the total redo log size (`innodb_log_file_size` *

```
innodb_log_files_in_group).
```

As a result, `innodb_log_file_size` * `innodb_log_files_in_group` should be 10 times larger than the largest `BLOB` data size found in the rows of your tables plus the length of other variable length fields (`VARCHAR`, `VARBINARY`, and `TEXT` type fields). No action is required if `innodb_log_file_size`* `innodb_log_files_in_group` is already sufficiently large or if your tables contain no `BLOB` data.

(Bug #73707, Bug #19498877)References: See also: Bug #16963396.

- Partitioning: When multiple columns are used in `KEY` partitioning, their order may help determine

the partition in which the row is placed. Changing this order by means of an `ALTER TABLE` that uses`ALGORITHM=INPLACE` can lead to inconsistency when placing rows in partitions; in other words, a row inserted before such an operation is placed in one partition, but the same row inserted afterwards is placed in a different one. For this reason, altering the order of a multicolumn index online is no longer allowed when that index is also used as the base for partitioning the table by `KEY`; instead, you must use a copying `ALTER TABLE` to perform the change. (Bug #17896265)

- Replication: When using a MySQL version that had been compiled with the `WITH_DEBUG` option

enabled, using `expire_logs_days` to purge binary logs caused a restart to crash the server. This problem arose after the fix for Bug #17283409. The fix ensures that `current_thd` is checked before calling `DEBUG_SYNC()`. (Bug #19553099)

- Replication: Sometimes the slave I/O thread leaves a partial group in the current relay log, for

example when it is killed or stopped. After it is restarted, a new relay log is created on rotation and a pair of `ROTATE_EVENT` and `FORMAT_DESCRIPTION_EVENT` is replicated from master and written into the new relay log. When using a multithreaded slave, problems such as error 1755 were encountered when applying the remaining part of the group in the relay log. This fix ensures that if`MASTER_AUTO_POSITION` is enabled, then the worker rolls back the partial group, finishes its work, and then applies the new complete copy of the group. If `MASTER_AUTO_POSITION` is disabled, the worker does not roll back the partial group. (Bug #19545298)

- Replication: A corrupted header length in `FORMAT_DESCRIPTION_LOG_EVENT` could cause the server

to stop unexpectedly. This was due to `FORMAT_DESCRIPTION_LOG_EVENT` being considered invalid if the header length was too short. (Bug #19145712)

- Replication: Start log events were not checked by slaves for minimum size. (Bug #19145698)
- Replication: When using row-based replication with `slave_type_conversions` enabled, a binary

log with more than one `Rows_log_event` in succession caused a crash. This was due to the temporary tables generated as part of the `slave_type_conversions` process being released too early. This fix ensures that the temporary tables are not released too early, and also ensures that long transactions do not cause an out of memory error. (Bug #18770469, Bug #19704825)

- Replication: When using binary log files that had been manually copied from the master, for

example to avoid I/O thread reading delay, a multithreaded slave generated error 1755. Because the `Previous_gtids` log event is logged using the master's `server_id` and not the slave's

## MySQL 5.6 Release Notes

`server_id,` the previous events were not being skipped correctly. This fix ensures that the events in `Previous_gtids` log event are always skipped, regardless of whether they are from the relay log(generated on the slave) or from the binary log (generated on the master and manually copied to the slave as the relay log). (Bug #17812024)

- Replication: When replicating from an earlier version MySQL master, such as version 4.1, checksums

are not used for events. Replicating to a slave running a newer version of MySQL, such as version 5.6,which has `slave_sql_verify_checksum` enabled by default meant that the last 4 bytes of events from the older master were being incorrectly interpreted as the checksum. A warning is now generated and to avoid such a situation, set `slave_sql_verify_checksum=0` to disable checksums on the slave. (Bug #17276183)

- Replication: When restarting MySQL with `relay_log_recovery` enabled to recover from a crash,

if the SQL thread had never been started, the position from which to start recovery was not correctly initialized because `Relay_Master_Log_File` was missing. This fix ensures that in such a situation each of the relay logs, starting from the first relay log file, is searched for a rotate event from the master,which specifies where replication started from. This rotate event is then used to set the SQL thread's`Relay_Master_Log_File` and `Relay_Log_Pos` and recovery continues as normal. (Bug #73039,Bug #19021091)

- Replication: When using GTIDs for replication and with `MASTER_AUTO_POSITION` enabled, if a

slave requested GTIDs which had been already been purged by the master, the master was sending all available GTIDs. This happened because the master reads all available binary logs and searches for a binary log which contains a GTID that is not contained in the union of `gtid_executed` and`gtid_retrieved`. If such a GTID is found, the master starts sending the information starting from that location. In a situation where the union of the slave's `gtid_executed` and `gtid_retreived` set did not contain the master's `gtid_purged` set, the slave would expect GTIDs which had already been purged by the master. This fix ensures that in such a situation, the slave's I/O thread is aborted with an error "Master has purged binary logs containing GTIDs that the slave requires.". (Bug #73032, Bug#19012085)

- Replication: A kernel mutex contention was being caused because `mysqlbinlog` was calling

localtime() for every event read, which in turn called stat(/etc/localtime). This fix ensures that`mysqlbinlog` uses localtime_r(), which is optimized to store the read only timezone internal structure.

This also means that `mysqlbinlog` now establishes the time zone at the beginning of processing and you can not change it during processing. This is the same behavior as MySQL server. (Bug #72701, Bug#18808072)

- Microsoft Windows: On Windows, the `replace` utility did not work. (Bug #16581605)
- The AppArmor profile installed by Debian packages was missing entries required for successful server

startup. (Bug #20057782)

- `InnoDB` table checksum calculation could yield an incorrect result if the value of the

`innodb_checksum_algorithm` system variable was modified during the operation. (Bug #19931177)

- For a materialized internal temporary table used with semijoins, the optimizer could add an index to it but

then use an inappropriate lookup strategy, causing a server exit. (Bug #19695490, Bug #21782943)

- `GROUP BY` or `ORDER BY` on a `CHAR(0) NOT NULL` column could lead to a server exit. (Bug

#19660891)

- With the `validate_password` plugin activated and dictionary lookups enabled, passing a user-defined

variable to `PASSWORD()` could cause a server exit. (Bug #19388163)

- Debian packages were built using the `complex` set of character sets, not the `all` set of character sets.

(Bug #19363801)

## MySQL 5.6 Release Notes

- `mysqldump` failed to report a disk-full error if the dump destination was located on an NFS mount. (Bug

#18817867)

- Previously, `InnoDB` permitted a foreign key to be created which referenced a parent table for which

the user did not have sufficient privileges. Now, the user must have at least one of the `SELECT`,`INSERT`, `UPDATE`, `DELETE`, or `REFERENCES` privileges for the parent table to create a foreign key. (Bug#18790730, Bug #11746917)

- Copying `InnoDB` tables containing full-text columns from Windows to Linux caused a server exit on

Linux during full-text index initialization. (Bug #18285007, Bug #19864963, Bug #73155)

- On Debian, `apt-get upgrade` did not replace some packages from the repository. The workaround is

to first manually install `mysql-client` by running `apt-get install mysql-client` or directly run`apt-get dist-upgrade`. (Bug #75485, Bug #20348793)

- On CentOS 6, specifying a relative path name for the `--socket` option caused MySQL startup script

failure. (Bug #74111, Bug #19775856)

- In Solaris 11.2, `dtrace -V` output changed from `Sun D` to `Oracle D`, causing detection of DTrace

availability to fail during MySQL configuration. (Bug #73826, Bug #19586917)

- `mysql_config --libs_r` produces output containing link flags for `libmysqlclient_r`, even

though that library was removed in MySQL 5.5 and replaced with a symbolic link to the underlying`libmysqlclient` library. The output now refers directly to `libmysqlclient`. (The implication is that it is no longer necessary to maintain the symbolic link for the sake of being able to use `mysql_config``--libs_r`.) (Bug #73724, Bug #19506315)

- For statement digest calculation, the Performance Schema failed to recognize signed literal numbers as

values representable by ? and created multiple digests for statements that should have had the same signature. Now all instances of unary plus and unary minus followed by a number reduce to ? in digests.

(Bug #73504, Bug #19389709)

- Compilation on Windows using Visual Studio 2013 resulted in “unresolved external symbol” errors. (Bug

#73461, Bug #19351573)

- Certain queries for which subquery materialization or `UNION DISTINCT` was used together with a hash

index on a temporary table could produce incorrect results or cause a server exit. (Bug #73368, Bug#19297190)

- The `IS_FREE_LOCK()` and `IS_USED_LOCK()` function implementations contained a race condition

due to which they could access freed memory when a user lock was concurrently checked and freed.

Accessing freed memory could result in an incorrect function return value or server exit. (Bug #73123,Bug #19070633)

- `LOCK TABLES` sometimes acquired an insufficiently strong lock for implicitly locked tables. (Bug #72887,

Bug #18913551)

- The `ENABLED_LOCAL_INFILE` `CMake` option incorrectly was enabled by default. (Bug #72106, Bug

#18448743)

- Use of ODBC-format date literals could produce incorrect query results. (Bug #69233, Bug #16812821)
- `mysql_install_db` ignored option files in the default locations. (Bug #68807, Bug #16570238)
- `mysql_setpermission` failed to properly quote user names in SQL statements that it generated. (Bug

#66317, Bug #14486004)
