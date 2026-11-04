---
title: DBA_HIST_STREAMS_POOL_ADVICE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4057.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_STREAMS_POOL_ADVICE` displays historical information about the estimated count of spilled or unspilled messages and the associated time spent in the spill or unspill activity for different Streams pool sizes. This view is intended for use with Automatic Workload Repository (AWR).

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