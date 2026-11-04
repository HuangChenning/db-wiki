---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_MUTEX_SLEEP.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.13 DBA\_HIST\_MUTEX\_SLEEP

`DBA_HIST_MUTEX_SLEEP` displays mutex sleep summary historical statistics information.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database identifier for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `MUTEX_TYPE` | `VARCHAR2(32)` | `NOT NULL` | Mutex type |
| `LOCATION` | `VARCHAR2(40)` | `NOT NULL` | The code location where the waiter slept for the mutex |
| `SLEEPS` | `NUMBER` |  | Number of sleeps for this `MUTEX_TYPE` and `LOCATION` |
| `WAIT_TIME` | `NUMBER` |  | Wait time in microseconds |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |