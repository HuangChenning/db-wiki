---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_DATABASE_INCARNATION.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about all database incarnations registered in the recovery catalog.

Oracle creates a new incarnation whenever you open a database with the `RESETLOGS` option. Records about the current and immediately previous incarnation are also contained in the `V$DATABASE` view.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the database. Use this column to join with almost any other catalog view. |
| `DBID` | `NUMBER` | Unique identifier for the database. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation. |
| `GUID` | `RAW(16)` | Globally unique identifier (GUID) of this PDB. |
| `NAME` | `VARCHAR2(8)` | The `DB_NAME` for the database at the time of the `RESETLOGS`. The value is `UNKNOWN` if you have done at least one `RESETLOGS` before registering the target database with RMAN, because RMAN does not know the `DB_NAME` before the `RESETLOGS`. |
| `REG_DB_UNIQUE_NAME` | `VARCHAR2(30)` | `DB_UNIQUE_NAME` of the database that registered this database. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` operation that created this incarnation. |
| `RESETLOGS_TIME` | `DATE` | The time stamp of the `RESETLOGS` operation that created this incarnation. |
| `CURRENT_INCARNATION` | `VARCHAR2(3)` | `YES` if it is the current incarnation; `NO` if it is not. |
| `PARENT_DBINC_KEY` | `NUMBER` | The `DBINC_KEY` of the previous incarnation for this database. The value is `NULL` if it is the first incarnation recorded for the database. |
| `PRIOR_RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` operation that created the parent of this incarnation. |
| `PRIOR_RESETLOGS_TIME` | `DATE` | The time stamp of the `RESETLOGS` operation that created the parent of this incarnation. |
| `STATUS` | `VARCHAR2(8)` | `CURRENT` if this incarnation is the current database incarnation. `PARENT` if this is a noncurrent incarnation that is a direct ancestor of the current incarnation. `ORPHAN` if this is a noncurrent incarnation that is not a direct ancestor of the current incarnation. |
| `CON_ID` | `NUMBER` | ID of the container to which the data pertains. Possible values include:  - 0: Rows containing data that pertain to the whole multitenant container database (CDB) - 1: Rows containing data that pertains only to the root - n: Where n is the applicable container ID for the rows containing data |