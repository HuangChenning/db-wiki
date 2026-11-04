---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_PIECE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about backup pieces. This view corresponds to the `V$BACKUP_PIECE` view.

Each backup set contains one or more backup pieces. Multiple copies of the same backup piece can exist, but each copy has its own record in the control file and its own row in the view.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DB_ID` | `NUMBER` | The database identifier. |
| `PDB_KEY` | `NUMBER` | The primary key of the PDB in the recovery catalog. Use this column to identify the PDB that owns the backup piece. |
| `BP_KEY` | `NUMBER` | The primary key for the backup piece in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The backup piece `RECID` from `V$BACKUP_PIECE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The backup piece stamp propagated from `V$BACKUP_PIECE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `BS_KEY` | `NUMBER` | The primary key of the backup set to which this record belongs in the recovery catalog. Use this column to join with `RC_BACKUP_SET`, `RC_BACKUP_CONTROLFILE`, `RC_BACKUP_DATAFILE`, and so on. |
| `SET_STAMP` | `NUMBER` | The `SET_STAMP` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `SET_COUNT` | `NUMBER` | The `SET_COUNT` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `BACKUP_TYPE` | `VARCHAR2(1)` | The type of the backup: `D` (full or level 0 incremental), `I` (incremental level 1), `L` (archived redo log). |
| `INCREMENTAL_LEVEL` | `NUMBER` | The level of the incremental backup: `NULL,` 0, or 1. |
| `PIECE#` | `NUMBER` | The number of the backup piece. The first piece has the value of 1. |
| `COPY#` | `NUMBER` | The copy number of the backup piece. |
| `DEVICE_TYPE` | `VARCHAR2(255)` | The type of backup device, for example, `DISK`. |
| `HANDLE` | `VARCHAR2(1024)` | The file name of the backup piece. |