---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SERVICE_EVENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.7 V$SERVICE\_EVENT

`V$SERVICE_EVENT` displays aggregated wait counts and wait times for each wait statistic.

| Column | Datatype | Description |
| --- | --- | --- |
| `SERVICE_NAME` | `VARCHAR2(64)` | Service name from `V$SERVICES` |
| `SERVICE_NAME_HASH` | `NUMBER` | Service name hash from `V$SERVICES` |
| `EVENT` | `VARCHAR2(64)` | Name of the wait event; derived statistic name from `V$EVENT_NAME`  See Also: " [Oracle Wait Events](oracle-wait-events.md) " |
| `EVENT_ID` | `NUMBER` | Identifier of the wait event |
| `TOTAL_WAITS` | `NUMBER` | Total number of waits for the event by the service |
| `TOTAL_TIMEOUTS` | `NUMBER` | Total number of timeouts for the event by the service |
| `TIME_WAITED` | `NUMBER` | Total amount of time waited for the event by the service (in hundredths of a second) |
| `AVERAGE_WAIT` | `NUMBER` | Average amount of time waited for the event by the service (in hundredths of a second) |
| `MAX_WAIT` | `NUMBER` | Maximum amount of time waited for the event by the service (in hundredths of a second) |
| `TIME_WAITED_MICRO` | `NUMBER` | Total amount of time waited for the event by the service (in microseconds) |
| `CPU` | `NUMBER` | Total amount of CPU time consumed by the service while implementing the wait event itself (in microseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |