---
title: DBA_HIST_TABLESPACE_STAT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4063.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_TABLESPACE_STAT` displays tablespace information from the control file. This view contains snapshots of `V$TABLESPACE` and `DBA_TABLESPACE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `TS#` | `NUMBER` |  | Tablespace number |
| `TSNAME` | `VARCHAR2(30)` |  | Tablespace name |
| `CONTENTS` | `VARCHAR2(9)` |  | Tablespace contents: |
| `STATUS` | `VARCHAR2(9)` |  | Tablespace status: |
| `SEGMENT_SPACE_MANAGEMENT` | `VARCHAR2(6)` |  | Indicates whether the free and used segment space in the tablespace is managed using free lists (`MANUAL`) or bitmaps (`AUTO`) |
| `EXTENT_MANAGEMENT` | `VARCHAR2(10)` |  | Indicates whether the extents in the tablespace are dictionary managed (`DICTIONARY`) or locally managed (`LOCAL`) |
| `IS_BACKUP` | `VARCHAR2(5)` |  | Indicates whether the tablespace is part of a backup |