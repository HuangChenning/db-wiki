---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_OPANCILLARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.296 ALL\_OPANCILLARY

`ALL_OPANCILLARY` describes operators whose bindings are ancillary to other (primary) operators.

Related Views

- `DBA_OPANCILLARY` describes such information about all operators in the database.
- `USER_OPANCILLARY` describes such information about operators owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the ancillary operator |
| `OPERATOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the ancillary operator |
| `BINDING#` | `NUMBER` | `NOT NULL` | Binding number of the ancillary operator |
| `PRIMOP_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the primary operator |
| `PRIMOP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the primary operator |
| `PRIMOP_BIND#` | `NUMBER` | `NOT NULL` | Binding number of the primary operator |

See Also:

- " [DBA\_OPANCILLARY](DBA_OPANCILLARY.md) "
- " [USER\_OPANCILLARY](USER_OPANCILLARY.md) "