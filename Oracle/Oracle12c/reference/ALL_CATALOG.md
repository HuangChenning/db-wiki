---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_CATALOG.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_CATALOG` displays the tables, clusters, views, synonyms, and sequences accessible to the current user.

Related Views

- `DBA_CATALOG` displays all tables, clusters, views, synonyms, and sequences in the entire database.
- `USER_CATALOG` displays the tables, clusters, views, synonyms, and sequences in the current user's schema. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the `TABLE`, `CLUSTER`, `VIEW`, `SYNONYM`, `SEQUENCE`, or `UNDEFINED` |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the `TABLE`, `CLUSTER`, `VIEW`, `SYNONYM`, `SEQUENCE`, or `UNDEFINED` |
| `TABLE_TYPE` | `VARCHAR2(11)` |  | Type of the `TABLE`, `CLUSTER`, `VIEW`, `SYNONYM`, `SEQUENCE`, or `UNDEFINED` |

See Also:

- " [DBA\_CATALOG](DBA_CATALOG.md) "
- " [USER\_CATALOG](USER_CATALOG.md) "