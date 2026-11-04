---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_HIVE_DATABASES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_HIVE_DATABASES` describes all the Hive schemas accessible to the current user in a Hadoop cluster.

Related Views

- `DBA_HIVE_DATABASES` describes all the Hive schemas in a Hadoop cluster.
- `USER_HIVE_DATABASES` describes all the Hive schemas owned by the current user in a Hadoop cluster.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CLUSTER_ID` | `VARCHAR2(4000)` |  | Hadoop cluster name |
| `DATABASE_NAME` | `VARCHAR2(4000)` |  | Name of the Hive database |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the Hive database |
| `DB_LOCATION` | `VARCHAR2(4000)` |  | Physical location of the Hive database |
| `HIVE_URI` | `VARCHAR2(4000)` |  | The connection string (URI and port number) for the metastore database |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_HIVE\_DATABASES](DBA_HIVE_DATABASES.md) "
- " [USER\_HIVE\_DATABASES](USER_HIVE_DATABASES.md) "