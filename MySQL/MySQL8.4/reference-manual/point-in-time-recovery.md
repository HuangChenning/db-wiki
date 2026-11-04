---
title: "9.5 Point-in-Time (Incremental) Recovery"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/point-in-time-recovery.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

Point-in-time recovery refers to recovery of data changes up to a given point in time. Typically, this type of recovery is performed after restoring a full backup that brings the server to its state as of the time the backup was made. (The full backup can be made in several ways, such as those listed in [Section 9.2, “Database Backup Methods”](backup-methods.md).) Point-in-time recovery then brings the server up to date incrementally from the time of the full backup to a more recent time.