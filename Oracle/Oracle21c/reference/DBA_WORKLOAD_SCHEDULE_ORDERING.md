---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WORKLOAD_SCHEDULE_ORDERING.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.129 DBA\_WORKLOAD\_SCHEDULE\_ORDERING

`DBA_WORKLOAD_SCHEDULE_ORDERING` displays the start ordering between workload captures in the replay schedule.

Each row in the view defines one start ordering between two workload captures in the same replay schedule.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEDULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a schedule to be replayed |
| `SCHEDULE_CAP_ID` | `NUMBER` | `NOT NULL` | Identifies the workload capture that will wait |
| `WAITFOR_CAP_ID` | `NUMBER` | `NOT NULL` | Identifies the workload capture for which the workload capture identified by `SCHEDULE_CAP_ID` needs to wait. The replay of capture `SCHEDULE_CAP_ID` will not start until capture `WAITFOR_CAP_ID` finishes its replay.  If the view has multiple rows with the same `SCHEDULE_CAP_ID` but different `WAITFOR_CAP_ID`, it defines a schedule so that the replay of a capture specified by `SCHEDULE_CAP_ID` will not start unless all the replays of the waited captures run into completion.  If the view has multiple rows with the same `WAITFOR_CAP_ID` but different `SCHEDULE_CAP_ID`, it defines a schedule so that the replay of multiple captures will not start unless the replay of the capture specified by `WAITFOR_CAP_ID` finishes. |