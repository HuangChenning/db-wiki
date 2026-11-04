---
title: "21.6.11 NDB Cluster Disk Data Tables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-disk-data.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.6.11 NDB Cluster Disk Data Tables

It is possible to store the nonindexed columns of [`NDB`](mysql-cluster.md) tables on disk, rather than in RAM.

As part of implementing NDB Cluster Disk Data work, a number of improvements were made in NDB Cluster for the efficient handling of very large amounts (terabytes) of data during node recovery and restart. These include a “no-steal” algorithm for synchronizing a starting node with very large data sets. For more information, see the paper *[Recovery Principles of NDB Cluster 5.1](http://www.vldb2005.org/program/paper/wed/p1108-ronstrom.pdf)*, by NDB Cluster developers Mikael Ronström and Jonas Oreland.

NDB Cluster Disk Data performance can be influenced by a number of configuration parameters. For information about these parameters and their effects, see *[NDB Cluster Disk Data configuration parameters](mysql-cluster-ndbd-definition.md)* and *[NDB Cluster Disk Data storage and GCP Stop errors](mysql-cluster-ndbd-definition.md)*

The performance of an NDB Cluster that uses Disk Data storage can also be greatly improved by separating data node file systems from undo log files and tablespace data files, which can be done using symbolic links. For more information, see [Section 21.6.11.2, “Using Symbolic Links with Disk Data Objects”](mysql-cluster-disk-data-symlinks.md).