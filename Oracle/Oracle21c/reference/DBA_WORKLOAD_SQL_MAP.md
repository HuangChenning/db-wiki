---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WORKLOAD_SQL_MAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.130 DBA\_WORKLOAD\_SQL\_MAP

`DBA_WORKLOAD_SQL_MAP` contains the mapping information for skipping or replacing a SQL statement based on its sql\_id during workload replay.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPLAY_ID` | `NUMBER(38)` | `NOT NULL` | A foreign key to the ID column in the DBA\_WORKLOAD\_REPLAYs view |
| `SCHEDULE_CAP_ID` | `NUMBER(38)` | `NOT NULL` | The ID of a capture in the schedule |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the SQL statement at the time of capture |
| `OPERATION` | `VARCHAR2(7)` |  | `SKIP` or `REPLACE` |
| `SQL_ID_NUMBER` | `NUMBER` |  | Internal representation of `SQL_ID` |
| `REPLACEMENT_SQL_TEXT` | `VARCHAR2(4000)` |  | When the value in the `OPERATION` column is `SKIP`, this column is NULL.  When the value in the `OPERATION` column is `REPLACE`, this column shows the SQL statement to be used. |