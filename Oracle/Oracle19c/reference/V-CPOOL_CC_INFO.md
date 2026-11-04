---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-CPOOL_CC_INFO.html
tags:
  - oracle
  - 19c
  - reference
---

## 7.153 V$CPOOL\_CC\_INFO

`V$CPOOL_CC_INFO` displays information about the pool-to-connection class mapping for the Database Resident Connection Pool per instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `POOL_NAME` | `VARCHAR2(1024)` | Name of the Database Resident Connection Pool |
| `CCLASS_NAME` | `VARCHAR2(1024)` | Name of the connection class |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |