---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_DYN_REMASTER_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.400 DBA\_HIST\_DYN\_REMASTER\_STATS

`DBA_HIST_DYN_REMASTER_STATS` displays historical statistical information about the dynamic remastering process.

All times are given in hundredths of a second, and total values reflect what has been collected since instance startup. This view contains snapshots of `V$DYNAMIC_REMASTER_STATS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `REMASTER_TYPE` | `VARCHAR2(11)` | `NOT NULL` | Remaster process type. Possible values:  - `AFFINITY`: This value is used for the row containing statistics that pertain to dynamic remastering activity on object affinity. - `READ-MOSTLY`: This value is used for the row containing statistics that pertain to dynamic remastering activity on read-mostly objects. |
| `PERSISTENT_OBJECTS` | `NUMBER` |  | Current number of objects that are marked persistent read-mostly in the cluster |
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
| `CURRENT_OBJECTS` | `NUMBER` |  | Current number of objects remastered on this instance due to affinity or the current number of objects that are marked read-mostly in the cluster |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$DYNAMIC\_REMASTER\_STATS](V-DYNAMIC_REMASTER_STATS.md) "