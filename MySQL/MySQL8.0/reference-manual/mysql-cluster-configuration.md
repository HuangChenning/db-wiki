---
title: "25.4 Configuration of NDB Cluster"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster-configuration.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

A MySQL server that is part of an NDB Cluster differs in one chief respect from a normal (nonclustered) MySQL server, in that it employs the [`NDB`](mysql-cluster.md) storage engine. This engine is also referred to sometimes as [`NDBCLUSTER`](mysql-cluster.md), although `NDB` is preferred.

To avoid unnecessary allocation of resources, the server is configured by default with the [`NDB`](mysql-cluster.md) storage engine disabled. To enable [`NDB`](mysql-cluster.md), you must modify the server's `my.cnf` configuration file, or start the server with the [`--ndbcluster`](mysql-cluster-options-variables.md) option.

This MySQL server is a part of the cluster, so it also must know how to access a management node to obtain the cluster configuration data. The default behavior is to look for the management node on `localhost`. However, should you need to specify that its location is elsewhere, this can be done in `my.cnf`, or with the [**mysql**](mysql.md) client. Before the [`NDB`](mysql-cluster.md) storage engine can be used, at least one management node must be operational, as well as any desired data nodes.

For more information about [`--ndbcluster`](mysql-cluster-options-variables.md) and other [**mysqld**](mysqld.md) options specific to NDB Cluster, see [Section 25.4.3.9.1, “MySQL Server Options for NDB Cluster”](mysql-cluster-options-variables.md).

For general information about installing NDB Cluster, see [Section 25.3, “NDB Cluster Installation”](mysql-cluster-installation.md).