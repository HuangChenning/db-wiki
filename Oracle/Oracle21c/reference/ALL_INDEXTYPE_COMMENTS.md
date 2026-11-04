---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_INDEXTYPE_COMMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.238 ALL\_INDEXTYPE\_COMMENTS

`ALL_INDEXTYPE_COMMENTS` displays comments for the user-defined indextypes accessible to the current user.

Related Views

- `DBA_INDEXTYPE_COMMENTS` displays comments for all user-defined indextypes in the database.
- `USER_INDEXTYPE_COMMENTS` displays comments for the user-defined indextypes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the user-defined indextype |
| `INDEXTYPE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user-defined indextype |