---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-WORKLOAD_REPLAY_THREAD.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.135 V$WORKLOAD\_REPLAY\_THREAD

`V$WORKLOAD_REPLAY_THREAD` displays information for all the different types of replay sessions.

| Column | Datatype | Description |
| --- | --- | --- |
| `CLOCK` | `NUMBER` | Current simulated SCN based on the SCN recorded at capture time |
| `NEXT_TICKER` | `NUMBER` | Next stream ID that will increment the `CLOCK` after a commit action |
| `SID` | `NUMBER` | Session ID of the replay session |
| `SERIAL#` | `NUMBER` | Session serial number of the replay session |
| `SPID` | `VARCHAR2(24)` | The server process ID of the replay session |
| `LOGON_USER` | `VARCHAR2(128)` | Logon username of the replay session |
| `LOGON_TIME` | `DATE` | Logon time of the replay session |
| `EVENT` | `VARCHAR2(64)` | Event name |
| `EVENT_ID` | `NUMBER` | Event identifier |
| `EVENT#` | `NUMBER` | Event operation code |
| `P1TEXT` | `VARCHAR2(64)` | Text for event parameter 1 |
| `P1` | `NUMBER` | Value of event parameter 1 |
| `P2TEXT` | `VARCHAR2(64)` | Text for event parameter 2 |
| `P2` | `NUMBER` | Value of event parameter 2 |
| `P3TEXT` | `VARCHAR2(64)` | Text for event parameter 3 |
| `P3` | `NUMBER` | Value of event parameter 3 |
| `WAIT_FOR_SCN` | `NUMBER` | The captured SCN for which the current user call should wait |
| `FILE_ID` | `NUMBER` | The stream ID that is being replayed |
| `CALL_COUNTER` | `NUMBER` | The call counter of the user call that is being replayed |
| `DEPENDENT_SCN` | `NUMBER` | The dependent SCN, captured to order the commit actions using block-level dependencies |
| `STATEMENT_SCN` | `NUMBER` | Statement SCN |
| `COMMIT_WAIT_SCN` | `NUMBER` | The (maximum) SCN that the current commit should wait for |
| `POST_COMMIT_SCN` | `NUMBER` | The next SCN after the current commit |
| `ACTION_TYPE` | `NUMBER` | The type of commits. The possible values are: `COMMIT`, `ROLLBACK`, `FAKED_` `COMMIT`, and `NULL`. A value of `NULL` means it is not a commit operation. |
| `SESSION_TYPE` | `VARCHAR2(13)` | The type of replay session:  `LOGON`  `ADMIN`  `DISPATCHER`  `REPLAY` |
| `WRC_ID` | `NUMBER` | Unique replay client ID assigned by the server to all participating replay clients when replay starts |
| `SCHEDULE_CAP_ID` | `NUMBER` | An unique identifier for a workload capture added to a replay schedule. A value of `0` is used for a non-consolidated replay. |
| `FILE_NAME` | `VARCHAR2(51)` | File name of the captured stream |
| `SKIP_IT` | `VARCHAR2(1)` | Whether or not the current replayed user call is skipped or not |
| `DIRTY_BUFFERS` | `VARCHAR2(1)` | Reserved for internal use |
| `DBTIME` | `NUMBER` | Accumulated database time for the replay session |
| `NETWORK_TIME` | `NUMBER` | Accumulated network time for the replay session |
| `THINK_TIME` | `NUMBER` | Accumulated think time for the replay session |
| `TIME_GAIN` | `NUMBER` | If nonzero, the accumulated time in macro seconds indicating how fast the replay is |
| `TIME_LOSS` | `NUMBER` | If nonzero, the accumulated time in macro seconds indicating how slow the replay is |
| `USER_CALLS` | `NUMBER` | Total number of user calls |
| `PLSQL_CALLS` | `NUMBER` | Total number of PL/SQL calls recorded in the workload capture |
| `PLSQL_SUBCALLS` | `NUMBER` | Total number of calls recorded in the workload capture for SQL executed from PL/SQL |
| `PLSQL_DBTIME` | `NUMBER` | Total amount of database time in microseconds from PL/SQL calls that have been recorded in the workload capture |
| `CLIENT_OS_USER` | `VARCHAR2(15)` | Operating system username of the replay client |
| `CLIENT_HOST` | `VARCHAR2(64)` | Host name of the replay client |
| `CLIENT_PID` | `VARCHAR2(24)` | Process ID of the replay client |
| `PROGRAM` | `VARCHAR2(84)` | Program name of the replay client |
| `CAPTURE_ELAPSED_TIME` | `NUMBER` | Total amount of elapsed time of a session since capture starts (in seconds) |
| `REPLAY_ELAPSED_TIME` | `NUMBER` | Total amount of elapsed time of a session since replay starts (in seconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |