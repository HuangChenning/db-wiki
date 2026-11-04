---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MAP_LIBRARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.72 V$MAP\_LIBRARY

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
| `FILE_CFGID` | `VARCHAR2(13)` | Type of configuration ID supported for files:  - `NONE` - Not supported - `PERSISTENT` - `NONPERSISTENT` |
| `MAP_ELEM` | `VARCHAR2(1)` | Indicates whether the library supports mapping elements (`Y`) or not (`N`) |
| `ELEM_CFGID` | `VARCHAR2(13)` | Type of configuration id supported for elements:  - `NONE` - Not supported - `PERSISTENT` - `NONPERSISTENT` |
| `MAP_SYNC` | `VARCHAR2(1)` | Indicates whether the library needs to be explicitly synchronized so that future mappings reflect the most recent changes (`Y`) or not (`N`). Note that configuration IDs cannot be supported if the library needs to be explicitly synced. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |