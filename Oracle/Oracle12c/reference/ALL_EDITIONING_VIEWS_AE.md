---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_EDITIONING_VIEWS_AE.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_EDITIONING_VIEWS_AE` describes the editioning views (across all editions) accessible to the current user.

Related Views

- `DBA_EDITIONING_VIEWS_AE` describes all editioning views (across all editions) in the database.
- `USER_EDITIONING_VIEWS_AE` describes the editioning views (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of an editioning view |
| `VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of an editioning view |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of an editioning view's base table |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the editioning view is defined |

See Also:

- " [DBA\_EDITIONING\_VIEWS\_AE](DBA_EDITIONING_VIEWS_AE.md) "
- " [USER\_EDITIONING\_VIEWS\_AE](USER_EDITIONING_VIEWS_AE.md) "