---
title: "25.4.4 Using High-Speed Interconnects with NDB Cluster"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/mysql-cluster-interconnects.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 25.4.4 Using High-Speed Interconnects with NDB Cluster

Even before design of [`NDBCLUSTER`](mysql-cluster.md) began in 1996, it was evident that one of the major problems to be encountered in building parallel databases would be communication between the nodes in the network. For this reason, [`NDBCLUSTER`](mysql-cluster.md) was designed from the very beginning to permit the use of a number of different data transport mechanisms, or transporters.

NDB Cluster supports three of these (see [Section 25.2.1, “NDB Cluster Core Concepts”](mysql-cluster-basics.md)). A fourth transporter, Scalable Coherent Interface (SCI), was also supported in very old versions of `NDB`. This required specialized hardware, software, and MySQL binaries that are no longer available.