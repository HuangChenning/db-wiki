---
title: "MySQL :: MySQL 26.10 Reference Manual :: 3.2 Upgrade Paths"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/upgrade-paths.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 3.2 Upgrade Paths

Notes

- Make sure you understand [the MySQL release model](mysql-releases.md) for MySQL for MySQL long long-term support (LTS) and Innovation versions before proceeding with a downgrade.
- We recommend checking upgrade compatibility with MySQL Shell's [Upgrade Checker Utility](https://dev.mysql.com/doc/mysql-shell/26.10/en/mysql-shell-utilities-upgrade.html) before performing an upgrade.
- A replication topology is upgraded by following the rolling upgrade scheme described at [Section 19.5.3, “Upgrading or Downgrading a Replication Topology”](replication-upgrade.md), which uses one of the supported single-server methods for each individual server upgrade.
- Monthly Rapid Updates (MRUs) and hot fixes also count as releases in this documentation.

### Calendar-Version Upgrade Validation

When a target server starts using a data directory created by another server version, it validates the persisted source-release metadata against its own release metadata. Starting with MySQL 26.7.0, this validation uses compatibility lineages rather than inferring compatibility from calendar version numbers alone.

The following rules apply:

- A sequential release can enter the first calendar-versioned lineage only from MySQL 9.7.x LTS. The target must belong to the lineage anchored by MySQL 9.7.0.
- Other sequential releases, including Innovation releases and earlier LTS series, cannot upgrade directly to a calendar-versioned release. Upgrade them through MySQL 9.7.x LTS first.
- An Innovation release can upgrade only to a later release in the same compatibility lineage.
- The LTS release that closes a lineage belongs to that lineage; therefore, an Innovation release can upgrade to that LTS release.
- An LTS release can upgrade into the immediately following lineage. For this comparison, only the \`YY.M\` release base of the source LTS release is considered; its patch number is ignored.
- An Innovation release cannot cross a lineage boundary, and an LTS release cannot skip a lineage.

Existing server upgrade thresholds continue to apply. An otherwise valid transition is rejected if the target is earlier than the applicable upgrade threshold and the transition crosses a visible release base.

**Table 3.1 Sequential and CalVer Upgrade Paths**

| Source | Target | Result | Reason |
| --- | --- | --- | --- |
| MySQL 9.7.x LTS | MySQL 26.7.0 Innovation | Accepted | MySQL 9.7.x LTS is the entry point to the first calendar-versioned lineage. |
| MySQL 9.6.x Innovation | MySQL 26.7.0 Innovation | Rejected | The source is not MySQL 9.7.x LTS. |
| MySQL 26.7.0 Innovation | MySQL 28.4.0 LTS | Accepted | Both releases belong to the lineage anchored by MySQL 9.7.0. |
| MySQL 28.1.0 Innovation | MySQL 28.10.0 Innovation | Rejected | The target belongs to the next compatibility lineage. |
| MySQL 28.4.0 LTS | MySQL 28.10.0 Innovation | Accepted | The target begins the lineage anchored by MySQL 28.4.0. |
| MySQL 28.4.0 LTS | MySQL 30.7.0 Innovation | Rejected | The target is beyond the immediately following lineage. |

**Table 3.2 Upgrade Paths for MySQL Server**

| Upgrade Path | Path Examples | Supported Upgrade Methods |
| --- | --- | --- |
| Within an LTS or Bugfix series | 8.0.37 to 8.0.46 or 8.4.0 to 8.4.11 | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), [replication](replication-upgrade.md), and [MySQL Clone](https://dev.mysql.com/doc/mysql-shell/26.10/en/mysql-innodb-cluster-clone-deployment.html) |
| From an LTS or Bugfix series to the next [LTS series](glossary.md) | 8.0.37 to 8.4.x LTS, 8.4.11 LTS to 9.7.2 LTS | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), and [replication](replication-upgrade.md) |
| From an LTS or Bugfix release to an Innovation release *before the next LTS series* | 8.0.34 to 8.3.0 or 8.4.x LTS to 9.6.0 | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), and [replication](replication-upgrade.md) |
| From an [Innovation series](glossary.md) to the next [LTS series](glossary.md) | 8.3.0 to 8.4 LTS, 9.5 to 9.7 LTS | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), and [replication](replication-upgrade.md) |
| From an Innovation series to an Innovation release *after the next LTS series* | Not allowed, several steps are required: 8.3.0 to 8.4 LTS, and 8.4 LTS to 9.7, and 9.7 to 26.7 Innovation | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), and [replication](replication-upgrade.md) |
| From within an Innovation series | 8.1.0 to 8.3.0 | [In-place upgrade](upgrade-binary-package.md), [logical dump and load](upgrade-binary-package.md), and [replication](replication-upgrade.md) |
| From MySQL 5.7 to an LTS or Innovation release | MySQL 5.7 to 8.4 | A bugfix or LTS series cannot be skipped, so in this example first upgrade MySQL 5.7 to MySQL 8.0, and then upgrade MySQL 8.0 to MySQL 8.4. |