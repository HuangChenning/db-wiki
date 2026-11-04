---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_EDITIONING_VIEWS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.170 ALL\_EDITIONING\_VIEWS

`ALL_EDITIONING_VIEWS` describes the editioning views accessible to the current user.

Related Views

- `DBA_EDITIONING_VIEWS` describes all editioning views in the database.
- `USER_EDITIONING_VIEWS` describes the editioning views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of an editioning view |
| `VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of an editioning view |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of an editioning view's base table |

See Also:

- " [DBA\_EDITIONING\_VIEWS](DBA_EDITIONING_VIEWS.md) "
- " [USER\_EDITIONING\_VIEWS](USER_EDITIONING_VIEWS.md) "