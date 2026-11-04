---
title: "Changes in MySQL 5.6.28 (2015-12-07, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=44"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Functionality Added or Changed
- Bugs Fixed

> Functionality Added or Changed

- MySQL Server RPM packages now contain a conflict indicator for MySQL Connector C, such that an

error occurs when installing MySQL Server if MySQL Connector C is also installed. To install MySQL Server, remove any MySQL Connector C packages first. (Bug #21900800)

- These client programs now support the `--enable-cleartext-plugin` option: `mysqlcheck`,

`mysqldump`, `mysqlimport`, `mysqlshow`. This option enables the `mysql_clear_password` cleartext authentication plugin. (See Client-Side Cleartext Pluggable Authentication.) (Bug #21235226)

- Support for building with Solaris Studio 5.13 was added. (Bug #21185883)
- `mysql_upgrade` now attempts to print more informative errors than `FATAL ERROR: Upgrade`

`failed`. (Bug #77803, Bug #21489398)

- Performance Schema digests in `DIGEST_TEXT` columns have `...` appended to the end to indicate

when statements exceed the maximum statement size and were truncated. This is also now done for statement text values in `SQL_TEXT` columns. (Bug #75861, Bug #20519832)

> Bugs Fixed

- InnoDB: `InnoDB` returned an invalid corruption-related error message during an `IMPORT TABLESPACE`

operation. (Bug #21838158, Bug #77321)

- InnoDB: An old version of `numactl` headers on the build host caused a compilation error when building

a MySQL version that includes NUMA memory policy support. (Bug #21785074)

- InnoDB: An online `ALTER TABLE` operation caused a server exit. (Bug #21640679)
- InnoDB: A schema mismatch error occurred when importing a tablespace that was altered by `DROP`

`INDEX` operation on the source server. (Bug #21514135, Bug #77659)

- InnoDB: A duplicate key error that occurred during an online DDL operation reported an incorrect key

name. (Bug #21364096, Bug #77572)

- InnoDB: An `ALTER TABLE` operation caused the server to exit on disk full. (Bug #21326304, Bug

#77497)

- InnoDB: The system tablespace data file did not extend automatically when reaching the file size

limit, causing startup to fail with a size mismatch error and preventing the addition of another system tablespace data file. (Bug #21287796, Bug #77128)

- InnoDB: Altering the lettercase of a column introduced an inconsistency between the `.frm` file and data

dictionary resulting in a failed `CREATE INDEX` operation on the altered column. (Bug #20755615)

- InnoDB: An `ALTER TABLE` operation that converted a table to an `InnoDB` file-per-table tablespace did

not check for unknown files with the same name as the destination `.idb` file, permitting an unknown file of the same name to be overwritten. (Bug #19218794, Bug #73225)

## MySQL 5.6 Release Notes

- Replication: As `binlog_error_action=ABORT_SERVER` is the default in MySQL 5.7.7 and later

it is being used for more error situations. The behavior has been adjusted to generate a core dump to improve troubleshooting possibilities. (Bug #21486161, Bug #77738)

- Replication: On a multithreaded slave configured with `master_info_repository=TABLE` and

`relay_log_info_repository=TABLE` which had previously been run with `autocommit=1`,if the slave was stopped and `autocommit` changed to 0, executing `START SLAVE` caused the session to appear to hang. After the lock wait timeout, when `START SLAVE` proceeded the server would stop unexpectedly. The fix ensures that when `master_info_repository=TABLE`,`relay_log_info_repository=TABLE`, and `autocommit=0` a new transaction is generated for start and commit to avoid deadlocks. (Bug #21440793)

- Replication: Fatal errors encountered during flushing or synchronizing the binary log were being

ignored. Such errors are now caught and handled depending on the setting of `binlog_error_action`.

(Bug #76795, Bug #68953, Bug #20938915, Bug #16666407)

- Possible buffer overflow from incorrect use of `strcpy()` and `sprintf()` was corrected. (Bug

#21973610)

- MySQL RPM packages for RHEL5 failed to create the `mysql` system user. (Bug #21950975)
- For Debian package control files, `libnuma-dev` was added to `Build-Depends` to enable NUMA

support. (Bug #21822631)

- Selecting `DECIMAL` values into user-defined variables could cause a server exit. (Bug #21819304)
- Concurrent `FLUSH PRIVILEGES` and `REVOKE` or `GRANT` statements could produce a small time window

during which invalid memory access to proxy user information could occur, leading to a server exit. (Bug#21602056)

- Starting the server with the `query_alloc_block_size` system variable set to certain negative values

on a machine without enough memory could result in out-of-memory errors. (Bug #21503595)

- Using `UNINSTALL PLUGIN` to uninstall the `daemon_example` plugin could cause a server exit. (Bug

#21467458)

- `FLUSH DES_KEY_FILE` failed to reload the DES key file. (Bug #21370329)
- If an error occurred during the setup phase of subquery materialization used to compute an `IN` predicate,

cleanup of the temporary table did not happen, leading to Valgrind errors. (Bug #21346081)

- Queries rejected by MySQL Enterprise Firewall were truncated to 512 characters when written to the

error log. (Bug #20948270)

- A server exit could occur for the second execution of a prepared statement for which an `ORDER BY`

clause referred to a column position. (Bug #20755389)

- Repeated execution of a prepared statement could cause a server exit if the default database was

changed. (Bug #20447262)

- Outer references do not work as arguments to `MATCH()`, but the server did not properly detect them.

Now it does and raises an error. (Bug #20007383)References: See also: Bug #21140088.

- Valgrind errors were produced during row comparator setup. (Bug #19929406)
- After failure to create a temporary table during join processing and releasing the table descriptor, an

attempt to access the now-invalid descriptor could cause a server exit. (Bug #19918299)

## MySQL 5.6 Release Notes

- Type conversion failure for `DECIMAL` values could cause a server exit. (Bug #19912326, Bug

#20013538)

- `INSERT DELAYED` could cause a server exit for tables partitioned with a character column as the key

and for which the expression required a character set conversion. (Bug #19894161)

- During a `filesort` for an `UPDATE` statement, the optimizer could access a stale pointer, resulting in a

server exit. (Bug #19893908)

- A server exit could occur when updating a view using an `ALL` comparison operator on a subquery that

selects from an indexed column in the main table. (Bug #19434916)

- Internal buffer sizes in `resolve_stack_dump` were increased to accommodate larger symbol space

requirements for C++ code. (Bug #78885, Bug #22071592)

- MySQL development RPM packages could fail to install if MySQL Connector/C development RPM

packages were installed. (Bug #78815, Bug #22005375)

- Some stress test files in the `mysql-test/suite/innodb_stress` directory had the executable file

mode set although they were not script files. (Bug #78403, Bug #21822413)

- The server initialization script used for the `service mysql status` command on Linux sometimes

incorrectly reported that the server was stopped. (Bug #77696, Bug #21768876)
