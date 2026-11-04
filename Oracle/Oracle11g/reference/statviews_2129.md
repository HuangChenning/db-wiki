---
title: ALL_UPDATABLE_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2129.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_UPDATABLE_COLUMNS` describes all columns in a join view that are updatable by the current user, subject to appropriate privileges.

Related Views

- `DBA_UPDATABLE_COLUMNS` describes all columns in a join view that are updatable by the database administrator, subject to appropriate privileges.
- `USER_UPDATABLE_COLUMNS` describes all columns owned by the current user that are in a join view and are updatable by the current user, subject to appropriate privileges.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Column name |
| `UPDATABLE` | `VARCHAR2(3)` |  | Indicates whether the column is updatable (`YES`) or not (`NO`) |
| `INSERTABLE` | `VARCHAR2(3)` |  | Indicates whether the column is insertable (`YES`) or not (`NO`) |
| `DELETABLE` | `VARCHAR2(3)` |  | Indicates whether the column is deletable (`YES`) or not (`NO`) |