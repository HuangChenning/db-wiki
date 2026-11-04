---
title: "9.4.4 Reloading Delimited-Text Format Backups"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/reloading-delimited-text-dumps.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 9.4.4 Reloading Delimited-Text Format Backups

For backups produced with [**mysqldump --tab**](mysqldump.md), each table is represented in the output directory by an `.sql` file containing the [`CREATE TABLE`](create-table.md) statement for the table, and a `.txt` file containing the table data. To reload a table, first change location into the output directory. Then process the `.sql` file with [**mysql**](mysql.md) to create an empty table and process the `.txt` file to load the data into the table:

```
$> mysql db1 < t1.sql
$> mysqlimport db1 t1.txt
```

An alternative to using [**mysqlimport**](mysqlimport.md) to load the data file is to use the [`LOAD         DATA`](load-data.md) statement from within the [**mysql**](mysql.md) client:

```
mysql> USE db1;
mysql> LOAD DATA INFILE 't1.txt' INTO TABLE t1;
```

If you used any data-formatting options with [**mysqldump**](mysqldump.md) when you initially dumped the table, you must use the same options with [**mysqlimport**](mysqlimport.md) or [`LOAD         DATA`](load-data.md) to ensure proper interpretation of the data file contents:

```
$> mysqlimport --fields-terminated-by=,
         --fields-enclosed-by='"' --lines-terminated-by=0x0d0a db1 t1.txt
```

Or:

```
mysql> USE db1;
mysql> LOAD DATA INFILE 't1.txt' INTO TABLE t1
       FIELDS TERMINATED BY ',' FIELDS ENCLOSED BY '"'
       LINES TERMINATED BY '\r\n';
```