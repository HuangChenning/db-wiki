---
title: "MySQL :: MySQL 26.7 Reference Manual :: 24 InnoDB ReplicaSet"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/mysql-innodb-replicaset-introduction.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## Chapter 24 InnoDB ReplicaSet

This chapter introduces MySQL InnoDB ReplicaSet, which combines MySQL technologies to enable you to deploy and administer [Chapter 19, *Replication*](replication.md). This content is a high-level overview of InnoDB ReplicaSet, for full documentation, see [MySQL InnoDB ReplicaSet](https://dev.mysql.com/doc/mysql-shell/26.7/en/mysql-innodb-replicaset.html).

An InnoDB ReplicaSet consists of at least two MySQL Server instances, and it provides all of the MySQL Replication features you are familiar with, such as read scale-out and data security. InnoDB ReplicaSet uses the following MySQL technologies:

- [MySQL Shell](https://dev.mysql.com/doc/mysql-shell/26.7/en/), which is an advanced client and code editor for MySQL.
- MySQL Server, and [Chapter 19, *Replication*](replication.md), which enables a set of MySQL instances to provide availability and asynchronous read scale-out. InnoDB ReplicaSet provides an alternative, easy to use programmatic way to work with Replication.
- [MySQL Router](https://dev.mysql.com/doc/mysql-router/26.7/en/), a lightweight middleware that provides transparent routing between your application and InnoDB ReplicaSet.

The interface to an InnoDB ReplicaSet is similar to [MySQL InnoDB Cluster](https://dev.mysql.com/doc/mysql-shell/26.7/en/mysql-innodb-cluster.html), you use MySQL Shell to work with MySQL Server instances as a ReplicaSet, and MySQL Router is also tightly integrated in the same way as InnoDB Cluster.

Being based on MySQL Replication, an InnoDB ReplicaSet has a single primary, which replicates to one or more secondary instances. An InnoDB ReplicaSet does not provide all of the features which InnoDB Cluster provides, such as automatic failover, or multi-primary mode. But, it does support features such as configuring, adding, and removing instances in a similar way. You can manually switch over or fail over to a secondary instance, for example in the event of a failure. You can even adopt an existing Replication deployment and then administer it as an InnoDB ReplicaSet.

You work with InnoDB ReplicaSet using the [AdminAPI](https://dev.mysql.com/doc/mysql-shell/26.7/en/admin-api-overview.html), provided as part of MySQL Shell. AdminAPI is available in JavaScript and Python, and is well suited to scripting and automation of deployments of MySQL to achieve high-availability and scalability. By using MySQL Shell's AdminAPI, you can avoid the need to configure many instances manually. Instead, AdminAPI provides an effective modern interface to sets of MySQL instances and enables you to provision, administer, and monitor your deployment from one central tool.

To get started with InnoDB ReplicaSet you need to [download](https://dev.mysql.com/downloads/shell/) and [install](https://dev.mysql.com/doc/mysql-shell/26.7/en/mysql-shell-install.html) MySQL Shell. You need some hosts with MySQL Server instances [installed](installing.md), and you can also [install](https://dev.mysql.com/doc/mysql-router/26.7/en/mysql-router-installation.html) MySQL Router.

InnoDB ReplicaSet supports [MySQL Clone](clone-plugin.md), which enables you to provision instances simply. In the past, to provision a new instance before it joined a MySQL Replication deployment, you would need to somehow manually transfer the transactions to the joining instance. This could involve making file copies, manually copying them, and so on. You can simply [add an instance](https://dev.mysql.com/doc/mysql-shell/26.7/en/add-instance-replicaset.html) to the replica set and it is automatically provisioned.

Similarly, InnoDB ReplicaSet is tightly integrated with [MySQL Router](https://dev.mysql.com/doc/mysql-router/26.7/en/), and you can use AdminAPI to [work with](https://dev.mysql.com/doc/mysql-shell/26.7/en/registered-routers.html) them together. MySQL Router can automatically configure itself based on an InnoDB ReplicaSet, in a process called [bootstrapping](https://dev.mysql.com/doc/mysql-shell/26.7/en/admin-api-bootstrapping-router.html), which removes the need for you to configure routing manually. MySQL Router then transparently connects client applications to the InnoDB ReplicaSet, providing routing and load-balancing for client connections. This integration also enables you to administer some aspects of a MySQL Router bootstrapped against an InnoDB ReplicaSet using AdminAPI. InnoDB ReplicaSet status information includes details about MySQL Routers bootstrapped against the ReplicaSet. Operations enable you to [create MySQL Router users](https://dev.mysql.com/doc/mysql-shell/26.7/en/configuring-router-user.html) at the ReplicaSet level, to work with the MySQL Routers bootstrapped against the ReplicaSet, and so on.

For more information on these technologies, see the user documentation linked in the descriptions. In addition to this user documentation, there is developer documentation for all AdminAPI methods in the MySQL Shell JavaScript API Reference or MySQL Shell Python API Reference, available from [Connectors and APIs](https://dev.mysql.com/doc/index-connectors.html).