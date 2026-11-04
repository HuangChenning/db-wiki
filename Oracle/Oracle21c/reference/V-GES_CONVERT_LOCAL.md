---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-GES_CONVERT_LOCAL.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.253 V$GES\_CONVERT\_LOCAL

`V$GES_CONVERT_LOCAL` displays statistics for local GES enqueue operations. This view records average convert times, count information, and timed statistics for global enqueue requests.

| Column | Datatype | Description |
| --- | --- | --- |
| `INST_ID` | `NUMBER` | ID of the instance |
| `CONVERT_TYPE` | `VARCHAR2(16)` | Conversion type:  - `NULL -> SS ` - NULL mode to subshared mode - `NULL -> SX  ` - NULL mode to shared exclusive mode - `NULL -> S` - NULL mode to shared mode - `NULL -> SSX` - NULL mode to subshared exclusive mode - `NULL -> X` - NULL mode to exclusive mode - `SS -> SX ` - Subshared mode to shared exclusive mode - `SS -> S ` - Subshared mode to shared mode - `SS -> SSX` - Subshared mode to subshared exclusive mode - `SS -> X ` - Subshared mode to exclusive mode - `SX -> S ` - Shared exclusive mode to shared mode - `SX -> SSX` - Shared exclusive mode to subshared exclusive mode - `SX -> X ` - Shared exclusive mode to exclusive mode - `S -> SX ` - Shared mode to shared exclusive mode - `S -> SSX` - Shared mode to subshared exclusive mode - `S -> X ` - Shared mode to exclusive mode - `SSX -> X ` - Sub-shared exclusive mode to exclusive mode |
| `AVERAGE_CONVERT_TIME` | `NUMBER` | Average conversion time for each type of lock operation (in hundredths of a second) |
| `CONVERT_COUNT` | `NUMBER` | Number of operations |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |