---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ADVISOR_PROGRESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.11 V$ADVISOR\_PROGRESS

`V$ADVISOR_PROGRESS` displays information about the progress of advisor execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID |
| `SERIAL#` | `NUMBER` | Session serial number |
| `USERNAME` | `VARCHAR2(128)` | Oracle user name |
| `OPNAME` | `VARCHAR2(64)` | Operation name |
| `ADVISOR_NAME` | `VARCHAR2(64)` | Advisor name |
| `TASK_ID` | `NUMBER` | Task ID |
| `TARGET_DESC` | `VARCHAR2(32)` | Description of the target of the advisor |
| `SOFAR` | `NUMBER` | Amount of work done so far |
| `TOTALWORK` | `NUMBER` | Total work to be done |
| `UNITS` | `VARCHAR2(32)` | Units that the work is measured in |
| `BENEFIT_SOFAR` | `NUMBER` | Benefit obtained so far |
| `BENEFIT_MAX` | `NUMBER` | Estimate of maximum benefit that could be obtained |
| `FINDINGS` | `NUMBER` | Number of findings so far |
| `RECOMMENDATIONS` | `NUMBER` | Number of recommendations so far |
| `TIME_REMAINING` | `NUMBER` | Estimate of time remaining for the completion of the task (in seconds) |
| `START_TIME` | `DATE` | Start time of the task |
| `LAST_UPDATE_TIME` | `DATE` | Last time progress was posted |
| `ELAPSED_SECONDS` | `NUMBER` | Elapsed time so far |
| `ADVISOR_METRIC1` | `NUMBER` | Value of the advisor-specific metric |
| `METRIC1_DESC` | `VARCHAR2(64)` | Description of the advisor-specific metric |
| `EXECUTION_TYPE` | `VARCHAR2(64)` | Type of the last execution. This information is optional for single-execution tasks. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |