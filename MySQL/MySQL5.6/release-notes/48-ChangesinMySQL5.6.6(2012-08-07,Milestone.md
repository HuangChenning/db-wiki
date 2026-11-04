---
title: "Changes in MySQL 5.6.6 (2012-08-07, Milestone 9)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=191"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Note This is a milestone release, for use at your own risk. Upgrades between milestone releases (or from a milestone release to a GA release) are not supported.

Significant development changes take place in milestone releases and you may encounter compatibility issues, such as data format changes that require attention in addition to the usual procedure of running `mysql_upgrade`. For example, you may find it necessary to dump your data with `mysqldump` before the upgrade and reload it afterward. (Making a backup before the upgrade is a prudent precaution in any case.)

- Binary Logging
- Configuration Notes
- Deprecation and Removal Notes
- Performance Schema Notes
- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> Binary Logging

- Performance: The server now implements group commit for the binary log: Multiple commits are

grouped in memory, then written and flushed to disk as a group rather than individually. This reduces the number of writes and flushes, improving performance of binary logging. Group commit works for all storage engines. `InnoDB` implements some optimizations to take advantage of group commit capability.

These system variables were added in conjunction with group commit:

- `binlog_order_commits`: Whether to commit transactions in the same order they are written to the

binary log or permit them to be committed in parallel.

- `binlog_max_flush_queue_time`: How long in microseconds to keep reading transactions from the

flush queue before proceeding with the group commit.

- `innodb_flush_log_at_timeout`: Write and flush logs every N seconds.

(WL #5223)

> Configuration Notes

- This MySQL release implements changes to the default values of several server parameters. The

motivation for these changes is to provide better out-of-box performance and to reduce the need for database administrators to change settings manually. These changes are subject to revision in future releases as we gain feedback. (See Changes to Server Defaults.)In some cases, a parameter has a different fixed default value. In other cases, the server autosizes a parameter at startup using a formula based on other related parameters or server host configuration,rather than using a fixed value. For example, the setting for `back_log` is its previous default of 50,adjusted up by an amount proportional to the value of `max_connections`. The idea behind autosizing

## MySQL 5.6 Release Notes

is that when the server has information available to make a decision about a parameter setting likely to be better than a fixed default, it will.

The following table summarizes changes to defaults. For variables that are autosized, the main variable description provides additional detail about the sizing algorithm. See Server System Variables, and InnoDB Startup Options and System Variables. Any of these default settings can be overridden by specifying an explicit value at server startup.

Parameter Old Default New Default`back_log` 50 Autosized using

```
max_connections
binlog_checksum  NONE  CRC32
```

`--binlog-row-event-max-` 1024 8192

```
size
```

`flush_time` 1800 (on Windows) 0

```
innodb_autoextend_increment8  64
```

`innodb_buffer_pool_instances`1 8 (platform dependent)

```
innodb_checksum_algorithm INNODB  CRC32
innodb_concurrency_tickets500  5000
innodb_file_per_table  0  1
innodb_old_blocks_time  0  1000
```

`innodb_open_files` 300 Autosized using

```
innodb_file_per_table,
table_open_cache
innodb_stats_on_metadata ON  OFF
```

`join_buffer_size` 128KB 256KB

```
max_allowed_packet  1MB  4MB
max_connect_errors  10  100
performance_schema  OFF  ON
performance_schema_events_waits_history_long_size10000  Autosized
performance_schema_events_waits_history_size10  Autosized
```

`performance_schema_max_cond_instances`1000 Autosized`performance_schema_max_file_instances`10000 Autosized`performance_schema_max_mutex_instances`1000000 Autosized`performance_schema_max_rwlock_instances`1000000 Autosized`performance_schema_max_table_handles`100000 Autosized`performance_schema_max_table_instances`50000 Autosized

```
performance_schema_max_thread_instances1000  Autosized
```

`sql_mode` '' (empty string) `NO_ENGINE_SUBSTITUTION``sync_master_info` 0 10000`sync_relay_log` 0 10000

## MySQL 5.6 Release Notes

> Parameter Old Default New Default

```
sync_relay_log_info  0  10000
```

With regard to compatibility with previous releases, the most important changes are:

- `innodb_file_per_table` is enabled (previously disabled)
- `innodb_checksum_algorithm` is `CRC32` (previously `INNODB`)
- `binlog_checksum` is `CRC32` (previously `NONE`)

Therefore, if you are upgrading an existing MySQL installation, have not already changed the values of these parameters from their previous defaults, and backward compatibility is a concern, you may want to explicitly set these parameters to their previous defaults. For example, put these lines in the server option file:

```
[mysqld]
innodb_file_per_table=0
innodb_checksum_algorithm=INNODB
binlog_checksum=NONE
```

Those settings preserve compatibility as follows:

- With the new default of `innodb_file_per_table` enabled, `ALTER TABLE` operations following an

upgrade will move `InnoDB` tables that are in the system tablespace to individual `.ibd` files. Using`innodb_file_per_table=0` will prevent this from happening.

- Setting `innodb_checksum_algorithm=INNODB` permits binary downgrades after upgrading to this

release. With a setting of `CRC32`, InnoDB would use checksumming that older MySQL versions cannot use.

- With `binlog_checksum=NONE`, the server can be used as a replication master without causing

failure of older slaves that do not understand binary log checksums.

(WL #6216)

> Deprecation and Removal Notes

- Important Change: `INSERT DELAYED` is now deprecated, and will be removed in a future release. Use

`INSERT` (without `DELAYED`) instead. (Bug #13985071)

- The `YEAR(2)` data type is now deprecated because it is problematic. `YEAR(2)` columns in existing

tables are treated as before, but `YEAR(2)` in new or altered tables are converted to `YEAR(4)`. Support for `YEAR(2)` will be removed entirely in a future MySQL release. For more information, see 2-Digit YEAR(2) Limitations and Migrating to 4-Digit YEAR. (WL #6219)

> Performance Schema Notes

- The Performance Schema is now enabled by default (the `performance_schema` system variable is

enabled by default). To disable it, set `performance_schema=off` at server startup.

In addition, the Performance Schema now automatically sizes the values of several of its parameters at server startup if they are not set explicitly. For example, it sizes the parameters that control the sizes of the events waits tables this way. To see which parameters are sized under this policy, use `mysqld --``verbose --help` and look for those with a default value of −1, or see Performance Schema System Variables.

## MySQL 5.6 Release Notes

For each autosized parameter that is not set at server startup (or is set to −1), the Performance Schema determines how to set its value based on the value of the following system values, which are considered as “hints” about how you have configured your MySQL server:

```
max_connections
open_files_limit
table_definition_cache
table_open_cache
```

To override autosizing for a given parameter, set it a value other than −1 at startup. In this case, the Performance Schema assigns it the specified value.

At runtime, `SHOW VARIABLES` displays the actual values that autosized parameters were set to.

If the Performance Schema is disabled, its autosized parameters remain set to −1 and `SHOW``VARIABLES` displays −1. (WL #6135)

> Security Notes

- These security improvements were implemented:
- MySQL now provides a method for storing authentication credentials encrypted in an option file named

`.mylogin.cnf`. To create the file, use the `mysql_config_editor` utility. The file can be read later by MySQL client programs to obtain authentication credentials for connecting to a MySQL server.

`mysql_config_editor` writes the `.mylogin.cnf` file using encryption so the credentials are not stored as clear text, and its contents when decrypted by client programs are used only in memory.

In this way, passwords can be stored in a file in non-cleartext format and used later without ever needing to be exposed on the command line or in an environment variable. For more information, see mysql_config_editor — MySQL Configuration Utility.

The `.mylogin.cnf` file can contain multiple sets of options, known as “login paths.” This makes it easy to set up multiple “personalities” for connecting to different MySQL servers. Any of these can be selected by name later using the `--login-path` option when you invoke a client program. See Command-Line Options that Affect Option-File Handling.

- MySQL now supports stronger encryption for user account passwords, available through an

authentication plugin named `sha256_password` that implements SHA-256 password hashing. This plugin is built in, so it is always available and need not be loaded explicitly. For more information,including instructions for creating accounts that use SHA-256 passwords, see SHA-256 Pluggable Authentication.

Other changes associated with the introduction of the `sha256_password` plugin:

- The `old_passwords` system variable previously permitted values of 1 or 0 to control whether “old”

or “new” MySQL native password hashing was used by the `CREATE USER` and `GRANT` statements and the `PASSWORD()` function. Now `old_passwords` permits a value of 2 to select use of SHA-256 password hashing.

Note Previously, `old_passwords` permitted values of `OFF` or `ON` as synonyms for 0 or 1. That is no longer true.

- SHA-256 password hashing (`old_passwords=2`) uses a random salt value, which makes the

result from `PASSWORD()` nondeterministic. Consequently, statements that use this function are no longer safe for statement-based replication and cannot be stored in the query cache.

## MySQL 5.6 Release Notes

- If MySQL is built with OpenSSL, RSA encryption can be used to transmit passwords

during the client connection process. The `sha256_password_private_key_path` and`sha256_password_public_key_path` system variables permit the private and public key files to be named on the server side. The `Rsa_public_key` status variable displays the public key value.

The `mysql` and `mysqltest` clients support a `--server-public-key` option permitting the public key file to be specified explicitly when connecting to the server. (This option is implemented through a new `MYSQL_SERVER_PUBLIC_KEY` option to the `mysql_options()` C API function.)MySQL Connector support: Connectors that use the C client library should work with`sha256_password` with no changes. Connectors that implement the authentication process for themselves must be updated to account for changes in the client/server protocol.

- The server now has a `--default-authentication-plugin` option to specify the default

plugin to associate with new accounts for which no plugin is named explicitly. Permitted values are `mysql_native_password` (use MySQL native passwords; this is the default value) and`sha256_password` (use SHA-256 passwords). This option also changes the initial `old_passwords`value to be consistent with the password hashing method required by the default plugin, if necessary.

Note If you use this option to change the default authentication method to a value other than `mysql_native_password`, clients older than MySQL 5.5.7 will no longer be able to connect because they will not understand the change to the authentication protocol.

- The `mysql.user` table now has a `password_expired` column to enable DBAs to expire account

passwords and require users to reset their password. The default `password_expired` value is `'N'`,but can be set to `'Y'` with the new `ALTER USER` statement. After an account's password has been expired, all operations performed by the account in subsequent connections to the server result in an error until the user issues a `SET PASSWORD` statement to establish a new account password. For more information, see ALTER USER Statement, and Server Handling of Expired Passwords.

If you upgrade to this MySQL release from an earlier version, you must run `mysql_upgrade` (and restart the server) to incorporate this change into the `mysql` database.

Caution Update: `ALTER USER` also set the `Password` column to the empty string,so do not use this statement in 5.6.6. This problem has been fixed in MySQL

5.6.7.

- MySQL now has provision for checking password security:
- In statements that assign a password supplied as a cleartext value, the value is checked

against the current password policy and rejected if it is weak (the statement returns an`ER_NOT_VALID_PASSWORD` error). This affects the `CREATE USER`, `GRANT`, and `SET PASSWORD`statements. Passwords given as arguments to the `PASSWORD()` and `OLD_PASSWORD()` functions are checked as well.

## MySQL 5.6 Release Notes

- The strength of potential passwords can be assessed using the new

`VALIDATE_PASSWORD_STRENGTH()` SQL function, which takes a password argument and returns an integer from 0 (weak) to 100 (strong).

Both capabilities are implemented by the `validate_password` plugin. If the plugin is not installed,the affected statements and `PASSWORD()` and `OLD_PASSWORD()` work as before (no password checking), and `VALIDATE_PASSWORD_STRENGTH()` always returns 0.

The `validate_password` plugin also implements a set of system variables corresponding to the parameters that control password checking. If the plugin is installed, you can modify these variables to configure the password policy.

The `validate_password` plugin is written using the MySQL plugin API, which has been extended to support writing password-validation plugins.

For more information, see The Password Validation Plugin. For information about writing password-checking plugins, see Writing Password-Validation Plugins.

- `mysql_upgrade` now produces a warning if it finds user accounts with passwords hashed with

the older pre-4.1 hashing method. Such accounts should be updated to use more secure password hashing. See Password Hashing in MySQL(Bug #65461, Bug #14136939, WL #2739, WL #2392, WL #5602, WL #5603)

- For the `WITH_SSL` CMake option, `no` is no longer a permitted value or the default value. The default is

now `bundled`. Consequently, MySQL now is always built with SSL support.

> Functionality Added or Changed

- Incompatible Change: It is now explicitly disallowed to assign the value `DEFAULT` to stored procedure

or function parameters or stored program local variables (for example with a `SET var_name =``DEFAULT` statement). This was not previously supported, or documented as permitted, but is flagged as an incompatible change in case existing code inadvertently used this construct. It remains permissible to assign `DEFAULT` to system variables, as before, but assigning `DEFAULT` to parameters or local variables now results in a syntax error.

After an upgrade to MySQL 5.6.6 or later, existing stored programs that use this construct produce a syntax error when invoked. If a `mysqldump` file from 5.6.5 or earlier is loaded into 5.6.6 or later, the load operation fails and affected stored program definitions must be changed. (WL #6230)

- Incompatible Change: The `--safe-mode` server option has been removed. (WL #5185, WL #6311)
- Important Change; Partitioning: MySQL nows supports partition lock pruning, which allows for many

DDL and DML statements against partitioned tables using `MyISAM` (or another storage engine that employs table-level locking) to lock only those partitions directly affected by the statement. These statements include (but are not limited to) many `SELECT`, `SELECT ... PARTITION`, `UPDATE`,`REPLACE`, `INSERT`, and other statements. This enhancement improves especially the performance of many such statements when used with tables having many (32 or more) partitions. For a complete list of affected statements with particulars, and other information, see Partitioning and Locking. (Bug #37252,Bug #11748732)

- Important Change; Replication: It is now possible, in the event that a multithreaded slave fails while

running with the `--relay-log-recovery` option, to switch it safely to single-threaded mode despite the presence of any gaps with unprocessed transactions in the relay log. To accomplish this, you can now use `START SLAVE [SQL_THREAD] UNTIL SQL_AFTER_MTS_GAPS` to cause the slave SQL

## MySQL 5.6 Release Notes

threads to run until no more such gaps are found in the relay log. Once this statement has completed,you can change the `slave_parallel_workers` system variable, and (if necessary) issue a `CHANGE``MASTER TO` statement before restarting the slave. (Bug #13893363)References: See also: Bug #13893310.

- Important Change; Replication: `INSERT ON DUPLICATE KEY UPDATE` is now marked as unsafe

for statement-based replication if the target table has more than one primary or unique key. For more information, see Determination of Safe and Unsafe Statements in Binary Logging. (Bug #58637, Bug#11765650, Bug #13038678)

- Important Change; Replication: The `SHOW BINARY LOGS` statement (and its equivalent `SHOW`

`MASTER LOGS`) may now be executed by a user with the `REPLICATION CLIENT` privilege. (Formerly,the `SUPER` privilege was necessary to use either form of this statement.) (WL #6236)

- Important Change: In MySQL, the `TIMESTAMP` data type differs in nonstandard ways from other data

types:

- `TIMESTAMP` columns not explicitly declared with the `NULL` attribute are assigned the `NOT NULL`

attribute. (Columns of other data types permit `NULL` values if not explicitly declared with the `NOT NULL`attribute.) Setting such a column to `NULL` sets it to the current timestamp.

- The first `TIMESTAMP` column in a table, if not declared with the `NULL` attribute or an explicit `DEFAULT`

or `ON UPDATE` attribute, is automatically assigned the `DEFAULT CURRENT_TIMESTAMP` and `ON``UPDATE CURRENT_TIMESTAMP` attributes.

- `TIMESTAMP` columns following the first one, if not declared with the `NULL` attribute or an explicit

`DEFAULT` attribute, are automatically assigned `DEFAULT '0000-00-00 00:00:00'` (the “zero”timestamp). For inserted rows that specify no explicit value for such a column, the column is assigned`'0000-00-00 00:00:00'` and no warning occurs.

Those nonstandard behaviors remain the default for `TIMESTAMP` but now are deprecated and this warning appears at startup:

```
[Warning] TIMESTAMP with implicit DEFAULT value is deprecated.
Please use --explicit_defaults_for_timestamp server option (see
documentation for more details).
```

As indicated by the warning, to turn off the nonstandard behaviors, enable the new`explicit_defaults_for_timestamp` system variable at server startup. With this variable enabled,the server handles `TIMESTAMP` as follows instead:

- `TIMESTAMP` columns permit `NULL` values if not explicitly declared with the `NOT NULL` attribute. Setting

such a column to `NULL` sets it to `NULL`, not the current timestamp.

- No `TIMESTAMP` column is assigned the `DEFAULT CURRENT_TIMESTAMP` or `ON UPDATE`

`CURRENT_TIMESTAMP` attributes automatically. Those attributes must be explicitly specified.

- `TIMESTAMP` columns declared as `NOT NULL` and without an explicit `DEFAULT` attribute are treated as

having no default value. For inserted rows that specify no explicit value for such a column, the result depends on the SQL mode. If strict SQL mode is enabled, an error occurs. If strict SQL mode is not enabled, the column is assigned the implicit default of `'0000-00-00 00:00:00'` and a warning occurs. This is similar to how MySQL treats other temporal types such as `DATETIME`.

To upgrade servers used for replication, upgrade the slaves first, then the master. Replication between the master and its slaves should work provided that all use the same value of

```
explicit_defaults_for_timestamp:
```

## MySQL 5.6 Release Notes

1. Bring down the slaves, upgrade them, configure them with the desired value of

`explicit_defaults_for_timestamp`, and bring them back up.

The slaves will recognize from the format of the binary logs received from the master that the master is older (predates the introduction of `explicit_defaults_for_timestamp`) and that operations on `TIMESTAMP` columns coming from the master use the old `TIMESTAMP` behavior.

2. Bring down the master, upgrade it, and configure it with the same

`explicit_defaults_for_timestamp` value used on the slaves, and bring it back up.

(Bug #63034, Bug #13344629, Bug #55131, Bug #11762529, WL #6292)

- Performance; InnoDB: Many DDL operations on `InnoDB` tables can now be performed online, without

making the tables unavailable for queries. Some operations, such as creating or dropping indexes, even allow DML statements (`INSERT`, `UPDATE`, `DELETE`) on the table while the operation is in progress. A single online DDL operation can also take the place of a sequence of statements, such as several `DROP``INDEX` statements, `ALTER TABLE ... ADD COLUMN`, and then several `CREATE INDEX` statements.

See InnoDB and Online DDL for full details.

An additional effect of this change occurs for consistent-read transactions that try to re-read data from a table which was changed by `ALTER TABLE` in another session. Instead of receiving an empty set, the transaction will receive an error (`ER_TABLE_DEF_CHANGED`, “Table definition has changed, please retry transaction”). (Bug #58368, Bug #11765404, Bug #11872643, Bug #12325508, Bug #11765266, Bug#60689, WL #5526, WL #5545, WL #6251, WL #6255)

- Performance; InnoDB: The persistent statistics feature for `InnoDB` tables is now enabled

by default, and can be controlled at the level of individual tables. This feature involves the configuration options `innodb_stats_persistent`, `innodb_stats_auto_recalc`, and`innodb_stats_persistent_sample_pages`, and the clauses `STATS_PERSISTENT`,

```
STATS_AUTO_RECALC, and STATS_SAMPLE_PAGES of the CREATE TABLE and ALTER TABLE
```

statements. See Configuring Persistent Optimizer Statistics Parameters for usage details. (WL #6175,WL #6189)

- Performance; InnoDB: The MySQL server now includes the widely used `memcached` in-memory

caching system, and a plugin that allows fast NoSQL-style access to `InnoDB` tables through the`memcached` protocol. This access method avoids the overhead of SQL parsing and constructing a query optimization plan. You can store the underlying data in a single `InnoDB` table, or spread it across multiple tables. You can read and write data through both `memcached` and SQL. For example, you can do fast single-key lookups through `memcached` `get` calls, and do statistical reports across all the data through SQL.

Several configuration options let you fine-tune this system, in particular to balance raw performance against durability and consistency of data. The main new configuration

```
options are daemon_memcached_option, daemon_memcached_r_batch_size,
daemon_memcached_w_batch_size, innodb_api_trx_level, innodb_api_enable_mdl, and
innodb_api_enable_binlog.
```

See InnoDB memcached Plugin for full details. (WL #5824, WL #6218)

- InnoDB: For systems with constant heavy workloads, or workloads that fluctuate widely,

several new configuration options let you fine-tune the flushing behavior for `InnoDB`

```
tables: innodb_adaptive_flushing_lwm, innodb_max_dirty_pages_pct_lwm,
```

`innodb_max_io_capacity` (changed in subsequent point releases to `innodb_io_capacity_max`),and `innodb_flushing_avg_loops`. These options feed into an improved formula used by the`innodb_adaptive_flushing` option. See Configuring Buffer Pool Flushing. (WL #5666)

## MySQL 5.6 Release Notes

- InnoDB: `InnoDB` tables now support the notion of “transportable tablespaces”, allowing `.ibd` files to be

exported from a running MySQL instance and imported into another running instance. The `FOR EXPORT`clause of the `FLUSH TABLES` statement writes any unsaved changes from `InnoDB` memory buffers to the `.ibd` file. After copying the `.ibd` file and a separate metadata file to the other server, you can use the `DISCARD TABLESPACE` and `IMPORT TABLESPACE` clauses of the `ALTER TABLE` statement to bring the table data into a different MySQL instance.

For more information, see Importing InnoDB Tables. (WL #5522, WL #6168, WL #6169)

- InnoDB: `InnoDB` now supports the `DATA DIRECTORY='directory'` clause of the `CREATE TABLE`

statement, which permits creating tables outside the data directory. For more information, see Creating Tables Externally. (WL #5980)

- Replication: The `STOP SLAVE` option `SQL_BEFORE_GTIDS` did not function correctly, and the

`SQL_AFTER_GTIDS` option for the same statement did not function at all. (Bug #13810456)

- Replication: Added the `slave_rows_search_algorithms` system variable for `mysqld`,

which determines the search algorithms used for finding matches for slave updates when`slave_allow_batching` is enabled, including whether or not table or index hashing is used with searches employing a primary or unique key, some other key, or no key.

- The Performance Schema has a new system variable,

`performance_schema_session_connect_attrs_size`, and new status variable,`Performance_schema_session_connect_attrs_lost`. The system variable is the amount of preallocated memory per thread reserved to hold connection attribute key/value pairs. If the aggregate size of connection attribute data sent by a client is larger than this amount, the Performance Schema truncates the attribute data and increments the status variable. See Performance Schema Connection Attribute Tables. (Bug #14076427)

- yaSSL was upgraded from version 1.7.2 to 2.1.4. (Bug #13713205)

References: See also: Bug #13706828.

- The optimizer's cost model for disk-sweep Multi-Read Range (DS-MRR) has been improved. The

improved cost model makes it more likely that DSMRR will be used for queries that read much data from disk. (WL #6082)

- Previously, the default value for the `bind_address` system variable was `0.0.0.0`, which causes the

server to accept TCP/IP connections on all server host IPv4 interfaces. To make it easier to use IPv6 connections without special configuration, the default `bind_address` value now is *. This is similar to`0.0.0.0`, but causes the server to also accept TCP/IP connections on all IPv6 interfaces if the server host supports IPv6. (Another way to accept IPv4 and IPv6 connections is by using `bind_address=::`,but in this case an error occurs if the server host does not support IPv6.) (WL #6301)

- It is now possible for client programs to pass connection attributes to the server in the form of

key/value pairs. Attributes are manipulated using the `MYSQL_OPT_CONNECT_ATTR_RESET`and `MYSQL_OPT_CONNECT_ATTR_DELETE` options for the `mysql_options()` C API function, and the `MYSQL_OPT_CONNECT_ATTR_ADD` option for the new `mysql_options4()`function. Connection attributes are exposed through the `session_connect_attrs` and`session_account_connect_attrs` Performance Schema tables.

If you upgrade to this MySQL release from an earlier version, you must run `mysql_upgrade` (and restart the server) to incorporate these changes into the `performance_schema` database.

For more information, see C API Function Reference, and MySQL Performance Schema. (WL #5924)

## MySQL 5.6 Release Notes

- Previously, for semijoin processing the outer query specification was limited to simple table scans or

inner joins using comma syntax, and view references were not possible. Now outer join and inner join syntax is permitted in the outer query specification, and the restriction that table references must be base tables has been lifted. (WL #5561)

- To improve scalability by reducing contention among sessions for the global lock on the open tables

cache, the cache now can be partitioned into several smaller cache instances. A session now need lock only one instance to access it for DML statements. This segments cache access among instances,permitting higher performance for operations that need to use the cache when many there are many sessions accessing tables. (DDL statements still require a lock on the entire cache, but such statements are much less frequent than DML statements.)A new system variable, `table_open_cache_instances`, permits control over the number of cache instances. Each instance has a size of `table_open_cache` / `table_open_cache_instances`. By default, the number of instances is 1.

Three new status variables provide information about the operation of the open tables cache.

`Table_open_cache_hits` and `Table_open_cache_misses` indicate the number of hits and misses or lookups in the cache. `Table_open_cache_overflows` indicates how many times, after a table is opened or closed, an instance has an unused entry and the size of the instance is larger than

```
table_open_cache / table_open_cache_instances. (WL #5772)
```

- The generic “procedure API” has been removed from the server. This was formerly present as a means

of writing server procedures, but went unused except for `PROCEDURE ANALYSE()`. Removing the interface simplifies aspects of the internal procedure representation that were related to code no longer in the server but had a negative effect on its operation, in the sense that these aspects hindered the ability of the optimizer to perform better on more common query types. In addition, this code hindered future optimizer development and its removal will have benefit that development.

`PROCEDURE ANALYSE()` remains available, but is no longer implemented using a public interface.

(For information, see Using PROCEDURE ANALYSE.) One consequence of removing the procedure interface is that `EXPLAIN SELECT ... PROCEDURE ANALYSE()` now works where previously it produced an error. (WL #6242)

> Bugs Fixed

- Incompatible Change: Metadata was handled incorrectly for objects such as tables or views that were

used in a stored program. Metadata for each such object was gathered at the beginning of program execution, but not updated if DDL statements modified the object during program execution (or modified it between executions of the program if the program remained in the stored program cache). This resulted in mismatches between the actual object structure and the structure the stored program believed the object to have during execution, and caused problems such as data errors or server crashes.

Now metadata changes to objects used in a stored program are detected during execution and affected statements within the program are reparsed so that they use the updated metadata.

Example: Suppose that a stored program executes this statement in a loop and that the columns in the table `t1` are altered during loop execution:

```
SELECT * FROM t1;
```

Previously, errors occurred because program execution did not detect that `SELECT *` evaluates to a different set of columns after the change. Now the table change is detected and the `SELECT` is reparsed to determine the new set of columns.

## MySQL 5.6 Release Notes

Reparsing occurs for other cases as well, such as t1 being changed from a base table to a view or a`TEMPORARY` table. For more information, see Caching of Prepared Statements and Stored Programs.

There is a possible incompatibility regarding the new behavior: Application code that assumed the previous behavior and implemented a workaround may need to be changed.

Other instances of corrected problems:

- `SELECT *` within a stored program could fail for `TEMPORARY` tables created within the program using

prepared statements.

- “Unknown column” errors or bad data could result from changing the set of columns in a table used

within a stored program between executions of the program or while the table was used within a program loop. Errors could also occur under similar circumstances for a view if the view definition was changed, for a `TEMPORARY` table if the table was dropped.

- Failure of triggers to notice metadata changes in objects accessed within the program could cause

trigger malfunction.

- Failure of a stored program to notice metadata changes in objects accessed within the program could

cause replication to fail.

(Bug #61434, Bug #12652835, Bug #55678, Bug #11763018, Bug #64574, Bug #13840615, Bug#33843, Bug #11747732, Bug #33289, Bug #11747626, Bug #33255, Bug #11747619, Bug #33000, Bug#11747566, Bug #27011, Bug #11746530, Bug #33083, Bug #11747581, Bug #32868, Bug #11747537,Bug #12257, Bug #11745236, WL #4179)

- Important Change; NDB Cluster: `mysqld_safe` now traps Signal 13 (`SIGPIPE`) so that this signal no

longer kills the MySQL server process. (Bug #33984)

- Performance; InnoDB; Partitioning: The statistics used by the optimizer for queries against partitioned

`InnoDB` tables were based only on the first partition of each such table, leading to use of the wrong execution plan. (Bug #13694811)References: This issue is a regression of: Bug #11756867.

- Performance; InnoDB: Improved the efficiency of `InnoDB` code with regard to CPU cache coherency.

(Bug #14034087)

- Performance; InnoDB: Improved the efficiency of the system calls to get the system time to record the

start time for a transaction. This fix reduces potential cache coherency issues that affected performance.

(Bug #13993661)

- Performance; InnoDB: Improved the algorithm related to adaptive flushing. This fix increases the rate

of flushing in cases where compression is used and the data set is larger than the buffer pool, leading to eviction. (Bug #13990648, Bug #65061)

- Performance; InnoDB: Improved the efficiency of the `COMMIT` operation for `InnoDB` tables, by reducing

the potential for context switching and acquiring/re-acquiring mutexes while the operation is in progress.

(Bug #13989037)

- Performance; InnoDB: The order in which flushes are performed when the

`innodb_flush_neighbors` configuration option is enabled was improved. The algorithm makes the neighbor-flushing technique faster on HDD storage, while reducing the performance overhead on SSD storage. (`innodb_flush_neighbors` typically is not needed for SSD hardware.) (Bug #13798956)

## MySQL 5.6 Release Notes

- Performance; InnoDB: This fix improves the speed of `DROP TABLE` for `InnoDB` tables by removing

a scan of the buffer pool to remove entries for the adaptive hash index. This improvement is most noticeable on systems with very large buffer pools and the `innodb_adaptive_hash_index` option enabled. (Bug #13704145, Bug #64284)

- Performance; Replication: All changes made as part of a given transaction are cached; when the

transaction is committed, the contents of this cache are written to the binary log. When using global transaction identifiers, the GTID identifying this transaction must be the first event among all events in the cache belonging to the transaction.

Previously, a portion of the cache was preallocated as a buffer when the transaction began; upon commit it was completed with a valid GTID. However, because it was not possible to perform a seek in the cache, it was necessary to flush it to a temporary file, and then seek within this file. When the cache buffer is not big enough to accommodate all changes comprising a given transaction, it swapped the data to disk, then reinitialized the cache to have the buffer properly filled with the correct data again.

The buffer was actually flushed and the cache reinitialized every time a GTID event was written, even in those cases in which all events making up a given transaction fit within the cache buffer, which could negatively impact the performance of binary logging (and thus replication) when using GTIDs.

Now the cache is reinitialized only when it is actually necessary—in other words, only when the cache is in fact swapped to disk.

In addition, the fix for this issue addresses a missing unlock operation when the server failed to write an empty transaction group and reduces the amount of code needed for prepending the GTID to the contents of the cache before flushing the cache to disk. (Bug #13877432)References: See also: Bug #13738296.

- Performance: Within stored programs, the overhead of making statements log friendly was incurred

even when the corresponding log was not enabled. (Bug #12884336)

- Performance: The `MD5()` and `SHA1()` functions had excessive overhead for short strings. (Bug

#49491, Bug #11757443, Bug #60227, Bug #14134662)

- InnoDB; Replication: When binary log statements were replayed on the slave, the `Com_insert`,

`Com_update`, and `Com_delete` counters were incremented by `BEGIN` statements initiating transactions affecting `InnoDB` tables but not by `COMMIT` statements ending such transactions. This affected these statements whether they were replicated or they were run using `mysqlbinlog`. (Bug #12662190)

- InnoDB: Dropping an `InnoDB` temporary table could leave behind the `.ibd` file if the table was created

with the `innodb_file_per_table` setting enabled. On Windows systems, this could cause an additional problem: repeated attempts to drop the file for 2000 seconds. In addition to resolving the incorrect path name used to drop the file, this fix also limits the retry loop to 10 seconds, for example if the file cannot be removed because it is locked by a backup process. (Bug #14169459)

- InnoDB: When importing an `InnoDB` tablespace representing a compressed table, unnecessary

checksum calculations were being performed. (Bug #14161424)

- InnoDB: If MySQL crashed during an `ALTER TABLE t DISCARD TABLESPACE` operation, it could

leave `InnoDB` in a state where it crashes at the next startup. The error message was:

```
InnoDB: Error: a record lock wait happens in a dictionary operation!
```

(Bug #14146981)

- InnoDB: A race condition could cause a crash during an online `CREATE INDEX` statement for an

`InnoDB` table. This bug only affected very small tables. It required a DML operation to be in progress

## MySQL 5.6 Release Notes

for the table, affecting the primary key columns, at the same time the `CREATE INDEX` statement was issued. (Bug #14117641)

- InnoDB: An assertion error could occur if an XA transaction was created within a session designated as

read-only. (Bug #14108709)

- InnoDB: If a row was deleted from an `InnoDB` table, then another row was re-inserted with the same

primary key value, an attempt by a concurrent transaction to lock the row could succeed when it should have waited. This issue occurred if the locking select used a `WHERE` clause that performed an index scan using a secondary index. (Bug #14100254, Bug #65389)

- InnoDB: This fix improves the accuracy of the data in the `INFORMATION_SCHEMA` table

`innodb_metrics` for systems with `innodb_buffer_pool_instances` set to greater than 1. The improved information applies to the number of pages flushed from the buffer pool, specifically these entries in the table:

```
buffer_flush_batch_total_pages
buffer_flush_neighbor_total_pages
buffer_flush_adaptive_total_pages
buffer_flush_sync_total_pages
buffer_flush_background_total_pages
buffer_LRU_batch_total_pages
```

(Bug #14037167)

- InnoDB: In a transaction using the `REPEATABLE READ` isolation level, an `UPDATE` or `DELETE` statement

for an `InnoDB` table could sometimes overlook rows recently committed by other transactions. As explained in Consistent Nonlocking Reads, DML statements within a `REPEATABLE READ` transaction apply to rows committed by other transactions, even if a query could not see those rows. (Bug#14007649, Bug #65111)

- InnoDB: During an `ANALYZE TABLE` statement for an `InnoDB` table, the server could hang (in non-

debug builds), or an assertion error could occur, indicating recursive acquisition of a lock (in debug builds). (Bug #14007109)

- InnoDB: An assertion could be raised if an `InnoDB` table was moved to a different database using

`ALTER TABLE ... RENAME` while the database was being dropped by `DROP DATABASE`. (Bug#13982017)

- InnoDB: Querying the `INFORMATION_SCHEMA.INNODB_TRX` or related tables while the server was

running a heavy `InnoDB` workload could cause a crash, with messages in the error log referring to the function `fetch_data_into_cache_low`. This issue arose during new feature work and only affected MySQL 5.6. (Bug #13966453)

- InnoDB: Fixes a recently introduced issue with `InnoDB` persistent statistics, that could cause a crash

(non-debug builds) or assertion error (debug builds). (Bug #13946118)

- InnoDB: Including a % character in a query using an `InnoDB` `FULLTEXT` index could cause a crash.

(`FULLTEXT` indexes for `InnoDB` tables are a new feature, still under development.) (Bug #13940669,Bug #64901)

- InnoDB: Using the `KILL` statement to terminate a query could cause an unnecessary message in the

error log:

```
[ERROR] Got error -1 when reading table table_name
```

(Bug #13933132)

## MySQL 5.6 Release Notes

- InnoDB: When a table was renamed, the `InnoDB` persistent statistics were not associated with the new

table name. (Bug #13920437)

- InnoDB: If the server crashed while dropping an `InnoDB` temporary table or an index on a temporary

table, further errors could occur during crash recovery, preventing the server from restarting. (Bug#13913670)

- InnoDB: A `FULLTEXT` query for an `InnoDB` table could filter the search terms incorrectly if a term using

the minus operator was followed by another term using the plus operator. (Bug #13907075)

- InnoDB: The `performance_schema` counters for `InnoDB` RW-locks did not record some cases where

mini-transactions acquired locks. (Bug #13860722)

- InnoDB: Deleting a huge amount of data from `InnoDB` tables within a short time could cause the

purge operation that removes delete-marked records to stall. This issue could result in unnecessary disk space use, but does not cause any problems with data integrity. If this issue causes a disk space shortage, restart the server to work around it. This issue is only likely to occur on 32-bit platforms. (Bug#13847885)

- InnoDB: A slave server in a replication configuration could exit while creating an `InnoDB` temporary

table. (Bug #13838761)

- InnoDB: The server could crash when using the `SAVEPOINT` statement in conjunction with `InnoDB`

tables containing `FULLTEXT` indexes. (Bug #13831840)

- InnoDB: With the `innodb_force_recovery` configuration option set to 2 or greater, a shutdown could

hang after the message:

```
InnoDB: Waiting for purge thread to be suspended
```

This issue was introduced during recent changes within the MySQL 5.6 development cycle. (Bug#13830371)

- InnoDB: Running concurrent bulk inserts on a server with `auto_increment_offset=1`,

`auto_increment_increment` greater than 1, and `innodb_autoinc_lock_mode=1` could result in intermittent errors like the following, even with the primary key set to auto_increment and omitted from the `INSERT` statement:

```
Duplicate entry 'value' for key 'PRIMARY'
```

The workaround was to set `auto_increment_offset=1` or `innodb_autoinc_lock_mode=0`(“traditional”). (Bug #13817703, Bug #61209)

- InnoDB: The server could halt with an assertion error when DDL and DML operations were run on the

same `InnoDB` table simultaneously:

```
InnoDB: Error: a record lock wait happens in a dictionary operation!
```

This fix stems from the online DDL feature in MySQL 5.6. (Bug #13641926)

- InnoDB: During an `ALTER TABLE` statement to create a primary key for an `InnoDB` table, some column

characteristics could be set incorrectly, leading to errors during subsequent queries. The incorrect data could be the maximum length for a column prefix, or the state of the `NOT NULL` flag.

In MySQL 5.1, this fix applies to the InnoDB Plugin, but not the built-in InnoDB storage engine. (Bug#13641275)

## MySQL 5.6 Release Notes

- InnoDB: An `ALTER TABLE` statement for an `InnoDB` table that dropped one index and create

another could fail with an error code 1280, and displaying the wrong index name in the message. (Bug#13029445, Bug #62544)

- InnoDB: If the `innodb_undo_tablespaces` and `innodb_undo_logs` configuration options were

specified to refer to separate undo tablespaces, and the associated tablespaces did not exist, that error condition was not being correctly detected during startup. (Bug #13016100)

- InnoDB: The error handling and message was improved for attempting to create a foreign key with a

column referencing itself. The message suggested a potential problem with the data dictionary, when no such problem existed. (Bug #12902967)

- InnoDB: For an `InnoDB` table with a trigger, under the setting `innodb_autoinc_lock_mode=1`,

sometimes auto-increment values could be interleaved when inserting into the table from two sessions concurrently. The sequence of auto-increment values could vary depending on timing, leading to data inconsistency in systems using replication. (Bug #12752572, Bug #61579)

- InnoDB: An `ALTER TABLE` with both `IGNORE` and `ADD UNIQUE KEY` clauses produced an error if

duplicates were found, rather than removing all duplicate rows after the first one. With this fix, the `ALTER``TABLE IGNORE` syntax automatically enables the `ALGORITHM=COPY` clause if the `ALTER TABLE`statement creates an index. (Bug #12622150)

- InnoDB: When data was removed from an `InnoDB` table, newly inserted data might not reuse the freed

disk blocks, leading to an unexpected size increase for the system tablespace or `.ibd` file (depending on the setting of `innodb_file_per_table`. The `OPTIMIZE TABLE` could compact a `.ibd` file in some cases but not others. The freed disk blocks would eventually be reused as additional data was inserted. (Bug #11766634, Bug #59783)

- InnoDB: The `CHECK TABLE` statement could fail for a large `InnoDB` table due to a timeout value of 2

hours. For typical storage devices, the issue could occur for tables that exceeded approximately 200 or 350 GB, depending on I/O speed. The fix relaxes the locking performed on the table being checked,which makes the timeout less likely. It also makes `InnoDB` recognize the syntax `CHECK TABLE QUICK`,which avoids the possibility of the timeout entirely. (Bug #11758510, Bug #50723)

- InnoDB: Full-text search in `InnoDB` tried to follow foreign key references without keeping track of which

ones it had already seen. With circular and other complex setups, this could loop forever or a very long time, leading to the appearance of the query thread hanging. (Bug #64274, Bug #13701973)

- Partitioning: If a partitioned table `t1` was created using the `ROW_FORMAT` option, attempting to perform

`ALTER TABLE t1 EXCHANGE PARTITION ... WITH TABLE t2` failed with the error `Tables have``different definitions` even if the definition for table `t2` was identical to that for `t1`. This occurred because a check was made for an explicit `ROW_FORMAT` setting in the table definition, and if this was set,the operation was rejected.

Now in such cases the row format actually used for each table is checked explicitly and the `EXCHANGE``PARTITION` operation is permitted to execute if both row formats are the same. (Bug #11894100)

- Partitioning: The `PARTITION_COMMENT` column of the `INFORMATION_SCHEMA.PARTITIONS` table

truncated partition comments, displaying only the first 80 characters.

As part of the fix for this issue, the maximum length for a partition comment is now set at 1024 characters, and this width is honored by `INFORMATION_SCHEMA.PARTITIONS.PARTITION_COMMENT`.

(Bug #11748924, Bug #37728)

- Replication: When a complete global transaction spanned relay logs such that only its GTID appeared

in a given relay log while the body of the transaction (including `BEGIN` and `COMMIT` statements)

## MySQL 5.6 Release Notes

appeared in the next relay log, the GTID was interpreted incorrectly as belonging to an empty group.

(Bug #14136654)

- Replication: It was possible in some cases when using semisynchronous replication for log rotation to

take place before an ongoing transaction was committed or rolled back. (Bug #14123372)

- Replication: If the relay logs were removed after the server was stopped, without stopping replication

first, the server could not be started correctly. (Bug #14029212, Bug #65152)References: See also: Bug #13971348.

- Replication: The `--bootstrap` option for `mysqld` is used by `mysql_install_db` when it initializes

the system tables. Now, whenever this option is used, GTIDs (see Replication with Global Transaction Identifiers) and replication are automatically disabled. (Bug #13992602)

- Replication: It was theoretically possible for concurrent execution of more than one instance of `SHOW`

`BINLOG EVENTS` to crash the MySQL Server. (Bug #13979418)

- Replication: If errors were encountered while trying to initialize the `mysql.slave_master_info` or

`mysql.slave_relay_log_info` tables, the server refused to start. Now in such cases, the warning

```
message Error while checking replication metadata. This might also happen when
doing a live upgrade from a version that did not make use of the replication
```

`metadata tables` is issued to advise the user that this has happened, but the server is permitted to continue starting. (Bug #13893363)

- Replication: The text for the error `ER_AUTO_POSITION_REQUIRES_GTID_MODE_ON` referred to

`AUTO_POSITION = 1` although this should be `MASTER_AUTO_POSITION = 1`. The text has been corrected. (Bug #13868465)

- Replication: A `CHANGE MASTER TO` statement could alter the effective value of `relay_log_purge`.

In addition, the `relay_log_recovery` system variable is now read-only, and can be changed only by starting the server with `--relay-log-recovery`. (Bug #13840948)

- Replication: When `binlog_rows_query_log_events` = 1 and a statement is written to the binary

log using the row-based logging format, the server generates a an additional log event containing the text of the original statement. If `mysqlbinlog` is executed on this log using the `--verbose` `--``verbose`, the original statement is printed. To prevent the statement from being executed in addition to the row event (which would in effect cause the statement to be excuted twice), it is commented out with a leading # character.

This was implemented with the assumption that such a statement would consist of a single line, which meant that a statement covering multiple lines was handled incorrectly, in that only the first line of the statement actually commented out. Now in such cases, every line of the statement is commented out with a leading #. (Bug #13799555)

- Replication: Queries that were more than 255 characters in length were truncated when viewed in

the output of `SHOW BINLOG EVENTS` or `mysqlbinlog`. This was due to the length of the query being stored in `Rows_query_log_events` using a single byte. (Bug #13799489)

- Replication: Replication locks and some of the protocols controlling the use of these locks were not well

implemented or enforced. In particular, this fix improves lock handling for statements such as `CHANGE``MASTER TO`, `SHOW SLAVE STATUS`, and `FLUSH LOGS`. (Bug #13779291)

- Replication: When logging transactions that affected both transactional and nontransactional tables, the

following statements could sometimes be written into the binary log in the wrong order or on the wrong side of a transaction boundary:

- `SET`,

## MySQL 5.6 Release Notes

```
- CREATE FUNCTION,
- SHOW BINLOG EVENTS,
- REVOKE ALL PRIVILEGES.
```

(Bug #13627921)

- Replication: Setting `binlog_checksum` on the master to a value that was unknown on the slave

caused replication to fail. Now in such cases, replication checksums are disabled on the slave and replication stops with an appropriate error message. (Bug #13553750, Bug #61096)

- Replication: To provide a crash-safe slave, it was previously necessary to change the storage engine

for the `slave_master_info`, `slave_relay_log_info`, and `slave_worker_info` tables from`MyISAM` to `InnoDB` manually, by issuing `ALTER TABLE`. To simplify the setup of replication using these slave log tables, they are now created using the `InnoDB` storage engine. (Bug #13538891)

- Replication: When the slave had been set using `CHANGE MASTER TO` with the `MASTER_DELAY` option

equal to any permitted value greater than zero, then stopped using `STOP SLAVE`, pointed at the current relay log position (as shown by SHOW SLAVE STATUS), and started again, `START SLAVE` failed with the error `Could not initialize master info structure`. (Bug #12995174)

- Replication: The `--relay-log-space-limit` option was sometimes ignored.

More specifically, when the SQL thread went to sleep, it allowed the I/O thread to queue additional events in such a way that the relay log space limit was bypassed, and the number of events in the queue could grow well past the point where the relay logs needed to be rotated. Now in such cases, the SQL thread checks to see whether the I/O thread should rotate and provide the SQL thread a chance to purge the logs (thus freeing space).

Note that, when the SQL thread is in the middle of a transaction, it cannot purge the logs; it can only ask for more events until the transaction is complete. Once the transaction is finished, the SQL thread can immediately instruct the I/O thread to rotate. (Bug #12400313, Bug #64503)References: See also: Bug #13806492.

- Replication: An event whose length exceeded the size of the master dump thread's

`max_allowed_packet` caused replication to fail. This could occur when updating many large rows and using row-based replication.

As part of this fix, a new `slave_max_allowed_packet` system variable is added, which permits`max_allowed_packet` to be exceeded by the slave SQL and I/O threads. Now the size of a packet transmitted from the master to the slave is checked only against this value, and not against the value of`max_allowed_packet`. (Bug #12400221, Bug #60926)

- Replication: Statements using `AUTO_INCREMENT`, `LAST_INSERT_ID()`, `RAND()`, or user variables

could be applied in the wrong context on the slave when using statement-based replication and replication filtering server options (see How Servers Evaluate Replication Filtering Rules). (Bug#11761686, Bug #54201)References: See also: Bug #11754117, Bug #45670, Bug #11746146, Bug #23894.

- Replication: An `INSERT` into a table that has a composite primary key that includes an

`AUTO_INCREMENT` column that is not the first column of this composite key is not safe for statement-based binary logging or replication. Such statements are now marked as unsafe and fail with an error

## MySQL 5.6 Release Notes

when using the `STATEMENT` binary logging format. For more information, see Determination of Safe and Unsafe Statements in Binary Logging, as well as Replication and AUTO_INCREMENT.

Note This issue does not affect tables using the `InnoDB` storage engine, since an`InnoDB` table with an AUTO_INCREMENT column requires at least one key where the auto-increment column is the only or leftmost column.

(Bug #11754117, Bug #45670)References: See also: Bug #11761686, Bug #54201, Bug #11746146, Bug #23894.

- Replication: After upgrading a replication slave to MySQL 5.6.2 or later, enabling the query cache

eventually caused the slave to fail. (Bug #64624, Bug #14005409)

- Microsoft Windows: On Windows, `mysqlslap` crashed for attempts to connect using shared memory.

(Bug #31173, Bug #11747181, Bug #59107, Bug #11766072)

- Microsoft Windows: For Microsoft Windows, the deprecated MySQL Configuration Wizard is no longer

distributed, and instead the newer MySQL Installer is available and preferred.

- After running `ALTER TABLE tbl DISCARD TABLESPACE` for an `InnoDB` table, certain other `ALTER`

`TABLE` operations such as renaming the table or rebuilding the primary key could cause a crash. (Bug#14213568)

- For conditions of the form `WHERE p1 AND (p2 OR p3)`, the optimizer now uses the index merge

access method on `(p2,p3)` if it is more efficient than a range scan on `p1`. Previously, index merge was not considered when a range scan was possible. (Bug #14208922)

- Error messages that should have said "YEAR(2)" said "YEAR(0)" instead. (Bug #14167585)
- For debug builds, `INSERT IGNORE INTO ... SELECT` that selected more than `max_join_size`

rows could raise an assertion. (Bug #14145442)

- With logging of the general query log to a table, logging was disabled within a read-only transaction

because write lock acquisition on the log table was blocked. (Bug #14136866)

- The `ARCHIVE` storage engine could not be built unless the Performance Schema was also built. (Bug

#14116252)

- If a nonexistent page was requested to be loaded into the `InnoDB` buffer pool by the

`innodb_buffer_pool_load_at_startup` configuration option, a subsequent shutdown operation could hang. (Bug #14106082)

- In debug builds, the server failed to check for error status from the storage engine and raised an

assertion. (Bug #14101852)

- In debug builds, warnings occurring during creation of an `InnoDB` table with `ROW_FORMAT=DYNAMIC`

and `innodb_file_per_table` disabled could raise an assertion. (Bug #14101563)

- Derived tables and tables created with `CREATE TABLE ... SELECT` using the output from single-row

queries with `NULL` in the first column could change the value to 0. (Bug #14069831)

- Incorrect assessment of column nullability for a subquery result within a trigger could cause “column

cannot be null” errors. (Bug #14069810, Bug #14005353)

- The Performance Schema did not generate consistent digest values for `CALL` statements. (Bug

#14069132)

## MySQL 5.6 Release Notes

- The LooseScan semijoin strategy could fail to remove duplicates from the result set. (Bug #14053325)
- Certain arguments to `RPAD()` could lead to “uninitialized variable” warnings. (Bug #14039955)
- For debug builds compiled with `gcov`, tests that used `DBUG_SUICIDE` lost `gcov` data. (Bug #14028421)
- When the index enforcing a foreign key constraint was dropped while `foreign_key_checks=0`,

further operations involving the foreign key column could cause a serious error after the`foreign_key_checks` option was re-enabled. (Bug #14025221)

- Mishandling of failed internal commits in administrative statements such as `ANALYZE TABLE` could

cause an assertion to be raised. (Bug #14001091)

- Improper calculation of decimals for `TIME` values given as arguments to `IF()` or `IFNULL()` could cause

a server crash. (Bug #13988413, Bug #14042545)

- Some arguments to `MAKETIME()` could cause a buffer overflow. (Bug #13982125)
- For debug builds, conversion of a double-precision value to the `lldiv_t` type could raise an assertion.

(Bug #13976233)

- Mishandling of failure during multiple-table `UPDATE IGNORE` statements could cause an assertion to be

raised. (Bug #13974815)

- Queries that grouped by an outer `BLOB` column in a subquery caused a server crash. (Bug #13966809)
- Selecting `MIN()` or `MAX()` from a left or right join involving an `INFORMATION_SCHEMA` table could

cause a server crash. (Bug #13966514)

- Queries containing references to user variables were not written to the general query log with some

rewriting, not as received. (Bug #13958454)

- For debug builds, the optimizer could change the query plan when checking sort order and return

incorrect results. (Bug #13949068)

- An infinite thread loop could develop within Performance Schema, causing the server to become

unresponsive. (Bug #13898343)

- Overhead for Performance Schema table aggregation operations was excessive. (Bug #13862186)
- The `version_compile_machine` system variable sometimes did not include the value 64 for server

binaries compiled on a 64-bit system. (Bug #13859866)

- With subquery materialization enabled, some queries with a subquery in the `HAVING` clause caused a

server crash. (Bug #13848789)

- When the `InnoDB` persistent statistics feature was turned on, an `ALTER TABLE` statement on an

`InnoDB` table with delete-marked records could cause a crash (non-debug builds) or assertion error(debug builds). (Bug #13838962, Bug #13867915)

- In bootstrap mode, the server signal handler thread did not shut down if the server aborted early. (Bug

#13837221)

- Some errors in MySQL 5.6 had different numbers than in MySQL 5.5. (Bug #13833438)
- If `KILL QUERY` interrupted an `INSERT` or `UPDATE` that had the `IGNORE` modifier, OK was incorrectly

returned to the client rather than an error code. Now an error (“Query execution was interrupted”) is returned instead. (Bug #13822652)

## MySQL 5.6 Release Notes

- If `KILL QUERY` interrupted a statement during derived table materialization, the server crashed later

trying to read the nonexistent materialized table. (Bug #13820776)

- Incorrect cost calculations for two-table joins could lead to incorrect join order. (Bug #13810048)

References: This issue is a regression of: Bug #26106.

- The Performance Schema stored identifiers in digest tables as `utf8` without converting them from the

original character set first. (Bug #13809293)

- Incorrect stored program caching could cause statements within a stored program that included a `GROUP`

`BY` clause to return different results across multiple program invocations. (Bug #13805127)

- For comparison of a temporal value to and indexed character column, the optimizer could apply the

`range` access method and thus perform an indexed search that found only literal matches. This is incorrect because MySQL permits a variety of delimiters in temporal values represented as strings. (Bug#13803810)

- Several clarifications were made to optimizer trace output. (Bug #13799348)
- `viosslfactories` did not compile on Oracle Linux 6.0 with `CMake` options `-DWITH_SSL=system` and

`-DWITH_DEBUG=1`. (Bug #13799126)

- In debug builds, a race condition in a signal handler during shutdown caused a server crash. (Bug

#13793813)

- A prepared statement that referenced views and were executed using semijoin transformation could

return different results for different executions. (Bug #13773979)References: See also: Bug #14641759.

- Outer join queries with `ALL` could return incorrect results because the optimizer incorrectly rewrote them

to use inner join. (Bug #13735712)

- `(a,b) IN (SELECT c,d FROM t1 WHERE ...)` could produce incorrect results if `t1` had an index

on `(c, d)` and c or d contained `NULL` values. (Bug #13731417)

- For open ranges that effectively resulted in a full index scan, the optimizer did not discard the range

predicate as unneeded. (Bug #13731380)

- The range optimizer sometimes did not treat equivalent expressions the same, depending on the order

of the operands. For example, it could treat `a <= b` and `b >= a` differently. (Bug #13701206)

- With semijoin optimization enabled, an assertion was raised for queries for which the number of tables

was greater than the search depth. (Bug #13685026)

- Truncating a table partition did not invalidate queries in the query cache that used the table. (Bug

#13485448)

- Setting `max_sort_length` to small values could cause a server crash. (Bug #13485416)
- A query executed with literal values in the `WHERE` clause could return results different from the same

query written to select the same literal values from a separate table using a `SELECT` statement in the`WHERE` clause. (Bug #13468414)

- Condition handler code could assume that after handler execution, control would pass up a single level

to the parent, sometimes leading to a server crash. (Bug #13431226)

- If a `GROUP_CONCAT()` result was calculated using intermediate results (for example, if `ORDER BY` or

`DISTINCT` was present), individual intermediate results were each truncated to a maximum of 64K,

## MySQL 5.6 Release Notes

even if the `group_concat_max_len` system variable was set to a larger value. Now the length of any intermediate result and the final result are controlled by the `group_concat_max_len` value. (Bug#13387020, WL #6098)

- Queries with `ALL` subquery predicates could return incorrect results due to a faulty query transformation.

(Bug #13330886)

- Switching between index scans and random scans using the `HANDLER` interface could result in failure of

the interface to properly reinitialize scans. (Bug #13008220)

- The presence of a file named `.empty` in the `test` database prevented that database from being

dropped. (Bug #12845091)

- For queries with `ORDER BY COUNT(*)` and `LIMIT`, the optimizer could choose an execution plan that

produced incorrect results. (Bug #12713907)

- For some subqueries that should be executed using a range scan on a nonprimary index and required

use of filesort, only the first execution of the subquery was done as a range scan. All following executions were done as full table scans, resulting in poor performance. In addition, if index condition pushdown was used, incorrect results could be returned. (Bug #12667154)

- IPv6 functions such as `IS_IPV6()` produced Valgrind warnings with arguments that used a multibyte

character set. (Bug #12635232, Bug #14040277)

- Queries that used `STRAIGHT_JOIN` and were executed using Multi-Range Read optimization could

result in a memory leak. (Bug #12365385)

- Overhead for the Performance Schema was reduced. (Bug #12346211)
- `IN` subqueries that used a variance or standard deviation aggregate function could return a different

result depending on whether the `optimizer_switch` `materialization` flag was enabled.

Note Those aggregate functions may now return a result with a different number of decimals from previously.

(Bug #11766758)

- On Windows, initial database creation failed during bootstrapping. (Bug #11766342)
- A regression bug in the optimizer could cause excessive disk usage for `UPDATE` statements on `InnoDB`

tables. For tables created with `innodb_file_per_table` enabled, `OPTIMIZE TABLE` can be used to recover excessive space used. For tables created in the `InnoDB` system tablespace,it is necessary to perform a dump and restore into a new instance of the system tablespace. (Bug #65745, Bug#14248833)

- Parse errors that occurred while loading UCA or LDML collation descriptions were not written to the error

log. (Bug #65593, Bug #14197426)

- Incorrect metadata could be produced for columns returned from some views. (Bug #65379, Bug

#14096619)

- If an account had a nonzero `MAX_USER_CONNECTIONS` value, that value was not always respected.

(Bug #65104, Bug #14003080)

- When an `ALTER TABLE` operation was performed with an invalid foreign key constraint, the error

reported was `ER_CANT_CREATE_TABLE` rather than `ER_CANNOT_ADD_FOREIGN`. (Bug #64617, Bug#13840553)

## MySQL 5.6 Release Notes

- `SAVEPOINT` statements were incorrectly disallowed within XA transactions. (Bug #64374, Bug

#13737343)References: See also: Bug #11766752.

- The server crashed at shutdown if the slow query log file was a named pipe. (Bug #64345, Bug

#13733221)

- Some Czech error messages contained invalid characters. (Bug #64310, Bug #13726075)
- With `lower_case_table_names=2` on systems with case-insensitive file systems such as Windows or

OS X, `CREATE TABLE ... LIKE` did not preserve lettercase of the destination table name as given in the statement. (Bug #64211, Bug #13702397)

- File access by the `ARCHIVE` storage engine was not instrumented and thus not shown in Performance

Schema tables. (Bug #63340, Bug #13417440)

- The Performance Schema incorrectly displayed some backslashes in Windows file names (by doubling

them). (Bug #63339, Bug #13417446)

- An inappropriate mutex was used to protect random number generation, causing contention during

connect operations. (Bug #62282, Bug #12951609)

- `mysql_store_result()` and `mysql_use_result()` are not for use with prepared statements and

are not intended to be called following `mysql_stmt_execute()`, but failed to return an error when invoked that way in `libmysqld`. (Bug #62136, Bug #13738989)References: See also: Bug #47485.

- Under some conditions, the effect of `RENAME USER` was not recognized until `FLUSH PRIVILEGES` was

used (which should not be necessary). (Bug #61865, Bug #12766319)

- If the `bind_address` system variable was given a host name value and the host name resolved to

more than one IP address, the server failed to start. For example, with `bind_address=localhost`,if `localhost` resolved to both `127.0.0.1` and `::1`, startup failed. Now the server prefers the IPv4 address in such cases. (Bug #61713, Bug #12762885)

- `SHOW TABLES` was very slow unless the required information was already in the disk cache. (Bug

#60961, Bug #12427262)

- On Windows, the `mysql` client crashed when invoked using its full path name. (Bug #60858, Bug

#12402882)

- Sessions could end up deadlocked when executing a combination of `SELECT`, `DROP TABLE`, `KILL`, and

`SHOW ENGINE INNODB STATUS`. (Bug #60682, Bug #12636001)

- For debug builds, errors occurring during processing of `INSERT DELAYED` statements could crash the

server. (Bug #60114, Bug #11827404)

- Using `CONCAT()` to construct a pattern for a `LIKE` pattern match could result in memory corrupting and

match failure. (Bug #59140, Bug #11766101)

- Due to a race condition, it was possible for two threads to end up with the same query ID for different

queries. (Bug #58785, Bug #11765785)

- For queries with range predicates, the optimizer could miscalculate the number of key parts used,

possibly leading to a server crash. (Bug #58731, Bug #11765737)

## MySQL 5.6 Release Notes

- `SHOW` statements treated stored procedure, stored function, and event names as case sensitive. (Bug

#56224, Bug #11763507)

- `mysqlbinlog` exited with no error code if file write errors occurred. (Bug #55289, Bug #11762667)
- yaSSL rejected valid SSL certificates that OpenSSL accepts. (Bug #54348, Bug #11761822)
- If the server held a global mutex while doing network I/O, client disconnections could be slow. (Bug

#53096, Bug #11760669)

- A multiple-table `UPDATE` with the `IGNORE` keyword resulted in an inappropriate and not meaningful `Got`

`error 0 from storage engine` message. (Bug #49539, Bug #11757486)

- When dumping the `mysql` database, `mysqldump` did not include the `general_log` and

`slow_query_log` tables because they cannot be locked. This caused a problem after reloading the dump file if that file contained a `DROP DATABASE` statement for the `mysql` database: The database no longer contained the log tables and attempts to log to them failed. Now `mysqldump` includes statements to re-create the `general_log` and `slow_query_log` tables so that they exist after loading the dump file. Log table contents still are not dumped. (Bug #45740, Bug #11754178)

- When a query was killed, the error code was not always properly propagated up through the server

code. (Bug #43353, Bug #11752226)

- The optimizer could chose a worse execution plan for a condition that used a quoted number compared

to the unquoted number. (Bug #43319, Bug #11752201)

- Queries that used `WHERE (col1, col2) IN ((const, const))` were optimized for `SELECT`, but

not for `DELETE` or `UPDATE`. (Bug #43187, Bug #11752097)

- For `ALTER TABLE` with the `IGNORE` keyword, `IGNORE` is now part of the information provided to the

storage engine. It is up to the storage engine whether to use this when choosing between the in-place or copy algorithm for altering the table. For `InnoDB` index operations, `IGNORE` is not used if the index is unique, so the copy algorithm is used. (Bug #40344, Bug #11750045)

- `LEFT JOIN` on derived tables was very slow. This is now addressed through the use of subquery

materialization. (Bug #34364, Bug #11747876)

- MySQL was overly agressive in enforcing the `NO_ZERO_DATE` and `NO_ZERO_IN_DATE` SQL modes

for default values in column definitions for `CREATE TABLE` and `ALTER TABLE` statements. Previously,default dates that were invalid with those SQL modes enabled produced an error, even when strict mode was not enabled. Now with `NO_ZERO_DATE` or `NO_ZERO_IN_DATE` enabled, invalid default dates produce a warning if strict SQL mode is not enabled, and an error if strict mode is enabled. (Bug #34280,Bug #11747847)

- Redundant “Specified key was too long” messages could be produced by index-creation operations.

(Bug #31149, Bug #11747177)

- Code for the storage engine API did not check the return value from the `ha_rnd_init()`,

`ha_index_init()`, and `index_init()` functions. (Bug #26040, Bug #11746399, Bug #54166, Bug#11761652)

- For table or database names that are longer than 64 characters, the error “Incorrect table name” was

returned rather than “Identifier too long”. (Bug #25168, Bug #11746295)

- During the startup process, `mysqld` could incorrectly remove the PID file of an already running `mysqld`.

(Bug #23790, Bug #11746142)References: See also: Bug #14726272.

## MySQL 5.6 Release Notes

- Using `ALTER TABLE` to add a `TIMESTAMP` column containing `DEFAULT CURRENT_TIMESTAMP` in the

definition resulted in a column containing `'0000-00-00 00:00:00'`, not the current timestamp. (Bug#17392, Bug #11745578)
