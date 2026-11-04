---
title: "V$STREAMS_POOL_ADVICE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3082.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$STREAMS_POOL_ADVICE` displays information about the estimated count of spilled or unspilled messages and the associated time spent in the spill or unspill activity for different Streams pool sizes. The sizes range from 10% to 200% of the current Streams pool size, in equal intervals. The value of the interval depends on the current size of the Streams pool.

| Column | Datatype | Description |
| --- | --- | --- |
| `STREAMS_POOL_SIZE_FOR_ESTIMATE` | `NUMBER` | Streams pool size (in megabytes) for the estimate. The size ranges from values smaller than the current Streams pool size to values larger than the current Streams pool size, and there is a separate row for each increment. There is always an entry that shows the current Streams pool size, and there are always 20 increments. The range and the size of the increments depend on the current size of the Streams pool. |
| `STREAMS_POOL_SIZE_FACTOR` | `NUMBER` | Size factor with respect to the current Streams pool size |
| `ESTD_SPILL_COUNT` | `NUMBER` | Estimated count of messages spilled from the Streams pool |
| `ESTD_SPILL_TIME` | `NUMBER` | Estimated elapsed time (in seconds) to spill |
| `ESTD_UNSPILL_COUNT` | `NUMBER` | Estimated count of unspills (read back from disk) |
| `ESTD_UNSPILL_TIME` | `NUMBER` | Estimated elapsed time (in seconds) to unspill |

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_otmon.htm#STRMS147) for more information about this view