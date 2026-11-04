---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_EDITIONING_VIEWS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.178 ALL\_EDITIONING\_VIEWS

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