---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EVENT_HISTOGRAM_MICRO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.217 V$EVENT\_HISTOGRAM\_MICRO

`V$EVENT_HISTOGRAM_MICRO` displays a histogram of the number of waits, the maximum wait, and total wait time on an event basis, in microseconds. The histogram has buckets of time intervals from < 1 us, < 2 us, < 4 us, < 8 us,... < 2 <sup>31</sup> us, < 2 <sup>32</sup> us, and >= 2 <sup>32</sup> us.

The histogram will not be filled unless the `TIMED_STATISTICS` initialization parameter is set to `true`.

| Column | Datatype | Description |
| --- | --- | --- |
| `EVENT#` | `NUMBER` | Event number |
| `EVENT` | `VARCHAR2(64)` | Name of the event |
| `WAIT_TIME_FORMAT` | `VARCHAR2(30)` | A human readable time string which is converted from `WAIT_TIME_MICRO`. When `WAIT_TIME_MICRO` < 1 millisecond, `WAIT_TIME_FORMAT` is shown in microseconds. When `WAIT_TIME_MICRO` < 1 second, `WAIT_TIME_FORMAT` is shown in milliseconds. When `WAIT_TIME_MICRO` < 1 minute, `WAIT_TIME_FORMAT` is shown in seconds. When `WAIT_TIME_MICRO` > 1 minute, `WAIT_TIME_FORMAT` is shown in minutes and seconds. |
| `WAIT_TIME_MICRO` | `NUMBER` | Amount of time the bucket represents (in microseconds). If the duration = `num`, then this column represents waits of duration < `num` that are not included in any smaller bucket. |
| `WAIT_COUNT` | `NUMBER` | Number of waits of the duration belonging to the bucket of the histogram |
| `LAST_UPDATE_TIME` | `VARCHAR2(64)` | Indicates the last time the bucket was updated (the ending timestamp of the last wait falling into the bucket's duration) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |