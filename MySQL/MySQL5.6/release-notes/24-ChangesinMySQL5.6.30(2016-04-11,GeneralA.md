---
title: "Changes in MySQL 5.6.30 (2016-04-11, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=37"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Security Notes

## MySQL 5.6 Release Notes

- Bugs Fixed

> Security Notes

- The linked OpenSSL library for the MySQL Commercial Server has been updated to version 1.0.1s. For

a description of issues fixed in this version, see http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #22685885, Bug #22923458)

- MySQL client programs now support an `--ssl-mode` option that enables you to specify the security

state of the connection to the server. If the option is not specified, the default value is `DISABLED`(establish an unencrypted connection). `--ssl-mode=REQUIRED` can be specified to require an encrypted connection, or fail if an encrypted connection cannot be obtained.

These clients support `--ssl-mode`: `mysql`, `mysqladmin`, `mysqlcheck`, `mysqldump`, `mysqlimport`,

```
mysqlshow, mysqlpump, mysqlslap, mysqltest, mysql_upgrade.
```

For more information, see Command Options for Encrypted Connections.

Note In MySQL 5.7 and higher, the C client library provides native support for requiring encrypted connections: call the `mysql_options()` C API function, passing the`MYSQL_OPT_SSL_MODE` option with a value of `SSL_MODE_REQUIRED`. In MySQL

8.0, the client library provides no such support because doing so would break binary compatibility with previous library versions within the series. Clients that require encrypted connections must implement the logic themselves.

To require encrypted connections in MySQL 8.0, the standard MySQL client programs use this technique: If `--ssl-mode=REQUIRED` was specified, the client program turns on SSL, connects to the server, and checks whether the resulting connection is encrypted. If not, the client exits with an error. Third-party applications that must be able to require encrypted connections can use the same technique. For details, see mysql_ssl_set().

(WL #8785, WL #9072)

> Bugs Fixed

- InnoDB; Partitioning: When `OPTIMIZE TABLE` rebuilt a partitioned `InnoDB` table, it placed the

resulting partition tablespace files (`*.ibd` files) in the default data directory instead of the directory specified using the `DATA DIRECTORY` option. (Bug #75112, Bug #20160327)

- InnoDB: Running `REPLACE` operations on multiple connections resulted in a hang. (Bug #22530768,

Bug #79185)

- InnoDB: MySQL stalled when synchronizing the `InnoDB` full-text index cache. (Bug #22516559, Bug

#16510576, Bug #73816)

- InnoDB: A `CREATE TABLE ... DATA DIRECTORY` operation failed to create a table while

`innodb_flush_method` was set to `O_DIRECT`. (Bug #22180006, Bug #79200)References: This issue is a regression of: Bug #21113036.

- InnoDB: The `innodb_open_files` setting could exceed the open files limit. (Bug #22111472)

## MySQL 5.6 Release Notes

- Replication: Issuing `STOP SLAVE` caused a spurious `Error reading packet from server:`

`Lost connection to MySQL server during query` message to be written to the error log. With this fix, when connection to the master is lost, the `abort_slave` flag is checked and the error message is printed only if the flag is not set. (Bug #22305605, Bug #79504)References: See also: Bug #12977988, Bug #22290309.

- Replication: When a multithreaded slave stopped with an error, the same error message was printed

three times. Now, the SQL thread's kill acceptance status is saved, and only printed once. (Bug#21198611, Bug #77237)

- Replication: `mysqlbinlog --verbose` displayed BINARY and VARBINARY data as ordinary

strings, causing any single quote (“'”) or backslash (“\”) among the data to be printed as such, which was confusing to the users and, in the case of a backslash, caused the next character to be skipped. This fix makes `mysqlbinlog` print the characters' hexadecimal values (“\x27” for single quote and “\x5c” for backslash) instead. (Bug #20836250)

- Replication: The test case `main.merge` failed when the variables `binlog_format` was set to “`ROW,`”

as the server tried to get information for table creation for a child table before it was opened. With this fix,the server skips getting information for the table in the situation. (Bug #20574550, Bug #75976)

- Replication: If a query on a master generated an error and partial results were written to the binary log,

for example due to a `DROP TABLE IF EXISTS` statement applying to multiple tables that would break foreign key constraints, when a slave configured with replication filters encountered the query it could be incorrectly binary logged. This caused errors such as:

```
Last_SQL_Error: Query caused different errors on master and slave. Error on
master: message (format)='Cannot delete or update a parent row: a foreign
key constraint fails' error code=1217 ; Error on slave: actual message='no
error', error code=0. Default database: 'db1'. Query: 'DROP TABLE IF EXISTS
`table1` /* generated by server */'
```

There were two fixes required for this bug.

- If a `DROP TABLE` statement used to drop a single table fails, to avoid partial results causing this bug

the query is not written to the binary log. If a `DROP TABLE` statement used to drop a list of tables fails,any partial results it generates are written to the binary log with an error.

- When a query that generates an error as expected was received by a slave but it was skipped due

to replication filters, the slave was incorrectly checking the error. The fix for Bug #76493 ensures that this comparison of the expected error from the master with the actual error from the slave does not happen.

(Bug #77684, Bug #21435502)References: See also: Bug #20797764, Bug #76493.

- Integer overflow could occur during client handshake processing, leading to a server exit. (Bug

#22722946)

- The System-V initialization script for RHEL6 or older failed to enable the `mysqld` service by default. (Bug

#22600974)

- When `ExtractValue()` found no match for the supplied expression, it returned `NULL` instead of an

empty string as expected.

This issue affected MySQL 5.6.28 and 5.6.29 only. (Bug #22552615)

## MySQL 5.6 Release Notes

- Improper host name checking in X509 certificates could permit man-in-the-middle attacks. (Bug

#22295186, Bug #22738607)

- A boolean mode full-text search caused a segmentation fault. (Bug #22176795)
- Concurrent selecting and flushing of a `FEDERATED` table while killing connections accessing it could

result in a server exit. (Bug #21918190)

- Executing `GRANT PROXY` statements after altering the definition of the `mysql.user` system table could

result in a server exit. (Bug #21699037)

- Certain error messages included part of the SQL statement that produced them, possibly exposing data.

(Bug #21682356)

- Although it is possible to create nontemporary tables using the prefix `#sql`, Performance Schema

assumed that tables named using this prefix were temporary and could be ignored. Performance Schema now uses table attributes other than the name to identify temporary tables. (Bug #21105475,Bug #22532368, Bug #79934)

- Account filtering performed by the `audit_log` plugin incorrectly used the account named by the

`USER()` function rather than the `CURRENT_USER()` function (the latter being the account used for authentication). (Bug #19509471, Bug #22454245, Bug #77553)

- Character set conversion operations on `NULL` parameters to prepared statements could cause a server

exit. (Bug #18823979)

- Loose Index Scan was not chosen for queries that had an equality condition. (Bug #18109609)
- A MySQL 5.6 server exited during startup if used with a 5.7 data directory due to the change in 5.7 of the

`mysql.plugin` table from `MyISAM` to `InnoDB`. A safe shutdown now occurs in this circumstance. (Bug#79290, Bug #22216779)

- For `INSERT` and `UPDATE` operations that caused `FOREIGN KEY` constraint violations, errors were

reported rather than warnings when the `IGNORE` keyword was used. (Bug #78853, Bug #22037930)References: See also: Bug #23135731.

- For some queries, an Index Merge access plan was chosen over a range scan when the cost for the

range scan was the same or less. (Bug #77209, Bug #21178196)

- Certain queries could raise an assertion when a internal string operation produced a `NULL` pointer rather

than an empty string. (Bug #74500, Bug #19875294, Bug #13358486, Bug #79988, Bug #22551116)

- `EXPLAIN` for `SELECT ... FOR UPDATE` statements acquired locks. (Bug #72858, Bug #18899860)
- Processlist state information was not updated correctly for `LOAD DATA` and could show a state different

from `executing`. (Bug #69375, Bug #16912362)
