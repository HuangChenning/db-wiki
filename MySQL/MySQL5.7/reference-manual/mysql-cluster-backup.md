---
title: "21.6.8 Online Backup of NDB Cluster"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-backup.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.6.8 Online Backup of NDB Cluster

The next few sections describe how to prepare for and then to create an NDB Cluster backup using the functionality for this purpose found in the [**ndb\_mgm**](mysql-cluster-programs-ndb-mgm.md) management client. To distinguish this type of backup from a backup made using [**mysqldump**](mysqldump.md), we sometimes refer to it as a “native” NDB Cluster backup. (For information about the creation of backups with [**mysqldump**](mysqldump.md), see [Section 4.5.4, “mysqldump — A Database Backup Program”](mysqldump.md).) Restoration of NDB Cluster backups is done using the [**ndb\_restore**](mysql-cluster-programs-ndb-restore.md) utility provided with the NDB Cluster distribution; for information about [**ndb\_restore**](mysql-cluster-programs-ndb-restore.md) and its use in restoring NDB Cluster backups, see [Section 21.5.24, “ndb\_restore — Restore an NDB Cluster Backup”](mysql-cluster-programs-ndb-restore.md).