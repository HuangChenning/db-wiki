---
title: "14.10.1 Enabling File Formats"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-file-format-enabling.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 14.10.1 Enabling File Formats

The [`innodb_file_format`](innodb-parameters.md) configuration option enables an `InnoDB` file format for [file-per-table](glossary.md) tablespaces.

`Barracuda` is the default [`innodb_file_format`](innodb-parameters.md) setting. In earlier releases, the default file format was `Antelope`.

Note

The [`innodb_file_format`](innodb-parameters.md) configuration option is deprecated and may be removed in a future release. For more information, see [Section 14.10, “InnoDB File-Format Management”](innodb-file-format.md).

You can set the value of [`innodb_file_format`](innodb-parameters.md) on the command line when you start [**mysqld**](mysqld.md), or in the option file (`my.cnf` on Unix, `my.ini` on Windows). You can also change it dynamically with a `SET GLOBAL` statement.

```
SET GLOBAL innodb_file_format=Barracuda;
```

#### Usage notes

- `InnoDB` file format settings do not apply to tables stored in [general tablespaces](general-tablespaces.md). General tablespaces provide support for all row formats and associated features. For more information, see [Section 14.6.3.3, “General Tablespaces”](general-tablespaces.md).
- The [`innodb_file_format`](innodb-parameters.md) setting is not applicable when using the `TABLESPACE           [=] innodb_system` table option with [`CREATE TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md) to store a `DYNAMIC` table in the system tablespace.
- The [`innodb_file_format`](innodb-parameters.md) setting is ignored when creating tables that use the `DYNAMIC` row format. For more information, see [DYNAMIC Row Format](innodb-row-format.md).