---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_ILMRESULTS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_ILMRESULTS` displays information on data movement-related Automatic Data Optimization jobs in the database.

Related View

`USER_ILMRESULTS` displays information on data movement-related Automatic Data Optimization jobs for tasks created by the user.

Note:

Automatic Data Optimization is supported in multitenant environments starting with Oracle Database 12c Release 2 (12.2.0.1).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER` |  | Number that uniquely identifies a specific Automatic Data Optimization task |
| `JOB_NAME` | `VARCHAR2(128)` |  | Name of the Automatic Data Optimization job |
| `JOB_STATE` | `VARCHAR2(35)` |  | State of the job. Possible values:  - `JOB CREATED` - `COMPLETED SUCCESSFULLY` - `FAILED` - `STOPPED` - `JOB CREATION FAILED` - `DEPENDENT OBJECTS BEING REBUILT` - `FAILED TO REBUILD DEPENDENT OBJECTS` |
| `START_TIME` | `TIMESTAMP(6)` |  | Start time of the Automatic Data Optimization job |
| `COMPLETION_TIME` | `TIMESTAMP(6)` |  | Completion time of the Automatic Data Optimization job |