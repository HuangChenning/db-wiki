---
title: "16.2.4 Relay Log and Replication Metadata Repositories"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/replica-logs.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 16.2.4 Relay Log and Replication Metadata Repositories

A replica server creates several repositories of information to use for the replication process:

- The *relay log*, which is written by the replication I/O thread, contains the transactions read from the replication source server's binary log. The transactions in the relay log are applied on the replica by the replication SQL thread. For information about the relay log, see [Section 16.2.4.1, “The Relay Log”](replica-logs-relaylog.md).
- The replica's *connection metadata repository* contains information that the replication I/O thread needs to connect to the replication source server and retrieve transactions from the source's binary log. The connection metadata repository is written to the `mysql.slave_master_info` table or to a file.
- The replica's *applier metadata repository* contains information that the replication SQL thread needs to read and apply transactions from the replica's relay log. The applier metadata repository is written to the `mysql.slave_relay_log_info` table or to a file.

The connection metadata repository and applier metadata repository are collectively known as the replication metadata repositories. For information about these, see [Section 16.2.4.2, “Replication Metadata Repositories”](replica-logs-status.md).

**Making replication resilient to unexpected halts.** The `mysql.slave_master_info` and `mysql.slave_relay_log_info` tables are created using the transactional storage engine [`InnoDB`](innodb-storage-engine.md). Updates to the replica's applier metadata repository table are committed together with the transactions, meaning that the replica's progress information recorded in that repository is always consistent with what has been applied to the database, even in the event of an unexpected server halt. For information on the combination of settings on the replica that is most resilient to unexpected halts, see [Section 16.3.2, “Handling an Unexpected Halt of a Replica”](replication-solutions-unexpected-replica-halt.md).