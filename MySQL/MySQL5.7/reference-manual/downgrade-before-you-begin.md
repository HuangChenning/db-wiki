---
title: "2.11.1 Before You Begin"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/downgrade-before-you-begin.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 2.11.1 Before You Begin

Review the information in this section before downgrading. Perform any recommended actions.

- Protect your data by taking a backup. The backup should include the `mysql` database, which contains the MySQL system tables. See [Section 7.2, “Database Backup Methods”](backup-methods.md).
- Review [Section 2.11.2, “Downgrade Paths”](downgrade-paths.md) to ensure that your intended downgrade path is supported.
- Review [Section 2.11.3, “Downgrade Notes”](downgrading-to-previous-series.md) for items that may require action before downgrading.
	Note
	The downgrade procedures described in the following sections assume you are downgrading with data files created or modified by the newer MySQL version. However, if you did not modify your data after upgrading, downgrading using backups taken *before* upgrading to the new MySQL version is recommended. Many of the changes described in [Section 2.11.3, “Downgrade Notes”](downgrading-to-previous-series.md) that require action are not applicable when downgrading using backups taken *before* upgrading to the new MySQL version.
- Use of new features, new configuration options, or new configuration option values that are not supported by a previous release may cause downgrade errors or failures. Before downgrading, reverse changes resulting from the use of new features and remove configuration settings that are not supported by the release you are downgrading to.