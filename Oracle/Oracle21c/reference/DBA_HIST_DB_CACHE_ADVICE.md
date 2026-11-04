---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_DB_CACHE_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.397 DBA\_HIST\_DB\_CACHE\_ADVICE

`DBA_HIST_DB_CACHE_ADVICE` displays historical predictions of the number of physical reads for the cache size corresponding to each row.

This view contains snapshots of `V$DB_CACHE_ADVICE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `BPID` | `NUMBER` | `NOT NULL` | Buffer Pool identifier (ranges from 1 to 8) |
| `BUFFERS_FOR_ESTIMATE` | `NUMBER` | `NOT NULL` | Cache size for prediction (in terms of buffers) |
| `NAME` | `VARCHAR2(20)` |  | Buffer pool name |
| `BLOCK_SIZE` | `NUMBER` |  | Block size in bytes for buffers in the pool (the standard block size, the power of 2 nonstandard block sizes, 2048, 4096, 8192, 16384, or 32768) |
| `ADVICE_STATUS` | `VARCHAR2(3)` |  | Status of the advisory:  - `ON` - Currently running - `OFF` - Disabled (the estimates are historical and calculated when last enabled) |
| `SIZE_FOR_ESTIMATE` | `NUMBER` |  | Cache size for prediction (in megabytes) |
| `SIZE_FACTOR` | `NUMBER` |  | Size factor with respect to the current cache size |
| `PHYSICAL_READS` | `NUMBER` |  | Physical reads for the cache size |
| `BASE_PHYSICAL_READS` | `NUMBER` |  | Base physical reads for the cache size |
| `ACTUAL_PHYSICAL_READS` | `NUMBER` |  | Actual physical reads for the cache size |
| `ESTD_PHYSICAL_READ_TIME` | `NUMBER` |  | Estimated physical read time for the cache size |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$DB\_CACHE\_ADVICE](V-DB_CACHE_ADVICE.md) "