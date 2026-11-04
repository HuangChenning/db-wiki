---
title: DBA_HIST_SGASTAT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4041.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SGASTAT` displays detailed historical information on the system global area (SGA). This view contains snapshots of `V$SGASTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `NAME` | `VARCHAR2(64)` |  | SGA component group |
| `POOL` | `VARCHAR2(12)` |  | Designates the pool in which the memory in `NAME` resides: - `shared pool` - Memory is allocated from the shared pool - `large pool` - Memory is allocated from the large pool - `java pool` - Memory is allocated from the Java pool - `streams pool` - Memory is allocated from the Streams pool |
| `BYTES` | `NUMBER` |  | Memory size (in bytes) |