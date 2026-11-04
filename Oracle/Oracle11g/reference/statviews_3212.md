---
title: DBA_HIST_COMP_IOSTAT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3212.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_COMP_IOSTAT` displays information about I/O statistics aggregated on the component level.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `COMPONENT` | `VARCHAR2(64)` | `NOT NULL` | Component name |
| `FILE_TYPE` | `VARCHAR2(64)` | `NOT NULL` | File type |
| `IO_TYPE` | `CHAR(5)` | `NOT NULL` | The type of I/O performed |
| `OPERATION` | `CHAR(5)` | `NOT NULL` | Operation name |
| `BYTES` | `NUMBER` | `NOT NULL` | Number of bytes |
| `IO_COUNT` | `NUMBER` | `NOT NULL` | Number of I/Os that were performed |