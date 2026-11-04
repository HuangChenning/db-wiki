---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_PLAN_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.61 V$SQL\_PLAN\_STATISTICS

`V$SQL_PLAN_STATISTICS` provides execution statistics at the row source level for each child cursor.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the handle to the parent for this cursor |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent statement in the library cache. The two columns `ADDRESS` and `HASH_VALUE` can be used to join with `V$SQLAREA` to locate the parent cursor. |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent statement in the library cache |
| `PLAN_HASH_VALUE` | `NUMBER` | Numerical representation of the current SQL plan for this cursor. Comparing one `PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line by line) |
| `FULL_PLAN_HASH_VALUE` | `NUMBER` | Numeric representation of the complete SQL plan for this cursor. Comparing one `FULL_PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line by line). Note that the `FULL_PLAN_HASH_VALUE` cannot be compared across databases releases. It is not backward compatible. |
| `CHILD_ADDRESS` | `RAW(4 \| 8)` | Address of the child cursor |
| `CHILD_NUMBER` | `NUMBER` | Number of the child cursor that uses this work area. The columns `ADDRESS`, `HASH_VALUE`, and `CHILD_NUMBER` can be used to join with `V$SQL` to locate the child cursor using this area. |
| `OPERATION_ID` | `NUMBER` | A number assigned to each step in the execution plan |
| `EXECUTIONS` | `NUMBER` | Number of times this cursor has been executed |
| `LAST_STARTS` | `NUMBER` | Number of times this operation has been started, during the last execution |
| `STARTS` | `NUMBER` | Number of times this operation has been started, accumulated over the past executions |
| `LAST_OUTPUT_ROWS` | `NUMBER` | Number of rows produced by the row source, during the last execution |
| `OUTPUT_ROWS` | `NUMBER` | Number of rows produced by the row source, accumulated over the past executions |
| `LAST_CR_BUFFER_GETS` | `NUMBER` | Number of buffers retrieved in consistent mode, during the last execution. Buffers are usually retrieved in consistent mode for queries. |
| `CR_BUFFER_GETS` | `NUMBER` | Number of buffers retrieved in consistent mode, accumulated over the past executions. Buffers are usually retrieved in consistent mode for queries. |
| `LAST_CU_BUFFER_GETS` | `NUMBER` | Number of buffers retrieved in current mode, during the last execution. Buffers are retrieved in current mode for statements such as `INSERT`, `UPDATE`, and `DELETE`. |
| `CU_BUFFER_GETS` | `NUMBER` | Number of buffers retrieved in current mode, accumulated over the past executions. Buffers are retrieved in current mode for statements such as `INSERT`, `UPDATE`, and `DELETE`. |
| `LAST_DISK_READS` | `NUMBER` | Number of physical disk reads performed by the operation, during the last execution |
| `DISK_READS` | `NUMBER` | Number of physical disk reads performed by the operation, accumulated over the past executions |
| `LAST_DISK_WRITES` | `NUMBER` | Number of physical disk writes performed by the operation, during the last execution |
| `DISK_WRITES` | `NUMBER` | Number of physical disk writes performed by the operation, accumulated over the past executions |
| `LAST_ELAPSED_TIME` | `NUMBER` | Elapsed time (in microseconds) corresponding to this operation, during the last execution |
| `ELAPSED_TIME` | `NUMBER` | Elapsed time (in microseconds) corresponding to this operation, accumulated over the past executions |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SQLAREA](V-SQLAREA.md) "