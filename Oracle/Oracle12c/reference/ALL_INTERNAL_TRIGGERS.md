---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_INTERNAL_TRIGGERS.html
tags:
  - oracle
  - 12c
  - reference
---

Internal triggers are internal pieces of code executed when a particular flag is set for a table. This view does not display the `OWNER_NAME` column.

Related Views

- `DBA_INTERNAL_TRIGGERS` describes internal triggers on all tables in the database.
- `USER_INTERNAL_TRIGGERS` describes all internal triggers on tables owned by the current user. This view does not display the `OWNER_NAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_NAME ` | `VARCHAR2(128)` |  | Name of the table on which the trigger is defined |
| `INTERNAL_TRIGGER_TYPE` | `VARCHAR2(19)` |  | Indicates the type of internal trigger on the table |

See Also:

- " [DBA\_INTERNAL\_TRIGGERS](DBA_INTERNAL_TRIGGERS.md) "
- " [USER\_INTERNAL\_TRIGGERS](USER_INTERNAL_TRIGGERS.md) "