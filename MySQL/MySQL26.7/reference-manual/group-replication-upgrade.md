---
title: "MySQL :: MySQL 26.7 Reference Manual :: 20.8 Upgrading Group Replication"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/group-replication-upgrade.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 20.8 Upgrading Group Replication

This section explains how to upgrade a Group Replication setup. The basic process of upgrading members of a group is the same as upgrading stand-alone instances, see [Chapter 3, *Upgrading MySQL*](upgrading.md) for the actual process of doing upgrade and types available. Choosing between an in-place or logical upgrade depends on the amount of data stored in the group. Usually an in-place upgrade is faster, and therefore is recommended. You should also consult [Section 19.5.3, “Upgrading or Downgrading a Replication Topology”](replication-upgrade.md).

Note

Before MySQL 8.4, a server would not join a group if it was running a lower MySQL Server version than the lowest group member's version. For example, for a group with S1 (8.0.30), S2 (8.0.31), and S3 (8.0.32), the joining member needs to be 8.0.30 or higher. As of MySQL 8.4, all versions within the same LTS series can join a group. For example, an 8.4.0 server could join a group consisting of S1 (8.4.1) and S2 (8.4.2), and a 9.7.0 server could join a group consisting of S1 (9.7.1) and S2 (9.7.2).

As of MySQL 8.4, in-place downgrades of servers within groups are also supported within the same LTS series. For example, a member of a group running MySQL 9.7.2 can be downgraded to MySQL 9.7.0.

While you are in the process of upgrading an online group, in order to maximize availability, you might need to have members with different MySQL Server versions running at the same time. Group Replication includes compatibility policies that enable you to safely combine members running different versions of MySQL in the same group during the upgrade procedure. Depending on your group, the effects of these policies might affect the order in which you should upgrade group members. For details, see [Section 20.8.1, “Combining Different Member Versions in a Group”](group-replication-online-upgrade-combining-versions.md).

If your group can be taken fully offline see [Section 20.8.2, “Group Replication Offline Upgrade”](group-replication-offline-upgrade.md). If your group needs to remain online, as is common with production deployments, see [Section 20.8.3, “Group Replication Online Upgrade”](group-replication-online-upgrade.md) for the different approaches available for upgrading a group with minimal downtime.