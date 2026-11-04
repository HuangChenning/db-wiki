---
title: "V$ADVISOR_PROGRESS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1008.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ADVISOR_PROGRESS` displays information about the progress of advisor execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID |
| `SERIAL#` | `NUMBER` | Session serial number |
| `USERNAME` | `VARCHAR2(30)` | Oracle user name |
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