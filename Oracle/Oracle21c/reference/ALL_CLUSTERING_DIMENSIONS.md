---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CLUSTERING_DIMENSIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.126 ALL\_CLUSTERING\_DIMENSIONS

`ALL_CLUSTERING_DIMENSIONS` describes dimension tables associated with tables with an attribute clustering clause that the user owns or has system privileges for.

Related Views

- `DBA_CLUSTERING_DIMENSIONS` describes dimension tables associated with all tables with an attribute clustering clause in the database.
- `USER_CLUSTERING_DIMENSIONS` describes dimension tables associated with tables with an attribute clustering clause owned by the user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the attribute clustering table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute clustering table |
| `DIMENSION_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the dimension table |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the dimension table |

See Also:

- " [DBA\_CLUSTERING\_DIMENSIONS](DBA_CLUSTERING_DIMENSIONS.md) "
- " [USER\_CLUSTERING\_DIMENSIONS](USER_CLUSTERING_DIMENSIONS.md) "
- The `ALTER TABLE` section in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF01001) for information about using the `CLUSTERING` clause to create an attribute clustering table
- The `CREATE TABLE` section in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF01402) for information about using the `CLUSTERING` clause to create an attribute clustering table
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG8170) for information about dimension tables
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG-GUID-6874226F-1DC1-4864-9695-5FBDF646F59D) for information about attribute clustering with zone maps