---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_STREAMS_POOL_ADVICE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_STREAMS_POOL_ADVICE` displays historical information about the estimated count of spilled or unspilled messages and the associated time spent in the spill or unspill activity for different Streams pool sizes.

This view is intended for use with Automatic Workload Repository (AWR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID of the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number of the snapshot |
| `SIZE_FOR_ESTIMATE` | `NUMBER` | `NOT NULL` | Pool size for the estimate (in megabytes) |
| `SIZE_FACTOR` | `NUMBER` |  | Size factor with respect to the current pool size |
| `ESTD_SPILL_COUNT` | `NUMBER` |  | Estimated count of messages spilled from the Streams pool |
| `ESTD_SPILL_TIME` | `NUMBER` |  | Estimated elapsed time (in seconds) to spill |
| `ESTD_UNSPILL_COUNT` | `NUMBER` |  | Estimated count of unspills (read back from disk) |
| `ESTD_UNSPILL_TIME` | `NUMBER` |  | Estimated elapsed time (in seconds) to unspill |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |