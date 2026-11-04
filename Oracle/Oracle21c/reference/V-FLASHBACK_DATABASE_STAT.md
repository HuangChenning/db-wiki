---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FLASHBACK_DATABASE_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.236 V$FLASHBACK\_DATABASE\_STAT

`V$FLASHBACK_DATABASE_STAT` displays statistics for monitoring the I/O overhead of logging flashback data. This view also displays the estimated flashback space needed based on previous workloads.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Beginning of the time interval |
| `END_TIME` | `DATE` | End of the time interval |
| `FLASHBACK_DATA` | `NUMBER` | Number of bytes of flashback data written during the interval |
| `DB_DATA` | `NUMBER` | Number of bytes of database data read and written during the interval |
| `REDO_DATA` | `NUMBER` | Number of bytes of redo data written during the interval |
| `ESTIMATED_FLASHBACK_SIZE` | `NUMBER` | Value of `ESTIMATED_FLASHBACK_SIZE` in `V$FLASHBACK_DATABASE_LOG` at the end of the time interval |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |