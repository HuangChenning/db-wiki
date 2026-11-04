---
title: "15.1 Setting the Storage Engine"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/storage-engine-setting.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

When you create a new table, you can specify which storage engine to use by adding an `ENGINE` table option to the [`CREATE TABLE`](create-table.md) statement:

```
-- ENGINE=INNODB not needed unless you have set a different
-- default storage engine.
CREATE TABLE t1 (i INT) ENGINE = INNODB;
-- Simple table definitions can be switched from one to another.
CREATE TABLE t2 (i INT) ENGINE = CSV;
CREATE TABLE t3 (i INT) ENGINE = MEMORY;
```

When you omit the `ENGINE` option, the default storage engine is used. The default engine is [`InnoDB`](innodb-storage-engine.md) in MySQL 5.7. You can specify the default engine by using the [`--default-storage-engine`](server-system-variables.md) server startup option, or by setting the [`default-storage-engine`](server-system-variables.md) option in the `my.cnf` configuration file.

You can set the default storage engine for the current session by setting the [`default_storage_engine`](server-system-variables.md) variable:

```
SET default_storage_engine=NDBCLUSTER;
```

The storage engine for `TEMPORARY` tables created with [`CREATE       TEMPORARY TABLE`](create-table.md) can be set separately from the engine for permanent tables by setting the [`default_tmp_storage_engine`](server-system-variables.md), either at startup or at runtime.

To convert a table from one storage engine to another, use an [`ALTER TABLE`](alter-table.md) statement that indicates the new engine:

```
ALTER TABLE t ENGINE = InnoDB;
```

See [Section 13.1.18, “CREATE TABLE Statement”](create-table.md), and [Section 13.1.8, “ALTER TABLE Statement”](alter-table.md).

If you try to use a storage engine that is not compiled in or that is compiled in but deactivated, MySQL instead creates a table using the default storage engine. For example, in a replication setup, perhaps your source server uses `InnoDB` tables for maximum safety, but the replica servers use other storage engines for speed at the expense of durability or concurrency.

By default, a warning is generated whenever [`CREATE TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md) cannot use the default storage engine. To prevent confusing, unintended behavior if the desired engine is unavailable, enable the [`NO_ENGINE_SUBSTITUTION`](sql-mode.md) SQL mode. If the desired engine is unavailable, this setting produces an error instead of a warning, and the table is not created or altered. See [Section 5.1.10, “Server SQL Modes”](sql-mode.md).

For new tables, MySQL always creates an `.frm` file to hold the table and column definitions. The table's index and data may be stored in one or more other files, depending on the storage engine. The server creates the `.frm` file above the storage engine level. Individual storage engines create any additional files required for the tables that they manage. If a table name contains special characters, the names for the table files contain encoded versions of those characters as described in [Section 9.2.4, “Mapping of Identifiers to File Names”](identifier-mapping.md).