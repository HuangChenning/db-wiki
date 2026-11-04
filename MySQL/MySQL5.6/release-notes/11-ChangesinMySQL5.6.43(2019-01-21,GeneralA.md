---
title: "Changes in MySQL 5.6.43 (2019-01-21, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=11"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> Security Notes

- The linked OpenSSL library for the MySQL Commercial Server has been updated to version

1.0.2q. Issues fixed in the new OpenSSL version are described at http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #28988091)

> Functionality Added or Changed

- Microsoft Windows: The access control granted to clients on the named pipe created by the MySQL

server now is set to the minimum necessary for successful communication on Windows. Newer MySQL client software can open named pipe connections without any additional configuration. If older client software cannot be upgraded immediately, the new `named_pipe_full_access_group` server system variable can be used to give a Windows group the necessary permissions to open a named pipe connection. Membership in the full-access group should be restricted and temporary. (WL #12445)

> Bugs Fixed

- Replication: A patch to correct the handling of quotes for identifiers in `ROLLBACK TO SAVEPOINT`

statements in the binary log was not correctly applied to subsequent MySQL versions. (Bug #28569645)

- Replication: In some circumstances, the `CHANGE MASTER TO` statement could not

be used on a replication slave if the master info log had been changed from a table(`master_info_repository=TABLE`) into a file (`master_info_repository=FILE`). (Bug#28529558)

- Replication: The value returned by a `SHOW SLAVE STATUS` statement for the total combined size of

all existing relay log files (`Relay_Log_Space`) could become much larger than the actual disk space used by the relay log files. The I/O thread did not lock the variable while it updated the value, so the SQL thread could automatically delete a relay log file and write a reduced value before the I/O thread finished updating the value. The I/O thread then wrote its original size calculation, ignoring the SQL thread's update and so adding back the space for the deleted file. The `Relay_Log_Space` value is now locked during updates to prevent concurrent updates and ensure an accurate calculation. (Bug #26997096, Bug#87832)

- Replication: If the relay log index file was temporarily locked for viewing by a backup process for a

replication slave, and MySQL Server also attempted to access the file at that time for rename or delete operations, the backup completed with warnings, but MySQL Server experienced an unexpected halt.

MySQL Server now retries the file access operation a number of times in case this or a similar scenario is the explanation and the file becomes available again before long. (Bug #25839610)

- The server permitted creation of databases with the same name as redo log files, which could result in

unexpected server behavior. Such names are no longer permitted as database names. (Bug #28867993)

- When a subquery contained a `UNION`, the count of the number of subquery columns was calculated

incorrectly. (Bug #28499924)

## MySQL 5.6 Release Notes

- Comparing log file names as strings using the `memcmp()` function resulted in uninitialized memory

read errors. The comparison now uses the `strncmp()` function. Thanks to Zsolt Parragi and Laurynas Biveinis for their contributions. (Bug #28178776, Bug #90238)

- The transformation of `IN` subquery predicates into semijoins was not handled correctly for a very large

number of tables. (Bug #28004674)

- Executing a prepared statement to do a multiple-row insert with large number of placeholders consumed

excessive memory and could execute slowly. (Bug #27703912)

- The parser accepted invalid `SET` statement syntax in trigger definitions that could result in a server exit.

(Bug #27595603)

- `MyISAM` index corruption could occur for bulk-insert and table-repair operations that involve the repair-

by-sorting algorithm and many (more than 450 million) rows. (Bug #26929724, Bug #88003, Bug#28483283)

- A query employing a dynamic range and an index merge could use more memory than expected. (Bug

#89953, Bug #27659490)
