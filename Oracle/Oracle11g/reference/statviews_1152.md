---
title: ALL_MVIEW_REFRESH_TIMES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1152.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_MVIEW_REFRESH_TIMES` describes refresh times of the materialized views accessible to the current user.

Related Views

- `DBA_MVIEW_REFRESH_TIMES` describes refresh times of all materialized views in the database.
- `USER_MVIEW_REFRESH_TIMES` describes refresh times of the materialized views owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the materialized view |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the materialized view |
| `MASTER_OWNER` | `VARCHAR2(30)` |  | Owner of the master table |
| `MASTER` | `VARCHAR2(30)` |  | Name of the master table |
| `LAST_REFRESH` | `DATE` |  | `SYSDATE` from the master site at the time of the last refresh |

See Also:

- ["DBA\_MVIEW\_REFRESH\_TIMES"](statviews_4148.md)
- ["USER\_MVIEW\_REFRESH\_TIMES"](statviews_5367.md)