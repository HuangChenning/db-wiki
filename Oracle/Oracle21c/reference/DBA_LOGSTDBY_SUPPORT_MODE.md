---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LOGSTDBY_SUPPORT_MODE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.170 DBA\_LOGSTDBY\_SUPPORT\_MODE

`DBA_LOGSTDBY_SUPPORT_MODE` displays information about whether tables in the database are supported for logical standby.

The query results for this view depend on whether the database is currently undergoing a manual rolling upgrade performed using transient logical standby databases. If the database is undergoing such an upgrade, then this view displays information about whether tables in the database are supported for transient logical standby. If the database is not undergoing such an upgrade, then this view displays information about whether tables in the database are supported for logical standby.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Table owner |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Table name |
| `SUPPORT_MODE` | `VARCHAR2(11)` |  | If the database is currently undergoing a manual rolling upgrade performed using transient logical standby databases, then this column indicates whether the table is supported for transient logical standby. Otherwise, this column indicates whether the table is supported for logical standby.  Possible values:  - `SUPPORTED` - The table is fully supported - `INTERNAL` - The table is not supported because it contains data that should not be replicated. Such tables include mapping tables for index-organized tables, storage tables for nested tables, materialized view logs, secondary objects associated with domain indexes, and temporary tables. - `UNSUPPORTED` - The table is not supported because it contains a data type that is not supported or uses a feature that is not supported |
| `EXPLANATION` | `VARCHAR2(4000)` |  | Reason the table is not fully supported for transient logical standby  This column is populated only when all of the following conditions are met:  - The database is currently undergoing a manual rolling upgrade using transient logical standby databases - The value of the `COMPATIBLE` initialization parameter is `20.0` or higher - The value of the `SUPPORT_MODE` column is `INTERNAL` or `UNSUPPORTED` |

Note:

This view is available starting with Oracle Database 21c.