---
title: "Changes in MySQL 5.6.12 (2013-06-03, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=120"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Known limitations of this release:

## MySQL 5.6 Release Notes

Important`InnoDB` may fail to open a tablespace that has multiple data files due to newly introduced corruption checking functionality. It is recommended that you do not upgrade to this version if you have more than one file for your shared `InnoDB`tablespace. If you have upgraded to an affected version and the server no longer starts, you can upgrade to a later version when it becomes available or downgrade to an earlier version.

Note If you have `InnoDB` tables with full-text search indexes and you are upgrading from MySQL 5.6.10 to a MySQL version up to and including MySQL 5.6.18, the server will fail to start after the upgrade (Bug#72079). This bug is fixed in MySQL 5.6.19.

As a workaround, remove full-text search indexes prior to upgrading and rebuild full-text search indexes after the upgrade is completed.

- Functionality Added or Changed
- Bugs Fixed

> Functionality Added or Changed

- `mysql_upgrade` now verifies that the server version matches the version against which it was

compiled, and exits if there is a mismatch. In addiion, a `--version-check` option permits specifying whether to enable version checking (the default), or disable checking if given as `--skip-version-``checking`. (Bug #16500013)

> Bugs Fixed

- Incompatible Change: When used for an existing MySQL account, the `GRANT` statement could produce

unexpected results if it included an `IDENTIFIED WITH` clause that named an authentication plug differing from the plugin named in the corresponding `mysql.user` table row.

Because `IDENTIFIED WITH` is intended only for `GRANT` statements that create a new user, it is now prohibited if the named account already exists. (Bug #16083276)

- Important Change; Replication: When the server was running with `--binlog-ignore-db` and

`SELECT` `DATABASE()` returned `NULL` (that is, there was no currently selected database), statements using fully qualified table names in `dbname`.`tblname` format were not written to the binary log. This was because the lack of a currently selected database in such cases was treated as a match for any possible ignore option rather than for no such option; this meant that these statements were always ignored.

Now, if there is no current database, a statement using fully qualified table names is always written to the binary log. (Bug #11829838, Bug #60188)

- InnoDB; Partitioning: Joins involving partitioned `InnoDB` tables having one or more `BLOB` columns

were not always handled correctly. The `BLOB` column or columns were not required to be join columns,or otherwise to be named or referenced in the statement containing the join, for this issue to occur. (Bug#16367691)

- InnoDB: In debug builds, an online `ALTER TABLE` operation that performed a full table copy would

raise an assertion. The assertion was due to a race condition that would occur during BLOB retrieval,when applying the table modification log to any log block except for the very last one. This fix modifies`row_log_table_apply_convert_mrec()` to ensure that an index B-tree lock is acquired to protect the access to `log->blobs` and the BLOB page. (Bug #16774118)

## MySQL 5.6 Release Notes

- InnoDB: When the function `trx_rollback_or_clean_recovered()` rolls back or cleans

up transactions during a crash recovery, it removes the trx objects from the `trx_sys` list without freeing up the memory used by those objects. To prevent a memory leak, this fix adds`trx_free_for_background()` calls to `trx_rollback_resurrected()`, the function that removes the trx objects. (Bug #16754776)

- InnoDB: A memory leak would occur in `dict_check_tablespaces_and_store_max_id()` when

`space_id` is equal to zero. (Bug #16737332)

- InnoDB: A missing comma in `SHOW STATUS` output would break MySQL Enterprise Monitor parsing.

(Bug #16723686)

- InnoDB: After a clean shutdown, `InnoDB` does not check `.ibd` file headers at startup. As a result, in a

crash recovery scenario, `InnoDB` could load a corrupted tablespace file. This fix implements consistency and status checks to avoid loading corrupted files. (Bug #16720368)

- InnoDB: This fix addresses a race condition that would occur between the rollback of a recovered

transaction and creation of a secondary index in a locked operation. The race condition would corrupt the secondary index. (Bug #16593427)

- InnoDB: DML operations on compressed temporary tables would result in a Valgrind error in the buffer

manager stack. (Bug #16593331)

- InnoDB: For `ALTER TABLE` operations on `InnoDB` tables that required a table-copying operation,

other transactions on the table might fail during the copy. However, if such a transaction issued a partial rollback, the rollback was treated as a full rollback. (Bug #16544143)

- InnoDB: The `recv_writer` thread would only start after all redo log scans finished. In the case

of multiple redo log scans, accumulated redo records would be applied after each scan and before processing the next scan. The absence of the `recv_writer` thread to help with flushing would slow recovery or result in a server startup timeout. This fix ensures that the `recv_writer` thread starts before the first scan batch is processed. (Bug #16501172)

- InnoDB: Under certain circumstances, LRU flushing would take a long time possibly affecting all flushing

activity and causing a shutdown timeout. (Bug #16500209)

- InnoDB: The `InnoDB` memcached `test.demo_test` table failed to work when defined as a `utf8`

charset table. (Bug #16499038)

- InnoDB: In cases where threads are forced to do single page flushing, `fsync()` would be triggered for

all data files. This fix allows for synchronous single page flushing. (Bug #16477781)

- InnoDB: This fix removes most calls to `OS_THREAD_SLEEP` from InnoDB. (Bug #16472953, Bug

#68588)

- InnoDB: `FLUSH TABLES ... FOR EXPORT` slept too often while flushing pages from buffer pools.

(Bug #16471701)

- InnoDB: Concurrently inserting into a full-text table would cause some inserts to fail. Duplicate values

would be generated for full-text search document IDs when performing inserts into a hidden full-text search document ID column. (Bug #16469399)

- InnoDB: The `page_zip_available` function would count some fields twice. (Bug #16463505)
- InnoDB: This fix replaces the `IB_ULONGLONG_MAX` constant with `LSN_MAX` where the code refers to

log sequence numbers, or with `TRX_ID_MAX` where `trx->no` is initialized to an undefined value. This change does not alter the value of the constant. (Bug #16458660)

## MySQL 5.6 Release Notes

- InnoDB: This fix corrects the text for InnoDB error 6025, which stated, “InnoDB: read can't be opened

in ./ib_logfile0 mode.”. The corrected message states, “InnoDB: ./ib_logfile0 can't be opened in read mode.” The variable and mode in the message construct were transposed. (Bug #16434398)

- InnoDB: Creating a foreign key constraint using the `ALTER TABLE` `INPLACE` algorithm requires

`foreign_key_checks` to be set to 0 (`SET foreign_key_checks = 0;`). As a result, an appropriate duplicate ID check would not be performed. (Bug #16413976)

- InnoDB: In debug builds, an insert failed with an invalid assertion: `sync_thread_levels_g(array,`

`level - 1, TRUE)`. (Bug #16409715)

- InnoDB: Multiple concurrent calls to `dict_update_statistics()` would result in unnecessary server

load. (Bug #16400412)

- InnoDB: On 64-bit Windows builds, `INNODB_BUFFER_POOL_SIZE` would not accept an allocation of

more than 32GB. This limitation was due to a bug that truncated the internal value for the InnoDB buffer pool size to 32 bits on 64-bit Windows builds. (Bug #16391722, Bug #68470)

- InnoDB: `DROP DATABASE` failed if the database contained an InnoDB table that had a data file in an

external data directory. The external data file had an “InnoDB Symbolic Link” file type (`.isl`) that was not recognized by MySQL. This fix adds `.isl` as a known InnoDB file type. (Bug #16338667)

- InnoDB: `RENAME TABLE` would result in a hang due to a MySQL mutex acquisition deadlock. (Bug

#16305265)

- InnoDB: Under testing, a `FLUSH TABLES` operation resulted in a timeout due to a missing

acknowledgment that the purge thread had stopped. (Bug #16277387)

- InnoDB: For compressed tables, a page reorganize operation would always write

an `MLOG_ZIP_PAGE_REORGANIZE` record to the redo log, which is only correct if

```
innodb_log_compressed_pages=OFF. When innodb_log_compressed_pages=ON, the page
```

reorganize operation should log the compressed page image. (Bug #16267120)

- InnoDB: When tables are linked by foreign key constraints, loading one table would open other linked

tables recursively. When numerous tables are linked by foreign key constraints, this would sometimes lead to a thread stack overflow causing the server to exit. Tables linked by foreign key constraints are now loaded iteratively. Cascade operations, which were also performed in a recursive manner, are now performed iteratively using an explicit stack. (Bug #16244691, Bug #65384)

- InnoDB: After disabling foreign key checks with `SET` `foreign_key_checks=0` and performing a

`DROP INDEX`, the table was no longer accessible after restarting the server. This fix allows the table with missing foreign key indexes to be accessed when `SET foreign_key_checks=0`. When the table is accessible, the user must recreate the missing indexes to fulfill the foreign key constraints. (Bug#16208542, Bug #68148)

- InnoDB: When a transaction is in `READ COMMITTED` isolation level, gap locks are still taken in

the secondary index when a row is inserted. This occurs when the secondary index is scanned for duplicates. The function `row_ins_scan_sec_index_for_duplicate()` always calls the function `row_ins_set_shared_rec_lock()` with `LOCK_ORDINARY` irrespective of the transaction isolation level. This fix modifies the `row_ins_scan_sec_index_for_duplicate()` function to call`row_ins_set_shared_rec_lock()` with `LOCK_ORDINARY` or `LOCK_REC_NOT_GAP`, based on the transaction isolation level. (Bug #16133801, Bug #68021)

- InnoDB: Starting `mysqld` with `--innodb-log-buffer-size=50GB` failed to allocate memory and

returned NULL. For non-debug builds there was no check in place and a segmentation fault occurred.

This fix adds a log message stating that memory failed to be allocated, and adds an assertion. (Bug#16069598, Bug #68025)

## MySQL 5.6 Release Notes

- InnoDB: When `UNIV_DEBUG` is enabled in debug builds, `buf_validate()` is often called which

sometimes results in false alarms in tests on semaphore wait timeout. This fix increases counter values to reduce false alarms. (Bug #16068056)

- InnoDB: The `explain_filename` function, which provides information about a partition by parsing the

file name, would return an error when attempting to parse a file name with no partition information. (Bug#16051728)

- InnoDB: Stopping the server, removing a database table (d1.t1) `.frm` file from the data directory,

restarting the server, and dropping the database (d1), would cause an assertion. (Bug #16043216)

- InnoDB: While processing read-write workloads, InnoDB would scan more pages than are required for

flushing, unnecessarily consuming CPU resource. (Bug #16037180)

- InnoDB: An active `FLUSH TABLES ... FOR EXPORT` thread would cause a hang during shutdown.

The fix ensures that `trx_is_interrupted()` is checked during `ibuf_merge`. (Bug #15953255)

- InnoDB: A multi-row `INSERT ... ON DUPLICATE KEY UPDATE` insert failure, caused by a duplicate

key error, would result in duplicate auto-increment values. (Bug #14483484, Bug #66301)

- Replication: Issuing a `FLUSH TABLES` statement on a GTID-enabled master caused replication to

fail. It was found that this misbehavior was introduced by the fix for Bug #16062608, which disallowed statements that perform an implicit commit but whose changes are not logged when `gtid_next` is set to any value other than `AUTOMATIC`. The changes made in that fix have been reverted, and such statements are (again) allowed without regard to the value of this variable. (Bug #16715809, Bug#69045)References: Reverted patches: Bug #16062608.

- Replication: Point-in-time recovery could fail when trying to restore a single database from a binary log

in row-based format using `mysqlbinlog` with the `--database` option. (Bug #16698172)

- Replication: A crash-on-commit error caused `InnoDB` to lose the previous transaction following

execution of a `RESET MASTER` statement. This occurred because the prepare phase caused a flush to disk, while the commit phase did not perform a corresponding flush within `InnoDB`.

To fix this problem, `RESET MASTER` now causes storage engine logs to be flushed on commit. (Bug#16666456, Bug #68932)

- Replication: When processing an `Update_rows_log_event` or `Delete_rows_log_event` from

the binary log, the before image is hashed and stored in a hash table. Following this, the original table is scanned for the desired records; subsequent processing hashes each record fetched from the original table and performs a lookup for it in the hash table. However, columns read from the image that had originally been set to `NULL` could instead contain random or “garbage” data, causing the lookup(and thus replication) to fail with an error such as `Could not execute Update_rows event on``table...`. (Bug #16621923)References: See also: Bug #11766865. This issue is a regression of: Bug #16566658.

- Replication: When used with the options `--dump-slave` `--include-master-host-port`,

`mysqldump` printed the port number within quotation marks, as if it were a string value rather than an integer. (Bug #16615117)

- Replication: Due to time resolution issues on some systems, the time to be taken by the dump

thread for a reply from the slave could be calculated to be less than zero, leading to `Semi-sync``master wait for reply fail to get wait time` errors. Since this condition does not have a negative impact on replication, errors caused by these conditions have been reduced to warnings. (Bug#16579028)

## MySQL 5.6 Release Notes

- Replication: Trying to update a column, previously set to `NULL`, of a table with no primary key caused

replication to fail with `Can't find record in 'table'...`.

This issue was originally fixed in MySQL 5.6.3 but was inadvertently reintroduced in MySQL 5.6.6. (Bug#16566658)References: See also: Bug #16621923. This issue is a regression of: Bug #11766865.

- Replication: Running the server with `--log-slave-updates` together with `--replicate-wild-`

`ignore-table` or `--replicate-ignore-table` in some cases caused updates to user variables not to be logged. (Bug #16541422)

- Replication: When using `mysqlbinlog` and the `mysql` client to roll forward two or more binary logs on

a server having GTIDs enabled, the `gtid_next` variable was not properly reset when switching from the first to the second binary log, causing processing to halt with an error at that point. (Bug #16532543)

- Replication: The `mysqlbinlog` options `--include-gtids`, `--exclude-gtids`, and `--skip-`

`gtids` did not work correctly when trying to process multiple files. (Bug #16517775)

- Replication: When one or more GTID log events but no previous GTIDs log events were found in the

binary log, the resulting error was mishandled and led to a failure of the server. (This is an extremely rare condition that should never occur under normal circumstances, and likely indicates that the binary log file has somehow been corrupted.) Now in such cases, an appropriate error is issued, and is handled correctly. (Bug #16502579, Bug #68638)

- Replication: Attempting to execute `START SLAVE` after importing new `slave_master_info` and

`slave_relay_log_info` tables failed with an empty error message. Now an appropriate error and message are issued in such cases. (Bug #16475866, Bug #68605)

- Replication: Restarting the server after the `slave_relay_log_info` table had been emptied caused

`mysqld` to fail while trying to return an error. (Bug #16460978, Bug #68604)

- Replication: Extra binary log rotations were performed due to concurrent attempts at rotation when the

binary log became full, which were allowed to succeed. This could lead to the unnecessary creation of many small binary log files. (Bug #16443676, Bug #68575)

- Replication: When the size of an execution event exceeded the maximum set for the buffer

(`slave_pending_jobs_size_max`), row-based replication could hang with `Waiting for slave``workers to free pending events`. (Bug #16439245, Bug #68462)

- Replication: Following disconnection from the master, the slave could under certain conditions

report erroneously on reconnection that it had received a packet that was larger than`slave_max_allowed_packet`, causing replication to fail. (Bug #16438800, Bug #68490)

- Replication: An SQL thread error during MTS slave recovery caused the slave to fail. (Bug #16407467,

Bug #68506)

- Replication: When using the options `--read-from-remote-server` `--stop-never` `--base64-`

`output=decode-rows` `--verbose`, `mysqlbinlog` failed to reset the counter used to store the current position within the file when the binary log on the server was rotated. (Bug #16316123, Bug #68347)

- Replication: When using `mysqldump` to back up a database created with MySQL 5.6.4 or an earlier

version, setting `--set-gtid-purged=AUTO` caused the backup to fail, because pre-5.6.5 versions of MySQL did not support GTIDs, and it could not be determined if GTIDs were enabled for the database.

This fix makes sure `mysqldump` does not attempt to output a `SET @@GLOBAL.gtid_purged` statement when backing up any pre-5.6.5 databases. (Bug #16303363, Bug #68314)

## MySQL 5.6 Release Notes

- Replication: Deadlocks could sometimes occur on group commits with a high number of concurrent

updates, as well as when one client held a lock from a commit while another client imposed a lock while rotating the binary log. (Bug #16271657, Bug #16491597, Bug #68251, Bug #68569)

- Replication: When semisynchronous replication was enabled, the automatic dropping on the master of

an event created using `ON COMPLETION NOT PRESERVE` caused the master to fail. (Bug #15948818,Bug #67276)

- Replication: Setting a `SET` column to `NULL` inside a stored procedure caused replication to fail. (Bug

#14593883, Bug #66637)

- Replication: The binary log contents got corrupted sometimes, because the function

`MYSQL_BIN_LOG::write_cache` always thought it had reached the end-of-cache when the function`my_b_fill()` reported a '0,' while that could also mean an error had occurred. This fix makes sure that whenever `my_b_fill()` returns a '0,' an error check is performed on `info->error`. (Bug #14324766,Bug #60173)

- Replication: `PURGE BINARY LOGS` by design does not remove binary log files that are in use or active,

but did not provide any notice when this occurred. Now, when log files are not removed under such conditions, a warning is issued; this warning includes information about the file or files were not removed when the statement was issued. (Bug #13727933, Bug #63138)

- Replication: When replicating to a `BLACKHOLE` table using the binary logging format, updates and

deletes cannot be applied and so are skipped. Now a warning is generated for this whenever it occurs.

Note`binlog_format=STATEMENT` is recommended when replicating to tables that use the `BLACKHOLE` storage engine.

(Bug #13004581)

- Removing a server RPM package did not shut down the existing server if it was running. (Bug

#16798868)

- Overhead for setting `PROCESSLIST_STATE` values in the `THREADS` Performance Schema table has

been reduced. (Bug #16633515)

- The Windows authentication plugin failed to free a context buffer for each connection. (Bug #16591288)
- The `DBUG_PRINT()` macro unnecessarily evaluated arguments when debugging was not enabled. (Bug

#16556597)

- Geometry methods that worked with WKB data performed insufficient input data validation, which could

cause Valgrind errors or a server exit. (Bug #16510712, Bug #12772601)

- The server could attempt a `filesort` operation for a zero-size sort length, causing it to exit. (Bug

#16503160)

- Opening a cursor on a `SELECT` within a stored procedure could cause a segmentation fault. (Bug

#16499751)References: This issue is a regression of: Bug #14740889.

- `my_load_defaults()` was modified to accommodate some problems under compilation with `gcc`

4.7.2 that could cause a client crash during option processing. (Bug #16497125)

- `SET PASSWORD` treated `user@'%'` and `user@''` as referring to the same `mysql.user` table row. (Bug

#16488043)

## MySQL 5.6 Release Notes

- When index condition pushdown was used on a descending range scan and the first range interval

did not contain any qualifying records, the result of the range scan could be empty even if other range intervals contained qualifying records. (Bug #16483273)

- The WKB reader for spatial operations could fail and cause a server exit. (Bug #16451878)
- Optimizer heuristics inappropriately preferred range access over `ref` access in cases when the `ref`

access referred to a column of a table earlier in the join seqence. (Bug #16437940)

- Performance Schema parameter autosizing at startup did not take into account later autosizing changes

to other startup parameters on which the Performance Schema parameters depended. (Bug #16430532)

- Some `INFORMATION_SCHEMA` queries that used `ORDER BY` did not use a `filesort` optimization as

they did in MySQL 5.5. (Bug #16423536)

- Manually-created accounts (using `INSERT`) with a malformed password effectively had no password.

(Bug #16414396)

- For debug builds, `DBUG_EXPLAIN` resulted in a buffer overflow when the `debug` system variable value

was more than 255 characters. (Bug #16402143)

- Several scripts in the `sql-bench` directory that were supposed to be executable did not have the

executable access bit set. (Bug #16395606)

- For debug builds, with an XA transaction in IDLE or PREPARED status, execution of a query with the

query cache enabled could cause a server exit. (Bug #16388996)

- Installing Debian packages on Ubuntu 12.10 succeeded using `dpkg`, but not with Software Center

5.4.1.4. (Bug #16387513)

- Within an XA transaction in ACTIVE state, statements causing an implicit commit could result in

metadata locks being released too early. (Bug #16362832)

- For debug builds, `GROUP_CONCAT(... ORDER BY)` within an `ORDER BY` clause could cause a server

exit. (Bug #16347426)

- A `GROUP_CONCAT()` invocation containing subquery having an outer reference caused the server to

exit. (Bug #16347343)

- The `validate_password` plugin did not always enforce appropriate constraints against assigning

empty passwords. (Bug #16346443)

- Re-execution of a stored procedure could cause a server exit in `Item_field::fix_outer_field`.

(Bug #16317443)

- For debug builds, the server could exit for queries involving a nested subquery, a subquery transformed

into a semijoin and using a view. (Bug #16317076)

- `thread_pool_high_priority_connection` could not be set at server startup. (Bug #16310373)
- With `secure_auth` enabled, a user with a password that used the pre-4.1 (old) hashing could not

update it to use the 4.1 (new) hashing. (Bug #16304018)

- The range optimizer could set up incorrect ranges for queries that used `XOR` operations. (Bug

#16272562)

- `mysql_secure_installation` could not connect to the server if the account used had an

expired password. It invoked `mysql` noninteractively, resulting in that program failing to connect.

Now `mysql` supports a `--connect-expired-password` option that indicates to the server that

## MySQL 5.6 Release Notes

it can handle sandbox mode for expired-password accounts even if invoked noninteractively, and`mysql_secure_installation` invokes `mysql` with this option. (Bug #16248315)

- If Loose Index Scan was used on a query that used `MIN()`, a segmentation fault could occur. (Bug

#16222245)

- An outer join between a regular table and a derived table that is implicitly groups could cause a server

exit. (Bug #16177639)

- If multiple statements were sent in a single request, the audit log plugin logged only the last one. Now it

logs each statement separately. (Bug #16169063)

- For debug builds, an assertion was incorrectly raised for queries executed using `eq_ref` access and

`filesort`. (Bug #16164885)

- A prepared statement that used `GROUP_CONCAT()` and an `ORDER BY` clause that named multiple

columns could cause the server to exit. (Bug #16075310)

- `ORDER BY MATCH ... AGAINST` could cause a server exit. (Bug #16073689)
- Creating a `FEDERATED` table without specifying a connection string caused a server exit. (Bug

#16048546)

- Client programs from MySQL 5.6.4 and up could confuse older servers during the connection process by

using newer protocol features not understood by older servers. (Bug #15965409)

- The `mysql.server` script exited with an error if the `status` command was executed with multiple

servers running. (Bug #15852074)

- In some cases, `REVOKE` could fail to revoke the `GRANT OPTION` privilege. (Bug #14799187)
- Use of the `VALUES()` function in the `VALUES()` clause of an `INSERT` statement could result in Valgrind

warnings or an unstable server, possibly leading to a server exit. (Bug #14789787)

- The `mysql` client allocated but did not free a string after reading each line in interactive mode, resulting

in a memory leak. (Bug #14685362)

- Killing a connection while it was in the process of disconnecting could lead to an assertion being raised,

Valgrind warnings, and general unstability. (Bug #14560522)

- `INSERT ... ON DUPLICATE KEY UPDATE` on a view could cause a server exit. (Bug #14261010)
- Grouping by an outer `BLOB` column in a subquery caused a server exit. (Bug #13966809, Bug

#14700180)

- The server could exit due to improper handling of the error from an invalid comparison. (Bug #13009341)
- The `CMake` check for `unsigned time_t` failed on all platforms. (Bug #11766815)
- `mysqladmin debug` causes the server to write debug information to the error log. On systems that

supported `mallinfo()`, the memory-status part of this output was incorrect in 64-bit environments when `mysqld` consumed more than 4GB memory.

Now the server uses `malloc_info()` to obtain memory-status information. `malloc_info()` does not report the memory that the `glibc` `malloc()` implementation internally allocates using `mmap()`.

However, it does provide the memory usage information in all the memory arenas.

This bug fix also involves a change of output format. The server now writes memory information in XML format rather than as plain text. Example:

## MySQL 5.6 Release Notes

```
Memory status:
<malloc version="1">
<heap nr="0">
<sizes>
<size from="33" to="33" total="1056" count="32"/>
<size from="65" to="65" total="65" count="1"/>
<size from="113" to="113" total="226" count="2"/>
<size from="129" to="129" total="2451" count="19"/>
<size from="145" to="145" total="290" count="2"/>
<size from="161" to="161" total="1288" count="8"/>
<size from="209" to="209" total="418" count="2"/>
</sizes>
<total type="fast" count="0" size="0"/>
<total type="rest" count="66" size="5794"/>
<system type="current" size="10833920"/>
<system type="max" size="10833920"/>
<aspace type="total" size="10833920"/>
<aspace type="mprotect" size="10833920"/>
</heap>
<total type="fast" count="0" size="0"/>
<total type="rest" count="66" size="5794"/>
<system type="current" size="10833920"/>
<system type="max" size="10833920"/>
<aspace type="total" size="10833920"/>
<aspace type="mprotect" size="10833920"/>
</malloc>
```

(Bug #11746658)

- Queries against a view that was created using a `CASE` operator and a `HAVING` clause were incorrectly

rejected with `ER_VIEW_INVALID` (Error 1356). (Bug #69774, Bug #17183462)

- `FOUND_ROWS()` could return an incorrect value if the preceding query used `filesort`. (Bug #69119,

Bug #16760474)References: This issue is a regression of: Bug #68458.

- The optimizer could choose a poor execution plan for queries with `ORDER BY ... LIMIT`. (Bug

#69013, Bug #16697792)

- When specified in an option file, the `plugin-dir` client option was ignored. (Bug #68800, Bug

#16680313)

- When only counting events but not timing them, Performance Schema would report `MIN_TIMER_WAIT`

values as a large number instead of 0. (Bug #68768, Bug #16552425)

- Using range access with an index prefix could produce incorrect results. (Bug #68750, Bug #16540042)
- For debug builds, metadata locking for `CREATE TABLE ... SELECT` could raise an assertion. (Bug

#68695, Bug #16503173)

- `mysqld` `--help` and `mysqld` `--verbose` `--help` performed unnecessary logging. (Bug #68578, Bug

#16442113)

- A new `CMake` option, `WITH_EDITLINE`, is provided to indicate whether to use the bundled or system

`libedit`/`editline` library. The permitted values are `bundled` (the default) and `system`.

`WITH_EDITLINE` replaces `WITH_LIBEDIT`, which has been removed. (Bug #68558, Bug #16430208)

- If Loose Index Scan was used to evaluate a query that compared an integer column to an integer

specified as a quoted string (for example, `col_name = '1'`), the query could return incorrect results.

(Bug #68473, Bug #16394084)

## MySQL 5.6 Release Notes

- In a MySQL server newer than MySQL 5.5 using a nonupgraded `mysql.user` table (for which

`mysql_upgrade` had not been run), statements to set passwords caused a server exit due to a faulty check for the `password_expired` column. (Bug #68385, Bug #16339767)

- Indexes on derived tables that were used during the first invocation of a stored procedure were not used

in subsequent invocations. (Bug #68350, Bug #16346367)

- If a function such as `AES_DECRYPT()` that requires SSL support failed, the error could affect later calls

to functions that require SSL support. (Bug #68340, Bug #16315767)

- For `DELETE` and `UPDATE` statements, `EXPLAIN` displayed `NULL` in the `ref` column for some cases

where `const` is more appropriate. (Bug #68299, Bug #16296268)

- The `mysql` client incorrectly used `latin1` for certain comparisons even if started with a multibyte

default character set, resulting in a client crash. (Bug #68107, Bug #16182919)

- `InnoDB` does not support full-text parser plugins, but failed to report an error if they were specified. Now

an `ER_INNODB_NO_FT_USES_PARSER` error is returned. (Bug #62004, Bug #12843070)

- The `url` columns in the `mysql` datatbase help tables were too short to hold some of the URLs in

the help content. These columns are now created as type `TEXT` to accommodate longer URLs. (Bug#61520, Bug #12671635)

- Two problems adding or subtracting keyword from the current `debug` system variable setting were

corrected:

- A `debug` value of `'d'` means “all debug macros enabled”. The following sequence left the value in an

incorrect state:

```
mysql> SET debug = 'd';SELECT @@debug;
+---------+
| @@debug |
+---------+
| d       |
+---------+
mysql> SET debug = '+d,M1';SELECT @@debug;
+---------+
| @@debug |
+---------+
| d,M1    |
+---------+
```

The first `SET` statement enables all debug macros. The second `SET` should add the `M1` macro to the current set, which should result in no change because the current set is already “all macros”. Instead,the second `SET` reset the current set to only the `M1` macro, effectively disabling all others. The server now correctly leaves `debug` set to `'d'`.

- A `debug` value of `''` means “no debug macros enabled”. The following sequence left the value in an

incorrect state:

```
mysql> SET debug = 'd,M1';SELECT @@debug;
+---------+
| @@debug |
+---------+
| d,M1    |
+---------+
mysql> SET debug = '-d,M1';SELECT @@debug;
```

## MySQL 5.6 Release Notes

```
+---------+
| @@debug |
+---------+
| d       |
+---------+
```

The first `SET` statement sets `debug` to the `M1*` macro. The second `SET` should subtract the `M1` macro from the current set, leaving no debug macros enabled. Instead, the second `SET` reset the current set to `'d'` (all macros enabled). The server now correctly sets `debug` to `''`.

(Bug #58630, Bug #11765644)

- It is now possible to suppress installation of the `mysql-test` directory after compiling MySQL from

source by invoking `CMake` with the `INSTALL_MYSQLTESTDIR` option explicitly set to empty:

```
cmake . -DINSTALL_MYSQLTESTDIR=
```

Previously, attempts to do this resulted in an error. (Bug #58615, Bug #11765629)

- On 64-bit OS X systems, `CMake` used `x86` rather than `x86_64` when determining the machine type.

(Bug #58462, Bug #11765489)

- `IF()` function evaluations could produce different results when executed in a prepared versus

nonprepared statement. (Bug #45370, Bug #11753852)
