---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_COL_COMMENTS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_COL_COMMENTS` displays comments on the columns of the tables and views accessible to the current user.

Related Views

- `DBA_COL_COMMENTS` displays comments on the columns of all tables and views in the database.
- `USER_COL_COMMENTS` displays comments on the columns of the tables and views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the column |