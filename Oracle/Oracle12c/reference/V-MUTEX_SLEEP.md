---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-MUTEX_SLEEP.html
tags:
  - oracle
  - 12c
  - reference
---

`V$MUTEX_SLEEP` shows the wait time, and the number of sleeps for each combination of mutex type and location.

| Column | Datatype | Description |
| --- | --- | --- |
| `MUTEX_TYPE` | `VARCHAR2(32)` | Type of action/object the mutex protects |
| `LOCATION` | `VARCHAR2(40)` | The code location where the waiter slept for the mutex |
| `SLEEPS` | `NUMBER` | Number of sleeps for this `MUTEX_TYPE` and `LOCATION` |
| `WAIT_TIME` | `NUMBER` | Wait time in microseconds |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |