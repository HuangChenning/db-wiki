---
title: "V$STREAMS_POOL_STATISTICS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3083.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$STREAMS_POOL_STATISTICS` displays information about the current Streams pool usage percentage.

| Column | Datatype | Description |
| --- | --- | --- |
| `TOTAL_MEMORY_ALLOCATED` | `NUMBER` | Total memory allocated to the Streams pool (in bytes). It should always be less than the current size of the Streams pool. You can get the percentage of the Streams pool used by dividing `TOTAL_MEMORY_ALLOCATED` by `CURRENT_SIZE`. |
| `CURRENT_SIZE` | `NUMBER` | Current size of the Streams pool (in bytes) |
| `SGA_TARGET_VALUE` | `NUMBER` | Value of `SGA_TARGET`. Used to determine whether or not streams pool automatic tuning is enabled. This should be set even if `MEMORY_TARGET` is set and `SGA_TARGET` is not set. |
| `SHRINK_PHASE` | `NUMBER` | This only pertains to the Streams pool in an automatic tuning environment (`SGA_TARGET` and `MEMORY_TARGET` set). In this case, this shows whether or not the Streams pool is being asked to shrink. During the shrink phase, enqueues are blocked, flow control is enabled for all components, and cached memory is returned to the SGA. |
| `ADVICE_DISABLED` | `NUMBER` | This determines whether or not Streams pool advice in `V$STREAMS_POOL_ADVICE` as well as all statistics gathering related to auto-tuning the Streams pool have been disabled. |