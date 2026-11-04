---
title: DBA_ADVISOR_SQLA_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3030.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_SQLA_TABLES` displays cross references between the workload statements and the tables referenced in the statement.

Related View

`USER_ADVISOR_SQLA_TABLES` displays cross references between the workload statements and the tables referenced in the statement for the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the workload object |
| `TASK_ID` | `NUMBER` |  | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(30)` |  | Name of the task |
| `SQL_ID` | `VARCHAR2(13)` |  | SQL identifier of the parent cursor in the library cache |
| `STMT_ID` | `NUMBER` |  | Statement ID |
| `TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Table name |