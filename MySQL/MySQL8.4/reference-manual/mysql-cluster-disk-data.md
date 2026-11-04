---
title: "25.6.11 NDB Cluster Disk Data Tables"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/mysql-cluster-disk-data.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 25.6.11 NDB Cluster Disk Data Tables

NDB Cluster supports storing nonindexed columns of [`NDB`](mysql-cluster.md) tables on disk, rather than in RAM. Column data and logging metadata are kept in data files and undo log files, conceptualized as tablespaces and log file groups, as described in the next section—see [Section 25.6.11.1, “NDB Cluster Disk Data Objects”](mysql-cluster-disk-data-objects.md).

NDB Cluster Disk Data performance can be influenced by a number of configuration parameters. For information about these parameters and their effects, see [Disk Data Configuration Parameters](mysql-cluster-ndbd-definition.md), and [Disk Data and GCP Stop errors](mysql-cluster-ndbd-definition.md).

You should also set the [`DiskDataUsingSameDisk`](mysql-cluster-ndbd-definition.md) data node configuration parameter to `false` when using separate disks for Disk Data files.

For more information, see the following: