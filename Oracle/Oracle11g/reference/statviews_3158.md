---
title: DBA_DMT_FREE_SPACE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3158.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_DMT_FREE_SPACE` describes the free extents in all dictionary managed tablespaces in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_ID` | `NUMBER` | `NOT NULL` | Identifier number of the tablespace containing the extent |
| `FILE_ID` | `NUMBER` | `NOT NULL` | File identifier number of the file containing the extent |
| `BLOCK_ID` | `NUMBER` | `NOT NULL` | Starting block number of the extent |
| `BLOCKS` | `NUMBER` | `NOT NULL` | Size of the extent (in Oracle blocks) |