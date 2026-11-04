---
title: "MySQL :: MySQL 26.7 Reference Manual :: 4.1 Downgrade Validation"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/downgrading-downgrade-validation.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 4.1 Downgrade Validation

For calendar-versioned releases, a direct downgrade that starts a target server on a data directory created by a later server is considered only when all of the following conditions are satisfied:

- The source release is an LTS release.
- The source and target have the same YY.M release base.
- The target is not earlier than the applicable server downgrade threshold.

A direct downgrade between different YY.M release bases is not supported. Patch downgrades between Innovation releases are also not supported, even when both releases have the same YY.M release base.

For example, assuming that MySQL 28.4 is an LTS release, a downgrade from MySQL 28.4.4 LTS to MySQL 28.4.2 LTS may be accepted if the downgrade threshold permits it. A downgrade from MySQL 28.10.4 Innovation to MySQL 28.10.3 Innovation is rejected, as is a downgrade from MySQL 28.10.4 Innovation to MySQL 28.4.0.

These direct-downgrade restrictions do not change the logical dump-and-load or replication rollback alternatives listed in Table 4.1, “Downgrade Paths for MySQL Server”.

**Table 4.1 Downgrade Paths for MySQL Server**

| Downgrade Path | Path Examples | Supported Downgrade Methods | Notes |
| --- | --- | --- | --- |
| Within an LTS series | 8.4.y LTS to 8.4.x LTS | In-place, logical dump and load, MySQL Clone, or by using replication |  |
| From an LTS or Bugfix series to the previous LTS or Bugfix series | 8.4.x LTS to 8.0.y | Logical dump and load or by using replication | Only supported for rollback purposes (that is, if no new server functionality has been applied to the data) |
| From an LTS or Bugfix series to an Innovation series *after the previous LTS series* | 8.4.x LTS to 8.3.0 Innovation | Logical dump and load or by using replication | Only supported for rollback purposes (that is, if no new server functionality has been applied to the data) |
| From within an Innovation series | 26.10 to 9.6 | Logical dump and load or by using replication | Only supported for rollback purposes (that is, if no new server functionality has been applied to the data) |