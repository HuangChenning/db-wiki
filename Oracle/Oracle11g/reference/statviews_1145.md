---
title: ALL_MVIEW_COMMENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1145.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_MVIEW_COMMENTS` displays comments on the materialized views accessible to the current user.

Related Views

- `DBA_MVIEW_COMMENTS` displays comments on the materialized views in the database.
- `USER_MVIEW_COMMENTS` displays comments on the materialized views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the materialized view |
| `COMMENTS` | `VARCHAR2(4000)` |  | Comment on the materialized view |

See Also:

- ["DBA\_MVIEW\_COMMENTS"](statviews_4140.md)
- ["USER\_MVIEW\_COMMENTS"](statviews_5360.md)