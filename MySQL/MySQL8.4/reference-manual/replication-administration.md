---
title: "19.1.7 Common Replication Administration Tasks"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/replication-administration.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 19.1.7 Common Replication Administration Tasks

Once replication has been started it executes without requiring much regular administration. This section describes how to check the status of replication, how to pause a replica, and how to skip a failed transaction on a replica.

Tip

To deploy multiple instances of MySQL, you can use [InnoDB Cluster](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.4-en/mysql-innodb-cluster.html) which enables you to easily administer a group of MySQL server instances in [MySQL Shell](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.4-en/). InnoDB Cluster wraps MySQL Group Replication in a programmatic environment that enables you easily deploy a cluster of MySQL instances to achieve high availability. In addition, InnoDB Cluster interfaces seamlessly with [MySQL Router](https://docs.oracle.com/cd/E17952_01/mysql-router-8.4-en/), which enables your applications to connect to the cluster without writing your own failover process. For similar use cases that do not require high availability, however, you can use [InnoDB ReplicaSet](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.4-en/mysql-innodb-replicaset.html). Installation instructions for MySQL Shell can be found [here](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.4-en/mysql-shell-install.html).