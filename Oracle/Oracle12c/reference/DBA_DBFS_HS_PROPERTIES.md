---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_DBFS_HS_PROPERTIES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_DBFS_HS_PROPERTIES` shows modifiable properties of all Database File System (DBFS) hierarchical stores.

Related View

`USER_DBFS_HS_PROPERTIES` shows modifiable properties of all DBFS hierarchical stores owned by current user. This view does not display the `STOREOWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STORENAME` | `VARCHAR2(256)` |  | Name of store |
| `STOREOWNER` | `VARCHAR2(64)` |  | Owner of store |
| `PROPERTYNAME` | `VARCHAR2(256)` |  | Property name |
| `PROPERTYVALUE` | `VARCHAR2(256)` |  | Property value |

See Also:

" [USER\_DBFS\_HS\_PROPERTIES](USER_DBFS_HS_PROPERTIES.md) "