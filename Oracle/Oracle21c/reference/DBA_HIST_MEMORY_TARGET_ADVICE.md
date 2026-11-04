---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_MEMORY_TARGET_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.10 DBA\_HIST\_MEMORY\_TARGET\_ADVICE

This view contains snapshots of `V$MEMORY_TARGET_ADVICE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `MEMORY_SIZE` | `NUMBER` | `NOT NULL` | If the `MEMORY_SIZE_FACTOR` column has a value of 1, then this column shows the current size of memory, as set by the `MEMORY_TARGET` initialization parameter.  If the value of the `MEMORY_SIZE_FACTOR` column is less than or greater than 1, then this column shows a proposed memory size. |
| `MEMORY_SIZE_FACTOR` | `NUMBER` |  | A multiplier for the current memory size. Possible values are 0.25, 0.5, 0.75, 1, 1.5, 1.75 and 2. This multiplier times the current memory size equals the value of the `MEMORY_SIZE` column. |
| `ESTD_DB_TIME` | `NUMBER` |  | For current memory size (`MEMORY_SIZE_FACTOR = 1`), the amount of database time required to complete the current workload. For a proposed memory size, the estimated amount of database time that would be required if the `MEMORY_TARGET` parameter were changed to the proposed size. |
| `ESTD_DB_TIME_FACTOR` | `NUMBER` |  | For a proposed memory size, ratio of estimated database time to current database time |
| `VERSION` | `NUMBER` |  | Version number of this recommendation |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$MEMORY\_TARGET\_ADVICE](V-MEMORY_TARGET_ADVICE.md) "