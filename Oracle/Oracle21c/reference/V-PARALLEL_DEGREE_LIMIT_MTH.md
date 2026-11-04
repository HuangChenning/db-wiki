---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PARALLEL_DEGREE_LIMIT_MTH.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.107 V$PARALLEL\_DEGREE\_LIMIT\_MTH

`V$PARALLEL_DEGREE_LIMIT_MTH` displays all available parallel degree limit resource allocation methods.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(40)` | Name of the parallel degree limit resource allocation method |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |