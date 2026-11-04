---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_XTERNAL_TAB_PARTITIONS.html
tags:
  - oracle
  - 19c
  - reference
---

## 3.167 ALL\_XTERNAL\_TAB\_PARTITIONS

`ALL_XTERNAL_TAB_PARTITIONS` describes partition-level information for partitioned external tables accessible to the current user.

Related Views

- `DBA_XTERNAL_TAB_PARTITIONS` describes partition-level information for partitioned external tables in the databae
- `USER_XTERNAL_TAB_PARTITIONS` describes partition-level information for partitioned external tables owned by the current user. This view does not display the `TABLE_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the partitioned external table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the partitioned external table |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the partition |
| `DEFAULT_DIRECTORY_OWNER` | `CHAR(3)` |  | Owner of the default directory for the external table partition |
| `DEFAULT_DIRECTORY_NAME` | `VARCHAR2(128)` |  | Name of the default directory for the external table partition |
| `ACCESS_TYPE` | `VARCHAR2(7)` |  | Type of access parameters for the partition (`BLOB`, `CLOB`) |
| `ACCESS_PARAMETERS` | `CLOB` |  | Access parameters for the external table partition |

See Also:

- " [DBA\_XTERNAL\_TAB\_PARTITIONS](DBA_XTERNAL_TAB_PARTITIONS.md) "
- " [USER\_XTERNAL\_TAB\_PARTITIONS](USER_XTERNAL_TAB_PARTITIONS.md) "