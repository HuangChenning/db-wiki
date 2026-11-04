---
title: "V$SYS_TIME_MODEL"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3088.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SYS_TIME_MODEL` displays the system-wide accumulated times for various operations. The time reported is the total elapsed or CPU time (in microseconds). Any timed operation will buffer at most 5 seconds of time data. Specifically, this means that if a timed operation (such as SQL execution) takes a long period of time to perform, the data published to this view is at most missing 5 seconds of the time accumulated for the operation.

The time values are 8-byte integers and can therefore hold approximately 580,000 years worth of time before wrapping. Background process time is not included in a statistic value unless the statistic is specifically for background processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `STAT_ID` | `NUMBER` | Statistic identifier for the time statistic |
| `STAT_NAME` | `VARCHAR2(64)` | Name of the statistic (see [Table 9-1](dynviews_3015.md)) |
| `VALUE` | `NUMBER` | Amount of time (in microseconds) that the system has spent in this operation |