---
title: "Changes in MySQL 5.6.7 (2012-09-29, Release Candidate)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=176"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Beginning with MySQL 5.6.7, Oracle no longer provides binaries for OS X 10.5, Debian 5, RHEL/OL 4,SLES 10, FreeBSD 7, Windows XP, or Windows 2003.

- Configuration Notes
- Deprecation and Removal Notes
- Functionality Added or Changed
- Bugs Fixed

> Configuration Notes

- This release continues the process begun in MySQL 5.6.6 of making changes to the default values of

server parameters. The motivation for these changes is to provide better out-of-box performance and to reduce the need for database administrators to change settings manually. These changes are subject to revision in future releases as we gain feedback.

## MySQL 5.6 Release Notes

The following table summarizes changes to defaults. Any of these default settings can be overridden by specifying an explicit value at server startup.

Parameter Old Default New Default`innodb_data_file_path` ibdata1:10M:autoextend ibdata1:12M:autoextend(WL #6216)

> Deprecation and Removal Notes

- If the server was started with `secure_auth` disabled, it did not produce a warning that this is a

deprecated setting. (Bug #65462, Bug #14136937)

- The following items are deprecated and will be removed in a future MySQL release. Where alternatives

are shown, applications should be updated to use them.

- The `SHOW PROFILE` and `SHOW PROFILES` statements. Use the Performance Schema instead; see

MySQL Performance Schema.

- The unused `date_format` `datetime_format` `time_format`, and `max_tmp_tables` system

variables.

- The obsolete `mysql.host` table. New MySQL 5.6 installations will no longer create this table. For

upgrades, `mysql_upgrade` will check for this table and issue a warning about it being deprecated if it is nonempty.

- The (undocumented) `--plugin-xxx` syntax for controlling plugin option `xxx`.

(WL #6443)

- The unused `multi_range_count` system variable is now deprecated, and will be removed in a future

release. (WL #6398)

- In MySQL 5.6.6, `INSERT DELAYED` was deprecated, to be removed in a future release. The

same is now also true for `DELAYED`-related system variables `delayed_insert_limit`,

```
delayed_insert_timeout, delayed_queue_size, max_delayed_threads, and
```

`max_insert_delayed_threads`, and `DELAYED`-related status variables `Delayed_errors`,

```
Delayed_insert_threads, Delayed_writes, and Not_flushed_delayed_rows.
```

> Functionality Added or Changed

- Important Change; Partitioning: The maximum number of partitions for a user-partitioned table is

increased from 1024 to 8192. (Bug #11755685)

- Performance; InnoDB: A new setting `O_DIRECT_NO_FSYNC` was added to the

`innodb_flush_method` configuration option. This setting is similar to `O_DIRECT`, but omits the subsequent `fsync()` call. Suitable for some filesystems but not others. (Bug #11754304, Bug #45892)

- InnoDB: The `--innodb-read-only` option lets you run a MySQL server in read-only mode. You

can access `InnoDB` tables on read-only media such as a DVD or CD, or set up a data warehouse with multiple instances all sharing the same data directory. See Configuring InnoDB for Read-Only Operation for usage details. (Bug #14143600, WL #6445)

- InnoDB: New `INFORMATION_SCHEMA` tables, `innodb_cmp_per_index` and

`innodb_cmp_per_index_reset`, provide statistics on `InnoDB` tables that use compression. The statistics at the index level let DBAs measure whether the proportion of successful or failed compression

## MySQL 5.6 Release Notes

operations is acceptable for a particular combination of table, index, page size, and workload. Typically,the compression failure rate should be less than 10%, particularly when using a compressed table to handle an OLTP-style workload with frequent `INSERT`, `UPDATE`, or `DELETE` operations.

Because gathering those statistics could be very time consuming and would hurt performance negatively, the new tables are enabled only when the new configuration option`innodb_cmp_per_index_enabled` is set to `ON`. (It is `OFF` by default.) (WL #6347)

- InnoDB: Each data block in an `InnoDB` compressed table contains a certain amount of empty space

(padding) to allow DML operations to modify the row data without re-compressing the new values.

Too much padding can increase the chance of a compression failure, requiring a page split, when the data does need to be re-compressed after extensive changes. The amount of padding can now be adjusted dynamically, so that DBAs can reduce the rate of compression failures without re-creating the entire table with new parameters, or re-creating the entire instance with a different page size.

The associated new configuration options are `innodb_compression_failure_threshold_pct`,

```
innodb_compression_pad_pct_max (WL #6345)
```

- InnoDB: You can now select the compression level for `InnoDB` compressed tables, from the familiar

range of 0-9 used by `zlib`. The compression level is controlled by the `innodb_compression_level`configuration option, with a default value of 6:

- Increasing the compression level increases CPU overhead, possibly reducing the amount of storage

needed for any particular row, reducing the possibility of a compression failure and subsequent page split.

- Decreasing the compression level reduces CPU overhead, possibly increasing the amount of storage

needed for any particular row, increasing the possibility of a compression failure and subsequent page split.

You can also control whether compressed pages in the buffer pool are stored in the redo log when an update operation causes pages to be compressed again. This behavior is controlled by the`innodb_log_compressed_pages` configuration option. Turning off logging for compressed pages reduces the amount of redo data that is generated, possibly improving throughput. If the compressed page is required during crash recovery, it is compressed again at that time. (WL #6344)

- When MySQL is configured with `-DWITH_SSL=system` to build with OpenSSL, CMake now produces

an error if OpenSSL is older than version 1.0.1 (Bug #14167227)

- The default has changed from false to true for the `--secure-auth` option for `mysql` and the

`MYSQL_SECURE_AUTH` option for the `mysql_options()` C API function. (Bug #13789417)

- The `WITH_SSL` option for CMake now accepts a `path_name` value that indicates the path name to the

OpenSSL installation to use. This can be useful instead of a value of `system` when the CMake code detects an older or incorrect installed OpenSSL version. (Another permitted way to do the same thing is to set the `CMAKE_PREFIX_PATH` option to `path_name`.) (Bug #61619, Bug #12762891)

- The server now issues a `Note` diagnostic if an index is created that duplicates an existing index. (Bug

#37520, Bug #11748842)

- The MySQL client library now includes SSL support built in. When linking MySQL client programs, you

should no longer specify either `-lssl` or `-lcrypto`.

References: See also: Bug #12762891, Bug #14167227.

- The `mysql_clear_password` cleartext client-side authentication plugin is intended for authentication

schemes that require the server to receive the password as entered on the client side, without hashing.

Because the password is sent in the clear, this plugin should be used within the context of an encrypted

## MySQL 5.6 Release Notes

connection, such as an SSL connection, to avoid exposing the password over the network. To make inadvertent use of this plugin less likely, it is now required that clients explicitly enable it. This can be done several ways:

- Set the `LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN` environment variable to a value that begins with 1,

Y, or y. This enables the plugin for all client connections.

- The `mysql`, `mysqladmin`, and `mysqlslap` client programs support an `--enable-cleartext-`

`plugin` option that enables the plugin on a per-invocation basis.

- The `mysql_options()` C API function supports a `MYSQL_ENABLE_CLEARTEXT_PLUGIN` option that

enables the plugin on a per-connection basis. Also, any program that uses `libmysqlclient` and reads option files can enable the plugin by including an `enable-cleartext-plugin` option in an option group read by the client library.

> Bugs Fixed

- Incompatible Change: Using `ALTER TABLE` to change the definition of a foreign key column could

cause a loss of referential integrity. For example, changing a foreign key column that contained `NULL`values to be `NOT NULL` caused the `NULL` values to be the empty string. Similarly, an `ALTER TABLE``IGNORE` that removed rows in a parent table could break referential integrity.

The server now prohibits changes to foreign key columns with the potential to cause loss of referential integrity. A workaround is to use `ALTER TABLE ... DROP FOREIGN KEY` before changing the column definition and `ALTER TABLE ... ADD FOREIGN KEY` afterward. (Bug #46599, Bug #11754911)

- Important Change; Replication: When issued during an ongoing transaction, any of the following

statements that are used to control MySQL Replication now cause the transaction to be committed:

```
- CHANGE MASTER TO
- START SLAVE
- STOP SLAVE
- RESET SLAVE
```

For more information, see Statements That Cause an Implicit Commit. (Bug #13858841)References: See also: Bug #14298750, Bug #13627921.

- Important Change: The `ALTER USER` statement cleared the user password in the `mysql.user` table.

It no longer does this. (Bug #14226518)

- Important Change: Formerly, the `ExtractValue()` and `UpdateXML()` functions supported a

maximum length of 127 characters for XPath expressions supplied to them as arguments. This limitation has now been removed. (Bug #13007062, Bug #62429)

- Performance; InnoDB: This fix improves the performance of the `InnoDB` `memcached` plugin in several

ways:

- A background thread periodically commits changes made to the database through `memcached`

API calls. This commit interval based on time rather than number of operations lets you increase

```
the value of daemon_memcached_w_batch_size and daemon_memcached_r_batch_size
```

without the risk of some changes remaining uncommitted when DML activity is infrequent. You can control the frequency of these automatic commits through the `innodb_api_bk_commit_interval`configuration option.

## MySQL 5.6 Release Notes

- When binary log support is enabled through the `innodb_api_enable_binlog` configuration option,

you can increase the value of `daemon_memcached_w_batch_size` higher than the default of 1,allowing several DML operations to be committed together rather than a separate commit for each one.

- Internally, the efficiency of mutexes and table opening/closing was improved for operations involving

the `memcached` plugin.

(Bug #14252821)

- Performance; InnoDB: The `OPTIMIZE TABLE` statement now updates the `InnoDB` persistent statistics

for that table when appropriate. (Bug #14238097)

- Performance; InnoDB: This fix removes redundant checksum validation on `InnoDB` pages. The

checksum was being verified both when a compressed page was read from disk and when it was uncompressed. Now the verification is only performed when the page is read from disk. (Bug#14212892, Bug #64170)

- Performance; Replication; Solaris: On Solaris systems, enabling `slave_parallel_workers` could

lead to a slowdown in event executions on the slave. (Bug #14641110)References: See also: Bug #13897025.

- Performance; Replication: When `slave_parallel_workers` was enabled, an internal multiplier

representing the number of events above a certain overrun level in the worker queue was never reset to zero, even when the excess had been taken care of; this caused the multiplier to grow without interruption over time, leading to a slowdown in event executions on the slave. (Bug #13897025)

- Performance: View definitions (in `.frm` files) were not cached and thus every access to a view involved

a file read. Definitions now are cached for better performance. (Bug #13819275)

- Performance: Certain instances of subquery materialization could lead to poor performance. Subquery

materialization now is chosen only if it is less costly than the `EXISTS` transformation. (See Optimizing Subqueries with Materialization, and Optimizing Subqueries with the EXISTS Strategy.)This fix introduces a new flag for the `optimizer_switch` system variable named`subquery_materialization_cost_based`. If the flag is `on` (the default), the optimizer performs a cost-based choice between subquery materialization and `IN -> EXISTS` subquery transformation if either method could be used. If the flag is `off`, the optimizer chooses subquery materialization over `IN``-> EXISTS` subquery transformation, which was the previous behavior. (Bug #13111584)

- InnoDB; Partitioning: A `SELECT` from a partitioned `InnoDB` table having no primary key sometimes

failed to return any rows where a nonempty result was expected. In such cases the server also returned the error `Can't find record in table_name` or `Incorrect key file for table``table_name`. (Bug #13947868)

- InnoDB: When configuring the InnoDB memached plugin system table,

`INNODB_MEMCACHE.CONTAINERS`, a comma (“,”) and empty space are used as a delimiter for mapping multiple columns to a memcached value. This fix allows the pipe character, (“|”), to also be used as a delimiter. (Bug #14560228)

- InnoDB: On Windows systems, a file access error due to an incorrect value for `MYSQL_DATADIR` could

cause an `InnoDB` assertion error. The error could persist after restarting MySQL. (Bug #14558324)

- InnoDB: Inserting data of varying record lengths into an `InnoDB` table that used compression could

cause the server to halt with an error. (Bug #14554000, Bug #13523839, Bug #63815, Bug #12845774,Bug #61456, Bug #12595091, Bug #61208)

## MySQL 5.6 Release Notes

- InnoDB: The default for the `innodb_checksum_algorithm`, which was briefly changed to `crc32`

during the MySQL 5.6 development cycle, was switched back to `innodb` for improved compatibility of`InnoDB` data files during a downgrade to an earlier MySQL version. (Bug #14525151)

- InnoDB: In an `ALTER TABLE` that rebuilds a table, and in particular, `ADD COLUMN`, `DROP COLUMN`,

there were some assertion failures related to `FULLTEXT` indexes, particularly for tables containing more than one `FULLTEXT` index. The fix makes the `ALTER TABLE` correctly use or not use online DDL depending on the presence of `FULLTEXT` indexes. If a table had a `FULLTEXT` index that was dropped,any restrictions on online DDL for that table remain, due to the hidden `FTS_DOC_ID` column. (Bug#14488218)

- InnoDB: Under certain conditions, the `innodb_io_capacity_max` configuration option now uses the

following formula to calculate a default value:

```
innodb_io_capacity_max = max(2000, innodb_io_capacity * 2)
```

The formula only takes affect when you specify a value for `innodb_io_capacity` at server startup and do not specify a value for `innodb_io_capacity_max`. The formula is not used when setting a value for `innodb_io_capacity` dynamically using a `SET` statement. (Bug #14469086)

- InnoDB: Under heavy load of concurrent DML and queries, an `InnoDB` table with a unique index could

return nonexistent duplicate rows to a query. (Bug #14399148, Bug #66134)

- InnoDB: The syntax `ALTER TABLE ... DROP FOREIGN KEY ... ALGORITHM=COPY` incorrectly

considered the names of foreign keys to be case-sensitive. (Bug #14394071)

- InnoDB: When an error (such as a duplicate key error) was detected during an online DDL operation,

while applying changes made to the table while an index was being built, MySQL could encounter an assertion error if the same `ALTER TABLE` statement also contained any `DROP INDEX` clauses. (Bug#14392805)

- InnoDB: When an InnoDB table had a system-chosen primary key, based on a unique index on non-

nullable columns, an error was issued if one of the primary key columns was altered to be nullable. The message was:

```
Warning 1082 InnoDB: Table table_name has a primary key in InnoDB data
dictionary, but not in MySQL!
```

This issue only affected `ALTER TABLE` statements using the online DDL mechanism, that is, with the`ALGORITHM=INPLACE` clause specified or implied. (Bug #14353985)

- InnoDB: A heavy query workload against an `InnoDB` table with a `FULLTEXT` index could cause a crash.

The issue only occurred with some number of queries per second and some number of concurrent connections. (Bug #14347352)

- InnoDB: If an online `CREATE INDEX` operation failed, there was a brief period of time when concurrent

DML operations could fail because the table was considered to be in an error state. (Bug #14341099)

- InnoDB: `ALTER TABLE` statements for partitioned tables could cause unnecessary locking and undo

information. As part of the new online DDL feature, MySQL minimizes this overhead when practical, or you can specify the `ALGORITHM=INPLACE` clause on the `ALTER TABLE` statement. (Bug #14322667)

- InnoDB: The `mysql_install_db` command could crash with an assertion error:

```
InnoDB: Assertion failure in thread thread_num in file trx0rseg.cc line 326
```

The size of the `InnoDB` system tablespace was being capped at 10MB, but during the 5.6 development cycle, the minimum size of a system tablespace became slightly larger than 10MB. (Bug #14315223)

## MySQL 5.6 Release Notes

- InnoDB: A race condition could cause assertion errors during a `DROP TABLE` statement for an `InnoDB`

table. Some internal `InnoDB` functions did not correctly determine if a tablespace was missing; other functions did not handle the error code correctly if a tablespace was missing. (Bug #14251529)

- InnoDB: When more than one `InnoDB` temporary table was created and accessed within the same

transaction, queries on those temporary tables could fail with an `ER_TABLE_DEF_CHANGED` error. (Bug#14234581)

- InnoDB: The server could crash with a combination of a transaction with `SERIALIZABLE` isolation level,

`FLUSH TABLES ... WITH READ LOCK`, and a subsequent query. The error message was:

```
InnoDB: Failing assertion: prebuilt->stored_select_lock_type != LOCK_NONE_UNSET
```

(Bug #14222066)

- InnoDB: Clustered index entries that were rolled back during the rebuild phase of an in-place `ALTER`

`TABLE` operation were not removed from the secondary index. (Bug #14221812)

- InnoDB: This fix addresses several issues regarding `AUTO_INCREMENT` columns when adding a column

using online DDL (that is, with `ALGORITHM=INPLACE`). Now the `AUTO_INCREMENT_OFFSET` value is used properly, the calculation for the next value is corrected, `FLOAT`, `DOUBLE`, and unsigned `INTEGER`auto-increment values are handled correctly, and overflow conditions are detected. (Bug #14219624)

- InnoDB: With the MySQL 5.6 online DDL feature, an `ALTER TABLE` statement to add a primary key to

an `InnoDB` table could succeed, even though the primary key columns contained duplicate values. (Bug#14219515)

- InnoDB: This fix prevents online DDL operations from conflicting with foreign key operations happening

simultaneously on the same table. Updates or deletes based on `CASCADE` or `SET NULL` clauses in the foreign key definition are blocked while the online DDL is in progress, because the information needed in case of a `ROLLBACK` would not be available after the `ALTER TABLE` statement completes. (Bug#14219233)

- InnoDB: A `SHOW ENGINE...STATUS` command could crash if an XA transaction was created using the

statement `START TRANSACTION READ ONLY`. (Bug #14218867)

- InnoDB: The server could crash if a read-only transaction was killed in a session that contained an

`InnoDB` temporary table. (Bug #14213784)

- InnoDB: An `INSERT` into a table after a failed online DDL operation could cause an erroneous assertion

error:

```
InnoDB: Failing assertion: prebuilt->trx_id == 0 || prebuilt->trx_id <= last_index->trx_id
```

(Bug #14176821)

- InnoDB: The server could hang at startup, during crash recovery, if the rollback of previously active

transactions conflicted with the dropping of temporary tables. With this fix, persistent statistics do not apply to `InnoDB` temporary tables. (Bug #14175080)

- InnoDB: The configuration option `innodb_max_io_capacity` was renamed to

`innodb_io_capacity_max`, to emphasize its relationship to the existing `innodb_io_capacity`option. (Bug #14175020)

- InnoDB: An online DDL operations to add a foreign key could incorrectly leave some memory allocated

if the DDL encountered an error. (Bug #14156259)

- InnoDB: The server could crash with a signal 8 (division by zero error) due to a race condition while

computing index statistics. (Bug #14150372)

## MySQL 5.6 Release Notes

- InnoDB: When an auto-increment column used a `FLOAT` or `DOUBLE` data type, if the auto-increment

value became very large (larger than the maximum `unsigned long long` value), subsequent inserts could fail or cause the server to halt. (Bug #14145950, Bug #55071)

- InnoDB: Deleting from an `InnoDB` table containing a prefix index, and subsequently dropping the index,

could cause a crash with an assertion error. (Bug #13807811)

- InnoDB: The value of the `NUMBER_PAGES_CREATED` and `NUMBER_PAGES_WRITTEN` columns of the

`INFORMATION_SCHEMA.INNODB_BUFFER_POOL_STATS` table were set to incorrect values, and the`NUMBER_PAGES_GET` column was not being set at all. (Bug #13639187)

- InnoDB: The error message was improved for the case where an `UPDATE` failed because the row

included several BLOB values greater than 768 bytes each, causing the size of a row to exceed half the page size. The old message, was misleading; it suggested using BLOBs, when the 768-byte prefix for each BLOB column was the cause of the limit error:

```
Error Code 1118: Row size too large. The maximum row size for the used table
type, not counting BLOBs, is 8126. You have to change some columns to TEXT or
BLOBs
```

A workaround for the problem was to create the table with the `ROW_FORMAT=DYNAMIC` or`ROW_FORMAT=COMPRESSED` clause, which is now suggested in the message. (Bug #13453036, Bug#63507)

- InnoDB: The server could crash when updating very large BLOB values, typically 16MB or more. (Bug

#13450566)

- InnoDB: A problem in the locking mechanism could cause a serious error with queries using the

`HANDLER` statement. (Bug #11766271, Bug #59344)

- InnoDB: When a `SELECT ... FOR UPDATE`, `UPDATE`, or other SQL statement scanned rows in an

`InnoDB` table using a < or `<=` operator in a `WHERE` clause, the next row after the affected range could also be locked. This issue could cause a lock wait timeout for a row that was not expected to be locked.

The issue occurred under various isolation levels, such as `READ COMMITTED` and `REPEATABLE READ`.

(Bug #11765218)

- InnoDB: The new online DDL feature addressed long-standing bugs where `ALTER TABLE` statements

caused table rebuilds unnecessarily. This particular bug applied to changing default values for`TIMESTAMP` columns. (Bug #11753646, Bug #45124)

- InnoDB: Various inconsistent behaviors, including tables becoming inaccessible, were cleaned up

for `ALTER TABLE` statements involving `InnoDB` tables involved in foreign key relationships. (Bug#11744929, Bug #5670)

- Partitioning: For tables using `PARTITION BY HASH` or `PARTITION BY KEY`, when the partition

pruning mechanism encountered a multi-range list or inequality using a column from the partitioning key, it continued with the next partitioning column and tried to use it for pruning, even if the previous column could not be used. This caused partitions which possibly matched one or more of the previous partitioning columns to be pruned away, leaving partitions that matched only the last column of the partitioning key.

This issue was triggered when both of the following conditions were met:

1. The columns making up the table's partitioning key were used in the same order as in the partitioning

key definition by a `SELECT` statement's `WHERE` clause as in the column definitions;

## MySQL 5.6 Release Notes

2. The `WHERE` condition used with the last column of the partitioning key was satisfied only by a single

value, while the condition testing some previous column from the partitioning key was satisfied by a range of values.

An example of a statement creating a partitioned table and a query against this for which the issue described above occurred is shown here:

```
CREATE TABLE t1 (
c1 INT,
c2 INT,
PRIMARY KEY(c2, c1)
) PARTITION BY KEY()  # Use primary key as partitioning key
PARTITIONS 2;
SELECT * FROM t1 WHERE c2 = 2 AND c1 <> 2;
```

This issue is resolved by ensuring that partition pruning skips any remaining partitioning key columns once a partition key column that cannot be used in pruning is encountered. (Bug #14342883)

- Partitioning: The buffer for the row currently read from each partition used for sorted reads was

allocated on open and freed only when the partitioning handler was closed or destroyed. For SELECT statements on tables with many partitions and large rows, this could cause the server to use excessive amounts of memory.

This issue has been addressed by allocating buffers for reads from partitioned tables only when they are needed and freeing them immediately once they are no longer needed. As part of this fix, memory is now allocated for reading from rows only in partitions that have not been pruned (see Partition Pruning). (Bug#13025132)References: See also: Bug #11764622, Bug #14537277.

- Replication; Microsoft Windows: On 64-bit Windows platforms, values greater than 4G for the

`max_binlog_cache_size` and `max_binlog_stmt_cache_size` system variables were truncated to 4G. This caused `LOAD DATA` to fail when trying to load a file larger than 4G in size, even when`max_binlog_cache_size` was set to a value greater than this. (Bug #13961678)

- Replication: Updates writing user variables whose values were never set on a slave while using `--`

`replicate-ignore-table` could cause the slave to fail. (Bug #14597605)References: This issue is a regression of: Bug #14275000.

- Replication: A manually created file named `slave_worker_info` in the MySQL Server's data

directory could be mistaken for the actual relay log info file. In addition, when the number of workers(`slave_parallel_workers` server system variable) was decreased, the corresponding info files were not removed as expected. (Bug #14578740)References: See also: Bug #13804728, Bug #14550905, Bug #14550945.

- Replication: With `relay_log_info_repository=FILE` and `slave_parallel_workers` greater

than 0, changing the relay log info repository type to `TABLE` and restarting the slave `mysqld` caused a subsequent `START SLAVE` statement to crash the slave. (Bug #14550945)References: See also: Bug #13804728, Bug #14550905, Bug #14578740.

- Replication: When the number of multithreaded slave workers (as determined by setting

the `slave_parallel_workers` server system variable) was changed when using`relay_log_info_repository=TABLE`, the `mysql.slave_worker_info` table did not reflect the change. (Bug #14550905)

## MySQL 5.6 Release Notes

References: See also: Bug #13804728, Bug #14550945, Bug #14578740.

- Replication: Using `COM_BINLOG_DUMP_GTID` with incorrect data could cause the server to crash. (Bug

#14509140)

- Replication: Executing the `SQL_THREAD_WAIT_AFTER_GTIDS()` function without binary logging

enabled could cause the server to crash. (Bug #14457883)

- Replication: An internal routine in the MySQL Replication code removed elements from a hash used

to store a mapping between databases and worker threads at the same time that the hash was being iterated over. This could cause an unintended reordering of the has elements and thus possibly to incorrect results from routines using this hash. (Bug #14381701)References: See also: Bug #13864642.

- Replication: The names of the binary log and relay log Performance Schema mutexes were mistakenly

changed to names that differed from the MySQL 5.5 names. The names have been reverted to those used in MySQL 5.5. (Bug #14366314)

- Replication: When setting up replication between a master and a slave which was using

`master_info_repository=TABLE`, the `mysql.slave_master_info` table was not updated the first time that `START SLAVE` was issued. (Bug #14298750)References: See also: Bug #13858841.

- Replication: The `--disable-gtid-unsafe-statements` option caused any nontransactional

DML statement involving temporary tables to be rejected with an error even with `binlog_format` set explicitly to `ROW`, in spite of the fact that they are not written to the binary log in this case. Now, such statements are allowed when using row-based logging, as long as any nontransactional tables affected by the statements are also temporary tables. (Bug #14272627)

- Replication: When using multithreaded slaves, `--replicate-rewrite-db` rules were not honored

while assigning databases to slave worker threads, which could cause statements to be executed out of order when this option was used. This could result in a slave that was inconsistent with the master. (Bug#14232958)

- Replication: `mysql_upgrade` failed when the server was running with `gtid_mode=ON` and `--`

`disable-gtid-unsafe-statements` because the MySQL system tables are stored using `MyISAM`.

This problem is fixed by changing the default logging behavior for `mysql_upgrade`; logging is now disabled by default. (Actions taken by `mysql_upgrade` depend on the server version, and thus should not be replicated to slaves.) To enable logging, you can execute `mysql_upgrade` using the `--write-``binlog` option. (Bug #14221043, Bug #13833710)

- Replication: The initialization and usage of a number of internal programming objects relating to GTIDs

did not work properly with `PERFORMANCE_SCHEMA`. (Bug #14152637)

- Replication: The scheduler for multithreaded slaves did not take into account databases implicitly

involved in operations through foreign key dependencies, which could lead to a temporary loss of consistency on the slave. To avoid this problem, replication events on the master that invoke foreign key relationships between table is different databases are now marked in such a way that they can be scheduled sequentially to avoid race conditions and thereby inconsistency. However, this can adversely affect performance. (Bug #14092635)

- Replication: When using a multithreaded slave, the repository type employed for the relay log info log

was not always used automatically for worker repositories as expected. (Bug #13804728)References: See also: Bug #14550905, Bug #14550945, Bug #14578740.

## MySQL 5.6 Release Notes

- Replication: It was possible for the multithreaded slave coordinator to leak memory when the slave was

stopped while waiting for the next successful job to be added to the worker queue. (Bug #13635612)

- Replication: The `Master_id` column of the `mysql.slave_master_info` and

`mysql.slave_relay_log_info` tables showed the slave's server ID instead of the master's server ID. (Bug #12344346)

- Replication: Statements such as `UPDATE ... WHERE primary_key_column = constant LIMIT`

1 are flagged as unsafe for statement-based logging, despite the fact that such statements are actually safe. In cases where a great many such statements were run, this could lead to disk space becoming exhausted do to the number of such false warnings being logged. To prevent this from happening, a warning suppression mechanism is introduced. This warning suppression acts as follows: Whenever the 50 most recent `ER_BINLOG_UNSAFE_STATEMENT` warnings have been generated more than 50 times in any 50-second period, warning suppression is enabled. When activated, this causes such warnings not to be written to the error log; instead, for each 50 warnings of this type, a note is written to the error log stating `The last warning was repeated N times in last S seconds`. This continues as long as the 50 most recent such warnings were issued in 50 seconds or less; once the number of warnings has decreased below this threshold, the warnings are once again logged normally.

The fix for this issue does not affect how these warnings are reported to MySQL clients; a warning is still sent to the client for each statement that generates the warning. This fix also does not make any changes in how the safety of any statement for statement-based logging is determined. (Bug#11759333, Bug #51638)References: See also: Bug #11751521, Bug #42415.

- `ALTER TABLE ... DROP FOREIGN KEY` that did not name the foreign key to be dropped caused a

server crash. Now the foreign key name is required. (Bug #14530380)

- In-place `ALTER TABLE` operations for `InnoDB` tables could raise an assertion attempting to acquire a

lock. (Bug #14516798)

- `mysql_secure_installation` did not work if `old_passwords` was set to 2 (use the

`sha256_password` authentication plugin). (Bug #14506073)

- Index condition pushdown in conjunction with descending index range scan caused a performance

regression. (Bug #14503142)

- `Item_cache_str::save_in_field()` dereferenced a null pointer if the cached value was `NULL`.

(Bug #14501403)

- A query with `GROUP BY ... WITH ROLLUP` comparing a grouping column using the `IN` operator

caused an assertion to be raised. (Bug #14500792)

- In debug builds, with semijoin enabled, `GROUP BY ... WITH ROLLUP` that did not use a temporary

table could cause a server crash. (Bug #14499409)

- An assertion was raised when using the join cache for a query that contained an `IN` subquery query with

a subquery that is expected to return a single row but returned more than one. (Bug #14499331)

- The optimizer could raise an assertion when grouping and sorting in descending order on an indexed

column. (Bug #14498999)

- Polygons with holes could cause a server crash for spatial operations. (Bug #14497827)
- For complex conditions, the optimizer could produce an incorrect range construction and return incorrect

query results. (Bug #14497598)

## MySQL 5.6 Release Notes

```
- In mysql_com.h, the CLIENT_CONNECT_ATTRS and CLIENT_PLUGIN_AUTH_LENENC_CLIENT_DATA
```

symbols incorrectly were defined as the same value. (Bug #14482472)

- The `Threads_running` status variable was not updated properly. (Bug #14471011)
- `GROUP_CONCAT()` with `DISTINCT` or `ORDER BY` on `GEOMETRY` values caused a server crash. (Bug

#14468106)

- With a password policy of `STRONG` and a password of 100 characters or more,

`VALIDATE_PASSWORD_STRENGTH()` could cause a server crash. (Bug #14458293)

- `PASSWORD(NULL)` and `OLD_PASSWORD(NULL)` could cause a server crash. (Bug #14458217)
- The `explicit_defaults_for_timestamp` system variable was not visible (for example, with `SHOW`

`VARIABLES`), so it was not possible to make runtime decisions based on its value. (Bug #14409088)

- When resolving outer fields, `Item_field::fix_outer_fields()` creates new `Item_ref`s for each

execution of a prepared statement, so these must be allocated in the runtime memroot. The memroot switching before resolving `JOIN::having` caused these to be allocated in the statement root, leaking memory for each prepared statement execution. (Bug #14409015)

- An `ALTER TABLE` for an `InnoDB` table that attempted to add an index and also change the nullability of

a column participating in that index raised an assertion. (Bug #14404635)

- For debug builds, if one session used a DDL statement to alter an `InnoDB` table, another session could

raise an assertion failure if it had a pre-alter consistent snapshot of the table. (Bug #14365043)

- The result set could contain extra rows for queries on `MyISAM` tables that used the

`SQL_BUFFER_RESULT` modifier and a subquery. (Bug #14348858)

- The `--server-public-key` option for `mysql` and `mysqltest` has been renamed to `--server-`

`public-key-path` to reflect that it refers to a file and for consistency with related server-side variable naming. Also, this option now is available only if MySQL was built with OpenSSL (not yaSSL) because yaSSL does not support the necessary RSA encryption. (Bug #14348721)

- The RPM spec file now also runs the test suite on the new binaries, before packaging them. (Bug

#14318456)

- Inside a stored program, references to stored program variables in XML functions such as

`ExtractValue()` failed after the first execution of the stored program. (Bug #14317442)

- The Performance Schema used listed the nanosecond timer by default for stages and statements in the

`setup_timers` table. But if this timer was not available on a given platform (such as Windows), timing for stages and statements failed to work. Now the idle, stage, and statement timers used the preferred timers if they are available, but alternate timers if not. (Bug #14298586)

- Some queries for which the optimizer used index condition pushdown in conjunction with `ref` access

could be very slow if the index was read in descending order. (Bug #14287654, Bug #14503142)

- Queries executed using MaterializeScan semijoin strategy and a materialized subquery could return too

many rows. (Bug #14272788)

- A LooseScan semijoin could return duplicate rows from the outer table. (Bug #14271594)
- The Performance Schema generated different digests for a statement before and after selecting a

database. (Bug #14256311)

- The Performance Schema digest-generation code could fail with a race condition. (Bug #14250296)
- The server did not build with `gcc` 4.7. (Bug #14238406)

## MySQL 5.6 Release Notes

- An optimizer trace could crash attempting to print freed subquery items. (Bug #14238404)
- With semijoin optimization enabled, subqueries in the `WITH CHECK OPTION` clause of view definitions

were evaluated incorrectly. (Bug #14230177)

- `ALTER SERVER`, `CREATE SERVER`, and `DROP SERVER` with an empty server name caused a server

crash. (Bug #14220942)

- `ALTER TABLE` with `DISCARD TABLESPACE` or `IMPORT TABLESPACE` did not acquire a sufficiently

strong metadata lock to prevent a concurrent `ALTER TABLE` statement with `ADD` or `DROP` from modifying the tablespace. This could result in warnings or raise an assertion. (Bug #14213236)

- `WEIGHT_STRING()` could crash if given a bad flags argument. (Bug #14211236)
- `REQUIRE ISSUER` clauses for `GRANT` statements were not rewritten properly for logging and caused a

server crash. (Bug #14211069)

- If a call to `socket()` failed, the Performance Schema created instrumentation for it anyway. (Bug

#14209598)

- Some queries with a `HAVING` clause with a function that referred to a function in the `WHERE` list with a

subquery as parameter caused an assertion to be raised. (Bug #14209318)

- String allocation could cause Valgrind warnings. (Bug #14201818)
- For queries that used range access, the optimizer could read uninitialized data, resulting in Valgrind

warnings. (Bug #14200538)

- `mysql_upgrade` did not set the `STATS_PERSISTENT=0` table option for `InnoDB` tables in the `mysql`

database. (Bug #14195056)

- In debug builds, the optimizer raised an unnecessary (too strict) assertion about `MyISAM` key lengths.

(Bug #14179461)

- Join processing could attempt to clean up a temporary table that had not been instantiated, causing a

server crash. (Bug #14168270)

- Incorrect internal conversion of string-format dates could cause a server crash. (Bug #14167911)
- For JSON-format `EXPLAIN` statements, derived tables were not handled properly and caused a server

crash. (Bug #14167499)

- In debug builds, comparisons for strings that had the `ucs2_unicode_520_ci` collation could raise an

assertion. (Bug #14161973)

- In-place `ALTER TABLE` did not work for a table with a `GEOMETRY` column, even if the alteration did not

involve that column. (Bug #14140927)

- For nonexistent files, the Performance Schema file I/O instrumentation sometimes did extra work or was

subject to instrumentation leaks. (Bug #14113704)

- Small `sort_buffer_size` values could result in a server crash. (Bug #14111180)
- Within a trigger, references to a temporary table used during the query execution process could end up

pointing to nonexisting fields on subsequent executions, causing a server crash. (Bug #14105951)

- Negative values could be erroneously reported for some columns in the

`buffer_pool_pages_in_flush` row in the `information_schema.innodb_metrics` table. (Bug#14090287)

## MySQL 5.6 Release Notes

- `JSON`-format `EXPLAIN` statements could raise an assertion or cause the server to hang for statements

with an impossible-`WHERE` clause and subqueries in `ORDER BY` or `GROUP BY` clauses. (Bug #14084642)

- The FirstMatch strategy for semijoins produced incorrect results for some queries with multiple inner

tables. (Bug #14081638)

- With materialization and semijoins enabled, some queries with an OR condition could produce incorrect

results. (Bug #14075016)

- In-place `ALTER TABLE` did not handle autopartitioning storage engines such as `NDB`. (Bug #14063233)
- `RELEASE SAVEPOINT` did not have sufficient checks for the XA transaction state to prevent a savepoint

from being released while the transaction was in a prepared state. (Bug #14062726)

- Improper error handling for `CREATE SERVER`, `DROP SERVER`, and `ALTER SERVER` could raise an

assertion. (Bug #14061851)

- Improper initialization by spatial functions could cause a server crash the first time they were invoked

following server startup. (Bug #14015762)

- For JSON-format `EXPLAIN` statements, improper handling of subqueries could cause an assertion to be

raised. (Bug #13956275)

- `SELECT` on a partitioned table that used a join buffer could cause a server crash. (Bug #13949549)
- Polygon sorting by spatial functions could be done incorrectly and cause a server crash. (Bug

#13938850)

- For `DELETE` statements, `WHERE` clause row retrieval that should access only the index tree could raise

an assertion. (Bug #13919180)

- The argument for `LIMIT` must be an integer, but if the argument was given by a placeholder in a

prepared statement, the server did not reject noninteger values such as `'5'`. (Bug #13868860)

- Some arguments could cause `ST_Buffer()` to crash. (Bug #13832749, Bug #13833019)
- Queries that used the `ST_Contains` and `Within()` functions yielded incorrect results when argument

columns had a spatial index. (Bug #13813064)

- `CHECK TABLE` and `REPAIR TABLE` could crash if a key definition differed in the `.frm` and `.MYI` files of

a `MyISAM` table. Now the server produces an error. (Bug #13555854)

- The optimizer used a full index scan for cases for which a Loose Index Scan was preferable. (Bug

#13464493)References: This issue is a regression of: Bug #12540545.

- `COUNT(DISTINCT(SELECT 1))` could be evaluated incorrectly if the optimizer used Loose Index Scan.

(Bug #13444084)References: See also: Bug #13813126.

- A query for a `FEDERATED` table could return incorrect results when the underlying table had a compound

index on two columns and the query included an `AND` condition on the columns. (Bug #12876932)

- In debug builds, an `InnoDB` assertion was overly aggressive about prohibiting an open range. (Bug

#66513, Bug #14547952)

- Starting the server with `bind_address=*` is supposed to cause the server to accept TCP/IP

connections on all server host IPv6 and IPv4 interfaces if the server host supports IPv6, or TCP/IP

## MySQL 5.6 Release Notes

connections on all IPv4 addresses otherwise. But the server sometimes did not correctly detect when IPv6 was not supported, and failed to start. (Bug #66303, Bug #14483430)

- Queries with `ALL` over a `UNION` could return an incorrect result if the `UNION` result contained `NULL`. (Bug

#65902, Bug #14329235)

- In-place `ALTER TABLE` incorrectly handled indexes using key prefixes by using a copy algorithm. (Bug

#65865, Bug #14304973)

- The `ST_Contains()` and `Within()` functions yielded an incorrect result when used on a column with

a `SPATIAL` index. (Bug #65348, Bug #14096685)

- For some queries, the optimizer used `index_merge` access method when this was more work than `ref`

access. (Bug #65274, Bug #14120360)

- The `GeomFromWKB()` function did not return `NULL` if the SRID argument was `NULL`, and non-`NULL` SRID

values were not included in the converted result. (Bug #65094, Bug #13998446)

- Internal temporary `MyISAM` tables were unnecessarily registered in an open-table list protected by a

global mutex, causing excessive mutex contention. (Bug #65077, Bug #14000697)

- In prepared statements, `MYSQL_TYPE_DATE` parameters when converted to an integer were handled

as `MYSQL_TYPE_DATETIME` values and the conversion produced incorrect results. (Bug #64667, Bug#13904869)

- “Illegal mix of collation” errors were returned for some operations between strings that should have been

legal. (Bug #64555, Bug #13812875)

- `COUNT(DISTINCT(IF ...))` could be evaluated incorrectly if the optimizer used Loose Index Scan.

(Bug #64445, Bug #13813126)References: See also: Bug #13444084.

- The argument to the `--ssl-key` option was not verified to exist and be a valid key. The resulting

connection used SSL, but the key was not used. (Bug #62743, Bug #13115401)

- With statement-based binary logging, stored routines that accessed but did not modify tables took too

strong a lock for the tables, unnecessarily blocking other statements that also accessed those tables.

(Bug #62540, Bug #13036505)

- `mysqlhotcopy` failed for databases containing views. (Bug #62472, Bug #13006947, Bug #12992993)
- Adding a `LIMIT` clause to a query containing `GROUP BY` and `ORDER BY` could cause the optimizer to

choose an incorrect index for processing the query, and return more rows than required. (Bug #54599,Bug #11762052)

- `mysqlbinlog` did not accept input on the standard input when the standard input was a pipe. (Bug

#49336, Bug #11757312)

- There was a performance regression for queries that used `GROUP BY` and `COUNT(DISTINCT)`. (Bug

#49111, Bug #11757108)

- `mysqldump` could dump views and the tables on which they depend in such an order that errors

occurred when the dump file was reloaded. (Bug #44939, Bug #11753490)

## MySQL 5.6 Release Notes
