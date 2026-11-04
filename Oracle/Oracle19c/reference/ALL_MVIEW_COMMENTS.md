---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_MVIEW_COMMENTS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.273 ALL\_MVIEW\_COMMENTS

`ALL_MVIEW_COMMENTS` displays comments on the materialized views accessible to the current user.

Related Views

- `DBA_MVIEW_COMMENTS` displays comments on the materialized views in the database.
- `USER_MVIEW_COMMENTS` displays comments on the materialized views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |