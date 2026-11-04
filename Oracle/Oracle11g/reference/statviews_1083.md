---
title: ALL_EDITIONING_VIEWS_AE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1083.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_EDITIONING_VIEWS_AE` describes the editioning views (across all editions) accessible to the current user.

Related Views

- `DBA_EDITIONING_VIEWS_AE` describes all editioning views (across all editions) in the database.
- `USER_EDITIONING_VIEWS_AE` describes the editioning views (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of an editioning view |
| `VIEW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of an editioning view |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of an editioning view's base table |
| `EDITION_NAME` | `VARCHAR2(30)` |  | Name of the application edition where the editioning view is defined |

See Also:

- ["DBA\_EDITIONING\_VIEWS\_AE"](statviews_3164.md)
- ["USER\_EDITIONING\_VIEWS\_AE"](statviews_5293.md)