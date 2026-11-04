---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_MVIEW_REFRESH_TIMES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_MVIEW_REFRESH_TIMES` describes refresh times of the materialized views accessible to the current user.

Related Views

- `DBA_MVIEW_REFRESH_TIMES` describes refresh times of all materialized views in the database.
- `USER_MVIEW_REFRESH_TIMES` describes refresh times of the materialized views owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `MASTER_OWNER` | `VARCHAR2(128)` |  | Owner of the master table |
| `MASTER` | `VARCHAR2(128)` |  | Name of the master table |
| `LAST_REFRESH` | `DATE` |  | `SYSDATE` from the master site at the time of the last refresh |

See Also:

- " [DBA\_MVIEW\_REFRESH\_TIMES](DBA_MVIEW_REFRESH_TIMES.md) "
- " [USER\_MVIEW\_REFRESH\_TIMES](USER_MVIEW_REFRESH_TIMES.md) "