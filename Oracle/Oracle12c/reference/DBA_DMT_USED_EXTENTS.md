---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_DMT_USED_EXTENTS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_DMT_USED_EXTENTS` describes the extents comprising the segments in all dictionary managed tablespaces in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SEGMENT_FILEID` | `NUMBER` | `NOT NULL` | File number of the segment header of the extent |
| `SEGMENT_BLOCK` | `NUMBER` | `NOT NULL` | Block number of the segment header of the extent |
| `TABLESPACE_ID` | `NUMBER` | `NOT NULL` | Identifier number of the tablespace containing the extent |
| `EXTENT_ID` | `NUMBER` | `NOT NULL` | Extent number in the segment |
| `FILEID` | `NUMBER` | `NOT NULL` | File identifier number of the file containing the extent |
| `BLOCK` | `NUMBER` | `NOT NULL` | Starting block number of the extent |
| `LENGTH` | `NUMBER` | `NOT NULL` | Number of blocks in the extent |