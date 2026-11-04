---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CON_EVENT_HISTOGRAM_MICRO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.130 V$CON\_EVENT\_HISTOGRAM\_MICRO

`V$CON_EVENT_HISTOGRAM_MICRO` displays a histogram of the number of waits, the maximum wait, and total wait time on an event basis for a container, in microseconds. The histogram has buckets of time intervals from < 1 us, < 2 us, < 4 us, < 8 us,... < 2 <sup>31</sup> us, < 2 <sup>32</sup> us, and >= 2 <sup>32</sup> us.

The histogram will not be filled unless the `TIMED_STATISTICS` initialization parameter is set to `true`.

| Column | Datatype | Description |
| --- | --- | --- |
| `EVENT#` | `NUMBER` | Event number |
| `EVENT` | `VARCHAR2(64)` | Name of the event |
| `WAIT_TIME_FORMAT` | `VARCHAR2(30)` | A human readable time string which is converted from `WAIT_TIME_MICRO`. When `WAIT_TIME_MICRO` < 1 millisecond, `WAIT_TIME_FORMAT` is shown in microseconds. When `WAIT_TIME_MICRO` < 1 second, `WAIT_TIME_FORMAT` is shown in milliseconds. When `WAIT_TIME_MICRO` < 1 minute, `WAIT_TIME_FORMAT` is shown in seconds. When `WAIT_TIME_MICRO` > 1 minute, `WAIT_TIME_FORMAT` is shown in minutes and seconds. |
| `WAIT_TIME_MICRO` | `NUMBER` | Amount of time the bucket represents (in microseconds). If the duration = `num`, then this column represents waits of duration < `num` that are not included in any smaller bucket. |
| `WAIT_COUNT` | `NUMBER` | Number of waits of the duration belonging to the bucket of the histogram |
| `LAST_UPDATE_TIME` | `VARCHAR2(73)` | Indicates the last time the bucket was updated (the ending timestamp of the last wait falling into the bucket's duration) |
| `CON_ID` | `NUMBER` | When queried from a non-CDB, the wait event data in that instance are returned, and the `CON_ID` value is `0`.  When queried from the root of a CDB, the wait event data in every container is returned, and the `CON_ID` value indicates the container to which the wait event data belong.  When queried from a PDB, wait event data in that PDB are returned, and the `CON_ID` value is the container ID for that PDB. |