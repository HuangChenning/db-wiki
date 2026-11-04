---
title: DBA_PARALLEL_EXECUTE_TASKS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4171.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_PARALLEL_EXECUTE_TASKS` displays all tasks in the database.

Related View

`USER_PARALLEL_EXECUTE_TASKS` displays the tasks created by the current user. This view does not display the `TASK_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the task |
| `TASK_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the task |
| `CHUNK_TYPE` | `VARCHAR2(12)` |  | Type of parallel update: |
| `STATUS` | `VARCHAR2(19)` |  | Status of the task: - `CREATED` - `CHUNKING` - `CHUNKING_FAILED` - `CHUNKED` - `PROCESSING` - `FINISHED` - `FINISHED_WITH_ERROR` - `CRASHED` |
| `TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the table to be chunked |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table to be chunked |
| `NUMBER_COLUMN` | `VARCHAR2(30)` |  | Name of the column holding IDs (only applicable to `NUMBER_RANGE` chunking type) |
| `TASK_COMMENT` | `VARCHAR2(4000)` |  | Comment field |
| `JOB_PREFIX` | `VARCHAR2(30)` |  | Prefix of the job name executing this task |
| `SQL_STMT` | `CLOB` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `LANGUAGE_FLAG` | `NUMBER` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `EDITION` | `VARCHAR2(30)` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `APPLY_CROSSEDITION_TRIGGER` | `VARCHAR2(30)` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `FIRE_APPLY_TRIGGER` | `VARCHAR2(10)` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `PARALLEL_LEVEL` | `NUMBER` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `JOB_CLASS` | `VARCHAR2(30)` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |

See Also:

["USER\_PARALLEL\_EXECUTE\_TASKS"](statviews_5386.md)