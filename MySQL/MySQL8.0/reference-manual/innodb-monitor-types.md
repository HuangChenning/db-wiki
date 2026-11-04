---
title: "17.17.1 InnoDB Monitor Types"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/innodb-monitor-types.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 17.17.1 InnoDB Monitor Types

There are two types of `InnoDB` monitor:

- The standard `InnoDB` Monitor displays the following types of information:
	- Work done by the main background thread
	- Semaphore waits
	- Data about the most recent foreign key and deadlock errors
	- Lock waits for transactions
	- Table and record locks held by active transactions
	- Pending I/O operations and related statistics
	- Insert buffer and adaptive hash index statistics
	- Redo log data
	- Buffer pool statistics
	- Row operation data
- The `InnoDB` Lock Monitor prints additional lock information as part of the standard `InnoDB` Monitor output.