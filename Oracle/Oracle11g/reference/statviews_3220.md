---
title: DBA_HIST_DYN_REMASTER_STATS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3220.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_DYN_REMASTER_STATS` displays historical statistical information about the dynamic remastering process. All times are given in hundredths of a second, and total values reflect what has been collected since instance startup. This view contains snapshots of `V$DYNAMIC_REMASTER_STATS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `REMASTER_OPS` | `NUMBER` |  | Total number of dynamic remastering operations |
| `REMASTER_TIME` | `NUMBER` |  | Total dynamic remastering time |
| `REMASTERED_OBJECTS` | `NUMBER` |  | Total number of objects dynamically remastered due to affinity |
| `QUIESCE_TIME` | `NUMBER` |  | Total quiesce step time |
| `FREEZE_TIME` | `NUMBER` |  | Total freeze step time |
| `CLEANUP_TIME` | `NUMBER` |  | Total cleanup step time |
| `REPLAY_TIME` | `NUMBER` |  | Total replay step time |
| `FIXWRITE_TIME` | `NUMBER` |  | Total fixwrite step time |
| `SYNC_TIME` | `NUMBER` |  | Total synchronization step time |
| `RESOURCES_CLEANED` | `NUMBER` |  | Total number of resources cleaned in the cleanup steps |
| `REPLAYED_LOCKS_SENT` | `NUMBER` |  | Total number of locks replayed to other instances in the replay steps |
| `REPLAYED_LOCKS_RECEIVED` | `NUMBER` |  | Total number of locks received from other instances in the replay steps |
| `CURRENT_OBJECTS` | `NUMBER` |  | Current number of objects remastered on this instance due to affinity |