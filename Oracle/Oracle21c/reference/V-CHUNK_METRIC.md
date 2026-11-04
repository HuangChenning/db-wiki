---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CHUNK_METRIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.121 V$CHUNK\_METRIC

`V$CHUNK_METRIC` displays the metric values captured for the most recent 30-second intervals for the workload against each chunk available on the database.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `CHUNK_ID` | `NUMBER` | Chunk number (internal) |
| `CALLSPERSEC` | `NUMBER` | Number of user calls per second to the chunks |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SERVICE\_REGION\_METRIC](V-SERVICE_REGION_METRIC.md) "