---
title: ALL_TSTZ_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2123.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TSTZ_TABLES` displays information about the tables accessible to the current user, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types.

Related Views

- `DBA_TSTZ_TABLES` displays information about all tables in the database, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types.
- `USER_TSTZ_TABLES` displays information about the tables owned by the current user, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `UPGRADE_IN_PROGRESS` | `VARCHAR2(3)` |  | Indicates whether a table upgrade is in progress (`YES`) or not (`NO`) |

See Also:

- ["DBA\_TSTZ\_TABLES"](statviews_5072.md)
- ["USER\_TSTZ\_TABLES"](statviews_5498.md)