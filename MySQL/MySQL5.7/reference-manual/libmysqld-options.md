---
title: "27.6.3 Options with the Embedded Server"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/libmysqld-options.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 27.6.3 Options with the Embedded Server

Any options that may be given with the [**mysqld**](mysqld.md) server daemon, may be used with an embedded server library. Server options may be given in an array as an argument to the [`mysql_library_init()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-library-init.html), which initializes the server. They also may be given in an option file like `my.cnf`. To specify an option file for a C program, use the [`--defaults-file`](option-file-options.md) option as one of the elements of the second argument of the [`mysql_library_init()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-library-init.html) function. See [mysql\_library\_init()](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-library-init.html), for more information on the [`mysql_library_init()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-library-init.html) function.

Using option files can make it easier to switch between a client/server application and one where MySQL is embedded. Put common options under the `[server]` group. These are read by both MySQL versions. Client/server-specific options should go under the `[mysqld]` section. Put options specific to the embedded MySQL server library in the `[embedded]` section. Options specific to applications go under section labeled `[ApplicationName_SERVER]`. See [Section 4.2.2.2, “Using Option Files”](option-files.md).