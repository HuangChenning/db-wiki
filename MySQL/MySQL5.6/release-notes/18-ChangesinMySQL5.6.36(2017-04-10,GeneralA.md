---
title: "Changes in MySQL 5.6.36 (2017-04-10, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=22"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Compilation Notes
- Configuration Notes
- Packaging Notes
- Security Notes
- Thread Pool Notes
- Functionality Added or Changed
- Bugs Fixed

## MySQL 5.6 Release Notes

> Compilation Notes

- Windows builds now use the default runtime libraries (builds use the `/MD` flag). (Bug #25611609)
- `CMake` support was added for compiling with Developer Studio 12.6. (Bug #25384295)

> Configuration Notes

- MySQL failed to compile if `-DENABLE_DEBUG_SYNC=OFF` AND `-DWITH_DEBUG=ON` were both given.

The `ENABLE_DEBUG_SYNC` option has been removed and enabling `WITH_DEBUG` enables Debug Sync.

(Bug #18374703)

> Packaging Notes

- Microsoft Windows: Reminder: MySQL 5.6 requires the Microsoft Visual C++ 2010 Redistributable

Package to run on Windows platforms. Users should make sure the package has been installed on the system before starting the server. The package is available at the Microsoft Download Center.

- Changes in RPM package structure require a larger set of packages to be removed to install MySQL

Server cleanly. (Bug #25603087)

- To avoid potential race conditions, Debian packages now use the GNU `install` utility rather than a

combination of `mkdir`, `touch`, and `chown`. (Bug #25258829)

- `CMake`-generated packaging for Debian/Ubuntu packages was refactored for improved maintainability.

The change includes updated logic for correctly replacing native distribution packaging in Debian and Ubuntu. (Bug #25126961, Bug #25251872, Bug #84198)

> Security Notes

- The linked OpenSSL library for the MySQL Commercial Server has been updated to version

1.0.2k. Issues fixed in the new OpenSSL version are described at http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #25768671, Bug #25615451)

- The `mysql_options()` C API function now supports a `MYSQL_OPT_SSL_MODE` option. The only

permitted option value is `SSL_MODE_REQUIRED`, to require an encrypted connection to the server. It causes `mysql_real_connect()` to fail if an encrypted connection cannot be obtained, without falling back to an unencrypted connection. Thus, `mysql_real_connect()` returns an error if the server does not support SSL or the client is not configured to use SSL. The client/server exchange terminates immediately after the initial server packet has been received if the server indicates that it does not support SSL.

To require an encrypted connection in MySQL 8.0, the standard MySQL client programs call`mysql_options()` to set `MYSQL_OPT_SSL_MODE` if the `--ssl-mode=REQUIRED` command-line option was specified. Third-party applications that must be able to require encrypted connections can use the same technique. For details, see mysql_ssl_set().

The minor C API version number was not incremented for this change. Application programs compiled for MySQL 8.0 that require `MYSQL_OPT_SSL_MODE` may fail to operate properly if the dynamic loader provides an older client library without `MYSQL_OPT_SSL_MODE`. Such applications must be written to handle this possibility by checking whether the `mysql_options()` call succeeds or fails. (Bug#25575605)

## MySQL 5.6 Release Notes

> Thread Pool Notes

- To improve `thread_pool` plugin performance, connection authentication and initialization have been

moved from the acceptor thread to the thread pool worker threads that handle client connections. This enables the acceptor thread to handle new connections at a higher rate with reduced latency. The`INFORMATION_SCHEMA` `TP_THREAD_GROUP_STATE` table now contains a `CONNECT_THREAD_COUNT`column that indicates the number of threads that are processing or waiting to process connection initialization and authentication. There can be a maximum of four connection threads per thread group;

these threads expire after a period of inactivity. (Bug #17159742, WL #7195, WL #10287)

> Functionality Added or Changed

- Replication: When a negative or fractional timeout parameter was supplied to

`WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS()`, the server behaved in unexpected ways. With this fix:

- A fractional timeout value is read as-is, with no round-off.
- A negative timeout value is rejected with an error if the server is on a strict SQL mode; if the server is

not on a strict SQL mode, the value makes the function return NULL immediately without any waiting and then issue a warning.

(Bug #24976304, Bug #83537)

- The performance of UTF-8 binary collations was improved. (Bug #24788778, Bug #83247, Bug

#25076862)

- Consistency and maintainability of Debian/Ubuntu packaging maintainer scripts was improved. (Bug

#23588977)

- `mysql_secure_installation` is more strict about what it considers valid yes and no responses.

(Bug #13344753, Bug #62925)

> Bugs Fixed

- InnoDB: The restriction that required the first undo tablespace to use space ID 1 was removed. The first

undo tablespace may now be assigned a space ID other than 1. Space ID values for undo tablespaces are still assigned in a consecutive sequence. (Bug #25551311)

- InnoDB: Compiling the server without the Performance Schema caused a build failure. (Bug

#25348787)

- InnoDB: The file handle type name for `InnoDB` file I/O Performance Schema instrumentation was

changed from `os_pfs_file_t` to `pfs_os_file_t`. (Bug #25220118)

- InnoDB: A server exit on restart was caused by missing `my_thread_init()` and

`my_thread_exit()` functions for background threads that initialize the `st_my_thread_var` structure.

(Bug #25167032)

- InnoDB: A `memcached` read operation with a non-default read batch size configuration resulted in a

server exit. (Bug #25147515)

- InnoDB: An error in code related to table statistics raised an assertion in the `dict0stats.cc` source

file. (Bug #24585978)

- InnoDB: Performance Schema instrumentation for `InnoDB` file I/O was disabled on Windows. (Bug

#14025581)

## MySQL 5.6 Release Notes

- InnoDB: The `row_search_mvcc()` function unnecessarily traversed the entire table for a range query,

which occurred when the record was not in the transaction read view. (Bug #84202, Bug #23481444,Bug #25251375)

- Replication: When using a multithreaded slave (`slave_parallel_workers` greater than 0) the value

of `Seconds_Behind_Master` was incorrect when rotating a relay log. (Bug #23532304)

- Ubuntu 12.04 LTS: This is the last release in the MySQL 8.0 series to support Ubuntu 12.04 LTS. As per

the MySQL Support Lifecycle policy regarding ending support for OS versions that are obsolete or have reached end of life, we plan to discontinue building binaries for the Linux distribution in future releases.

(Bug #25828475)

- Oracle Linux 5, Red Hat Enterprise Linux 5, and CentOS 5: This is the last release in the MySQL 8.0

series to support Oracle Linux 5, Red Hat Enterprise Linux 5, and CentOS 5. As per the MySQL Support Lifecycle policy regarding ending support for OS versions that are obsolete or have reached end of life,we plan to discontinue building binaries for those Linux distributions in future releases. Moreover, we plan to build the generic Linux tarballs for the next release on Oracle Linux 6 using glibc 2.12. (Bug#25828375)

- `mysqldump` failed to properly quote certain identifiers in SQL statements written to the dump output.

(Bug #25717383)

- Client preauthorization by the server was missing a length check for a length-encoded string. (Bug

#25714674)

- For Debian/Ubuntu packages, user-defined collation files could be overwritten during MySQL upgrades.

Charset files are now marked as conffiles so that user customizations generate a prompt during upgrades whether to overwrite them. (Bug #25525628, Bug #84761)

- For `CREATE TABLE` statements that specified the table name with a database qualifier and included a

`DATA DIRECTORY` or `INDEX DIRECTORY` option, an error occurred if there was no default database.

(Bug #25514146, Bug #84861)

- Starting the server with `performance_schema_digests_size=1` caused an abnormal exit. (Bug

#25492129, Bug #84786)

- `mysqld_safe` did not check whether the directory named by the `--basedir` option existed. (Bug

#25365194)

- `mysqld_safe` failed if the error log file named by the `--log-error` option was a FIFO. (Bug

#25356221, Bug #84427)

- `mysqld_safe` could fail if the `--datadir` option value ended with a / character. (Bug #25319457)
- A recent change to `mysqld_safe` caused the `mysql.server` script to be unable to start it if the base

directory was specified as an absolute path that differed from the compiled-in default absolute path. (Bug#25319392, Bug #84263)

- The fix for Bug #78777 had different effects depending on whether the Performance Schema is enabled.

(Bug #25309017, Bug #84305)References: This issue is a regression of: Bug #78777.

- The `CONNECTION_CONTROL` plugin failed to compile if the Performance Schema was disabled. (Bug

#25308357, Bug #84304)

- For System V init scripts for RPMs, the `[mysqld]` option-file section was being ignored for some

options, such as `pid-file`. (Bug #25287707, Bug #84172)

## MySQL 5.6 Release Notes

- Init scripts failed to launch `mysqld_safe` if a non-default base directory was used. (Bug #25261472,

Bug #84219)

- `mysqld_safe --no-defaults` did not work (inadvertent consequence of an earlier bug fix). (Bug

#25244898, Bug #84173)

- Semicolon (;) characters within or between statements could cause distinct digests to be generated from

identical statements. (Bug #25244533, Bug #83253)

- For a client linked against `libmysqlclient`, invalid memory access could occur during use of

prepared statements. (Bug #25164932)

- The fix for Bug #25088048 caused the command used by `mysqld_safe` to start the MySQL server to

no longer include the `mysqld` path. (Bug #25144379)References: This issue is a regression of: Bug #25088048.

- Executing a stored procedure containing a query that accessed a view could allocate memory that was

not freed until the session ended. (Bug #25053286)

- A query could produce incorrect results if the `WHERE` clause contained a dependent subquery, the table

had a secondary index on the columns in the select list followed by the columns in the subquery, and`GROUP BY` or `DISTINCT` permitted the query to use a Loose Index Scan. (Bug #24671968, Bug #83005)

- Creation of a `MyISAM` temporary table during query processing could fail if the key length in the query

was greater than the maximum `MyISAM` key length, resulting in a server exit. (Bug #24659861)

- The `DebugPrintTest` and `DebugPrintDeathTest` unit tests did not handle divide-by-zero testing

properly on the Aarch64 platform. Thanks to Alexey Kopytov for the patch. (Bug #24624555, Bug#82889)

- Changes made to `mysqld_safe` in recent MySQL releases require the `--ledir`, `--mysqld`, `--`

`mysqld-version` options to be specified on the command line; they can no longer be specified in option files. This could cause failure of init scripts that invoke `mysqld_safe`. Such scripts now pass the value of the `MYSQLD_OPTS` environment variable as the first command-line argument to `mysqld_safe`,with the value set to such command line-only `mysqld_safe` option values as may be required. On platforms that use systemd, the `MYSQLD_OPTS` value can be set in `/etc/sysconfig/mysqld` with a line such as this:

```
MYSQLD_OPTS=" --ledir=/mysqld_ledir --mysqld=my_wrapper "
```

The value of `MYSQLD_OPTS` can also include `mysqld` options for `mysqld_safe` to pass to `mysqld`.

(Bug #24619033, Bug #82920)References: This issue is a regression of: Bug #24464380, Bug #24483092, Bug #25088048, Bug#25378439, Bug #25378565.

- For `LOAD DATA` used to insert data into an updateable view, the check to verify whether a column is

actually updatable was missing. (Bug #24595937)

- On Debian/Ubuntu platforms, the systemd startup script for MySQL ignored `datadir` settings in `/etc/`

`mysql/my.cnf`. (Bug #24517024, Bug #82709)

- A regular expression pattern match into a large string could result in a server exit due to memory

allocation failure or integer overflow. (Bug #24449076, Bug #24449090)

- An incorrect error was reported for `CREATE TABLE` statements with a large value for the `CONNECTION`

table option. The value is now limited to 1024 bytes. (Bug #24437124)

## MySQL 5.6 Release Notes

- MySQL now uses `readdir()` rather than `readdir_r()`. The latter has been deprecated since `glibc`

2.24 and caused debug builds of MySQL and builds using GCC 6.1 to fail.

Additionally, several problems resulting in GCC 6.1 compiler warnings were corrected. (Bug #23708395,Bug #24437737, Bug #82515, Bug #24459890, Bug #82583, Bug #25103242)

- The `-DWITH_EDITLINE=system` `CMake` option failed with recent versions of the `editline` library.

(Bug #23708332, Bug #25391997, Bug #84501)

- Grant tables with incorrect structure may cause problems in user management operations. As a

consequence of the fix for this, for any operation that modifies a grant table, the server now checks whether the table has the expected structure and produces an error if not. `mysql_upgrade` must be run to update the tables to the expected structure. (Bug #23295423, Bug #25095876, Bug #25448037)

- The `QUOTE()` function could allocate excessive memory. A limit of `max_allowed_packet` bytes is now

imposed and returns `NULL` with a warning for attempts to allocate more. (Bug #23195404)

- When attempting to locate the data directory, `mysqld_safe` incorrectly considered

`$MY_BASEDIR_VERSION/var` as one of the possible locations. (Bug #23013510, Bug #80866)

- The `main.log_tables-big` test case could be unstable on highly loaded hosts. Thanks to Laurynas

Biveinis for the patch. (Bug #22874167, Bug #80607)

- Queries that used an aggregate function with `DISTINCT` could produce incorrect results. (Bug

#22686994, Bug #80310)

- With the `use_index_extensions` flag of the `optimizer_switch` system variable disabled, some

`SELECT DISTINCT` queries could return incorrect results. (Bug #21749123, Bug #78244)

- Debian packages were missing an AppArmor-related include file and incorrectly were marked dependent

on AppArmor (making it impossible to disable AppArmor by uninstalling it). (Bug #20768958)

- In a replication environment, `SET PASSWORD` or `ALTER USER` could fail to execute on the slave due to

failure to parse the hash string correctly. (Bug #20228478)

- On non-Linux Unix systems, the `mysql.server` startup script used the Linux command `pidof` rather

than `pgrep`. (Bug #13788154, Bug #64342)

- Starting multiple instances of `mysqld_safe` after an abnormal server exit could result in one

`mysqld_safe` instance killing another. As a consequence of the bug fix, the `mysqld_safe.pid` file is no longer used. (Bug #11751149, Bug #41908)

- The `--help` message for `mysqld_safe` was corrected to mention that the `--no-defaults`, `--`

`defaults-file`, and `--defaults-extra-file` options, if given, must be the first argument. (Bug#11745176, Bug #11192)

- The bounds check for the XML parser position stack for each level (which has a fixed depth) used the

size of the array as the upper limit, and so was off by one. This is fixed by decreasing the allowable depth by one, which actually matches the maximum number of elements in the position stack. (Bug#83871, Bug #25111907)References: See also: Bug #14040071, Bug #15948580.

- Timestamps for server-side prepared statements could be written to the binary log up to a second behind

timestamps for the corresponding nonprepared statements, leading to time value differences between master and slave servers. (Bug #74550, Bug #19894382, Bug #25187670)
