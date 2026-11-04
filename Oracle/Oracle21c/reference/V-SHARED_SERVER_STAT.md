---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SHARED_SERVER_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.43 V$SHARED\_SERVER\_STAT

`V$SHARED_SERVER_STAT` displays statistics for all shared server processes. The statistics are cumulative from the start of the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `MESSAGES` | `NUMBER` | Number of messages processed |
| `BYTES` | `NUMBER` | Total number of bytes in all messages |
| `IDLE` | `NUMBER` | Total idle time (in hundredths of a second) |
| `BUSY` | `NUMBER` | Total busy time (in hundredths of a second) |
| `IN_NET` | `NUMBER` | Total incoming network wait time (in hundredths of a second) |
| `OUT_NET` | `NUMBER` | Total outgoing network wait time (in hundredths of a second) |
| `REQUESTS` | `NUMBER` | Total number of requests taken from the common queue |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |