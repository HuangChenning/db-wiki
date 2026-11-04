---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-QUARANTINE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.152 V$QUARANTINE

| Column | Datatype | Description |
| --- | --- | --- |
| `OBJECT` | `VARCHAR2(64)` | Type of quarantined object (description of the memory) |
| `ADDRESS` | `RAW(8)` | Address of the object |
| `BYTES` | `NUMBER` | Amount of memory used by the object (this is the minimum amount; the actual amount may be unknown) |
| `ERROR` | `VARCHAR2(128)` | Oracle error causing quarantine |
| `TIMESTAMP` | `TIMESTAMP(6) WITH TIME ZONE` | Time the object was quarantined |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |