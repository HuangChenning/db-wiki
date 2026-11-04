---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_XTERNAL_TAB_PARTITIONS.html
tags:
  - oracle
  - 12c
  - reference
---

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

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_XTERNAL\_TAB\_PARTITIONS](DBA_XTERNAL_TAB_PARTITIONS.md) "
- " [USER\_XTERNAL\_TAB\_PARTITIONS](USER_XTERNAL_TAB_PARTITIONS.md) "