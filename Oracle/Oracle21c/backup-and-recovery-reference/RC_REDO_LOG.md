---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_REDO_LOG.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about the online redo logs for all incarnations of the database since the last catalog resynchronization. This view corresponds to a join of the `V$LOG` and `V$LOGFILE` views.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `THREAD#` | `NUMBER` | The number of the redo thread. |
| `GROUP#` | `NUMBER` | The number of the online redo log group. |
| `NAME` | `VARCHAR2(1024)` | The name of the online redo log file. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this file. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |
| `BYTES` | `NUMBER` | The size of the file in bytes. |
| `TYPE` | `VARCHAR2(7)` | The type of redo log: `ONLINE` or `STANDBY`. |