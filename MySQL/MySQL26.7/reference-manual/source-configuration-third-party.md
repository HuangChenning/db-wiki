---
title: "MySQL :: MySQL 26.7 Reference Manual :: 2.8.9 MySQL Configuration and Third-Party Tools"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/source-configuration-third-party.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 2.8.9 MySQL Configuration and Third-Party Tools

Third-party tools that need to determine the MySQL version from the MySQL source can read the `MYSQL_VERSION` file in the top-level source directory. The file lists the pieces of the version separately. For example, if the version is MySQL 9.5.0, the file looks like this:

```svg
MYSQL_VERSION_MAJOR=9
MYSQL_VERSION_MINOR=5
MYSQL_VERSION_PATCH=0
MYSQL_VERSION_EXTRA="INNOVATION"
```

To construct a five-digit number from the version components, use this formula:

```svg
MYSQL_VERSION_MAJOR*10000 + MYSQL_VERSION_MINOR*100 + MYSQL_VERSION_PATCH
```