---
title: "9.4.2 Reloading SQL-Format Backups"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/reloading-sql-format-dumps.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 9.4.2 Reloading SQL-Format Backups

To reload a dump file written by [**mysqldump**](mysqldump.md) that consists of SQL statements, use it as input to the [**mysql**](mysql.md) client. If the dump file was created by [**mysqldump**](mysqldump.md) with the [`--all-databases`](mysqldump.md) or [`--databases`](mysqldump.md) option, it contains [`CREATE DATABASE`](create-database.md) and [`USE`](use.md) statements and it is not necessary to specify a default database into which to load the data:

```
$> mysql < dump.sql
```

Alternatively, from within [**mysql**](mysql.md), use a `source` command:

```
mysql> source dump.sql
```

If the file is a single-database dump not containing [`CREATE DATABASE`](create-database.md) and [`USE`](use.md) statements, create the database first (if necessary):

```
$> mysqladmin create db1
```

Then specify the database name when you load the dump file:

```
$> mysql db1 < dump.sql
```

Alternatively, from within [**mysql**](mysql.md), create the database, select it as the default database, and load the dump file:

```
mysql> CREATE DATABASE IF NOT EXISTS db1;
mysql> USE db1;
mysql> source dump.sql
```

Note

For Windows PowerShell users: Because the "<" character is reserved for future use in PowerShell, an alternative approach is required, such as using quotes `cmd.exe /c "mysql           < dump.sql"`.