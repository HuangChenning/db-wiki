---
title: ALL_TAB_COMMENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2104.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TAB_COMMENTS` displays comments on the tables and views accessible to the current user.

Related Views

- `DBA_TAB_COMMENTS` displays comments on all tables and views in the database.
- `USER_TAB_COMMENTS` displays comments on the tables and views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `TABLE_TYPE` | `VARCHAR2(11)` |  | Type of the object |
| `COMMENTS` | `VARCHAR2(4000)` |  | Comment on the object |

See Also:

- ["DBA\_TAB\_COMMENTS"](statviews_5045.md)
- ["USER\_TAB\_COMMENTS"](statviews_5477.md)