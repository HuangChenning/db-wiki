---
title: "MySQL :: MySQL 26.7 Reference Manual :: 9.5 Point-in-Time (Incremental) Recovery"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/point-in-time-recovery.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 9.5 Point-in-Time (Incremental) Recovery

Point-in-time recovery refers to recovery of data changes up to a given point in time. Typically, this type of recovery is performed after restoring a full backup that brings the server to its state as of the time the backup was made. (The full backup can be made in several ways, such as those listed in [Section 9.2, “Database Backup Methods”](backup-methods.md).) Point-in-time recovery then brings the server up to date incrementally from the time of the full backup to a more recent time.