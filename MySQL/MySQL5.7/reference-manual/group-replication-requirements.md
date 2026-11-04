---
title: "17.3.1 Group Replication Requirements"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/group-replication-requirements.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 17.3.1 Group Replication Requirements

Server instances that you want to use for Group Replication must satisfy the following requirements.

#### Infrastructure

- **InnoDB Storage Engine.** Data must be stored in the [`InnoDB`](innodb-storage-engine.md) transactional storage engine. Transactions are executed optimistically and then, at commit time, are checked for conflicts. If there are conflicts, in order to maintain consistency across the group, some transactions are rolled back. This means that a transactional storage engine is required. Moreover, [`InnoDB`](innodb-storage-engine.md) provides some additional functionality that enables better management and handling of conflicts when operating together with Group Replication. The use of other storage engines, including the temporary [`MEMORY`](memory-storage-engine.md) storage engine, might cause errors in Group Replication. Convert any tables in other storage engines to use [`InnoDB`](innodb-storage-engine.md) before using the instance with Group Replication. You can prevent the use of other storage engines by setting the [`disabled_storage_engines`](server-system-variables.md) system variable on group members, for example:
	```
	disabled_storage_engines="MyISAM,BLACKHOLE,FEDERATED,ARCHIVE,MEMORY"
	```
- **Primary Keys.** Every table that is to be replicated by the group must have a defined primary key, or primary key equivalent where the equivalent is a non-null unique key. Such keys are required as a unique identifier for every row within a table, enabling the system to determine which transactions conflict by identifying exactly which rows each transaction has modified.
- **IPv4 Network.** The group communication engine used by MySQL Group Replication only supports IPv4. Therefore, Group Replication requires an IPv4 network infrastructure.
- **Network Performance.** MySQL Group Replication is designed to be deployed in a cluster environment where server instances are very close to each other. The performance and stabiity of a group can be impacted by both network latency and network bandwidth. Bi-directional communication must be maintained at all times between all group members. If either inbound or outbound communication is blocked for a server instance (for example, by a firewall, or by connectivity issues), the member cannot function in the group, and the group members (including the member with issues) might not be able to report the correct member status for the affected server instance.

#### Server Instance Configuration

The following options must be configured on server instances that are members of a group.

- **Unique Server Identifier.** Use the [`server_id`](replication-options.md) system variable to configure the server with a unique server ID, as required for all servers in replication topologies. With the default server ID of 0, servers in a replication topology cannot connect to each other. The server ID must be a positive integer between 1 and (2 <sup>32</sup>)−1, and it must be different from every other server ID in use by any other server in the replication topology.
- **Binary Log Active.** Set [`--log-bin[=log_file_name]`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/replication-options-binary-log.html#sysvar_log_bin). MySQL Group Replication replicates binary log contents, therefore the binary log needs to be on for it to operate. This option is enabled by default. See [Section 5.4.4, “The Binary Log”](binary-log.md).
- **Replica Updates Logged.** Set [`--log-slave-updates`](replication-options-binary-log.md). Servers need to log binary logs that are applied through the replication applier. Servers in the group need to log all transactions that they receive and apply from the group. This is required because recovery is conducted by relying on binary logs form participants in the group. Therefore, copies of each transaction need to exist on every server, even for those transactions that were not initiated on the server itself.
- **Binary Log Row Format.** Set [`--binlog-format=row`](replication-options-binary-log.md). Group Replication relies on row-based replication format to propagate changes consistently among the servers in the group. It relies on row-based infrastructure to be able to extract the necessary information to detect conflicts among transactions that execute concurrently in different servers in the group. See [Section 16.2.1, “Replication Formats”](replication-formats.md).
- **Binary Log Checksums Off.** Set [`--binlog-checksum=NONE`](replication-options-binary-log.md). Due to a design limitation of replication event checksums, Group Replication cannot make use of them, and they must be disabled.
- **Global Transaction Identifiers On.** Set [`gtid_mode=ON`](replication-options-gtids.md) and [`enforce_gtid_consistency=ON`](replication-options-gtids.md). Group Replication uses global transaction identifiers to track exactly which transactions have been committed on every server instance and thus be able to infer which servers have executed transactions that could conflict with already committed transactions elsewhere. In other words, explicit transaction identifiers are a fundamental part of the framework to be able to determine which transactions may conflict. See [Section 16.1.3, “Replication with Global Transaction Identifiers”](replication-gtids.md).
	In addition, if you need to set the value of [`gtid_purged`](replication-options-gtids.md), you must do so while Group Replication is not running.
- **Replication Information Repositories.** Set [`master_info_repository=TABLE`](replication-options-replica.md) and [`relay_log_info_repository=TABLE`](replication-options-replica.md). The replication applier needs to have the source and replica metadata written to the `mysql.slave_master_info` and `mysql.slave_relay_log_info` system tables. This ensures the Group Replication plugin has consistent recoverability and transactional management of the replication metadata. See [Section 16.2.4.2, “Replication Metadata Repositories”](replica-logs-status.md).
- **Transaction Write Set Extraction.** Set [`--transaction-write-set-extraction=XXHASH64`](replication-options-binary-log.md) so that while collecting rows to log them to the binary log, the server collects the write set as well. The write set is based on the primary keys of each row and is a simplified and compact view of a tag that uniquely identifies the row that was changed. This tag is then used for detecting conflicts.
- **Lower Case Table Names.** Set [`--lower-case-table-names`](server-system-variables.md) to the same value on all group members. A setting of 1 is correct for the use of the [`InnoDB`](innodb-storage-engine.md) storage engine, which is required for Group Replication. Note that this setting is not the default on all platforms.
- **Multithreaded Appliers.** Group Replication members can be configured as multithreaded replicas, enabling transactions to be applied in parallel. A nonzero value for [`slave_parallel_workers`](replication-options-replica.md) enables the multithreaded applier on the member, and up to 1024 parallel applier threads can be specified. If you do this, the following settings are also required:
	[`slave_preserve_commit_order=1`](replication-options-replica.md)
	This setting is required to ensure that the final commit of parallel transactions is in the same order as the original transactions. Group Replication relies on consistency mechanisms built around the guarantee that all participating members receive and apply committed transactions in the same order.
	[`slave_parallel_type=LOGICAL_CLOCK`](replication-options-replica.md)
	This setting is required with [`slave_preserve_commit_order=1`](replication-options-replica.md). It specifies the policy used to decide which transactions are allowed to execute in parallel on the replica.
	Setting [`slave_parallel_workers=0`](replication-options-replica.md) disables parallel execution and gives the replica a single applier thread and no coordinator thread. With that setting, the [`slave_parallel_type`](replication-options-replica.md) and [`slave_preserve_commit_order`](replication-options-replica.md) options have no effect and are ignored.