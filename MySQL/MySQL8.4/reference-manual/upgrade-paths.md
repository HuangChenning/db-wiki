---
title: "3.2 Upgrade Paths"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/upgrade-paths.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

Notes

- Make sure you understand [the MySQL release model](mysql-releases.md) for MySQL for MySQL long long-term support (LTS) and Innovation versions before proceeding with a downgrade.
- We recommend checking upgrade compatibility with MySQL Shell's [Upgrade Checker Utility](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.4-en/mysql-shell-utilities-upgrade.html) before performing an upgrade.
- A replication topology is upgraded by following the rolling upgrade scheme described at [Section 19.5.3, “Upgrading or Downgrading a Replication Topology”](replication-upgrade.md), which uses one of the supported single-server methods for each individual server upgrade.
- Monthly Rapid Updates (MRUs) and hot fixes also count as releases in this documentation.

**Table 3.1 Upgrade Paths for MySQL Server**

| Upgrade Path | Path Examples | Supported Upgrade Methods |
| --- | --- | --- |
| Within an LTS or Bugfix series | 8.0.37 to 8.0.41 or 8.4.0 to 8.4.4 | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), [replication](replication-upgrade.md), and [MySQL Clone](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.4-en/mysql-innodb-cluster-clone-deployment.html) |
| From an LTS or Bugfix series to the next [LTS series](glossary.md) | 8.0.37 to 8.4.x LTS | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), and [replication](replication-upgrade.md) |
| From an LTS or Bugfix release to an Innovation release *before the next LTS series* | 8.0.34 to 8.3.0 or 8.4.0 to 9.0.0 | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), and [replication](replication-upgrade.md) |
| From an [Innovation series](glossary.md) to the next [LTS series](glossary.md) | 8.3.0 to 8.4 LTS | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), and [replication](replication-upgrade.md) |
| From an Innovation series to an Innovation release *after the next LTS series* | Not allowed, two steps are required: 8.3.0 to 8.4 LTS, and 8.4 LTS to 9.x Innovation | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), and [replication](replication-upgrade.md) |
| From within an Innovation series | 8.1.0 to 8.3.0 | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), and [replication](replication-upgrade.md) |
| From MySQL 5.7 to an LTS or Innovation release | MySQL 5.7 to 8.4 | A bugfix or LTS series cannot be skipped, so in this example first [upgrade MySQL 5.7 to MySQL 8.0](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/upgrade-paths.html), and then upgrade MySQL 8.0 to MySQL 8.4. |