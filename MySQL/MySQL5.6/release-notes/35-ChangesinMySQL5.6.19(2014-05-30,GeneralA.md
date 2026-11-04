---
title: "Changes in MySQL 5.6.19 (2014-05-30, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=82"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

There is no MySQL Community Server 5.6.18. That version number was used for an out-of-schedule release of MySQL Enterprise Edition to address the OpenSSL “Heartbleed” issue. This issue did not affect MySQL Community Edition because it uses yaSSL, not OpenSSL, so a new release of the Community Server was not needed, and 5.6.17 is followed by 5.6.19.

- Deprecation and Removal Notes
- Functionality Added or Changed
- Bugs Fixed

> Deprecation and Removal Notes

- The `mysqlbug`, `mysql_waitpid`, and `mysql_zap` utilities have been deprecated and will be removed

in MySQL 5.7. (WL #7689, WL #7826)

> Functionality Added or Changed

- The obsolete and unmaintained `charset2html` utility has been removed from MySQL distributions.

(Bug #71897, Bug #18352347)

## MySQL 5.6 Release Notes

> Bugs Fixed

- InnoDB: After upgrading from 5.6.10 to MySQL versions up to and including MySQL 5.6.18, `InnoDB`

would attempt to rename obsolete full-text search auxiliary tables on server startup, resulting in an assertion failure. (Bug #18634201, Bug #72079)

- InnoDB: With persistent statistics enabled, `SHOW TABLE STATUS` output and the `TABLE_ROWS` column

of `INFORMATION_SCHEMA.TABLES` could report an incorrect number of table rows for tables with externally stored pages. (Bug #18384390)

- InnoDB: The fix for Bug#17699331 caused a high rate of read/write lock creation and destruction which

resulted in a performance regression. (Bug #18345645, Bug #71708)References: This issue is a regression of: Bug #17699331.

- InnoDB: For each insert, `memset` would be called three times to allocate memory for system fields. To

reduce CPU usage, the three `memset` calls are now combined into a single call. (Bug #17858679, Bug#71014)

- InnoDB: Enabling the `InnoDB` Table Monitor would result in a `ib_table->stat_initialized`

assertion failure. (Bug #17039528, Bug #69641)

- InnoDB: With `innodb_max_dirty_pages_pct=0` buffer pool flushing would not be initiated until the

percentage of dirty pages reached at least 1%, which would leave up to 1% of dirty pages unflushed.

(Bug #13029450, Bug #62534)

- Replication: Log rotation events could cause `group_relay_log_pos` to be moved forward incorrectly

within a group. This meant that, when the transaction was retried, or if the SQL thread was stopped in the middle of a transaction following one or more log rotations (such that the transaction or group spanned multiple relay log files), part or all of the group was silently skipped.

This issue has been addressed by correcting a problem in the logic used to avoid touching the coordinates of the SQL thread when updating the log position as part of a relay log rotation whereby it was possible to update the SQL thread's coordinates when not using a multithreaded slave, even in the middle of a group. (Bug #18482854)

- Replication: When running the server with `--gtid-mode=ON`, `STOP SLAVE` followed

by `START SLAVE` resulted in a mismatch between the information provided by

```
INFORMATION_SCHEMA.INNODB_TEMP_TABLE_INFO and the Slave_open_temp_tables
```

status variable: the `INNODB_TEMP_TABLE_INFO` table showed that no temporary tables existed, but`Slave_open_temp_tables` had a nonzero value. (Bug #18364070)References: See also: Bug #18236612.

- Replication: In certain cases, the server mishandled triggers and stored procedures that tried to modify

other tables when called by `CREATE TABLE ... SELECT`. This is now handled correctly as an error.

(Bug #18137535)

- Replication: When used on a table employing a transactional storage engine, a failed `TRUNCATE`

`TABLE` was still written to the binary log and thus replayed on the slave. This could lead to inconsistency when the master retained data that was removed on the slave.

Now in such cases `TRUNCATE TABLE` is logged only when it executes successfully. (Bug #17942050,Bug #71070)

- Replication: The server did not always handle the `auto.cnf` file correctly in cases where this file's

permissions were incorrect. (Bug #17786581, Bug #70891)

## MySQL 5.6 Release Notes

- Replication: When the binary log was rotated due to receipt of a `SIGHUP` signal, the new binary log

did not contain the `Previous_gtid_event` required for subsequent processing of that binary log's GTID events. Now when `SIGHUP` is received, steps are taken to insure that the server writes the necessary `Previous_gtid_event` to the new log before writing any GTID events to the new log. (Bug#17026898)

- Replication: When `gtid_mode=ON`, and a transaction is filtered out on the slave, the GTID of the

transaction is still logged on the slave as an “empty” transaction (consisting of a GTID followed immediately by `BEGIN` and then `COMMIT`). This is necessary to prevent the transaction from being retransmitted the next time the slave reconnects or is involved in a failover. The current fix addresses two issues relating to such “empty” transactions:

- No empty transaction was generated for `CREATE TEMPORARY TABLE` or `DROP TEMPORARY TABLE`

statements.

- If the slave used a database filter (`--replicate-do-db` or `--replicate-ignore-db` option), no

empty transaction was generated.

(Bug #71376, Bug #18095502, Bug #18145032)

- The server could fail to properly reprepare triggers that referred to another table after that table was

truncated. (Bug #18596756, Bug #72446, Bug #18665853)

- For indexes on prefixes or character string columns, index corruption could occur for assignment of

binary data to the column due to improper character counting. (Bug #18359924)

- Certain `INFORMATION_SCHEMA` queries could cause a server exit. (Bug #18319790)
- Solaris-specific scripts were included in and installed by non-Solaris packages. (Bug #18305641)
- `innobase_strnxfrm()` wrote one byte too many. (Bug #18277082)
- `EXPLAIN` on a query with an `EXISTS` subquery containing a `UNION` could cause a server exit.

Multiple executions of a prepared `EXPLAIN` on a `UNION` of subqueries could cause a server exit. (Bug#18167356)

- Concurrent execution of a `FLUSH TABLES` operation and a stored program that used a cursor could

cause a server exit. (Bug #18158639)

- The client library could cause clients to exit due to incorrectly mapping the client error number to the

corresponding message, if reallocation of packet buffer memory occurred. (Bug #18080920)

- Calling `mysql_get_server_version()` with an invalid connection handler argument caused the

client to exit. Now it returns 0 and reports a `CR_COMMANDS_OUT_OF_SYNC` error. (Bug #18053212)

- On Windows, calling `mysql_thread_init()` call without `mysql_init()` caused the client to exit.

windows. Now it returns a nonzero result because it is an error to call `mysql_thread_init()` before the client library is initialized with `mysql_library_init()`. (Bug #17514920)

- `mysqldump` could create table definitions in the dump file that resulted in `Too many columns` errors

when reloading the dump file. (Bug #17477959)

- The optimizer trace could cause a server exit in cases where a subquery was transformed away. (Bug

#17458054)

- The Debug Sync facility could lose a signal, leading to a spurious `ER_DEBUG_SYNC_TIMEOUT` error.

(Bug #14765080, Bug #18221750)

## MySQL 5.6 Release Notes

- A statement of the following form broke row-based replication because it created a table having a field of

data type `BIGINT` with a display width of 3000, which is beyond the maximum acceptable value of 255:

```
CREATE TABLE t1 AS SELECT REPEAT('A',1000) DIV 1 AS a;
```

(Bug #71179, Bug #17994219)

- `CMake` produced not-useful warnings about `INTERFACE_LINK_LIBRARIES` policy. (Bug #71089, Bug

#17905155, Bug #17894997)

- Updates could fail to update all applicable rows in cases where multiple key values were identical except

for trailing spaces. (Bug #69684, Bug #17156940)

- On Windows, `REPAIR TABLE` and `OPTIMIZE TABLE` failed for `MyISAM` tables with `.MYD` files larger

than 4GB. (Bug #69683, Bug #17235179)

- Compilation problems were fixed for errors reported by `Clang` and `gcc` when compiling in C++11 mode.

(Bug #66803, Bug #14631159)

- `LOAD DATA LOCAL` could use all CPU if import errors occurred when there were no line delimiters. (Bug

#51840, Bug #11759519)
