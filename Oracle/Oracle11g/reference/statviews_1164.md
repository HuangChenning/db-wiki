---
title: ALL_OPERATORS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1164.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_OPERATORS` describes the operators accessible to the current user.

Related Views

- `DBA_OPERATORS` describes all operators in the database.
- `USER_OPERATORS` describes the operators owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the operator |
| `OPERATOR_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the operator |
| `NUMBER_OF_BINDS` | `NUMBER` | `NOT NULL` | Number of bindings associated with the operator |

See Also:

- ["DBA\_OPERATORS"](statviews_4164.md)
- ["USER\_OPERATORS"](statviews_5382.md)