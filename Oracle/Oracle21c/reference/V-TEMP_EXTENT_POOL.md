---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TEMP_EXTENT_POOL.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.108 V$TEMP\_EXTENT\_POOL

Note that loading of the temporary space cache is lazy and that instances can be dormant.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |
| `FILE_ID` | `NUMBER` |  | Absolute file number |
| `EXTENTS_CACHED` | `NUMBER` |  | Number of extents that have been cached |
| `EXTENTS_USED` | `NUMBER` |  | Number of extents that are actually being used |
| `BLOCKS_CACHED` | `NUMBER` |  | Number of blocks that are cached |
| `BLOCKS_USED` | `NUMBER` |  | Number of blocks that are used |
| `BYTES_CACHED` | `NUMBER` |  | Number of bytes that are cached |
| `BYTES_USED` | `NUMBER` |  | Number of bytes that are used |
| `RELATIVE_FNO` | `NUMBER` |  | Relative file number |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |