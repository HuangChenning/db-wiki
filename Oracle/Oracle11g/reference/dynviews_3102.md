---
title: "V$TEMP_EXTENT_MAP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3102.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TEMP_EXTENT_MAP` displays the status of each unit for all LOCALLY MANAGED temporary tablespaces.

| Column | Datatype | Description |
| --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | Name of the tablespace this unit belongs to |
| `FILE_ID` | `NUMBER` | Absolute file number |
| `BLOCK_ID` | `NUMBER` | Begin block number for this unit |
| `BYTES` | `NUMBER` | Bytes in the extent |
| `BLOCKS` | `NUMBER` | Blocks in the extent |
| `OWNER` | `NUMBER` | Instance which owns this unit |
| `RELATIVE_FNO` | `NUMBER` | Relative file number |