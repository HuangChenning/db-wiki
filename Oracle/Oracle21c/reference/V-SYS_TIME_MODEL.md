---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SYS_TIME_MODEL.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.93 V$SYS\_TIME\_MODEL

`V$SYS_TIME_MODEL` displays the system-wide accumulated times for various operations. The time reported is the total elapsed or CPU time (in microseconds). Any timed operation will buffer at most 5 seconds of time data. Specifically, this means that if a timed operation (such as SQL execution) takes a long period of time to perform, the data published to this view is at most missing 5 seconds of the time accumulated for the operation.

The time values are 8-byte integers and can therefore hold approximately 580,000 years worth of time before wrapping. Background process time is not included in a statistic value unless the statistic is specifically for background processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `STAT_ID` | `NUMBER` | Statistic identifier for the time statistic |
| `STAT_NAME` | `VARCHAR2(64)` | Name of the statistic (see [Table 10-1](V-SESS_TIME_MODEL.md)) |
| `VALUE` | `NUMBER` | Amount of time (in microseconds) that the system has spent in this operation |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view returns instance-wide data and a value of `0` in the `CON_ID` column when queried from the root of a CDB.