---
title: ALL_UNUSED_COL_TABS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2128.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_UNUSED_COL_TABS` describes the tables accessible to the current user that contain unused columns.

Related Views

- `DBA_UNUSED_COL_TABS` describes all tables in the database that contain unused columns.
- `USER_UNUSED_COL_TABS` describes the tables owned by the current user that contain unused columns. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `COUNT` | `NUMBER` |  | Number of unused columns |

See Also:

- ["DBA\_UNUSED\_COL\_TABS"](statviews_5079.md)
- ["USER\_UNUSED\_COL\_TABS"](statviews_5504.md)