---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SEGMENTS_OLD.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.354 DBA\_SEGMENTS\_OLD

`DBA_SEGMENTS_OLD` lists information about storage allocated for all database segments.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Username of the segment owner |
| `SEGMENT_NAME` | `VARCHAR2(128)` |  | Name, if any, of the segment |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the partition |
| `SEGMENT_TYPE` | `VARCHAR2(18)` |  | Type of segment: `INDEX PARTITION, TABLE PARTITION, TABLE, CLUSTER, INDEX, ROLLBACK, DEFERRED ROLLBACK, TEMPORARY, CACHE, LOBSEGMENT` and `LOBINDEX` |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the segment |
| `HEADER_FILE` | `NUMBER` |  | ID of the file containing the segment header |
| `HEADER_BLOCK` | `NUMBER` |  | ID of the block containing the segment header |
| `BYTES` | `NUMBER` |  | Size, in bytes, of the segment |
| `BLOCKS` | `NUMBER` |  | Size, in Oracle blocks, of the segment |
| `EXTENTS` | `NUMBER` |  | Number of extents allocated to the segment |
| `INITIAL_EXTENT` | `NUMBER` |  | Size in bytes requested for the initial extent of the segment at create time. (Oracle rounds the extent size to multiples of 5 blocks if the requested size is greater than 5 blocks.) |
| `NEXT_EXTENT` | `NUMBER` |  | Size in bytes of the next extent to be allocated to the segment |
| `MIN_EXTENTS` | `NUMBER` |  | Minimum number of extents allowed in the segment |
| `MAX_EXTENTS` | `NUMBER` |  | Maximum number of extents allowed in the segment |
| `PCT_INCREASE` | `NUMBER` |  | Percent by which to increase the size of the next extent to be allocated |
| `FREELISTS` | `NUMBER` |  | Number of process freelists allocated to the segment |
| `FREELIST_GROUPS` | `NUMBER` |  | Number of freelist groups allocated to this segment |
| `RELATIVE_FNO` | `NUMBER` |  | Relative file number of the segment header |
| `BUFFER_POOL` | `VARCHAR2(7)` |  | Buffer pool for the object |