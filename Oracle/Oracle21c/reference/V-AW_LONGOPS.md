---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AW_LONGOPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.79 V$AW\_LONGOPS

`V$AW_LONGOPS` displays status information about active SQL cursors initiated in an analytic workspace.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Identifier for the session in which the fetch is executing. This table can be joined with ` V$SESSION` to obtain the user name. |
| `CURSOR_NAME` | `VARCHAR2(64)` | Name assigned to the cursor |
| `COMMAND` | `VARCHAR2(17)` | Command that is actively fetching data from relational tables:  - `QUERY` - `FETCH` - `IMPORT` - `EXECUTE` - `UPDATE` - `SOLVE` - `CLEAR` - `LOAD CUBE` - `LOAD DIMENSION` - `DIMENSION COMPILE` |
| `STATUS` | `VARCHAR2(9)` | Status of the current operation:  - `EXECUTING` - Command has begun executing - `FETCHING` - Data is being fetched into the analytic workspace - `FINISHED` - Command has finished executing. This status appears very briefly before the record disappears from the table. |
| `ROWS_PROCESSED` | `NUMBER` | Number of rows already inserted, updated, or deleted |
| `SEQ_NUMBER` | `NUMBER` | Sequence number in the Cube Build log |
| `SQL_ID` | `VARCHAR2(13)` | SQL ID of the statement |
| `TARGET` | `VARCHAR2(64)` | Operated object name |
| `TARGET_DESC` | `VARCHAR2(64)` | A brief description of the operated object |
| `START_TIME` | `DATE` | Time the command started executing |
| `LAST_UPDATE_TIME` | `DATE` | Last updated time |
| `ELAPSED_SECONDS` | `NUMBER` | Number of seconds between `START_TIME` and `LAST_UPDATE_TIME` |
| `SOFAR` | `NUMBER` | Number of units so far |
| `TOTALWORK` | `NUMBER` | Total number of units |
| `UNITS` | `VARCHAR2(6)` | Units description:  - `ROWS` - `NODES` - `VALUES` |
| `MESSAGE` | `VARCHAR2(512)` | Message for the user |
| `USERNAME` | `VARCHAR2(32)` | User name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |