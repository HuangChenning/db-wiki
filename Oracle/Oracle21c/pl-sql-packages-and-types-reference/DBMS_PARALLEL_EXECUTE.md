---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_PARALLEL_EXECUTE.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 127 DBMS\_PARALLEL\_EXECUTE

The `DBMS_PARALLEL_EXECUTE` package enables incremental update of table data in parallel.

This chapter contains the following topics:

See Also:

- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADFNS020)
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN-GUID-AEFFCE5D-AB5B-4EE1-9CB3-4491F3D3D0E7)

### 127.1 DBMS\_PARALLEL\_EXECUTE Overview

This package lets you incrementally update table data in parallel, in two high-level steps.

1. Group sets of rows in the table into smaller-sized chunks.
2. Run a user-specified statement on these chunks in parallel, and commit when finished processing each chunk.

This package introduces the notion of parallel execution task. This task groups the various steps associated with the parallel execution of a PL/SQL block, which is typically updating table data.

All of the package subroutines (except the GENERATE\_TASK\_NAME Function and the TASK\_STATUS Procedure) perform a commit.

### 127.2 DBMS\_PARALLEL\_EXECUTE Security Model

`DBMS_PARALLEL_EXECUTE` is a `SYS` -owned package which is granted to `PUBLIC`.

Users who have the `ADM_PARALLEL_EXECUTE_TASK` role can perform administrative routines (qualified by the prefix `ADM_`) and access the DBA view.

Apart from the administrative routines, all the subprograms refer to tasks owned by the current user.

To execute chunks in parallel, you must have `CREATE` `JOB` system privilege.

The `CHUNK_BY_SQL`, `RUN_TASK`, and `RESUME_TASK` subprograms require a query, and are executed using `DBMS_SQL`. Invokers of the `DBMS_SQL` interface must ensure that no query contains SQL injection.

### 127.3 DBMS\_PARALLEL\_EXECUTE Constants

The `DBMS_PARALLEL_EXECUTE` package uses the constants described in these two tables.

Table 127-1 DBMS\_PARALLEL\_EXECUTE Constants - Chunk Status Value

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `ASSIGNED` | `NUMBER` | 1 | Chunk has been assigned for processing |
| `PROCESSED` | `NUMBER` | 2 | Chunk has been processed successfully |
| `PROCESSED_WITH_ERROR` | `NUMBER` | 3 | Chunk has been processed, but an error occurred during processing |
| `UNASSIGNED` | `NUMBER` | 0 | Chunk is unassigned |

Table 127-2 DBMS\_PARALLEL\_EXECUTE Constants - Task Status Value

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `CHUNKED` | `NUMBER` | 5 | Table associated with the task has been chunked, but none of the chunk has been assigned for processing |
| `CHUNKING` | `NUMBER` | 2 | Table associated with the task is being chunked |
| `CHUNKING_FAILED` | `NUMBER` | 3 | Chunking failed |
| `CRASHED` | `NUMBER` | 9 | Only applicable if parallel execution is used, this occurs if a job slave crashes or if the database crashes during `EXECUTE`, leaving a chunk in `ASSIGNED` or `UNASSIGNED` state. |
| `CREATED` | `NUMBER` | 1 | The task has been created by the `CREATE_TASK Procedure` |
| `FINISHED` | `NUMBER` | 7 | All chunks processed without error |
| `FINISHED_WITH_ERROR` | `NUMBER` | 8 | All chunks processed, but with errors in some cases |
| `NO_CHUNKS` | `NUMBER` | 4 | Table associated with the task has no chunks created |
| `PROCESSING` | `NUMBER` | 6 | Part of the chunk assigned for processing, or which has been processed |

Note:

Use constants instead of absolute values, because absolute values might change in future.

### 127.5 DBMS\_PARALLEL\_EXECUTE Exceptions

The following table lists the exceptions raised by `DBMS_PARALLEL_EXECUTE`.

Table 127-3 Exceptions Raised by DBMS\_PARALLEL\_EXECUTE

| Exception | Error Code | Description |
| --- | --- | --- |
| `CHUNK_NOT_FOUND` | 29499 | Specified chunk does not exist |
| `DUPLICATE_TASK_NAME` | 29497 | Same task name has been used by an existing task |
| `INVALID_STATE_FOR_CHUNK` | 29492 | Attempts to chunk a table that is not in `CREATED` or `CHUNKING_FAILED` state |
| `INVALID_STATE_FOR_REDSUME` | 29495 | Attempts to resume execution, but the task is not in `FINISHED_WITH_ERROR` or `CRASHED` state |
| `INVALID_STATE_FOR_RUN` | 29494 | Attempts to execute the task that is not in `CHUNKED` state |
| `INVALID_STATUS` | 29493 | Attempts to set an invalid value to the chunk status |
| `INVALID_TABLE` | 29491 | Attempts to chunk a table by rowid in cases in which the table is not a physical table, or the table is an IOT |
| `MISSING_ROLE` | 29490 | User does not have the necessary `ADM_PARALLEL_EXECUTE` role |
| `TASK_NOT_FOUND` | 29498 | Specified `task_name` does not exist |

### 127.6 DBMS\_PARALLEL\_EXECUTE Examples

The following examples run on the Human Resources (HR) schema of the Oracle Database Sample Schemas. They requires that the HR schema be created with the `JOB` `SYSTEM` privilege.

Chunk by ROWID

This example shows the most common usage of this package. After calling the RUN\_TASK Procedure, it checks for errors and reruns in the case of error.

```
DECLARE
  l_sql_stmt VARCHAR2(1000);
  l_try NUMBER;
  l_status NUMBER;
BEGIN
 
  -- Create the TASK
  DBMS_PARALLEL_EXECUTE.CREATE_TASK ('mytask');
 
  -- Chunk the table by ROWID
  DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_ROWID('mytask', 'HR', 'EMPLOYEES', true, 100);
 
  -- Execute the DML in parallel
  l_sql_stmt := 'update EMPLOYEES e 
      SET e.salary = e.salary + 10
      WHERE rowid BETWEEN :start_id AND :end_id';
  DBMS_PARALLEL_EXECUTE.RUN_TASK('mytask', l_sql_stmt, DBMS_SQL.NATIVE,
                                 parallel_level => 10);
 
  -- If there is an error, RESUME it for at most 2 times.
  L_try := 0;
  L_status := DBMS_PARALLEL_EXECUTE.TASK_STATUS('mytask');
  WHILE(l_try < 2 and L_status != DBMS_PARALLEL_EXECUTE.FINISHED) 
  LOOP
    L_try := l_try + 1;
    DBMS_PARALLEL_EXECUTE.RESUME_TASK('mytask');
    L_status := DBMS_PARALLEL_EXECUTE.TASK_STATUS('mytask');
  END LOOP;
 
  -- Done with processing; drop the task
  DBMS_PARALLEL_EXECUTE.DROP_TASK('mytask');
   
END;
/
```

Chunk by User-Provided SQL

A user can specify a chunk algorithm by using the CREATE\_CHUNKS\_BY\_SQL Procedure. This example shows that rows with the same `manager_id` are grouped together and processed in one chunk.

```
DECLARE
  l_chunk_sql VARCHAR2(1000);
  l_sql_stmt VARCHAR2(1000);
  l_try NUMBER;
  l_status NUMBER;
BEGIN
 
  -- Create the TASK
  DBMS_PARALLEL_EXECUTE.CREATE_TASK ('mytask');
 
  -- Chunk the table by MANAGER_ID
  l_chunk_sql := 'SELECT distinct manager_id, manager_id FROM employees';
  DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_SQL('mytask', l_chunk_sql, false);
 
  -- Execute the DML in parallel
  --   the WHERE clause contain a condition on manager_id, which is the chunk
  --   column. In this case, grouping rows is by manager_id.
  l_sql_stmt := 'update EMPLOYEES e 
      SET e.salary = e.salary + 10
      WHERE manager_id between :start_id and :end_id';
  DBMS_PARALLEL_EXECUTE.RUN_TASK('mytask', l_sql_stmt, DBMS_SQL.NATIVE,
                                  parallel_level => 10);
 
  -- If there is error, RESUME it for at most 2 times.
  L_try := 0;
  L_status := DBMS_PARALLEL_EXECUTE.TASK_STATUS('mytask');
  WHILE(l_try < 2 and L_status != DBMS_PARALLEL_EXECUTE.FINISHED) 
  Loop
    L_try := l_try + 1;
    DBMS_PARALLEL_EXECUTE.RESUME_TASK('mytask');
    L_status := DBMS_PARALLEL_EXECUTE.TASK_STATUS('mytask');
  END LOOP;
 
  -- Done with processing; drop the task
  DBMS_PARALLEL_EXECUTE.DROP_TASK('mytask');
 
end;
/
```

Executing Chunks in an User-defined Framework

You can execute chunks in a self-defined framework without using the RUN\_TASK Procedure. This example shows how to use GET\_ROWID\_CHUNK Procedure, `EXECUTE` `IMMEDIATE`, SET\_CHUNK\_STATUS Procedure to execute the chunks.

```
DECLARE
  l_sql_stmt varchar2(1000);
  l_try number;
  l_status number;
  l_chunk_id number;
  l_start_rowid rowid;
  l_end_rowid rowid;
  l_any_rows boolean;
  CURSOR c1 IS SELECT chunk_id
               FROM user_parallel_execute_chunks
               WHERE task_name = 'mytask'
                 AND STATUS IN (DBMS_PARALLEL_EXECUTE.PROCESSED_WITH_ERROR,
                                DBMS_PARALLEL_EXECUTE.ASSIGNED);
BEGIN
 
  -- Create the Objects, task, and chunk by ROWID
  DBMS_PARALLEL_EXECUTE.CREATE_TASK ('mytask');
  DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_ROWID('mytask', 'HR', 'EMPLOYEES', true, 100);
 
  l_sql_stmt := 'update EMPLOYEES e 
      SET e.salary = e.salary + 10
      WHERE rowid BETWEEN :start_id AND :end_id';
 
  -- Execute the DML in his own framework 
  --
  -- Process each chunk and commit.
  -- After processing one chunk, repeat this process until
  -- all the chunks are processed.
  --
  <<main_processing>>
  LOOP
      --
      -- Get a chunk to process; if there is nothing to process, then exit the 
      -- loop;
      --
      DBMS_PARALLEL_EXECUTE.GET_ROWID_CHUNK('mytask',
                                                          l_chunk_id,
                                                          l_start_rowid,
                                                          l_end_rowid,
                                                          l_any_rows);
      IF (l_any_rows = false) THEN EXIT; END IF;
 
      --
      -- The chunk is specified by start_id and end_id.
      -- Bind the start_id and end_id and then execute it
      --
      -- If no error occured, set the chunk status to PROCESSED.
      --
      -- Catch any exception. If an exception occured, store the error num/msg
      -- into the chunk table and then continue to process the next chunk.
      -- 
      BEGIN
        EXECUTE IMMEDIATE l_sql_stmt using l_start_rowid, l_end_rowid;
        DBMS_PARALLEL_EXECUTE.SET_CHUNK_STATUS('mytask',l_chunk_id,
          DBMS_PARALLEL_EXECUTE.PROCESSED);
      EXCEPTION WHEN OTHERS THEN
        DBMS_PARALLEL_EXECUTE.SET_CHUNK_STATUS('mytask', l_chunk_id,
          DBMS_PARALLEL_EXECUTE.PROCESSED_WITH_ERROR, SQLCODE, SQLERRM);
      END;
 
      --
      -- Finished processing one chunk; Commit here
      --
      COMMIT;
  END LOOP;
```

### 127.7 Summary of DBMS\_PARALLEL\_EXECUTE Subprograms

This table lists the `DBMS_PARALLEL_EXECUTE` subprograms and briefly describes them.

Table 127-4 DBMS\_PARALLEL\_EXECUTE Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADM\_DROP\_CHUNKS Procedure | Drops all chunks of the specified task owned by the specified owner |
| ADM\_DROP\_TASK Procedure | Drops the task of the given user and all related chunks |
| ADM\_TASK\_STATUS Function | Returns the task status |
| ADM\_STOP\_TASK Procedure | Stops the task of the given owner and related job slaves |
| CREATE\_TASK Procedure | Creates a task for the current user |
| CREATE\_CHUNKS\_BY\_NUMBER\_COL Procedure | Chunks the table associated with the given task by the specified column. |
| CREATE\_CHUNKS\_BY\_ROWID Procedure | Chunks the table associated with the given task by `ROWID` |
| CREATE\_CHUNKS\_BY\_SQL Procedure | Chunks the table associated with the given task by means of a user-provided `SELECT` statement |
| DROP\_TASK Procedure | Drops the task and all related chunks |
| DROP\_CHUNKS Procedure | Drops the task's chunks |
| GENERATE\_TASK\_NAME Function | Returns a unique name for a task |
| GET\_NUMBER\_COL\_CHUNK Procedure | Picks an unassigned `NUMBER` chunk and changes it to `ASSIGNED` |
| GET\_ROWID\_CHUNK Procedure | Picks an unassigned `ROWID` chunk and changes it to `ASSIGNED` |
| PURGE\_PROCESSED\_CHUNKS Procedure | Deletes all the processed chunks whose status is `PROCESSED` or `PROCESSED_WITH_ERROR` |
| RESUME\_TASK Procedures | Retries the given the task if the RUN\_TASK Procedure finished with an error, or resumes the task if a crash occurred. |
| RUN\_TASK Procedure | Executes the specified SQL statement on the chunks in parallel |
| SET\_CHUNK\_STATUS Procedure | Sets the status of the chunk |
| STOP\_TASK Procedure | Stops the task and related job slaves |
| TASK\_STATUS Procedure | Returns the task status |

#### 127.7.1 ADM\_DROP\_CHUNKS Procedure

This procedure drops all chunks of the specified task owned by the specified owner.

Syntax

```
DBMS_PARALLEL_EXECUTE.ADM_DROP_CHUNKS (
   task_owner      IN  VARCHAR2,
   task_name       IN  VARCHAR2);
```

Parameters

Table 127-5 ADM\_DROP\_CHUNKS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_owner` | Owner of the task |
| `task_name` | Name of the task |

#### 127.7.2 ADM\_DROP\_TASK Procedure

This procedure drops the task of the specified user and all related chunks.

Syntax

```
DBMS_PARALLEL_EXECUTE.ADM_DROP_TASK (
   task_owner      IN  VARCHAR2,
   task_name       IN  VARCHAR2);
```

Parameters

Table 127-6 ADM\_DROP\_TASK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_owner` | Owner of the task |
| `task_name` | Name of the task |

#### 127.7.3 ADM\_TASK\_STATUS Function

This function returns the task status.

Syntax

```
DBMS_PARALLEL_EXECUTE.ADM_TASK_STATUS  (
   task_owner      IN  VARCHAR2,
   task_name       IN  VARCHAR2)
 RETURN NUMBER;
```

Parameters

Table 127-7 ADM\_TASK\_STATUS Function Parameters

| Parameter | Description |
| --- | --- |
| `task_owner` | Owner of the task |
| `task_name` | Name of the task |

#### 127.7.4 ADM\_STOP\_TASK Procedure

This procedure stops the task of the specified owner and related job slaves.

Syntax

```
DBMS_PARALLEL_EXECUTE.ADM_STOP_TASK (
   task_owner      IN  VARCHAR2,
   task_name       IN  VARCHAR2);
```

Parameters

Table 127-8 ADM\_STOP\_TASK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_owner` | Owner of the task |
| `task_name` | Name of the task |

#### 127.7.5 CREATE\_TASK Procedure

This procedure creates a task for the current user. The pairing of `task_name` and `current_user` must be unique.

Syntax

```
DBMS_PARALLEL_EXECUTE.CREATE_TASK (
   task_name        IN   VARCHAR2,
   comment          IN   VARCHAR2 DEFAULT NULL);
```

Parameters

Table 127-9 CREATE\_TASK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task. The task\_name can be any string in which related length must be less than or equal to 128 bytes. |