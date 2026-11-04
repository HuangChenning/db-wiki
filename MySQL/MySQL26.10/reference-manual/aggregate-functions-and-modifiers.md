---
title: "MySQL :: MySQL 26.10 Reference Manual :: 14.19 Aggregate Functions"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/aggregate-functions-and-modifiers.html"
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

[26.7](https://dev.mysql.com/doc/refman/26.7/en/aggregate-functions-and-modifiers.html)  
[9.7 current](https://dev.mysql.com/doc/refman/9.7/en/aggregate-functions-and-modifiers.html)  
[8.4](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions-and-modifiers.html)  
[8.0](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions-and-modifiers.html)  

[8.0 Japanese](https://dev.mysql.com/doc/refman/8.0/ja/aggregate-functions-and-modifiers.html)

[MySQL 26.10 Reference Manual](https://dev.mysql.com/doc/refman/26.10/en/) / [Functions and Operators](functions.md) / Aggregate Functions

## 14.19 Aggregate Functions

Aggregate functions operate on sets of values. They are often used with a `GROUP BY` clause to group values into subsets. This section describes most aggregate functions. For information about aggregate functions that operate on geometry values, see [Section 14.16.12, “Spatial Aggregate Functions”](spatial-aggregate-functions.md).

[PREV](replication-functions-synchronization.md) [HOME](index.md) [UP](functions.md) [NEXT](aggregate-functions.md)

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb