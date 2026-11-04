---
title: "V$SESSION_EVENT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3020.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SESSION_EVENT` displays information on waits for an event by a session. Note that the `TIME_WAITED` and `AVERAGE_WAIT` columns will contain a value of zero on those platforms that do not support a fast timing mechanism. If you are running on one of these platforms and you want this column to reflect true wait times, then you must set `TIMED_STATISTICS` to `true` in the parameter file; doing this will have a small negative effect on system performance.

See Also:

["TIMED\_STATISTICS"](initparams259.md)

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | ID of the session |
| `EVENT` | `VARCHAR2(64)` | Name of the wait event  See Also: [Appendix C, "Oracle Wait Events"](waitevents.md) |
| `TOTAL_WAITS` | `NUMBER` | Total number of waits for the event by the session |
| `TOTAL_TIMEOUTS` | `NUMBER` | Total number of timeouts for the event by the session |
| `TIME_WAITED` | `NUMBER` | Total amount of time waited for the event by the session (in hundredths of a second) |
| `AVERAGE_WAIT` | `NUMBER` | Average amount of time waited for the event by the session (in hundredths of a second) |
| `MAX_WAIT` | `NUMBER` | Maximum time waited for the event by the session (in hundredths of a second) |
| `TIME_WAITED_MICRO` | `NUMBER` | Total amount of time waited for the event by the session (in microseconds) |
| `EVENT_ID` | `NUMBER` | Identifier of the wait event |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the class of the wait event |
| `WAIT_CLASS#` | `NUMBER` | Number of the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the class of the wait event |