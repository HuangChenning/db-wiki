---
title: ALL_EDITIONING_VIEW_COLS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1080.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_EDITIONING_VIEW_COLS` describes the relationship between the columns of the editioning views accessible to the current user and the table columns to which they map.

Related Views

- `DBA_EDITIONING_VIEW_COLS` describes the relationship between the columns of all editioning views in the database and the table columns to which they map.
- `USER_EDITIONING_VIEW_COLS` describes the relationship between the columns of the editioning views owned by the current user and the table columns to which they map. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of an editioning view |
| `VIEW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of an editioning view |
| `VIEW_COLUMN_ID` | `NUMBER` | `NOT NULL` | Column number within the editioning view |
| `VIEW_COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the column in the editioning view |
| `TABLE_COLUMN_ID` | `NUMBER` | `NOT NULL` | Column number of a table column to which this editioning view column maps |
| `TABLE_COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a table column to which this editioning view column maps |

See Also:

- ["DBA\_EDITIONING\_VIEW\_COLS"](statviews_3161.md)
- ["USER\_EDITIONING\_VIEW\_COLS"](statviews_5290.md)