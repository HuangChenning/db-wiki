---
title: "MySQL :: MySQL 26.7 Reference Manual :: 25.6.7 Adding NDB Cluster Data Nodes Online"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/mysql-cluster-online-add-node.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 25.6.7 Adding NDB Cluster Data Nodes Online

This section describes how to add NDB Cluster data nodes “online”—that is, without needing to shut down the cluster completely and restart it as part of the process.

Important

Currently, you must add new data nodes to an NDB Cluster as part of a new node group. In addition, it is not possible to change the number of fragment replicas (or the number of nodes per node group) online.