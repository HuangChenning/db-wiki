---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_WAITCLASSMET_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.84 DBA\_HIST\_WAITCLASSMET\_HISTORY

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
| `TIME_WAITED_FG` | `NUMBER` |  | Time waited (in hundredths of a second), from foreground sessions |
| `WAIT_COUNT_FG` | `NUMBER` |  | Number of times waited, from foreground sessions |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |