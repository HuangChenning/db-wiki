---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_RESTORE_POINT.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists all restore points for all incarnations of the database since the last catalog resynchronization. This view corresponds to `V$RESTORE_POINT`.

| Column | Data Type | Description |
| --- | --- | --- |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `RECID` | `NUMBER` | The recid of the corresponding row in the control file. |
| `STAMP` | `NUMBER` | The timestamp of the row in the control file. (Because control file records are reused, you must combine the timestamp and recid to get a value unique across all records in `RC_RMAN_STATUS`.) |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this restore point. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |
| `NAME` | `VARCHAR2(128)` | The name of the restore point. |
| `RESTORE_POINT_TIME` | `DATE` | The database time associated with the restore point SCN. |
| `CREATION_TIME` | `DATE` | The date when the restore point was created. |
| `SCN` | `NUMBER` | The database SCN when the restore point was created |
| `LONG_TERM` | `VARCHAR2(3)` | `YES` if the restore point is associated with a backup created with the `KEEP` option specified; otherwise `NO`. |
| `PRESERVED` | `VARCHAR2(3)` | `YES` if the restore point must be explicitly deleted; otherwise `NO`. |
| `GUARANTEE_FLASHBACK_DATABASE` | `VARCHAR2(3)` | `YES` if the flashback logs must be retained to guarantee a flashback to this point; otherwise `NO`. |
| `PDB_KEY` | `NUMBER` | The primary key of the PDB in the recovery catalog. |
| `CLEAN` | `VARCHAR2(3)` | Indicates whether the restore point is a clean PDB restore point. Possible values are YES or NO. |