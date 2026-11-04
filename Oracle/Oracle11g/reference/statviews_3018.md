---
title: DBA_ADVISOR_EXECUTIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3018.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_EXECUTIONS` displays metadata information for task executions. For example, the SQL Performance Analyzer creates a minimum of three executions to perform a change impact analysis on a SQL workload. The first one collects performance data for the version of the workload before the change, the second one collects data for the version of the workload after the change, and the third one performs impact analysis. All of these executions belong to the same task and are grouped into this view. Similarly, the automatic SQL tuning task, `SYS_AUTO_SQL_TUNING_TASK`, creates a new execution for each tuning run.

Related View

`USER_ADVISOR_EXECUTIONS` displays metadata information for task executions owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(30)` |  | Name of the task |
| `EXECUTION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the task execution with which this entry (row) is associated |
| `EXECUTION_ID` | `NUMBER` | `NOT NULL` | Execution ID |
| `DESCRIPTION` | `VARCHAR2(256)` |  | User-supplied description of the task |
| `EXECUTION_TYPE` | `VARCHAR2(30)` |  | Type of the last execution (optional for single-execution tasks) |
| `EXECUTION_TYPE#` | `NUMBER` |  | Reserved for internal use |
| `EXECUTION_START` | `DATE` |  | Execution start date and time |
| `EXECUTION_LAST_MODIFIED` | `DATE` | `NOT NULL` | Last modified date and time for the execution |
| `EXECUTION_END` | `DATE` |  | Execution end date and time |
| `ADVISOR_NAME` | `VARCHAR2(30)` |  | Advisor associated with the task |
| `ADVISOR_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the advisor |
| `STATUS` | `VARCHAR2(11)` |  | Current operational status of the task: |
| `STATUS#` | `NUMBER` | `NOT NULL` | Reserved for internal use |
| `STATUS_MESSAGE` | `VARCHAR2(4000)` |  | Informational message provided by the advisor regarding the status |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Informational message or an error message indicating the current operation or condition |