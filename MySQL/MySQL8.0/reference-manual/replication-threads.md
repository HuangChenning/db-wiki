---
title: "19.2.3 Replication Threads"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/replication-threads.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 19.2.3 Replication Threads

MySQL replication capabilities are implemented using the following types of threads:

- **Binary log dump thread.** The source creates a thread to send the binary log contents to a replica when the replica connects. This thread can be identified in the output of [`SHOW             PROCESSLIST`](show-processlist.md) on the source as the `Binlog             Dump` thread.
- **Replication I/O receiver thread.** When a [`START REPLICA`](start-replica.md) statement is issued on a replica server, the replica creates an I/O (receiver) thread, which connects to the source and asks it to send the updates recorded in its binary logs.
	The replication receiver thread reads the updates that the source's `Binlog Dump` thread sends (see previous item) and copies them to local files that comprise the replica's relay log.
	The state of this thread is shown as `Slave_IO_running` in the output of [`SHOW REPLICA STATUS`](show-replica-status.md).
- **Replication SQL applier thread.** When [`replica_parallel_workers`](replication-options-replica.md) (in MySQL 8.0.26 and earlier, use [`slave_parallel_workers`](replication-options-replica.md)) is equal to 0, the replica creates an SQL (applier) thread to read the relay log that is written by the replication receiver thread and execute the transactions contained in it. When `replica_parallel_workers` is ``*`N`* >= 1``, there are *`N`* applier threads and one coordinator thread, which reads transactions sequentially from the relay log, and schedules them to be applied by worker threads. Each worker applies the transactions that the coordinator has assigned to it.

You can enable further parallelization for tasks on a replica by setting the system variable `replica_parallel_workers` (MySQL 8.0.26 or later) or `slave_parallel_workers` (prior to MySQL 8.0.26) to a value greater than 0. When this is done, the replica creates the specified number of worker threads to apply transactions, plus a coordinator thread which reads transactions from the relay log and assigns them to workers. A replica with `replica_parallel_workers` (`slave_parallel_workers`) set to a value greater than 0 is called a multithreaded replica. If you are using multiple replication channels, each channel has the number of threads specified using this variable.

Note

Multithreaded replicas are supported by NDB Cluster beginning with NDB 8.0.33. (Previously, `NDB` silently ignored any setting for `replica_parallel_workers`.) See [Section 25.7.11, “NDB Cluster Replication Using the Multithreaded Applier”](mysql-cluster-replication-mta.md), for more information.