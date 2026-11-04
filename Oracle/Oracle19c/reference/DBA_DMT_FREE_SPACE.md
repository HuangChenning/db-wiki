---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_DMT_FREE_SPACE.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.268 DBA\_DMT\_FREE\_SPACE

`DBA_DMT_FREE_SPACE` describes the free extents in all dictionary managed tablespaces in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_ID` | `NUMBER` | `NOT NULL` | Identifier number of the tablespace containing the extent |
| `FILE_ID` | `NUMBER` | `NOT NULL` | File identifier number of the file containing the extent |
| `BLOCK_ID` | `NUMBER` | `NOT NULL` | Starting block number of the extent |
| `BLOCKS` | `NUMBER` | `NOT NULL` | Size of the extent (in Oracle blocks) |