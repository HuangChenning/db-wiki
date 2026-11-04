---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_OPARGUMENTS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_OPARGUMENTS` describes arguments for each operator binding accessible to the current user.

Related Views

- `DBA_OPARGUMENTS` describes arguments of all operator bindings in the database.
- `USER_OPARGUMENTS` describes arguments of all operator bindings owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the operator argument |
| `OPERATOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the operator argument |
| `BINDING#` | `NUMBER` | `NOT NULL` | Binding number of the operator argument |
| `POSITION` | `NUMBER` | `NOT NULL` | Position of the operator argument (1, 2, 3,...) |
| `ARGUMENT_TYPE` | `VARCHAR2(61)` |  | Datatype of the operator argument |

See Also:

- " [DBA\_OPARGUMENTS](DBA_OPARGUMENTS.md) "
- " [USER\_OPARGUMENTS](USER_OPARGUMENTS.md) "