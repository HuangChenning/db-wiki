---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-MAP_EXT_ELEMENT.html
tags:
  - oracle
  - 12c
  - reference
---

`V$MAP_EXT_ELEMENT` displays supplementary information for all element mapping structures.

| Column | Datatype | Description |
| --- | --- | --- |
| `ELEM_IDX` | `NUMBER` | Index corresponding to the element |
| `NUM_ATTRB` | `NUMBER` | Number of Attributes (maximum is 5) |
| `ATTRB1_NAME` | `VARCHAR2(256)` | Name of the first Attribute |
| `ATTRB1_VAL` | `VARCHAR2(256)` | Value of the first attribute |
| `ATTRB2_NAME` | `VARCHAR2(256)` | Name of the second attribute |
| `ATTRB2_VAL` | `VARCHAR2(256)` | Value of the second attribute |
| `ATTRB3_NAME` | `VARCHAR2(256)` | Name of the third attribute |
| `ATTRB3_VAL` | `VARCHAR2(256)` | Value of the third attribute |
| `ATTRB4_NAME` | `VARCHAR2(256)` | Name of the fourth attribute |
| `ATTRB4_VAL` | `VARCHAR2(256)` | Value of the fourth attribute |
| `ATTRB5_NAME` | `VARCHAR2(256)` | Name of the fifth attribute |
| `ATTRB5_VAL` | `VARCHAR2(256)` | Value of the fifth attribute |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |