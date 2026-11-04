---
title: RC_BACKUP_SPFILE_SUMMARY
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews023.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

`RC_BACKUP_SPFILE_SUMMARY` provides summary information about server parameter file backups for databases registered in the recovery catalog.

This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `NUM_FILES_BACKED` | `NUMBER` | Number of files backed up. |
| `NUM_DISTINCT_FILES_BACKED` | `NUMBER` | Number of distinct files backed up (based on differing modification timestamps). |
| `MIN_MODIFICATION_TIME` | `DATE` | Earliest modification time of any `SPFILE` backed up for this database. |
| `MAX_MODIFICATION_TIME` | `DATE` | Latest modification time of any `SPFILE` backed up for this database. |
| `INPUT_BYTES` | `NUMBER` | Total number of bytes in the input files backed up. |
| `INPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Same value as `INPUT_BYTES`, but converted to a user-displayable format, for example, 798.01M or 5.25G. |