---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_ACCHK_STATISTICS.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.5 DBA\_ACCHK\_STATISTICS

`DBA_ACCHK_STATISTICS` displays Application Continuity protection statistics for each session that executed during an Application Continuity Protection Check (ACCHK) workload run.

ACCHK should be used on a running workload. Sessions that are terminated are not included in this view.

The `ACCHK_READ` role allows users with no administrative privileges to query this view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INST_ID` | `NUMBER` | `NOT NULL` | Identifier for the instance for the session |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `CON_UID` <sup>Foot 1</sup> | `NUMBER` | `NOT NULL` | Unique ID of the container used by the session |
| `TIMESTAMP` | `TIMESTAMP(3) WITH TIME ZONE` |  | Time at which the session was terminated and the statistics were reported |
| `SESSION_ID` | `NUMBER` | `NOT NULL` | ID of the session |
| `SERIAL#` | `NUMBER` | `NOT NULL` | Serial number of the session |
| `STAT_TYPE` | `VARCHAR2(32)` |  | Type of statistic  The value of this column is always `SESSION_STATISTICS`. |
| `SERVICE_NAME` | `VARCHAR2(64)` |  | Service name of the session |
| `FAILOVER_TYPE` | `VARCHAR2(16)` |  | Indicates the `FAILOVER_TYPE` service setting for the session. Possible values:  - `AUTO` - Transparent Application Continuity (TAC) was enabled for the session - `TRANSACTION` - Application Continuity (AC) was enabled for the session - `NONE` - Failover was disabled for the session |
| `FAILOVER_RESTORE` | `VARCHAR2(16)` |  | Indicates the `FAILOVER_RESTORE` service setting for the session. Possible values:  - `AUTO` - Transparent Application Continuity - `LEVEL1` - Application Continuity - `NONE` - Session state was not restored at failover |
| `RESET_STATE` | `VARCHAR2(16)` |  | Indicates the `RESET_STATE` service setting for the session. Possible values:  - `LEVEL1` - The session state was cleaned at the end of a request - `NONE` - The session state was not cleaned at the end of a request |
| `PROGRAM` | `VARCHAR2(84)` |  | Name of the operating system program |
| `BEGIN_REQUESTS` | `NUMBER` |  | Number of begin requests received for the session |
| `END_REQUESTS` | `NUMBER` |  | Number of end requests received for the session |
| `USER_CALLS_IN_REQUESTS` | `NUMBER` |  | Number of user calls received from the application within requests (between begin request and end request) |
| `PROTECTED_CALLS_IN_REQUESTS` | `NUMBER` |  | Number of user calls protected by Application Continuity within requests (between begin request and end request) |
| `TIME_IN_REQUESTS` | `NUMBER` |  | Time (in microseconds) spent on user calls within requests (between begin request and end request) |
| `TIME_PROTECTED_IN_REQUESTS` | `NUMBER` |  | Time (in microseconds) spent on user calls protected by Application Continuity within requests (between begin request and end request) |
| `MAX_USER_CALLS_PER_REQUEST` <sup>Foot 1</sup> | `NUMBER` |  | Maximum number of user calls received from the application per request (between begin request and end request) |
| `MAX_PROT_CALLS_PER_REQUEST` <sup>Foot 1</sup> | `NUMBER` |  | Maximum number of user calls protected by Application Continuity received from the application per request (between begin request and end request) |
| `CON_ID_EXT` <sup>Foot 1</sup> | `NUMBER` |  | Container ID used by the session for external recognition |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 19c, Release Update 19.19.

Note:

This view is available starting with Oracle Database 19c, Release Update 19.11.

For Oracle Database 19c, Release Update 19.11 through Release Update 19.18, this view is not created by default. To create this view, you must run the `DBMS_APP_CONT_ADMIN.ACCHK_VIEWS` procedure. See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ARPLS-GUID-19FCC848-EB10-4105-8F7E-6E6CEB4E4294) for more information.

Starting with Oracle Database 19c, Release Update 19.19, this view is created by default.