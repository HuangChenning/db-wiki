---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ACTIVITY_SNAPSHOT_META.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.10 DBA\_ACTIVITY\_SNAPSHOT\_META

`DBA_ACTIVITY_SNAPSHOT_META` displays information about activity snapshots taken by the Object Activity Tracking System (OATS).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Activity snapshot identifier |
| `CON_DBNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the container to which the data pertains |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Identifier for the instance in which the activity snapshot was taken |
| `BEGIN_TIME` | `TIMESTAMP(3)` | `NOT NULL` | Begin time for the activity snapshot interval |
| `END_TIME` | `TIMESTAMP(3)` | `NOT NULL` | End time for the activity snapshot interval |
| `FLUSH_ELAPSED_TIME` | `INTERVAL DAY(2) TO SECOND(3)` |  | Amount of time spent creating the activity snapshot |
| `FLUSH_IS_MANUAL` | `VARCHAR2(3)` |  | Indicates whether the activity snapshot was created manually (`YES`) or not (`NO`) |

Note:

This view is available starting with Oracle Database 21c.