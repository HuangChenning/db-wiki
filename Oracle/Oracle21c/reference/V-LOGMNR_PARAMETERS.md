---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGMNR_PARAMETERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.55 V$LOGMNR\_PARAMETERS

| Column | Datatype | Description |
| --- | --- | --- |
| `START_DATE` | `DATE` | Date to start the search |
| `REQUIRED_START_DATE` | `DATE` | Required date to start the search if DDL tracking is enabled |
| `END_DATE` | `DATE` | Date to end the search |
| `START_SCN` | `NUMBER` | System change number to start the search |
| `REQUIRED_START_SCN` | `NUMBER` | Required system change number to start the search if DDL tracking is enabled |
| `END_SCN` | `NUMBER` | System change number to end the search |
| `OPTIONS` | `NUMBER` | Options specified for the current LogMiner session |
| `INFO` | `VARCHAR2(32)` | This column is always null. |
| `STATUS` | `NUMBER` | This column is always `0`. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |