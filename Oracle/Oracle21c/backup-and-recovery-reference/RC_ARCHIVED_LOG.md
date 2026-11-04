---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_ARCHIVED_LOG.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view contains historical information about archived and unarchived redo log files. It corresponds to the `V$ARCHIVED_LOG` view in the target database control file.

Oracle inserts an archived redo log record after the online redo log is successfully archived. If a log that has not been archived is cleared, then a record is inserted with the `NAME` column set to `NULL`. If the log is archived multiple times, then the view contains multiple archived log records with the same `THREAD#`, `SEQUENCE#`, and `RESETLOGS_CHANGE#`, but with a different name.

An archived log record is also inserted when an archived log is restored from a backup set or a copy. An archived log can have no record if the record ages out of the control file.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database to which this record belongs. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `AL_KEY` | `NUMBER` | The primary key of the archived redo log in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The archived redo log `RECID` from `V$ARCHIVED_LOG`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The archived redo log stamp from `V$ARCHIVED_LOG`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `NAME` | `VARCHAR2(1024)` | The file name of the archived redo log. |
| `THREAD#` | `NUMBER` | The number of the redo thread. |
| `SEQUENCE#` | `NUMBER` | The log sequence number. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The `SCN` of the most recent `RESETLOGS` when the record was created. |
| `RESETLOGS_TIME` | `DATE` | The time stamp of the most recent `RESETLOGS` when the record was created. |
| `FIRST_CHANGE#` | `NUMBER` | The first SCN of this redo log. |
| `FIRST_TIME` | `DATE` | The time when Oracle switched into the redo log. |
| `NEXT_CHANGE#` | `NUMBER` | The first SCN of the next redo log in the thread. |
| `NEXT_TIME` | `DATE` | The first time stamp of the next redo log in the thread. |
| `BLOCKS` | `NUMBER` | The size of this archived log in operating system blocks. |
| `BLOCK_SIZE` | `NUMBER` | The size of the block in bytes. |
| `COMPLETION_TIME` | `DATE` | The time when the redo log was archived or copied. |
| `ARCHIVED` | `VARCHAR2(3)` | Indicates whether the log was archived: `YES` (archived redo log) or `NO` (inspected file header of online redo log and added record to `V$ARCHIVED_LOG`). Inspecting the online logs creates archived log records for them, which allows them to be applied during RMAN recovery. Oracle sets `ARCHIVED` to `NO` to prevent online logs from being backed up. |
| `STATUS` | `VARCHAR2(1)` | The status of the archived redo log: `A` (available), `U` (unavailable), `D` (deleted), or X (expired). |
| `IS_STANDBY` | `VARCHAR2(3)` | The database that archived this log: `Y` (belongs to a standby database) or `N` (belongs to the primary database). |
| `DICTIONARY_BEGIN` | `VARCHAR2(3)` | Indicates whether this archived log contains the start of a LogMiner dictionary: `YES` or `NO`.  If both `DICTIONARY_BEGIN` and `DICTIONARY_END` are `YES`, then this log contains a complete LogMiner dictionary. If `DICTIONARY_BEGIN` is `YES` but `DICTIONARY_END` is `NO`, this log contains the start of the dictionary, and it continues through each subsequent log of this thread and ends in the log where `DICTIONARY_END` is `YES`. |
| `DICTIONARY_END` | `VARCHAR2(3)` | Indicates whether this archived log contains the end of a LogMiner dictionary: `YES` or `NO`. See the description of `DICTIONARY_BEGIN` for an explanation of how to interpret this value. |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | This copy is located in the fast recovery area: `YES` or `NO`. |
| `COMPRESSED` | `VARCHAR2(3)` | Internal only |
| `CREATOR` | `VARCHAR2(7)` | Creator of the archived redo log:  - `ARCH` - Archiver process - `FGRD` - Foreground process - `RMAN` - Recovery Manager - `SRMN` - RMAN at standby - `LGWR` - Log Writer process |
| `TERMINAL` | `VARCHAR2(3)` | Indicates whether this log was created during terminal recovery of a standby database. Values are `YES` or `NO`. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this file. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |