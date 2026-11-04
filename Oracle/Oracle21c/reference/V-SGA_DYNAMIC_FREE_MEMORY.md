---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SGA_DYNAMIC_FREE_MEMORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.34 V$SGA\_DYNAMIC\_FREE\_MEMORY

`V$SGA_DYNAMIC_FREE_MEMORY` displays information about the amount of SGA memory available for future dynamic SGA resize operations.

| Column | Datatype | Description |
| --- | --- | --- |
| `CURRENT_SIZE` | `NUMBER` | Amount of available memory (in bytes) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |