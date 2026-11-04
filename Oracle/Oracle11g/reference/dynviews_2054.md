---
title: "V$MAP_FILE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2054.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MAP_FILE` displays a list of all file mapping structures in the shared memory of the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_MAP_IDX` | `NUMBER` | Index corresponding to the file |
| `FILE_CFGID` | `VARCHAR2(256)` | Configuration ID (N/A if configuration ID is not supported) |
| `FILE_STATUS` | `VARCHAR2(7)` | Status of the mapping information: |
| `FILE_NAME` | `VARCHAR2(256)` | Absolute file name |
| `FILE_TYPE` | `VARCHAR2(11)` | File type: |
| `FILE_STRUCTURE` | `VARCHAR2(9)` | File structure: |
| `FILE_SIZE` | `NUMBER` | File size in HKB (half KB) |
| `FILE_NEXTS` | `NUMBER` | Number of file extents in the file (not necessarily the same as the number of file extents mapped) |
| `LIB_IDX` | `NUMBER` | Index of mapping library claiming ownership of the file |