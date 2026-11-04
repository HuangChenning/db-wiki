---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_RESYNC.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about recovery catalog resynchronizations. Every full resynchronization takes a snapshot of the target database control file and resynchronizes the recovery catalog from the snapshot.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `RESYNC_KEY` | `NUMBER` | The primary key for the resynchronization. |
| `CONTROLFILE_CHANGE#` | `NUMBER` | The control file checkpoint SCN from which the catalog was resynchronized. |
| `CONTROLFILE_TIME` | `DATE` | The control file checkpoint time stamp from which the catalog was resynchronized. |
| `CONTROLFILE_SEQUENCE#` | `NUMBER` | The control file sequence number. |
| `CONTROLFILE_VERSION` | `DATE` | The creation time for the version of the control file from which the catalog was resynchronized. |
| `RESYNC_TYPE` | `VARCHAR2(7)` | The type of resynchronization: `FULL` or `PARTIAL`. |
| `DB_STATUS` | `VARCHAR2(7)` | The status of the target database: `OPEN` or `MOUNTED`. |
| `RESYNC_TIME` | `DATE` | The time of the resynchronization. |