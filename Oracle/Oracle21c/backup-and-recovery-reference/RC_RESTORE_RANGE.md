---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_RESTORE_RANGE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

The `RC_RESTORE_RANGE` view contains details about the restore range of databases registered in the recovery catalog.

Because a database can have multiple restore ranges, this view can contain multiple rows for a single database. This view corresponds to the `V$RESTORE_RANGE` view.

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