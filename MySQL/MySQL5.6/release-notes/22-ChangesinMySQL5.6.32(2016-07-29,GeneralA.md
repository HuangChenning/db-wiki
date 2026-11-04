---
title: "Changes in MySQL 5.6.32 (2016-07-29, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=33"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

> Bugs Fixed

- Incompatible Change: For multibyte character sets, `LOAD DATA` could fail to allocate space correctly

and ignore input rows as a result.

A consequence of this change is that previously accepted invalid character data is now rejected, which can cause issues if you replicate from an older server without this bug fix to a newer server with this bug fix. For example, if an older server that accepts invalid `utf8` character set data replicates to a newer server with this bug fix, the newer server will not accept the data and replication will fail with an “Invalid utf8 character string” error. Solutions for this issue include:

- Correct the invalid data so that it is correct for the character set
- Use a different character set for which the data is not invalid
- Upgrade the master to a version that has the bug fix so that master and slave interpret the data the

same way(Bug #76237, Bug #20683959, Bug #23080148)References: This issue is a regression of: Bug #14653594.

- InnoDB: Full-text search auxiliary tables could be dropped by one session while being access by

another. (Bug #23742339)

- InnoDB: Selecting full-text index information schema tables for a deleted table caused a segmentation

fault. (Bug #23479595)

- InnoDB: Rollback of a full-text index synchronization operation raised an assertion. The rollback

operation attempted to acquire a mutex still held by the background synchronization thread. (Bug#23320569)

- InnoDB: Setting `innodb_monitor_enable` to `all` did not enable all counters. (Bug #22576241, Bug

#80083)

## MySQL 5.6 Release Notes

- Replication: An incorrectly formed `server_uuid` read in from `auto.conf` could cause an unexpected

halt. (Bug #21936933)

- Replication: After issuing a `PURGE BINARY LOGS` statement, if the binary log index file was not

available, for example because it had been opened by another application such as MEB, the server could stop unexpectedly. Although this situation was rare, the handling has been made more robust to avoid unexpected halts and more informative errors are provided. (Bug #20381055)

- Replication: When using row-based replication and `InnoDB`, replication slaves reverted to using an

older locking scheme when a transaction had already acquired an `AUTOINC` lock related to a `LOAD``FILE` or `INSERT ... SELECT` type of statement, reducing replication slave performance. The fix ensures that `sql_command` is set correctly for any of the DML events such as `WRITE_ROWS_EVENT`,`UPDATE_EVENT`, and `DELETE_EVENT`. (Bug #79324, Bug #22247668)

- Replication: A MySQL version 5.5 slave does not have a `server_uuid` and replication identified

servers by their `server_id`. Starting from MySQL version 5.6, replication masters detected a zombie dump thread based only on a slave's `server_uuid` value, under the assumption that each slave has a unique UUID. Connecting a MySQL 5.5 slave to a MySQL 5.6 and later master meant that the master was unable to detect zombie dump threads that were created to serve slaves running versions older than MySQL 5.6. The fix ensures that a master now first checks if a slave has a `server_uuid` set. If it is set,zombie dump thread detection happens based on the slave's UUID. If a slave's `server_uuid` is not set,zombie dump thread detection happens based on `server_id`. (Bug #77195, Bug #21179199)

- Replication: With `slave_skip_errors` enabled there were still special cases when slave errors were

not being correctly ignored. For example:

- When opening and locking a table failed.
- When field conversions failed on a server running row-based replication.

In these cases the error was considered critical and it was not respecting the state of`slave_skip_errors`. The fix ensures that with `slave_skip_errors` enabled, all errors reported during applying a transaction are correctly handled. This means that in such a set up, upon receiving an error with the `log_warnings` option set to greater than 1, if the error can be ignored then the warning is printed into the error log and the server continues as it does in the case of other ignored errors. (Bug#70640, Bug #17653275)

- Replication: When using statement-based or mixed binary logging format with `--read-only=ON`, it

was not possible to modify temporary tables. (Bug #62008, Bug #12818255)References: See also: Bug #14294223, Bug #16561483.

- MySQL Server upgrades performed using RPM packages failed when upgrading from MySQL 5.5

Community to MySQL 5.6 Community or MySQL 5.5 Commercial to MySQL 5.6 Commercial. (Bug#23736787)

- The code for reading character set information from Performance Schema statement events tables (for

example, `events_statements_current`) did not prevent simultaneous writing to that information. As a result, the SQL query text character set could be invalid, which could result in a server exit. Now an invalid character set causes `SQL_TEXT` column truncation. (Bug #23540008)

- A buffer overflow in the `regex` library was fixed. (Bug #23498283)
- Certain arguments to `NAME_CONST()` could cause a server exit. (Bug #23279858)
- For unit-testing with the MySQL test suite, the `make unit-test` command is no longer available. The

`ctest` program should be used instead. See the MySQL Server Doxygen documentation, available at https://dev.mysql.com/doc/index-other.html. (Bug #23273434, Bug #81389)

## MySQL 5.6 Release Notes

- `ST_Distance()` could raise an assertion for `NULL` return values. (Bug #22760390)
- With the query cache enabled, executing a prepared statement with `CURSOR_TYPE_READ_ONLY` and

then again with `CURSOR_TYPE_NO_CURSOR` caused the server to return an error. (Bug #22559575, Bug#80026)

- `mysql_real_connect()` was not thread-safe when invoked with the `MYSQL_READ_DEFAULT_FILE`

or `MYSQL_READ_DEFAULT_GROUP` option enabled. (Bug #22322504, Bug #79510)

- Installing MySQL from a `yum` or `zypper` repository resulted in `/var/log/mysqld.log` being created

with incorrect user and group permissions. (Bug #21879694, Bug #78512)

- If a stored function updated a view for which the view table had a trigger defined that updated another

table, it could fail and report an error that an existing table did not exist. (Bug #21142859, Bug #76808)

- If an `INSTALL PLUGIN` statement contained invalid UTF-8 characters in the shared library name, it

caused the server to hang (or to raise an assertion in debug builds). (Bug #14653594, Bug #23080148,Bug #27167197)
