---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_PARTIAL_DROP_TABS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.7 ALL\_PARTIAL\_DROP\_TABS

Such operations might have been interrupted by the user or by a system crash.

Related Views

- `DBA_PARTIAL_DROP_TABS` describes all tables in the database that have partially completed `DROP COLUMN` operations.
- `USER_PARTIAL_DROP_TABS` describes tables in the schema of the current user that have partially completed `DROP COLUMN` operations. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |

See Also:

- " [DBA\_PARTIAL\_DROP\_TABS](DBA_PARTIAL_DROP_TABS.md) "
- " [USER\_PARTIAL\_DROP\_TABS](USER_PARTIAL_DROP_TABS.md) "