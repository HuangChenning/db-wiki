---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTO_MV_VERIFICATION_STATUS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.188 DBA\_AUTO\_MV\_VERIFICATION\_STATUS

`DBA_AUTO_MV_VERIFICATION_STATUS` displays the status of verifications associated with automatic materialized views.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `EXECUTION_NAME` | `VARCHAR2(128)` | `NOT NULL` | The name of the task execution with which this entry (row) is associated |
| `STS_NAME_FOR_SRS` | `VARCHAR2(256)` |  | Name of the SQL tuning set used for simple random sampling |
| `STS_OWNER_NAME_FOR_SRS` | `CHAR(3)` |  | Owner of the SQL tuning set used for simple random sampling |
| `SPA_TASK_NAME_FOR_SRS` | `VARCHAR2(256)` |  | Name of the SQL Performance Analyzer task used for simple random sampling |
| `SPA_OWNER_NAME_FOR_SRS` | `CHAR(3)` |  | Owner of the SQL Performance Analyzer task used for simple random sampling |
| `STS_NAME_FOR_VERIFICATION` | `VARCHAR2(256)` |  | Name of the SQL tuning set used for verification on sampled queries |
| `STS_OWNER_NAME_FOR_VERIFICATION` | `CHAR(3)` |  | Owner of the SQL tuning set used for verification on sampled queries |
| `SPA_TASK_NAME_FOR_VERIFICATION` | `VARCHAR2(256)` |  | Name of the SQL Performance Analyzer task used for for verification on sampled queries |
| `SPA_OWNER_NAME_FOR_VERIFICATION` | `CHAR(3)` |  | Owner of the SQL Performance Analyzer task used for for verification on sampled queries |
| `START_TIME` | `TIMESTAMP(6)` |  | Date and time the verification started |
| `END_TIME` | `TIMESTAMP(6)` |  | Date and time the verification ended |
| `STATUS` | `VARCHAR2(128)` |  | Verification status |

Note:

This view is available starting with Oracle Database 21c.