---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-WAITCLASSMETRIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.131 V$WAITCLASSMETRIC

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |