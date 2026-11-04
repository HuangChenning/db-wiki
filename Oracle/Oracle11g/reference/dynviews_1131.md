---
title: "V$EVENTMETRIC"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1131.htm
tags:
  - oracle
  - 11g
  - reference
---

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