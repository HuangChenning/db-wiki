---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_AUTOTASK_SCHEDULE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_AUTOTASK_SCHEDULE` displays the schedule of maintenance windows for the next 32 days for each client.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WINDOW_NAME` | `VARCHAR2(128)` |  | Name of the maintenance window |
| `START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Projected start time of the window |
| `DURATION` | `INTERVAL DAY(3) TO SECOND(0)` |  | Currently defined duration of the window (NULL for the currently open window) |