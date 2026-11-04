---
title: "20.4 Monitoring Group Replication"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/group-replication-monitoring.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

You can use the MySQL [Performance Schema](performance-schema.md) to monitor Group Replication. These Performance Schema tables display information specific to Group Replication:

These Performance Schema replication tables also show information relating to Group Replication:

- [`replication_connection_status`](performance-schema-replication-connection-status-table.md) shows information regarding Group Replication, such as transactions received from the group and queued in the applier queue (relay log).
- [`replication_applier_status`](performance-schema-replication-applier-status-table.md) shows the states of channels and threads relating to Group Replication. These can also be used to monitor what individual worker threads are doing.

Replication channels created by the Group Replication plugin are listed here:

- `group_replication_recovery`: Used for replication changes related to distributed recovery.
- `group_replication_applier`: Used for the incoming changes from the group, to apply transactions coming directly from the group.

For information about system variables affecting Group Replication, see [Section 20.9.1, “Group Replication System Variables”](group-replication-system-variables.md). See [Section 20.9.2, “Group Replication Status Variables”](group-replication-status-variables.md), for status variables providing information about Group Replication.

Messages relating to Group Replication lifecycle events other than errors are classified as system messages; these are always written to the replication group member' error log. You can use this information to review the history of a given server's membership in a replication group.

Some lifecycle events that affect the whole group are logged on every group member, such as a new member entering `ONLINE` status in the group or a primary election. Other events are logged only on the member where they take place, such as super read only mode being enabled or disabled on the member, or the member leaving the group. A number of lifecycle events that can indicate an issue if they occur frequently are logged as warning messages, including a member becoming unreachable and then reachable again, and a member starting distributed recovery by state transfer from the binary log or by a remote cloning operation.

Note

If you are monitoring one or more secondary instances using [**mysqladmin**](mysqladmin.md), you should be aware that a [`FLUSH STATUS`](flush.md) statement executed by this utility creates a GTID event on the local instance which may impact future group operations.