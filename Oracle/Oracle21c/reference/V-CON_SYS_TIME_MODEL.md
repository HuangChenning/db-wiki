---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CON_SYS_TIME_MODEL.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.131 V$CON\_SYS\_TIME\_MODEL

`V$CON_SYS_TIME_MODEL` displays the systemwide accumulated times for various operations for the container from which it is queried.

The time reported is the total elapsed or CPU time (in microseconds). Any timed operation will buffer at most 5 seconds of time data. Specifically, this means that if a timed operation (such as SQL execution) takes a long period of time to perform, the data published to this view is at most missing 5 seconds of the time accumulated for the operation.

The time values are 8-byte integers and can therefore hold approximately 580,000 years worth of time before wrapping. Background process time is not included in a statistic value unless the statistic is specifically for background processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `STAT_ID` | `NUMBER` | Statistic identifier for the time statistic |
| `STAT_NAME` | `VARCHAR2(64)` | Name of the statistic (see [Table 10-1](V-SESS_TIME_MODEL.md)) |
| `VALUE` | `NUMBER` | Amount of time (in microseconds) that the system has spent in this operation |
| `CON_ID` | `NUMBER` | When queried from a non-CDB, the accumulated times for operations in that instance are returned, and the `CON_ID` value is `0`.  When queried from the root of a CDB, accumulated times for operations in every container are returned, and the `CON_ID` value indicates the container to which the times belong.  When queried from a PDB, accumulated times for operations in that PDB are returned, and the `CON_ID` value is the container ID for that PDB. |