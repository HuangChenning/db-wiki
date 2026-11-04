---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-ACCESS.html
tags:
  - oracle
  - 19c
  - reference
---

## 7.4 V$ACCESS

`V$ACCESS` displays information about locks that are currently imposed on library cache objects.

The locks are imposed to ensure that they are not aged out of the library cache while they are required for SQL execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session number that is accessing an object |
| `OWNER` | `VARCHAR2(64)` | Owner of the object |
| `OBJECT` | `VARCHAR2(1000)` | Name of the object |
| `TYPE` | `VARCHAR2(64)` | Type identifier for the object |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |