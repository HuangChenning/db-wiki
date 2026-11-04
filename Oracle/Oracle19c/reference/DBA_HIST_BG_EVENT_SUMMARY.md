---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_HIST_BG_EVENT_SUMMARY.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.353 DBA\_HIST\_BG\_EVENT\_SUMMARY

`DBA_HIST_BG_EVENT_SUMMARY` displays the historical summary background event activity.

This view contains snapshots from `V$SESSION_EVENT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `EVENT_ID` | `NUMBER` | `NOT NULL` | Identifier of the wait event |
| `EVENT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the wait event |
| `WAIT_CLASS_ID` | `NUMBER` |  | Identifier of the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` |  | Name of the class of the wait event |
| `TOTAL_WAITS` | `NUMBER` |  | Total number of waits for the event |
| `TOTAL_TIMEOUTS` | `NUMBER` |  | Total number of timeouts for the event |
| `TIME_WAITED_MICRO` | `NUMBER` |  | Total amount of time waited for the event (in microseconds) |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SESSION\_EVENT](V-SESSION_EVENT.md) "