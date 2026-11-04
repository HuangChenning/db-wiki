---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_INDEXTYPE_OPERATORS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.239 ALL\_INDEXTYPE\_OPERATORS

`ALL_INDEXTYPE_OPERATORS` lists all operators supported by indextypes accessible to the current user.

Related Views

- `DBA_INDEXTYPE_OPERATORS` lists all operators supported by indextypes in the database.
- `USER_INDEXTYPE_OPERATORS` lists all operators supported by indextypes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the indextype |
| `INDEXTYPE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the indextype |
| `OPERATOR_SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Name of the operator schema |
| `OPERATOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the operator for which the indextype is defined |
| `BINDING#` | `NUMBER` | `NOT NULL` | Binding number associated with the operator |

See Also:

- " [DBA\_INDEXTYPE\_OPERATORS](DBA_INDEXTYPE_OPERATORS.md) "
- " [USER\_INDEXTYPE\_OPERATORS](USER_INDEXTYPE_OPERATORS.md) "