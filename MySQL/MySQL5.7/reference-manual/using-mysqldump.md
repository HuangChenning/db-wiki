---
title: "7.4 Using mysqldump for Backups"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/using-mysqldump.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

This section describes how to use [**mysqldump**](mysqldump.md) to produce dump files, and how to reload dump files. A dump file can be used in several ways:

- As a backup to enable data recovery in case of data loss.
- As a source of data for setting up replicas.
- As a source of data for experimentation:
	- To make a copy of a database that you can use without changing the original data.
	- To test potential upgrade incompatibilities.

[**mysqldump**](mysqldump.md) produces two types of output, depending on whether the [`--tab`](mysqldump.md) option is given:

- Without [`--tab`](mysqldump.md), [**mysqldump**](mysqldump.md) writes SQL statements to the standard output. This output consists of `CREATE` statements to create dumped objects (databases, tables, stored routines, and so forth), and `INSERT` statements to load data into tables. The output can be saved in a file and reloaded later using [**mysql**](mysql.md) to recreate the dumped objects. Options are available to modify the format of the SQL statements, and to control which objects are dumped.
- With [`--tab`](mysqldump.md), [**mysqldump**](mysqldump.md) produces two output files for each dumped table. The server writes one file as tab-delimited text, one line per table row. This file is named ``*`tbl_name`*.txt`` in the output directory. The server also sends a [`CREATE TABLE`](create-table.md) statement for the table to [**mysqldump**](mysqldump.md), which writes it as a file named ``*`tbl_name`*.sql`` in the output directory.