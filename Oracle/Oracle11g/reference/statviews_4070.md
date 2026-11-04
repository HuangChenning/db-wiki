---
title: DBA_HIST_WAITCLASSMET_HISTORY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4070.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_WAITCLASSMET_HISTORY` displays the history of the wait event class metric data kept by the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID of the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number of the snapshot |
| `WAIT_CLASS_ID` | `NUMBER` | `NOT NULL` | Identifier of the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` |  | Name of the class of the wait event |
| `BEGIN_TIME` | `DATE` | `NOT NULL` | Begin time of the interval |
| `END_TIME` | `DATE` | `NOT NULL` | End time of the interval |
| `INTSIZE` | `NUMBER` | `NOT NULL` | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Metric group ID |
| `AVERAGE_WAITER_COUNT` | `NUMBER` | `NOT NULL` | Average waiter count |
| `DBTIME_IN_WAIT` | `NUMBER` | `NOT NULL` | Percent of database time spent in the wait |
| `TIME_WAITED` | `NUMBER` | `NOT NULL` | Time waited during the interval (in microseconds) |
| `WAIT_COUNT` | `NUMBER` | `NOT NULL` | Number of times waited |