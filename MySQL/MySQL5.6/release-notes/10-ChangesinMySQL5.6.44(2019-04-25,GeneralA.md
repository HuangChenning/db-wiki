---
title: "Changes in MySQL 5.6.44 (2019-04-25, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=9"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Beginning with MySQL 5.6.44, Oracle no longer provides binaries for SUSE 11.

- Packaging Notes
- Security Notes

## MySQL 5.6 Release Notes

- Bugs Fixed

> Packaging Notes

- The `libevent` library bundled with MySQL was upgraded to version 2.1.8. (Bug #28207237, Bug

#29041505, Bug #29055011)

> Security Notes

- The linked OpenSSL library for the MySQL Commercial Server has been updated to version

1.0.2r. Issues fixed in the new OpenSSL version are described at http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #28988091)

> Bugs Fixed

- InnoDB: The `INDEX_LENGTH` value in `INFORMATION_SCHEMA.TABLES` was not updated when adding

an index. (Bug #19811005)

- Partitioning: An `AUTO_INCREMENT` key added to a partitioned table by an `ALTER TABLE` statement

using `ALGORITHM=INPLACE` restarted on each partition. (Bug #92241, Bug #28573894)

- Replication: If an applier thread was stopped while it was in the process of opening a table, no error

was set, which could result in a segmentation fault or assertion depending on the build type. Error handling is now correctly activated in this situation. (Bug #28864557)

- Replication: If a storage engine has the capability to log in `STATEMENT` format but not in `ROW` format,

when `binlog_format` is set to `STATEMENT`, an unsafe SQL statement should be logged and a warning message should be written to the error log. However, such statements were instead not executed and an error message was written to the error log, which is the correct behavior when `binlog_format` is set to`MIXED` or `ROW`. The issue has now been corrected so that unsafe statements are logged with a warning as expected when `binlog_format` is set to `STATEMENT`. (Bug #28429993, Bug #73936)

- Microsoft Windows: Validity testing for the `named_pipe_full_access_group` system variable did

not account for `NULL` values. (Bug #29256690)

- MySQL 5.6 did not build with maintainer mode enabled with GCC 7. (Bug #29048768)
- A damaged `mysql.user` table could cause a server exit. (Bug #28986737)
- `mysqladmin shutdown` did not wait for `mysqld` to shut down. (Bug #28466137, Bug #91803)

References: This issue is a regression of: Bug #25364806.

- Some status variable values could temporarily increase before returning to their original value. (Bug

#27839644, Bug #90351)

- The binary file for the `udf_example` loadable function was omitted from binary distributions. (Bug

#26115002, Bug #29178542)

- Compiling the `InnoDB` `memcached` plugin did not work on some platforms where MySQL was

configured using `-DWITH_LIBEVENT=system`, for `libevent` version 2.0 or higher. (Bug #80073, Bug#22573379, Bug #23567441)

- Ubuntu 14.04 and SLES 11 are EOL, and no longer supported.

## MySQL 5.6 Release Notes
