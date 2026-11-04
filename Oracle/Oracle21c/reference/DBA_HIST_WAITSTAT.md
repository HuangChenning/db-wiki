---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_WAITSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.85 DBA\_HIST\_WAITSTAT

`DBA_HIST_WAITSTAT` displays historical block contention statistics. This view contains snapshots of `V$WAITSTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `CLASS` | `VARCHAR2(18)` | `NOT NULL` | Class of the block |
| `WAIT_COUNT` | `NUMBER` |  | Number of waits by the OPERATION for this CLASS of block |
| `TIME` | `NUMBER` |  | Sum of all wait times for all the waits by the OPERATION for this CLASS of block |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$WAITSTAT](V-WAITSTAT.md) "