---
title: ALL_EDITIONING_VIEWS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1082.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_EDITIONING_VIEWS` describes the editioning views accessible to the current user.

Related Views

- `DBA_EDITIONING_VIEWS` describes all editioning views in the database.
- `USER_EDITIONING_VIEWS` describes the editioning views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of an editioning view |
| `VIEW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of an editioning view |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of an editioning view's base table |

See Also:

- ["DBA\_EDITIONING\_VIEWS"](statviews_3163.md)
- ["USER\_EDITIONING\_VIEWS"](statviews_5292.md)