---
title: "MySQL :: MySQL 26.10 Reference Manual :: 10.5 Optimizing for InnoDB Tables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/optimizing-innodb.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

[Documentation Home](https://dev.mysql.com/doc/)

---

MySQL 26.10 Reference Manual

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb

version 26.10

[26.7](https://dev.mysql.com/doc/refman/26.7/en/optimizing-innodb.html)  
[9.7 current](https://dev.mysql.com/doc/refman/9.7/en/optimizing-innodb.html)  
[8.4](https://dev.mysql.com/doc/refman/8.4/en/optimizing-innodb.html)  
[8.0](https://dev.mysql.com/doc/refman/8.0/en/optimizing-innodb.html)  

[8.0 Japanese](https://dev.mysql.com/doc/refman/8.0/ja/optimizing-innodb.html)

[MySQL 26.10 Reference Manual](https://dev.mysql.com/doc/refman/26.10/en/) / [Optimization](optimization.md) / Optimizing for InnoDB Tables

## 10.5 Optimizing for InnoDB Tables

[`InnoDB`](innodb-storage-engine.md) is the storage engine that MySQL customers typically use in production databases where reliability and concurrency are important. `InnoDB` is the default storage engine in MySQL. This section explains how to optimize database operations for `InnoDB` tables.

[PREV](column-count-limit.md) [HOME](index.md) [UP](optimization.md) [NEXT](optimizing-innodb-storage-layout.md)

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb