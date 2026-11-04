---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_OPERATOR_COMMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.299 ALL\_OPERATOR\_COMMENTS

`ALL_OPERATOR_COMMENTS` displays comments for the user-defined operators accessible to the current user.

Related Views

- `DBA_OPERATOR_COMMENTS` displays comments for all user-defined operators in the database.
- `USER_OPERATOR_COMMENTS` displays comments for the user-defined operators owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the user-defined operator |
| `OPERATOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user-defined operator |