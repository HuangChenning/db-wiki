---
title: "V$SERVICE_EVENT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3007.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SERVICE_EVENT` displays aggregated wait counts and wait times for each wait statistic.

| Column | Datatype | Description |
| --- | --- | --- |
| `SERVICE_NAME` | `VARCHAR2(64)` | Service name from `V$SERVICES` |
| `SERVICE_NAME_HASH` | `NUMBER` | Service name hash from `V$SERVICES` |
| `EVENT` | `VARCHAR2(64)` | Name of the wait event; derived statistic name from `V$EVENT_NAME` |
| `EVENT_ID` | `NUMBER` | Identifier of the event |
| `TOTAL_WAITS` | `NUMBER` | Total amount of time waited for the event by this service (in hundredths of a second) |
| `TOTAL_TIMEOUTS` | `NUMBER` | Total number of timeouts for the event by this service |
| `TIME_WAITED` | `NUMBER` | Time waited for the event (in hundredths of a second) |
| `AVERAGE_WAIT` | `NUMBER` | Average amount of time waited for the event by this service (in hundredths of a second) |
| `MAX_WAIT` | `NUMBER` | Maximum time (in hundredths of a second) waited for the event by this service |
| `TIME_WAITED_MICRO` | `NUMBER` | Total time waited for the event (in microseconds) |