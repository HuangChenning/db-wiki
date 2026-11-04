---
title: "20.9.2 Group Replication Status Variables"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/group-replication-status-variables.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 20.9.2 Group Replication Status Variables

This section describes the status variables providing information about Group Replication.

The status variables and their meanings are listed here:

- `Gr_all_consensus_proposals_count`
	Sum of all proposals that were initiated and terminated on this node.
- `Gr_all_consensus_time_sum`
	The total elapsed time for all consensus rounds started and finished on this node. By comparing this value with `Gr_all_consensus_proposals_count`, we can determine whether a given consensus time has an upward trend, which may signal a problem.
- `Gr_certification_garbage_collector_count`
	The number of times certification garbage collection has been run.
- `Gr_certification_garbage_collector_time_sum`
	Sum of the times in microseconds taken by certification garbage collection.
- `Gr_consensus_bytes_received_sum`
	The sum of all socket-level bytes received from group nodes having this node as a destination.
- `Gr_consensus_bytes_sent_sum`
	Sum of all socket-level bytes originating on this node that were sent to all (other) group nodes. More data is reported here than for sent messages, since they are multiplexed and sent to each member.
	For example, if we have a group with three members and we send a 100-byte message, this value accounts for 300 bytes, since we send 100 bytes to each node.
- `Gr_control_messages_sent_count`
	Number of control messages sent by this member.
- `Gr_control_messages_sent_bytes_sum`
	Sum of the number of bytes used in control messages sent by this member; this is the on-the-wire size.
- `Gr_control_messages_sent_roundtrip_time_sum`
	Sum of the round-trip times in microseconds for control messages sent by this member; a round trip is measured between the sending and the delivery of the message on the sender. This should provide the time between sending and delivery of control messages for the majority of the members of the group, including the sender.
- `Gr_data_messages_sent_bytes_sum`
	Sum in bytes used by data messages sent by this member; this is the on-the-wire size.
- `Gr_data_messages_sent_count`
	This is the nmber of transaction data messages sent by this member.
- `Gr_data_messages_sent_roundtrip_time_sum`
	Sum of the round-trip times in microseconds for data messages sent by this member; a round trip is measured between the sending and the delivery of the message on the sender. This should provide the time between sending and delivery of data messages for the majority of the members of the group, including the sender.
- `Gr_empty_consensus_proposals_count`
	Sum of all empty proposal rounds that were initiated and terminated on this node.
- `Gr_extended_consensus_count`
	The number of full 3-phase rounds that this node has initiated. If this number grows over time, it means that at least one node is having problems answering to proposals, either due to something it to run slowly, or to network issues. Use this value together with the `count_member_failure_suspicions` column of the Performance Schema [`replication_group_communication_information`](performance-schema-replication-group-communication-information-table.md) table when diagnosing such issues.
- `Gr_last_consensus_end_timestamp`
	The time when the last consensus proposal was approved, in a timestamp format. This can be an indicator whether the group is making slow progress, or has halted.
- `Gr_total_messages_sent_count`
	The number of high-level messages sent by this node to the group. These are the messages received from the API for proposing to the group. The XCom batching mechanism batches these messages and proposes them all together. The value shown for this variable reflects the number of messages prior to batching.
- `Gr_transactions_consistency_after_sync_count`
	Number of transactions on secondaries that waited to start, while waiting for transactions from the primary with [`group_replication_consistency`](group-replication-system-variables.md) equal to `AFTER` or `BEFORE_AND_AFTER` to be committed.
- `Gr_transactions_consistency_after_sync_time_sum`
	Sum of the times in microseconds that transactions on secondaries waited on transactions from the primary with [`group_replication_consistency`](group-replication-system-variables.md) equal to `AFTER` or `BEFORE_AND_AFTER` to be committed, before starting.
- `Gr_transactions_consistency_after_termination_count`
	The number of transactions executed with [`group_replication_consistency`](group-replication-system-variables.md) equal to `AFTER` or `BEFORE_AND_AFTER`.
- `Gr_transactions_consistency_after_termination_time_sum`
	Sum of the time in microseconds between delivery of the transaction executed with [`group_replication_consistency`](group-replication-system-variables.md) equal to `AFTER` or `BEFORE_AND_AFTER`, and acknowledgement by the other group members that the transaction is prepared.
	This value does not include transaction send roundtrip time.
- `Gr_transactions_consistency_before_begin_count`
	Number of transactions executed with [`group_replication_consistency`](group-replication-system-variables.md) equal to `BEFORE` or `BEFORE_AND_AFTER`.
- `Gr_transactions_consistency_before_begin_time_sum`
	Sum of the time in microseconds that the member waited until its group replication applier channel was consumed before executing the transaction with [`group_replication_consistency`](group-replication-system-variables.md) equal to `BEFORE` or `BEFORE_AND_AFTER`.

These status variables all have member scope since they reflect what the local member observes. They are reset on group bootstrap, joining of a new member, automatic rejoin of an existing member, and server restart.