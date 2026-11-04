---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_LMT_FREE_SPACE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_LMT_FREE_SPACE` describes the free extents in all locally managed tablespaces in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_ID` | `NUMBER` |  | Identifier number of the tablespace containing the extent |
| `FILE_ID` | `NUMBER` |  | File identifier number of the file containing the extent |
| `BLOCK_ID` | `NUMBER` |  | Starting block number of the extent |
| `BLOCKS` | `NUMBER` |  | Size of the extent (in Oracle blocks) |