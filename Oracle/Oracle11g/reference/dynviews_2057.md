---
title: "V$MAP_LIBRARY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2057.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MAP_LIBRARY` displays a list of all mapping libraries dynamically loaded by the external process.

| Column | Datatype | Description |
| --- | --- | --- |
| `LIB_IDX` | `NUMBER` | Index corresponding to the library |
| `LIB_NAME` | `VARCHAR2(256)` | Absolute library name |
| `VENDOR_NAME` | `VARCHAR2(64)` | Name of the vendor implementing the library |
| `PROTOCOL_NUM` | `NUMBER` | Mapping protocol that the library supports |
| `VERSION_NUM` | `VARCHAR2(32)` | Version number |
| `PATH_NAME` | `VARCHAR2(4000)` | Path name |
| `MAP_FILE` | `VARCHAR2(1)` | Indicates whether the library supports mapping files (`Y`) or not (`N`) |
| `FILE_CFGID` | `VARCHAR2(13)` | Type of configuration ID supported for files: |
| `MAP_ELEM` | `VARCHAR2(1)` | Indicates whether the library supports mapping elements (`Y`) or not (`N`) |
| `ELEM_CFGID` | `VARCHAR2(13)` | Type of configuration id supported for elements: |
| `MAP_SYNC` | `VARCHAR2(1)` | Indicates whether the library needs to be explicitly synced so that future mappings reflect the most recent changes (`Y`) or not (`N`). Note that configuration IDs cannot be supported if the library needs to be explicitly synced. |