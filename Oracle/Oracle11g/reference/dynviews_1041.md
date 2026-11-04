---
title: "V$AW_LONGOPS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1041.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$AW_LONGOPS` displays status information about active SQL cursors initiated in an analytic workspace.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Identifier for the session in which the fetch is executing. This table can be joined with `V$SESSION` to obtain the user name. |
| `CURSOR_NAME` | `VARCHAR2(64)` | Name assigned to the cursor |
| `COMMAND` | `VARCHAR2(17)` | Command that is actively fetching data from relational tables: - `QUERY` - `FETCH` - `IMPORT` - `EXECUTE` - `UPDATE` - `SOLVE` - `CLEAR` - `LOAD CUBE` - `LOAD DIMENSION` - `DIMENSION COMPILE` |
| `STATUS` | `VARCHAR2(9)` | Status of the current operation: - `EXECUTING` - Command has begun executing - `FETCHING` - Data is being fetched into the analytic workspace - `FINISHED` - Command has finished executing. This status appears very briefly before the record disappears from the table. |
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
| `UNITS` | `VARCHAR2(6)` | Units description: |
| `MESSAGE` | `VARCHAR2(512)` | Message for the user |
| `USERNAME` | `VARCHAR2(32)` | User name |