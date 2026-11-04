---
title: "V$SQL_WORKAREA"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3061.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_WORKAREA` displays information about work areas used by SQL cursors. Each SQL statement stored in the shared pool has one or more child cursors that are listed in the `V$SQL` view. `V$SQL_WORKAREA` lists all work areas needed by these child cursors; `V$SQL_WORKAREA` can be joined with `V$SQLAREA` on (`ADDRESS`, `HASH_VALUE`) and with `V$SQL` on (`ADDRESS`, `HASH_VALUE`, `CHILD_NUMBER`).

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
| `OPERATION_TYPE` | `VARCHAR2(20)` | Type of operation using the work area (`SORT`, `HASH JOIN`, `GROUP BY`, `BUFFERING`, `BITMAP MERGE`, or `BITMAP CREATE`) |
| `OPERATION_ID` | `NUMBER` | A unique number used to identify the operation in the execution plan. This identifier can be joined to `V$SQL_PLAN` to locate the operation that uses this work area. |
| `POLICY` | `VARCHAR2(10)` | Sizing policy for this work area (`MANUAL` or `AUTO`) |
| `ESTIMATED_OPTIMAL_SIZE` | `NUMBER` | Estimated size (in bytes) required by this work area to execute the operation completely in memory (optimal execution). Derived from either optimizer statistics or previous executions. |
| `ESTIMATED_ONEPASS_SIZE` | `NUMBER` | Estimated size (in bytes) required by this work area to execute the operation in a single pass. Derived from either optimizer statistics or previous executions. |
| `LAST_MEMORY_USED` | `NUMBER` | Memory (in bytes) used by this work area during the last execution of the cursor |
| `LAST_EXECUTION` | `VARCHAR2(10)` | Indicates whether this work area runs using `OPTIMAL, ONE PASS`, or `ONE PASS` memory requirement (or `MULTI-PASS`), during the last execution of the cursor |
| `LAST_DEGREE` | `NUMBER` | Degree of parallelism used during the last execution of this operation |
| `TOTAL_EXECUTIONS` | `NUMBER` | Number of times this work area was active |
| `OPTIMAL_EXECUTIONS` | `NUMBER` | Number of times this work area ran in optimal mode |
| `ONEPASS_EXECUTIONS` | `NUMBER` | Number of times this work area ran in one-pass mode |
| `MULTIPASSES_EXECUTIONS` | `NUMBER` | Number of times this work area ran below the one-pass memory requirement |
| `ACTIVE_TIME` | `NUMBER` | Average time this work area is active (in hundredths of a second) |
| `MAX_TEMPSEG_SIZE` | `NUMBER` | Maximum temporary segment size (in bytes) created by an instantiation of this work area. This column is NULL if this work area has never spilled to disk. |
| `LAST_TEMPSEG_SIZE` | `NUMBER` | Temporary segment size (in bytes) created in the last instantiation of this work area. This column is NULL if the last instantiation of this work area did not spill to disk. |