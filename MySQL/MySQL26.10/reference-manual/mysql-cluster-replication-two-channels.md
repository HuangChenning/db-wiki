---
title: "MySQL :: MySQL 26.10 Reference Manual :: 25.7.7 Using Two Replication Channels for NDB Cluster Replication"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/mysql-cluster-replication-two-channels.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 25.7.7 Using Two Replication Channels for NDB Cluster Replication

In a more complete example scenario, we envision two replication channels to provide redundancy and thereby guard against possible failure of a single replication channel. This requires a total of four replication servers, two source servers on the source cluster and two replica servers on the replica cluster. For purposes of the discussion that follows, we assume that unique identifiers are assigned as shown here:

**Table 25.45 NDB Cluster replication servers described in the text**

| Server ID | Description |
| --- | --- |
| 1 | Source - primary replication channel (*S*) |
| 2 | Source - secondary replication channel (*S'*) |
| 3 | Replica - primary replication channel (*R*) |
| 4 | replica - secondary replication channel (*R'*) |

Setting up replication with two channels is not radically different from setting up a single replication channel. First, the [**mysqld**](mysqld.md) processes for the primary and secondary replication source servers must be started, followed by those for the primary and secondary replicas. The replication processes can be initiated by issuing the [`START       REPLICA`](start-replica.md) statement on each of the replicas. The commands and the order in which they need to be issued are shown here:

1. Start the primary replication source:
	```svg
	shellS> mysqld --ndbcluster --server-id=1 \
	               --log-bin &
	```
2. Start the secondary replication source:
	```svg
	shellS'> mysqld --ndbcluster --server-id=2 \
	               --log-bin &
	```
3. Start the primary replica server:
	```svg
	shellR> mysqld --ndbcluster --server-id=3 \
	               --skip-replica-start &
	```
4. Start the secondary replica server:
	```svg
	shellR'> mysqld --ndbcluster --server-id=4 \
	                --skip-replica-start &
	```
5. Finally, initiate replication on the primary channel by executing the [`START REPLICA`](start-replica.md) statement on the primary replica as shown here:
	```sql
	mysqlR> START REPLICA;
	```
	Warning
	Only the primary channel must be started at this point. The secondary replication channel needs to be started only in the event that the primary replication channel fails, as described in [Section 25.7.8, “Implementing Failover with NDB Cluster Replication”](mysql-cluster-replication-failover.md). Running multiple replication channels simultaneously can result in unwanted duplicate records being created on the replicas.

As mentioned previously, it is not necessary to enable binary logging on the replicas.