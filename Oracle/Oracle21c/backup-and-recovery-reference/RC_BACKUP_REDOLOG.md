---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_BACKUP_REDOLOG.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about archived redo log files in backup sets. It corresponds to the `V$BACKUP_REDOLOG` view.

You cannot back up online logs directly: you must first archive them to disk and then back them up. An archived log backup set contains one or more archived logs.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `BRL_KEY` | `NUMBER` | The primary key of the archived redo log in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The record identifier propagated from `V$BACKUP_REDOLOG`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The stamp from `V$BACKUP_REDOLOG`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `BS_KEY` | `NUMBER` | The primary key of the backup set to which this record belongs in the recovery catalog. Use this column to join with `RC_BACKUP_SET` or `RC_BACKUP_PIECE`. |
| `SET_STAMP` | `NUMBER` | The `SET_STAMP` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `SET_COUNT` | `NUMBER` | The `SET_COUNT` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `BACKUP_TYPE` | `VARCHAR2(1)` | The type of the backup: `L` (archived redo log). |
| `COMPLETION_TIME` | `DATE` | The time when the backup completed. |
| `THREAD#` | `NUMBER` | The thread number of the redo log. |
| `SEQUENCE#` | `NUMBER` | The log sequence number. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the most recent `RESETLOGS` when the record was created. |
| `RESETLOGS_TIME` | `DATE` | The time stamp of the most recent `RESETLOGS` when the record was created. |
| `FIRST_CHANGE#` | `NUMBER` | The SCN generated when Oracle switched into the redo log. |
| `FIRST_TIME` | `DATE` | The time when Oracle switched into the redo log. |
| `NEXT_CHANGE#` | `NUMBER` | The first SCN of the next redo log in the thread. |
| `NEXT_TIME` | `DATE` | The first time stamp of the next redo log in the thread. |
| `BLOCKS` | `NUMBER` | The number of operating system blocks written to the backup. |
| `BLOCK_SIZE` | `NUMBER` | The number of bytes in each block of this redo log. |
| `STATUS` | `VARCHAR2(1)` | The status of the backup set: `A` (all pieces available), `D` (all pieces deleted), `O` (some pieces are available but others are not, so the backup set is unusable). |
| `BS_RECID` | `NUMBER` | The `RECID` value from `V$BACKUP_SET`. |
| `BS_STAMP` | `NUMBER` | The `STAMP` value from `V$BACKUP_SET`. `BS_STAMP` is different from `SET_STAMP`. `BS_STAMP` is the stamp of the backup set record when created in the control file, whereas `SET_STAMP` joins with `SET_COUNT` to make a unique identifier. |
| `PIECES` | `NUMBER` | The number of pieces in the backup set. |
| `TERMINAL` | `VARCHAR2(3)` | Indicates whether this log was created during terminal recovery of a standby database. Values are `YES` or `NO`. |
| `PARTIAL` | `VARCHAR2(3)` | Indicates that this archivelog is created during the activation of failover of a standby database and it contains partial archivelog contents. It is created by Zero Data Loss Recovery Appliance (ZDLRA) when the connection with the primary database is lost. A value of YES indicates that the log is partial. |