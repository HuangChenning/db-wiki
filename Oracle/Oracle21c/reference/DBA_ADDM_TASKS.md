---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADDM_TASKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.17 DBA\_ADDM\_TASKS

`DBA_ADDM_TASKS` displays information about all ADDM tasks in the database.

The view contains one row for each row in the related `DBA_ADVISOR_TASKS` view that has `ADVISOR_NAME=ADDM` and `STATUS=COMPLETED`.

Related View

`USER_ADDM_TASKS` displays information about the ADDM tasks owned by the current user. The view contains one row for each row in the related `USER_ADVISOR_TASKS` view that has `ADVISOR_NAME=ADDM` and `STATUS=COMPLETED`. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `DESCRIPTION` | `VARCHAR2(256)` |  | User-supplied description of the task |
| `ADVISOR_NAME` | `VARCHAR2(128)` |  | Advisor associated with the task |
| `CREATED` | `DATE` | `NOT NULL` | Creation date of the task |
| `LAST_MODIFIED` | `DATE` | `NOT NULL` | Date on which the task was last modified |
| `PARENT_TASK_ID` | `NUMBER` |  | Identifier of the parent task (if the task was created because of the recommendation of another task) |
| `PARENT_RXEC_ID` | `NUMBER` |  | Identifier of the recommendation within the parent task that resulted in the creation of the task |
| `LAST_EXECUTION` | `VARCHAR2(128)` |  | Name of the current or last task execution |
| `EXECUTION_TYPE` | `VARCHAR2(128)` |  | Type of the last execution. This information is optional for single-execution tasks. |
| `EXECUTION_TYPE` # | `NUMBER` |  | Reserved for internal use |
| `EXECUTION_DESCRIPTION` | `VARCHAR2(256)` |  | Optional description of the last execution |
| `EXECUTION_START` | `DATE` |  | Execution start date and time of the task |
| `EXECUTION_END` | `DATE` |  | Execution end date and time of the task |
| `STATUS` | `VARCHAR2(11)` |  | Current operational status of the task:  - `INITIAL` - Initial state of the task; no recommendations are present - `EXECUTING` - Task is currently running - `INTERRUPTED` - Task analysis was interrupted by the user. Recommendation data, if present, can be viewed and reported at this time. - `COMPLETED` - Task successfully completed the analysis operation. Recommendation data can be viewed and reported. - `ERROR` - An error occurred during the analysis operation. Recommendations, if present, can be viewed and reported at this time. |
| `STATUS_MESSAGE` | `VARCHAR2(4000)` |  | Informational message provided by the advisor, regarding the status |
| `PCT_COMPLETION_TIME` | `NUMBER` |  | Percent completion, in terms of time, of the task when it is executing |
| `PROGRESS_METRIC` | `NUMBER` |  | Metric that measures the progress of the task in terms of quality. Each advisor may have its own metric. |
| `METRIC_UNITS` | `VARCHAR2(64)` |  | Unit of the metric used to measure progress |
| `ACTIVITY_COUNTER` | `NUMBER` |  | Counter that is updated frequently by the advisor, denoting that useful work is being performed |
| `RECOMMENDATION_COUNT` | `NUMBER` |  | Number of recommendations produced |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Informational message or an error message indicating the current operation or condition |
| `SOURCE` | `VARCHAR2(128)` |  | Optional name that identifies the creator of the task |
| `HOW_CREATED` | `VARCHAR2(30)` |  | Optional task or template on which the object was based |
| `READ_ONLY` | `VARCHAR2(5)` |  | Indicates whether the task is read-only (`TRUE`) or not (`FALSE`) |
| `SYSTEM_TASK` | `VARCHAR2(5)` |  | Indicates whether the task is a system task (`TRUE`) or not (`FALSE`). The automatic SQL tuning task, `SYS_AUTO_SQL_TUNING_TASK`, is one example of a system task. |
| `ADVISOR_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the advisor |
| `STATUS#` | `NUMBER` |  | Reserved for internal use |
| `DBID` | `NUMBER` |  | The database ID that the task was using |
| `DBNAME` | `VARCHAR2(9)` |  | The name of the database that the task was analyzing |
| `DBVERSION` | `VARCHAR2(17)` |  | The version of the database that the task was analyzing |
| `ANALYSIS_VERSION` | `VARCHAR2(17)` |  | The version of the database that executed the task |
| `BEGIN_SNAP_ID` | `NUMBER` |  | The snapshot ID that starts the analysis period |
| `BEGIN_TIME` | `TIMESTAMP(3)` |  | The `SYSDATE` at the time the `BEGIN_SNAP_ID` was taken |
| `END_SNAP_ID` | `NUMBER` |  | The snapshot ID that ends the analysis period |
| `END_TIME` | `TIMESTAMP(3)` |  | The `SYSDATE` at the time the `END_SNAP_ID` was taken |
| `REQUESTED_ANALYSIS` | `VARCHAR2(8)` |  | The type of ADDM analysis that was requested before task execution, as follows:  `DATABASE` - global ADDM  `INSTANCE` - local ADDM  `PARTIAL` - continental ADDM |
| `ACTUAL_ANALYSIS` | `VARCHAR2(8)` |  | The type of ADDM analysis that was actually performed when the task was executed (either `DATABASE`, `INSTANCE`, or `PARTIAL`) |
| `DATABASE_TIME` | `NUMBER` |  | The total database time accumulated in the analysis period (and analyzed instances) in microseconds |
| `ACTIVE_SESSIONS` | `NUMBER` |  | The average active sessions during the analysis period (and analyzed sessions) |
| `METER_LEVEL` | `VARCHAR2(6)` |  | Reserved for future use |
| `FDG_COUNT` | `NUMBER` |  | The number of findings for the ADDM task, which will appear in the list of findings in a default ADDM report |
| `DB_TYPE_DETECTED` <sup>Foot 1</sup> | `VARCHAR2(10)` |  | Indicates the open mode of the database that the task was analyzing, as detected by ADDM. Possible values:  - `READ-ONLY` - `READ-WRITE` |
| `DB_TYPE_ANALYZED` <sup>Foot 1</sup> | `VARCHAR2(10)` |  | Indicates the assumed open mode of the database that the task was analyzing. If the value of this column is different from the value of the `DB_TYPE_DETECTED` column, then ADDM ignored the detected open mode of the database and analyzed the task as if it occurred on a database with the assumed open mode. Possible values:  - `READ-ONLY` - `READ-WRITE` |
| `CDB_TYPE_DETECTED` <sup>Foot 1</sup> | `VARCHAR2(25)` |  | Indicates the type of database that the task was analyzing, as detected by ADDM. Possible values:  - `NON-CDB` - A non-CDB - `CDB` `ROOT` - The root container in a CDB - `PDB` - A pluggable database (PDB) in a CDB - `AUTONOMOUS` `DATA` `WAREHOUSE` - A PDB that hosts an Oracle Autonomous Data Warehouse Cloud service - `AUTONOMOUS` `OLTP` - A PDB that hosts an Oracle Autonomous Transaction Processing service |
| `CDB_TYPE_ANALYZED` <sup>Foot 1</sup> | `VARCHAR2(25)` |  | Indicates the assumed type of database that the task was analyzing. If the value of this column is different from the value of the `CDB_TYPE_DETECTED` column, then ADDM ignored the detected type of database and analyzed the task as if it occurred on the assumed type of database. Possible values:  - `NON-CDB` - A non-CDB - `CDB` `ROOT` - The root container in a CDB - `PDB` - A pluggable database (PDB) in a CDB - `AUTONOMOUS` `DATA` `WAREHOUSE` - A PDB that hosts an Oracle Autonomous Data Warehouse Cloud service - `AUTONOMOUS` `OLTP` - A PDB that hosts an Oracle Autonomous Transaction Processing service |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 19c. If the task was analyzing a database at a release earlier than Oracle Database 19c, and that database was subsequently upgraded to Oracle Database 19c, then the value of this column is NULL.