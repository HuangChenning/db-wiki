---
title: "10.11 Optimizing Locking Operations"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/locking-issues.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

MySQL manages contention for table contents using [locking](glossary.md):

- Internal locking is performed within the MySQL server itself to manage contention for table contents by multiple threads. This type of locking is internal because it is performed entirely by the server and involves no other programs. See [Section 10.11.1, “Internal Locking Methods”](internal-locking.md).
- External locking occurs when the server and other programs lock [`MyISAM`](myisam-storage-engine.md) table files to coordinate among themselves which program can access the tables at which time. See [Section 10.11.5, “External Locking”](external-locking.md).