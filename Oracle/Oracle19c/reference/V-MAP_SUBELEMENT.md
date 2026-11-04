---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-MAP_SUBELEMENT.html
tags:
  - oracle
  - 19c
  - reference
---

## 8.72 V$MAP\_SUBELEMENT

`V$MAP_SUBELEMENT` displays a list of all subelement mapping structures in the shared memory of the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `CHILD_IDX` | `NUMBER` | Index in `V$MAP_ELEMENT` corresponding to the child element |
| `PARENT_IDX` | `NUMBER` | Index in `V$MAP_ELEMENT` corresponding to the parent element |
| `SUB_NUM` | `NUMBER` | Subelement number |
| `SUB_SIZE` | `NUMBER` | Subelement size in HKB |
| `ELEM_OFFSET` | `NUMBER` | Offset in HKB on the child element |
| `SUB_FLAGS` | `NUMBER` | Subelement flags (currently unused) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |