---
title: "Chapter 20 Group Replication"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/group-replication.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

This chapter explains Group Replication in MySQL 9.7, and how to install, configure and monitor groups. MySQL Group Replication enables you to create elastic, highly-available, fault-tolerant replication topologies.

Groups can operate in a single-primary mode with automatic primary election, where only one server accepts updates at a time. Alternatively, groups can be deployed in multi-primary mode, where all servers can accept updates, even if they are issued concurrently.

There is a built-in group membership service that keeps the view of the group consistent and available for all servers at any given point in time. Servers can leave and join the group and the view is updated accordingly. Sometimes servers can leave the group unexpectedly, in which case the failure detection mechanism detects this and notifies the group that the view has changed. This is all automatic.

Group Replication guarantees that the database service is continuously available. However, it is important to understand that if one of the group members becomes unavailable, the clients connected to that group member must be redirected, or failed over, to a different server in the group, using a connector, load balancer, router, or some form of middleware. Group Replication does not have an inbuilt method to do this. For example, see [MySQL Router 9.7](https://docs.oracle.com/cd/E17952_01/mysql-router-9.7-en/).

Group Replication is provided as a plugin to MySQL Server. You can follow the instructions in this chapter to configure the plugin on each of the server instances that you want in the group, start up the group, and monitor and administer the group. An alternative way to deploy a group of MySQL server instances is by using InnoDB Cluster.

Tip

To deploy multiple instances of MySQL, you can use [InnoDB Cluster](https://docs.oracle.com/cd/E17952_01/mysql-shell-9.7-en/mysql-innodb-cluster.html) which enables you to easily administer a group of MySQL server instances in [MySQL Shell](https://docs.oracle.com/cd/E17952_01/mysql-shell-9.7-en/). InnoDB Cluster wraps MySQL Group Replication in a programmatic environment that enables you easily deploy a cluster of MySQL instances to achieve high availability. In addition, InnoDB Cluster interfaces seamlessly with [MySQL Router](https://docs.oracle.com/cd/E17952_01/mysql-router-9.7-en/), which enables your applications to connect to the cluster without writing your own failover process. For similar use cases that do not require high availability, however, you can use [InnoDB ReplicaSet](https://docs.oracle.com/cd/E17952_01/mysql-shell-9.7-en/mysql-innodb-replicaset.html). Installation instructions for MySQL Shell can be found [here](https://docs.oracle.com/cd/E17952_01/mysql-shell-9.7-en/mysql-shell-install.html).

MySQL 9.7 and later support a number of MySQL components for use with MySQL Group Replication. See [Section 7.5.6, “Replication Components”](replication-components.md), for more information.

This chapter is structured as follows:

- [Section 20.1, “Group Replication Background”](group-replication-background.md) provides an introduction to groups and how Group Replication works.
- [Section 20.2, “Getting Started”](group-replication-getting-started.md) explains how to configure multiple MySQL Server instances to create a group.
- [Section 20.3, “Requirements and Limitations”](group-replication-requirements-and-limitations.md) explains architecture and setup requirements and limitations for Group Replication.
- [Section 20.4, “Monitoring Group Replication”](group-replication-monitoring.md) explains how to monitor a group.
- [Section 20.5, “Group Replication Operations”](group-replication-operations.md) explains how to work with a group.
- [Section 20.6, “Group Replication Security”](group-replication-security.md) explains how to secure a group.
- [Section 20.7, “Group Replication Performance and Troubleshooting”](group-replication-performance.md) explains how to fine tune performance for a group.
- [Section 20.8, “Upgrading Group Replication”](group-replication-upgrade.md) explains how to upgrade a group.
- [Section 20.9, “Group Replication Variables”](group-replication-options.md) is a reference for the system variables specific to Group Replication.
- [Section 20.10, “Frequently Asked Questions”](group-replication-frequently-asked-questions.md) provides answers to some technical questions about deploying and operating Group Replication.