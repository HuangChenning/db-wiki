---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_SET_SUMMARY.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

`RC_BACKUP_SET_SUMMARY` provides aggregate information about available backup sets for each database registered in the recovery catalog.

This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `NUM_BACKUPSETS` | `NUMBER` | Total number of available backup sets recorded in the recovery catalog for this database. |
| `OLDEST_BACKUP_TIME` | `DATE` | Creation time of the oldest available backup set recorded in the recovery catalog for this database. |
| `NEWEST_BACKUP_TIME` | `DATE` | Creation time of the newest available backup set recorded in the recovery catalog for this database. |
| `OUTPUT_BYTES` | `NUMBER` | Sum of sizes of all backup pieces for all available backup sets recorded in the recovery catalog for this database. |
| `ORIGINAL_INPUT_BYTES` | `NUMBER` | Sum of sizes of all input files for all available backup sets recorded in the recovery catalog for this database. |
| `ORIGINAL_INPRATE_BYTES` | `NUMBER` | Average input rate in bytes for the creation of all available backup sets recorded in the recovery catalog for this database. |
| `OUTPUT_RATE_BYTES` | `NUMBER` | Average output rate in bytes for the creation of all available backup sets recorded in the recovery catalog for this database. |
| `COMPRESSION_RATIO` | `NUMBER` | Aggregate compression ratio for all available backup sets recorded in the recovery catalog for this database. |
| `ORIGINAL_INPUT_BYTES_DISPLAY` | `VARCHAR2(32K)` | Total size of all input files stored in all available backup sets recorded in the recovery catalog for this database. |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(32K)` | Same value as `OUTPUT_BYTES`, but converted to a user-displayable format, for example, 798.01M or 5.25G. |
| `ORIGINAL_INPRATE_BYTES_DISPLAY` | `VARCHAR2(32K)` | Same value as `ORIGINAL_INPRATE_BYTES`, but converted to a user-displayable format, for example, 798.01M or 5.25G. |
| `OUTPUT_RATE_BYTES_DISPLAY` | `VARCHAR2(32K)` | Same value as `OUTPUT_RATE_BYTES`, but converted to a user-displayable format, for example, 798.01M or 5.25G. |