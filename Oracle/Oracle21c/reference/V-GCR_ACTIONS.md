---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-GCR_ACTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.246 V$GCR\_ACTIONS

`V$GCR_ACTIONS` displays information about the current status of the actions defined to the GCR component that runs under the LMHB background process to detect and mitigate potential issues in the cluster instances.

| Column | Datatype | Description |
| --- | --- | --- |
| `ACTION_ID` | `NUMBER` | Action identification number as used internally to refer to the metric |
| `ACTION_NAME` | `VARCHAR2(40)` | Name of the action |
| `ENVIRONMENT` | `NUMBER` | Environment that the action should run in:  - `0`: Nowhere (do not run) - `1`: Oracle ASM instance only - `2`: Oracle Database instance only - `3`: Oracle ASM and Oracle Database instance - `4`: Standby instance - `5`: Oracle ASM and Standby instance - `6`: Oracle Database and Standby instance - `7`: Oracle Database, Oracle ASM, and Standby instance - `15`: All instance types |
| `FLAGS` | `NUMBER` | Various flags describing the action. Used only by Oracle for diagnosis. |
| `ACTIVE` | `VARCHAR2(9)` | Whether the action is active or not: - `ACTIVE`: Action is active. - `INACTIVE`: Action is disabled. |
| `STATUS_CHANGE_TIME` | `TIMESTAMP(6)` | Time of last action change of status |
| `LAST_RAN_ITERATION` | `NUMBER` | Iteration of the last time the action ran |
| `LAST_RAN_TIME` | `TIMESTAMP(6)` | Time of last run |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |