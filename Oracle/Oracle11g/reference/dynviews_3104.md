---
title: "V$TEMP_SPACE_HEADER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3104.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TEMP_SPACE_HEADER` displays aggregate information per file per LOCALLY MANAGED temporary tablespace regarding how much space is currently being used and how much is free as identified in the space header.

| Column | Datatype | Description |
| --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | Name of the temporary tablespace |
| `FILE_ID` | `NUMBER` | Absolute file number |
| `BYTES_USED` | `NUMBER` | How many bytes are in use |
| `BLOCKS_USED` | `NUMBER` | How many blocks are in use |
| `BYTES_FREE` | `NUMBER` | How many bytes are free |
| `BLOCKS_FREE` | `NUMBER` | How many blocks are free |
| `RELATIVE_FNO` | `NUMBER` | The relative file number for the file |