---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_COPY_SUMMARY.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

`RC_BACKUP_COPY_SUMMARY` contains summary information about all `AVAILABLE` control file and data file copies for each database.

This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `NUM_COPIES` | `NUMBER` | Total number of image copy backups. |
| `NUM_DISTINCT_COPIES` | `NUMBER` | Number of distinct image copy backups. |
| `MIN_CHECKPOINT_CHANGE#` | `NUMBER` | Minimum checkpoint SCN among all image copy backups described in this view. |
| `MAX_CHECKPOINT_CHANGE#` | `NUMBER` | Maximum checkpoint SCN among all image copy backups described in this view. |
| `MIN_CHECKPOINT_TIME` | `DATE` | Earliest checkpoint time among all copies described in this view. |
| `MAX_CHECKPOINT_TIME` | `DATE` | Latest checkpoint time among all copies described in this view. |
| `OUTPUT_BYTES` | `NUMBER` | Sum of sizes of all data file and control file copies. |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(32K)` | Same value as `OUTPUT_BYTES`, but converted to a user-displayable format, for example, 798.01M or 5.25G. |