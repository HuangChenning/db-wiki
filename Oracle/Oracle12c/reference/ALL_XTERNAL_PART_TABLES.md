---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_XTERNAL_PART_TABLES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_XTERNAL_PART_TABLES` describes object-level information for partitioned external tables accessible to the current user.

Related Views

- `DBA_XTERNAL_PART_TABLES` describes object-level information for partitioned external tables in the database
- `USER_XTERNAL_PART_TABLES` describes object-level information for partitioned external tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the partitioned external table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the partitioned external table |
| `TYPE_OWNER` | `CHAR(3)` |  | Owner of the implementation type for the external table access driver |
| `TYPE_NAME` | `VARCHAR2(128)` |  | Name of the implementation type for the external table access driver |
| `DEFAULT_DIRECTORY_OWNER` | `CHAR(3)` |  | Owner of the default directory for the external table |
| `DEFAULT_DIRECTORY_NAME` | `VARCHAR2(128)` |  | Name of the default directory for the external table |
| `REJECT_LIMIT` | `VARCHAR2(40)` |  | Reject limit for the external table, or `UNLIMITED` |
| `ACCESS_TYPE` | `VARCHAR2(7)` |  | Type of access parameters for the external table (`BLOB`, `CLOB`) |
| `ACCESS_PARAMETERS` | `CLOB` |  | Access parameters for the external table |
| `PROPERTY` | `VARCHAR2(10)` |  | Property of the external table (`REFERENCED`, `ALL`) |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_XTERNAL\_PART\_TABLES](DBA_XTERNAL_PART_TABLES.md) "
- " [USER\_XTERNAL\_PART\_TABLES](USER_XTERNAL_PART_TABLES.md) "