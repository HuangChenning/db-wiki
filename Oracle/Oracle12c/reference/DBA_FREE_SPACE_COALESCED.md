---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_FREE_SPACE_COALESCED.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_FREE_SPACE_COALESCED` describes statistics on coalesced space in all tablespaces in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace |
| `TOTAL_EXTENTS` | `NUMBER` |  | Total number of free extents in the tablespace |
| `EXTENTS_COALESCED` | `NUMBER` |  | Total number of coalesced free extents in the tablespace |
| `PERCENT_EXTENTS _COALESCED` | `NUMBER` |  | Percentage of coalesced free extents in the tablespace |
| `TOTAL_BYTES` | `NUMBER` |  | Total number of free bytes in the tablespace |
| `BYTES_COALESCED` | `NUMBER` |  | Total number of coalesced free bytes in the tablespace |
| `TOTAL_BLOCKS` | `NUMBER` |  | Total number of free Oracle blocks in the tablespace |
| `BLOCKS_COALESCED` | `NUMBER` |  | Total number of coalesced free Oracle blocks in the tablespace |
| `PERCENT_BLOCKS _COALESCED` | `NUMBER` |  | Percentage of coalesced free Oracle blocks in the tablespace |