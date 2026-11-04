---
title: "MySQL :: MySQL 26.10 Reference Manual :: 3.13 Upgrade Troubleshooting"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/upgrade-troubleshooting.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 3.13 Upgrade Troubleshooting

- A schema mismatch in a MySQL 9.7 instance between the `.frm` file of a table and the `InnoDB` data dictionary can cause an upgrade to MySQL 26.10 to fail. Such mismatches may be due to `.frm` file corruption. To address this issue, dump and restore affected tables before attempting the upgrade again.
- If problems occur, such as that the new [**mysqld**](mysqld.md) server does not start, verify that you do not have an old `my.cnf` file from your previous installation. You can check this with the [`--print-defaults`](option-file-options.md) option (for example, [**mysqld --print-defaults**](mysqld.md)). If this command displays anything other than the program name, you have an active `my.cnf` file that affects server or client operation.
- If, after an upgrade, you experience problems with compiled client programs, such as `Commands out of           sync` or unexpected core dumps, you probably have used old header or library files when compiling your programs. In this case, check the date for your `mysql.h` file and `libmysqlclient.a` library to verify that they are from the new MySQL distribution. If not, recompile your programs with the new headers and libraries. Recompilation might also be necessary for programs compiled against the shared client library if the library major version number has changed (for example, from `libmysqlclient.so.20` to `libmysqlclient.so.21`).
- If you have created a loadable function with a given name and upgrade MySQL to a version that implements a new built-in function with the same name, the loadable function becomes inaccessible. To correct this, use [`DROP           FUNCTION`](drop-function.md) to drop the loadable function, and then use [`CREATE FUNCTION`](create-function.md) to re-create the loadable function with a different nonconflicting name. The same is true if the new version of MySQL implements a built-in function with the same name as an existing stored function. See [Section 11.2.5, “Function Name Parsing and Resolution”](function-resolution.md), for the rules describing how the server interprets references to different kinds of functions.
- If upgrade to MySQL 26.10 fails due to any of the issues outlined in [Section 3.6, “Preparing Your Installation for Upgrade”](upgrade-prerequisites.md), the server reverts all changes to the data directory. In this case, remove all redo log files and restart the MySQL 9.7 server on the existing data directory to address the errors. The redo log files (`ib_logfile*`) reside in the MySQL data directory by default. After the errors are fixed, perform a slow shutdown (by setting [`innodb_fast_shutdown=0`](innodb-parameters.md)) before attempting the upgrade again.