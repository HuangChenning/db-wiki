---
title: DBA_SQLTUNE_BINDS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4287.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SQLTUNE_BINDS` displays the bind values associated with all tuned SQL statements in the database.

Related View

`USER_SQLTUNE_BINDS` displays the bind values associated with the tuned SQL statements owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER(38)` | `NOT NULL` | Tuning task identifier |
| `OBJECT_ID` | `NUMBER(38)` | `NOT NULL` | Advisor framework object identifier |
| `POSITION` | `NUMBER(38)` | `NOT NULL` | Bind position |
| `VALUE` | `ANYDATA` |  | Bind value |

See Also:

["USER\_SQLTUNE\_BINDS"](statviews_5458.md)