---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_DIM_ATTRIBUTES.html
tags:
  - oracle
  - 12c
  - reference
---

The level columns and the dependent column must be in the same table.

Related Views

- `DBA_DIM_ATTRIBUTES` describes all such dimension relationships in the database.
- `USER_DIM_ATTRIBUTES` describes all such dimension attributes in the current user's schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the dimension |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` |  | Name of the attribute |
| `LEVEL_NAME` | `VARCHAR2(128)` |  | Name of the hierarchy level |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Dependent column name |
| `INFERRED` | `CHAR(1)` |  | Indicates whether the attribute is inferred from a JOIN KEY specification (`Y`) or not (`N`) |

See Also:

- " [DBA\_DIM\_ATTRIBUTES](DBA_DIM_ATTRIBUTES.md) "
- " [USER\_DIM\_ATTRIBUTES](USER_DIM_ATTRIBUTES.md) "