---
title: "Changes in MySQL 5.6.20 (2014-07-31, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=75"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Deprecation and Removal Notes
- DTrace Support
- InnoDB Notes
- MySQL Enterprise Notes
- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> Deprecation and Removal Notes

- The `timed_mutexes` system variable has no effect and is deprecated. (Bug #18277305, WL #7436)
- The `mysqlhotcopy` utility is now deprecated and will be removed in a future MySQL version. Among

the reasons for this: It works only for the `MyISAM` and `ARCHIVE` storage engines; it works on Unix but not Windows. Alternatives include `mysqldump` and MySQL Enterprise Backup. (WL #7854)

> DTrace Support

- MySQL now includes DTrace support on Oracle Linux 6 or higher with UEK kernel. If DTrace is present,

server builds will detect it with no special `CMake` options required. For information about using DTrace on MySQL, see Tracing mysqld Using DTrace. (WL #7894)

## MySQL 5.6 Release Notes

> InnoDB Notes

- Important Change: Redo log writes for large, externally stored `BLOB` fields could overwrite the most

recent checkpoint. The 5.6.20 patch limits the size of redo log `BLOB` writes to 10% of the redo log file size. The 5.7.5 patch addresses the bug without imposing a limitation. For MySQL 5.5, the bug remains a known limitation.

As a result of the redo log `BLOB` write limit introduced for MySQL 5.6, the `innodb_log_file_size`setting should be 10 times larger than the largest `BLOB` data size found in the rows of your tables plus the length of other variable length fields (`VARCHAR`, `VARBINARY`, and `TEXT` type fields). No action is required if your `innodb_log_file_size` setting is already sufficiently large or your tables contain no`BLOB` data.

Note In MySQL 5.6.22, the redo log `BLOB` write limit is relaxed to 10% of the total redo

```
log size (innodb_log_file_size * innodb_log_files_in_group).
```

(Bug #16963396, Bug #19030353, Bug #69477)

> MySQL Enterprise Notes

- The audit log plugin included in MySQL Enterprise Edition now has the capability of filtering audited

events based on user account and event status. Several new system variables provide DBAs with filtering control. In addition, audit log plugin reporting capability has been improved by the addition of several status variables.

Incompatible configuration change: `audit_log_policy` can be set at server startup (as before), but at runtime is now a read-only variable. This is due to the introduction of two new system variables,`audit_log_connection_policy` and `audit_log_statement_policy`, that provide finer control over logging policy and that can be set either at startup or at runtime. If you continue to use`audit_log_policy` at startup instead of the other two variables, the server uses its value to set those variables.

For more information, see Configuring Audit Logging Characteristics, and Audit Log Plugin Status Variables. (WL #7219)

> Security Notes

- The linked OpenSSL library for the MySQL 5.6 Commercial Server has been updated from version

1.0.1g to version 1.0.1h. Versions of OpenSSL prior to and including 1.0.1g are reported to be vulnerable to CVE-2014-0224.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server 5.6, which uses the yaSSL library instead. (Bug #18917858)

> Functionality Added or Changed

- Replication: The new system variable `binlogging_impossible_mode` controls what happens if the

server cannot write to the binary log, for example, due to a file error. For backward compatibility, the default for `binlogging_impossible_mode` is `IGNORE_ERROR`, meaning the server logs the error,halts logging, and continues updates to the database. Setting this variable to `ABORT_SERVER` makes the server halt logging and shut down if it cannot write to the binary log. (Bug #51014, Bug #11758766)

## MySQL 5.6 Release Notes

- New Debian7, Ubuntu12.04, and Ubuntu14.04 distribution support that was introduced with 5.6.17 now

comes with the platform-specific packaging source placed under the `packaging` directory, in the `deb-``precise`, `deb-wheezy`, and `deb-trusty` directories. (Bug #19020385)

- `CMake` support was updated to handle `CMake` version 3. (Bug #19001781)
- Support for LinuxThreads has been removed from the source code. LinuxThreads was superseded by

NPTL in Linux 2.6. (Bug #17007529, Bug #72888, Bug #18913935)

- By default, `mysql_install_db` creates a `my.cnf` file in the installation base directory using a

template. This may be undesireable for some deployments. To enable this behavior to be suppressed,`mysql_install_db` now supports a `--keep-my-cnf` option to preserve any existing `my.cnf` file and not create a new `my.cnf` file. (Bug #71600, Bug #18205019)

> Bugs Fixed

- Important Change; Replication: A `DROP TABLE` statement may be divided into multiple statements

before it is sent to the binary log if it contains regular (not temporary) tables and temporary tables, or if it contains temporary tables using both transactional and non-transactional storage engines. Now,when using GTIDs, `DROP TABLE` statements affecting these combinations of tables are no longer allowed unless the value of the `gtid_next` system variable is `AUTOMATIC`. This is because, with GTIDs enabled on the server, issuing a `DROP TABLE` in the cases just described while having only one GTID associated with each statement (the SQL thread does this following `SET` `gtid_next='uuid:number'`)causes problems when there are not enough GTIDs for assignment to all the resulting statements following the division of the original `DROP TABLE`.

A `DROP TABLE` statement might be split due to the behavior of the statement with respect to the current transaction varying, depending on table characteristics, as follows:

- `DROP TABLE` of a regular (not temporary) table is committed immediately
- `DROP TABLE` of a temporary table using a transactional storage engine is committed with the current

transaction (following `COMMIT`)

- `DROP TABLE` of a temporary table that uses a nontransactional storage engine is committed

immediately Naming all three of these types of tables in a single `DROP TABLE` statement causes the MySQL server to divide the original statement into three separate `DROP TABLE` statements in the binary log. If GTIDs are enabled but the value of `gtid_next` is not `AUTOMATIC`, issuing a `DROP TABLE` statement that mixes any of the table types described previously causes the server to have an insufficient number of GTIDs to write with all of the resulting statements into the binary log. In addition, `DROP TABLE IF``EXISTS` is always written in the binary log for all tables specified in the statement, even if some or all of the tables do not exist.

Because temporary tables are handled differently by `DROP TABLE` depending on whether they use a transactional or nontransactional storage engine, any tables named by a `DROP TEMPORARY TABLE`statement that do not exist are assumed to be transactional. This means that, if a `DROP TEMPORARY``TABLE` with two nontransactional temporary tables is issued on the master, it would writes only one`DROP TABLE` statement naming both tables. If one of the temporary tables no longer exists on the slave,then, when the SQL thread executes the statement, it tries to divide it into multiple statements due to it affecting a nontransactional (but existing) temporary table and a nonexistent transactional temporary table; this leads to problems because the SQL thread has only one GTID for the original `DROP TABLE`statement but must write two `DROP TABLE` statements in the binary log.

## MySQL 5.6 Release Notes

In addition, when the slave dropped temporary tables after detecting that the master had restarted, it logged one `DROP TABLE` statement per pseudo-thread and per database, but combined temporary tables using transactional and nontransactional storage engines in a single `DROP TABLE` statement.

Now, we throw an error in the client session if `gtid_next` is set to a `uuid`:`number` value and a `DROP``TABLE` statement is issued mixing any of the table types described previously.

In addition, we now group the nonexistent temporary tables and assume them to be transactional only if at least one transactional temporary table is dropped by the statement. If no transactional temporary tables are dropped, any nonexistent temporary tables are assumed to be nontransactional temporary tables.

The slave now also handles dropping of temporary tables correctly in the event of the restart by the master. (Bug #17620053)

- InnoDB: Opening a parent table that has thousands of child tables could result in a long semaphore wait

condition. (Bug #18806829)

- InnoDB: On `mysqld` start, specifying multiple data files using the `innodb_data_file_path`

option would return a `Space id in fsp header` error after data is written to the second file. (Bug#18767811)

- InnoDB: For single item full-text searches, deleted documents were included in inverse document

frequency (IDF) calculations. (Bug #18711306, Bug #72548)

- InnoDB: A `DELETE` operation on a table with full-text search indexes raised an assertion. (Bug

#18683832)References: See also: Bug #14639605.

- InnoDB: When `InnoDB` is built as a shared library, attempting to load the `InnoDB` full-text search (FTS)

`INFORMATION_SCHEMA` plugin would fail with a `Can't open shared library 'ha_innodb.so'`error. (Bug #18655281, Bug #70178)

- InnoDB: When calling the `memcached` `flush_all` command, `InnoDB` attempts to initialize a

connection and a transaction. If the transaction is in `TRX_STATE_NOT_STARTED` state, `InnoDB` failed to set `CONN_DATA->CRSR_TRX` to NULL, resulting in a serious error. (Bug #18652854)

- InnoDB: A regression introduced in MySQL 5.6.5 would cause full-text search index tables to be created

in the system tablespace (space 0) even though `innodb_file_per_table` was enabled. (Bug#18635485)

- InnoDB: The `InnoDB` `memcached` plugin would call `plugin_del` without acquiring the `lock_plugin`

mutex. This bug fix also addresses a race condition in `ib_cursor_delete_row`. (Bug #18409840)

- InnoDB: The fix for Bug#16418661 added superfluous `buf_flush_list()` logic to `InnoDB` startup

code. (Bug #17798076, Bug #70899)References: This issue is a regression of: Bug #16418661.

- InnoDB: A race condition in `fts_get_next_doc_id` resulted in `Duplicate FTS_DOC_ID` and

```
Cannot find index FTS_DOC_ID_INDEX in InnoDB index translation table errors. (Bug
```

#17447086, Bug #70311)References: See also: Bug #16469399.

## MySQL 5.6 Release Notes

- InnoDB: Due to differences in memory ordering on different processor types, some mutex and read-

write lock flags were not read consistently. (Bug #11755438, Bug #47213)

- Partitioning: Selecting from a table having multiple columns in its primary key and partitioned by `LIST`

`COLUMNS(R)`, where R was the last (rightmost) column listed in the primary key definition, returned an incorrect result. (Bug #17909699, Bug #71095)

- Replication: `mysqlbinlog` `--raw` did not check for errors caused by failed writes, which could result in

silent corruption of binary logs. Now in such cases it stops with an error. (Bug #18742916, Bug #72597)

- Replication: When a slave worker thread tried to execute a statement that was too large, the resulting

error caused a crash. Now in such cases, the error is truncated to fit the size of the buffer. (Bug#18563480)

- Replication: When using row-based replication, updating or deleting a row on the master that did not

exist on the slave led to failure of the slave when it tried to process the change. This problem occurred with `InnoDB` tables lacking a primary key. (Bug #18432495, Bug #72085)

- Replication: Quotation marks were not always handled correctly by `LOAD DATA` when written into the

binary log. (Bug #18207212, Bug #71603)

- Replication: Beginning in MySQL 5.6.20, when a user specified `AUTO_INCREMENT` value falls outside

of the range between the current `AUTO_INCREMENT` value and the sum of the current and number of rows affected values it is replicated correctly. In previous versions, an error was generated by the slave even if the user specified `AUTO_INCREMENT` value fell outside of the range. (Bug #17588419, Bug#70583)

- Replication: On Windows, `mysqldump` failed if the error log file was deleted (missing) from the active

MySQL server. (Bug #17076131)

- Replication: Client applications should be able to set the `BINLOG_DUMP_NON_BLOCK` flag in the initial

handshake packet (`COM_BINLOG_DUMP`). Clients connecting to a server issuing a `COM_BINLOG_DUMP`with the flag unset do not get an EOF when the server has sent the last event in the binary log, which causes the connection to block. This flag, which was removed in error in MySQL 5.6.5, is now restored in the current release.

As part of this fix, a new `--connection-server-id` option is added to `mysqlbinlog`. This option can be used by the client to test a MySQL server for the presence of this issue. (Bug #71178, Bug#18000079)

- Replication: Uninstalling and reinstalling semisynchronous replication plugins while semisynchronous

replication was active caused replication failures. The plugins now check whether they can be uninstalled and produce an error if semisynchronous replication is active. To uninstall the master-side plugin, there must be no semisynchronous slaves. To uninstall the slave-side plugin, there must be no semisynchronous I/O threads running. (Bug #70391, Bug #17638477)

- Replication: Replication of tables that contained temporal type fields (such as `TIMESTAMP`, `DATETIME`,

and `TIME`) from different MySQL versions failed due to incompatible `TIMESTAMP` types. The fractional`TIMESTAMP` format added in MySQL 5.6.4 was not being correctly converted. You can now replicate a `TIMESTAMP` in either format correctly according to the `slave_type_conversions` variable. (Bug#70124, Bug #17532932)

- Replication: A group of threads involved in acquiring locks could deadlock when the following events

occurred:

1. Dump thread reconnects from slave; on master, a new dump thread tries to kill zombie dump

threads; having acquired the thread's `LOCK_thd_data`, it is about to acquire `LOCK_log`.

## MySQL 5.6 Release Notes

2. Application thread executing show binary logs, having acquired `LOCK_log` and about to acquire

```
LOCK_index.
```

3. Application thread executing `PURGE BINARY LOGS`; having acquired `LOCK_index`, it is about to

acquire `LOCK_thread_count`.

4. Application thread executing `SHOW PROCESSLIST` (or `SELECT * FROM`

`INFORMATION_SCHEMA.PROCESSLIST`), having acquired `LOCK_thread_count` and about to acquire the zombie dump thread's `LOCK_thd_data`.

This leads to the 4 threads deadlocking in the same order which the threads have been listed here.

This problem arises because there are ordering rules for `LOCK_log` and `LOCK_index`, as well as rules for ordering `LOCK_thread_count` and `LOCK_thd_data`, but there are no rules for ordering across these two sets of locks. This was because the internal `mysqld_list_processes()` function invoked by `SHOW PROCESSLIST` acquired `LOCK_thread_count` for the complete lifetime of the function as well as acquiring and releasing each thread's `LOCK_thd_data`. Now this function takes a copy of the threads from the global thread list and performs its traversal on these, and only after releasing`LOCK_thread_count`. During this traversal, removal from the global thread list is blocked using`LOCK_thd_remove` such that the copies that would otherwise be destroyed by the removal remain valid during traversal. The locking order following this fix is shown here:

```
LOCK_thd_remove -> LOCK_thd_data -> LOCK_log -> LOCK_index -> LOCK_thread_count
```

(Bug #69954, Bug #17283409)References: See also: Bug #73475, Bug #19364731, Bug #19365180.

- When a `SELECT` included a derived table in a join in its `FROM` list and the `SELECT` list included

`COUNT(DISTINCT)`, the `COUNT()` returned 1 even if the underlying result set was empty. (Bug#18853696)References: This issue is a regression of: Bug #11760197.

- Enabling optimizer trace could cause a server exit for queries with a subquery in a `HAVING` clause. (Bug

#18791851)

- SHA and MD5 functions failed for operations using the internal `filename` character set and could cause

a server exit. (Bug #18786138)

- Large arguments passed to `mysqldump` could lead to buffer overflow and program exit. (Bug

#18779944)

- After a metadata change, a reprepared trigger could cause a server exit or prune an incorrect partition.

(Bug #18684393)

- `ALTER TABLE` on a partitioned table could result in the wrong storage engine being written into the

table's `.frm` file and displayed in `SHOW CREATE TABLE`. (Bug #18618561)

- Compiler flags were not passed to DTrace, causing problems for 32-bit builds cross-compiled on 64-bit

platforms. (Bug #18593044)

- With the `max_heap_table_size` system variable set to a large value (20GB), creation of a temporary

table or a table using the `MEMORY` storage engine caused a server exit. (Bug #18463911)

## MySQL 5.6 Release Notes

- If MySQL was built with the `-DINSTALL_LIBDIR=lib64` option, `mysql_config` did not work if the

MySQL package was unpacked into a location with a different installation prefix. Also, `mysql_config`did not work for some RPM builds because it used an incorrect installation prefix. (Bug #18382225)

- For debug builds, a `0x00` character in a full-text query string that used the `ujis_japanese_ci`,

`utf8mb4_turkish_ci`, or `eucjpms_bin` collation could raise an assertion. (Bug #18277305)

- yaSSL code had an off-by-one error in certificate decoding that could cause buffer overflow.

yaSSL code had an `opendir()` without a corresponding `closedir()`. (Bug #18178997, Bug#17201924)

- `mysqladmin password` masked the old password given on the command line, but not the new

password. (Bug #18163964)

- For full-text queries on `InnoDB` tables, attempts to access deleted document IDs could lead to a server

exit. (Bug #18079671)

- `MyISAM` temporary files could be used to mount a code-execution attack. (Bug #18045646)
- For queries that selected from the `events_statements_current` Performance Schema table, adding

an `ORDER BY` clause could produce incorrect results. (Bug #17729044)

- If a query had both `MIN()/MAX()` and `aggregate_function(DISTINCT)` (for example,

`SUM(DISTINCT)`) and was executed using Loose Index Scan, the result values of `MIN()/MAX()` were set improperly. (Bug #17217128)

- For `UNION` statements, the rows-examined value was calculated incorrectly. This was manifest as

too-large values for the `ROWS_EXAMINED` column of Performance Schema statement tables (such as`events_statements_current`). (Bug #17059925)

- Clients could determine based on connection error message content whether an account existed. (Bug

#16513435, Bug #17357528, Bug #19273967)

- An assertion could be raised when creating a index on a prefix of a `TINYBLOB` or `GEOMETRY` column in

an `InnoDB` column. (Bug #16368875, Bug #18776592, Bug #17665767)

- Use of a nonmultibyte algorithm for skipping leading spaces in multibyte strings could cause a server

exit. (Bug #12368495, Bug #18315770)

- Binary MySQL distributions for OS X 10.8 and up now bundle the `MySQL.prefPane` and

`MySQLStartupItem.pkg` tools into the main package as configurable options instead of separate packages. (Bug #74123, Bug #19701502)

- A new `CMake` option, `SUNPRO_CXX_LIBRARY`, enables linking against `libCstd` instead of `stlport4`

on Solaris 10 or later. This works only for client code because the server depends on C++98. Example usage:

```
cmake -DWITHOUT_SERVER=1 -DSUNPRO_CXX_LIBRARY=Cstd
```

(Bug #72352, Bug #18605389)

- `mysql_config_editor` exited when given an empty argument to the `--login-path` option. (Bug

#71837, Bug #18311024, Bug #18830493)

- Upgrades using RPM packages could change the ownership of an installation directory. (Bug #71715,

Bug #18281535)

- Proxy users were unable to execute statements if the proxied user password had expired. (Bug #71337,

Bug #18057562)

## MySQL 5.6 Release Notes

- MySQL did not compile with Bison 3. (Bug #71250, Bug #18017820, Bug #18978946)
- Deadlock could occur if three threads simultaneously performed `INSTALL PLUGIN`, `SHOW VARIABLES`,

and `mysql_change_user()`. (Bug #71236, Bug #18008907, Bug #72870, Bug #18903155)

- If there was a predicate on a column referenced by `MIN()` or `MAX()` and that predicate was not present

in all the disjunctions on key parts earlier in the compound index, Loose Index Scan returned an incorrect result. (Bug #71097, Bug #17909656)

- Client auto-reconnect did not work for clients linked against `libmysqlclient`, even with

`MYSQL_OPT_RECONNECT` enabled.

Also, if a `FEDERATED` table was accessed after `wait_timeout` expired, a `Lost connection to``MySQL server` error occurred without an attempt to re-establish the connection. (Bug #70026, Bug#17309863, Bug #14874, Bug #11745408)

- File permissions and line endings of several test and configuration files were made more consistent to

avoid warnings from package checkers. (Bug #68521, Bug #16415173, Bug #16395459, Bug #68517,Bug #16415032, Bug #71112, Bug #17919313, Bug #71113, Bug #17919422)

- Configuring with `cmake -DWITHOUT_SERVER` to build clients without the server failed for builds outside

of the source tree. (Bug #66000, Bug #14367046)

- For a view defined on a `UNION`, the server could create an invalid view definition. (Bug #65388, Bug

#14117018, Bug #72018, Bug #18405221)

- With `big_tables` enabled, queries that used `COUNT(DISTINCT)` on a simple join with a constant

equality condition on a non-duplicate key returned incorrect results. (Bug #52582, Bug #11760197)References: See also: Bug #18853696.
