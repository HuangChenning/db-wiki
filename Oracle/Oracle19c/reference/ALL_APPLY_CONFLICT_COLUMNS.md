---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_APPLY_CONFLICT_COLUMNS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.56 ALL\_APPLY\_CONFLICT\_COLUMNS

`ALL_APPLY_CONFLICT_COLUMNS` displays information about the conflict handlers on the tables accessible to the current user.

Related View

`DBA_APPLY_CONFLICT_COLUMNS` displays information about the conflict handlers on all tables in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the object on which the update conflict handler is defined |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object on which the update conflict handler is defined |
| `METHOD_NAME` | `VARCHAR2(92)` |  | Name of the update conflict handler used to resolve conflicts |
| `RESOLUTION_COLUMN` | `VARCHAR2(4000)` |  | Name of the column used to resolve conflicts |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of a column in the column list for the update conflict handler |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | Database link to which changes are applied. If null, then changes are applied to the local database. |

See Also:

" [DBA\_APPLY\_CONFLICT\_COLUMNS](DBA_APPLY_CONFLICT_COLUMNS.md) "