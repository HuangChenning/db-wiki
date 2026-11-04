---
title: "MySQL :: MySQL 26.10 Reference Manual :: 20.7.5 Message Fragmentation"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/group-replication-performance-message-fragmentation.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 20.7.5 Message Fragmentation

When an abnormally large message is sent between Group Replication group members, it can result in some group members being reported as failed and expelled from the group. This is because the single thread used by Group Replication's group communication engine (XCom, a Paxos variant) is occupied processing the message for too long, so some of the group members might report the receiver as failed. By default, large messages are automatically split into fragments that are sent separately and reassembled by the recipients.

The system variable [`group_replication_communication_max_message_size`](group-replication-system-variables.md) specifies a maximum message size for Group Replication communications, above which messages are fragmented. The default maximum message size is 10485760 bytes (10 MiB). The greatest permitted value is the same as the maximum value of the [`replica_max_allowed_packet`](replication-options-replica.md) system variable (1 GB). [`group_replication_communication_max_message_size`](group-replication-system-variables.md) must be less than [`replica_max_allowed_packet`](replication-options-replica.md) because the applier thread cannot handle message fragments larger than the maximum permitted packet size. To switch off fragmentation, specify a zero value for [`group_replication_communication_max_message_size`](group-replication-system-variables.md).

As with most other Group Replication system variables, you must restart the Group Replication plugin for the change to take effect. For example:

```sql
STOP GROUP_REPLICATION;
SET GLOBAL group_replication_communication_max_message_size= 5242880;
START GROUP_REPLICATION;
```

Message delivery for a fragmented message is considered complete when all the fragments of the message have been received and reassembled by all the group members. Fragmented messages include information in their headers that enables a member joining during message transmission to recover the earlier fragments that were sent before it joined. If the joining member fails to recover the fragments, it expels itself from the group.

The Group Replication communication protocol version in use by the group must allow fragmentation. You can obtain the communication protocol in use by a group using [`group_replication_get_communication_protocol()`](group-replication-functions-for-communication-protocol.md), which returns the oldest MySQL Server version that the group supports. If necessary, use [`group_replication_set_communication_protocol()`](group-replication-functions-for-communication-protocol.md) to set the communication protocol version high enough (8.0.16 or above) to allow fragmentation. For more information, see [Section 20.5.1.4, “Setting a Group's Communication Protocol Version”](group-replication-communication-protocol.md).

If a replication group cannot use fragmentation because some members do not support it, the system variable [`group_replication_transaction_size_limit`](group-replication-system-variables.md) can be used to limit the maximum size of transactions the group accepts. Transactions above this size are rolled back. You can also use [`group_replication_member_expel_timeout`](group-replication-system-variables.md) to allow additional time (up to an hour) before a member under suspicion of having failed is expelled from the group.