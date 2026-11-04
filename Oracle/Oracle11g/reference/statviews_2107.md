---
title: ALL_TAB_MODIFICATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2107.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TAB_MODIFICATIONS` describes tables accessible to the current user that have been modified since the last time statistics were gathered on the tables.

Related Views

- `DBA_TAB_MODIFICATIONS` describes such information for all tables in the database.
- `USER_TAB_MODIFICATIONS` describes such information for tables owned by the current user. This view does not display the `TABLE_OWNER` column.

Note:

These views are populated only for tables with the `MONITORING` attribute. They are intended for statistics collection over a long period of time. For performance reasons, the Oracle Database does not populate these views immediately when the actual modifications occur. Run the `FLUSH_DATABASE_MONITORING_INFO` procedure in the `DBMS_STATS` PL/SQL package to populate these views with the latest information. The `ANALYZE_ANY` system privilege is required to run this procedure.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the modified table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the modified table |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the modified partition |
| `SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Name of the modified subpartition |
| `INSERTS` | `NUMBER` |  | Approximate number of inserts since the last time statistics were gathered |
| `UPDATES` | `NUMBER` |  | Approximate number of updates since the last time statistics were gathered |
| `DELETES` | `NUMBER` |  | Approximate number of deletes since the last time statistics were gathered |
| `TIMESTAMP` | `DATE` |  | Indicates the last time the table was modified |
| `TRUNCATED` | `VARCHAR2(3)` |  | Indicates whether the table has been truncated since the last analyze (`YES`) or not (`NO`) |
| `DROP_SEGMENTS` | `NUMBER` |  | Number of partition and subpartition segments dropped since the last analyze |