---
title: "V$WAITCLASSMETRIC"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3123.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$WAITCLASSMETRIC` displays metric values of wait classes for the most recent 60-second interval. A history of the last one hour will be kept in the system.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `WAIT_CLASS#` | `NUMBER` | Number of the class of the wait event |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the class of the wait event |
| `AVERAGE_WAITER_COUNT` | `NUMBER` | Average waiter count |
| `DBTIME_IN_WAIT` | `NUMBER` | Percent of database time spent in the wait |
| `TIME_WAITED` | `NUMBER` | Time waited during the interval (in hundredths of a second) |
| `WAIT_COUNT` | `NUMBER` | Number of times waited |
| `TIME_WAITED_FG` | `NUMBER` | Amount of time (in hundredths of a second) spent in waits from this wait class in foreground sessions |
| `WAIT_COUNT_FG` | `NUMBER` | Number of times foreground processes waited |