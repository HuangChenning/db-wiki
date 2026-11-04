---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XTERNAL_PART_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.168 ALL\_XTERNAL\_PART\_TABLES

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
| `INMEMORY` <sup>Foot 1</sup> | `VARCHAR2(8)` |  | Indicates whether the In-Memory Column Store (IM column store) is by default enabled (`ENABLED`), disabled (`DISABLED`), or not specified (`NONE`) for partitions in the external table |
| `INMEMORY_COMPRESSION` <sup>Foot 1</sup> | `VARCHAR2(17)` |  | Indicates the default compression level for the IM column store:  - `NO MEMCOMPRESS` - `FOR DML` - `FOR QUERY [ LOW \| HIGH ]` - `FOR CAPACITY [ LOW \| HIGH ]` - `NULL` |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c. It appears in the USER\_XTERNAL\_PART\_TABLES view and is omitted from the ALL\_XTERNAL\_PART\_TABLES and DBA\_XTERNAL\_PART\_TABLES views.

See Also:

- " [DBA\_XTERNAL\_PART\_TABLES](DBA_XTERNAL_PART_TABLES.md) "
- " [USER\_XTERNAL\_PART\_TABLES](USER_XTERNAL_PART_TABLES.md) "