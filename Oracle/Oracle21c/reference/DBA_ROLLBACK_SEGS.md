---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ROLLBACK_SEGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.295 DBA\_ROLLBACK\_SEGS

`DBA_ROLLBACK_SEGS` describes rollback segments.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SEGMENT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rollback segment |
| `OWNER ` | `VARCHAR2(6)` |  | Owner of the rollback segment:  - `PUBLIC` - `SYS` |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace containing the rollback segment |
| `SEGMENT_ID ` | `NUMBER` | `NOT NULL` | ID number of the rollback segment |
| `FILE_ID` | `NUMBER` | `NOT NULL` | Absolute file number of the data file containing the segment header |
| `BLOCK_ID` | `NUMBER` | `NOT NULL` | ID number of the block containing the segment header |
| `INITIAL_EXTENT` | `NUMBER` |  | Initial extent size in bytes |
| `NEXT_EXTENT` | `NUMBER` |  | Secondary extent size in bytes |
| `MIN_EXTENTS` | `NUMBER` | `NOT NULL` | Minimum number of extents |
| `MAX_EXTENTS` | `NUMBER` | `NOT NULL` | Maximum number of extent |
| `PCT_INCREASE` | `NUMBER` |  | Percent increase for extent size |
| `STATUS ` | `VARCHAR2(16)` |  | Rollback segment status:  - `OFFLINE` - `ONLINE` - `NEEDS RECOVERY` - `PARTLY AVAILABLE` - `UNDEFINED` |
| `INSTANCE_NUM` | `VARCHAR2(40)` |  | Rollback segment owning Oracle Real Application Clusters instance number |
| `RELATIVE_FNO` | `NUMBER` | `NOT NULL` | Relative file number of the segment header |