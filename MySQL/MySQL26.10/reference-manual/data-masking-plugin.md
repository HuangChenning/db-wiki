---
title: "MySQL :: MySQL 26.10 Reference Manual :: 8.5.4 MySQL Enterprise Data Masking Plugin"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/data-masking-plugin.html"
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

[26.7](https://dev.mysql.com/doc/refman/26.7/en/data-masking-plugin.html)  
[9.7 current](https://dev.mysql.com/doc/refman/9.7/en/data-masking-plugin.html)  
[8.4](https://dev.mysql.com/doc/refman/8.4/en/data-masking-plugin.html)  
[8.0](https://dev.mysql.com/doc/refman/8.0/en/data-masking-plugin.html)  

[8.0 Japanese](https://dev.mysql.com/doc/refman/8.0/ja/)

[MySQL 26.10 Reference Manual](https://dev.mysql.com/doc/refman/26.10/en/) / ... / MySQL Enterprise Data Masking Plugin

### 8.5.4 MySQL Enterprise Data Masking Plugin

MySQL Enterprise Data Masking is based on a plugin library that implements these elements:

- A server-side plugin named `data_masking`.
- A set of loadable functions provides an SQL-level API for performing masking and de-identification operations. Some of these functions require the [`SUPER`](privileges-provided.md) privilege.

[PREV](data-masking-policy-usage.md) [HOME](index.md) [UP](data-masking.md) [NEXT](data-masking-plugin-installation.md)

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb