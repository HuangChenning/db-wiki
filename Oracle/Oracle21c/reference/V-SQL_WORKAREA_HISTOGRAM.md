---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_WORKAREA_HISTOGRAM.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.70 V$SQL\_WORKAREA\_HISTOGRAM

`V$SQL_WORKAREA_HISTOGRAM` displays the cumulative work area execution statistics (cumulated since instance startup) for different work area groups. The work areas are split into 33 groups based on their optimal memory requirements with the requirements increasing in powers of two. That is, work areas whose optimal requirement varies from 0 KB to 1 KB, 1 KB to 2 KB, 2 KB to 4 KB,... and 2 TB to 4 TB.

For each work area group, the `V$SQL_WORKAREA_HISTOGRAM` view shows how many work areas in that group were able to run in optimal mode, how many were able to run in one-pass mode, and finally how many ran in multi-pass mode. The DBA can take a snapshot at the beginning and the end of a desired time interval to derive the same statistics for that interval.

| Column | Datatype | Description |
| --- | --- | --- |
| `LOW_OPTIMAL_SIZE` | `NUMBER` | Lower bound for the optimal memory requirement of work areas included in this row (bytes) |
| `HIGH_OPTIMAL_SIZE` | `NUMBER` | Upper bound for the optimal memory requirement of work areas included in this row (bytes) |
| `OPTIMAL_EXECUTIONS` | `NUMBER` | Number of work areas with an optimal memory requirement comprised between `LOW_OPTIMAL_SIZE` and `HIGH_OPTIMAL_SIZE` which have been executed in optimal mode since instance startup |
| `ONEPASS_EXECUTIONS` | `NUMBER` | Number of work areas with an optimal memory requirement comprised between `LOW_OPTIMAL_SIZE` and `HIGH_OPTIMAL_SIZE` which have been executed in one-pass mode since instance startup |
| `MULTIPASSES_EXECUTIONS` | `NUMBER` | Number of work areas with an optimal memory requirement comprised between `LOW_OPTIMAL_SIZE` and `HIGH_OPTIMAL_SIZE` which have been executed in multi-pass mode since instance startup |
| `TOTAL_EXECUTIONS` | `NUMBER` | Sum of `OPTIMAL_EXECUTIONS`, `ONEPASS_EXECUTIONS`, and `MULTIPASSES_EXECUTIONS` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA480) for detailed information on how to monitor automatic PGA memory performance using this view