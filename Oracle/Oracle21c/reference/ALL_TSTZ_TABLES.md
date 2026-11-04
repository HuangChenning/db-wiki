---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TSTZ_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.129 ALL\_TSTZ\_TABLES

`ALL_TSTZ_TABLES` displays information about the tables accessible to the current user, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types.

Related Views

- `DBA_TSTZ_TABLES` displays information about all tables in the database, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types.
- `USER_TSTZ_TABLES` displays information about the tables owned by the current user, which have columns defined on `TIMESTAMP WITH TIME ZONE` data types or object types containing attributes of `TIMESTAMP WITH TIME ZONE` data types. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `UPGRADE_IN_PROGRESS` | `VARCHAR2(3)` |  | Indicates whether a table upgrade is in progress (`YES`) or not (`NO`) |

See Also:

- " [DBA\_TSTZ\_TABLES](DBA_TSTZ_TABLES.md) "
- " [USER\_TSTZ\_TABLES](USER_TSTZ_TABLES.md) "