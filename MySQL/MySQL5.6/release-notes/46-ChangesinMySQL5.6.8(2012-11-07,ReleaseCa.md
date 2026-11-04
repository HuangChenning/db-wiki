---
title: "Changes in MySQL 5.6.8 (2012-11-07, Release Candidate)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=166"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Configuration Notes
- Deprecation and Removal Notes
- Installation Notes
- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> Configuration Notes

- This release continues the process begun in MySQL 5.6.6 of making changes to the default values of

server parameters. The motivation for these changes is to provide better out-of-box performance and to

## MySQL 5.6 Release Notes

reduce the need for database administrators to change settings manually. These changes are subject to revision in future releases as we gain feedback.

In some cases, a parameter has a different fixed default value. In other cases, the server autosizes a parameter at startup using a formula based on other related parameters or server host configuration,rather than using a fixed value. For example, the setting for `host_cache_size` is its previous default of 128, adjusted up by an amount proportional to the value of `max_connections`. The idea behind autosizing is that when the server has information available to make a decision about a parameter setting likely to be better than a fixed default, it will.

The following table summarizes changes to defaults. For variables that are autosized, the main variable description provides additional detail about the sizing algorithm. See Server System Variables, and InnoDB Startup Options and System Variables. Any of these default settings can be overridden by specifying an explicit value at server startup.

Parameter Old Default New Default`host_cache_size` 128 Autosized using

```
max_connections
innodb_log_file_size  5MB  48MB
```

`open_files_limit` 0 Autosized using

```
max_connections
performance_schema  OFF  ON
performance_schema_events_waits_history_long_size10000  Autosized
performance_schema_events_waits_history_size10  Autosize
performance_schema_max_cond_instances1000  Autosize
```

`performance_schema_max_file_instances`10000 Autosize`performance_schema_max_mutex_instances`1000000 Autosize`performance_schema_max_rwlock_instances`1000000 Autosize`performance_schema_max_table_handles`100000 Autosize`performance_schema_max_table_instances`50000 Autosize

```
performance_schema_max_thread_instances1000  Autosize
query_cache_size  0  1M
query_cache_type  ON  OFF
```

`table_definition_cache` 400 Autosized using

```
table_open_cache
```

`table_open_cache` 400 2000`thread_cache_size` 0 Autosized using

```
max_connections
```

(WL #6216)

> Deprecation and Removal Notes

- The `SHOW AUTHORS` and `SHOW CONTRIBUTORS` statements have been removed. (WL #6454)

## MySQL 5.6 Release Notes

> Installation Notes

- `mysql_install_db` is now a Perl script and can be used on any system with Perl installed. Previously,

it was a shell script and available only on Unix platforms.

In addition, `mysql_install_db` is more strict about the `--datadir` option value. Only the last component of the path name is created if it does not exist; the parent directory must already exist or an error occurs. Previously, it created any nonexistent directories in the path name.

- On Unix platforms, `mysql_install_db` now creates a default option file named `my.cnf` in the base

installation directory. This file is created from a template included in the distribution package named `my-``default.cnf`. You can find the template in or under the base installation directory. When started using`mysqld_safe`, the server uses `my.cnf` file by default. If `my.cnf` already exists, `mysql_install_db`assumes it to be in use and writes a new file named `my-new.cnf` instead.

With one exception, the settings in the default option file are commented and have no effect.

The exception is that the file changes the `sql_mode` system variable from its default of`NO_ENGINE_SUBSTITUTION` to also include `STRICT_TRANS_TABLES`:

```
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
```

This setting produces a server configuration that results in errors rather than warnings for bad data in operations that modify transactional tables. See Server SQL Modes.

The `my-default.cnf` template replaces the older sample option files (`my-small.cnf`, `my-``medium.cnf`, and so forth), which are no longer distributed.

- On Unix platforms, `mysql_install_db` supports a new option, `--random-passwords`, that provides

for more secure MySQL installation. Invoking `mysql_install_db` with `--random-passwords` causes it to perform the following actions in addition to its normal operation:

- The installation process creates a random password, assigns it to the initial MySQL `root` accounts,

and sets the “password expired” flag for those accounts.

- The initial random `root` password is written to the `.mysql_secret` file in the directory named by the

`HOME` environment variable. Depending on operating system, using a command such as `sudo` may cause the value of `HOME` to refer to the home directory of the `root` system user. `.mysql_secret` is created with mode 600 to be accessible only to the system user for whom it is created.

If `.mysql_secret` already exists, the new password information is appended to it. Each password entry includes a timestamp so that in the event of multiple install operations it is possible to determine the password associated with each one.

- No anonymous-user MySQL accounts are created.

As a result of these actions, it is necessary after installation to start the server, connect as `root` using the password written to the `.mysql_secret` file, and to select a new `root` password. Until this is done,`root` cannot do anything else. This must be done for each `root` account you intend to use. To change the password, you can use the `SET PASSWORD` statement (for example, with the `mysql` client). You can

```
also use mysqladmin or mysql_secure_installation.
```

New RPM install operations (not upgrades) invoke `mysql_install_db` with the `--random-``passwords` option. As a consequence, RPM installs from this version onward will have their `root`

## MySQL 5.6 Release Notes

accounts secured, and will have no anonymous-user accounts. (Install operations using RPMs for Unbreakable Linux Network are unaffected because they do not use `mysql_install_db`.)For install operations using a binary `.tar.gz` distribution or a source distribution, you can invoke`mysql_install_db` with the `--random-passwords` option manually to make your MySQL installation more secure. This is recommended, particularly for sites with sensitive data.

> Security Notes

- On Windows, many MySQL executables depend on the `libeay32.dll` and `ssleay32.dll` SSL

libraries at runtime. To ensure that the proper versions of these libraries are found, the install process copies them into the same directory as the executables.

> Functionality Added or Changed

- InnoDB: The `InnoDB` transportable tablespace feature was enhanced to allow `ALTER TABLE ...`

`IMPORT TABLESPACE` to succeed in some cases where the corresponding `.cfg` file was not available.

This enhancement allows recovery of data even in some cases where the system tablespace is corrupted or deleted. (Bug #14589582, Bug #66715)

- The number of atomic operations performed by the Performance Schema was reduced. (Bug

#14658739)

- `ALTER USER` now can be used as a prepared statement. (Bug #66874, Bug #14646014)
- On Unix systems, the `mysql` client writes statements executed interactively to a history file (see mysql

Client Logging). `mysql` now ignores for logging purposes statements that match any pattern in the“ignore” list. By default, the pattern list is `"*IDENTIFIED*:*PASSWORD*"`, to ignore statements that refer to passwords. Pattern matching is not case sensitive. Within patterns, two characters are special:

- ? matches any single character.
- * matches any sequence of zero or more characters.

To specify additional patterns, use the `--histignore` command option or set the `MYSQL_HISTIGNORE`environment variable. (If both are specified, the option value takes precedence.) The value should be a colon-separated list of one or more patterns, which are appended to the default pattern list.

Patterns specified on the command line might need to be quoted or escaped to prevent your command interpreter from treating them specially. For example, to suppress logging for `UPDATE` and `DELETE`statements in addition to statements that refer to passwords, invoke `mysql` like this:

```
shell> mysql --histignore="*UPDATE*:*DELETE*"
```

(Bug #48287, Bug #11756377)

> Bugs Fixed

- Important Change; Replication: When running the slave with the `--slave-skip-errors` option,

successive skipped events (errors logged as warnings) were found to contain information from previous warnings, which caused an excessive amount of redundant information to be written to the error log. This problem could occur when using row-based or mixed-format binary logging.

The fix for this issue is to clear these warnings prior to processing the next skipped event. In addition,the skipped events are now handled in the same way regardless of the value of `binlog_format`,and a skipped error always causes a warning to be written to the error log, as long as the value of the`log_warnings` system variable is greater than 1. (Bug #12776842)

## MySQL 5.6 Release Notes

- Important Change: The server system variables `profiling`, `have_profiling`, and

`profiling_history_size` are now deprecated, and are subject to removal in a future release of the MySQL Server. (Bug #14658683)

- InnoDB: The thread gathering persistent statistics for an `InnoDB` table could cause a serious error if it

accessed the table while a `TRUNCATE TABLE` operation was in progress:

```
InnoDB: Assertion failure in thread thread_num in file fsp0fsp.cc line 1882
```

(Bug #14765035)

- InnoDB: When a `CREATE INDEX` operation failed for an `InnoDB` `FULLTEXT` index due to a duplicate

key error, some allocated memory was not freed. (Bug #14759111)

- InnoDB: During a brief time window while creating an `InnoDB` unique index, MySQL could print a

spurious warning message:

```
WARNING: CANNOT FIND INDEX ?index_name IN INNODB INDEX TRANSLATION TABLE
```

The cause was that MySQL started enforcing the uniqueness constraint before the existence of the index was fully registered. The fix suppresses the incorrect message during this final stage of index creation. (Bug #14735988)

- InnoDB: An online DDL operation to create a unique index could fail to detect duplicate index values,

when the duplicate values were caused by DML operations while the index was being created. (Bug#14733674)

- InnoDB: During an online DDL operation, a duplicate key error could be incorrectly issued if a record

was inserted and subsequently updated while the table was being rebuilt. (Bug #14723456)

- InnoDB: The auxiliary tables for `FULLTEXT` indexes were being created in the system tablespace,

regardless of the setting for the `innodb_file_per_table` configuration option. (Bug #14723291)

- InnoDB: When using the transportable tablespace feature, the `ALTER TABLE ... IMPORT`

`TABLESPACE` statement could crash if the `InnoDB` table being flushed contained a `FULLTEXT` index.

With this fix, the table data can be imported, although you must drop and re-create the `FULLTEXT` index after the import operation. (Bug #14712962, Bug #67081)

- InnoDB: An assertion failure occurred when a bogus duplicate key error was flagged during online

`ALTER TABLE`. This issue only occurred for a table that lacked a primary key and any secondary indexes. This patch fixes the assertion failure, but not the bogus duplicate key error, which is reported as Bug#14723456. (Bug #14712710)

- InnoDB: The `InnoDB` `memcached` plugin can now work with tables where the underlying character set

is multibyte. (Bug #14711015, Bug #67076)

- InnoDB: If a `CREATE TABLE` statement failed due to a disk full error, some memory allocated during the

operation was not freed properly. (Bug #14708715)

- InnoDB: An `ALTER TABLE` operation on an `InnoDB` table containing a `FULLTEXT` index could cause

make the server halt with an assertion error. The fix causes all `ALTER TABLE` operations for such tables to use the table-copying behavior of the `ALGORITHM=COPY` clause. (Bug #14681198)

- InnoDB: If the server crashed while executing `TRUNCATE TABLE` for an `InnoDB` table containing a

`FULLTEXT` index, further errors could occur during crash recovery, preventing the server from restarting.

(Bug #14676345)

## MySQL 5.6 Release Notes

- InnoDB: If an `InnoDB` table containing a `FULLTEXT` index was being modified by a `TRUNCATE TABLE`

statement and on online DDL operation simultaneously, the server could end up with inconsistent internal locks or could crash. (Bug #14676329)

- InnoDB: If creation of a `FULLTEXT` index failed because of a “row too large” condition, a subsequent

`ALTER TABLE` operation could cause the server to halt with an error. (Bug #14668777)

- InnoDB: If the MySQL server crashed while XA transactions were in `PREPARED` state, inconsistent

data could be produced during crash recovery if the query cache was enabled. The fix allows MySQL to disable the query cache during crash recovery if required. (Bug #14658648)

- InnoDB: MySQL could crash while creating an `InnoDB` table if the disk became full at a specific

moment: after the .frm file was created but before the corresponding .ibd file was created. (Bug#14645935)

- InnoDB: If the server crashed at the specific point when a change buffer entry was being merged into

a buffer pool page, the transaction log and the change buffer were left in an inconsistent state. After a restart, MySQL could crash after reading the corresponding secondary index page. The problem was more likely to occur in MySQL 5.5 or later, where the original insert buffering mechanism was generalized to cover other operations. (Bug #14636528, Bug #66819, Bug #58571, Bug #61104, Bug#65443)

- InnoDB: If a crash occurred during a `CREATE TABLE` operation, the `InnoDB` data dictionary could

be left in an inconsistent state, causing a crash if the partially created table was accessed later. (Bug#14601290)

- InnoDB: On startup, MySQL would not start if there was a mismatch between the value of the

`innodb_log_file_size` configuration option and the actual size of the `ib_logfile*` files that make up the redo log. This behavior required manually removing the redo log files after changing the value of`innodb_log_file_size`. The fix causes MySQL to write all dirty pages to disk and re-create the redo log files during startup if it detects a size mismatch. (Bug #14596550, WL #6494)

- InnoDB: With the `innodb_file_per_table` setting enabled, a `DROP TABLE` operation could cause

a crash, due to a race condition that depended on the timing of pending I/O requests. (Bug #14594600,Bug #66718)

- InnoDB: If an online DDL operation failed due to a duplicate key error, caused by DML changes being

made concurrently to the table, the server could crash with an assertion error. (Bug #14591797)

- InnoDB: A query against an `InnoDB` table with a `FULLTEXT` index could crash, if the `AGAINST` clause

contained a character sequence that was encoded incorrectly for the character set of the table. (Bug#14588091)

- InnoDB: If a `FULLTEXT` index was dropped from an `InnoDB` table, and the server crashed later for an

unrelated reason, an additional error could occur while attempting to access nonexistent `FULLTEXT` data structures. (Bug #14586855)

- InnoDB: The server could crash with a confusing message if it ran out of space for temporary files

during index creation.

```
InnoDB: Assertion failure in thread thread_num in file mtr0mtr.cc line 306
InnoDB: Failing assertion: mtr->state == 12231
```

(Bug #14586256)

- InnoDB: An `ALTER TABLE` on an `InnoDB` table that dropped the primary key and then re-created it

with columns in a different order could cause an error. The issue affected tables where the swapped columns referenced each other in a single-table foreign key relationship. The data dictionary could be left

## MySQL 5.6 Release Notes

in an inconsistent state, where the table was listed in `SHOW TABLES` output but could not be queried or dropped. For example, if the table was declared with primary key columns `(c1,c2)` and a foreign key

```
with c1 REFERENCES c2:
ALTER TABLE t2 DROP PRIMARY KEY, ADD PRIMARY KEY (c2, c1);
ERROR 1030 (HY000): Got error 38 from storage engine
```

(Bug #14548753)

- InnoDB: During an online DDL operation, a `ROLLBACK` affecting the same table could cause an

assertion error if the table formerly contained a `FULLTEXT` index. Some bookkeeping information related to `FULLTEXT` indexes for `InnoDB` tables is preserved even after such an index is dropped. (Bug#14503700)

- InnoDB: If a table was defined with an index key length very close to the upper length limit of 3072, a

query against that table could cause a serious error. (Bug #14500557, Bug #14537695)

- InnoDB: Table names containing non-ASCII characters were displayed incorrectly when the

`MYSQL.INNODB_TABLE_STATS.TABLE_NAME` column was queried. (Bug #14404879)

- InnoDB: A race condition could cause a crash during an online `CREATE INDEX` statement for an

`InnoDB` table. This bug only affected very small tables. It required a DML operation to be in progress for the table, affecting the primary key columns, at the same time the `CREATE INDEX` statement was issued. (Bug #14117641)

- InnoDB: If a transaction was started with a consistent snapshot, then new indexes were added to the

table while the transaction was in progress, a subsequent `UPDATE` statement could incorrectly encounter the error:

```
ER_TABLE_DEF_CHANGED: insufficient history for index
```

This issue could cause an assertion error in debug builds. (Bug #14036214)

- InnoDB: The server could crash with an assertion error during operations on tables with

`ROW_FORMAT=COMPRESSED`. (Bug #14001972)

- InnoDB: In rare circumstances, during operations on an `InnoDB` table containing foreign keys, pages in

the buffer pool could be evicted but not written to disk, leading to data inconsistency. (Bug #13688491)

- InnoDB: In rare circumstances, MySQL could apply `InnoDB` undo records out of order during a

ROLLBACK of an operation that modified a BLOB column. This issue could cause an assertion error in debug builds:

```
!bpage->file_page_was_freed
```

(Bug #13249921)

- InnoDB: In debug builds, a mismatch in the `InnoDB` `PAGE_FREE` list would cause an assertion. (Bug

#12701488)

- Partitioning: The server now skips pruning of tables (see Partition Pruning) that use a storage engine

which handles its own partitioning internally. The server now also explicitly rejects attempts to use explicit partitioning for such tables. (Bug #14672885)

- Partitioning: When used with a table having multiple columns in its primary key, but partitioned by

`KEY` using a column that was not part of the primary key as the partitioning column, a query using an aggregate function and `DISTINCT` such as `SELECT` `SUM(DISTINCT pk_column_1) FROM table``WHERE pk_column_2 = constant` was not handled correctly. (Bug #14495351)

## MySQL 5.6 Release Notes

- Replication: When using a multithreaded slave, if all worker threads were kept busy, it was possible for

cleanup of an internal MTS circular buffer to fail, resulting in a full buffer and failure of the slave. (Bug#14710881)

- Replication: Executing `FLUSH LOGS` in parallel with `COMMIT` could cause the server to hang. (Bug

#14640486)

- Replication: When invoked while `gtid_mode` was set to `OFF`, the

`SQL_THREAD_WAIT_AFTER_GTIDS()` function waited indefinitely, unless a timeout was specified.

In the latter case, the function could return incorrect values. Now, when `gtid_mode` is `OFF`,`SQL_THREAD_WAIT_AFTER_GTIDS()` always returns `NULL`, as expected. (Bug #14640065)

- Replication: Partially-failed `GRANT` and `REVOKE` statements were not always handled the same way on

the master and the slave. We now log an incident event whenever an error occurs, even if it is only a partial error, with a message stating that manual reconciliation is required. (Bug #14598585)

- Replication: There existed a gap in time between the appending of the current GTID to the server's list

of logged GTIDs and the commit of the transaction by the storage engine. On slow platforms, or when using profiling, this could cause `SELECT` `SQL_THREAD_WAIT_AFTER_GTIDS(gtid)` to return before the data actually reached the database.

Now the current GTID is appended to the logged GTIDs following the commit, which removes this gap and so eliminates a possible source of inconsistency. (Bug #14116526)

- Replication: The error shown when a relay log file was missing from the relay log index file informed

the user only that the log file was not found, but did not specify the exact reason. Now in such cases,the error message returned is `Could not find target log file mentioned in relay log`

```
info in the index file 'index_file_name' during relay log initialization. (Bug
```

#11758505)

- Replication: Following an insert into a nontransactional table that failed due to insufficient disk space,

the server did not properly clean up all pending events, leading to an assert or possibly to other errors.

(Bug #11750014)

- Replication: Backtick (`) characters were not always handled correctly in internally generated SQL

statements, which could sometimes lead to errors on replication slaves or cause failure of restore operations from binary log files. (Bug #66550, Bug #14548159, Bug #29422, Bug #11746883)

- A `DELETE` statement for an `InnoDB` table could write incorrect transaction metadata into a record,

causing the server to halt with an error. To work around this issue, reduce the specified length of the primary key to less than 1K bytes. (Bug #14731482)

- `mysql_secure_installation` could not change the password for an account that had

`password_expired='Y'` in the `mysql.user` table row for that account. (Bug #14726722)

- For an in-place `ALTER TABLE` operation on an `InnoDB` table that produced a duplicate-key error for

`NULL` values, the error message displayed the column default value rather than `NULL`. (Bug #14723364)

- Patches for materialized semijoins caused failures of the query plan interface used by `NDBCLUSTER`.

(Bug #14704659)

- `mysqladmin password` did not work for accounts with an expired password. (The fix for this problem

is limited to accounts with passwords that use native or “old” native hashing. It still does not handle accounts that use SHA-256 password hashing.)As a consequence of this patch, the restricted mode of operation enforced by the server on operations permitted to clients with expired passwords now includes `SET` statements in addition to `SET PASSWORD`.

## MySQL 5.6 Release Notes

This is useful if the account uses a password hashing format that requires `old_passwords` to be set to a value different from its default. (Bug #14698309)

- Repeated execution of a query containing a subquery that used `MAX()` could result in increasing

memory consumption. (Bug #14683676)

- Queries that used a nested join with a subquery in the `FROM` clause and an `ORDER BY ... DESC`

clause could return too few rows. (Bug #14678404)

- With the optimizer tracing enabled, the `INFORMATION_SCHEMA.OPTIMIZER_TRACE` table can be

queried to find tracing information about the last statements. However, for queries for which the results were retrieved from the query cache, this information was not available. (Bug #14665052)

- There was a performance regression for queries using `SELECT ... INTO` user variables and a `WHERE`

condition on one or more of the variables in the `INTO` list. (Bug #14664077)References: This issue is a regression of: Bug #12408412.

- In debug builds, the server could crash because `db_suicide()` failed to handle `SIGABRT` signals. (Bug

#14649493)

- `USE dbname` could fail with `Unknown database` when `dbname` contained multiple backtick (`)

characters. (Bug #14645196)

- Outer joins could execute inefficiently and return incorrect results if joins were pushed down to the

storage engine. (Bug #14644936)

- A prepared statement that referenced views in an `IN` subquery could return different results for different

executions. (Bug #14641759)References: See also: Bug #13773979.

- Within a stored program, memory allocated to hold condition information was not released until program

exit, leading to excessive memory use. (Bug #14640599)

- Attempts to insert, update, delete from, or lock unknown Performance Schema tables failed with an

`ER_TABLEACCESS_DENIED_ERROR` error rather than `ER_NO_SUCH_TABLE`. (Bug #14633008)

- An incomplete result could be stored in the query cache when a query failed with an error (providing

that the query cache was enabled, and was set to a nonzero size). This fix ensures that it is no longer possible for queries that finish with an error to be cached. (Bug #14621700)References: This issue is a regression of: Bug #40264.

- The thread cache implementation worked in LIFO rather than FIFO fashion and could result in a thread

being denied service (although this was a remote possibility). (Bug #14621627)

- The server could crash when registering tables in the query cache for queries that selected from views.

(Bug #14619935)

- With semijoin and materialization optimizations enabled, a query that materialized a `const` table

returned incorrect results when `STRAIGHT_JOIN` was added. (Bug #14609394)

- Index condition pushdown in conjunction with descending index range scan could return incorrect results

if there were multiple ranges in the range scan. (Bug #14604223)

- `EXPLAIN DELETE ... WHERE impossible_condition` could function incorrectly when it was used

in a stored routine. (Bug #14601802)References: This issue is a regression of: Bug #11752097.

## MySQL 5.6 Release Notes

- Small values of `max_sort_length` could produce incorrect results for integer, decimal, floating-point,

or temporal data types. Now `max_sort_length` is ignored for those data types. (Bug #14596888)

- The `configure.pl` script that converts GNU `configure` options to `CMake` equivalents generated

erroneous output for the `--with-client-ldflags` and `--with-mysqld-ldflags` options. It now ignores those options. (Bug #14593123)

- A query with a subquery and `ORDER BY` and `LIMIT` clauses returned fewer rows than expected when

executed using semijoin materialization. (Bug #14580874)

- The server printed excessive `Got error 159 when reading table` messages to the error log

when one transaction attempted to access a table that had been modified by another. (Bug #14579877)

- The optimizer could choose an incorrect execution plan for updates to `InnoDB` tables based on indexes

that use column prefixes. (Bug #14578060)

- Materialization of a subquery in the `FROM` clause could return the wrong number of rows if the subquery

included a `LIMIT` clause. (Bug #14576727)

- In-source builds modified the source file `sql/share/dictionary.txt`. (Bug #14562699)
- Improper memory cleanup could cause the server to exit. (Bug #14536113)
- A query with a subquery in the `JOIN ... ON` clause with an outer reference to a field that was out of

scope could cause the server to crash. (Bug #14498914)

- On Windows, `mysql_plugin` could not find `my_print_defaults`. (Bug #14471052)
- When used in `GRANT` statements, quoted user name or host name values containing leading or trailing

spaces caused privileges to be assigned incorrectly until a `FLUSH PRIVILEGES` statement was issued.

Now, as a result of this fix, quoted name and host identifiers used in a `GRANT` statement are automatically trimmed of any leading and trailing spaces, before privileges are assigned. (Bug#14328259)

- Granting or revoking the `PROXY` privilege caused the server to exit if the server was started with the

`skip_name_resolve` system variable enabled. (Bug #14211140)

- `CREATE USER` and `DROP USER` could fail to flush the privileges, requiring `FLUSH PRIVILEGES` to be

used explicitly. (Bug #13864642)

- On OS X, the `version_compile_machine` system variable did not include the value 64 for server

binaries compiled on a 64-bit system. (Bug #13859866)

- Access to `INFORMATION_SCHEMA` tables through a view could leak memory. (Bug #13734987)
- On Microsoft Windows with CMake 2.6, the build process would not stop if the `create_initial_db`

step failed. (Bug #13713525)

- The test in `mysqld_safe` for the presence of the `--plugin_dir` option and assignment of a default

value to it were performed before the actual argument parsing took place. (Bug #13548161)

- A cached query result was not empty at the end of statement execution as expected. This could occur

when executing queries (with the query cache enabled and set to a nonzero size) where the result was not sent to the client such as those executed by the Event Scheduler, or when executing stored routines containing queries while the server was running in bootstrap mode. (Bug #11755580, Bug #14609893)

- The number of connection errors from a given host as counted by the server was periodically reset, with

the result that `max_connect_errors` was never reached and invalid hosts were never blocked from trying to connect. (Bug #11753779)

## MySQL 5.6 Release Notes

References: See also: Bug #38247, Bug #43006, Bug #45584, Bug #45606.

- The `Range checked for each record` optimization is now used for conditions with outer query

references. (Bug #11750963)

- Random number generation during client authentication consumed excessive CPU. (Bug #66567, Bug

#14555434)

- Metadata locking resulted in excessive contention in read-only workloads involving `InnoDB` tables and a

low number of connections.

Now the set of metadata locks can be partitioned into separate hashes to permit connections accessing different objects to use different locking hashes and reduce contention. The new`metadata_locks_hash_instances` system variable can be used to specify the number of hashes.

(Bug #66473, Bug #14569140)

- On Windows, the Perl version of `mysql_install_db` created system tables in the `mysql` database

that were not populated properly. (Bug #65584, Bug #14181049)

- `ST_Contains()` and `ST_Within()` incorrectly reported that a polygon did not contain itself.

`ST_Equals()` incorrectly returned 0 for polygons that differed only in shifted vertices. (Bug #64653, Bug#13864679)

- `ST_Difference()` could incorrectly produce empty polygons in the result. (Bug #64649, Bug

#13865773)

- `libmysqlclient` did not use symbol versioning. Thanks to Nicholas Bamber for the patch. (Bug

#64386, Bug #13788218)

- The parser rejected legal queries that involved a `UNION` where the right hand side query term has a table

in parenthese. (Bug #54382, Bug #11761854)

- For some queries involving `ORDER BY`, the optimizer chose the wrong index for accessing the table.

(Bug #45969, Bug #11754370, Bug #14338686)

- In debug builds, `vio_read()` printed `errno` rather than `socket_error` to the debug trace. (Bug

#28775, Bug #11746795)
