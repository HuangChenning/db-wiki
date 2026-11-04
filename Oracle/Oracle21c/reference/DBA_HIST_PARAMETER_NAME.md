---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_PARAMETER_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.18 DBA\_HIST\_PARAMETER\_NAME

`DBA_HIST_PARAMETER_NAME` displays information about the parameter names captured in the workload repository.

This view is used with the `DBA_HIST_PARAMETER` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `PARAMETER_HASH` | `NUMBER` | `NOT NULL` | Parameter hash |
| `PARAMETER_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the parameter |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [DBA\_HIST\_PARAMETER](DBA_HIST_PARAMETER.md) "