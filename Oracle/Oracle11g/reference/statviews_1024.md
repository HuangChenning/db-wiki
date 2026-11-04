---
title: ALL_BASE_TABLE_MVIEWS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1024.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_BASE_TABLE_MVIEWS` describes the materialized views using materialized view logs accessible to the current user. A materialized view log can be created for a master, base table, or master materialized view. Query this view at the master site or the master materialized view site to show one row for each materialized view using a materialized view log.

Related Views

- `DBA_BASE_TABLE_MVIEWS` describes all materialized views using materialized view logs in the database.
- `USER_BASE_TABLE_MVIEWS` describes the materialized views using materialized view logs owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Schema in which the master table or the master materialized view was created |
| `MASTER` | `VARCHAR2(30)` | `NOT NULL` | Name of the master table or the master materialized view |
| `MVIEW_LAST_REFRESH_TIME` | `DATE` | `NOT NULL` | Date when the materialized view based on the master was last refreshed |
| `MVIEW_ID` | `NUMBER(38)` |  | Unique identifier of the materialized view that is based on the master |

See Also:

- ["DBA\_BASE\_TABLE\_MVIEWS"](statviews_3095.md)
- ["USER\_BASE\_TABLE\_MVIEWS"](statviews_5240.md)