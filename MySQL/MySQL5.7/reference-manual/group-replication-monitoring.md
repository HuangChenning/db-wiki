---
title: "17.4 Monitoring Group Replication"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/group-replication-monitoring.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

You can use the MySQL [Performance Schema](performance-schema.md) to monitor Group Replication. These Performance Schema tables display information specific to Group Replication:

These Performance Schema replication tables also show information relating to Group Replication:

- [`replication_connection_status`](performance-schema-replication-connection-status-table.md) shows information regarding Group Replication, such as transactions received from the group and queued in the applier queue (relay log).
- [`replication_applier_status`](performance-schema-replication-applier-status-table.md) shows the states of channels and threads relating to Group Replication. These can also be used to monitor what individual worker threads are doing.

Replication channels created by the Group Replication plugin are listed here:

- `group_replication_recovery`: Used for replication changes related to distributed recovery.
- `group_replication_applier`: Used for the incoming changes from the group, to apply transactions coming directly from the group.

For information about system variables affecting Group Replication, see [Section 17.7.1, “Group Replication System Variables”](group-replication-system-variables.md). See [Section 17.7.2, “Group Replication Status Variables”](group-replication-status-variables.md), for status variables providing information about Group Replication.

Note

If you are monitoring one or more secondary instances using [**mysqladmin**](mysqladmin.md), you should be aware that a [`FLUSH STATUS`](flush.md) statement executed by this utility creates a GTID event on the local instance which may impact future group operations.