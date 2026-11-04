---
title: ALL_INDEXTYPE_OPERATORS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1112.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_INDEXTYPE_OPERATORS` lists all operators supported by indextypes accessible to the current user.

Related Views

- `DBA_INDEXTYPE_OPERATORS` lists all operators supported by indextypes in the database.
- `USER_INDEXTYPE_OPERATORS` lists all operators supported by indextypes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the indextype |
| `INDEXTYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the indextype |
| `OPERATOR_SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Name of the operator schema |
| `OPERATOR_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the operator for which the indextype is defined |
| `BINDING#` | `NUMBER` | `NOT NULL` | Binding number associated with the operator |

See Also:

- ["DBA\_INDEXTYPE\_OPERATORS"](statviews_4084.md)
- ["USER\_INDEXTYPE\_OPERATORS"](statviews_5326.md)