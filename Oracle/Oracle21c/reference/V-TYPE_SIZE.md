---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TYPE_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.125 V$TYPE\_SIZE

`V$TYPE_SIZE` displays the sizes of various database components for use in estimating data block capacity.

| Column | Datatype | Description |
| --- | --- | --- |
| `COMPONENT` | `VARCHAR2(8)` | Component name, such as segment or buffer header |
| `TYPE` | `VARCHAR2(8)` | Component type |
| `DESCRIPTION` | `VARCHAR2(32)` | Description of the component |
| `TYPE_SIZE` | `NUMBER` | Size of the component |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |