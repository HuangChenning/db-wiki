---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SGA_TARGET_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.36 V$SGA\_TARGET\_ADVICE

`V$SGA_TARGET_ADVICE` displays information about the `SGA_TARGET` initialization parameter.

| Column | Datatype | Description |
| --- | --- | --- |
| `SGA_SIZE` | `NUMBER` | Size of the SGA |
| `SGA_SIZE_FACTOR` | `NUMBER` | Ratio between the SGA\_SIZE and the current size of the SGA |
| `ESTD_DB_TIME` | `NUMBER` | Estimated DB\_TIME for this SGA\_SIZE |
| `ESTD_DB_TIME_FACTOR` | `NUMBER` | Ratio between ESTD\_DB\_TIME and DB\_TIME for the current size of the SGA |
| `ESTD_PHYSICAL_READS` | `NUMBER` | Estimated number of physical reads |
| `ESTD_BUFFER_CACHE_SIZE` | `NUMBER` | Estimated size of the buffer cache |
| `ESTD_SHARED_POOL_SIZE` | `NUMBER` | Estimated size of the shared pool |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [SGA\_TARGET](SGA_TARGET.md) "