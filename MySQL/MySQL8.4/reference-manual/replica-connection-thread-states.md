---
title: "10.14.7 Replication Connection Thread States"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/replica-connection-thread-states.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 10.14.7 Replication Connection Thread States

These thread states occur on a replica server but are associated with connection threads, not with the I/O or SQL threads.

- `Changing master`
	`Changing replication source`
	The thread is processing a [`CHANGE             REPLICATION SOURCE TO`](change-replication-source-to.md) statement.
- `Killing slave`
	The thread is processing a `STOP REPLICA` statement.
- `Opening master dump table`
	This state occurs after `Creating table from master             dump`.
- `Reading master dump table data`
	This state occurs after `Opening master dump             table`.
- `Rebuilding the index on master dump table`
	This state occurs after `Reading master dump table             data`.