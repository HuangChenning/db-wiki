---
title: "17.4 InnoDB Architecture"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/innodb-architecture.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

Skip to Main Content

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

The following diagram shows in-memory and on-disk structures that comprise the `InnoDB` storage engine architecture. For information about each structure, see [Section 17.5, “InnoDB In-Memory Structures”](innodb-in-memory-structures.md), and [Section 17.6, “InnoDB On-Disk Structures”](innodb-on-disk-structures.md).

**Figure 17.1 InnoDB Architecture**

![InnoDB architecture diagram showing in-memory and on-disk structures. In-memory structures include the buffer pool, adaptive hash index, change buffer, and log buffer. On-disk structures include tablespaces, redo logs, and doublewrite buffer files.](img/innodb-architecture-8-0.png)

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")