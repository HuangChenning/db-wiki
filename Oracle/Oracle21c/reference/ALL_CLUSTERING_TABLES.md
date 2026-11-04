---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CLUSTERING_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.129 ALL\_CLUSTERING\_TABLES

`ALL_CLUSTERING_TABLES` describes tables with an attribute clustering clause that are accessible to the user.

Related Views

- `DBA_CLUSTERING_TABLES` describes all the tables with an attribute clustering clause.
- `USER_CLUSTERING_TABLES` describes the tables with an attribute clustering clause owned by the user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `CLUSTERING_TYPE` | `VARCHAR2(11)` |  | Clustering type:  - `INTERLEAVED` - `LINEAR` |
| `ON_LOAD` | `VARCHAR2(3)` |  | Indicates whether Oracle will cluster data on load (`YES`) or not (`NO`) |
| `ON_DATAMOVEMENT` | `VARCHAR2(3)` |  | Indicates whether Oracle will cluster data on data movement, for example, partition move (`YES`), or not (`NO`) |
| `VALID` | `VARCHAR2(3)` |  | Indicates if clustering is valid (`YES`) or not (`NO`).  For clustering with dimension tables, it is required that the joins of the fact table to the dimensions is via primary key or unique key on the dimension table. Therefore, dimension join keys must have a valid primary key or unique key constraint. If the primary key or unique key constraint is not valid, then clustering will not occur.  If there are no joins in the `CLUSTERING` clause, then the value of this column is `YES`. |
| `WITH_ZONEMAP` | `VARCHAR2(3)` |  | Indicates if a zonemap was created with clustering (`YES`) or not (`NO`). |
| `LAST_LOAD_CLST` | `TIMESTAMP(6)` |  | Last time the clustering occurred on load |
| `LAST_DATAMOVE_CLST` | `TIMESTAMP(6)` |  | Last time the clustering occurred on data movement, for example, partition move |

See Also:

- " [DBA\_CLUSTERING\_TABLES](DBA_CLUSTERING_TABLES.md) "
- " [USER\_CLUSTERING\_TABLES](USER_CLUSTERING_TABLES.md) "
- The `ALTER TABLE` section in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF01001) for information about using the `CLUSTERING` clause to create an attribute clustering table
- The `CREATE TABLE` section in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF01402) for information about using the `CLUSTERING` clause to create an attribute clustering table
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG8170) for information about dimension tables
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG-GUID-6874226F-1DC1-4864-9695-5FBDF646F59D) for information about attribute clustering with zone maps