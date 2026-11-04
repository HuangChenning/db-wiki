---
title: "20.7.3 Single Consensus Leader"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/group-replication-single-consensus-leader.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 20.7.3 Single Consensus Leader

By default, the group communication engine for Group Replication (XCom, a Paxos variant) operates using every member of the replication group as a leader. The group communication engine can use a single leader to drive consensus when the group is in single-primary mode. Operating with a single consensus leader improves performance and resilience in single-primary mode, particularly when some of the group’s secondary members are currently unreachable.

To use a single consensus leader, the group must be configured as follows:

- The group must be in single-primary mode.
- The [`group_replication_paxos_single_leader`](group-replication-system-variables.md) system variable must be set to `ON`. With the default setting `OFF`, the behavior is disabled. You must carry out a full reboot of the replication group (bootstrap) for Group Replication to pick up a change to this setting.
- The Group Replication communication protocol version must be set to 8.0.27 or later. Use the [`group_replication_get_communication_protocol()`](group-replication-functions-for-communication-protocol.md) function to view the group's communication protocol version. If a lower version is in use, the group cannot use this behavior. You can use the [`group_replication_set_communication_protocol()`](group-replication-functions-for-communication-protocol.md) function to set the group's communication protocol to a higher version if all group members support it. MySQL InnoDB Cluster manages the communication protocol version automatically. For more information, see [Section 20.5.1.4, “Setting a Group's Communication Protocol Version”](group-replication-communication-protocol.md).

When this configuration is in place, Group Replication instructs the group communication engine to use the group’s primary as the single leader to drive consensus. When a new primary is elected, Group Replication tells the group communication engine to use it instead. If the primary is currently unhealthy, the group communication engine uses an alternative member as the consensus leader. The Performance Schema table [`replication_group_communication_information`](performance-schema-replication-group-communication-information-table.md) shows the current preferred and actual consensus leader, with the preferred leader being Group Replication’s choice, and the actual leader being the one selected by the group communication engine.

If the group is in multi-primary mode, has a lower communication protocol version, or the behavior is disabled by the [`group_replication_paxos_single_leader`](group-replication-system-variables.md) setting, all members are used as leaders to drive consensus. In this situation, the Performance Schema table [`replication_group_communication_information`](performance-schema-replication-group-communication-information-table.md) shows all of the members as both the preferred and actual leaders.

The `WRITE_CONSENSUS_SINGLE_LEADER_CAPABLE` column of the Performance Schema [`replication_group_communication_information`](performance-schema-replication-group-communication-information-table.md) table shows whether the group supports the use of a single leader, even if [`group_replication_paxos_single_leader`](group-replication-system-variables.md) is currently set to `OFF` on the queried member. The column value is 1 if the group was started with [`group_replication_paxos_single_leader`](group-replication-system-variables.md) set to `ON`, and its communication protocol version is MySQL 8.0.27 or above. This information is returned only for group members in `ONLINE` or `RECOVERING` state.