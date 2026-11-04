---
title: DBA_HIST_SGA
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4039.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SGA` displays historical summary information about the system global area (SGA). This view contains snapshots of `V$SGA`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `NAME` | `VARCHAR2(64)` | `NOT NULL` | SGA component group |
| `VALUE` | `NUMBER` | `NOT NULL` | Memory size (in bytes) |