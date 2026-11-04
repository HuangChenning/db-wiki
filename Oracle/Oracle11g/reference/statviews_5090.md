---
title: DBA_WORKLOAD_ACTIVE_USER_MAP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5090.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_WORKLOAD_ACTIVE_USER_MAP` contains the mappings that are going to be valid for the next replay or are valid for the current replay.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEDULE_CAP_ID` | `NUMBER` |  | The ID of a capture in the schedule |
| `CAPTURE_USER` | `VARCHAR2(4000)` | `NOT NULL` | The user name during the time of the workload capture |
| `REPLAY_USER` | `VARCHAR2(4000)` |  | The user name to which captured user should be remapped during replay |

Note:

This view is available starting with Oracle Database 11g Release 2 (11.2.0.4).