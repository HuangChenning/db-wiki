---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XTERNAL_LOC_PARTITIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.166 ALL\_XTERNAL\_LOC\_PARTITIONS

`ALL_XTERNAL_LOC_PARTITIONS` describes partition-level locations accessible to the current user.

Related Views

If an external table is partitioned, then the existing `ALL_EXTERNAL_LOCATIONS`, `DBA_EXTERNAL_LOCATIONS`, and `USER_EXTERNAL_LOCATIONS` views will have no rows for that table. Instead, locations will be indicated in the `ALL_XTERNAL_LOC_PARTITIONS`, `DBA_XTERNAL_LOC_PARTITIONS`, `USER_XTERNAL_LOC_PARTITIONS`, `ALL_XTERNAL_LOC_SUBPARTITIONS`, `` `DBA_XTERNAL_LOC_SUBPARTITIONS` ``, and `USER_XTERNAL_LOC_SUBPARTITIONS` views.

- `DBA_XTERNAL_LOC_PARTITIONS` describes partition-level locations in the database.
- `USER_XTERNAL_LOC_PARTITIONS` describes partition-level locations owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the partitioned external table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the partitioned external table |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the partition |
| `LOCATION` | `VARCHAR2(4000)` |  | External table location clause for the partition |
| `DIRECTORY_OWNER` | `CHAR(3)` |  | Owner of the directory containing the external table partition location |
| `DIRECTORY_NAME` | `VARCHAR2(128)` |  | Name of the directory containing the external table partition location |

See Also:

- " [DBA\_XTERNAL\_LOC\_PARTITIONS](DBA_XTERNAL_LOC_PARTITIONS.md) "
- " [USER\_XTERNAL\_LOC\_PARTITIONS](USER_XTERNAL_LOC_PARTITIONS.md) "