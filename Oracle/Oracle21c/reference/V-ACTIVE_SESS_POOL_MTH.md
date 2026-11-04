---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ACTIVE_SESS_POOL_MTH.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.7 V$ACTIVE\_SESS\_POOL\_MTH

`V$ACTIVE_SESS_POOL_MTH` displays available active session pool resource allocation methods.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(40)` | Name of the active session pool resource allocation method |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |