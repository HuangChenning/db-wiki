---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CLUSTERING_KEYS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.128 ALL\_CLUSTERING\_KEYS

`ALL_CLUSTERING_KEYS` describes clustering keys for tables with an attribute clustering clause accessible to the user.

Related Views

- `DBA_CLUSTERING_KEYS` describes clustering keys for all tables with an attribute clustering clause.
- `USER_CLUSTERING_KEYS` describes clustering keys for tables with an attribute clustering clause owned by the user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table on which the clustering clause is defined |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table on which the clustering clause is defined |
| `DETAIL_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the detailed table contributing to the clustering keys |
| `DETAIL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the detailed table contributing to the clustering keys |
| `DETAIL_COLUMN` | `VARCHAR2(128)` | `NOT NULL` | Name of the detail column |
| `POSITION` | `NUMBER` | `NOT NULL` | Position of the column in the clustering clause |
| `GROUPID` | `NUMBER` | `NOT NULL` | Group ID of the column in the clustering clause |

See Also:

- " [DBA\_CLUSTERING\_KEYS](DBA_CLUSTERING_KEYS.md) "
- " [USER\_CLUSTERING\_KEYS](USER_CLUSTERING_KEYS.md) "
- The `ALTER TABLE` section in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF01001) for information about using the `CLUSTERING` clause to create an attribute clustering table
- The `CREATE TABLE` section in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF01402) for information about using the `CLUSTERING` clause to create an attribute clustering table
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG8170) for information about dimension tables
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG-GUID-6874226F-1DC1-4864-9695-5FBDF646F59D) for information about attribute clustering with zone maps