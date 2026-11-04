---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RECYCLEBIN.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.270 DBA\_RECYCLEBIN

`DBA_RECYCLEBIN` displays information about all recycle bins in the database.

Related View

`USER_RECYCLEBIN` displays information about the recycle bin owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Name of the original owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | New name of the object |
| `ORIGINAL_NAME` | `VARCHAR2(128)` |  | Original name of the object |
| `OPERATION` | `VARCHAR2(9)` |  | Operation carried out on the object:  - `DROP` - Object was dropped - `TRUNCATE` - Object was truncated 	Note: The Oracle Database currently only supports recovering dropped objects from the recycle bin. The truncated objects cannot be recovered. |
| `TYPE` | `VARCHAR2(25)` |  | Type of the object:  - `TABLE` - `NORMAL INDEX` - `BITMAP INDEX` - `NESTED TABLE` - `LOB` - `LOB INDEX` - `DOMAIN INDEX` - `IOT TOP INDEX` - `IOT OVERFLOW SEGMENT` - `IOT MAPPING TABLE` - `TRIGGER` - `Table Partition` - `Table Composite Partition` - `Index Partition` - `Index Composite Partition` - `LOB Partition` - `LOB Composite Partition` |
| `TS_NAME` | `VARCHAR2(30)` |  | Name of the tablespace to which the object belongs |
| `CREATETIME` | `VARCHAR2(19)` |  | Timestamp for the creation of the object |
| `DROPTIME` | `VARCHAR2(19)` |  | Timestamp for the dropping of the object |
| `DROPSCN` | `NUMBER` |  | System change number (SCN) of the transaction which moved the object to the recycle bin |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the partition which was dropped |
| `CAN_UNDROP` | `VARCHAR2(3)` |  | Indicates whether the object can be undropped (`YES`) or not (`NO`) |
| `CAN_PURGE` | `VARCHAR2(3)` |  | Indicates whether the object can be purged (`YES`) or not (`NO`) |
| `RELATED` | `NUMBER` | `NOT NULL` | Object number of the parent object |
| `BASE_OBJECT` | `NUMBER` | `NOT NULL` | Object number of the base object |
| `PURGE_OBJECT` | `NUMBER` | `NOT NULL` | Object number for the object which gets purged |
| `SPACE` | `NUMBER` |  | Number of blocks used by the object |

See Also:

" [USER\_RECYCLEBIN](USER_RECYCLEBIN.md) "