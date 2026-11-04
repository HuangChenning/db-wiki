---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LMT_FREE_SPACE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.144 DBA\_LMT\_FREE\_SPACE

`DBA_LMT_FREE_SPACE` describes the free extents in all locally managed tablespaces in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_ID` | `NUMBER` |  | Identifier number of the tablespace containing the extent |
| `FILE_ID` | `NUMBER` |  | File identifier number of the file containing the extent |
| `BLOCK_ID` | `NUMBER` |  | Starting block number of the extent |
| `BLOCKS` | `NUMBER` |  | Size of the extent (in Oracle blocks) |