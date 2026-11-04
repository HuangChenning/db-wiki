---
title: "7.4.1 Dumping Data in SQL Format with mysqldump"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysqldump-sql-format.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 7.4.1 Dumping Data in SQL Format with mysqldump

This section describes how to use [**mysqldump**](mysqldump.md) to create SQL-format dump files. For information about reloading such dump files, see [Section 7.4.2, “Reloading SQL-Format Backups”](reloading-sql-format-dumps.md).

By default, [**mysqldump**](mysqldump.md) writes information as SQL statements to the standard output. You can save the output in a file:

```
$> mysqldump [arguments] > file_name
```

To dump all databases, invoke [**mysqldump**](mysqldump.md) with the [`--all-databases`](mysqldump.md) option:

```
$> mysqldump --all-databases > dump.sql
```

To dump only specific databases, name them on the command line and use the [`--databases`](mysqldump.md) option:

```
$> mysqldump --databases db1 db2 db3 > dump.sql
```

The [`--databases`](mysqldump.md) option causes all names on the command line to be treated as database names. Without this option, [**mysqldump**](mysqldump.md) treats the first name as a database name and those following as table names.

With [`--all-databases`](mysqldump.md) or [`--databases`](mysqldump.md), [**mysqldump**](mysqldump.md) writes [`CREATE         DATABASE`](create-database.md) and [`USE`](use.md) statements prior to the dump output for each database. This ensures that when the dump file is reloaded, it creates each database if it does not exist and makes it the default database so database contents are loaded into the same database from which they came. If you want to cause the dump file to force a drop of each database before recreating it, use the [`--add-drop-database`](mysqldump.md) option as well. In this case, [**mysqldump**](mysqldump.md) writes a [`DROP DATABASE`](drop-database.md) statement preceding each [`CREATE DATABASE`](create-database.md) statement.

To dump a single database, name it on the command line:

```
$> mysqldump --databases test > dump.sql
```

In the single-database case, it is permissible to omit the [`--databases`](mysqldump.md) option:

```
$> mysqldump test > dump.sql
```

The difference between the two preceding commands is that without [`--databases`](mysqldump.md), the dump output contains no [`CREATE         DATABASE`](create-database.md) or [`USE`](use.md) statements. This has several implications:

- When you reload the dump file, you must specify a default database name so that the server knows which database to reload.
- For reloading, you can specify a database name different from the original name, which enables you to reload the data into a different database.
- If the database to be reloaded does not exist, you must create it first.
- Because the output contains no [`CREATE             DATABASE`](create-database.md) statement, the [`--add-drop-database`](mysqldump.md) option has no effect. If you use it, it produces no [`DROP DATABASE`](drop-database.md) statement.

To dump only specific tables from a database, name them on the command line following the database name:

```
$> mysqldump test t1 t3 t7 > dump.sql
```