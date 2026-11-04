---
title: "8.14.8 Replication Replica Connection Thread States"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/replica-connection-thread-states.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.14.8 Replication Replica Connection Thread States

These thread states occur on a replica server but are associated with connection threads, not with the I/O or SQL threads.

- `Changing master`
	The thread is processing a [`CHANGE             MASTER TO`](change-master-to.md) statement.
- `Killing slave`
	The thread is processing a `STOP SLAVE` statement.
- `Opening master dump table`
	This state occurs after `Creating table from master             dump`.
- `Reading master dump table data`
	This state occurs after `Opening master dump             table`.
- `Rebuilding the index on master dump table`
	This state occurs after `Reading master dump table             data`.