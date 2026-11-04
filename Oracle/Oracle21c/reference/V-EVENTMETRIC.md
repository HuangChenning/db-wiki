---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EVENTMETRIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.219 V$EVENTMETRIC

`V$EVENTMETRIC` displays values of wait event metrics for the most recent 60-second interval.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `EVENT#` | `NUMBER` | Number of the event |
| `EVENT_ID` | `NUMBER` | Identifier of the event |
| `NUM_SESS_WAITING` | `NUMBER` | Number of sessions waiting at the end of the interval |
| `TIME_WAITED` | `NUMBER` | Time waited (in hundredths of a second) |
| `WAIT_COUNT` | `NUMBER` | Number of times waited |
| `TIME_WAITED_FG` | `NUMBER` | Time waited (in hundredths of a second), from foreground sessions |
| `WAIT_COUNT_FG` | `NUMBER` | Number of times waited, from foreground sessions |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |