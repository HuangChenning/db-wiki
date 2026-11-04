---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SYSTEM_EVENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.100 V$SYSTEM\_EVENT

Note that the `TIME_WAITED` and `AVERAGE_WAIT` columns will contain a value of zero on those platforms that do not support a fast timing mechanism. If you are running on one of these platforms and you want this column to reflect true wait times, then you must set `TIMED_STATISTICS` to `TRUE` in the parameter file; doing this will have a small negative effect on system performance.

See Also:

" [TIMED\_STATISTICS](TIMED_STATISTICS.md) "

| Column | Datatype | Description |
| --- | --- | --- |
| `EVENT` | `VARCHAR2(64)` | Name of the wait event; derived statistic name from `V$EVENT_NAME`  See Also: " [Oracle Wait Events](oracle-wait-events.md) " |
| `TOTAL_WAITS` | `NUMBER` | Total number of waits for the event |
| `TOTAL_TIMEOUTS` | `NUMBER` | Total number of timeouts for the event |
| `TIME_WAITED` | `NUMBER` | Total amount of time waited for the event (in hundredths of a second) |
| `AVERAGE_WAIT` | `NUMBER` | Average amount of time waited for the event (in hundredths of a second) |
| `TIME_WAITED_MICRO` | `NUMBER` | Total amount of time waited for the event (in microseconds) |
| `CPU` | `NUMBER` | Total amount of CPU time consumed while implementing the wait event itself (in microseconds) |
| `TOTAL_WAITS_FG` | `NUMBER` | Total number of waits for the event, from foreground sessions |
| `TOTAL_TIMEOUTS_FG` | `NUMBER` | Total number of timeouts for the event, from foreground sessions |
| `TIME_WAITED_FG` | `NUMBER` | Total amount of time waited for the event, from foreground sessions (in hundredths of a second) |
| `AVERAGE_WAIT_FG` | `NUMBER` | Average amount of time waited for the event, from foreground sessions (in hundredths of a second) |
| `TIME_WAITED_MICRO_FG` | `NUMBER` | Total amount of time waited for the event, from foreground sessions (in microseconds) |
| `CPU_FG` | `NUMBER` | Total amount of CPU time consumed while implementing the wait event itself, from foreground sessions (in microseconds) |
| `EVENT_ID` | `NUMBER` | Identifier of the wait event |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the wait class of the wait event |
| `WAIT_CLASS#` | `NUMBER` | Number of the wait class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the wait class of the wait event |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view returns instance-wide data and a value of `0` in the `CON_ID` column when queried from the root of a CDB.