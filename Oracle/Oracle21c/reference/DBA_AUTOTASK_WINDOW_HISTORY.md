---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTOTASK_WINDOW_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.204 DBA\_AUTOTASK\_WINDOW\_HISTORY

`DBA_AUTOTASK_WINDOW_HISTORY` displays historical information for automated maintenance task windows.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WINDOW_NAME` | `VARCHAR2(261)` |  | Name of the maintenance window |
| `WINDOW_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Window start time |
| `WINDOW_END_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Window end time |