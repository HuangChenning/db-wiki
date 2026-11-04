---
title: ALL_MVIEW_KEYS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1150.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_MVIEW_KEYS` describes the columns or expressions in the `SELECT` list upon which materialized views accessible to the current user are based.

Related Views

- `DBA_MVIEW_KEYS` describes such columns and expressions for all materialized views in the database.
- `USER_MVIEW_KEYS` describes such columns and expressions for all materialized views owned by the current user.

Note:

All three views exclude materialized views that reference remote tables or that includes references to a nonstatic value such as `SYSDATE` or `USER`. These views also exclude materialized views that were created as snapshots prior to Oracle8i and that were never altered to enable query rewrite.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Materialized view name |
| `POSITION_IN_SELECT` | `NUMBER` | `NOT NULL` | Ordinal position of this key within the `SELECT` list |
| `CONTAINER_COLUMN` | `VARCHAR2(30)` | `NOT NULL` | Name of the column in the container table |
| `DETAILOBJ_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Detail object owner |
| `DETAILOBJ_NAME` | `VARCHAR2(30)` | `NOT NULL` | Detail object name (for example, the name of a table or view) |
| `DETAILOBJ_ALIAS` | `VARCHAR2(30)` |  | Implicit or explicit alias for detail relation |
| `DETAILOBJ_TYPE` | `VARCHAR2(5)` |  | Detail object type: |
| `DETAILOBJ_COLUMN` | `VARCHAR2(30)` | `NOT NULL` | Name of the detail relation column |