---
title: "Changes in MySQL 5.6.35 (2016-12-12, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=27"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

## MySQL 5.6 Release Notes

- Connection Management Notes
- MySQL Enterprise Notes
- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> Connection Management Notes

- MySQL Server now includes a plugin library that enables administrators to introduce an increasing delay

in server response to clients after a certain number of consecutive failed connection attempts. This capability provides a deterrent that slows down brute force attacks that attempt to access MySQL user accounts. For more information, see The Connection-Control Plugins. (WL #8885)

> MySQL Enterprise Notes

- Enterprise Encryption for MySQL Enterprise Edition now enables server administrators to impose limits

on maximum key length by setting environment variables. These can be used to prevent clients from using excessive CPU resources by passing very long key lengths to key-generation operations. For more information, see MySQL Enterprise Encryption Usage and Examples. (Bug #19687742)

> Security Notes

- Incompatible Change: These changes were made to `mysqld_safe`:
- Unsafe use of `rm` and `chown` in `mysqld_safe` could result in privilege escalation. `chown` now can be

used only when the target directory is `/var/log`. An incompatible change is that if the directory for the Unix socket file is missing, it is no longer created; instead, an error occurs. Due to these changes,`/bin/bash` is required to run `mysqld_safe` on Solaris. `/bin/sh` is still used on other Unix/Linux platforms.

- The `--ledir` option now is accepted only on the command line, not in option files.
- `mysqld_safe` ignores the current working directory.

Other related changes:

- Initialization scripts that invoke `mysqld_safe` pass `--basedir` explicitly.
- Initialization scripts create the error log file only if the base directory is `/var/log` or `/var/lib`.
- Unused systemd files for SLES were removed.

(Bug #24483092, Bug #25088048, Bug #25378439, Bug #25378565)References: See also: Bug #24464380, Bug #24388753, Bug #24619033, Bug #82920.

- OpenSSL is ending support for version 1.0.1 in December 2016; see https://www.openssl.org/policies/

releasestrat.html. Consequently, MySQL Commercial Server builds now use version 1.0.2 rather than version 1.0.1, and the linked OpenSSL library for the MySQL Commercial Server has been updated from version 1.0.1 to version 1.0.2j. For a description of issues fixed in this version, see https://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (WL #9136)

## MySQL 5.6 Release Notes

> Functionality Added or Changed

- InnoDB: By default, `InnoDB` reads uncommitted data when calculating statistics. In the case of

an uncommitted transaction that deletes rows from a table, `InnoDB` excludes records that are delete-marked when calculating row estimates and index statistics, which can lead to non-optimal execution plans for other transactions that are operating on the table concurrently using a transaction isolation level other than `READ UNCOMMITTED`. To avoid this scenario, a new configuration option,`innodb_stats_include_delete_marked`, can be enabled to ensure that `InnoDB` includes delete-marked records when calculating persistent optimizer statistics. (Bug #23333990)

- Unit testing now uses Google Mock 1.8. (Bug #24572381, Bug #82823)

> Bugs Fixed

- Incompatible Change: A change made in MySQL 5.6.32 for handling of multibyte character sets by

`LOAD DATA` was reverted due to the replication incompatibility (Bug #24487120, Bug #82641)References: See also: Bug #23080148.

- InnoDB: The GCC `mach_parse_compressed` function should load one to five bytes depending on the

value of the first byte. Due to a GCC bug, GCC 5 and 6 emit code to load four bytes before the first byte value is checked (GCC Bug #77673). A workaround prevents this behavior. Thanks to Laurynas Biveinis for the patch. (Bug #24707869, Bug #83073)

- InnoDB: Due to a `glibc` bug, short-lived detached threads could exit before the caller had returned

from `pthread_create()`, causing a server exit. Thanks to Laurynas Biveinis for the patch. (Bug#24605956, Bug #82886)

- InnoDB: An error during a table-rebuilding operation on a table with only a generated clustered index

(`GEN_CLUST_INDEX`) raised and assertion due to an error called with an invalid key name. (Bug#24444831)

- InnoDB: On a table without an explicitly defined primary key, `InnoDB` did not replace the implicit

clustered index (`GEN_CLUST_INDEX`) when a unique key was defined on a `NOT NULL` column. (Bug#24397406)

- InnoDB: `InnoDB` failed to free memory used by the full-text optimizer thread. (Bug #24331265)
- InnoDB: `SHOW ENGINE INNODB STATUS` output showed a “cleaning up” state for an idle thread.

Thread state information was not reset after statement execution. (Bug #21974225, Bug #78777)

- InnoDB: After a server restart, concurrent `INSERT` operations a table with an auto-increment primary

key resulted in a duplicate entry error. The current auto-increment value was not changed after`auto_increment_increment` and `auto_increment_offset` settings were modified. (Bug#20989615, Bug #76872)

- Replication: Tables with special `DEFAULT` columns, such as `DEFAULT CURRENT_TIMESTAMP`,

that existed only on a slave were not being updated when using row-based replication(`binlog_format=ROW`). (Bug #22916743)

- Replication: Enabling semisynchronous replication when a server was during the commit stage could

cause the master to stop unexpectedly. This was related to the patch for Bug# 75570. (Bug #22202516)

- Replication: The fix for Bug #81657 was not correctly merged into MySQL 8.0. Thanks to Laurynas

Biveinis for alerting us. (Bug #83124, Bug #24715790)

- Some Linux startup scripts did not process the `datadir` setting correctly. (Bug #25159791)

## MySQL 5.6 Release Notes

- `CREATE TABLE` now requires the `FILE` privilege if `DATA DIRECTORY` or `INDEX DIRECTORY` is

specified explicitly as a table or partition option. `ALTER TABLE` requires the `FILE` privilege if either option is specified explicitly as a partition option (it ignores them if specified as table options). (Bug#25092566)

- OEL RPM packages now better detect which platforms have multilib support (for which 32-bit and 64-bit

libraries can be installed). Thanks to Alexey Kopytov for the patch. (Bug #24925181, Bug #83457)

- Compiling MySQL using Microsoft Visual Studio 2015 Version 14.0.25420.1 in `relwithdebinfo` mode

failed with linking errors. (Bug #24748505)

- Warnings occurring during `CREATE TABLE ... SELECT` could cause a server exit. (Bug #24595992)
- For segmentation faults on FreeBSD, the server did not generate a stack trace. (Bug #24566529, Bug

#23575445, Bug #81827)

- The `.mylogin.cnf` option file is intended for use by client programs, but the server was reading it as

well. The server no longer reads it. (Bug #24557925)

- If `mysqladmin shutdown` encountered an error determining the server process ID file, it displayed

an error message that did not clearly indicate the error was nonfatal. It now indicates that execution continues. (Bug #24496214)

- The data structure used for `ZEROFILL` columns could experience memory corruption, leading eventually

to a server exit. (Bug #24489302)

- Use of very long subpartition names could result in a server exit. Now partition or subpartition names

larger than 64 characters produce an `ER_TOO_LONG_IDENT` error. (Bug #24400628, Bug #82429)

- On Solaris, `gettimeofday()` could return an invalid value and cause a server shutdown. (Bug

#23499695)

- A union query resulting in tuples larger than `max_join_size` could result in a server exit. (Bug

#23303485)

- The optimizer could choose `ref` access on a secondary index rather than `range` access on the primary

key, even when the cost was higher. (Bug #23259872, Bug #81341)

- For some deeply nested expressions, the optimizer failed to detect stack overflow, resulting in a server

exit. (Bug #23135667)

- When taking the server offline, a race condition within the Performance Schema could lead to a server

exit. (Bug #22551677)

- The Performance Schema `events_statements_summary_by_digest` table could contain multiple

rows for the same statement digest and schema combination, rather than the expected single (unique)row. (Bug #22320066, Bug #79533)

- For debug builds: Adding a unique index to a `POINT NOT NULL` column triggered a warning and the key

was not promoted to a primary key. Creating a unique index on a different non-`NULL` column in the same table then raised an assertion. (Bug #19635706, Bug #24469860)

- Compiling using Clang 3.5 or higher with AddressSanitizer (ASAN) enabled caused the `gen_lex_hash`

utility to abort on Clang LeakSanitizer memory leak check failures. (Bug #76351, Bug #20720615, Bug#22558597, Bug #80014)

- Miscalculation of memory requirements for qsort operations could result in stack overflow errors in

situations with a large number of concurrent server connections. (Bug #73979, Bug #19678930, Bug#23224078)

## MySQL 5.6 Release Notes
