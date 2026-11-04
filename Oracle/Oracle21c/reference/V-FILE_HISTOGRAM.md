---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FILE_HISTOGRAM.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.227 V$FILE\_HISTOGRAM

`V$FILE_HISTOGRAM` displays a histogram of all synchronous single block reads on a per-file basis (for data files). The histogram has buckets of time intervals from < 1 ms, < 2 ms, < 4 ms, < 8 ms,... < 2 <sup>21</sup> ms, < 2 <sup>22</sup> ms, and >= 2 <sup>22</sup> ms.

The histogram will not be filled unless the `STATISTICS_LEVEL` initialization parameter is set to `ALL`.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | File number |
| `SINGLEBLKRDTIM_MILLI` | `NUMBER` | Amount of time the bucket represents (in milliseconds). If the duration = `num`, then this column represents waits of duration < `num` that are not included in any smaller bucket. |
| `SINGLEBLKRDS` | `NUMBER` | Number of waits of the duration belonging to the bucket of the histogram |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |