---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_AUTOTASK_WINDOW_HISTORY.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_AUTOTASK_WINDOW_HISTORY` displays historical information for automated maintenance task windows.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WINDOW_NAME` | `VARCHAR2(261)` |  | Name of the maintenance window |
| `WINDOW_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Window start time |
| `WINDOW_END_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Window end time |