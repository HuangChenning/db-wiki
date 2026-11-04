---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-UNDOSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.126 V$UNDOSTAT

`V$UNDOSTAT` displays a histogram of statistical data to show how well the system is working. The available statistics include undo space consumption, transaction concurrency, and length of queries executed in the instance. You can use this view to estimate the amount of undo space required for the current workload. Oracle uses this view to tune undo usage in the system. The view returns NULL values if the system is in manual undo management mode.

Each row in the view keeps statistics collected in the instance for a 10-minute interval. The rows are in descending order by the `BEGIN_TIME` column value. Each row belongs to the time interval marked by (`BEGIN_TIME`, `END_TIME`). Each column represents the data collected for the particular statistic in that time interval. The first row of the view contains statistics for the (partial) current time period. The view contains a total of 576 rows, spanning a 4 day cycle.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Identifies the beginning of the time interval |
| `END_TIME` | `DATE` | Identifies the end of the time interval |
| `UNDOTSN` | `NUMBER` | Represents the last active undo tablespace in the duration of time. The tablespace ID of the active undo tablespace is returned in this column. If more than one undo tablespace was active in that period, the active undo tablespace that was active at the end of the period is reported. |
| `UNDOBLKS` | `NUMBER` | Represents the total number of undo blocks consumed. You can use this column to obtain the consumption rate of undo blocks, and thereby estimate the size of the undo tablespace needed to handle the workload on your system. |
| `TXNCOUNT` | `NUMBER` | Identifies the total number of transactions executed within the period |
| `MAXQUERYLEN` | `NUMBER` | Identifies the length of the longest query (in seconds) executed in the instance during the period. You can use this statistic to estimate the proper setting of the `UNDO_RETENTION` initialization parameter. The length of a query is measured from the cursor open time to the last fetch/execute time of the cursor. Only the length of those cursors that have been fetched/executed during the period are reflected in the view. |
| `MAXQUERYID` | `VARCHAR2(13)` | SQL identifier of the longest running SQL statement in the period |
| `MAXCONCURRENCY` | `NUMBER` | Identifies the highest number of transactions executed concurrently within the period |
| `UNXPSTEALCNT` | `NUMBER` | Number of attempts to obtain undo space by stealing unexpired extents from other transactions |
| `UNXPBLKRELCNT` | `NUMBER` | Number of unexpired blocks removed from certain undo segments so they can be used by other transactions |
| `UNXPBLKREUCNT` | `NUMBER` | Number of unexpired undo blocks reused by transactions |
| `EXPSTEALCNT` | `NUMBER` | Number of attempts to steal expired undo blocks from other undo segments |
| `EXPBLKRELCNT` | `NUMBER` | Number of expired undo blocks stolen from other undo segments |
| `EXPBLKREUCNT` | `NUMBER` | Number of expired undo blocks reused within the same undo segments |
| `SSOLDERRCNT` | `NUMBER` | Identifies the number of times the error `ORA-01555` occurred. You can use this statistic to decide whether or not the `UNDO_RETENTION` initialization parameter is set properly given the size of the undo tablespace. Increasing the value of `UNDO_RETENTION` can reduce the occurrence of this error. |
| `NOSPACEERRCNT` | `NUMBER` | Identifies the number of times space was requested in the undo tablespace and there was no free space available. That is, all of the space in the undo tablespace was in use by active transactions. The corrective action is to add more space to the undo tablespace. |
| `ACTIVEBLKS` | `NUMBER` | Total number of blocks in the active extents of the undo tablespace for the instance at the sampled time in the period |
| `UNEXPIREDBLKS` | `NUMBER` | Total number of blocks in the unexpired extents of the undo tablespace for the instance at the sampled time in the period |
| `EXPIREDBLKS` | `NUMBER` | Total number of blocks in the expired extents of the undo tablespace for the instance at the sampled time in the period |
| `TUNED_UNDORETENTION` | `NUMBER` | Amount of time (in seconds) for which undo will not be recycled from the time it was committed. At any point in time, the latest value of `TUNED_UNDORETENTION` is used to determine whether data committed at a particular time in the past can be recycled.  The value of this column is not meaningful on an Oracle Active Data Guard standby database instance, because the system does not tune this value on such instances. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [UNDO\_RETENTION](UNDO_RETENTION.md) "