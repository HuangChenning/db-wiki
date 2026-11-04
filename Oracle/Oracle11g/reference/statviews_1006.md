---
title: ALL_APPLY_CONFLICT_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1006.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_APPLY_CONFLICT_COLUMNS` displays information about the conflict handlers on the tables accessible to the current user.

Related View

`DBA_APPLY_CONFLICT_COLUMNS` displays information about the conflict handlers on all tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(30)` |  | Owner of the object on which the update conflict handler is defined |
| `OBJECT_NAME` | `VARCHAR2(30)` |  | Name of the object on which the update conflict handler is defined |
| `METHOD_NAME` | `VARCHAR2(92)` |  | Name of the update conflict handler used to resolve conflicts |
| `RESOLUTION_COLUMN` | `VARCHAR2(4000)` |  | Name of the column used to resolve conflicts |
| `COLUMN_NAME` | `VARCHAR2(30)` |  | Name of a column in the column list for the update conflict handler |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | Database link to which changes are applied. If null, then changes are applied to the local database. |

See Also:

["DBA\_APPLY\_CONFLICT\_COLUMNS"](statviews_3049.md)