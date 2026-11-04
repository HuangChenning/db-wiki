---
title: "Changes in MySQL 5.6.37 (2017-07-17, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=20"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Packaging Notes
- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> Packaging Notes

- `mysqladmin` was added to Docker/Minimal packages because it is needed by InnoDB Cluster. (Bug

#25998285)

- For Windows, MSI installer packages now include a check for the required Visual Studio redistributable

package, and produce a message asking the user to install it if it is missing. (Bug #25658832)

> Security Notes

- The linked OpenSSL library for the MySQL Commercial Server has been updated to version

1.0.2l. Issues fixed in the new OpenSSL version are described at http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #26160962)

> Functionality Added or Changed

- The `mysql` client now supports a `--binary-as-hex` option that causes display of binary data using

hexadecimal notation (`0xvalue`). Thanks to Daniël van Eeden for the patch. (Bug #25340722, Bug#84391)

## MySQL 5.6 Release Notes

- `mysqlaccess` now looks for its configuration file only in the `SYSCONFDIR` directory and `/etc`. (Bug

#25043674)

> Bugs Fixed

- InnoDB: The server allocated memory unnecessarily for an operation that rebuilt the table. (Bug

#25573565, Bug #85043)

- InnoDB: When using an index merge optimizer switch, a `SELECT COUNT(*)` operation sometimes

returned 0. Partitioning code incorrectly performed a `memcpy` instead of a column copy of columns read by the index, causing the wrong records to be copied. (Bug #25332330, Bug #81031)

- Replication: A `USE` statement that followed a `SET GTID_NEXT` statement sometimes had no effect.

(Bug #26128931)

- Replication: If the binary log on a master server was rotated and a full disk condition occurred on the

partition where the binary log file was being stored, the server could stop unexpectedly. The fix adds a check for the existence of the binary log when the dump thread switches to next binary log file. If the binary log is disabled, all binary logs up to the current active log are transmitted to slave and an error is returned to the receiver thread. (Bug #25076007)

- Replication: If a relay log index file named relay log files that did not exist, `RESET SLAVE ALL`

sometimes did not fully clean up properly. (Bug #24901077)

- Replication: `mysqlbinlog`, if invoked with the `--raw` option, does not flush the output file until

the process terminates. But if also invoked with the `--stop-never` option, the process never terminates, thus nothing is ever written to the output file. Now the output is flushed after each event.

(Bug #24609402)

- Replication: A memory leak in `mysqlbinlog` was fixed. The leak happened when processing fake

rotate events, or when using `--raw` and the destination log file could not be created. The leak only occurred when processing events from a remote server. Thanks to Laurynas Biveinis for his contribution to fixing this bug. (Bug #24323288, Bug #82283)

- Replication: Multithreaded slaves could not be configured with small queue sizes using

`slave_pending_jobs_size_max` if they ever needed to process transactions larger than that size. Any packet larger than `slave_pending_jobs_size_max` was rejected with the error ER_MTS_EVENT_BIGGER_PENDING_JOBS_SIZE_MAX, even if the packet was smaller than the limit

```
set by slave_max_allowed_packet.
```

With this fix, `slave_pending_jobs_size_max` becomes a soft limit rather than a hard limit. If the size of a packet exceeds `slave_pending_jobs_size_max` but is less than`slave_max_allowed_packet`, the transaction is held until all the slave workers have empty queues, and then processed. All subsequent transactions are held until the large transaction has been completed. The queue size for slave workers can therefore be limited while still allowing occasional larger transactions. (Bug #21280753, Bug #77406)

- Linux: The generic Linux build for MySQL 8.0 is now built on Oracle Linux 6 using `glibc` 2.12. Systems

that use the build need to have `glibc` 2.12 or later installed on them. (Bug #26005558)

- `mysqldump` could write database names in `USE` statements incorrectly. (Bug #25998635)
- If the `mysql_stmt_close()` C API function was called, it freed memory that later could be accessed if

`mysql_stmt_error()`, `mysql_stmt_errno()`, or `mysql_stmt_sqlstate()` was called. To obtain error information after a call to `mysql_stmt_close()`, call `mysql_error()`, `mysql_errno()`, or`mysql_sqlstate()` instead. (Bug #25988681)

## MySQL 5.6 Release Notes

- Queries could be cached incorrectly, leading to incorrect query results, under these circumstances:

`InnoDB` table; rows are being inserted but have not yet been committed; a query uses the table as a base table in a derived table; the optimizer chooses to materialize the derived table. (Bug #25943038,Bug #86047)

- Man pages for a few utilities were missing from Debian/Ubuntu packages. (Bug #25811814)
- The `field-t` unit test failed to run with AddressSanitizer enabled. Thanks to Laurynas Biveinis for the

patch. (Bug #25803823, Bug #85678)

- Debian client packages were missing information about conflicts with native packages. (Bug #25799475)
- The Perl path in `#!` lines at the beginning of Perl scripts has been adjusted to `/usr/local/bin/perl`

for FreeBSD 11. (Bug #25719975)

- The server exited abnormally attempting to access invalid memory. (Bug #25501659)
- A race condition could occur for `CREATE TABLE` statements with `DATA DIRECTORY` or `INDEX`

`DIRECTORY` clauses. (Bug #25451091)

- MySQL compilation in different directories produced different builds to leakage of absolute paths into

debug information and `__FILE__`. (Bug #25436469, Bug #84608, Bug #25859274, Bug #85855)

- `mysqld_failed` to start the server if the `--datadir` option was specified with a relative path name.

(Bug #25364806)

- With `read_only` enabled, creation of non-`TEMPORARY` tables by non-`SUPER` users was permitted under

certain conditions. (Bug #25250768)

- Certain stored functions, if used in a query `WHERE` clause, could be handled using Index Condition

Pushdown (which should not happen), resulting in a server exit. (Bug #25196653, Bug #25174454)

- On x86 machines, the `uint3korr()` macro read 4 bytes of data instead of the intended 3 bytes. (Bug

#24807826, Bug #83264)

- An assertion was raised during a fetch operation by the memcached plugin. (Bug #24605783)
- Queries that contained `UNION` in a subquery and `GROUP BY` could return incorrect results. (Bug

#24595639)

- `LOAD XML` performance became noticeably slower when the XML file being read contained a great

many spaces, such as those introduced by indenting or pretty-printing. Now all leading whitespace is trimmed from each such value before reading it into memory. (Bug #16212207)
