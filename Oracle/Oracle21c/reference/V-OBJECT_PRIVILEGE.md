---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-OBJECT_PRIVILEGE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.96 V$OBJECT\_PRIVILEGE

`V$OBJECT_PRIVILEGE` displays information about privileges associated with an object.

| Column | Datatype | Description |
| --- | --- | --- |
| `OBJECT_TYPE_NAME` | `VARCHAR2(64)` | Name of the object type |
| `OBJECT_TYPE_ID` | `NUMBER` | ID of the object type |
| `PRIVILEGE_ID` | `NUMBER` | ID of the privilege |
| `PRIVILEGE_NAME` | `VARCHAR2(64)` | Name of the privilege |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |