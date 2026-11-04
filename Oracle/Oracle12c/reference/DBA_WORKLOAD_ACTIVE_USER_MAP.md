---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_WORKLOAD_ACTIVE_USER_MAP.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_WORKLOAD_ACTIVE_USER_MAP` contains the mappings that are going to be valid for the next replay or are valid for the current replay.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEDULE_CAP_ID` | `NUMBER` |  | The ID of a capture in the schedule |
| `CAPTURE_USER` | `VARCHAR2(4000)` | `NOT NULL` | The user name during the time of the workload capture |
| `REPLAY_USER` | `VARCHAR2(4000)` |  | The user name to which captured user should be remapped during replay |