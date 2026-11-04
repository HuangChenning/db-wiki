---
title: "MySQL :: MySQL 26.7 Reference Manual :: 20.6 Group Replication Security"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/group-replication-security.html"
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

[26.10](https://dev.mysql.com/doc/refman/26.10/en/group-replication-security.html)  
[9.7 current](https://dev.mysql.com/doc/refman/9.7/en/group-replication-security.html)  
[8.4](https://dev.mysql.com/doc/refman/8.4/en/group-replication-security.html)  
[8.0](https://dev.mysql.com/doc/refman/8.0/en/group-replication-security.html)  

[8.0 Japanese](https://dev.mysql.com/doc/refman/8.0/ja/group-replication-security.html)

[MySQL 26.7 Reference Manual](https://dev.mysql.com/doc/refman/26.7/en/) / [Group Replication](group-replication.md) / Group Replication Security

## 20.6 Group Replication Security

This section explains how to secure a group, securing the connections between members of a group, or by establishing a security perimeter using an IP address allowlist.

[PREV](group-replication-enterprise-backup.md) [HOME](index.md) [UP](group-replication.md) [NEXT](group-replication-connection-security.md)

Related Documentation

[MySQL 26.7 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.7/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.7-en.pdf) - 42.0Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.7-en.a4.pdf) - 42.1Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.7-en.man-gpl.tar.gz) - 272.1Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.7-en.man-gpl.zip) - 378.3Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.7.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.7.info.zip) - 4.2Mb