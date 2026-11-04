---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-RESOURCE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$RESOURCE` contains resource name and address information.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of the resource object |
| `TYPE` | `VARCHAR2(2)` | Resource type; the resource types are listed in [Table 8-1](V-LOCK.md) |
| `ID1` | `NUMBER` | Resource identifier #1 |
| `ID2` | `NUMBER` | Resource identifier #2 |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |