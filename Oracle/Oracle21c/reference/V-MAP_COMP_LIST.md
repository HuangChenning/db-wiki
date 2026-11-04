---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MAP_COMP_LIST.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.66 V$MAP\_COMP\_LIST

`V$MAP_COMP_LIST` displays supplementary information for all element mapping structures.

| Column | Datatype | Description |
| --- | --- | --- |
| `ELEM_IDX` | `NUMBER` | Index corresponding to the element |
| `NUM_COMP` | `NUMBER` | Number of components (maximum is 5) |
| `COMP1_NAME` | `VARCHAR2(256)` | Name of the first component |
| `COMP1_VAL` | `VARCHAR2(256)` | Value of the first component |
| `COMP2_NAME` | `VARCHAR2(256)` | Name of the second component |
| `COMP2_VAL` | `VARCHAR2(256)` | Value of the second component |
| `COMP3_NAME` | `VARCHAR2(256)` | Name of the third component |
| `COMP3_VAL` | `VARCHAR2(256)` | Value of the third component |
| `COMP4_NAME` | `VARCHAR2(256)` | Name of the fourth component |
| `COMP4_VAL` | `VARCHAR2(256)` | Value of the fourth component |
| `COMP5_NAME` | `VARCHAR2(256)` | Name of the fifth component |
| `COMP5_VAL` | `VARCHAR2(256)` | Value of the fifth component |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |