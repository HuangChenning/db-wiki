---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SQL_PLAN_BASELINES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.366 DBA\_SQL\_PLAN\_BASELINES

`DBA_SQL_PLAN_BASELINES` displays information about the SQL plan baselines currently created for specific SQL statements.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SIGNATURE` | `NUMBER` | `NOT NULL` | Unique SQL identifier generated from normalized SQL text |
| `SQL_HANDLE` | `VARCHAR2(30)` | `NOT NULL` | Unique SQL identifier in string form as a search key |
| `SQL_TEXT` | `CLOB` | `NOT NULL` | Un-normalized SQL text |
| `PLAN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Unique plan identifier in string form as a search key |
| `CREATOR` | `VARCHAR2(128)` |  | User who created the plan baseline |
| `ORIGIN` | `VARCHAR2(29)` |  | How the plan baseline was created:  - `ADDM-SQLTUNE` - `AUTO-CAPTURE` - `AUTO-SQLTUNE` - `EVOLVE-AUTO-INDEX-LOAD` - `EVOLVE-CREATE-FROM-ADAPTIVE` - `EVOLVE-LOAD-FROM-AWR` - `EVOLVE-LOAD-FROM-CURSOR-CACHE` - `EVOLVE-LOAD-FROM-STS` - `MANUAL-LOAD` - `MANUAL-LOAD-FROM-AWR` - `MANUAL-LOAD-FROM-CURSOR-CACHE` - `MANUAL-LOAD-FROM-STS` - `MANUAL-SQLTUNE` - `STORED-OUTLINE` |
| `PARSING_SCHEMA_NAME` | `VARCHAR2(128)` |  | Name of the parsing schema |
| `DESCRIPTION` | `VARCHAR2(500)` |  | Text description provided for the plan baseline |
| `VERSION` | `VARCHAR2(64)` |  | Database version at the time of plan baseline creation |
| `CREATED` | `TIMESTAMP(6)` | `NOT NULL` | Timestamp when the plan baseline was created |
| `LAST_MODIFIED` | `TIMESTAMP(6)` |  | Timestamp when the plan baseline was last modified |
| `LAST_EXECUTED` | `TIMESTAMP(6)` |  | Timestamp when the plan baseline was last executed  Note: For performance reasons, this column is not updated immediately after each execution of the plan baseline. Therefore, the plan baseline may have been executed more recently than the value of this column indicates. |
| `LAST_VERIFIED` | `TIMESTAMP(6)` |  | Timestamp when the plan baseline was last verified |
| `ENABLED` | `VARCHAR2(3)` |  | Indicates whether the plan baseline is enabled (`YES`) or disabled (`NO`) |
| `ACCEPTED` | `VARCHAR2(3)` |  | Indicates whether the plan baseline is accepted (`YES`) or not (`NO`) |
| `FIXED` | `VARCHAR2(3)` |  | Indicates whether the plan baseline is fixed (`YES`) or not (`NO`) |
| `REPRODUCED` | `VARCHAR2(3)` |  | Indicates whether the optimizer was able to reproduce the plan (`YES`) or not (`NO`). The value of this column is set to `YES` when a plan is initially added to the plan baseline. |
| `AUTOPURGE` | `VARCHAR2(3)` |  | Indicates whether the plan baseline is auto-purged (`YES`) or not (`NO`) |
| `ADAPTIVE` | `VARCHAR2(3)` |  | Indicates whether a plan that is automatically captured by SQL plan management is marked adaptive or not.  When a new adaptive plan is found for a SQL statement that has an existing SQL plan baseline, that new plan will be added to the SQL plan baseline as an unaccepted plan, and the `ADAPTIVE` column will be marked `YES`. When this new plan is verified (either manually or via the auto evolve task), the plan will be test executed and the final plan determined at execution will become an accepted plan if its performance is better than the existing plan baseline. At this point, the value of the `ADAPTIVE` column is set to `NO` since the plan is no longer adaptive, but resolved. |
| `OPTIMIZER_COST` | `NUMBER` |  | Optimizer cost at the time the plan baseline was created |
| `MODULE` | `VARCHAR2(64)` |  | Application module name |
| `ACTION` | `VARCHAR2(64)` |  | Application action |
| `EXECUTIONS` <sup>Foot 1</sup> | `NUMBER` |  | Number of executions at the time the plan baseline was created |
| `ELAPSED_TIME` <sup>Foot 1</sup> | `NUMBER` |  | Total elapsed time (in microseconds) at the time the plan baseline was created |
| `CPU_TIME` <sup>Foot 1</sup> | `NUMBER` |  | Total CPU time (in microseconds) at the time the plan baseline was created |
| `BUFFER_GETS` <sup>Foot 1</sup> | `NUMBER` |  | Total buffer gets at the time the plan baseline was created |
| `DISK_READS` <sup>Foot 1</sup> | `NUMBER` |  | Total disk reads at the time the plan baseline was created |
| `DIRECT_WRITES` <sup>Foot 1</sup> | `NUMBER` |  | Total direct writes at the time the plan baseline was created |
| `ROWS_PROCESSED` <sup>Foot 1</sup> | `NUMBER` |  | Total rows processed at the time the plan baseline was created |
| `FETCHES` <sup>Foot 1</sup> | `NUMBER` |  | Total number of fetches at the time the plan baseline was created |
| `END_OF_FETCH_COUNT` <sup>Foot 1</sup> | `NUMBER` |  | Total number of full fetches at the time the plan baseline was created |

<sup>Footnote 1</sup>

If the value of the `ORIGIN` column is equal to `AUTO-CAPTURE`, then data for this column is not populated.

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL94621) for more information about SQL plan baselines
- The `DBMS_SQLTUNE` package in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS220)