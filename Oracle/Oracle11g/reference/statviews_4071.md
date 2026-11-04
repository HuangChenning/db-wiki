---
title: DBA_HIST_WAITSTAT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4071.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_WAITSTAT` displays historical block contention statistics. This view contains snapshots of `V$WAITSTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `CLASS` | `VARCHAR2(18)` |  | Class of the block |
| `WAIT_COUNT` | `NUMBER` |  | Number of waits by the OPERATION for this CLASS of block |
| `TIME` | `NUMBER` |  | Sum of all wait times for all the waits by the OPERATION for this CLASS of block |