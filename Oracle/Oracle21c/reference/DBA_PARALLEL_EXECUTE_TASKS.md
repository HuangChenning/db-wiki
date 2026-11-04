---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_PARALLEL_EXECUTE_TASKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.228 DBA\_PARALLEL\_EXECUTE\_TASKS

`DBA_PARALLEL_EXECUTE_TASKS` displays all tasks in the database.

Related View

`USER_PARALLEL_EXECUTE_TASKS` displays the tasks created by the current user. This view does not display the `TASK_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the task |
| `TASK_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the task |
| `CHUNK_TYPE` | `VARCHAR2(12)` |  | Type of parallel update:  - `UNDELARED` - `ROWID_RANGE` - `NUMBER_RANGE` |
| `STATUS` | `VARCHAR2(19)` |  | Status of the task:  - `CREATED` - `CHUNKING` - `CHUNKING_FAILED` - `CHUNKED` - `PROCESSING` - `FINISHED` - `FINISHED_WITH_ERROR` - `CRASHED` |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the table to be chunked |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table to be chunked |
| `NUMBER_COLUMN` | `VARCHAR2(128)` |  | Name of the column holding IDs (only applicable to `NUMBER_RANGE` chunking type) |
| `TASK_COMMENT` | `VARCHAR2(4000)` |  | Comment field |
| `JOB_PREFIX` | `VARCHAR2(128)` |  | Prefix of the job name executing this task |
| `SQL_STMT` | `CLOB` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `LANGUAGE_FLAG` | `NUMBER` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `EDITION` | `VARCHAR2(130)` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `APPLY_CROSSEDITION_TRIGGER` | `VARCHAR2(130)` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `FIRE_APPLY_TRIGGER` | `VARCHAR2(10)` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `PARALLEL_LEVEL` | `NUMBER` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |
| `JOB_CLASS` | `VARCHAR2(128)` |  | Argument used in the previous `DBMS_PARALLEL_EXECUTE.RUN_TASK` |

See Also:

- " [USER\_PARALLEL\_EXECUTE\_TASKS](USER_PARALLEL_EXECUTE_TASKS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS67375) for more information about the `DBMS_PARALLEL_EXECUTE.RUN_TASK` procedure