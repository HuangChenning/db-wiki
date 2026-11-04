---
title: DBA_HIST_TBSPC_SPACE_USAGE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4064.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_TBSPC_SPACE_USAGE` displays historical tablespace usage statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `TABLESPACE_ID` | `NUMBER` |  | Tablespace ID |
| `TABLESPACE_SIZE` | `NUMBER` |  | Tablespace size (in database blocks) |
| `TABLESPACE_MAXSIZE` | `NUMBER` |  | Maximum size of the tablespace (in database blocks) |
| `TABLESPACE_USEDSIZE` | `NUMBER` |  | Used size of the tablespace (in database blocks) |
| `RTIME` | `VARCHAR2(25)` |  | Runtime |