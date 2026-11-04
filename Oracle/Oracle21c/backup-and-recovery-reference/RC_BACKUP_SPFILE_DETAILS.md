---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_SPFILE_DETAILS.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

`RC_BACKUP_SPFILE_DETAILS` provides detailed information about SPFILE backups for each database registered in the recovery catalog.

This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier. Use in joins with `RC_RMAN_OUTPUT` and `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `SESSION_RECID` | `NUMBER` | With `SESSION_STAMP`, uniquely identifies output for this backup job from `RC_RMAN_OUTPUT`. |
| `SESSION_STAMP` | `NUMBER` | With `SESSION_RECID`, uniquely identifies output for this backup job from `RC_RMAN_OUTPUT`. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `BS_KEY` | `NUMBER` | Unique backup set identifier. Use this column to join with `RC_BACKUP_SET` or `RC_BACKUP_PIECE`. |
| `SET_STAMP` | `NUMBER` | Set stamp. |
| `SET_COUNT` | `NUMBER` | Set count. |
| `MODIFICATION_TIME` | `DATE` | Modification time. |
| `FILESIZE` | `NUMBER` | Size in bytes of the `SPFILE` that was backed up. |
| `FILESIZE_DISPLAY` | `VARCHAR2(32K)` | Same value as `FILESIZE`, but converted to a user-displayable format, for example, 798.01M or 5.25G. |