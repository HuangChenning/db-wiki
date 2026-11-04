---
title: RC_BACKUP_SPFILE_DETAILS
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews022.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

`RC_BACKUP_SPFILE_DETAILS` provides detailed information about SPFILE backups for each database registered in the recovery catalog.

This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier. Use in joins with `RC_RMAN_OUTPUT` and `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `SESSION_RECID` | `NUMBER` | Together with `SESSION_STAMP`, uniquely identifies output for this backup job from `RC_RMAN_OUTPUT`. |
| `SESSION_STAMP` | `NUMBER` | Together with `SESSION_RECID`, uniquely identifies output for this backup job from `RC_RMAN_OUTPUT`. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `BS_KEY` | `NUMBER` | Unique backup set identifier. Use this column to join with `RC_BACKUP_SET` or `RC_BACKUP_PIECE`. |
| `SET_STAMP` | `NUMBER` | Set stamp. |
| `SET_COUNT` | `NUMBER` | Set count. |
| `MODIFICATION_TIME` | `DATE` | Modification time. |
| `FILESIZE` | `NUMBER` | Size in bytes of the `SPFILE` that was backed up. |
| `FILESIZE_DISPLAY` | `VARCHAR2(4000)` | Same value as `FILESIZE`, but converted to a user-displayable format, for example, 798.01M or 5.25G. |