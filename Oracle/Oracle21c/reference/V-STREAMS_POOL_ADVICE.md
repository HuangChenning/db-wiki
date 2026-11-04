---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-STREAMS_POOL_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.88 V$STREAMS\_POOL\_ADVICE

`V$STREAMS_POOL_ADVICE` displays information about the estimated count of spilled or unspilled messages and the associated time spent in the spill or unspill activity for different Streams pool sizes. The sizes range from 10% to 200% of the current Streams pool size, in equal intervals. The value of the interval depends on the current size of the Streams pool.

| Column | Datatype | Description |
| --- | --- | --- |
| `STREAMS_POOL_SIZE_FOR_ESTIMATE` | `NUMBER` | Streams pool size (in megabytes) for the estimate. The size ranges from values smaller than the current Streams pool size to values larger than the current Streams pool size, and there is a separate row for each increment. There is always an entry that shows the current Streams pool size, and there are always 20 increments. The range and the size of the increments depend on the current size of the Streams pool. |
| `STREAMS_POOL_SIZE_FACTOR` | `NUMBER` | Size factor with respect to the current Streams pool size |
| `ESTD_SPILL_COUNT` | `NUMBER` | Estimated count of messages spilled from the Streams pool |
| `ESTD_SPILL_TIME` | `NUMBER` | Estimated elapsed time (in seconds) to spill |
| `ESTD_UNSPILL_COUNT` | `NUMBER` | Estimated count of unspills (read back from disk) |
| `ESTD_UNSPILL_TIME` | `NUMBER` | Estimated elapsed time (in seconds) to unspill |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |