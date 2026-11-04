---
title: "Changes in MySQL 5.6.2 (2011-04-11, Developer Milestone)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=265"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Note This is a milestone release, for use at your own risk. Upgrades between milestone releases (or from a milestone release to a GA release) are not supported.

Significant development changes take place in milestone releases and you may encounter compatibility issues, such as data format changes that require attention in addition to the usual procedure of running `mysql_upgrade`. For example, you may find it necessary to dump your data with `mysqldump` before the upgrade and reload it afterward. (Making a backup before the upgrade is a prudent precaution in any case.)

- INFORMATION_SCHEMA Tables for InnoDB Buffer Pool Information

## MySQL 5.6 Release Notes

- INFORMATION_SCHEMA Table for InnoDB Metrics
- INFORMATION_SCHEMA Tables for InnoDB Data Dictionary
- Persistent InnoDB Optimizer Statistics
- InnoDB Configurable Data Dictionary Cache
- Optimizer Notes
- Explicit Partition Selection
- Performance Schema Notes
- Pluggable Authentication
- Plugin Notes
- Crash-Safe Binary Log
- Slave Log Tables
- Row Image Control
- Functionality Added or Changed
- Bugs Fixed

> INFORMATION_SCHEMA Tables for InnoDB Buffer Pool Information

- InnoDB: The new `INFORMATION_SCHEMA` tables `INNODB_BUFFER_PAGE`,

`INNODB_BUFFER_PAGE_LRU`, and `INNODB_BUFFER_POOL_STATS` display `InnoDB` buffer pool information for tuning on large-memory or highly loaded systems. (WL #5614)

> INFORMATION_SCHEMA Table for InnoDB Metrics

- InnoDB: A new `INFORMATION_SCHEMA` table, `INNODB_METRICS`, lets you query low-level `InnoDB`

performance information, getting cumulative counts, averages, and minimum/maximum values for internal aspects of the storage engine operation. You can start, stop, and reset the metrics counters

```
using the innodb_monitor_enable, innodb_monitor_disable, innodb_monitor_reset, and
```

`innodb_monitor_reset_all` system variables. (WL #5316, WL #5776)

> INFORMATION_SCHEMA Tables for InnoDB Data Dictionary

- InnoDB: The `InnoDB` data dictionary, containing metadata about `InnoDB` tables, columns, indexes, and

foreign keys, is available for SQL queries through a set of `INFORMATION_SCHEMA` tables. (WL #5373)

> Persistent InnoDB Optimizer Statistics

- Performance; InnoDB: The optimizer statistics for `InnoDB` tables can now persist across server

restarts, producing more stable query performance. You can also control the amount of sampling done to estimate cardinality for each index, resulting in more accurate optimizer statistics. This feature involves the configuration options `innodb_analyze_is_persistent` (later replaced

```
by innodb_stats_persistent), innodb_stats_persistent_sample_pages, and
```

`innodb_stats_transient_sample_pages`, and the `ANALYZE TABLE` statement. See Configuring Persistent Optimizer Statistics Parameters for details. (WL #5520)

## MySQL 5.6 Release Notes

> InnoDB Configurable Data Dictionary Cache

- InnoDB: To ease the memory load on systems with huge numbers of tables, `InnoDB` now frees up

the memory associated with an opened table using an LRU algorithm to select tables that have gone the longest without being accessed. To reserve more memory to hold metadata for open `InnoDB`tables, increase the value of the `table_definition_cache` configuration option. `InnoDB` treats this value as a “soft limit” for the number of open table instances in the `InnoDB` data dictionary cache. The actual number of tables with cached metadata could be higher than the value specified for `table_definition_cache`, because metadata for `InnoDB` system tables, and parent and child tables in foreign key relationships, is never evicted from memory. For additional information, refer to the`table_definition_cache` documentation. (Bug #20877, Bug #11745884, WL #5457)

> Optimizer Notes

- The optimizer now more efficiently handles queries (and subqueries) of the following form:

```
SELECT ...
FROM single_table ...
ORDER BY non_index_column [DESC]
LIMIT [M,]N;
```

That type of query is common in web applications that display only a few rows from a larger result set.

For example:

```
SELECT col1, ... FROM t1 ... ORDER BY name LIMIT 10;
SELECT col1, ... FROM t1 ... ORDER BY RAND() LIMIT 15;
```

The sort buffer has a size of `sort_buffer_size`. If the sort elements for N rows are small enough to fit in the sort buffer (M+N rows if M was specified), the server can avoid using a merge file and perform the sort entirely in memory. For details, see LIMIT Query Optimization. (WL #1393)

- The optimizer implements Disk-Sweep Multi-Range Read. Reading rows using a range scan on a

secondary index can result in many random disk accesses to the base table when the table is large and not stored in the storage engine's cache. With the Disk-Sweep Multi-Range Read (MRR) optimization,MySQL tries to reduce the number of random disk access for range scans by first scanning the index only and collecting the keys for the relevant rows. Then the keys are sorted and finally the rows are retrieved from the base table using the order of the primary key. The motivation for Disk-sweep MRR is to reduce the number of random disk accesses and instead achieve a more sequential scan of the base table data. For more information, see Multi-Range Read Optimization. (WL #5692)

- The optimizer implements Index Condition Pushdown (ICP), an optimization for the case where MySQL

retrieves rows from a table using an index. Without ICP, the storage engine traverses the index to locate rows in the base table and returns them to the MySQL server which evaluates the `WHERE` condition for the rows. With ICP enabled, and if parts of the `WHERE` condition can be evaluated by using only fields from the index, the MySQL server pushes this part of the `WHERE` condition down to the storage engine.

The storage engine then evaluates the pushed index condition by using the index entry and only if this is satisfied is base row be read. ICP can reduce the number of accesses the storage engine has to do against the base table and the number of accesses the MySQL server has to do against the storage engine. For more information, see Index Condition Pushdown Optimization. (WL #5639)

> Explicit Partition Selection

- Partitioning: It is now possible to select one or more partitions or subpartitions when querying a

partitioned table. In addition, many data modification statements (`DELETE`, `INSERT`, `REPLACE`, `UPDATE`,`LOAD DATA`, and `LOAD XML`) that act on partitioned tables also now support explicit partition selection.

For example, assume we have a table named t with some integer column named c, and t has 4

## MySQL 5.6 Release Notes

partitions named `p0`, `p1`, `p2`, and `p3`. Then the query `SELECT * FROM t PARTITION (p0, p1)``WHERE c < 5` returns rows only in partitions `p0` and `p1` that match the `WHERE` condition, whereas partitions `p2` and `p3` are not checked.

For additional information and examples, see Partition Selection, as well as the descriptions of the statements just listed. (WL #5217)

> Performance Schema Notes

- The Performance Schema has these additions:
- The Performance Schema now has tables that contain summaries for table and index I/O wait events,

as generated by the `wait/io/table/sql/handler` instrument:

- `table_io_waits_summary_by_table`: Aggregates table I/O wait events. The grouping is by

table.

- `table_io_waits_summary_by_index_usage`: Aggregates table index I/O wait events. The

grouping is by table index.

The information in these tables can be used to assess the impact of table I/O performed by applications. For example, it is possible to see which tables are used and which indexes are used (or not used), or to identify bottlenecks on a table when multiple applications access it. The results may be useful to change how applications issue queries against a database, to minimize application footprint on the server and to improve application performance and scalability.

A change that accompanies the new tables is that the `events_waits_current` table now has an `INDEX_NAME` column to identify which index was used for the operation that generated the event. The same is true of the event-history tables, `events_waits_history`, and

```
events_waits_history_long.
```

- The Performance Schema now has an instrument named `wait/lock/table/sql/handler` in the

`setup_instruments` table for instrumenting table lock wait events. It differs from `wait/io/table/``sql/handler`, which instruments table I/O. This enables independent instrumentation of table I/O and table locks.

Accompanying the new instrument, the Performance Schema has a table named`table_lock_waits_summary_by_table` that aggregates table lock wait events, as generated by the new instrument. The grouping is by table.

The information in this table may be used to assess the impact of table locking performed by applications. The results may be useful to change how applications issue queries against the database and use table locks, to minimize the application footprint on the server and to improve application performance and scalability. For example, an application locking tables for a long time may negatively affect other applications; the instrumentation makes this visible.

- To selectively control which tables to instrument for I/O and locking, use the `setup_objects` table.

See Pre-Filtering by Object.

If you upgrade to this MySQL release from an earlier version, you must run `mysql_upgrade` (and restart the server) to incorporate these changes into the `performance_schema` database.

For more information, see MySQL Performance Schema. (WL #5379, WL #5420, WL #5371)

## MySQL 5.6 Release Notes

> Pluggable Authentication

- MySQL distributions now include `auth_socket`, a server-side authentication plugin that authenticates

clients that connect from the local host through the Unix socket file. The plugin uses the `SO_PEERCRED`socket option to obtain information about the user running the client program (and thus can be built only on systems that support this option). For a connection to succeed, the plugin requires a match between the login name of the connecting client user and the MySQL user name presented by the client program. For more information, see Socket Peer-Credential Pluggable Authentication. (Bug #59017, Bug#11765993, Bug #9411, Bug #11745104)

- MySQL distributions now include `mysql_clear_password`, a client-side authentication plugin that

sends the password to the server without hashing or encryption. Although this is insecure, and thus appropriate precautions should be taken (such as using an SSL connection), the plugin is useful in conjunction with server-side plugins that must have access to the original password in clear text. For more information, see Client-Side Cleartext Pluggable Authentication.

> Plugin Notes

- A new plugin service, `my_plugin_log_service`, enables plugins to report errors and specify error

messages. The server writes the messages to the error log. See MySQL Plugin Services. (WL #2940)

> Crash-Safe Binary Log

- Replication: Support for checksums when writing and reading the binary log is added to the MySQL

Server. Writing checksums into the binary log is disabled by default; it can be enabled by starting the server with the `--binlog-checksum` option. To cause the server to read checksums from the binary log, start the server with the `master_verify_checksum` system variable enabled. The `--slave-``sql-verify-checksum` option causes the slave to read checksums from the relay log. (WL #2540)

- Replication: The MySQL Server now records and reads back only complete events or transactions to

and from the binary log. By default, the server now logs the length of the event as well as the event itself and uses this information to verify that the event was written correctly to the log. A master also uses by default this value to verify events when reading from the binary log.

If you enable writing of checksums (using the `binlog_checksum` system variable), the master can use these instead by enabling the `master_verify_checksum` system variable. The slave I/O thread also verifies events received from the master. You can cause the slave SQL thread to use checksums(if available) as well, when reading from the relay log, by enabling the `slave_sql_verify_checksum`system variable on the slave. (WL #5493, WL #2540)

> Slave Log Tables

- Replication: It is now possible to write information about the slave connection to the master

and about the slave's execution point within the relay log to tables rather than files. Logging of master connection information and of slave relay log information to tables can be done independently of one another; this is controlled by the `master_info_repository` and`relay_log_info_repository` system variables. When `master_info_repository=TABLE`,connection information is logged in the `slave_master_info` table in the `mysql` system database. When `relay_log_info_repository=TABLE`, relay log information is logged to the`slave_relay_log_info` table, also in the `mysql` system database. (WL #2775, WL #5125)

> Row Image Control

- Replication: Added the `binlog_row_image` server system variable, which can be used to enable row

image control for row-based replication. This means that you can potentially save disk space, network

## MySQL 5.6 Release Notes

resources, and memory usage by the MySQL Server by logging only those columns that are required for uniquely identifying rows, or which are actually changed on each row, as opposed to logging all columns for each and every row change event. In addition, you can use a “noblob” mode where all columns,except for unneeded `BLOB` or `TEXT` columns, are logged.

For more information, see System Variables Used with Binary Logging. (Bug #47200, Bug #47303, Bug#56917, Bug #11755426, Bug #11755513, Bug #11764116, WL #5092)

> Functionality Added or Changed

- Incompatible Change: The following obsolete constructs have been removed. Where alternatives are

shown, applications should be updated to use them.

- The `FLUSH MASTER` and `FLUSH SLAVE` statements. Use the `RESET MASTER` and `RESET SLAVE`

statements instead.

(WL #5185, WL #6311)

- Important Change; Replication: Added the `binlog_rows_query_log_events` system variable

for `mysqld`. Enabling this variable causes a server logging in row-based mode to write informational rows query log events (SQL statements, for debugging and other purposes) to the binary log. MySQL server and MySQL programs from MySQL 5.6.2 and later normally ignore such events, so that they do not pose an issue when reading the binary log. `mysqld` and `mysqlbinlog` from previous MySQL releases cannot read such events in the binary log, and fail if they attempt to do so. For this reason, you should never prepare logs for a MySQL 5.6.1 or earlier replication slave server (or other reader such as`mysqlbinlog`) with this option enabled on the master. (Bug #50935, Bug #11758695, WL #4033, WL#5404)

- Performance; InnoDB: A separate `InnoDB` thread (`page_cleaner`) now handles the flushing of dirty

pages that was formerly done by the `InnoDB` master thread. (Bug #11762412, Bug #55004, WL #5579)

- Performance; InnoDB: The `innodb_purge_threads` system variable can now be set to a value

higher than 1. (WL #5459)

- Performance; InnoDB: The `InnoDB` kernel mutex, which controls concurrent access to the `InnoDB`

kernel, has been split into several mutexes and rw-locks, for improved concurrency. (WL #5458)

- InnoDB: `InnoDB` can optionally log details about all deadlocks that occur, to assist with troubleshooting

and diagnosis. This feature is controlled by the `innodb_print_all_deadlocks` system variable. (Bug#1784, Bug #17572, WL #5674)

- Replication: On MySQL replication slaves having multiple network interfaces, it is now possible to set

which interface to use for connecting to the master using the `MASTER_BIND='interface'` option in a`CHANGE MASTER TO` statement.

The value set by this option can be seen in the `Master_Bind` column of the output from `SHOW SLAVE``STATUS` or the `Bind` column of the `mysql.slave_master_info` table. (Bug #25939, Bug #11746389,WL #3127)

- Replication: Added the `log_bin_basename` system variable, which contains the complete file name

and path to the binary log file. (The `log_bin` system variable shows only whether or not binary logging is enabled; `log_bin_basename`, however, reflects the name set with the `--log-bin` server option.)Also added `relay_log_basename` system variable, which shows the file name and complete path to the relay log file. (WL #5465)References: See also: Bug #19614, Bug #11745759.

## MySQL 5.6 Release Notes

```
- The mysql_upgrade, mysqlbinlog, mysqlcheck, mysqlimport, mysqlshow, and mysqlslap
```

clients now have `--default-auth` and `--plugin-dir` options for specifying which authentication plugin and plugin directory to use. (Bug #58139)

- The server now includes the thread ID in rows written to the slow query log. In the slow query log file,

the thread ID is the last value in the line. In the `mysql.slow_log` log table, there is a new `thread_id`column.

To update the `slow_log` table if you are upgrading from an earlier release, run `mysql_upgrade`and restart the server. See mysql_upgrade — Check and Upgrade MySQL Tables. (Bug #53630, Bug#11761166)

- The server now writes thread shutdown messages to the error log during the shutdown procedure. (Bug

#48388, Bug #11756464)

- If the `init_file` system variable is given, the server now writes messages indicating the beginning and

end of file execution to the error log. (Bug #48387, Bug #11756463)

- Boolean system variables can be enabled at run time by setting them to the value `ON` or `OFF`, but

previously this did not work at server startup. Now at startup such variables can be enabled by setting them to `ON` or `TRUE`, or disabled by setting them to `OFF` or `FALSE`. Any other nonnumeric value is invalid.

(Bug #46393)References: See also: Bug #11754743, Bug #51631.

- MySQL distributions now include an `INFO_SRC` file that contains information about the source

distribution, such as the MySQL version from which it was created. MySQL binary distributions additionally include an `INFO_BIN` file that contains information about how the distribution was built, such as compiler options and feature flags. In RPM packages, these files are located in the `/usr/share/``doc/packages/MySQL-server` directory. In `tar.gz` and derived packages, they are located in the`Docs` directory under the location where the distribution is unpacked. (Bug #42969, Bug #11751935)

- Multi-read range access is now based on cost estimates and no longer used for simple queries for which

it is not beneficial. (Bug #37576, Bug #11748865)

- Previously, for queries that were aborted due to a sort problem, the server wrote the message `Sort`

`aborted` to the error log. Now the server writes more information to provide a more specific message,such as:

```
Sort aborted: Out of memory (Needed 24 bytes)
Out of sort memory, consider increasing server sort buffer size
Sort aborted: Out of sort memory, consider increasing server sort
buffer size
Sort aborted: Incorrect number of arguments for FUNCTION test.f1;
expected 0, got 1
```

In addition, if the server was started with `--log-warnings=2`, the server writes information about the host, user, and query. (Bug #36022, Bug #11748358)

- Previously, for queries that were aborted due to a sort problem or terminated with `KILL` in the middle

of a sort, the server wrote the message `Sort aborted` to the error log. Now the server writes more information about the cause of the error. These causes include:

- Insufficient disk space in the temporary file directory prevented a temp file from being created
- Insufficient memory for `sort_buffer_size` to be allocated
- Somebody ran `KILL id` in the middle of a filesort operation

## MySQL 5.6 Release Notes

- The server was shut down while some queries were sorting
- A transaction was rolled back or aborted due to a lock wait timeout or deadlock
- Unexpected errors, such as a source table or even temp table was corrupt
- Processing of a subquery failed which was also sorting

(Bug #30771, Bug #11747102)

- `mysqldump --xml` now displays comments from column definitions. (Bug #13618, Bug #11745324)
- Windows provides APIs based on UTF-16LE for reading from and writing to the console. MySQL now

supports a `utf16le` character set for UTF-16LE, and the `mysql` client for Windows has been modified to provide improved Unicode support by using these APIs.

To take advantage of this change, you must run `mysql` within a console that uses a compatible Unicode font and set the default character set to a Unicode character set that is supported for communication with the server. For instructions, see Unicode Support on Windows. (WL #5331)

- The undocumented `SHOW NEW MASTER` statement has been removed, and the

`Com_show_new_master` status variable along with it. (WL #5670)

> Bugs Fixed

- Security Fix: Pre-evaluation of `LIKE` predicates during view preparation could cause a server crash.

(Bug #54568, Bug #11762026)

- Incompatible Change; Replication: It is no longer possible to issue a `CREATE TABLE ... SELECT`

statement which changes any tables other than the table being created. Any such statement is not executed and instead fails with an error.

One consequence of this change is that `FOR UPDATE` may no longer be used at all with the `SELECT`portion of a `CREATE TABLE ... SELECT`.

This means that, prior to upgrading from a previous release, you should rewrite any `CREATE``TABLE ... SELECT` statements that cause changes in other tables so that the statements no longer do so.

This change also has implications for replication between a MySQL 5.6 (or later slave) and a master running a previous version of MySQL. In such a case, if a `CREATE TABLE ... SELECT` statement on the master that causes changes in other tables succeeds on the master, the statement nonetheless fails on the slave, causing replication to stop. To keep this from happening, you should rewrite the offending statement before running it on the master. (Bug #11749792, Bug #11745361, Bug #39804, Bug #55876,WL #5576)References: See also: Bug #47899.

- Incompatible Change: When `auto_increment_increment` is greater than one, values generated by

a bulk insert that reaches the maximum column value could wrap around rather producing an overflow error.

As a consequence of the fix, it is no longer possible for an auto-generated value to be equal to the maximum `BIGINT UNSIGNED` value. It is still possible to store that value manually, if the column can accept it. (Bug #39828, Bug #11749800)

## MySQL 5.6 Release Notes

- Important Change; Partitioning: Date and time functions used as partitioning functions now have the

types of their operands checked; use of a value of the wrong type is now disallowed in such cases. In addition, `EXTRACT(WEEK FROM col_name)`, where `col_name` is a `DATE` or `DATETIME` column, is now disallowed altogether because its return value depends on the value of the `default_week_format`system variable. (Bug #54483, Bug #11761948)References: See also: Bug #57071, Bug #11764255.

- Important Change; Replication: The `CHANGE MASTER TO` statement required the value for

`RELAY_LOG_FILE` to be an absolute path, whereas the `MASTER_LOG_FILE` path could be relative.

The inconsistent behavior is resolved by permitting relative paths for `RELAY_LOG_FILE`, in which case the path is assumed to be relative to the slave's data directory. (Bug #12190, Bug #11745232)

- Performance; InnoDB: An `UPDATE` statement for an `InnoDB` table could be slower than necessary if it

changed a column covered by a prefix index, but did not change the prefix portion of the value. The fix improves performance for InnoDB 1.1 in MySQL 5.5 and higher, and the InnoDB Plugin for MySQL 5.1.

(Bug #58912, Bug #11765900)

- InnoDB; Partitioning: The partitioning handler did not pass locking information to a table's storage

engine handler. This caused high contention and thus slower performance when working with partitioned`InnoDB` tables. (Bug #59013)

- InnoDB: This fix introduces a new configuration option, `innodb_change_buffer_max_size`, which

defines the size of the change buffer as a percentage of the size of the buffer pool. Because the change buffer shares memory space with the buffer pool, a workload with a high rate of DML operations could cause pages accessed by queries to age out of the buffer pool sooner than desirable. This fix also devotes more I/O capacity to flushing entries from the change buffer when it exceeds 1/2 of its maximum size. (Bug #11766168, Bug #59214)

- InnoDB: The presence of a double quotation mark inside the `COMMENT` field for a column could prevent

a foreign key constraint from being created properly. (Bug #59197, Bug #11766154)

- InnoDB: It was not possible to query the `information_schema.INNODB_TRX` table while other

connections were running queries involving `BLOB` types. (Bug #55397, Bug #11762763)

- InnoDB: `InnoDB` returned values for “rows examined” in the query plan that were higher than expected.

`NULL` values were treated in an inconsistent way. The inaccurate statistics could trigger “false positives”in combination with the `max_join_size` setting, because the queries did not really examine as many rows as reported.

A new configuration option `innodb_stats_method` lets you specify how `NULL` values are treated when calculating index statistics. Allowed values are `nulls_equal` (the default), `nulls_unequal` and`null_ignored`. The meanings of these values are similar to those of the `myisam_stats_method`option. (Bug #30423)

- Partitioning: Failed `ALTER TABLE ... PARTITION` statements could cause memory leaks. (Bug

#56380, Bug #11763641)References: See also: Bug #46949, Bug #11755209, Bug #56996, Bug #11764187.

- Replication: When using the statement-based logging format, `INSERT ON DUPLICATE KEY UPDATE`

and `INSERT IGNORE` statements affecting transactional tables that did not fail were not written to the binary log if they did not insert any rows. (With statement-based logging, all successful statements should be logged, whether they do or do not cause any rows to be changed.) (Bug #59338, Bug#11766266)

## MySQL 5.6 Release Notes

- Replication: Formerly, `STOP SLAVE` stopped the slave I/O thread first and then stopped the slave SQL

thread; thus, it was possible for the I/O thread to stop after replicating only part of a transaction which the SQL thread was executing, in which case—if the transaction could not be rolled back safely—the SQL thread could hang.

Now, `STOP SLAVE` stops the slave SQL thread first and then stops the I/O thread; this guarantees that the I/O thread can fetch any remaining events in the transaction that the SQL thread is executing,so that the SQL thread can finish the transaction if it cannot be rolled back safely. (Bug #58546, Bug#11765563)

- Replication: `mysqlbinlog` printed `USE` statements to its output only when the default database

changed between events. To illustrate how this could cause problems, suppose that a user issued the following sequence of statements:

```
CREATE DATABASE mydb;
USE mydb;
CREATE TABLE mytable (column_definitions);
DROP DATABASE mydb;
CREATE DATABASE mydb;
USE mydb;
CREATE TABLE mytable (column_definitions);
```

When played back using `mysqlbinlog`, the second `CREATE TABLE` statement failed with `Error: No``Database Selected` because the second `USE` statement was not played back, due to the fact that a database other than `mydb` was never selected.

This fix ensures that `mysqlbinlog` outputs a `USE` statement whenever it reads one from the binary log.

(Bug #50914, Bug #11758677)

- Replication: The `--help` text for `mysqlbinlog` now indicates that the `--verbose` (`-v`) option outputs

pseudo-SQL that is not necessarily valid SQL and cannot be guaranteed to work verbatim in MySQL clients. (Bug #47557, Bug #11755743)

- Microsoft Windows: On Windows, an object in thread local storage could be used before the object

was created. (Bug #55730, Bug #11763065)

- Two unused test files in `storage/ndb/test/sql` contained incorrect versions of the GNU Lesser

General Public License. The files and the directory containing them have been removed. (Bug#11810224)References: See also: Bug #11810156.

- Queries that used `COALESCE()` with `cp1251` strings could result in an “illegal mix of collations” error.

(Bug #60101, Bug #11766874)

- An assertion was raised if an `XA COMMIT` was issued when an XA transaction had already encountered

an error (such as a deadlock) that required the transaction to be rolled back. (Bug #59986, Bug#11766788)

- On some systems, debug builds of `comp_err` could fail due to an uninitialized variable. (Bug #59906,

Bug #11766729)

- Setting the `optimizer_switch` system variable to an invalid value caused a server crash. (Bug

#59894, Bug #11766719)

- Attempting to create a spatial index on a `CHAR` column longer than 31 bytes led to an assertion failure if

the server was compiled with safemutex support. (Bug #59888, Bug #11766714)

- Aggregation followed by a subquery could produce an incorrect result. (Bug #59839, Bug #11766675)

## MySQL 5.6 Release Notes

- The Performance Schema did not update status handler status variables, so `SHOW STATUS LIKE`

`'%handler%'` produced undercounted values. (Bug #59799, Bug #11766645)

- Internally, XOR items partially behaved like functions and partially as conditions. This resulted in

inconsistent handling and crashes. The issue is fixed by consistently treating XOR items as functions.

(Bug #59793, Bug #11766642)

- An incorrect character set pointer passed to `my_strtoll10_mb2()` caused an assertion to be raised.

(Bug #59648, Bug #11766519)

- `DES_DECRYPT()` could crash if the argument was not produced by `DES_ENCRYPT()`. (Bug #59632, Bug

#11766505)

- The server and client did not always properly negotiate authentication plugin names. (Bug #59453, Bug

#11766356)

- `--autocommit=ON` did not work (it set the global `autocommit` value to 0, not 1). (Bug #59432, Bug

#11766339)

- `FIND_IN_SET()` could work differently in MySQL 5.5 than in 5.1. (Bug #59405, Bug #11766317)
- `mysqldump` did not quote database names in `ALTER DATABASE` statements in its output, which could

cause an error at reload time for database names containing a dash. (Bug #59398, Bug #11766310)

- If `filesort` fell back to an ordinary sort/merge, it could fail to handle memory correctly. (Bug #59331,

Bug #11766260)

- Comparisons of aggregate values with `TIMESTAMP` values were incorrect. (Bug #59330, Bug

#11766259)

- The “greedy” query plan optimizer failed to consider the size of intermediate query results when

calculating the cost of a query. This could result in slowly executing queries when there are much faster execution plans available. (Bug #59326, Bug #11766256)

- A query of the following form returned an incorrect result, where the values for `col_name` in the result

set were entirely replaced with `NULL` values:

```
SELECT DISTINCT col_name ... ORDER BY col_name DESC;
```

(Bug #59308, Bug #11766241)

- The `MYSQL_HOME` environment variable was being ignored. (Bug #59280, Bug #11766219)
- `SHOW PRIVILEGES` did not display a row for the `PROXY` privilege. (Bug #59275, Bug #11766216)
- `SHOW PROFILE` could truncate source file names or fail to show function names. (Bug #59273, Bug

#11766214)

- For `DIV` expressions, assignment of the result to multiple variables could cause a server crash. (Bug

#59241, Bug #11766191)References: See also: Bug #8457.

- `MIN(year_col)` could return an incorrect result in some cases. (Bug #59211, Bug #11766165)
- With index condition pushdown enabled, a join could produce an extra row due to parts of the select

condition for the second table in the join not being evaluated. (Bug #59186, Bug #11766144)

- `DELETE` or `UPDATE` statements could fail if they used `DATE` or `DATETIME` values with a year, month, or

day part of zero. (Bug #59173)

## MySQL 5.6 Release Notes

- The `ESCAPE` clause for the `LIKE` operator permits only expressions that evaluate to a constant at

execution time, but aggregate functions were not being rejected. (Bug #59149, Bug #11766110)

- Valgrind warnings about uninitialized variables were corrected. (Bug #59145, Bug #11766106)
- Memory leaks detected by Valgrind, some of which could cause incorrect query results, were corrected.

(Bug #59110, Bug #11766075)

- `mysqlslap` failed to check for a `NULL` return from `mysql_store_result()` and crashed trying to

process the result set. (Bug #59109, Bug #11766074)

- There was an erroneous restriction on file attributes for `LOAD DATA`. The requirement that a file be

located in the database directory or world readable is now that the be located in the database directory or readable by the user account used to run the server. (Bug #59085, Bug #11766052)

- `SHOW CREATE TRIGGER` failed if there was a temporary table with the same name as the trigger subject

table. (Bug #58996, Bug #11765972)

- The `DEFAULT_CHARSET` and `DEFAULT_COLLATION` `CMake` options did not work. (Bug #58991, Bug

#11765967)

- In a subquery, a `UNION` with no referenced tables (or only a reference to the `DUAL` virtual table) did not

permit an `ORDER BY` clause. (Bug #58970, Bug #11765950)

- `OPTIMIZE TABLE` for an `InnoDB` table could raise an assertion if the operation failed because it had

been killed. (Bug #58933, Bug #11765920)

- If `max_allowed_packet` was set larger than 16MB, the server failed to reject too-large packets with

“Packet too large” errors. (Bug #58887, Bug #11765878)

- With index condition pushdown enabled, incorrect results were returned for queries on `MyISAM` tables

involving `HAVING` and `LIMIT`, when the column in the `WHERE` condition contained `NULL`. (Bug #58838,Bug #11765835)

- An uninitialized variable for the index condition pushdown access method could result in a server crash

or Valgrind warnings. (Bug #58837, Bug #11765834)

- A `NOT IN` predicate with a subquery containing a `HAVING` clause could retrieve too many rows, when

the subquery itself returned `NULL`. (Bug #58818, Bug #11765815)

- Running a query against an `InnoDB` table twice, first with index condition pushdown enabled and then

with it disabled, could produce different results. (Bug #58816, Bug #11765813)

- An assertion was raised if a stored routine had a `DELETE IGNORE` statement that failed but due to the

`IGNORE` had not reported any error. (Bug #58709, Bug #11765717)

- `WHERE` conditions of the following forms were evaluated incorrectly and could return incorrect results:

```
WHERE null-valued-const-expression NOT IN (subquery)
WHERE null-valued-const-expression IN (subquery) IS UNKNOWN
```

(Bug #58628, Bug #11765642)

- Issuing `EXPLAIN EXTENDED` for a query that would use condition pushdown could cause `mysqld` to

crash. (Bug #58553, Bug #11765570)

- An `OUTER JOIN` query using `WHERE col_name IS NULL` could return an incorrect result. (Bug

#58490, Bug #11765513)

## MySQL 5.6 Release Notes

- Starting the server with the `--defaults-file=file_name` option, where the file name had no

extension, caused a server crash. (Bug #58455, Bug #11765482)

- Outer joins with an empty table could produce incorrect results. (Bug #58422, Bug #11765451)
- In debug builds, `SUBSTRING_INDEX(FORMAT(...), FORMAT(...))` could cause a server crash.

(Bug #58371, Bug #11765406)

- When `mysqladmin` was run with the `--sleep` and `--count` options, it went into an infinite loop

executing the specified command. (Bug #58221, Bug #11765270)

- Some string-manipulating SQL functions use a shared string object intended to contain an immutable

empty string. This object was used by the SQL function `SUBSTRING_INDEX()` to return an empty string when one argument was of the wrong data type. If the string object was then modified by the SQL function `INSERT()`, undefined behavior ensued. (Bug #58165, Bug #11765225)

- Condition pushdown optimization could push down conditions with incorrect column references. (Bug

#58134, Bug #11765196)

- `injector::transaction` did not have support for rollback. (Bug #58082, Bug #11765150)
- Parsing nested regular expressions could lead to recursion resulting in a stack overflow crash. (Bug

#58026, Bug #11765099)

- The fix for Bug #25192 caused `load_defaults()` to add an argument separator to distinguish options

loaded from option files from those provided on the command line, whether or not the application needed it. (Bug #57953, Bug #11765041)References: See also: Bug #25192, Bug #11746296.

- The `mysql` client went into an infinite loop if the standard input was a directory. (Bug #57450, Bug

#11764598)

- If a multiple-table update updated a row through two aliases and the first update physically moved

the row, the second update failed to locate the row. This resulted in different errors depending on the storage engine, although these errors did not accurately describe the problem:

```
- MyISAM: Got error 134 from storage engine
- InnoDB: Can't find record in 'tbl'
```

For `MyISAM`, which is nontransactional, the update executed first was performed but the second was not. In addition, for two equal multiple-table update statements, one could succeed and the other fail depending on whether the record actually moved, which is inconsistent.

Now such an update returns an error if it will update a table through multiple aliases, and perform an update that may physically move the row in at least one of these aliases. (Bug #57373, Bug #11764529,Bug #55385, Bug #11762751)

- `SHOW WARNINGS` output following `EXPLAIN EXTENDED` could include unprintable characters. (Bug

#57341, Bug #11764503)

- Outer joins on a unique key could return incorrect results. (Bug #57034, Bug #11764219)
- For a query that used a subquery that included `GROUP BY` inside a `< ANY()` construct, no rows were

returned when there should have been. (Bug #56690, Bug #11763918)

## MySQL 5.6 Release Notes

- Some RPM installation scripts used a hardcoded value for the data directory, which could result in a

failed installation for users who have a nonstandard data directory location. The same was true for other configuration values such as the PID file name. (Bug #56581, Bug #11763817)

- On FreeBSD and OpenBSD, the server incorrectly checked the range of the system date, causing legal

values to be rejected. (Bug #55755, Bug #11763089)

- If one connection locked the `mysql.func` table using either `FLUSH TABLES WITH READ LOCK` or

`LOCK TABLE mysql.func WRITE` and a second connection tried to either create or drop a loadable function, a deadlock occurred when the first connection tried to use a loadable function. (Bug #53322,Bug #11760878)

- `DISTINCT` aggregates on `DECIMAL UNSIGNED` fields could trigger an assertion. (Bug #52171, Bug

#11759827)

- On FreeBSD, if `mysqld` was killed with a `SIGHUP` signal, it could corrupt `InnoDB` `.ibd` files. (Bug

#51023, Bug #11758773)

- An assertion could be raised if −1 was inserted into an `AUTO_INCREMENT` column by a statement writing

more than one row. (Bug #50619, Bug #11758417)

- A query that contains an aggregate function but no `GROUP BY` clause is implicitly grouped. If such a

query also contained an `ORDER BY` clause, the optimizer could choose to use a temporary table to perform the ordering. This is unnecessary because implicitly grouped queries return at most one row and need no ordering. (Bug #47853)

- The parser failed to initialize some internal objects properly, which could cause a server crash in the

cleanup phase after statement execution. (Bug #47511, Bug #11755703)

- When `CASE ... WHEN` arguments had different character sets, 8-bit values could be referenced as

`utf16` or `utf32` values, raising an assertion. (Bug #44793, Bug #11753363)

- When using `ExtractValue()` or `UpdateXML()`, if the XML to be read contained an incomplete XML

comment, MySQL read beyond the end of the XML string when processing, leading to a crash of the server. (Bug #44332, Bug #11752979)

- Bitmap functions used in one thread could change bitmaps used by other threads, raising an assertion.

(Bug #43152, Bug #11752069)

- `DATE_ADD()` and `DATE_SUB()` return a string if the first argument is a string, but incorrectly returned

a binary string. Now they return a character string with a collation of `connection_collation`. (Bug#31384, Bug #11747221)
