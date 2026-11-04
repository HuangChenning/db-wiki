---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_HIVE_COLUMNS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_HIVE_COLUMNS` describes all Hive columns accessible to the current user in a Hive metastore.

Related Views

- `DBA_HIVE_COLUMNS` describes all Hive columns in a Hive metastore.
- `USER_HIVE_COLUMNS` describes all Hive columns owned by the current user in a Hive metastore.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CLUSTER_ID` | `VARCHAR2(4000)` |  | Identifier for the Hadoop cluster |
| `DATABASE_NAME` | `VARCHAR2(4000)` |  | Hive database where the owning Hive table resides |
| `TABLE_NAME` | `VARCHAR2(4000)` |  | Hive table name that the column belongs to |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Hive column name |
| `HIVE_COLUMN_TYPE` | `VARCHAR2(4000)` |  | Data type of the Hive column |
| `ORACLE_COLUMN_TYPE` | `VARCHAR2(4000)` |  | Equivalent Oracle data type of the Hive column |
| `LOCATION` | `VARCHAR2(4000)` |  | Physical location of the Hive table |
| `OWNER` | `VARCHAR2(4000)` |  | Owner of the Hive table |
| `CREATION_TIME` | `DATE` |  | Time that the Hive column was created |
| `HIVE_URI` | `VARCHAR2(4000)` |  | The connection string (URI and port number) for the metastore database |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_HIVE\_COLUMNS](DBA_HIVE_COLUMNS.md) "
- " [USER\_HIVE\_COLUMNS](USER_HIVE_COLUMNS.md) "