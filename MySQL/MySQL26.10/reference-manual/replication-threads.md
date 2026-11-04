---
title: "MySQL :: MySQL 26.10 Reference Manual :: 19.2.3 Replication Threads"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/replication-threads.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 19.2.3 Replication Threads

MySQL replication capabilities are implemented using the following types of threads:

- **Binary log dump thread.** The source creates a thread to send the binary log contents to a replica when the replica connects. This thread can be identified in the output of [`SHOW             PROCESSLIST`](show-processlist.md) on the source as the `Binlog             Dump` thread.
- **Replication I/O receiver thread.** When a [`START REPLICA`](start-replica.md) statement is issued on a replica server, the replica creates an I/O (receiver) thread, which connects to the source and asks it to send the updates recorded in its binary logs.
	The replication receiver thread reads the updates that the source's `Binlog Dump` thread sends (see previous item) and copies them to local files that comprise the replica's relay log.
	The state of this thread is shown as `Slave_IO_running` in the output of [`SHOW REPLICA STATUS`](show-replica-status.md).
- **Replication SQL applier thread.** Each replication channel uses the applier implementation selected by `APPLIER_VERSION`. Applier version 1, the Multi-Threaded Applier (MTA), uses a coordinator that reads transactions from the relay log and assigns them to worker threads. Applier version 2, the Change Stream Applier (CSA), schedules transactions whose dependencies are satisfied to a channel-specific pool of worker sessions. See [Section 19.2.4, “Change Stream Applier”](change-stream-applier.md).

For a channel using the MTA, `replica_parallel_workers` specifies the number of worker threads. For a channel using the CSA, `APPLIER_WORKER_COUNT` specifies the number of workers for that channel. This permits different replication channels to use different numbers of CSA workers.

Multithreaded replicas are also supported by NDB Cluster. See [Section 25.7.11, “NDB Cluster Replication Using the Multithreaded Applier”](mysql-cluster-replication-mta.md), for more information.