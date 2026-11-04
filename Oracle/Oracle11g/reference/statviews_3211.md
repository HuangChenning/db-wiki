---
title: DBA_HIST_COLORED_SQL
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3211.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_COLORED_SQL` displays the SQL IDs that have been marked for AWR SQL capture. If a SQL statement is colored using the `DBMS_WORKLOAD_REPOSITORY.ADD_COLORED_SQL` procedure, then AWR will always capture the SQL statistics for the colored SQL ID. A SQL statement can be removed from coloring using the `DBMS_WORKLOAD_REPOSITORY.REMOVE_COLORED_SQL` procedure.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL ID of colored SQL statement |
| `CREATE_TIME` | `DATE` | `NOT NULL` | Time the SQL ID was colored |