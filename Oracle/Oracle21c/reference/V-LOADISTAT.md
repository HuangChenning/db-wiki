---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOADISTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.39 V$LOADISTAT

`V$LOADISTAT` contains errors that occurred when updating indexes on a table during a load using the Direct Path API.

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNER` | `VARCHAR2(31)` | Schema name |
| `TABNAME` | `VARCHAR2(31)` | Table name |
| `INDEXNAME` | `VARCHAR2(31)` | Index name |
| `SUBNAME` | `VARCHAR2(31)` | Index sub name |
| `MESSAGE_NUM` | `NUMBER` | Error message number |
| `MESSAGE` | `VARCHAR2(4000)` | Error message |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |