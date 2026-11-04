---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XML_NESTED_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.144 ALL\_XML\_NESTED\_TABLES

`ALL_XML_NESTED_TABLES` describes all the tables and their corresponding nested tables accessible to the current user.

Related Views

- `DBA_XML_NESTED_TABLES` describes all the tables and their corresponding nested tables in the database.
- `USER_XML_NESTED_TABLES` describes all the tables and their corresponding nested tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `NESTED_TABLE_NAME` | `VARCHAR2(128)` |  | Name of the nested table |
| `PARENT_COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the parent XML column |

See Also:

- " [DBA\_XML\_NESTED\_TABLES](DBA_XML_NESTED_TABLES.md) "
- " [USER\_XML\_NESTED\_TABLES](USER_XML_NESTED_TABLES.md) "