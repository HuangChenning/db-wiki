---
title: "V$FILE_HISTOGRAM"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1137.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FILE_HISTOGRAM` displays a histogram of all synchronous single block reads on a per-file basis (for data files). The histogram has buckets of time intervals from < 1 ms, < 2 ms, < 4 ms, < 8 ms,... < 2 <sup>21</sup> ms, < 2 <sup>22</sup> ms, and >= 2 <sup>22</sup> ms.

The histogram will not be filled unless the `STATISTICS_LEVEL` initialization parameter is set to `ALL`.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | File number |
| `SINGLEBLKRDTIM_MILLI` | `NUMBER` | Amount of time the bucket represents (in milliseconds). If the duration = `num`, then this column represents waits of duration < `num` that are not included in any smaller bucket. |
| `SINGLEBLKRDS` | `NUMBER` | Number of waits of the duration belonging to the bucket of the histogram |