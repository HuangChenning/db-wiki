---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TEMP_EXTENT_MAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.107 V$TEMP\_EXTENT\_MAP

`V$TEMP_EXTENT_MAP` displays the status of each unit for all LOCALLY MANAGED temporary tablespaces.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace this unit belongs to |
| `FILE_ID` | `NUMBER` |  | Absolute file number |
| `BLOCK_ID` | `NUMBER` |  | Begin block number for this unit |
| `BYTES` | `NUMBER` |  | Bytes in the extent |
| `BLOCKS` | `NUMBER` |  | Blocks in the extent |
| `OWNER` | `NUMBER` |  | Instance which owns this unit |
| `RELATIVE_FNO` | `NUMBER` |  | Relative file number |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |