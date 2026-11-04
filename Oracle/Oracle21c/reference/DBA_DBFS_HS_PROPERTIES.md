---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_DBFS_HS_PROPERTIES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.280 DBA\_DBFS\_HS\_PROPERTIES

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