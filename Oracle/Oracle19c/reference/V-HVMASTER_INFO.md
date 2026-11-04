---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-HVMASTER_INFO.html
tags:
  - oracle
  - 19c
  - reference
---

## 7.278 V$HVMASTER\_INFO

`V$HVMASTER_INFO` describes the current and previous master instances and the number of re-masterings of Global Enqueue Service resources.

| Column | Datatype | Description |
| --- | --- | --- |
| `HV_ID` | `NUMBER` | Hash value ID |
| `CURRENT_MASTER` | `NUMBER` | Master instance of this hash value ID |
| `PREVIOUS_MASTER` | `NUMBER` | Previous master instance of this hash value ID |
| `REMASTER_CNT` | `NUMBER` | Number of times this has been remastered |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |