---
title: "MySQL :: MySQL 26.10 Reference Manual :: 7.9.1 Debugging a MySQL Server"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/debugging-server.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 7.9.1 Debugging a MySQL Server

If you are using some functionality that is very new in MySQL, you can try to run [**mysqld**](mysqld.md) with the [`--skip-new`](server-options.md) option (which disables all new, potentially unsafe functionality). See [Section B.3.3.3, “What to Do If MySQL Keeps Crashing”](crashing.md).

If [**mysqld**](mysqld.md) does not want to start, verify that you have no `my.cnf` files that interfere with your setup! You can check your `my.cnf` arguments with [**mysqld --print-defaults**](mysqld.md) and avoid using them by starting with [**mysqld --no-defaults...**](mysqld.md).

If [**mysqld**](mysqld.md) starts to eat up CPU or memory or if it “hangs,” you can use [**mysqladmin processlist status**](mysqladmin.md) to find out if someone is executing a query that takes a long time. It may be a good idea to run [**mysqladmin -i10 processlist status**](mysqladmin.md) in some window if you are experiencing performance problems or problems when new clients cannot connect.

The command [**mysqladmin debug**](mysqladmin.md) dumps some information about locks in use, used memory and query usage to the MySQL log file. This may help solve some problems. This command also provides some useful information even if you have not compiled MySQL for debugging!

If the problem is that some tables are getting slower and slower you should try to optimize the table with [`OPTIMIZE TABLE`](optimize-table.md) or [**myisamchk**](myisamchk.md). See [Chapter 7, *MySQL Server Administration*](server-administration.md). You should also check the slow queries with [`EXPLAIN`](explain.md).

You should also read the OS-specific section in this manual for problems that may be unique to your environment. See [Section 2.1, “General Installation Guidance”](general-installation-issues.md).