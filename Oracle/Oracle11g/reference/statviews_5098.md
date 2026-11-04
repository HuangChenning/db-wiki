---
title: DBA_WORKLOAD_SCHEDULE_ORDERING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5098.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_WORKLOAD_SCHEDULE_ORDERING` displays the start ordering between workload captures in the replay schedule. Each row in the view defines one start ordering between two workload captures in the same replay schedule.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEDULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a schedule to be replayed |
| `SCHEDULE_CAP_ID` | `NUMBER` | `NOT NULL` | Identifies the workload capture that will wait |
| `WAITFOR_CAP_ID` | `NUMBER` | `NOT NULL` | Identifies the workload capture for which the workload capture identified by `SCHEDULE_CAP_ID` needs to wait. The replay of capture `SCHEDULE_CAP_ID` will not start until capture `WAITFOR_CAP_ID` finishes its replay.  If the view has multiple rows with the same `SCHEDULE_CAP_ID` but different `WAITFOR_CAP_ID`, it defines a schedule so that the replay of a capture specified by `SCHEDULE_CAP_ID` will not start unless all the replays of the waited captures run into completion.  If the view has multiple rows with the same `WAITFOR_CAP_ID` but different `SCHEDULE_CAP_ID`, it defines a schedule so that the replay of multiple captures will not start unless the replay of the capture specified by `WAITFOR_CAP_ID` finishes. |

Note:

This view is available starting with Oracle Database 11g Release 2 (11.2.0.4).