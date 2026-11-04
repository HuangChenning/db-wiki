---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_WORKAREA.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.68 V$SQL\_WORKAREA

Each SQL statement stored in the shared pool has one or more child cursors that are listed in the `V$SQL` view. `V$SQL_WORKAREA` lists all work areas needed by these child cursors; `V$SQL_WORKAREA` can be joined with `V$SQLAREA` on (`ADDRESS`, `HASH_VALUE`) and with `V$SQL` on (`ADDRESS`, `HASH_VALUE`, `CHILD_NUMBER`).

You can use this view to find out answers to the following questions:

- What are the top 10 work areas that require the most cache area?
- For work areas allocated in `AUTO` mode, what percentage of work areas are running using maximum memory?

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the parent cursor handle |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent statement in the library cache. Two columns `PARENT_HANDLE` and `HASH_VALUE` can be used to join with `V$SQLAREA` to locate the parent cursor. |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent statement in the library cache |
| `CHILD_NUMBER` | `NUMBER` | Number of the child cursor that uses this work area. The columns `PARENT_HANDLE`, `HASH_VALUE`, and `CHILD_NUMBER` can be used to join with `V$SQL` to locate the child cursor using this area. |
| `WORKAREA_ADDRESS` | `RAW(4 \| 8)` | Address of the work area handle. This is the primary key for the view. |
| `OPERATION_TYPE` | `VARCHAR2(160)` | Type of operation using the work area. Can include values such as `SORT`, `HASH JOIN`, `GROUP BY`, `BUFFER`, `BITMAP MERGE`, and `BITMAP CONSTRUCTION`. |
| `OPERATION_ID` | `NUMBER` | A unique number used to identify the operation in the execution plan. This identifier can be joined to `V$SQL_PLAN` to locate the operation that uses this work area. |
| `POLICY` | `VARCHAR2(40)` | Sizing policy for this work area (`MANUAL` or `AUTO`) |
| `ESTIMATED_OPTIMAL_SIZE` | `NUMBER` | Estimated size (in bytes) required by this work area to execute the operation completely in memory (optimal execution). Derived from either optimizer statistics or previous executions. |
| `ESTIMATED_ONEPASS_SIZE` | `NUMBER` | Estimated size (in bytes) required by this work area to execute the operation in a single pass. Derived from either optimizer statistics or previous executions. |
| `LAST_MEMORY_USED` | `NUMBER` | Memory (in bytes) used by this work area during the last execution of the cursor |
| `LAST_EXECUTION` | `VARCHAR2(40)` | Indicates whether this work area runs using `OPTIMAL, ONE PASS`, or `ONE PASS` memory requirement (or `MULTI-PASS`), during the last execution of the cursor |
| `LAST_DEGREE` | `NUMBER` | Degree of parallelism used during the last execution of this operation |
| `TOTAL_EXECUTIONS` | `NUMBER` | Number of times this work area was active |
| `OPTIMAL_EXECUTIONS` | `NUMBER` | Number of times this work area ran in optimal mode |
| `ONEPASS_EXECUTIONS` | `NUMBER` | Number of times this work area ran in one-pass mode |
| `MULTIPASSES_EXECUTIONS` | `NUMBER` | Number of times this work area ran below the one-pass memory requirement |
| `ACTIVE_TIME` | `NUMBER` | Average time this work area is active (in hundredths of a second) |
| `MAX_TEMPSEG_SIZE` | `NUMBER` | Maximum temporary segment size (in bytes) created by an instantiation of this work area. This column is NULL if this work area has never spilled to disk. |
| `LAST_TEMPSEG_SIZE` | `NUMBER` | Temporary segment size (in bytes) created in the last instantiation of this work area. This column is NULL if the last instantiation of this work area did not spill to disk. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$SQLAREA](V-SQLAREA.md) "
- " [V$SQL](V-SQL.md) "