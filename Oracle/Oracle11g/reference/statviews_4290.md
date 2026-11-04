---
title: DBA_SQLTUNE_STATISTICS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4290.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SQLTUNE_STATISTICS` displays statistics associated with all SQL statements in the database.

Related View

`USER_SQLTUNE_STATISTICS` displays statistics associated with the SQL statements owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER(38)` | `NOT NULL` | Tuning task identifier |
| `OBJECT_ID` | `NUMBER(38)` | `NOT NULL` | Advisor framework object identifier |
| `PARSING_SCHEMA_ID` | `NUMBER` |  | Schema under which the SQL is parsed |
| `MODULE` <sup>Foot 1</sup> | `VARCHAR2(48)` |  | Last application module recorded for the SQL |
| `ACTION` <sup>Footref 1</sup> | `VARCHAR2(32)` |  | Last application action recorded for the SQL |
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
| `OPTIMIZER_ENV` | `RAW(1000)` |  | Optimizer environment |
| `COMMAND_TYPE` | `NUMBER` |  | Command type |

<sup>Footnote 1</sup> The datatype of this column is `VARCHAR2(64)` starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

["USER\_SQLTUNE\_STATISTICS"](statviews_5461.md)