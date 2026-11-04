---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SGASTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.54 DBA\_HIST\_SGASTAT

`DBA_HIST_SGASTAT` displays detailed historical information on the system global area (SGA).

This view contains snapshots of `V$SGASTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `NAME` | `VARCHAR2(64)` |  | SGA component group |
| `POOL` | `VARCHAR2(30)` |  | Designates the pool in which the memory in `NAME` resides:  - `in-memory pool` - Memory is allocated from the In-Memory pool - `java pool` - Memory is allocated from the Java pool - `large pool` - Memory is allocated from the large pool - `numa pool` - Memory is allocated from the NUMA pool - `shared pool` - Memory is allocated from the shared pool - `streams pool` - Memory is allocated from the Streams pool |
| `BYTES` | `NUMBER` |  | Memory size (in bytes) |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SGASTAT](V-SGASTAT.md) "