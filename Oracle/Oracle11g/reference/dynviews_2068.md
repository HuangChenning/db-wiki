---
title: "V$MUTEX_SLEEP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2068.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MUTEX_SLEEP` shows the wait time, and the number of sleeps for each combination of mutex type and location.

| Column | Datatype | Description |
| --- | --- | --- |
| `MUTEX_TYPE` | `VARCHAR2(32)` | Type of action/object the mutex protects |
| `LOCATION` | `VARCHAR2(40)` | The code location where the waiter slept for the mutex |
| `SLEEPS` | `NUMBER` | Number of sleeps for this `MUTEX_TYPE` and `LOCATION` |
| `WAIT_TIME` | `NUMBER` | Wait time in microseconds |