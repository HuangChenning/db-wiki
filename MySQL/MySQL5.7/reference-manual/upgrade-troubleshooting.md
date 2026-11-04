---
title: "2.10.11 Upgrade Troubleshooting"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/upgrade-troubleshooting.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 2.10.11 Upgrade Troubleshooting

- If problems occur, such as that the new [**mysqld**](mysqld.md) server does not start, verify that you do not have an old `my.cnf` file from your previous installation. You can check this with the [`--print-defaults`](option-file-options.md) option (for example, [**mysqld --print-defaults**](mysqld.md)). If this command displays anything other than the program name, you have an active `my.cnf` file that affects server or client operation.
- If, after an upgrade, you experience problems with compiled client programs, such as `Commands out of           sync` or unexpected core dumps, you probably have used old header or library files when compiling your programs. In this case, check the date for your `mysql.h` file and `libmysqlclient.a` library to verify that they are from the new MySQL distribution. If not, recompile your programs with the new headers and libraries. Recompilation might also be necessary for programs compiled against the shared client library if the library major version number has changed (for example, from `libmysqlclient.so.15` to `libmysqlclient.so.16`).
- If you have created a loadable function with a given name and upgrade MySQL to a version that implements a new built-in function with the same name, the loadable function becomes inaccessible. To correct this, use [`DROP           FUNCTION`](drop-function.md) to drop the loadable function, and then use [`CREATE FUNCTION`](create-function.md) to re-create the loadable function with a different nonconflicting name. The same is true if the new version of MySQL implements a built-in function with the same name as an existing stored function. See [Section 9.2.5, “Function Name Parsing and Resolution”](function-resolution.md), for the rules describing how the server interprets references to different kinds of functions.