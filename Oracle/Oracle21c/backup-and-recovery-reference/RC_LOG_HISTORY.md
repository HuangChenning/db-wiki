---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_LOG_HISTORY.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists historical information about the online redo logs.

RMAN adds a new row during a catalog resynchronization whenever Oracle has switched out of the online redo log. This catalog view corresponds to the `V$LOG_HISTORY` view.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `RECID` | `NUMBER` | The redo log history `RECID` from `V$LOG_HISTORY`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The redo log history stamp from `V$LOG_HISTORY`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `THREAD#` | `NUMBER` | The thread number of the online redo log. |
| `SEQUENCE#` | `NUMBER` | The log sequence number of the redo log. |
| `FIRST_CHANGE#` | `NUMBER` | The SCN generated when switching into the redo log. |
| `FIRST_TIME` | `DATE` | The time stamp when switching into the redo log. |
| `NEXT_CHANGE#` | `NUMBER` | The first SCN of the next redo log in the thread. |
| `CLEARED` | `VARCHAR2(3)` | `YES` if the redo log was cleared with the `ALTER DATABASE CLEAR LOGFILE` statement; otherwise, `NULL`. This statement allows a log to be dropped without archiving it first. |