---
title: "10.6 Optimizing for MyISAM Tables"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/optimizing-myisam.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

Skip to Main Content

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

The [`MyISAM`](myisam-storage-engine.md) storage engine performs best with read-mostly data or with low-concurrency operations, because table locks limit the ability to perform simultaneous updates. In MySQL, [`InnoDB`](innodb-storage-engine.md) is the default storage engine rather than `MyISAM`.

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")