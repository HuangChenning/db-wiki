---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_PGA_TARGET_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.24 DBA\_HIST\_PGA\_TARGET\_ADVICE

`DBA_HIST_PGA_TARGET_ADVICE` displays historical predictions of how the cache hit percentage and over allocation count statistics displayed by the `V$PGASTAT` performance view would be impacted if the value of the `PGA_AGGREGATE_TARGET` parameter is changed.

This view contains snapshots of `V$PGA_TARGET_ADVICE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `PGA_TARGET_FOR_ESTIMATE` | `NUMBER` | `NOT NULL` | Value of `PGA_AGGREGATE_TARGET` for the prediction (in bytes) |
| `PGA_TARGET_FACTOR` | `NUMBER` |  | `PGA_TARGET_FOR_ESTIMATE` / the current value of the `PGA_AGGREGATE_TARGET` parameter |
| `ADVICE_STATUS` | `VARCHAR2(3)` |  | Indicates whether the advice is enabled (`ON`) or disabled (`OFF`) depending on the value of the `STATISTICS_LEVEL` parameter |
| `BYTES_PROCESSED` | `NUMBER` |  | Total bytes processed by all the work areas considered by this advice (in bytes) |
| `ESTD_TIME` | `NUMBER` |  | Time (in seconds) required to process the bytes |
| `ESTD_EXTRA_BYTES_RW` | `NUMBER` |  | Estimated number of extra bytes which would be read or written if `PGA_AGGREGATE_TARGET` was set to the value of the `PGA_TARGET_FOR_ESTIMATE` column. This number is derived from the estimated number and size of work areas which would run in one-pass (or multi-pass) for that value of `PGA_AGGREGATE_TARGET`. |
| `ESTD_PGA_CACHE_HIT_PERCENTAGE` | `NUMBER` |  | Estimated value of the cache hit percentage statistic when `PGA_AGGREGATE_TARGET` equals `PGA_TARGET_FOR_ESTIMATE`. This column is derived from the above two columns and is equal to `BYTES_PROCESSED` / (`BYTES_PROCESSED` + `ESTD_EXTRA_BYTES_RW`) |
| `ESTD_OVERALLOC_COUNT` | `NUMBER` |  | Estimated number of PGA memory over-allocations if the value of `PGA_AGGREGATE_TARGET` is set to `PGA_TARGET_FOR_ESTIMATE`. A nonzero value means that `PGA_TARGET_FOR_ESTIMATE` is not large enough to run the work area workload. Hence, `PGA_AGGREGATE_TARGET` should not be set to `PGA_TARGET_FOR_ESTIMATE` since Oracle will not be able to honor that target. |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |