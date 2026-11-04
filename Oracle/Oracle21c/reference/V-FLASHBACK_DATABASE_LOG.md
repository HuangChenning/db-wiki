---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FLASHBACK_DATABASE_LOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.234 V$FLASHBACK\_DATABASE\_LOG

`V$FLASHBACK_DATABASE_LOG` displays information about the flashback data. Use this view to help estimate the amount of flashback space required for the current workload.

| Column | Datatype | Description |
| --- | --- | --- |
| `OLDEST_FLASHBACK_SCN` | `NUMBER` | Lowest system change number (SCN) in the flashback data, for any incarnation |
| `OLDEST_FLASHBACK_TIME` | `DATE` | Time of the lowest SCN in the flashback data, for any incarnation |
| `RETENTION_TARGET` | `NUMBER` | Target retention time (in minutes) |
| `FLASHBACK_SIZE` | `NUMBER` | Current size (in bytes) of the flashback data |
| `ESTIMATED_FLASHBACK_SIZE` | `NUMBER` | Estimated size of flashback data needed (in bytes) for the current target retention |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |