---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_XML_NESTED_TABLES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_XML_NESTED_TABLES` describes all the tables and their corresponding nested tables accessible to the current user.

Related Views

- `DBA_XML_NESTED_TABLES` describes all the tables and their corresponding nested tables in the database.
- `USER_XML_NESTED_TABLES` describes all the tables and their corresponding nested tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `NESTED_TABLE_NAME` | `VARCHAR2(128)` |  | Name of the nested table |
| `PARENT_COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the parent XML column  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- " [DBA\_XML\_NESTED\_TABLES](DBA_XML_NESTED_TABLES.md) "
- " [USER\_XML\_NESTED\_TABLES](USER_XML_NESTED_TABLES.md) "