---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_DBFS_HS_FIXED_PROPERTIES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_DBFS_HS_FIXED_PROPERTIES` shows non-modifiable properties of all Database File System (DBFS) hierarchical stores.

Related View

`USER_DBFS_HS_FIXED_PROPERTIES` shows non-modifiable properties of all DBFS hierarchical stores owned by current user. This view does not display the `STORE_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STORE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of store |
| `STORE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of store |
| `PROP_NAME` | `VARCHAR2(256)` | `NOT NULL` | Property name |
| `PROP_VALUE` | `VARCHAR2(256)` | `NOT NULL` | Property value |

See Also:

" [USER\_DBFS\_HS\_FIXED\_PROPERTIES](USER_DBFS_HS_FIXED_PROPERTIES.md) "