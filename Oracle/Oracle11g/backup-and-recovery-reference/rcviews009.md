---
title: RC_BACKUP_COPY_SUMMARY
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews009.htm
tags:
  - oracle
  - 11g
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
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Same value as `OUTPUT_BYTES`, but converted to a user-displayable format, for example, 798.01M or 5.25G. |