---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TAB_COMMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.108 ALL\_TAB\_COMMENTS

`ALL_TAB_COMMENTS` displays comments on the tables and views accessible to the current user.

Related Views

- `DBA_TAB_COMMENTS` displays comments on all tables and views in the database.
- `USER_TAB_COMMENTS` displays comments on the tables and views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `TABLE_TYPE` | `VARCHAR2(11)` |  | Type of the object |