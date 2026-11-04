---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_REGISTERED_MVIEWS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.28 ALL\_REGISTERED\_MVIEWS

`ALL_REGISTERED_MVIEWS` describes all registered materialized views (registered at a master site or a master materialized view site) accessible to the current user.

A materialized view created with the `BUILD DEFERRED` option of the `CREATE MATERIALIZED VIEW` statement is only registered with `ALL_REGISTERED_MVIEWS` if that materialized view has been completely refreshed at least once.

Related Views

- `DBA_REGISTERED_MVIEWS` describes all registered materialized views in the database.
- `USER_REGISTERED_MVIEWS` describes all registered materialized views owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `MVIEW_SITE` | `VARCHAR2(128)` | `NOT NULL` | Global name of the materialized view site |
| `CAN_USE_LOG` | `VARCHAR2(3)` |  | Indicates whether the materialized view can use a materialized view log (`YES`) or the materialized view is too complex to use a log (`NO`) |
| `UPDATABLE` | `VARCHAR2(3)` |  | Indicates whether the materialized view is updatable (`YES`) or not and the materialized view is read only (`NO`) |
| `REFRESH_METHOD` | `VARCHAR2(11)` |  | Indicates whether the materialized view uses primary key (`PRIMARY KEY`), rowids (`ROWID`), or object identifiers (`OBJECT ID`) for fast refresh |
| `MVIEW_ID` | `NUMBER(38)` |  | Identifier for the materialized view used by the masters for fast refresh |
| `VERSION` | `VARCHAR2(26)` |  | Oracle version of the materialized view |
| `QUERY_TXT` | `LONG` |  | Query that defines the materialized view |

See Also:

- " [DBA\_REGISTERED\_MVIEWS](DBA_REGISTERED_MVIEWS.md) "
- " [USER\_REGISTERED\_MVIEWS](USER_REGISTERED_MVIEWS.md) "