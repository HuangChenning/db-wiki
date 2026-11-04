---
title: DBA_ROLLBACK_SEGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4221.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ROLLBACK_SEGS` describes rollback segments.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SEGMENT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rollback segment |
| `OWNER` | `VARCHAR2(6)` |  | Owner of the rollback segment: |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace containing the rollback segment |
| `SEGMENT_ID` | `NUMBER` | `NOT NULL` | ID number of the rollback segment |
| `FILE_ID` | `NUMBER` | `NOT NULL` | File identifier number of the file containing the segment head |
| `BLOCK_ID` | `NUMBER` | `NOT NULL` | ID number of the block containing the segment header |
| `INITIAL_EXTENT` | `NUMBER` |  | Initial extent size in bytes |
| `NEXT_EXTENT` | `NUMBER` |  | Secondary extent size in bytes |
| `MIN_EXTENTS` | `NUMBER` | `NOT NULL` | Minimum number of extents |
| `MAX_EXTENTS` | `NUMBER` | `NOT NULL` | Maximum number of extent |
| `PCT_INCREASE` | `NUMBER` |  | Percent increase for extent size |
| `STATUS` | `VARCHAR2(16)` |  | Rollback segment status: |
| `INSTANCE_NUM` | `VARCHAR2(40)` |  | Rollback segment owning Real Application Clusters instance number |
| `RELATIVE_FNO` | `NUMBER` | `NOT NULL` | Relative file number of the segment header |