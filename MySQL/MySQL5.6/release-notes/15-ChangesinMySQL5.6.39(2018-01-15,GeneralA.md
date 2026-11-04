---
title: "Changes in MySQL 5.6.39 (2018-01-15, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=17"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Configuration Notes
- Security Notes
- Test Suite Notes
- Bugs Fixed

> Configuration Notes

- For RHEL, SLES, and Fedora RPMs, the default plugin directory for debug builds has been changed

from `/usr/lib64/mysql/plugin` to `/usr/lib64/mysql/plugin/debug`. (Bug #27072155, Bug#88363)

> Security Notes

- Incompatible Change: Passwords are now restricted to a maximum of 256 characters for the

`sha256_password` authentication plugin, and for the `PASSWORD()` function when `old_passwords=2`.

Also, the number of password hashing rounds is capped to limit CPU time used. (Bug #27099029, Bug#27194270)

- The linked OpenSSL library for the MySQL Commercial Server has been updated to version

1.0.2n. Issues fixed in the new OpenSSL version are described at http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #27212666, Bug #27236394)

> Test Suite Notes

- Documentation for the MySQL Test Suite is now maintained in the MySQL source tree using Doxygen

(see the MySQL Server Doxygen documentation, available at https://dev.mysql.com/doc/index-other.html.) The related Unix man pages that previously were produced from the old test suite manual

## MySQL 5.6 Release Notes

are no longer updated and have gone out of date. Consequently, they are no longer included in MySQL distributions. (Bug #27021754)

> Bugs Fixed

- InnoDB: An `ALTER TABLE` operation caused the server to halt. (Bug #26492721)
- InnoDB: A `FLUSH TABLES` operation failed to drop an aborted index. While removing the table from the

cache, the clustered index was dropped prior to checking for the aborted index. (Bug #26256456, Bug#86607)

- InnoDB: Warnings that should only appear in debug builds of MySQL were printed to the error log when

the length of the history list exceeded 2000000. (Bug #24296076, Bug #82213)

- InnoDB: Full-text search on indexed columns that use a binary collation did not return case-sensitive

matches. (Bug #21625016, Bug #78048)

- Partitioning: In certain cases when fetching heap records a partition ID could be set to zero. (Bug

#86255, Bug #26034430)

- Replication: With semisynchronous replication in use, if `RESET MASTER` was issued while an active

transaction was waiting for an acknowledgement from the slave, the count of waiting sessions in the`Rpl_semi_sync_master_wait_sessions` server status variable was incorrect after the wait was completed. (Bug #26748533)

- Microsoft Windows: On Windows, with the `myisam_use_mmap` and `flush` system variables enabled,

`MyISAM` did not always flush table files properly. (Bug #26880757)

- Microsoft Windows: On Windows, resolution was improved of a timer used for query performance

assessment. (Bug #22305994, Bug #26734457)

- `VALUES()` was not handled correctly in some cases. (Bug #26881946)

References: See also: Bug #19601973, Bug #17458914.

- The Performance Schema now stores rewritten rather than raw SQL statement text when available. (Bug

#26732229)

- Incorrect results or a server exit could result when `SHA2()` was passed a user-defined variable in some

character sets. (Bug #26704451)

- Creating a table with excessive index information could cause a server exit. (Bug #26529369)
- `REFERENCES` privilege checking could use the incorrect database in some cases. (Bug #26106655)
- Some statements could cause a buffer overflow in the digest code. Thanks to Laurynas Biveinis and

Roel van de Paar for the patch. (Bug #26021187)

- Incorrect results could occur on a table with a unique index when the optimizer chose a Loose Index

Scan even though the unique index had no index extensions. (Bug #25989915, Bug #86165, Bug#26532061, Bug #87207)References: This issue is a regression of: Bug #21749123, Bug #78244.

- Executing a stored procedure containing a statement that created a table from the contents of certain

`SELECT` statements could result in a memory leak. (Bug #25586773)

- For geometry calculations, invalid input parameters could lead to an incorrect result buffer and cause an

assertion to be raised or a server exit. (Bug #25062396)

## MySQL 5.6 Release Notes

- Setting the `MYSQL_GROUP_SUFFIX` environment variable had no effect. (Bug #23072792)
- A circular dependency problem involving `sql/sql_builtin.cc` was resolved. (Bug #16877045)
- A prepared statement containing an `ORDER BY` list that referred to a parameter was not always handled

correctly. (Bug #87863, Bug #26867652)
