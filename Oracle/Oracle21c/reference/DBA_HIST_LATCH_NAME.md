---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_LATCH_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.4 DBA\_HIST\_LATCH\_NAME

`DBA_HIST_LATCH_NAME` displays information about decoded latch names for the latches shown in `DBA_HIST_LATCH`.

This view contains a snapshot of `V$LATCHNAME`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `LATCH_HASH` | `NUMBER` | `NOT NULL` | Latch hash |
| `LATCH_NAME` | `VARCHAR2(64)` | `NOT NULL` | Latch name |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [DBA\_HIST\_LATCH](DBA_HIST_LATCH.md) "
- " [V$LATCHNAME](V-LATCHNAME.md) "