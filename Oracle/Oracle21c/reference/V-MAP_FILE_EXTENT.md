---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MAP_FILE_EXTENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.70 V$MAP\_FILE\_EXTENT

`V$MAP_FILE_EXTENT` displays a list of all file extent mapping structures in the shared memory of the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_MAP_IDX` | `NUMBER` | File index (corresponds to `FILE_MAP_IDX` in `V$MAP_FILE`) |
| `EXT_NUM` | `NUMBER` | File extent number |
| `EXT_ELEM_OFF` | `NUMBER` | Element offset in HKB |
| `EXT_SIZE` | `NUMBER` | File extent size in HKB |
| `EXT_FILE_OFF` | `NUMBER` | File Offset in HKB |
| `EXT_TYPE` | `VARCHAR2(6)` | File Extent Type:  - `DATA` - `PARITY` - `NONE` |
| `ELEM_IDX` | `NUMBER` | Index in `V$MAP_ELEMENT` corresponding to the element where the file extent resides |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |