---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_IOSTAT_FUNCTION_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.417 DBA\_HIST\_IOSTAT\_FUNCTION\_NAME

`DBA_HIST_IOSTAT_FUNCTION_NAME` displays historical I/O statistics by function names.

This view contains snapshots of `V$IOSTAT_FUNCTION`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `FUNCTION_ID` | `NUMBER` | `NOT NULL` | Function ID |
| `FUNCTION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Function name |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$IOSTAT\_FUNCTION](V-IOSTAT_FUNCTION.md) "