---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-OPEN_CURSOR.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.103 V$OPEN\_CURSOR

`V$OPEN_CURSOR` lists cursors that each user session currently has opened and parsed, or cached.

| Column | Datatype | Description |
| --- | --- | --- |
| `SADDR` | `RAW(4 \| 8)` | Session address |
| `SID` | `NUMBER` | Session identifier |
| `USER_NAME` | `VARCHAR2(128)` | User that is logged in to the session |
| `ADDRESS` | `RAW(4 \| 8)` | Used with `HASH_VALUE` to uniquely identify the SQL statement being executed in the session |
| `HASH_VALUE` | `NUMBER` | Used with `ADDRESS` to uniquely identify the SQL statement being executed in the session |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the SQL statement being executed in the session |
| `SQL_TEXT` | `VARCHAR2(60)` | First 60 characters of the SQL statement that is parsed into the open cursor |
| `LAST_SQL_ACTIVE_TIME` | `DATE` | Time when this cursor was last executed |
| `SQL_EXEC_ID` | `NUMBER` | If the open cursor is executing, then the SQL execution identifier for that execution (see `V$SQL_MONITOR`) |
| `CURSOR_TYPE` | `VARCHAR2(64)` | Type of cursor:  - `OPEN PL/SQL` - Open PL/SQL cursors - `OPEN` - Other open cursors - `SESSION CURSOR CACHED` - Cursors cached in the generic session cursor cache - `OPEN-RECURSIVE` - Open recursive cursors - `DICTIONARY LOOKUP CURSOR CACHED` - Cursors cached in the dictionary lookup cursor cache - `BUNDLE DICTIONARY LOOKUP CACHED` - Cursors cached in the bundled dictionary lookup cursor cache - `JAVA NAME TRANSLATION CURSOR CACHED` - Cursors cached in the Java name translation cursor cache - `REPLICATION TRIGGER CURSOR CACHED` - Cursors cached in the replication trigger cursor cache - `CONSTRAINTS CURSOR CACHED` - Cursors cached in the constraints cursor cache - `PL/SQL CURSOR CACHED` - Cursors cached in the PL/SQL cursor cache |
| `CHILD_ADDRESS` | `RAW(4 \| 8)` | Address of the child cursor |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |