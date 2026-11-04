---
title: "MySQL :: MySQL 26.10 Reference Manual :: 25.6.8 Online Backup of NDB Cluster"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/mysql-cluster-backup.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 25.6.8 Online Backup of NDB Cluster

The next few sections describe how to prepare for and then to create an NDB Cluster backup using the functionality for this purpose found in the [**ndb\_mgm**](mysql-cluster-programs-ndb-mgm.md) management client. To distinguish this type of backup from a backup made using [**mysqldump**](mysqldump.md), we sometimes refer to it as a “native” NDB Cluster backup. (For information about the creation of backups with [**mysqldump**](mysqldump.md), see [Section 6.5.4, “mysqldump — A Database Backup Program”](mysqldump.md).) Restoration of NDB Cluster backups is done using the [**ndb\_restore**](mysql-cluster-programs-ndb-restore.md) utility provided with the NDB Cluster distribution; for information about [**ndb\_restore**](mysql-cluster-programs-ndb-restore.md) and its use in restoring NDB Cluster backups, see [Section 25.5.23, “ndb\_restore — Restore an NDB Cluster Backup”](mysql-cluster-programs-ndb-restore.md).

It is also possible to create backups using multiple LDMs to achieve parallelism on the data nodes. See [Section 25.6.8.5, “Taking an NDB Backup with Parallel Data Nodes”](mysql-cluster-backup-parallel-data-nodes.md).