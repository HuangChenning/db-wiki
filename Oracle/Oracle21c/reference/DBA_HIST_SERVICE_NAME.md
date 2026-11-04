---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SERVICE_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.46 DBA\_HIST\_SERVICE\_NAME

`DBA_HIST_SERVICE_NAME` displays the names of the Services tracked by the Workload Repository.

This view contains information for `V$SERVICES`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `SERVICE_NAME_HASH` | `NUMBER` | `NOT NULL` | Hash of the service name |
| `SERVICE_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the service |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SERVICES](V-SERVICES.md) "