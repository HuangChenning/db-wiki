---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SQLTUNE_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.383 DBA\_SQLTUNE\_STATISTICS

`DBA_SQLTUNE_STATISTICS` displays statistics associated with all SQL statements in the database.

Related View

`USER_SQLTUNE_STATISTICS` displays statistics associated with the SQL statements owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER(38)` | `NOT NULL` | Tuning task identifier |
| `OBJECT_ID` | `NUMBER(38)` | `NOT NULL` | Advisor framework object identifier |
| `PARSING_SCHEMA_ID` | `NUMBER` |  | Schema under which the SQL is parsed |
| `MODULE` | `VARCHAR2(64)` |  | Last application module recorded for the SQL |
| `ACTION` | `VARCHAR2(64)` |  | Last application action recorded for the SQL |
| `ELAPSED_TIME` | `NUMBER` |  | Elapsed time for the SQL statement |
| `CPU_TIME` | `NUMBER` |  | CPU time for the SQL |
| `BUFFER_GETS` | `NUMBER` |  | Number of buffer gets |
| `DISK_READS` | `NUMBER` |  | Number of disk reads |
| `DIRECT_WRITES` | `NUMBER` |  | Number of disk writes |
| `ROWS_PROCESSED` | `NUMBER` |  | Number of rows processed by the SQL |
| `FETCHES` | `NUMBER` |  | Number of fetches |
| `EXECUTIONS` | `NUMBER` |  | Number of executions |
| `END_OF_FETCH_COUNT` | `NUMBER` |  | End of fetch count |
| `OPTIMIZER_COST` | `NUMBER` |  | Optimizer cost for the SQL |
| `OPTIMIZER_ENV` | `RAW(2000)` |  | Optimizer environment |
| `COMMAND_TYPE` | `NUMBER` |  | Command type |

See Also:

" [USER\_SQLTUNE\_STATISTICS](USER_SQLTUNE_STATISTICS.md) "