---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TEMPUNDOSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.114 V$TEMPUNDOSTAT

It displays a histogram of statistical data to show how the system is working. Each row in the view keeps statistics collected in the instance for a 10-minute interval. The rows are in the descending order of the `BEGIN_TIME` column value. This view contains a total of 576 rows, spanning a 4-day cycle. This view is similar to the `V$UNDOSTAT` view.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Identifies the beginning of the time interval |
| `END_TIME` | `DATE` | Identifies the end of the time interval |
| `UNDOTSN` | `NUMBER` | Represents the last active undo tablespace in the duration of time. The tablespace ID of the active undo tablespace is returned in this column. If more than one undo tablespace was active in that period, the active undo tablespace that was active at the end of the period is reported. |
| `TXNCOUNT` | `NUMBER` | Total number of transaction that have bound to the temp undo segment contained in above tablespace within the interval period |
| `MAXCONCURRENCY` | `NUMBER` | Highest number of transactions executed concurrently which modified temporary objects within the interval period |
| `MAXQUERYLEN` | `NUMBER` | Reserved for future use |
| `MAXQUERYID` | `VARCHAR2(13)` | Reserved for future use |
| `UNDOBLKCNT` | `NUMBER` | Total number of temporary undo blocks consumed |
| `EXTCNT` | `NUMBER` | Total number of extents consumed |
| `USCOUNT` | `NUMBER` | Temp undo segments created in this period |
| `SSOLDERRCNT` | `NUMBER` | Identifies the number of times the error `ORA-01555` occurred. You can use this statistic to decide whether or not the `UNDO_RETENTION` initialization parameter is set properly given the size of the undo tablespace. Increasing the value of `UNDO_RETENTION` can reduce the occurrence of this error. |
| `NOSPACEERRCNT` | `NUMBER` | Total number of times the error 'no space left for temporary undo' was raised |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$UNDOSTAT](V-UNDOSTAT.md) "