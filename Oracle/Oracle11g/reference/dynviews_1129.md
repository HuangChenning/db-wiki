---
title: "V$EVENT_HISTOGRAM"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1129.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$EVENT_HISTOGRAM` displays a histogram of the number of waits, the maximum wait, and total wait time on an event basis. The histogram has buckets of time intervals from < 1 ms, < 2 ms, < 4 ms, < 8 ms,... < 2 <sup>21</sup> ms, < 2 <sup>22</sup> ms, and >= 2 <sup>22</sup> ms.

The histogram will not be filled unless the `TIMED_STATISTICS` initialization parameter is set to `true`.

| Column | Datatype | Description |
| --- | --- | --- |
| `EVENT#` | `NUMBER` | Event number |
| `EVENT` | `VARCHAR2(64)` | Name of the Event |
| `WAIT_TIME_MILLI` | `NUMBER` | Amount of time the bucket represents (in milliseconds). If the duration = `num`, then this column represents waits of duration < `num` that are not included in any smaller bucket. |
| `WAIT_COUNT` | `NUMBER` | Number of waits of the duration belonging to the bucket of the histogram |
| `LAST_UPDATE_TIME` | `VARCHAR2(64)` | Indicates the last time the bucket was updated (the ending timestamp of the last wait falling into the bucket's duration) |