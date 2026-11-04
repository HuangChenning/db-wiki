---
title: "MySQL :: MySQL 26.7 Reference Manual :: 9.4.2 Reloading SQL-Format Backups"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/reloading-sql-format-dumps.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 9.4.2 Reloading SQL-Format Backups

To reload a dump file written by [**mysqldump**](mysqldump.md) that consists of SQL statements, use it as input to the [**mysql**](mysql.md) client. If the dump file was created by [**mysqldump**](mysqldump.md) with the [`--all-databases`](mysqldump.md) or [`--databases`](mysqldump.md) option, it contains [`CREATE DATABASE`](create-database.md) and [`USE`](use.md) statements and it is not necessary to specify a default database into which to load the data:

```svg
$> mysql < dump.sql
```

Alternatively, from within [**mysql**](mysql.md), use a `source` command:

```sql
mysql> source dump.sql
```

If the file is a single-database dump not containing [`CREATE DATABASE`](create-database.md) and [`USE`](use.md) statements, create the database first (if necessary):

```svg
$> mysqladmin create db1
```

Then specify the database name when you load the dump file:

```svg
$> mysql db1 < dump.sql
```

Alternatively, from within [**mysql**](mysql.md), create the database, select it as the default database, and load the dump file:

```sql
mysql> CREATE DATABASE IF NOT EXISTS db1;
mysql> USE db1;
mysql> source dump.sql
```

Note

For Windows PowerShell users: Because the "<" character is reserved for future use in PowerShell, an alternative approach is required, such as using quotes `cmd.exe /c "mysql           < dump.sql"`.