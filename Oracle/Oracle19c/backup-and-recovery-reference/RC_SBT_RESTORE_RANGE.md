---
title: Backup and Recovery Reference
book: Oracle AI Database Backup and Recovery Reference
doc_id: E96242-15
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/rcmrf/RC_SBT_RESTORE_RANGE.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-reference
---

## 5.55 RC\_SBT\_RESTORE\_RANGE

The `RC_SBT_RESTORE_RANGE` view contains information about the restore range of the database for backup data that is stored on tape.

This view corresponds to the `V$SBT_RESTORE_RANGE` view.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The unique database identifier. |
| `SITE_KEY` | `NUMBER` | The primary key of the database site that is associated with this restore range. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use the `SITE_KEY` in join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |
| `LOW_TIME` | `DATE` | The earliest time to which the database can be restored. |
| `HIGH_TIME` | `DATE` | The latest time to which the database can be restored. |
| `LOW_SCN` | `NUMBER` | The lowest SCN to which the database can be restored. |
| `HIGH_SCN` | `NUMBER` | The highest SCN to which the database can be restored. |
| `LOW_DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the database to which `LOW_SCN` belongs. |
| `HIGH_DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the database to which `HIGH_SCN` belongs. |