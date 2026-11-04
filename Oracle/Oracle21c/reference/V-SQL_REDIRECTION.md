---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_REDIRECTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.63 V$SQL\_REDIRECTION

`V$SQL_REDIRECTION` displays SQL statements that are redirected.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the cursor handle |
| `PARENT_HANDLE` | `RAW(4 \| 8)` | Address of the parent cursor handle |
| `HASH_VALUE` | `NUMBER` | Hash value of the SQL statement |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the SQL statement |
| `CHILD_NUMBER` | `NUMBER` | Number of the child (instance) for the hash |
| `PARSING_USER_ID` | `NUMBER` | Parsing user ID |
| `PARSING_SCHEMA_ID` | `NUMBER` | Parsing schema ID |
| `COMMAND_TYPE` | `NUMBER` | `SELECT`, `UPDATE`, `INSERT`, `MERGE` |
| `REASON` | `VARCHAR2(14)` | Reason for redirection (`'INVALID OBJECT'`, `'ROWID'`, `'QUERY REWRITE'`, `'READ ONLY'`) |
| `ERROR_CODE` | `NUMBER` | Error code for local parse |
| `POSITION` | `NUMBER` | Error position, 0 if unknown |
| `SQL_TEXT_PIECE` | `VARCHAR2(1000)` | SQL Text containing position, usually a (qualified) identifier |
| `ERROR_MESSAGE` | `VARCHAR2(1000)` | Error code's corresponding error message resolved in the database language, no arguments resolved |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |