---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CON_SYSTEM_EVENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.136 V$CON\_SYSTEM\_EVENT

`V$CON_SYSTEM_EVENT` displays information on total waits for an event in a container.

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
| `CON_ID` | `NUMBER` | When queried from a non-CDB, the wait event data in that instance are returned, and the `CON_ID` value is `0`.  When queried from the root of a CDB, the wait event data in every container is returned, and the `CON_ID` value indicates the container to which the wait event data belong.  When queried from a PDB, wait event data in that PDB are returned, and the `CON_ID` value is the container ID for that PDB. |