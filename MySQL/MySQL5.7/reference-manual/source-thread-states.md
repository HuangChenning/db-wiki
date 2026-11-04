---
title: "8.14.5 Replication Source Thread States"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/source-thread-states.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.14.5 Replication Source Thread States

The following list shows the most common states you may see in the `State` column for the `Binlog         Dump` thread of the replication source. If you see no `Binlog Dump` threads on a source, this means that replication is not running; that is, that no replicas are currently connected.

- `Finished reading one binlog; switching to next             binlog`
	The thread has finished reading a binary log file and is opening the next one to send to the replica.
- `Master has sent all binlog to slave; waiting for             more updates`
	The thread has read all remaining updates from the binary logs and sent them to the replica. The thread is now idle, waiting for new events to appear in the binary log resulting from new updates occurring on the source.
- `Sending binlog event to slave`
	Binary logs consist of *events*, where an event is usually an update plus some other information. The thread has read an event from the binary log and is now sending it to the replica.
- `Waiting to finalize termination`
	A very brief state that occurs as the thread is stopping.