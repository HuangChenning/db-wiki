---
title: "V$SQL_REDIRECTION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3058.htm
tags:
  - oracle
  - 11g
  - reference
---

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