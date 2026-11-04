---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_HIVE_TAB_PARTITIONS.html
tags:
  - oracle
  - 12c
  - reference
---

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

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_HIVE\_TAB\_PARTITIONS](DBA_HIVE_TAB_PARTITIONS.md) "
- " [USER\_HIVE\_TAB\_PARTITIONS](USER_HIVE_TAB_PARTITIONS.md) "