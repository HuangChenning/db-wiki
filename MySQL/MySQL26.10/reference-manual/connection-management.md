---
title: "MySQL :: MySQL 26.10 Reference Manual :: 7.1.12 Connection Management"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/connection-management.html"
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

[26.7](https://dev.mysql.com/doc/refman/26.7/en/connection-management.html)  
[9.7 current](https://dev.mysql.com/doc/refman/9.7/en/connection-management.html)  
[8.4](https://dev.mysql.com/doc/refman/8.4/en/connection-management.html)  
[8.0](https://dev.mysql.com/doc/refman/8.0/en/connection-management.html)  

[8.0 Japanese](https://dev.mysql.com/doc/refman/8.0/ja/connection-management.html)

[MySQL 26.10 Reference Manual](https://dev.mysql.com/doc/refman/26.10/en/) / ... / Connection Management

### 7.1.12 Connection Management

This section describes how MySQL Server manages connections. This includes a description of the available connection interfaces, how the server uses connection handler threads, details about the administrative connection interface, and management of DNS lookups.

[PREV](sql-mode.md) [HOME](index.md) [UP](mysqld-server.md) [NEXT](connection-interfaces.md)

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb