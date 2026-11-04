---
title: "MySQL :: MySQL 26.7 Reference Manual :: 14.18.1 Group Replication Functions"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/group-replication-functions.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 14.18.1 Group Replication Functions

The functions described in the following sections are used with Group Replication.

**Table 14.25 Group Replication Functions**

| Name | Description |
| --- | --- |
| [`group_replication_disable_member_action()`](group-replication-functions-for-member-actions.md) | Disable member action for event specified |
| [`group_replication_enable_member_action()`](group-replication-functions-for-member-actions.md) | Enable member action for event specified |
| [`group_replication_get_communication_protocol()`](group-replication-functions-for-communication-protocol.md) | Get version of group replication communication protocol currently in use |
| [`group_replication_get_write_concurrency()`](group-replication-functions-for-maximum-consensus.md) | Get maximum number of consensus instances currently set for group |
| [`group_replication_reset_member_actions()`](group-replication-functions-for-member-actions.md) | Reset all member actions to defaults and configuration version number to 1 |
| [`group_replication_set_as_primary()`](group-replication-functions-for-new-primary.md) | Make a specific group member the primary |
| [`group_replication_set_communication_protocol()`](group-replication-functions-for-communication-protocol.md) | Set version for group replication communication protocol to use |
| [`group_replication_set_write_concurrency()`](group-replication-functions-for-maximum-consensus.md) | Set maximum number of consensus instances that can be executed in parallel |
| [`group_replication_switch_to_multi_primary_mode()`](group-replication-functions-for-mode.md) | Changes the mode of a group running in single-primary mode to multi-primary mode |
| [`group_replication_switch_to_single_primary_mode()`](group-replication-functions-for-mode.md) | Changes the mode of a group running in multi-primary mode to single-primary mode |