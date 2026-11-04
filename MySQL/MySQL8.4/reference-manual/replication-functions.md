---
title: "14.18 Replication Functions"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/replication-functions.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

The functions described in the following sections are used with MySQL Replication.

**Table 14.24 Replication Functions**

| Name | Description | Deprecated |
| --- | --- | --- |
| [`asynchronous_connection_failover_add_managed()`](replication-functions-async-failover.md) | Add group member source server configuration information to a replication channel source list |  |
| [`asynchronous_connection_failover_add_source()`](replication-functions-async-failover.md) | Add source server configuration information server to a replication channel source list |  |
| [`asynchronous_connection_failover_delete_managed()`](replication-functions-async-failover.md) | Remove a managed group from a replication channel source list |  |
| [`asynchronous_connection_failover_delete_source()`](replication-functions-async-failover.md) | Remove a source server from a replication channel source list |  |
| [`asynchronous_connection_failover_reset()`](replication-functions-async-failover.md) | Remove all settings relating to group replication asynchronous failover |  |
| [`group_replication_disable_member_action()`](group-replication-functions-for-member-actions.md) | Disable member action for event specified |  |
| [`group_replication_enable_member_action()`](group-replication-functions-for-member-actions.md) | Enable member action for event specified |  |
| [`group_replication_get_communication_protocol()`](group-replication-functions-for-communication-protocol.md) | Get version of group replication communication protocol currently in use |  |
| [`group_replication_get_write_concurrency()`](group-replication-functions-for-maximum-consensus.md) | Get maximum number of consensus instances currently set for group |  |
| [`group_replication_reset_member_actions()`](group-replication-functions-for-member-actions.md) | Reset all member actions to defaults and configuration version number to 1 |  |
| [`group_replication_set_as_primary()`](group-replication-functions-for-new-primary.md) | Make a specific group member the primary |  |
| [`group_replication_set_communication_protocol()`](group-replication-functions-for-communication-protocol.md) | Set version for group replication communication protocol to use |  |
| [`group_replication_set_write_concurrency()`](group-replication-functions-for-maximum-consensus.md) | Set maximum number of consensus instances that can be executed in parallel |  |
| [`group_replication_switch_to_multi_primary_mode()`](group-replication-functions-for-mode.md) | Changes the mode of a group running in single-primary mode to multi-primary mode |  |
| [`group_replication_switch_to_single_primary_mode()`](group-replication-functions-for-mode.md) | Changes the mode of a group running in multi-primary mode to single-primary mode |  |
| [`MASTER_POS_WAIT()`](replication-functions-synchronization.md) | Block until the replica has read and applied all updates up to the specified position | Yes |
| [`SOURCE_POS_WAIT()`](replication-functions-synchronization.md) | Block until the replica has read and applied all updates up to the specified position |  |
| [`WAIT_FOR_EXECUTED_GTID_SET()`](gtid-functions.md) | Wait until the given GTIDs have executed on the replica. |  |