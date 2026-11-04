---
title: "V$SQLTEXT_WITH_NEWLINES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3072.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQLTEXT_WITH_NEWLINES` is identical to the `V$SQLTEXT` view except that, to improve legibility, `V$SQLTEXT_WITH_NEWLINES` does not replace newlines and tabs in the SQL statement with spaces.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Used with `HASH_VALUE` to uniquely identify a cached cursor |
| `HASH_VALUE` | `NUMBER` | Used with `ADDRESS` to uniquely identify a cached cursor |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of a cached cursor |
| `COMMAND_TYPE` | `NUMBER` | Code for the type of SQL statement (`SELECT`, `INSERT`, and so on) |
| `PIECE` | `NUMBER` | Number used to order the pieces of SQL text |
| `SQL_TEXT` | `VARCHAR2(64)` | A column containing one piece of the SQL text |

See Also:

["V$SQLTEXT"](dynviews_3071.md)