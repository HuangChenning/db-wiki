---
title: DBA_FREE_SPACE_COALESCED
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3195.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_FREE_SPACE_COALESCED` describes statistics on coalesced space in all tablespaces in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace |
| `TOTAL_EXTENTS` | `NUMBER` |  | Total number of free extents in the tablespace |
| `EXTENTS_COALESCED` | `NUMBER` |  | Total number of coalesced free extents in the tablespace |
| `PERCENT_EXTENTS   _COALESCED` | `NUMBER` |  | Percentage of coalesced free extents in the tablespace |
| `TOTAL_BYTES` | `NUMBER` |  | Total number of free bytes in the tablespace |
| `BYTES_COALESCED` | `NUMBER` |  | Total number of coalesced free bytes in the tablespace |
| `TOTAL_BLOCKS` | `NUMBER` |  | Total number of free Oracle blocks in the tablespace |
| `BLOCKS_COALESCED` | `NUMBER` |  | Total number of coalesced free Oracle blocks in the tablespace |
| `PERCENT_BLOCKS   _COALESCED` | `NUMBER` |  | Percentage of coalesced free Oracle blocks in the tablespace |