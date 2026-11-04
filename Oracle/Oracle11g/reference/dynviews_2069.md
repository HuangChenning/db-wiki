---
title: "V$MUTEX_SLEEP_HISTORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2069.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MUTEX_SLEEP_HISTORY` displays time-series data. Each row in this view is for a specific time, mutex type, location, requesting session and blocking session combination. That is, it shows data related to a specific session (requesting session) that slept while requesting a specific mutex type and location, because it was being held by a specific blocking session. The data in this view is contained within a circular buffer, with the most recent sleeps shown.

| Column | Datatype | Description |
| --- | --- | --- |
| `MUTEX_IDENTIFIER` | `NUMBER` | Mutex ID |
| `SLEEP_TIMESTAMP` | `TIMESTAMP(6)` | The last date/time this `MUTEX_TYPE` and `LOCATION` was slept for by the `REQUESTING_SESSION`, while being held by the `BLOCKING_SESSION`. |
| `MUTEX_TYPE` | `VARCHAR2(32)` | Type of action/object the mutex protects |
| `GETS` | `NUMBER` | The number of times the mutex/location was requested by the requesting session while being held by the blocking session. `GETS` is only incremented once per request, irrespective of the number of sleeps required to obtain the mutex. |
| `SLEEPS` | `NUMBER` | The number of times the requestor had to sleep before obtaining the mutex |
| `REQUESTING_SESSION` | `NUMBER` | The SID of a session requesting the mutex |
| `BLOCKING_SESSION` | `NUMBER` | The SID of a session holding the mutex |
| `LOCATION` | `VARCHAR2(40)` | The code location where the waiter slept for the mutex |
| `MUTEX_VALUE` | `RAW(4)` | If the mutex is held in exclusive (X) mode, this column shows the SID of the blocking session, else it shows the number of sessions referencing the mutex in S mode. |
| `P1` | `NUMBER` | Reserved for internal use |
| `P1RAW` | `RAW(4)` | Reserved for internal use |
| `P2` | `NUMBER` | Reserved for internal use |
| `P3` | `NUMBER` | Reserved for internal use |
| `P4` | `NUMBER` | Reserved for internal use |
| `P5` | `VARCHAR2(64)` | Reserved for internal use |