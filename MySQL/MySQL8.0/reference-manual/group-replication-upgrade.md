---
title: "20.8 Upgrading Group Replication"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/group-replication-upgrade.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

This section explains how to upgrade a Group Replication setup. The basic process of upgrading members of a group is the same as upgrading stand-alone instances, see [Chapter 3, *Upgrading MySQL*](upgrading.md) for the actual process of doing upgrade and types available. Choosing between an in-place or logical upgrade depends on the amount of data stored in the group. Usually an in-place upgrade is faster, and therefore is recommended. You should also consult [Section 19.5.3, “Upgrading a Replication Topology”](replication-upgrade.md).

While you are in the process of upgrading an online group, in order to maximize availability, you might need to have members with different MySQL Server versions running at the same time. Group Replication includes compatibility policies that enable you to safely combine members running different versions of MySQL in the same group during the upgrade procedure. Depending on your group, the effects of these policies might affect the order in which you should upgrade group members. For details, see [Section 20.8.1, “Combining Different Member Versions in a Group”](group-replication-online-upgrade-combining-versions.md).

If your group can be taken fully offline see [Section 20.8.2, “Group Replication Offline Upgrade”](group-replication-offline-upgrade.md). If your group needs to remain online, as is common with production deployments, see [Section 20.8.3, “Group Replication Online Upgrade”](group-replication-online-upgrade.md) for the different approaches available for upgrading a group with minimal downtime.