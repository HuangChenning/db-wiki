---
title: ALL_PENDING_CONV_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2008.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_PENDING_CONV_TABLES` describes the pending conversion tables (tables which are not upgraded to the latest type version) accessible to the current user.

Related Views

- `DBA_PENDING_CONV_TABLES` describes all pending conversion tables in the database.
- `USER_PENDING_CONV_TABLES` describes the pending conversion tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |

See Also:

- ["DBA\_PENDING\_CONV\_TABLES"](statviews_4179.md)
- ["USER\_PENDING\_CONV\_TABLES"](statviews_5395.md)