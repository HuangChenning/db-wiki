---
title: "V$TEMPFILE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3105.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TEMPFILE` displays tempfile information.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Absolute file number |
| `CREATION_CHANGE#` | `NUMBER` | Creation System Change Number (SCN) |
| `CREATION_TIME` | `DATE` | Creation time |
| `TS#` | `NUMBER` | Tablespace number |
| `RFILE#` | `NUMBER` | Relative file number in the tablespace |
| `STATUS` | `VARCHAR2(7)` | Status of the file (`OFFLINE` \| `ONLINE`) |
| `ENABLED` | `VARCHAR2(10)` | Enabled for read and/or write |
| `BYTES` | `NUMBER` | Size of the file in bytes (from the file header) |
| `BLOCKS` | `NUMBER` | Size of the file in blocks (from the file header) |
| `CREATE_BYTES` | `NUMBER` | Creation size of the file (in bytes) |
| `BLOCK_SIZE` | `NUMBER` | Block size for the file |
| `NAME` | `VARCHAR2(513)` | Name of the file |