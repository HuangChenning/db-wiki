---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_COLORED_SQL.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.386 DBA\_HIST\_COLORED\_SQL

`DBA_HIST_COLORED_SQL` displays the SQL IDs that have been marked for AWR SQL capture.

If a SQL statement is colored using the `DBMS_WORKLOAD_REPOSITORY.ADD_COLORED_SQL` procedure, then AWR will always capture the SQL statistics for the colored SQL ID. A SQL statement can be removed from coloring using the `DBMS_WORKLOAD_REPOSITORY.REMOVE_COLORED_SQL` procedure.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL ID of colored SQL statement |
| `CREATE_TIME` | `DATE` | `NOT NULL` | Time the SQL ID was colored |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS093) for more information about the `DBMS_WORKLOAD_REPOSITORY` package.