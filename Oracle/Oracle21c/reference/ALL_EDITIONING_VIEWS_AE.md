---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_EDITIONING_VIEWS_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.179 ALL\_EDITIONING\_VIEWS\_AE

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