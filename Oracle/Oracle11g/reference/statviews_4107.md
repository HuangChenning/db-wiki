---
title: DBA_LMT_USED_EXTENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4107.htm
tags:
  - oracle
  - 11g
  - reference
---

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