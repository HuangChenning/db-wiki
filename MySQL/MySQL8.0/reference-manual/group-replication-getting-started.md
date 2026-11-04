---
title: "20.2 Getting Started"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/group-replication-getting-started.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

MySQL Group Replication is provided as a plugin for the MySQL server; each server in a group requires configuration and installation of the plugin. This section provides a detailed tutorial with the steps required to create a replication group with at least three members.

Tip

To deploy multiple instances of MySQL, you can use [InnoDB Cluster](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/mysql-innodb-cluster.html) which enables you to easily administer a group of MySQL server instances in [MySQL Shell](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/). InnoDB Cluster wraps MySQL Group Replication in a programmatic environment that enables you easily deploy a cluster of MySQL instances to achieve high availability. In addition, InnoDB Cluster interfaces seamlessly with [MySQL Router](https://docs.oracle.com/cd/E17952_01/mysql-router-8.0-en/), which enables your applications to connect to the cluster without writing your own failover process. For similar use cases that do not require high availability, however, you can use [InnoDB ReplicaSet](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/mysql-innodb-replicaset.html). Installation instructions for MySQL Shell can be found [here](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/mysql-shell-install.html).