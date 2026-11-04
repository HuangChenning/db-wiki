---
title: ALL_DB_LINKS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1067.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DB_LINKS` describes the database links accessible to the current user.

Related Views

- `DBA_DB_LINKS` describes all database links in the database.
- `USER_DB_LINKS` describes the database links owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the database link |
| `DB_LINK` | `VARCHAR2(128)` | `NOT NULL` | Name of the database link |
| `USERNAME` | `VARCHAR2(30)` |  | Name of the user when logging in |
| `HOST` | `VARCHAR2(2000)` |  | Oracle Net connect string |
| `CREATED` | `DATE` | `NOT NULL` | Creation time of the database link |

See Also:

- ["DBA\_DB\_LINKS"](statviews_3146.md)
- ["USER\_DB\_LINKS"](statviews_5280.md)