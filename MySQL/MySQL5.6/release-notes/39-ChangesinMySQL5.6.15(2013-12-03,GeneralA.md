---
title: "Changes in MySQL 5.6.15 (2013-12-03, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=98"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

A known limitation of this release:Note If you have `InnoDB` tables with full-text search indexes and you are upgrading from MySQL 5.6.10 to a MySQL version up to and including MySQL 5.6.18, the server will fail to start after the upgrade (Bug#72079). This bug is fixed in MySQL 5.6.19.

As a workaround, remove full-text search indexes prior to upgrading and rebuild full-text search indexes after the upgrade is completed.

- Packaging Notes
- Functionality Added or Changed
- Bugs Fixed

## MySQL 5.6 Release Notes

> Packaging Notes

- Previously, MySQL Server distributions included the MySQL Reference Manual in Info format (the Docs/

mysql.info file). Because the license for the manual restricts redistribution, its inclusion in Community packages caused problems for downstream redistributors, such as those who create Linux distributions.

Community distributions of MySQL Server no longer include the mysql.info file, to make the repackaging and redistribution process easier (for example, the source tarball and its checksum can be used directly).

This change applies to all source and binary Community packaging formats. Commercial (Enterprise)distributions are unchanged.

For those who wish to continue using the MySQL Reference Manual in Info format, we have made it available at https://dev.mysql.com/doc/.

> Functionality Added or Changed

- Incompatible Change: Several statement instruments in the `setup_instruments` table are used by

the Performance Schema during the early stages of statement classification before the exact statement type is known. These instruments were renamed to more clearly reflect their “abstract” nature:Old Instrument Name New Instrument Name

```
statement/com/  statement/abstract/new_packet
statement/com/Query  statement/abstract/Query
statement/rpl/relay_log  statement/abstract/relay_log
```

In addition, statistics for abstract instruments are no longer collected in the following tables, because no such instrument is ever used as the final classification for a statement:

```
events_statements_summary_by_thread_by_event_name
events_statements_summary_by_account_by_event_name
events_statements_summary_by_user_by_event_name
events_statements_summary_by_host_by_event_name
events_statements_summary_global_by_event_name
```

Applications that refer to the old instrument names must be updated with the new names. For more information about the use of abstract instruments in statement classification, see Performance Schema Statement Event Tables. (Bug #16750433, Bug #17271055)

- The Performance Schema now instruments the read/write lock `Delegate::lock`, which is used for the

following classes:

```
Trans_delegate
Binlog_storage_delegate
Binlog_transmit_delegate
Binlog_relay_IO_delegate
```

A different instrument name is used for each subclass, to have distinct statistics for distinct uses. The instruments are visible in the `schema.setup_instruments` table and have these names:

```
wait/synch/rwlock/sql/Trans_delegate::lock
wait/synch/rwlock/sql/Binlog_storage_delegate::lock
wait/synch/rwlock/sql/Binlog_transmit_delegate::lock
wait/synch/rwlock/sql/Binlog_relay_IO_delegate::lock
```

(Bug #17590161, Bug #70577)

- A new `CMake` option, `WITH_ASAN`, permits enabling AddressSanitizer for compilers that support it. (Bug

#17435338)

## MySQL 5.6 Release Notes

- The hash function used for metadata locking was modified to reduce overhead. (Bug #68487, Bug

#16396598)

> Bugs Fixed

- InnoDB; Replication: The `InnoDB` `mecached` plugin would update a record before inserting to the

binary log, which would cause slave server replication to stop. The insert should occur before the update. (Bug #17358875)

- InnoDB: A regression introduced by the fix for Bug#17371537 resulted a memory leak for `memcached`

insert operations. (Bug #17738935)References: See also: Bug #17371537.

- InnoDB: Fault-tolerant code found in the log apply code for `InnoDB` `ALTER TABLE ... IN PLACE`

could result in data corruption. (Bug #17625063, Bug #17512497)

- InnoDB: The `trx->error_key_num` field was not initialized in the error injection code found in

`storage/innobase/handler/handler0alter.cc`. The `error_key_num` field is usually 0 but can be a non zero value if the memory buffer of a DDL transaction object is reused. (Bug #17624926)

- InnoDB: Databases names beginning with a digit would cause a full-text search (FTS) parser error. (Bug

#17607956)References: See also: Bug #17161372.

- InnoDB: An `ALTER TABLE ... CHANGE [COLUMN]` operation would result in an

`rbt_empty(index_cache->words)` assertion. (Bug #17536995)

- InnoDB: `CHECK TABLE` would ignore the `QUICK` option. (Bug #17513737)
- InnoDB: An excessive amount of memory would be consumed when querying

`INFORMATION_SCHEMA.INNODB_FT_INDEX_TABLE`. The problem would occur for very large full-text search indexes. (Bug #17483582, Bug #70329)

- InnoDB: Running `SHOW ENGINE INNODB STATUS` on one connection thread and killing that thread

by running a `KILL CONNECTION` statement from a different connection thread would result in a severe error. (Bug #17474166)

- InnoDB: In debug builds, test case failures would occur due to `ibuf_contract_ext` performing

merges and `dict_stats_update` returning evicted pages back into the buffer pool while`ibuf_change_buffering_debug` is enabled. (Bug #17446090)

- InnoDB: Setting the `O_DIRECT` flag on a file on `tmpfs` on some operating systems would result in an

error printed to the error log. Creating multiple temporary tables on `tmpfs` would cause the error to be printed repeatedly. The error message has been changed to a warning that is only printed once when running `CREATE TABLE` multiple times. (Bug #17441867)

- InnoDB: `InnoDB` failed to return an error when attempting to run a query after discarding the

tablespace. (Bug #17431533)

- InnoDB: A severe error would occur after discarding a tablespace. (Bug #17430207)
- InnoDB: The `information_schema.innodb_metrics` `index_merge` counter was not incremented

in `btr0btr.cc`. This patch also introduces new counters (`index_page_reorg_attempts`,`index_page_reorg_successful` and `index_page_discards`) and renames the`index_merges` counter to `index_page_merge_attempts` to distinguish it from the`index_page_merge_successful` counter. (Bug #17409657, Bug #70241)

## MySQL 5.6 Release Notes

- InnoDB: During a `TRUNCATE TABLE` operation, `InnoDB: Trying to TRUNCATE a missing`

`index of table ...` warnings would be printed to the error log. These warnings should not be printed when the index is a full-text search (FTS) index. (Bug #17402002, Bug #70226)References: See also: Bug #12429565.

- InnoDB: During parallel full-text search (FTS) index creation, a scanner thread reads in documents

and passes them to the tokenizer. The tokenizer frees documents from memory when tokenization is complete. When tokenizing documents with a large amount of text, the tokenizer thread would not keep pace with the scanner thread. As a result, memory would not be freed fast enough and the “tokenization pending list” would grow in size. (Bug #17384979)

- InnoDB: `trx_create` and `trx_free` would be called for every `memcached` `get` request. (Bug

#17371537, Bug #70172)

- InnoDB: A full-text search (FTS) `BOOLEAN MODE` query with an invalid character in the query string

could result in a memory access violation failure. (Bug #17350055)

- InnoDB: Full-text index creation on a large table failed due to insufficient temporary table space and

result in a misleading “incorrect key file” error. (Bug #17339606)

- InnoDB: In `btr_validate_level` there are checks to ensure that all B-tree pages are marked when

allocated. The checks failed on the change buffer because the allocation of change buffer pages is handled differently than other B-tree pages. (Bug #16884217)

- InnoDB: The hardcoded size for the `srv_max_n_threads` variable was insufficient. The variable

setting is now configured based on the maximum number of connection threads and `InnoDB`background threads. (Bug #16884077)

- InnoDB: A `SELECT COUNT(*)` query would take a long time to complete when run concurrently with

a `LOAD DATA` operation. The `mtr_memo_contains` function, which determines if an object is part of a memo in a mini transaction, contained a nested loop that caused the query to run slowly. (Bug#16764240, Bug #69141)

- InnoDB: When the change buffer is enabled, `InnoDB` failed to write a transaction log record when

merging a record from the insert buffer to a secondary index page if the insert was performed as an“update-in-place”. (Bug #16752251, Bug #69122)

- InnoDB: An existing full-text index would become invalid after running `ALTER TABLE ADD FULLTEXT`

due to an unsynchronized full-text cache. (Bug #16662990, Bug #17373659)

- InnoDB: Due to a regression in MySQL 5.6, creating or dropping tables with

`innodb_force_recovery` set to 3 (`SRV_FORCE_NO_TRX_UNDO`) failed. Additionally, this bug fix includes a code modification that sets `InnoDB` to read-only when `innodb_force_recovery` is set to a value greater than 3 (`SRV_FORCE_NO_TRX_UNDO`). (Bug #16631778, Bug #69892)

- InnoDB: An `InnoDB` `memcached` configuration error message contained an incorrect file name.

The error message stated, `Please create config table containers in database``innodb_memcache by running innodb_config.sql. error 31`. The correct file name is `innodb_memcached_config.sql`. Also, the “error 31” portion of the error message has been translated to its text equivalent, which is “Table not found”. (Bug #16498810, Bug #68684)

- InnoDB: In `mutex_spin_wait()`, the `sync_array_reserve_cell` function could fail to find an

empty slot on systems with sync wait arrays that are small in size, resulting in an error. (Bug #16245498)

- InnoDB: Full-text search (FTS) index savepoint information would not be set resulting in a severe error

when attempting to rollback to the savepoint. (Bug #14639605, Bug #17456092)

## MySQL 5.6 Release Notes

- InnoDB: When `index_read_map` is called for an exact search and fails to return a record due to non-

matching search criteria, the cursor would be positioned on the next record after the searched key. A subsequent call to `index_next` would return the next record instead of returning the previous non-matching row, thereby skipping a record. (Bug #14621190, Bug #15965874, Bug #17314241, Bug#70038, Bug #17413093, Bug #12860669, Bug #60220, Bug #17565888)

- InnoDB: An implicit rollback caused the server to halt when restarting with an

`innodb_force_recovery` value of 3 or greater. This bug was addressed by the combination of fixes for Bug #16310467 and Bug #17253499. (Bug #14178835)References: See also: Bug #16310467, Bug #17253499.

- InnoDB: Converting a table with a large number of columns from `MyISAM` to `InnoDB` would cause an

assertion due to insufficient log buffer space. Instead of asserting, `InnoDB` now attempts to increase log buffer size automatically if the redo log size is too large. (Bug #11758196, Bug #50366)

- Partitioning: The storage engine was set incorrectly during a rebuild of a partition; the table storage

engine was ignored and the default storage engine used instead. Thus, in MySQL 5.1, it was possible for `REBUILD PARTITION` to change the partition storage engine from `InnoDB` to `MyISAM`, and for the reverse (rebuilding partitions of `MyISAM` tables causing the partitions to use `InnoDB`) to occurin MySQL

5.5 and later. Now, when rebuilding partitions, the storage engine actually used by the table is checked and used by the handler for the rebuild operation, so that the partition storage engine is not inadvertently changed. (Bug #17559867)

- Partitioning: After disabling the parent table's indexes with `ALTER TABLE ... DISABLE KEYS`,

rebuilding any of its partitions enabled the indexes on those partitions, leading `MyISAM` to fail with an error when the optimizer tried to use one of the affected indexes.

Now in such cases, we check for disabled indexes on the table before rebuilding any of its partitions.

If the indexes have been disabled, then we disable them on the partition following the rebuild. (Bug#16051817)

- Replication: A replication master did not handle correctly the disabling of the semisync plugin on the

master and the slave, with a subsequent stopping of the slave. (Bug #17460821, Bug #70349)

- Replication: The final argument in the `SET` clause of a `LOAD DATA ... SET` statement was repeated

in the binary log. (Bug #17429677, Bug #70277)

- Replication: When an error encountered by the dump thread while reading events from the active binary

log file was a temporary error, so that the dump thread tried to read the event, it was possible for the dump thread to seek the wrong position, which could cause one or more events to be resent. To prevent this, the thread's position is obtained after each correct read of an event.

In addition, with this fix, only binary logs that are not closed normally are marked as possibly being corrupted.

Finally, two warnings are added; these are now returned when a dump thread encounters a temporary error. (Bug #17402313)

- Replication: Setting `rpl_semi_sync_master_enabled` while the master was waiting for a reply from

the slave could in some cases cause the master to fail. (Bug #17327454, Bug #70045)

- Replication: When stopping the I/O thread, it was possible with a very large transaction (equivalent to

a binary log size greater than 100MB) that the thread did not receive the transaction to the end. When reconnecting with `MASTER_AUTO_POSITION=1` it then tried to fetch changes from the next transaction,which could lead to loss of the incomplete transaction and its data. (Bug #17280176, Bug #69943)

## MySQL 5.6 Release Notes

- Replication: Trying to set `CHANGE MASTER TO ... MASTER_AUTO_POSITION = 0` failed with error

1777 (`ER_AUTO_POSITION_REQUIRES_GTID_MODE_ON`). (Bug #17277744)

- Replication: The value of `LAST_INSERT_ID()` was not correctly replicated when filtering rules were

used on the slave. (Bug #17234370, Bug #69861)

- Replication: An internal function used for storing GTID values could sometimes try to handle them as

strings of the wrong length. (Bug #17032712, Bug #69618)

- Replication: During row-based replication with `binlog_row_image` set to `MINIMAL`, updating only

some columns of a table having 9 or more columns caused `mysqlbinlog` to fail when it was used with the `--verbose` option. (Bug #16960133)

- Replication: Issuing a `GRANT` statement with invalid parameters caused the master to write

`LOST_EVENTS` events into its binary logs, causing replication to stop. Now such cases, if one or more grants or revocations of privileges are successful, an incident is written to the log; otherwise, only a warning is logged. (Bug #16629195, Bug #68892)

- `libmysqlclient` version 18 files were removed from `MySQL-shared-compat` RPM packages to

avoid a conflict between the `MySQL-shared` and `MySQL-shared-compat` RPM packages. (Bug#17749617)

- Enabling Index Merge optimizer switches and setting a small `sort_buffer_size` value could lead to a

server exit. (Bug #17617945)

- Some license and documentation files were missing from Windows MSI packages. (Bug #17584523)
- Semijoin materialization strategy was not used for `VARCHAR` columns longer than 512 bytes, resulting in

use of a less-efficient strategy and worse query performance. (The limit in characters rather than bytes depends on the column character set; 170 characters for `utf8`, for example.) (Bug #17566396)

- Using MySQL Installer to install MySQL on Windows, then using Uninstall a Program in the Control

Panel to uninstall MySQL, resulted in the MySQL service entry not being removed. (Bug #17550741)

- Selecting from the `session_connect_attrs` Performance Schema table under high load could cause

a server exit. (Bug #17542370)

- Compilation failures under Visual Studio 2012 were corrected. (Bug #17430236)
- An assertion was raised if `SET PASSWORD` was used for an account that has been manually deleted

from the `mysql.user` table but still present in memory. (Bug #17359329)

- The `CLIENT_CONNECT_WITH_DB` flag was improperly handled in the C client library. This could lead to

a malformed packet sent to the server. (Bug #17351732)

- The `filesort` implementation sometimes failed to allocate enough buffer space, leading to a server

exit. (Bug #17326567)

- The `mysql_options()` C API function could leak memory if called more than once with the

`MYSQL_SET_CLIENT_IP` option. (Bug #17297012)

- The `CONV()` function could call `abs(INT_MIN)`, which is undefined, and cause a server exit. (Bug

#17296644)

- An error array in the SSL code was missing a comma, leading to implicit concatenation of adjacent

messages and a resulting off-by-one error in the relationship between error numbers and messages.

(Bug #17294150)

- `GRANT` without an `IDENTIFIED BY` clause resulted in an error even for existing users. (Bug #16938568)

## MySQL 5.6 Release Notes

- `GROUP_CONCAT()` with an invalid separator could cause a server exit. (Bug #16870783)
- An internal `InnoDB` string routine could write past the end of a buffer. (Bug #16765410)
- For uninstall operations, the MySQL Server MSI installer failed to remove some files if the server was

running. This could lead to problems for a subsequent installation of a lower MySQL version: The installer reported a successful operation but not some of the files from the original installation were not replaced by their lower-versioned counterparts. (Bug #16685125)

- GIS intersection-related code was missing a return value check, leading to a loop in nondebug builds

and a raised assertion in debug builds. (Bug #16659166)

- Using the binary client/server protocol, the second execution of a prepared statement for a query with

parameters in the `LIMIT` clause raised an assertion. (Bug #16346241)

- For upgrades using the Windows MSI package installer, the upgrade dialog message was missing the

“from” version. (Bug #16053094)

- Very long database names in queries could cause the server to exit. (Bug #15912213, Bug #16900358)
- Standalone Windows MSI packages did not have the `ALLUSERS` property set. They now set

`ALLUSERS=1`. For earlier MSI packages in this MySQL series, a workaround is to use the following command:

```
C:\> msiexec /i msi_installer_name ALLUSERS=1
```

(Bug #14647206)

- Recursion by functions called as arguments to XPath expressions was not handled correctly, sometimes

causing such expressions to fail. (Bug #14040071)

- Some `.pdb` files were missing from Windows Zip archive distributions. (Bug #13878021)
- Several issues identified by the Coverity static analysis tool were fixed. Thanks to Jan Staněk and Honza

Horak for the patches. (Bug #70591, Bug #17590095)

- Setting `host_cache_size` at startup had no effect. (Bug #70552, Bug #17576516)
- MySQL did not compile on OS X 10.9 (Mavericks). (Bug #70542, Bug #17647863)
- In some cases, range conditions over indexes defined on column prefixes returned incomplete result

sets. (For example, `SELECT ... WHERE 'abcdef1' < col_name AND col_name < 'abcdef9'`,where the index on `col_name` indexed only the first 6 characters.) (Bug #70341, Bug #17458273)

- `InnoDB` full-text searches failed to find records within transactions that included savepoints. (Bug

#70333, Bug #17458835)

- If asked to upgrade a server that was running without `InnoDB` enabled, `mysql_upgrade` issued

complaints about `InnoDB` tables not existing (tables that will not exist unless `InnoDB` is available). (Bug#70152, Bug #17361912)

- With the thread pool plugin enabled, the `PROCESSLIST_USER` and `PROCESSLIST_HOST` columns of the

`threads` Performance Schema table were always `NULL` for client sessions. Also, for the main thread,those columns were not `NULL` but set to a user account.

Note As part of the bug fix implementation, Performance Schema instrumentation for the thread pool plugin was changed to use `thread_pool`, not `sql`.

## MySQL 5.6 Release Notes

(Bug #70028, Bug #17310065, Bug #17049691)

- Performance Schema instrumentation overhead was reduced for frequent connect/disconnect

operations. (Bug #70018, Bug #17310878)

- `COUNT(DISTINCT)` should not count `NULL` values, but they were counted when the optimizer used

Loose Index Scan. (Bug #69841, Bug #17222452)

- In debug builds, static initialization code could call DBUG functions before the DBUG subsystem was

initialized. (Bug #69653, Bug #17063675)

- Some `INSERT INTO ... SELECT ... FROM` statements were slow unless the `tmp_table_size`

and `max_heap_table_size` system variables were set large enough to permit the temporary table used for query processing to be stored in the `MEMORY` storage engine. (Bug #69368, Bug #16894092)

- Some possible cases of memory use after being freed were fixed. Thanks to Jan Staněk for the patch.

(Bug #68918, Bug #16725945)

- Missing `va_end()` calls were added to logging and UCS2 code. Thanks to Jan Staněk for the patch.

(Bug #68896, Bug #16725769)

- For queries of the form `UPDATE ... WHERE unique_key ORDER BY ... LIMIT ...`, incorrect

rows could be updated. Unique keys permit multiple `NULL` values, but the optimizer did not always consider all of them. (Bug #68656, Bug #16482467)

- For an `ALTER TABLE` statement that renamed or changed the default value of a `BINARY` column, the

alteration was done using a table copy and not in place. (Bug #67141, Bug #14735373, Bug #69580,Bug #17024290)

- The server uses the ethernet hardware address for UUID generation, but made assumptions about the

names of ethernet devices rather than querying the system for their names. Thanks to Honza Horak for the patch. (Bug #63055, Bug #13548252)

- Host names in grant tables are stored in lowercase, but `mysql_install_db` could fail to observe

this convention, leading to accounts that could not be dropped with `DROP USER`. (Bug #62255, Bug#12917164, Bug #62254, Bug #12917151)

- Killing a query that is performing a `filesort` operation resulted in an `ER_SERVER_SHUTDOWN` (Server

shutdown in progess) error. (Bug #18256, Bug #11745656)
