---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_HIVE_PART_KEY_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.225 ALL\_HIVE\_PART\_KEY\_COLUMNS

`ALL_HIVE_PART_KEY_COLUMNS` provides information about all Hive table partition columns accessible to the current user in the database.

Related Views

- `DBA_HIVE_PART_KEY_COLUMNS` provides information about all Hive table partition columns in the database.
- `USER_HIVE_PART_KEY_COLUMNS` provides information about all Hive table partition columns owned by the current user in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CLUSTER_ID` | `VARCHAR2(4000)` |  | Hadoop cluster name |
| `DATABASE_NAME` | `VARCHAR2(4000)` |  | Hive database where the Hive table resides |
| `TABLE_NAME` | `VARCHAR2(4000)` |  | Hive table name |
| `OWNER` | `VARCHAR2(4000)` |  | Owner of the Hive table |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Partition column name |
| `COLUMN_TYPE` | `VARCHAR2(4000)` |  | Partition column type |
| `COLUMN_POSITION` | `NUMBER` |  | Partition column position in the Hive partition specification |
| `ORACLE_COLUMN_TYPE` | `VARCHAR2(4000)` |  | Equivalent Oracle data type of the Hive column |