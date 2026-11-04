---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SGA_TARGET_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.53 DBA\_HIST\_SGA\_TARGET\_ADVICE

`DBA_HIST_SGA_TARGET_ADVICE` provides historical information about the `SGA_TARGET` initialization parameter.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `SGA_SIZE` | `NUMBER` | `NOT NULL` | Size of the SGA |
| `SGA_SIZE_FACTOR` | `NUMBER` | `NOT NULL` | Ratio between the `SGA_SIZE` and the current size of the SGA |
| `ESTD_DB_TIME` | `NUMBER` | `NOT NULL` | Estimated DB\_TIME for this SGA\_SIZE |
| `ESTD_PHYSICAL_READS` | `NUMBER` |  | Estimated number of physical reads |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [SGA\_TARGET](SGA_TARGET.md) "