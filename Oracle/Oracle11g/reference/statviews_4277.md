---
title: DBA_SQL_PLAN_BASELINES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4277.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SQL_PLAN_BASELINES` displays information about the SQL plan baselines currently created for specific SQL statements.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SIGNATURE` | `NUMBER` | `NOT NULL` | Unique SQL identifier generated from normalized SQL text |
| `SQL_HANDLE` | `VARCHAR2(30)` | `NOT NULL` | Unique SQL identifier in string form as a search key |
| `SQL_TEXT` | `CLOB` | `NOT NULL` | Un-normalized SQL text |
| `PLAN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Unique plan identifier in string form as a search key |
| `CREATOR` | `VARCHAR2(30)` |  | User who created the plan baseline |
| `ORIGIN` | `VARCHAR2(14)` |  | How the plan baseline was created: - `MANUAL-LOAD` - `AUTO-CAPTURE` - `MANUAL-SQLTUNE` - `AUTO-SQLTUNE` |
| `PARSING_SCHEMA_NAME` | `VARCHAR2(30)` |  | Name of the parsing schema |
| `DESCRIPTION` | `VARCHAR2(500)` |  | Text description provided for the plan baseline |
| `VERSION` | `VARCHAR2(64)` |  | Database version at the time of plan baseline creation |
| `CREATED` | `TIMESTAMP(6)` | `NOT NULL` | Timestamp when the plan baseline was created |
| `LAST_MODIFIED` | `TIMESTAMP(6)` |  | Timestamp when the plan baseline was last modified |
| `LAST_EXECUTED` | `TIMESTAMP(6)` |  | Timestamp when the plan baseline was last executed |
| `LAST_VERIFIED` | `TIMESTAMP(6)` |  | Timestamp when the plan baseline was last verified |
| `ENABLED` | `VARCHAR2(3)` |  | Indicates whether the plan baseline is enabled (`YES`) or disabled (`NO`) |
| `ACCEPTED` | `VARCHAR2(3)` |  | Indicates whether the plan baseline is accepted (`YES`) or not (`NO`) |
| `FIXED` | `VARCHAR2(3)` |  | Indicates whether the plan baseline is fixed (`YES`) or not (`NO`) |
| `REPRODUCED` <sup>Foot 1</sup> | `VARCHAR2(3)` |  | Indicates whether the optimizer was able to reproduce the plan (`YES`) or not (`NO`). The value of this column is set to `YES` when a plan is initially added to the plan baseline. |
| `AUTOPURGE` | `VARCHAR2(3)` |  | Indicates whether the plan baseline is auto-purged (`YES`) or not (`NO`) |
| `OPTIMIZER_COST` | `NUMBER` |  | Optimizer cost at the time the plan baseline was created |
| `MODULE` <sup>Foot 2</sup> | `VARCHAR2(48)` |  | Application module name |
| `ACTION` <sup>Footref 2</sup> | `VARCHAR2(32)` |  | Application action |
| `EXECUTIONS` | `NUMBER` |  | Number of executions at the time the plan baseline was created |
| `ELAPSED_TIME` | `NUMBER` |  | Total elapsed time at the time the plan baseline was created |
| `CPU_TIME` | `NUMBER` |  | Total CPU time at the time the plan baseline was created |
| `BUFFER_GETS` | `NUMBER` |  | Total buffer gets at the time the plan baseline was created |
| `DISK_READS` | `NUMBER` |  | Total disk reads at the time the plan baseline was created |
| `DIRECT_WRITES` | `NUMBER` |  | Total direct writes at the time the plan baseline was created |
| `ROWS_PROCESSED` | `NUMBER` |  | Total rows processed at the time the plan baseline was created |
| `FETCHES` | `NUMBER` |  | Total number of fetches at the time the plan baseline was created |
| `END_OF_FETCH_COUNT` | `NUMBER` |  | Total number of full fetches at the time the plan baseline was created |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

<sup>Footnote 2</sup> The datatype of this column is `VARCHAR2(64)` starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

- The SQL Plan Management chapter in [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm)
- The `DBMS_SQLTUNE` package in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)