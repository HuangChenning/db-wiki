---
title: "A.8 MySQL 5.7 FAQ: Migration"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/faqs-migration.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

A.8.1. Where can I find information on how to upgrade or downgrade MySQL?

A.8.2. How has storage engine (table type) support changed in MySQL 5.7 from previous versions?

| **A.8.1.** | Where can I find information on how to upgrade or downgrade MySQL? |
| --- | --- |
|  | For detailed upgrade information, see [Section 2.10, “Upgrading MySQL”](upgrading.md). Do not skip a major version when upgrading, but rather complete the process in steps, upgrading from one major version to the next in each step. This may seem more complicated, but ultimately saves time and trouble. If you encounter problems during the upgrade, their origin is easier to identify, either by you or, if you have a MySQL Enterprise subscription, by MySQL support. |
| **A.8.2.** | How has storage engine (table type) support changed in MySQL 5.7 from previous versions? |
|  | Storage engine support has changed as follows:  - Support for `ISAM` tables was removed in MySQL 5.0 and you should now use the `MyISAM` storage engine in place of `ISAM`. To convert a table *`tblname`* from `ISAM` to `MyISAM`, simply issue a statement such as this one: 	``` 	ALTER TABLE tblname ENGINE=MYISAM; 	``` - Internal `RAID` for `MyISAM` tables was also removed in MySQL 5.0. This was formerly used to allow large tables in file systems that did not support file sizes greater than 2GB. All modern file systems allow for larger tables; in addition, there are now other solutions such as `MERGE` tables and views. - The [`VARCHAR`](char.md) column type now retains trailing spaces in all storage engines. - `MEMORY` tables (formerly known as `HEAP` tables) can also contain [`VARCHAR`](char.md) columns. |