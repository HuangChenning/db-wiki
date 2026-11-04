---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_SPFILE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about server parameter files in backup sets.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `BSF_KEY` | `NUMBER` | The primary key of the server parameter file in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The record identifier propagated from `V$BACKUP_SPFILE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The stamp from `V$BACKUP_SPFILE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `BS_KEY` | `NUMBER` | The primary key of the backup set to which this record belongs in the recovery catalog. Use this column to join with `RC_BACKUP_SET`. |
| `SET_STAMP` | `NUMBER` | The `SET_STAMP` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `SET_COUNT` | `NUMBER` | The `SET_COUNT` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `MODIFICATION_TIME` | `DATE` | The time when the server parameter file was last modified. |
| `STATUS` | `VARCHAR2(1)` | The status of the backup set: `A` (all backup pieces available), `D` (all backup pieces deleted), `O` (some backup pieces are available but others are not, so the backup set is unusable). |
| `BS_RECID` | `NUMBER` | The `RECID` value from `V$BACKUP_SET`. |
| `BS_STAMP` | `NUMBER` | The `STAMP` value from `V$BACKUP_SET`. `BS_STAMP` is different from `SET_STAMP`. `BS_STAMP` is the stamp of the backup set record when created in the control file, whereas `SET_STAMP` joins with `SET_COUNT` to make a unique identifier. |
| `COMPLETION_TIME` | `DATE` | The time when the backup set completed. |
| `BYTES` | `NUMBER` | The size of the backup set in bytes. |
| `DB_UNIQUE_NAME` | `VARCHAR2(30)` | The `DB_UNIQUE_NAME` of the database to which this record belongs. |