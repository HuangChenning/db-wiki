---
title: "V$MAP_FILE_EXTENT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2055.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MAP_FILE_EXTENT` displays a list of all file extent mapping structures in the shared memory of the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_MAP_IDX` | `NUMBER` | File index (corresponds to `FILE_MAP_IDX` in `V$MAP_FILE`) |
| `EXT_NUM` | `NUMBER` | File extent number |
| `EXT_ELEM_OFF` | `NUMBER` | Element offset in HKB |
| `EXT_SIZE` | `NUMBER` | File extent size in HKB |
| `EXT_FILE_OFF` | `NUMBER` | File Offset in HKB |
| `EXT_TYPE` | `VARCHAR2(6)` | File Extent Type: |
| `ELEM_IDX` | `NUMBER` | Index in `V$MAP_ELEMENT` corresponding to the element where the file extent resides |