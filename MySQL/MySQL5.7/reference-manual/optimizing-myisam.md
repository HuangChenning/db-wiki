---
title: "8.6 Optimizing for MyISAM Tables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/optimizing-myisam.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

Skip to Main Content

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

The [`MyISAM`](myisam-storage-engine.md) storage engine performs best with read-mostly data or with low-concurrency operations, because table locks limit the ability to perform simultaneous updates. In MySQL, [`InnoDB`](innodb-storage-engine.md) is the default storage engine rather than `MyISAM`.

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")