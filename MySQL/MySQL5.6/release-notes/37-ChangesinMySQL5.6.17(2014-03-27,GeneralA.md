---
title: "Changes in MySQL 5.6.17 (2014-03-27, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=86"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

A known limitation of this release:Note If you have `InnoDB` tables with full-text search indexes and you are upgrading from MySQL 5.6.10 to a MySQL version up to and including MySQL 5.6.18, the server will fail to start after the upgrade (Bug#72079). This bug is fixed in MySQL 5.6.19.

As a workaround, remove full-text search indexes prior to upgrading and rebuild full-text search indexes after the upgrade is completed.

- Deprecation and Removal Notes
- Functionality Added or Changed
- Bugs Fixed

> Deprecation and Removal Notes

- Incompatible Change: The `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ZERO_DATE`, and

`NO_ZERO_IN_DATE` SQL modes now are deprecated and setting the `sql_mode` value to include any of them generates a warning. In MySQL 5.7, these modes do nothing. Instead, their effects are included in the effects of strict SQL mode (`STRICT_ALL_TABLES` or `STRICT_TRANS_TABLES`). The motivation for the change in MySQL 5.7 is to reduce the number of SQL modes with an effect dependent on strict mode and make them part of strict mode itself.

To make advance preparation for an upgrade to MySQL 5.7, see SQL Mode Changes in MySQL 5.7.

That discussion provides guidelines to assess whether your applications will be affected by the SQL mode changes in MySQL 5.7. (WL #7467)

```
- The msql2mysql, mysql_convert_table_format, mysql_find_rows,
```

`mysql_fix_extensions`, `mysql_setpermission`, and `mysqlaccess` utilities are now deprecated and will be removed in MySQL 5.7. (Bug #27482, Bug #69012, Bug #69014, Bug #69015, Bug #69016,Bug #69017, Bug #11746603, Bug #16699248, Bug #16699279, Bug #16699284, Bug #16699317, Bug#18179576)

- The `IGNORE` clause for `ALTER TABLE` is now deprecated and will be removed in a future version of

MySQL. `ALTER IGNORE TABLE` causes problems for replication, prevents online `ALTER TABLE` for unique index creation, and causes problems with foreign keys (rows removed in the parent table). (WL#7395)

> Functionality Added or Changed

- Incompatible Change: The `AES_ENCRYPT()` and `AES_DECRYPT()` functions now permit control of the

block encryption mode and take an optional initialization vector argument:

- The new `block_encryption_mode` system variable controls the mode for block-based encryption

algorithms. Its default value is `aes-128-ecb`, which signifies encryption using a key length of 128 bits and ECB mode.

## MySQL 5.6 Release Notes

- An optional `init_vector` argument provides an initialization vector for encryption modes that require

it:

```
AES_ENCRYPT(str,key_str[,init_vector])
AES_DECRYPT(crypt_str,key_str[,init_vector])
```

- A random string of bytes to use for the initialization vector can be produced by calling the new

`RANDOM_BYTES()` function.

For more information, see Encryption and Compression Functions.

These changes make statements that use `AES_ENCRYPT()` or `AES_DECRYPT()` unsafe for statement-based replication and they cannot be stored in the query cache. Queries that use `RANDOM_BYTES()` are unsafe for statement-based replication and cannot be stored in the query cache. (WL #6781)

- InnoDB: Online DDL support is extended to the following operations for regular and partitioned `InnoDB`

tables:

```
- OPTIMIZE TABLE
- ALTER TABLE ... FORCE
```

- `ALTER TABLE ... ENGINE=INNODB` (when run on an `InnoDB` table)

Online DDL support reduces table rebuild time and permits concurrent DML. See InnoDB and Online DDL.

(Bug #13975225)

- Solaris: On Solaris, `mysql_config --libs` now includes `-R/path/to/library` so that libraries

can be found at runtime. (Bug #18235669)

- `mysql_install_db` provides a more informative diagnostic message when required Perl modules are

missing. (Bug #69844, Bug #18187451)

> Bugs Fixed

- Incompatible Change: Old clients (older than MySQL 5.5.7) failed to parse authentication data correctly

if the server was started with the `--default-authentication-plugin=sha256_password` option.

Note As a result of this bug fix, MySQL 5.6.16 clients cannot connect to a 5.6.17 server using an account that authenticates with the `sha256_password` plugin, nor can 5.6.17 clients connect to a 5.6.16 server. Similarly, MySQL 5.7.3 clients cannot connect to a 5.7.4 server using an account that authenticates with the`sha256_password` plugin.

(Bug #17495562)

- Important Change; InnoDB; Partitioning: The `FLUSH TABLES` statement's `FOR EXPORT` option is

now supported for partitioned `InnoDB` tables. (Bug #16943907)

- InnoDB: Running a `SELECT` on a partitioned table caused a memory access violation in `memcpy()`.

(Bug #18383840)References: See also: Bug #18167648.

## MySQL 5.6 Release Notes

- InnoDB: For full-text queries, a failure to check that `num_token` is less than `max_proximity_item`

could result in an assertion. (Bug #18233051)

- InnoDB: An invalid `memmove` in `fts_query_fetch_document` would cause a serious error. (Bug

#18229433)

- InnoDB: `innodb_ft_result_cache_limit` now has a hardcoded maximum value of 4294967295

bytes or (2**32 -1). The maximum value was previously defined as the maximum value of `ulong`. (Bug#18180057, Bug #71554)

- InnoDB: An `UPDATE` resulted in a memory access error in `lock_rec_other_trx_holds_expl`. The

transaction list (`trx_sys->rw_trx_list`) was traversed without acquiring the transaction subsystem mutex (`trx_sys->mutex`). (Bug #18161853)

- InnoDB: `InnoDB` failed to restore a corrupt first page of a system tablespace data file from the

doublewrite buffer, resulting in a startup failure. (Bug #18144349, Bug #18058884)

- InnoDB: A regression introduced by Bug #14329288 would result in a performance degradation when a

compressed table does not fit into memory. (Bug #18124788, Bug #71436)References: This issue is a regression of: Bug #14329288.

- InnoDB: The maximum value for `innodb_thread_sleep_delay` is now 1000000

microseconds. The previous maximum value (4294967295 microseconds on 32-bit and 18446744073709551615 microseconds on 64-bit) was unnecessarily large. Because the maximum value of `innodb_thread_sleep_delay` is limited by the value set for`innodb_adaptive_max_sleep_delay` (when set to a nonzero value), the maximum value for `innodb_thread_sleep_delay` is now the same as the maximum value for`innodb_adaptive_max_sleep_delay`. (Bug #18117322)

- InnoDB: Attempting to uninstall the `InnoDB` `memcached` plugin while the `InnoDB` `memcached` plugin is

still initializing would kill the `InnoDB` `memcached` daemon thread. Uninstall should wait until initialization is complete. (Bug #18038948)

- InnoDB: A full-text tokenizer thread would terminate with an incorrect error message. (Bug #18021306)
- InnoDB: In debug builds, creating a unique index on a binary column, with input data containing

duplicate keys, would cause an assertion. (Bug #18010711)

- InnoDB: The `srv_monitor_thread` would crash in the `lock_print_info_summary()` function due

to a race condition between the `srv_monitor_thread` and purge coordinator thread. (Bug #17980590,Bug #70430)

- InnoDB: Attempting to add an invalid foreign key when foreign key checking is disabled

(`foreign_key_checks=0`) would cause a serious error. (Bug #17666774)

- InnoDB: For debug builds, the table rebuilding variant of online `ALTER TABLE`, when run on tables with

BLOB columns, would cause an assertion in the `row_log_table_apply_update` function. For normal builds, a `DB_PRODUCTION` error would be returned. (Bug #17661919)

- InnoDB: When creating a table there are a minimum of three separate inserts on the

`mysql.innodb_index_stats` table. To improve `CREATE TABLE` performance, there is now a single`COMMIT` operation instead of one for each insert. (Bug #17323202, Bug #70063)

- InnoDB: The server would halt with an assertion in `lock_rec_has_to_wait_in_queue(lock)` due

to a locking-related issue and a transaction being prematurely removed from `trx_sys->rw_trx_set`.

(Bug #17320977)

## MySQL 5.6 Release Notes

- InnoDB: Server shutdown would result in a hang with the following message written to the error log:

“`[NOTE] InnoDB: Waiting for purge thread to be suspended`.” (Bug #16495065)

- InnoDB: `InnoDB` failed to start when `innodb_data_file_path` specified the data file size in kilobytes

by appending K to the size value. (Bug #16287752)

- InnoDB: An insert buffer merge would cause an assertion error due to incorrectly handled ownership

information for externally stored BLOBs.

```
InnoDB: Assertion failure in thread thread_num in file ibuf0ibuf.cc line 4080
InnoDB: Failing assertion: rec_get_deleted_flag(rec, page_is_comp(page))
```

(Bug #14668683)

- InnoDB: Decreasing the `auto_increment_increment` value would have no affect on the next auto-

increment value. (Bug #14049391, Bug #65225)

- Partitioning: When the `index_merge_intersection` flag (enabled by default) or the

`index_merge_union` flag was enabled by the setting of the `optimizer_switch` system variable,queries returned incorrect results when executed against partitoned tables that used the `MyISAM` storage engine, as well as partitioned `InnoDB` tables that lacked a primary key. (Bug #18167648)References: See also: Bug #16862316, Bug #17588348, Bug #17648468.

- Replication: The `MASTER_SSL_CRL` and `MASTER_SSL_CRLPATH` options are not available when using

yaSSL; MySQL Replication now sets these to `NULL` automatically whenever yaSSL is enabled. (Bug#18165937)

- Replication: Setting `slave_parallel_workers` to 1 or greater and starting the slave caused the

slave SQL thread to use but not release memory until the slave was restarted with `STOP SLAVE` and`START SLAVE`. (Bug #18001777, Bug #71197)

- Replication: When a slave was configured with replication filters and `--log-warnings=2`, every

statement which was filtered caused an entry to be written in the error log. For busy servers which generated many statements to be filtered, the result was that the error log could quickly grow to many gigabytes in size. Now a throttle is used for such errors, so that an error message is printed only once in a given interval, saying that this particular error occurred a specific number of times during that interval.

(Bug #17986385)

- Replication: `SHOW SLAVE STATUS` used incorrect values when reporting `MASTER_SSL_CRL` and

`MASTER_SSL_CRLPATH`. (Bug #17772911, Bug #70866)References: This issue is a regression of: Bug #11747191.

- Replication: Binary log events could be sent to slaves before they were flushed to disk on the master,

even when `sync_binlog` was set to 1. This could lead to either of those of the following two issues when the master was restarted following a crash of the operating system:

- Replication cannot continue because one or more slaves are requesting replicate events that do not

exist on the master.

- Data exists on one or more slaves, but not on the master.

Such problems are expected on less durable settings (`sync_binlog` not equal to 1), but it should not happen when `sync_binlog` is 1. To fix this issue, a lock (`LOCK_log`) is now held during synchronization, and is released only after the binary events are actually written to disk. (Bug#17632285, Bug #70669)

## MySQL 5.6 Release Notes

- Replication: When running the slave with `slave_parallel_workers` at 1 or greater, setting `--`

`slave-skip-errors=all` caused the error log to be filled with instances of the warning `Slave SQL:`

```
Could not execute Query event. Detailed error: ;, Error_code: 0. (Bug #17581990,
```

Bug #68429)References: See also: Bug #17986385.

- Replication: A number of possible state messages used as values for the `PROCESSLIST_STATE`

column of the `threads` Performance Schema table were longer than the width of the column (64 characters).

The long state messages are now silently truncated in order to avoid errors. This fix applies in MySQL

5.6 only; a permanent fix for the issue is made in MySQL 5.7 and later. (Bug #17319380)

- Replication: The server did not handle correctly the insertion of a row larger than 4 GB when using row-

based replication. (Bug #17081415)

- Replication: When using row-based replication, an additional auto-increment column on the slave

version of a table was not updated correctly; a zero was inserted instead. (Bug #17066269, Bug #69680)

- Replication: Statements involving the Performance Schema tables should not be written to the binary

log, because the content of these tables is applicable only to a given MySQL Server instance, and may differ greatly between different servers in a replication topology. The database administrator should be able to configure (`INSERT`, `UPDATE`, or `DELETE`) or flush (`TRUNCATE TABLE`) performance schema tables on a single server without affecting others. However, when replicating from a MySQL 5.5 master to a MySQL 5.5 or later slave, warnings about unsafe statements updating Performance Schema tables were elevated to errors. For MySQL 5.6 and later slaves, this prevented the simultaneous use of`performance_schema` and GTIDs (see Replication with Global Transaction Identifiers).

This fix causes all updates on tables in the `performance_schema` database to be filtered on the master and not replicated, regardless of the type of logging that is in effect. Prior to this fix, statements using were handled by being marked as unsafe for replication, which caused warnings during execution;

the statements were nonetheless written to the binary log, regardless of the logging format in effect.

Existing replication behavior for tables in the `INFORMATION_SCHEMA` database is not changed by this fix.

For more information, see MySQL Performance Schema. (Bug #16814264)References: See also: Bug #14741537, Bug #18259193.

- Replication: Modifying large amounts of data within a transaction can cause the creation of temporary

files. Such files are created when the size of the data modified exceeds the size of the binary log cache(`max_binlog_cache_size`). Previously, such files persisted until the client connection was closed,which could allow them to grow until they exhausted all available disk space in `tmpdir`. To prevent this from occurring, the size of a temporary file created in this way in a given transaction is now reset to 0 when the transaction is committed or rolled back. (Bug #15909788, Bug #18021493, Bug #66237)

- Replication: The server checks to determine whether semisynchronous replication has been enabled

without a lock, and if this is the case, it takes the lock and checks again. If semisynchronous replication was disabled after the first but prior to the second one, this could cause the server to fail. (Bug#14511533, Bug #66411)References: See also: Bug #17920923.

- Replication: Semisynchronous replication became very slow if there were many dump threads (such

as from `mysqlbinlog` or slave I/O connections) working at the same time. It was also found that

## MySQL 5.6 Release Notes

semisynchronous master plugin functions were called even when the dump connections did not support semisynchronous replication, which led to locking of the plugin lock as well as wasting time on necessary code.

After this fix, non-semisynchronous dump threads no longer call semisynchronous master functions to observe binary events. (Bug #70218, Bug #17434690)

- Microsoft Windows: On Microsoft Windows, the rw-lock backup implementation for the `my_atomic_*`

functions was always used. Now, the native Microsoft Windows implementation is used, where available.

(Bug #18054042)

- `mysql_install_db` could hang while reading `/dev/random` to generate a random `root` password.

(Bug #18395378)

- While printing the server version, the `mysql` client did not check for buffer overflow in a string variable.

(Bug #18186103)

- Compilation failed if MySQL was configured with `CFLAGS` set to include a `-Werror` option with an

argument. (Bug #18173037)

- A shared `libmysqld` embedded server library was not built on Linux. A new

`WITH_EMBEDDED_SHARED_LIBRARY` `CMake` option now makes this possible. (Bug #18123048, Bug#16430656, Bug #68559)

- Building MySQL from source on Windows using Visual Studio 2008 failed with an `identifier not`

`found` error due to a regression introduced by the patch for Bug#16249481. (Bug #18057449)References: This issue is a regression of: Bug #16249481.

- When tables are reopened from the table cache and the current thread is not instrumented for the

Performance Schema, a table handle was unnecessarily instrumented. (Bug #18047865)

- The `SUM_SORT_MERGE_PASSES` column value in the `events_statements_summary_by_digest`

Performance Schema table was calculated incorrectly. (Bug #17938255)

- If the `events_statements_summary_by_digest` Performance Schema table was full when a

statement with a new digest was found, the `Performance_schema_digest_lost` status variable was not incremented. (Bug #17935314)

- The audit log plugin could cause a server exit during log file rotation operations when there were many

operations happening for multiple connections. (Bug #17930339)

- The optimizer could push down a condition when the index did not have the key part present in the

condition. (Bug #17814492)

- Contraction information in a collation could be mishandled, resulting in incorrect decisions about whether

a character is part of a contraction, and miscalculation of contraction weights. (Bug #17760379)

- `DROP TRIGGER` succeeded even with the `read_only` system variable enabled. (Bug #17503460)
- If used to process a prepared `CALL` statement for a stored procedure with `OUT` or `INOUT` parameters,

`mysql_stmt_store_result()` did not properly set the flags required to retrieve all the result sets.

(Bug #14492429, Bug #17849978)

- Aggregating the results of a subquery in the `FROM` clause could produce incorrect results. (Bug #71244,

Bug #18014565)

- A query that creates a temporary table to find distinct values and has a constant value in the projected

list could produce incorrect results. (Bug #70657, Bug #17634335)

## MySQL 5.6 Release Notes

- When run by `root`, `mysqld --help --verbose` exited with a nonzero error code after displaying the

help message. (Bug #70058, Bug #17324415)

- A deadlock error occurring during subquery execution could cause an assertion to be raised. (Bug

#69969, Bug #17307201)

- A temporal literal string without delimiters and more than 14 digits was validated as a `TIMESTAMP/`

`DATETIME` value with a two-digit precision fractional seconds part. But fractional seconds should always be separated from other parts of a time by a decimal point. (Bug #69714, Bug #17080703)

- For system variables that take a string value, `SET` statements permitted an unquoted value, but values

that contained dots were parsed incorrectly and only part of the value was assigned. For example, `SET``GLOBAL slow_query_log_file = my_slow.log` assigned the value `my_slow`. Now such values must be quoted or an error occurs. (Bug #69703, Bug #17075846)

```
- The mysqladmin, mysqlbinlog, mysqlcheck, mysqldump, mysqlimport, mysqlslap, and
```

`mysqlshow` programs now support a `--secure-auth` option that prevents sending passwords to the server in old (pre-4.1) format. This option is enabled by default; use `--skip-secure-auth` to disable it. (Bug #69051, Bug #16723046)

- MySQL client programs from a Community Edition distribution could not connect using SSL to a MySQL

server from an Enterprise Edition. This was due to a difference in certificate handling by yaSSL and OpenSSL (used for Community and Enterprise, respectively). OpenSSL expected a blank certificate to be sent when not all of the `--ssl-ca`, `--ssl-cert`, and `--ssl-key` options were specified, and yaSSL did not do so. To resolve this, yaSSL has been modified to send a blank certificate when an option is missing. (Bug #68788, Bug #16715064)

- Messages written by the server to the error log for LDML collation definition problems were missing the

collation name. (Bug #68144, Bug #16204175)

- On Windows, `mysql_install_db.pl` could be run only from within the `bin` directory under the

installation directory. (Bug #42421, Bug #11751526)
