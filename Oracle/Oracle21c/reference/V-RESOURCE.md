---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RESOURCE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.167 V$RESOURCE

`V$RESOURCE` contains resource name and address information.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of the resource object |
| `TYPE` | `VARCHAR2(2)` | Resource type; the resource types are listed in [Table 9-1](V-LOCK.md) |
| `ID1` | `NUMBER` | Resource identifier #1 |
| `ID2` | `NUMBER` | Resource identifier #2 |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |