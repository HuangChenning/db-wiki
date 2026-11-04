---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_PGASTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.25 DBA\_HIST\_PGASTAT

`DBA_HIST_PGASTAT` displays historical PGA memory usage statistics as well as statistics about the automatic PGA memory manager when it is enabled.

This view contains snapshots of `V$PGASTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Database instance number |
| `NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the statistic:  - `aggregate PGA auto target` - `aggregate PGA target parameter` - `bytes processed` - `cache hit percentage` - `extra bytes read/written` - `global memory bound` - `max processes count` - `maximum PGA allocated` - `maximum PGA used for auto workareas` - `maximum PGA used for manual workareas` - `over allocation count` - `PGA memory freed back to OS` - `process count` - `recompute count (total)` - `total freeable PGA memory` - `total PGA allocated` - `total PGA inuse` - `total PGA used for auto workareas` - `total PGA used for manual workareas`  See Also: `V$PGASTAT` for descriptions of the statistics |
| `VALUE` | `NUMBER` |  | Statistic value |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$PGASTAT](V-PGASTAT.md) "