---
title: "Changes in MySQL 5.6.16 (2014-01-31, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=92"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Known limitations of this release:Note Building MySQL from source on Windows using Visual Studio 2008 fails with an `identifier not found` error. Later versions of Visual Studio are unaffected. The workaround is to set the `CMake` build option`INNODB_PAGE_ATOMIC_REF_COUNT` to `OFF`. This option is `ON` by default.

Note If you have `InnoDB` tables with full-text search indexes and you are upgrading from MySQL 5.6.10 to a MySQL version up to and including MySQL 5.6.18, the server will fail to start after the upgrade (Bug#72079). This bug is fixed in MySQL 5.6.19.

As a workaround, remove full-text search indexes prior to upgrading and rebuild full-text search indexes after the upgrade is completed.

- Functionality Added or Changed
- Bugs Fixed

## MySQL 5.6 Release Notes

> Functionality Added or Changed

- InnoDB: New global configuration parameters, `innodb_status_output` and

`innodb_status_output_locks`, allow you to dynamically enable and disable the standard `InnoDB`Monitor and `InnoDB` Lock Monitor for periodic output. Enabling and disabling monitors for periodic output by creating and dropping specially named tables is deprecated and may be removed in a future release. For additional information, see InnoDB Monitors. (WL #7377)

- Previously, `ALTER TABLE` in MySQL 5.6 could alter a table such that the result had temporal columns

in both 5.5 and 5.6 format. Now `ALTER TABLE` upgrades old temporal columns to 5.6 format for `ADD``COLUMN`, `CHANGE COLUMN`, `MODIFY COLUMN`, `ADD INDEX`, and `FORCE` operations. This conversion cannot be done using the `INPLACE` algorithm because the table must be rebuilt, so specifying`ALGORITHM=INPLACE` in these cases results in an error. Specify `ALGORITHM=COPY` if necessary.

When `ALTER TABLE` does produce a temporal-format conversion, it generates a message that can be

```
displayed with SHOW WARNINGS: TIME/TIMESTAMP/DATETIME columns of old format have
```

`been upgraded to the new format`. (Bug #17246318)

- `CMake` now supports a `-DTMPDIR=dir_name` option to specify the default `tmpdir` value. If unspecified,

the value defaults to `P_tmpdir` in `<stdio.h>`. Thanks to Honza Horak for the patch. (Bug #68338, Bug#16316074)

> Bugs Fixed

- InnoDB; Replication: Attempting to reset a replication slave while `innodb_force_recovery`

is greater than 0 would return a cryptic error message: `ERROR(1030) HY000: Got error``-1 from storage engine`. The error message has been changed to: `ERROR HY000:``Operation not allowed when innodb_force_recovery > 0`. Replication options such as`relay_log_info_repository=TABLE` and `master_info_repository=TABLE` store information in tables in `InnoDB`. When `innodb_force_recovery` is greater than 0, replication tables cannot be updated which may cause replication administration commands to fail. (Bug #17287443, Bug #69907)

- InnoDB; Replication: Using the `InnoDB` `memcached` plugin (see InnoDB memcached Plugin) with

`innodb_api_enable_binlog` set to 1 caused the server to leak memory. (Bug #70757, Bug#17675622)

- InnoDB: A boolean mode full-text search query would result in a memory access violation during

parsing. (Bug #17978763)

- InnoDB: When new indexes are added by an `ALTER TABLE` operation, instead of only saving table-

level statistics and statistics for the new indexes, `InnoDB` would save statistics for the entire table,including the table's other indexes. This behavior slowed `ALTER TABLE` performance. (Bug #17848838,Bug #16511145)

- InnoDB: Due to a parser error, full-text search queries that include a sub-expression could return the

wrong result. (Bug #17840768)

- InnoDB: The `innochecksum` tool did not use a Windows-specific API to retrieve file size information,

which resulted in an incorrect error message (`Error: ibdata1 cannot be found`) when the MySQL 5.6 `innochecksum` 2GB file size limit was exceeded. `innochecksum` now provides support for files larger than 2GB in both MySQL 5.6 and MySQL 5.7. (Bug #17810862, Bug #70936)

- InnoDB: Due to a regression introduced by the fix for Bug#17371537, memory was not allocated for the

default memcached engine when using the default memcached engine as the backstore for data instead of `InnoDB`. (Bug #17800829)

## MySQL 5.6 Release Notes

- InnoDB: `InnoDB` would report an incorrect operating system error code after failing to initialize. (Bug

#17788055, Bug #70867)

- InnoDB: Manipulating a table after discarding its tablespace using `ALTER TABLE ... DISCARD`

`TABLESPACE` could result in a serious error. (Bug #17700280)

- InnoDB: Persistent optimizer statistics would cause stalls due to latch contention. (Bug #17699331, Bug

#70768)

- InnoDB: An `InnoDB` full-text search failure would occur due to an “unended” token. The string and string

length should be passed for string comparison. (Bug #17659310)

- InnoDB: `MATCH() AGAINST()` queries that use a long string as an argument for `AGAINST()` could

result in an error when run on an `InnoDB` table with a full-text search index. (Bug #17640261)

- InnoDB: In debug builds, a merge insert buffer during a page read would cause a memory access

violation. (Bug #17561188)

- InnoDB: In `sync0rw.ic`, `rw_lock_x_lock_func_nowait` would needlessly call

`os_thread_get_curr_id`. (Bug #17509710, Bug #70417)

- InnoDB: Truncating a `memcached` `InnoDB` table while `memcached` is performing DML operations would

result in a serious error. (Bug #17468031)

- InnoDB: The server could fail to restart if a crash occurred immediately following a `RENAME TABLE` in

an `ALTER TABLE`, `RENAME TABLE` sequence. (Bug #17463290)

- InnoDB: If a tablespace data file path is updated in a `.isl` file and then a crash recovery is performed,

the updated tablespace data file path is read from the `.isl` file but the `SYS_DATAFILES` table would not be not updated. The `SYS_DATAFILES` table is now updated with the new data file path after crash recovery. (Bug #17448389)

- InnoDB: Attempting to rename a table to a missing database would result in a serious error. (Bug

#17447500)

- InnoDB: If the first page (page 0) of file-per-table tablespace data file was corrupt, recovery would be

halted even though the doublewrite buffer contained a clean copy of the page. (Bug #17335427, Bug#70087, Bug #17341780)

- InnoDB: The `InnoDB` `memcached` Readme file (`README-innodb_memcached`) incorrectly stated that

libevent 1.6.0 is linked statically into daemon `memcached`. The bundled version of libevent is 1.4.12, not

1.6.0. (Bug #17324419, Bug #70034)

- InnoDB: The `ALTER TABLE` `INPLACE` algorithm failed to decrease the auto-increment value. (Bug

#17250787, Bug #69882)

- InnoDB: Comments in `btr0cur.cc` incorrectly stated that `btr_cur_pessimistic_update()` and

`btr_cur_optimistic_update()` would accept a NULL value. (Bug #17231743, Bug #69847)

- InnoDB: `dict_table_schema_check` would call `dtype_sql_name` needlessly. (Bug #17193801,

Bug #69802)

- InnoDB: The function `os_file_get_status` would not work with raw devices. (Bug #17023438, Bug

#69424)

- InnoDB: During crash recovery, an incorrect transaction active time would result in rolling back an

uncommitted transaction. (Bug #16936961, Bug #69438)

## MySQL 5.6 Release Notes

- InnoDB: Heap block debugging information (`file_name`, `lineno`), used for logging diagnostics, would

appear in release builds. This information should only appear in debug builds. (Bug #16924719, Bug#69422)

- InnoDB: An online `ALTER TABLE` operation would consume more memory than expected. During an

online `ALTER TABLE` operation, an online log buffer containing a head and tail buffer is created for each index that is created or rebuilt. The tail buffer is the writer context and is only required for concurrent write operations on an index while the `ALTER TABLE` operation is in progress. The head buffer is the reader context and is only required during the log apply phase. To reduce memory consumption, the tail buffer is now allocated when the first DML statement is run on the index, and the head buffer is only allocated in the log apply phase and freed afterwards. (Bug #16868967, Bug #69325, Bug #17911720)

- InnoDB: Renaming a column while also adding or dropping columns in the same `ALTER TABLE`

operation would cause an error. (Bug #16864981)

- InnoDB: On Windows, the full-text search (FTS) object ID was not in the expected hexadecimal format.

(Bug #16559254)References: See also: Bug #16559119.

- InnoDB: Fetching and releasing pages from the buffer pool and tracking the page state are expensive

and complex operations. Prior to the bug fix, these operations were performed using a page mutex.

Using a page mutex to track several things is expensive and does not scale well. The bug fix separates fetch and release tracking (in-use state) of a page from page I/O state tracking. Fetch and release is now tracked using atomics where available.

For portability, a new `CMake` build option, `INNODB_PAGE_ATOMIC_REF_COUNT` (default `ON`), can be used to disable atomic page reference counting on platforms where atomics support is not available.

When atomic page reference counting is enabled (default), “`[Note] InnoDB: Using atomics``to ref count buffer pool pages`” is printed to the error log at server startup. If atomic page reference counting is disabled, “`[Note] InnoDB: Using mutexes to ref count buffer pool``pages`” is printed instead. (Bug #16249481, Bug #68079)

- InnoDB: Table renaming errors would appear in the `LATEST FOREIGN KEY ERROR` section of the

`SHOW ENGINE INNODB STATUS` output. (Bug #12762390, Bug #61746)

- InnoDB: `UNIV_SYNC_DEBUG`, which was disabled in `univ.i` with the fix for Bug#16720368, is now

enabled. (Bug #69617, Bug #17033591)

- Partitioning: Queries using the `index_merge` optimization (see Index Merge Optimization) could return

invalid results when run against tables that were partitioned by `HASH`. (Bug #17588348, Bug #70588)References: See also: Bug #16862316, Bug #17648468, Bug #18167648.

- Partitioning: When no partition had returned a row since the last `HA_ERR_KEY_NOT_FOUND` error, the

use of uninitialized memory in the priority queue used for returning rows in sorted order could lead to a crash of the server. (Bug #17401628)

- Replication: When the binary log I/O cache grew to exactly 32768 bytes and the current transaction was

preceded by a transaction whose size was greater than 32768 bytes, events could be corrupted when written into the binary log. (Bug #17842137)

- Replication: Creating and dropping large numbers of temporary tables could lead to increased memory

consumption. (Bug #17806014)

- Replication: When `log_warnings` is greater than 1, the master prints binary log dump thread

information—containing the slave server ID, binary log file name, and binary log position—in

## MySQL 5.6 Release Notes

`mysqld.1.err`. A slave server ID greater than 2 billion was printed with a negative value in such cases.

(Bug #17641586, Bug #70685)

- Replication: `mysqlbinlog` `--verbose` failed when it encountered a corrupt row event in the binary

log. Such a row event could also cause the slave to fail. (Bug #17632978)References: See also: Bug #16960133.

- Replication: `mysqlbinlog` did not properly decode `DECIMAL` values in a row-based binary log. This

could cause invalid values to be printed out for `DECIMAL` columns. (Bug #17544169)References: See also: Bug #14309019.

- Replication: `Seconds_Behind_Master` in the output of `SHOW SLAVE STATUS` could under some

conditions be reported as 0 when it should have had a value greater than zero. (Bug #17233214)References: See also: Bug #16579028.

- Replication: Invalid event offsets in the binary log were not always handled correctly, which could lead

to replication failure. (Bug #16736412, Bug #69087)

- Replication: The semisynchronous replication plugin was called twice for a DDL statement,

incrementing `Rpl_semi_sync_master_yes_tx` by 2 instead of 1 each time such a statement was executed. (Bug #70410, Bug #17509011)

- Microsoft Windows: On Windows, the `--local-service` server option did not work, and was not

displayed in the `--help` message. (Bug #69637, Bug #17049656)

- `FORCE INDEX [FOR ORDER BY] (index_name)` did not work for joins.

The fix for this bug also changes the warning created for `EXPLAIN`. Instead of printing only `{IGNORE|``USE|FORCE} INDEX` it now also prints `FOR {GROUP BY|ORDER BY|JOIN}` if that was specified in the query. (Bug #17889511)

- With the compressed client/server protocol enabled, Performance Schema statement instrumentation

could raise an assertion. (Bug #17794846)

- An assertion could be raised if a `filesort` failed to resize its main buffer when record properties

changed. (Bug #17757914)

- In some cases, `UNIX_TIMESTAMP()` could return `NULL` when it should return 0. (Bug #17728371)
- The cache used for the Index Merge access method was freed only after successful retrieval of all rows.

Interruption or failure of the operation led to a file descriptor leak. (Bug #17708621)

- Using the `mysqldump` `--set-gtid-purged` option with no value caused `mysqldump` to crash. (Bug

#17650245)

- A race condition between Performance Schema statement event threads led to a server exit. (Bug

#17637970)

- In a view definition requireing resolution of aggregrate expressions within a subquery to an outer query,

selecting from the view could cause a server exit. (Bug #17547804)References: This issue is a regression of: Bug #16436383.

- An addressing error in accessing the join buffer could produce invalid results or a server exit. (Bug

#17513341)

## MySQL 5.6 Release Notes

- `mysql_config` incorrectly included some flags to generate compiler warning output. (Bug #17400967)
- With semijoin optimization enabled, queries with nested subqueries could cause a server exit due to

incorrect resolution of references to columns in the middle query block. (Bug #17398972)

- In some cases, the optimizer wrote fixed-length temporary `MyISAM` tables to disk rather than variable-

length temporary tables. (Bug #17231940)

- Enabling the `validate_password` plugin could result in incorrect password hashes being stored in the

`mysql.user` table. (Bug #17065383)

- For accounts authenticated using the `sha256_password` plugin, setting the password after the

password had been expired did not clear the password-expired flag. (Bug #16872181)

- On OS X 10.7, a race condition involving `vio_shutdown()` and the select-based implementation of

`vio_io_wait()` could cause a server exit. (Bug #16354789, Bug #17733393)

- Host names in example URLs used within the source code were replaced by names in the example.com

domain, the domain intended by IANA for this purpose. (Bug #15890092)

- For `utf8` and `utf8mb4` strings, handler functions unnecessarily called a Unicode conversion function.

(Bug #14057034)

- Several `-W` warning flags were turned off for compilation in maintainer mode if MySQL was configured

with `-DWITH_INNODB_MEMCACHED=1`. (Bug #13898319)

- Calling the `ExtractValue()` function with an invalid XPath expression could in some cases lead to a

failure of the server. (Bug #12428404, Bug #61065)

- Use of a nonmultibyte algorithm for skipping leading spaces in multibyte strings could cause a server

exit. (Bug #12368495, Bug #18315770)

- With `ONLY_FULL_GROUP_BY` SQL mode enabled, a query that uses `GROUP BY` on a column derived

from a subquery in the `FROM` clause failed with a `column isn't in GROUP BY` error, if the query was in a view. (Bug #11923239)

- `mysqldump --single-transaction` acquired metadata locks for each dumped table but did not

release them until the dump operation finished. Consequently, other DDL operations on a dumped table blocked even after the table itself had been dumped. `mysqldump` now attempts to release metadata locks earlier. (Bug #71017, Bug #17862905)

- `sql_resolver.cc` referred to partitioning code that should have been protected by an `#ifdef`, even

when MySQL was configured with `-DWITH_PARTITION_STORAGE_ENGINE=OFF`. (Bug #71010, Bug#17876794)

- Several issues identified by the Coverity static analysis tool were fixed. Thanks to Honza Horak for the

patch. (Bug #70830, Bug #17760511)

- The prototype of the Performance Schema instrumentation API `mysql_cond_timedwait()` call was

fixed to be drop-in compatible with `pthread_cond_timedwait()`. This fix affects only implementors of third-party plugins. (Bug #70628, Bug #17702677)

- An incorrect result could be returned for a query with an `IF()` predicate in the `WHERE` clause combined

with `OUTER JOIN` in a subquery that is transformed to a semijoin. (A workaround is to disable semijoin using `SET optimizer_switch='semijoin=off';`) (Bug #70608, Bug #17600176)

- Complex updates of Performance Schema tables involving joins or subqueries failed to update every

row. (Bug #70025, Bug #17309657)

## MySQL 5.6 Release Notes

- Some files in the `file_instances` Performance Schema table were not being removed because the

file-removal operation was not instrumented. (Bug #69782, Bug #17209750)

- For the path specified with the `--basedir` option, `mysql_plugin` attempted to unlink the path rather

than free the memory in which the path was stored. (Bug #69752, Bug #17168602)

- It was not possible to query a view with an `ORDER BY` clause that referenced an alias in the `SELECT`

clause of the view definition, unless all columns in the view were named in the select list.

To handle this problem, the server now writes a view differently into the `.frm` file that stores the view definition. If you experience view-evaluation errors such as just described, drop and recreate the view so that the `.frm` file contains the updated view representation. (Bug #69678, Bug #17077305)

- For the `utf8_bin` collation, `ORDER BY LOWER(col_name)` could produce incorrect ordering. (Bug

#69005, Bug #16691598)

- A full-text search combined with derived tables (subqueries in the `FROM` clause) caused a server exit.

Now if a full-text operation depends on a derived table, the server produces an error indicating that a full-text search cannot be done on a materialized table. (Bug #68751, Bug #16539903)

- COUNT(DISTINCT) sometimes produced an incorrect result when the last read row contained a `NULL`

value. (Bug #68749, Bug #16539979, Bug #71028, Bug #17867117)

- Some scripts displayed out-of-date information regarding where to report bugs. (Bug #68742, Bug

#16530527)

- Updating a `FEDERATED` table with `UPDATE... JOIN` caused a server exit when the local table

contained a single row and that row could be joined to a row in the `FEDERATED` table. (Bug #68354, Bug#16324629)

- The `make_atomic_cas_body64` implementation on IA32 with `gcc` but without `gcc` builtins could be

miscompiled due to an incorrect constraint. The patch also causes MySQL to use builtin atomics when compiled using `Clang`. (Bug #63451, Bug #17242996)

- `mysql_install_db` referred to the obsolete `mysqlbug` script for reporting problems. It now refers to

http://bugs.mysql.com/ instead. (Bug #29716, Bug #11746921)
