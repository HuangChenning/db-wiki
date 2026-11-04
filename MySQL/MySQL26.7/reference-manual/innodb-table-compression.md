---
title: "MySQL :: MySQL 26.7 Reference Manual :: 17.9.1 InnoDB Table Compression"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/innodb-table-compression.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

[Documentation Home](https://dev.mysql.com/doc/)

---

MySQL 26.7 Reference Manual

Related Documentation

[MySQL 26.7 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.7/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.7-en.pdf) - 42.0Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.7-en.a4.pdf) - 42.1Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.7-en.man-gpl.tar.gz) - 272.1Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.7-en.man-gpl.zip) - 378.3Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.7.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.7.info.zip) - 4.2Mb

version 26.7

[26.10](https://dev.mysql.com/doc/refman/26.10/en/innodb-table-compression.html)  
[9.7 current](https://dev.mysql.com/doc/refman/9.7/en/innodb-table-compression.html)  
[8.4](https://dev.mysql.com/doc/refman/8.4/en/innodb-table-compression.html)  
[8.0](https://dev.mysql.com/doc/refman/8.0/en/innodb-table-compression.html)  

[8.0 Japanese](https://dev.mysql.com/doc/refman/8.0/ja/innodb-table-compression.html)

[MySQL 26.7 Reference Manual](https://dev.mysql.com/doc/refman/26.7/en/) / ... / InnoDB Table Compression

### 17.9.1 InnoDB Table Compression

This section describes `InnoDB` table compression, which is supported with `InnoDB` tables that reside in [file\_per\_table](glossary.md) tablespaces or [general tablespaces](glossary.md). Table compression is enabled using the `ROW_FORMAT=COMPRESSED` attribute with [`CREATE TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md).

[PREV](innodb-compression.md) [HOME](index.md) [UP](innodb-compression.md) [NEXT](innodb-compression-background.md)

Related Documentation

[MySQL 26.7 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.7/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.7-en.pdf) - 42.0Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.7-en.a4.pdf) - 42.1Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.7-en.man-gpl.tar.gz) - 272.1Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.7-en.man-gpl.zip) - 378.3Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.7.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.7.info.zip) - 4.2Mb