---
title: DBA_HIST_MTTR_TARGET_ADVICE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4012.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_MTTR_TARGET_ADVICE` displays historical predictions of the number of physical I/O requests for the MTTR corresponding to each row. The data also includes a physical I/O factor, which is the ratio of the number of estimated I/O requests to the number of I/O requests actually performed by the current MTTR setting during the measurement interval. This view contains snapshots of `V$MTTR_TARGET_ADVICE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `MTTR_TARGET_FOR_ESTIMATE` | `NUMBER` |  | MTTR setting being simulated (equal to the current MTTR setting if this is the first row of the view) |
| `ADVICE_STATUS` | `VARCHAR2(5)` |  | Current status of MTTR simulation: - `ON SET` - `READY SET` - `OFF` |
| `DIRTY_LIMIT` | `NUMBER` |  | Dirty buffer limit derived from the MTTR being simulated |
| `ESTD_CACHE_WRITES` | `NUMBER` |  | Estimated number of cache physical writes under the MTTR |
| `ESTD_CACHE_WRITE_FACTOR` | `NUMBER` |  | Estimated cache physical write ratio under the MTTR. It is the ratio of the estimated number of cache writes to the number of cache writes under the current MTTR setting. |
| `ESTD_TOTAL_WRITES` | `NUMBER` |  | Estimated total number of physical writes under the MTTR |
| `ESTD_TOTAL_WRITE_FACTOR` | `NUMBER` |  | Estimated total physical write ratio under the MTTR. It is the ratio of the estimated total number of physical writes to the total number of physical writes under the current MTTR setting. |
| `ESTD_TOTAL_IOS` | `NUMBER` |  | Estimated total number of I/O requests under the MTTR |
| `ESTD_TOTAL_IO_FACTOR` | `NUMBER` |  | Estimated total I/O ratio under the MTTR. It is the ratio of the estimated total number of I/O requests to the total number of I/O requests under the current MTTR setting. |