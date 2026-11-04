---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_DBFS_HS_COMMANDS.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.252 DBA\_DBFS\_HS\_COMMANDS

`DBA_DBFS_HS_COMMANDS` shows all the registered store commands for all Database File System (DBFS) hierarchical stores.

Related View

`USER_DBFS_HS_COMMANDS` shows all the registered store commands for all DBFS hierarchical stores owned by current user. This view does not display the `STOREOWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STORENAME` | `VARCHAR2(256)` |  | Name of store |
| `STOREOWNER` | `VARCHAR2(64)` |  | Owner of store |
| `STORECOMMAND` | `VARCHAR2(512)` |  | Store command |
| `STOREFLAGS` | `NUMBER` |  | Valid values are:  - `1` - Indicates that the command is sent to the device before put - `2` - Indicates that the command is sent to the device before get |

See Also:

" [USER\_DBFS\_HS\_COMMANDS](USER_DBFS_HS_COMMANDS.md) "