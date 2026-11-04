---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SESSION_LONGOPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.23 V$SESSION\_LONGOPS

`V$SESSION_LONGOPS` displays the status of various operations that run for longer than 6 seconds (in absolute time). These operations currently include many backup and recovery functions, statistics gathering, and query execution, and more operations are added for every Oracle release.

To monitor query execution progress, you must be using the cost-based optimizer and you must:

- Set the `TIMED_STATISTICS` or `SQL_TRACE` parameters to `true`
- Gather statistics for your objects with the `DBMS_STATS` package

You can add information to this view about application-specific long-running operations by using the `DBMS_APPLICATION_INFO.SET_SESSION_LONGOPS ` procedure.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Identifier of the session processing the long-running operation. If multiple sessions are cooperating in the long-running operation, then `SID` corresponds to the main session. |
| `SERIAL#` | `NUMBER` | Serial number of the session processing the long-running operation. If multiple sessions are cooperating in the long-running operation, then `SERIAL#` corresponds to the main session. `SERIAL#` is used to uniquely identify a session's objects. Guarantees that session-level commands are applied to the correct session objects if the session ends and another session begins with the same session ID. |
| `OPNAME` | `VARCHAR2(64)` | Brief description of the operation |
| `TARGET` | `VARCHAR2(64)` | Object on which the operation is carried out |
| `TARGET_DESC` | `VARCHAR2(32)` | Description of the target |
| `SOFAR` | `NUMBER` | Units of work done so far for the operation specified in the `OPNAME` column |
| `TOTALWORK` | `NUMBER` | Total units of work for the operation specified in the `OPNAME` column |
| `UNITS` | `VARCHAR2(32)` | Units of measurement |
| `START_TIME` | `DATE` | Starting time of the operation |
| `LAST_UPDATE_TIME` | `DATE` | Time when statistics were last updated for the operation |
| `TIMESTAMP` | `DATE` | Timestamp specific to the operation |
| `TIME_REMAINING` | `NUMBER` | Estimate (in seconds) of time remaining for the operation to complete |
| `ELAPSED_SECONDS` | `NUMBER` | Number of elapsed seconds from the start of the operations |
| `CONTEXT` | `NUMBER` | Context |
| `MESSAGE` | `VARCHAR2(512)` | Statistics summary message |
| `USERNAME` | `VARCHAR2(30)` | User ID of the user performing the operation |
| `SQL_ADDRESS` | `RAW(4 \| 8)` | Used with the value of the `SQL_HASH_VALUE` column to identify the SQL statement associated with the operation |
| `SQL_HASH_VALUE` | `NUMBER` | Used with the value of the `SQL_ADDRESS` column to identify the SQL statement associated with the operation |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the SQL statement associated with the long operation, if any |
| `SQL_PLAN_HASH_VALUE` | `NUMBER` | SQL plan hash value; NULL if `SQL_ID` is NULL |
| `SQL_EXEC_START` | `DATE` | Time when the execution of the SQL started; NULL if `SQL_ID` is NULL |
| `SQL_EXEC_ID` | `NUMBER` | SQL execution identifier (see `V$SQL_MONITOR`) |
| `SQL_PLAN_LINE_ID` | `NUMBER` | SQL plan line ID corresponding to the long operation; NULL if the long operation is not associated with a line of the execution plan |
| `SQL_PLAN_OPERATION` | `VARCHAR2(30)` | Plan operation name; NULL if `SQL_PLAN_LINE_ID` is NULL |
| `SQL_PLAN_OPTIONS` | `VARCHAR2(30)` | Plan operation options; NULL if `SQL_PLAN_LINE_ID` is NULL |
| `QCSID` | `NUMBER` | Session identifier of the parallel coordinator |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [TIMED\_STATISTICS](TIMED_STATISTICS.md) "
- " [SQL\_TRACE](SQL_TRACE.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65241) for more information about the `DBMS_APPLICATION_INFO.SET_SESSION_LONGOPS` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS059) for more information about the `DBMS_STATS` package