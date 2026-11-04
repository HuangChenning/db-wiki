---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ACTIVITY_CONFIG.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.8 DBA\_ACTIVITY\_CONFIG

`DBA_ACTIVITY_CONFIG` describes the configuration parameters that control the Object Activity Tracking System (OATS).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CON_DBNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the container to which the data pertains |
| `PARAMETER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the configuration parameter |
| `PARAMETER_VALUE` | `VARCHAR2(4000)` |  | Value of the configuration parameter |
| `LAST_UPDATED_TIME` | `TIMESTAMP(3)` |  | If the value of the configuration parameter was last updated by a user, then this column displays the time at which the parameter was updated. Otherwise, this column is null. |
| `LAST_UPDATED_USER` | `VARCHAR2(128)` |  | If the value of the configuration parameter was last updated by a user, then this column displays the name of the user who performed the update. Otherwise, this column is null. |

Note:

This view is available starting with Oracle Database 21c.