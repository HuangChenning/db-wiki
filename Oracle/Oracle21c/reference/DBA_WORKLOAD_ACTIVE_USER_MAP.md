---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WORKLOAD_ACTIVE_USER_MAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.116 DBA\_WORKLOAD\_ACTIVE\_USER\_MAP

`DBA_WORKLOAD_ACTIVE_USER_MAP` contains the mappings that are going to be valid for the next replay or are valid for the current replay.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEDULE_CAP_ID` | `NUMBER` |  | The ID of a capture in the schedule |
| `CAPTURE_USER` | `VARCHAR2(4000)` | `NOT NULL` | The user name during the time of the workload capture |
| `REPLAY_USER` | `VARCHAR2(4000)` |  | The user name to which captured user should be remapped during replay |