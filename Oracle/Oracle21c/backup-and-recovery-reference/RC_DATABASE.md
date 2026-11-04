---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_DATABASE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view gives information about the databases registered in the recovery catalog. It corresponds to the `V$DATABASE` view.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the current incarnation. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DBID` | `NUMBER` | Unique identifier for the database obtained from `V$DATABASE`. |
| `NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database for the current incarnation. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` of the current database incarnation. |
| `RESETLOGS_TIME` | `DATE` | The timestamp of the `RESETLOGS` of the current database incarnation. |
| `FINAL_CHANGE#` | `NUMBER` | The highest SCN to which a database can be recovered when using backups and redo logs available on Zero Data Loss Recovery Appliance (Recovery Appliance).  Use this value in the `SET UNTIL SCN` clause while recovering a database after the loss of all data files and online redo log files.  See Also: [Zero Data Loss Recovery Appliance Protected Database Configuration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=AMPDB871) |