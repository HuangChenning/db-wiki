---
title: "Changes in MySQL 5.6.42 (2018-10-22, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=12"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Packaging Notes
- Functionality Added or Changed
- Bugs Fixed

> Packaging Notes

- Binary packages that include `curl` rather than linking to the system `curl` library now use `curl` 7.60.0

rather than 7.45.0. (Bug #28043702)

- The zlib library bundled with MySQL has been upgraded from version 1.2.3 to version 1.2.11. MySQL

implements compression with the help of the zlib library.

The zlib `compressBound()` function in zlib 1.2.11 returns a slightly higher estimate of the buffer size required to compress a given length of bytes than it did in zlib version 1.2.3. The `compressBound()`function is called by `InnoDB` functions that determine the maximum row size permitted when creating compressed `InnoDB` tables or inserting rows into compressed `InnoDB` tables. As a result, `CREATE``TABLE ... ROW_FORMAT=COMPRESSED` or `INSERT` and `UPDATE` operations with row sizes very close to the maximum row size that were successful in earlier releases could now fail. For additional information, see Changes in MySQL 5.6. (WL #10551)

> Functionality Added or Changed

- Previously, file I/O performed in the I/O cache in the `mysys` library was not instrumented, affecting in

particular file I/O statistics reported by the Performance Schema about the binary log index file. Now,this I/O is instrumented and Performance Schema statistics are accurate. Thanks to Yura Sorokin for the contribution. (Bug #27788907, Bug #90264)

> Bugs Fixed

- InnoDB: An `ALTER TABLE` operation that added a primary key produced a segmentation fault. (Bug

#28395278)References: This issue is a regression of: Bug #27753193.

## MySQL 5.6 Release Notes

- InnoDB: An assertion was raised during an `OPTIMIZE TABLE` operation. (Bug #27753193)
- InnoDB: A foreign key constraint name was duplicated during a rename table operation, causing a

failure during later query execution. (Bug #27545888)

- InnoDB: The location of the Innodb Merge Temp File that reported by the `wait/io/file/innodb/`

`innodb_temp_file` Performance Schema instrument was incorrect. (Bug #21339079, Bug #77519)

- Replication: When `FLUSH` statements for specific log types (such as `FLUSH SLOW LOGS`) resulted in

an error, the statements were still written to the binary log. This stopped replication because the error had occurred on the master, but did not occur on the slave. MySQL Server now checks on the outcome of these `FLUSH` statements, and if an error occurred, the statement is not written to the binary log. (Bug#24786290, Bug #83232)

- Microsoft Windows: On Windows, uninstallation of the MySQL Server MSI package through MySQL

Installer produced a spurious popup window. (Bug #27463864)

- Concurrent `INSERT` and `SELECT` statements on a `MERGE` table could result in a server exit. (Bug

#28379285)

- MySQL Server and test RPM packages were missing `perl-Data-Dumper` as a dependency. (Bug

#28144933, Bug #72926)

- For the `mysql` client, the `-b` short option was associated with two long options, `--no-beep` and `--`

`binary-as-hex`. The `-b` option now is associated only with `--no-beep`. (Bug #28093271)

- Very long table keys were handled incorrectly on replication slaves. (Bug #27930505)
- During server startup/shutdown, PID files could be mishandled. (Bug #27919254)
- For `MEMORY` tables, memory overflow errors could occur. (Bug #27799513)
- When converting from a `BLOB` (or `TEXT`) type to a smaller `BLOB` (or `TEXT`) type, no warning or error was

reported informing about the truncation or data loss. Now an appropriate error is issued in strict SQL mode and a warning in nonstrict SQL mode. (Bug #27788685, Bug #90266)

- Failure to create a temporary table during a `MyISAM` query could cause a server exit. Thanks to

Facebook for the patch. (Bug #27724519, Bug #90145)

- An attempted read of an uncommitted transaction raised an assertion. (Bug #26876608)
- `ALTER TABLE ... REORGANIZE PARTITION ...` could result in incorrect behavior if any partition

other than the last was missing the `VALUES LESS THAN` part of the syntax. (Bug #26791931)

- `yum update` did not properly update from RHEL5 RPM packages to current packages. (Bug

#20560761)

- It was possible for a subquery that used a unique key on a column allowing NULL to return multiple

rows. (Bug #88670, Bug #27182010)
