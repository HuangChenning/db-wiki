---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SGAINFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.37 V$SGAINFO

`V$SGAINFO` displays size information about the SGA, including the sizes of different SGA items, the granule size, and free memory.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(32)` | Name of the SGA size item |
| `BYTES` | `NUMBER` | Size of the item (in bytes) |
| `RESIZEABLE` | `VARCHAR2(3)` | Indicates whether the item is resizeable (`Yes`) or not (`No`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |