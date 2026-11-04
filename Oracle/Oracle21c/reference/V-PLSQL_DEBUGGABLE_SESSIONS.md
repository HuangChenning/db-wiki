---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PLSQL_DEBUGGABLE_SESSIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.123 V$PLSQL\_DEBUGGABLE\_SESSIONS

`V$PLSQL_DEBUGGABLE_SESSIONS` shows the current sessions of all users that the current user has privileges to debug with a PL/SQL debugger.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `SERIAL#` | `NUMBER` | Session serial number |
| `LOGON_TIME` | `DATE` | Time of logon |
| `USER#` | `NUMBER` | Oracle user identifier |
| `USERNAME` | `VARCHAR2(128)` | Oracle user name |
| `OSUSER` | `VARCHAR2(128)` | Operating system client user name |
| `PROCESS` | `VARCHAR2(24)` | Operating system client process ID |
| `MACHINE` | `VARCHAR2(64)` | Operating system client machine name |
| `PORT` | `NUMBER` | Operating system client port number |
| `TERMINAL` | `VARCHAR2(30)` | Operating system client terminal name |
| `PROGRAM` | `VARCHAR2(84)` | Operating system client program name |
| `TYPE` | `VARCHAR2(10)` | Session type |
| `SERVICE_NAME` | `VARCHAR2(64)` | Service name of the session |
| `PLSQL_DEBUGGER_CONNECTED` | `VARCHAR2(5)` | Indicates whether the session is connected to a PL/SQL debugger. Possible values:  - `TRUE` - `FALSE` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |