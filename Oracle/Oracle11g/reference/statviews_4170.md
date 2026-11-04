---
title: DBA_PARALLEL_EXECUTE_CHUNKS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4170.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_PARALLEL_EXECUTE_CHUNKS` displays the chunks for all tasks in the database.

Related View

`USER_PARALLEL_EXECUTE_CHUNKS` displays the chunks for tasks created by the current user. This view does not display the `TASK_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CHUNK_ID` | `NUMBER` | `NOT NULL` | Unique ID for the chunk |
| `TASK_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the task |
| `TASK_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the task |
| `STATUS` | `VARCHAR2(20)` |  | Status of the chunk: - `UNASSIGNED` - `ASSIGNED` - `PROCESSED` - `PROCESSED_WITH_ERROR` |
| `START_ROWID` | `ROWID` |  | Rowid for the first row in the chunk |
| `END_ROWID` | `ROWID` |  | Rowid for the last row in the chunk |
| `START_ID` | `NUMBER` |  | Number column value of the first row in the chunk |
| `END_ID` | `NUMBER` |  | Number column value of the last row in the chunk |
| `JOB_NAME` | `VARCHAR2(30)` |  | Name of the job which processed this chunk |
| `START_TS` | `TIMESTAMP(6)` |  | Processing start time for the chunk |
| `END_TS` | `TIMESTAMP(6)` |  | Processing end time for the chunk |
| `ERROR_CODE` | `NUMBER` |  | Error code returned during the execution of the chunk if the `STATUS` column is `PROCESSED_WITH_ERROR` |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message returned during the execution of the chunk if the `STATUS` column is `PROCESSED_WITH_ERROR` |

See Also:

["USER\_PARALLEL\_EXECUTE\_CHUNKS"](statviews_5385.md)