---
title: DBA_AUTOTASK_SCHEDULE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3089.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AUTOTASK_SCHEDULE` displays the schedule of maintenance windows for the next 32 days for each client.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WINDOW_NAME` | `VARCHAR2(30)` |  | Name of the maintenance window |
| `START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Projected start time of the window |
| `DURATION` | `INTERVAL DAY(3) TO SECOND(0)` |  | Currently defined duration of the window (NULL for the currently open window) |