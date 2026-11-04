---
title: "Chapter 4 Downgrading MySQL"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/downgrading.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

Notes

- Make sure you understand [the MySQL release model](mysql-releases.md) for MySQL long-term support (LTS) and Innovation releases before proceeding with a downgrade.
- A replication topology is downgraded by following the rolling downgrade scheme described at [Section 19.5.3, “Upgrading or Downgrading a Replication Topology”](replication-upgrade.md), which uses one of the supported single-server methods for each individual server downgrade.
- Monthly Rapid Updates (MRUs) and hot fixes also count as releases in this documentation.

**Table 4.1 Downgrade Paths for MySQL Server**

| Downgrade Path | Path Examples | Supported Downgrade Methods | Notes |
| --- | --- | --- | --- |
| Within an LTS series | 8.4.y LTS to 8.4.x LTS | In-place, logical dump and load, MySQL Clone, or by using replication |  |
| From an LTS or Bugfix series to the previous LTS or Bugfix series | 8.4.x LTS to 8.0.y | Logical dump and load or by using replication | Only supported for rollback purposes (that is, if no new server functionality has been applied to the data) |
| From an LTS or Bugfix series to an Innovation series *after the previous LTS series* | 8.4.x LTS to 8.3.0 Innovation | Logical dump and load or by using replication | Only supported for rollback purposes (that is, if no new server functionality has been applied to the data) |
| From within an Innovation series | 9.6 to 9.6 | Logical dump and load or by using replication | Only supported for rollback purposes (that is, if no new server functionality has been applied to the data) |

Downgrading to MySQL 5.7 or earlier is not supported.