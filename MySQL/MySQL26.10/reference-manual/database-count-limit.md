---
title: "MySQL :: MySQL 26.10 Reference Manual :: 10.4.5 Limits on Number of Databases and Tables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/database-count-limit.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 10.4.5 Limits on Number of Databases and Tables

MySQL has no limit on the number of databases. The underlying file system may have a limit on the number of directories.

MySQL has no limit on the number of tables. The underlying file system may have a limit on the number of files that represent tables. Individual storage engines may impose engine-specific constraints. `InnoDB` permits up to 4 billion tables.