---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ARCHIVE_GAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.39 V$ARCHIVE\_GAP

`V$ARCHIVE_GAP` displays information about archive gaps on a standby database. This view can be used to find out the current archive gap that is blocking recovery for the current recovery incarnation.

| Column | Datatype | Description |
| --- | --- | --- |
| `THREAD#` | `NUMBER` | Thread number of the missing archived redo log files. The number is 1 for a single instance. For Oracle Real Application Clusters, this column will contain different numbers. |
| `LOW_SEQUENCE#` | `NUMBER` | Lowest sequence number of the log files received on the standby system |
| `HIGH_SEQUENCE#` | `NUMBER` | Highest sequence number of the log files received on the standby system |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |