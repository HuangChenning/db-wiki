---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTO_MV_MAINT_REPORT.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.185 DBA\_AUTO\_MV\_MAINT\_REPORT

`DBA_AUTO_MV_MAINT_REPORT` displays maintenance operation details associated with automatic materialized view refresh.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SWAT_MM_START_TIME` | `DATE` |  | Date and time of the maintenance invocation |
| `MESSAGE` | `VARCHAR2(4000)` |  | Message associated with the materialized view maintenance action |

Note:

This view is available starting with Oracle Database 21c.