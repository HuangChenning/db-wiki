---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LMT_USED_EXTENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.145 DBA\_LMT\_USED\_EXTENTS

`DBA_LMT_USED_EXTENTS` describes the extents comprising the segments in all locally managed tablespaces in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SEGMENT_FILEID` | `NUMBER` |  | File number of the segment header of the extent |
| `SEGMENT_BLOCK` | `NUMBER` |  | Block number of the segment header of the extent |
| `TABLESPACE_ID` | `NUMBER` |  | Identifier number of the tablespace containing the extent |
| `EXTENT_ID` | `NUMBER` |  | Extent number in the segment |
| `FILEID` | `NUMBER` |  | File identifier number of the file containing the extent |
| `BLOCK` | `NUMBER` |  | Starting block number of the extent |
| `LENGTH` | `NUMBER` |  | Number of blocks in the extent |