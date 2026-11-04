---
title: "V$TEMP_EXTENT_POOL"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3103.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TEMP_EXTENT_POOL` displays the state of temporary space cached and used for the instance. Note that loading of the temporary space cache is lazy and that instances can be dormant.

| Column | Datatype | Description |
| --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | Name of the tablespace |
| `FILE_ID` | `NUMBER` | Absolute file number |
| `EXTENTS_CACHED` | `NUMBER` | Number of extents that have been cached |
| `EXTENTS_USED` | `NUMBER` | Number of extents that are actually being used |
| `BLOCKS_CACHED` | `NUMBER` | Number of blocks that are cached |
| `BLOCKS_USED` | `NUMBER` | Number of blocks that are used |
| `BYTES_CACHED` | `NUMBER` | Number of bytes that are cached |
| `BYTES_USED` | `NUMBER` | Number of bytes that are used |
| `RELATIVE_FNO` | `NUMBER` | Relative file number |