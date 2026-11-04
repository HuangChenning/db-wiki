---
title: "Changes in MySQL 5.6.29 (2016-02-05, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=40"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Packaging Notes
- Security Notes
- Functionality Added or Changed
- Bugs Fixed

## MySQL 5.6 Release Notes

> Packaging Notes

- Packaging support was added for Ubuntu 15.10. (Bug #79104, Bug #22147191)

> Security Notes

- yaSSL was upgraded to version 2.3.9. This upgrade corrects an issue in which yaSSL handled only

cases of zero or one leading zeros for the key agreement instead of potentially any number, which in rare cases could cause connections to fail when using DHE cipher suites. (Bug #22361038)

- The linked OpenSSL library for the MySQL Commercial Server has been updated from version 1.0.1p

to version 1.0.1q. For a description of issues fixed in this version, see http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #22348181)

> Functionality Added or Changed

- InnoDB: A new `InnoDB` configuration option, `innodb_tmpdir`, allows you to configure a separate

directory for temporary files created during online `ALTER TABLE` operations that rebuild the table. This option was introduced to help avoid MySQL temporary directory overflows that could occur as a result of large temporary files created during online `ALTER TABLE` operations. `innodb_tmpdir` can be configured dynamically using a `SET` statement.

Online `ALTER TABLE` operations that rebuild a table also create an intermediate table file in the same directory as the original table. The `innodb_tmpdir` option is not applicable to intermediate table files.

(Bug #19183565)

- The Valgrind function signature in `mysql-test/valgrind.supp` was upgraded for Valgrind 3.11.

(Bug #22214867)

> Bugs Fixed

- InnoDB: A small `InnoDB` buffer pool size with a large `innodb_stats_persistent_sample_pages`

setting resulted in a `Difficult to find free blocks in the buffer pool` warning. (Bug#22385442)

- InnoDB: Starting the server with an empty `innodb_data_home_dir` entry in the configuration file

caused `InnoDB` to look for the buffer pool file in the root directory, resulting in a startup error. (Bug#22016556, Bug #78831)

- InnoDB: A full-text query run under high concurrency caused a server exit due to an invalid memory

access. (Bug #21922532)

- InnoDB: With a large `innodb_sort_buffer_size` setting, adding an index on an empty table

performed more slowly than expected. (Bug #21762319, Bug #78262)

- Replication: When DML invokes a trigger or a stored function that inserts into an `AUTO_INCREMENT`

column, that DML has to be marked as an unsafe statement. If the tables are locked in the transaction prior to the DML statement (for example by using `LOCK TABLES`), then the DML statement was not being marked as an unsafe statement. The fix ensures that such DML statements are marked correctly as unsafe. (Bug #17047208)

- Replication: As part of the fix for Bug #16290902, when writing a `DROP TEMPORARY TABLE IF`

`EXISTS` query into the binary log, the query is no longer preceded by a `USE `db` statement. Instead the query uses a fully qualified table name, for example `DROP TEMPORARY TABLE IF EXISTS`

## MySQL 5.6 Release Notes

`db`.`t1`;`. This changed the application of `replicate-rewrite-db` filter rules, as they work only on the default database specified in a `USE` statement. This caused slaves to fail when the resulting `CREATE TEMPORARY TABLE` was applied. The fix ensures that at the time of writing a `DROP``TEMPORARY TABLE IF EXISTS` query into the binary log, a check is made for the default database.

If it exists then the query is written as `USE default_db` in the binary log. If a default database is not present then the query is logged with the qualified table name. (Bug #77417, Bug #21317739)

- Replication: If generating a GTID for a transaction fails, the transaction is not written

to the binary log but still gets committed. Although running out of GTIDs is a rare situation, if it did occur an error was written to the binary log as a sync stage error. With`binlog_error_action=ABORT_SERVER`, the server aborts on such an error, avoiding data inconsistency. When `binlog_error_action=IGNORE_ERROR`, the server continues binary logging after such an error, potentially leading to data inconsistency between the master and the slave. The fix changes the error to be correctly logged as a flush stage error. (Bug #77393, Bug #21276561)

- Replication: When using `--gtid-mode=ON` , `--enforce-gtid-consistency` , and `--`

`binlog-format=row`, if a user defined function with multiple `DROP TEMPORARY TABLE`statements was executed on a master, the resulting binary log caused an error on slaves.

The fix ensures that stored functions and triggers are also considered multi-statement transactions, and that when `--enforce-gtid-consistency` is enabled, functions with `CREATE TEMPORARY TABLE` or `DROP TEMPORARY TABLE` statements generate an`ER_GTID_UNSAFE_CREATE_DROP_TEMPORARY_TABLE_IN_TRANSACTION` error. (Bug #77354, Bug#21253415)

- Replication: Stored procedure local variables that were used in an `ALTER EVENT` statement were

not being replicated correctly. This was related to the fact that `CALL` statements are not written into the binary log. Instead each statement executed in a stored procedure is binary logged separately,with the exception that the statement string is modified so that uses of stored procedure local variables are replaced with `NAME_CONST('spvar_name', 'spvar-value')` calls. DDL statements (which are always binary logged in statement binary log mode irrespective of the current binary log format)can also use stored procedure local variables and a clash could cause them to not be replicated correctly. The fix ensures that any stored procedure local variables used in a statement are replaced with`NAME_CONST(...)`, except for the case when it is a DML statement and the binary log format is `ROW`.

(Bug #77288, Bug #21229951)

- Replication: `DROP TABLE` statements are regenerated by the server before being written to the binary

log. If a table or database name contained a non-regular character, such as non-latin characters, the regenerated statement was using the wrong name, breaking replication. The fix ensures that in such a case the regenerated name is correctly converted back to the original character set. Also during work on this bug, it was discovered that in the rare case that a table or database name contained 64 characters,the server was throwing an `assert(M_TBLLEN < 128)` assertion. The assertion has been corrected to be less than or equal 128. (Bug #77249, Bug #21205695)References: See also: Bug #78036, Bug #22261585, Bug #21619371.

- Replication: Irrespective of the current `binlog_format` setting, DDL that changes metadata on a

master is always identified and written to the binary log in `STATEMENT` format. Such DDL could occur from event based SQL statements, such as `CREATE EVENT` or `DROP EVENT`, or transactions that had unsafe functions such as `sysdate()`. When `binlog_format=MIXED` and attempting to replicate such DDL, it was not being correctly identified and therefore was not being correctly replicated. (Bug #71859,Bug #19286708)

- Microsoft Windows: Added Microsoft Visual Studio 2015 support. Changes include using the

native (added in VS 2015) timespec library if it exists, renamed lfind/lsearch and timezone/tzname to avoid redefinition problems, set TMPDIR to "" by default as P_tmpdir no longer exists, deprecated std::hash_map in favor of std::unordered_map, and added Wix Toolset 3.10 support. (Bug #21770366)

## MySQL 5.6 Release Notes

References: See also: Bug #21657078.

- Inserting a token of 84 4-byte characters into a full-text index raised an assertion. The maximum token

length was 84 characters up to a maximum of 252 bytes, which did not account for 4-byte characters.

The maximum byte length is now 336 bytes. (Bug #22291765, Bug #79475)

- If a client attempted to use an unsupported client character set (`ucs2`, `utf16`, `utf32`), the error

message reported to the client differed for SSL and non-SSL connections. (Bug #22216715)

- Data corruption or a server exit could occur if a stored procedure had a variable declared as `TEXT` or

`BLOB` and data was copied to that variable using SELECT ... INTO syntax from a `TEXT` or `BLOB` column.

(Bug #22203532, Bug #22232332, Bug #21941152)

- `CREATE TEMPORARY TABLE .. SELECT` statements involving `BIT` columns that resulted in a column

type redefinition could cause a server exit or an improperly created table. (Bug #21902059)

- With `character_set_server=utf16le`, some values of `ft_boolean_syntax` could cause a server

exit for full-text searches. (Bug #21631855)

- With `LOCK TABLES` in force, an attempt to open a temporary `MERGE` table consisting of a view in its list

of tables (not the last table in the list) caused a server exit. (Bug #20691429)

- For certain prepared statements, the optimizer could transform join conditions such that it used a pointer

to a temporary table field that was no longer available after the initial execution. Subsequent executions caused a server exit. (Bug #19941403)

- Repeated execution of `ALTER TABLE v1 CHECK PARTITION` as a prepared statement, where `v1` is a

view, led to a server exit.

In addition, output for some administrative operations, when they are attempted on a view, changes from “Corrupt” to “Operation failed”. These include `ANALYZE TABLE`, `OPTIMIZE TABLE`, and `REPAIR``TABLE`, and `ALTER TABLE` statements that perform `ANALYZE PARTITION`, `CHECK PARTITION`,`OPTIMIZE PARTITION`, and `REPAIR PARTITION` operations. (Bug #19817021)

- Valgrind detected some possibly unsafe use of string functions in code used for asymmetric encryption.

(Bug #19688135)

- SSL connections ignored any change made by passing the `MYSQL_OPT_READ_TIMEOUT` option to the

`mysql_options()` C API function. (Bug #17618162)

- Solaris packages failed to note the dependency of the MySQL client library on the `libstlport` library.

(Bug #79778, Bug #22504264)

- Using systemd to start `mysqld` failed if configuration files contained multiple `datadir` lines. Now the

last `datadir` line is used. (Bug #79613, Bug #22361702)

- If server was started with `--thread-handling=no-threads`, no foreground thread was created for a

client connection. The Performance Schema did not account for the possibility of no foreground threads for queries on the `session_connect_attrs` table, causing an assertion to be raised. (Bug #78292,Bug #21765843)

- `ALTER TABLE ... CONVERT TO CHARACTER SET` operations that used the `INPLACE` algorithm were

ineffective if the table contained only numeric data types. Also, such operations failed to clean up their temporary `.frm` file. (Bug #77554, Bug #21345391)

```
- Heavy SHOW PROCESSLIST or SELECT ... FROM INFORMATION_SCHEMA.PROCESSLIST activity
```

could result in the server accepting more than `max_connections` connections. (Bug #75155, Bug#20201006)

## MySQL 5.6 Release Notes

- When used with the `libmysqld` embedded server, the `mysql_stmt_execute()` C API function

failed with a `malformed communication packet` error, even for simple prepared statements. (Bug#70664, Bug #17883203)
