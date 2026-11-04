---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_INDEXTYPE_COMMENTS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.230 ALL\_INDEXTYPE\_COMMENTS

`ALL_INDEXTYPE_COMMENTS` displays comments for the user-defined indextypes accessible to the current user.

Related Views

- `DBA_INDEXTYPE_COMMENTS` displays comments for all user-defined indextypes in the database.
- `USER_INDEXTYPE_COMMENTS` displays comments for the user-defined indextypes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the user-defined indextype |
| `INDEXTYPE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user-defined indextype |