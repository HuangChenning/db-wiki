---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_EDITIONING_VIEW_COLS_AE.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.169 ALL\_EDITIONING\_VIEW\_COLS\_AE

`ALL_EDITIONING_VIEW_COLS_AE` describes the relationship between the columns of the editioning views (across all editions) accessible to the current user and the table columns to which they map.

Related Views

- `DBA_EDITIONING_VIEW_COLS_AE` describes the relationship between the columns of all editioning views (across all editions) in the database and the table columns to which they map.
- `USER_EDITIONING_VIEW_COLS_AE` describes the relationship between the columns of the editioning views (across all editions) owned by the current user and the table columns to which they map. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of an editioning view |
| `VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of an editioning view |
| `VIEW_COLUMN_ID` | `NUMBER` | `NOT NULL` | Column number within the editioning view |
| `VIEW_COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the column in the editioning view |
| `TABLE_COLUMN_ID` | `NUMBER` | `NOT NULL` | Column number of a table column to which this editioning view column maps |
| `TABLE_COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a table column to which this editioning view column maps |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the editioning view is defined |

See Also:

- " [DBA\_EDITIONING\_VIEW\_COLS\_AE](DBA_EDITIONING_VIEW_COLS_AE.md) "
- " [USER\_EDITIONING\_VIEW\_COLS\_AE](USER_EDITIONING_VIEW_COLS_AE.md) "