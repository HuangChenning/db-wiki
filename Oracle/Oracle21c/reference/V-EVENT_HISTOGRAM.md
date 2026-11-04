---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EVENT_HISTOGRAM.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.216 V$EVENT\_HISTOGRAM

`V$EVENT_HISTOGRAM` displays a histogram of the number of waits, the maximum wait, and total wait time on an event basis, in milliseconds. The histogram has buckets of time intervals from < 1 ms, < 2 ms, < 4 ms, < 8 ms,... < 2 <sup>21</sup> ms, < 2 <sup>22</sup> ms, and >= 2 <sup>22</sup> ms.

The histogram will not be filled unless the `TIMED_STATISTICS` initialization parameter is set to `true`.

| Column | Datatype | Description |
| --- | --- | --- |
| `EVENT#` | `NUMBER` | Event number |
| `EVENT` | `VARCHAR2(64)` | Name of the event |
| `WAIT_TIME_MILLI` | `NUMBER` | Amount of time the bucket represents (in milliseconds). If the duration = `num`, then this column represents waits of duration < `num` that are not included in any smaller bucket. |
| `WAIT_COUNT` | `NUMBER` | Number of waits of the duration belonging to the bucket of the histogram |
| `LAST_UPDATE_TIME` | `VARCHAR2(64)` | Indicates the last time the bucket was updated (the ending timestamp of the last wait falling into the bucket's duration) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [TIMED\_STATISTICS](TIMED_STATISTICS.md) "