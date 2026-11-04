---
title: "MySQL :: MySQL 26.7 Reference Manual :: 20.2 Getting Started"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/group-replication-getting-started.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 20.2 Getting Started

MySQL Group Replication is provided as a plugin for the MySQL server; each server in a group requires configuration and installation of the plugin. This section provides a detailed tutorial with the steps required to create a replication group with at least three members.

Tip

To deploy multiple instances of MySQL, you can use [InnoDB Cluster](https://dev.mysql.com/doc/mysql-shell/26.7/en/mysql-innodb-cluster.html) which enables you to easily administer a group of MySQL server instances in [MySQL Shell](https://dev.mysql.com/doc/mysql-shell/26.7/en/). InnoDB Cluster wraps MySQL Group Replication in a programmatic environment that enables you easily deploy a cluster of MySQL instances to achieve high availability. In addition, InnoDB Cluster interfaces seamlessly with [MySQL Router](https://dev.mysql.com/doc/mysql-router/26.7/en/), which enables your applications to connect to the cluster without writing your own failover process. For similar use cases that do not require high availability, however, you can use [InnoDB ReplicaSet](https://dev.mysql.com/doc/mysql-shell/26.7/en/mysql-innodb-replicaset.html). Installation instructions for MySQL Shell can be found [here](https://dev.mysql.com/doc/mysql-shell/26.7/en/mysql-shell-install.html).