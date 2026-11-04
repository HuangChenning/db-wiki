---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_HIVE_TAB_PARTITIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.226 ALL\_HIVE\_TAB\_PARTITIONS

`ALL_HIVE_TAB_PARTITIONS` provides information about all Hive table partitions accessible to the current user in the database.

Related Views

- `DBA_HIVE_TAB_PARTITIONS` provides information about all Hive table partitions in the database.
- `USER_HIVE_TAB_PARTITIONS` provides information about all Hive table partitions owned by the current user in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CLUSTER_ID` | `VARCHAR2(4000)` |  | Hadoop cluster name |
| `DATABASE_NAME` | `VARCHAR2(4000)` |  | Hive database where the Hive table resides |
| `TABLE_NAME` | `VARCHAR2(4000)` |  | Hive table name |
| `LOCATION` | `VARCHAR2(4000)` |  | Physical location of the Hive partition |
| `OWNER` | `VARCHAR2(4000)` |  | Owner of the Hive table |
| `PARTITION_SPECS` | `VARCHAR2(4000)` |  | The current Hive partition specification |
| `PART_SIZE` | `NUMBER` |  | Partition size in bytes |
| `CREATION_TIME` | `DATE` |  | Time that the partition was created |

See Also:

- " [DBA\_HIVE\_TAB\_PARTITIONS](DBA_HIVE_TAB_PARTITIONS.md) "
- " [USER\_HIVE\_TAB\_PARTITIONS](USER_HIVE_TAB_PARTITIONS.md) "