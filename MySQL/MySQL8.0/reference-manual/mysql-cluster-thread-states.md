---
title: "10.14.8 NDB Cluster Thread States"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster-thread-states.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 10.14.8 NDB Cluster Thread States

- `Committing events to binlog`
- `Opening mysql.ndb_apply_status`
- `Processing events`
	The thread is processing events for binary logging.
- `Processing events from schema table`
	The thread is doing the work of schema replication.
- `Shutting down`
- `Syncing ndb table schema operation and             binlog`
	This is used to have a correct binary log of schema operations for NDB.
- `Waiting for allowed to take ndbcluster global             schema lock`
	The thread is waiting for permission to take a global schema lock.
- `Waiting for event from ndbcluster`
	The server is acting as an SQL node in an NDB Cluster, and is connected to a cluster management node.
- `Waiting for first event from ndbcluster`
- `Waiting for ndbcluster binlog update to reach             current position`
- `Waiting for ndbcluster global schema lock`
	The thread is waiting for a global schema lock held by another thread to be released.
- `Waiting for ndbcluster to start`
- `Waiting for schema epoch`
	The thread is waiting for a schema epoch (that is, a global checkpoint).