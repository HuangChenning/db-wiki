---
title: "V$OPEN_CURSOR"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2083.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$OPEN_CURSOR` lists cursors that each user session currently has opened and parsed, or cached.

| Column | Datatype | Description |
| --- | --- | --- |
| `SADDR` | `RAW(4 \| 8)` | Session address |
| `SID` | `NUMBER` | Session identifier |
| `USER_NAME` | `VARCHAR2(30)` | User that is logged in to the session |
| `ADDRESS` | `RAW(4 \| 8)` | Used with `HASH_VALUE` to uniquely identify the SQL statement being executed in the session |
| `HASH_VALUE` | `NUMBER` | Used with `ADDRESS` to uniquely identify the SQL statement being executed in the session |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the SQL statement being executed in the session |
| `SQL_TEXT` | `VARCHAR2(60)` | First 60 characters of the SQL statement that is parsed into the open cursor |
| `LAST_SQL_ACTIVE_TIME` | `DATE` | Time when this cursor was last executed |
| `SQL_EXEC_ID` | `NUMBER` | If the open cursor is executing, then the SQL execution identifier for that execution (see `V$SQL_MONITOR`) |
| `CURSOR_TYPE` | `VARCHAR2(64)` | Type of cursor: - `OPEN-PL/SQL` - Open PL/SQL cursors - `OPEN` - Other open cursors - `SESSION CURSOR CACHED` - Cursors cached in the generic session cursor cache - `OPEN-RECURSIVE` - Open recursive cursors - `DICTIONARY` `LOOKUP` `CURSOR` `CACHED` - Cursor cached in the dictionary lookup cursor cache - `BUNDLE DICTIONARY LOOKUP CACHED` - Cursors cached in the bundled dictionary lookup cursor cache - `JAVA NAME TRANSLATION CURSOR CACHED` - Cursors cached in the Java name translation cursor cache - `REPLICATION` `TRIGGER` `CURSOR` `CACHED` - Cursors cached in the replication trigger cursor cache - `CONSTRAINTS` `CURSOR` `CACHED` - Cursors cached in the constraints cursor cache - `PL/SQL` `CURSOR` `CACHED` - Cursors cached in the PL/SQL cursor cache |