---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MUTEX_SLEEP_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.86 V$MUTEX\_SLEEP\_HISTORY

Each row in this view is for a specific time, mutex type, location, requesting session and blocking session combination. That is, it shows data related to a specific session (requesting session) that slept while requesting a specific mutex type and location, because it was being held by a specific blocking session. The data in this view is contained within a circular buffer, with the most recent sleeps shown.

| Column | Datatype | Description |
| --- | --- | --- |
| `MUTEX_IDENTIFIER` | `NUMBER` | Mutex ID |
| `SLEEP_TIMESTAMP` | `TIMESTAMP(6)` | The last date/time this `MUTEX_TYPE` and `LOCATION` was slept for by the `REQUESTING_SESSION`, while being held by the `BLOCKING_SESSION`. |
| `MUTEX_TYPE` | `VARCHAR2(32)` | Type of action/object the mutex protects |
| `GETS` | `NUMBER` | The total number of gets since the mutex was created and up until the time of the wait (and from all sessions past and present) |
| `SLEEPS` | `NUMBER` | The number of times the requester had to sleep before obtaining the mutex |
| `REQUESTING_SESSION` | `NUMBER` | The SID of a session requesting the mutex |
| `BLOCKING_SESSION` | `NUMBER` | The SID of a session holding the mutex |
| `LOCATION` | `VARCHAR2(40)` | The code location where the waiter slept for the mutex |
| `MUTEX_VALUE` | `RAW(4 \| 8)` | If the mutex is held in exclusive (X) mode, this column shows the SID of the blocking session, else it shows the number of sessions referencing the mutex in S mode. |
| `P1` | `NUMBER` | Reserved for internal use |
| `P1RAW` | `RAW(4 \| 8)` | Reserved for internal use |
| `P2` | `NUMBER` | Reserved for internal use |
| `P3` | `NUMBER` | Reserved for internal use |
| `P4` | `NUMBER` | Reserved for internal use |
| `P5` | `VARCHAR2(64)` | Reserved for internal use |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |