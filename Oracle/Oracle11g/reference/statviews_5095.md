---
title: DBA_WORKLOAD_REPLAY_SCHEDULES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5095.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_WORKLOAD_REPLAY_SCHEDULES` displays the names of replay schedules for the current replay directory. A replay schedule defines one or multiple workload captures, and the order to start their replays. The current replay directory is set by `DBMS_WORKLOAD_REPLAY.SET_REPLAY_DIRECTORY('replay_dir')`. Each row in the view contains information about one replay schedule.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEDULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | The name of a schedule to be replayed. It defines one or multiple workload captures, and the order to start their replays. |
| `DIRECTORY` | `VARCHAR2(128)` | `NOT NULL` | Directory object name for the replay schedule name |
| `STATUS` | `VARCHAR2(128)` |  | `NEW` if the schedule is being created, `CURRENT` if the schedule is currently being used by a replay, otherwise `NULL` |

Note:

This view is available starting with Oracle Database 11g Release 2 (11.2.0.4).

See Also:

- ["DBA\_WORKLOAD\_SCHEDULE\_CAPTURES"](statviews_5097.md) displays the workload captures in a replay schedule.
- ["DBA\_WORKLOAD\_SCHEDULE\_ORDERING"](statviews_5098.md) displays the order to start captures in a replay schedule.
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_workload_replay.htm#ARPLS208) for more information about the `DBMS_WORKLOAD_REPLAY` package