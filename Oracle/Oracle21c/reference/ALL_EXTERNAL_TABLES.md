---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_EXTERNAL_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.190 ALL\_EXTERNAL\_TABLES

`ALL_EXTERNAL_TABLES` describes the external tables accessible to the current user.

Related Views

- `DBA_EXTERNAL_TABLES` describes all external tables in the database.
- `USER_EXTERNAL_TABLES` describes the external tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the external table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the external table |
| `TYPE_OWNER` | `CHAR(3)` |  | Owner of the implementation type for the external table access driver |
| `TYPE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the implementation type for the external table access driver |
| `DEFAULT_DIRECTORY_OWNER` | `CHAR(3)` |  | Owner of the default directory for the external table |
| `DEFAULT_DIRECTORY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the default directory for the external table |
| `REJECT_LIMIT` | `VARCHAR2(40)` |  | Reject limit for the external table, or `UNLIMITED` |
| `ACCESS_TYPE` | `VARCHAR2(7)` |  | Type of access parameters for the external table:  - `BLOB` - `CLOB` |
| `ACCESS_PARAMETERS` | `CLOB` |  | Access parameters for the external table |
| `PROPERTY` | `VARCHAR2(10)` |  | Property of the external table:  - `REFERENCED` - Referenced columns - `ALL` - All columns |
| `INMEMORY` | `VARCHAR2(8)` |  | Indicates whether the In-Memory Column Store (IM column store) is enabled (`ENABLED`) or disabled (`DISABLED`) for this table |
| `INMEMORY_COMPRESSION` | `VARCHAR2(17)` |  | Indicates the compression level for the IM column store:  - `NO MEMCOMPRESS` - `FOR DML` - `FOR CAPACITY [ HIGH \| LOW ]` - `FOR QUERY [ HIGH \| LOW ]` - `NULL`  This column has a value based on where the segments lie for a table. For example, if the table is partitioned and is enabled for the IM column store, the value is `NULL` for `ALL_EXTERNAL_TABLES` but non- `NULL` for `ALL_XTERNAL_TAB_PARTITIONS`. |

See Also:

- " [DBA\_EXTERNAL\_TABLES](DBA_EXTERNAL_TABLES.md) "
- " [USER\_EXTERNAL\_TABLES](USER_EXTERNAL_TABLES.md) "