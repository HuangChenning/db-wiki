---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_OPERATORS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.300 ALL\_OPERATORS

`ALL_OPERATORS` describes the operators accessible to the current user.

Related Views

- `DBA_OPERATORS` describes all operators in the database.
- `USER_OPERATORS` describes the operators owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the operator |
| `OPERATOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the operator |
| `NUMBER_OF_BINDS` | `NUMBER` | `NOT NULL` | Number of bindings associated with the operator |

See Also:

- " [DBA\_OPERATORS](DBA_OPERATORS.md) "
- " [USER\_OPERATORS](USER_OPERATORS.md) "