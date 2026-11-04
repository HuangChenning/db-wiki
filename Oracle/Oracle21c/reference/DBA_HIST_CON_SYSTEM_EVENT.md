---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_CON_SYSTEM_EVENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.392 DBA\_HIST\_CON\_SYSTEM\_EVENT

`DBA_HIST_CON_SYSTEM_EVENT` displays historical information on total waits for an event in a container. This view contains snapshots of `V$CON_SYSTEM_EVENT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `EVENT_ID` | `NUMBER` | `NOT NULL` | Identifier of the wait event |
| `EVENT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the wait event |
| `WAIT_CLASS_ID` | `NUMBER` |  | Identifier of the Class of the Wait Event |
| `WAIT_CLASS` | `VARCHAR2(64)` |  | Name of the Class of the Wait Event |
| `TOTAL_WAITS` | `NUMBER` |  | Total number of waits for the event |
| `TOTAL_TIMEOUTS` | `NUMBER` |  | Total number of timeouts for the event |
| `TIME_WAITED_MICRO` | `NUMBER` |  | Total amount of time waited for the event (in microseconds) |
| `TOTAL_WAITS_FG` | `NUMBER` |  | Total number of waits for the event, from foreground sessions |
| `TOTAL_TIMEOUTS_FG` | `NUMBER` |  | Total number of timeouts for the event, from foreground sessions |
| `TIME_WAITED_MICRO_FG` | `NUMBER` |  | Amount of time waited for the event (in microseconds), from foreground sessions |
| `CON_DBID` | `NUMBER` | `NOT NULL` | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$CON\_SYSTEM\_EVENT](V-CON_SYSTEM_EVENT.md) "