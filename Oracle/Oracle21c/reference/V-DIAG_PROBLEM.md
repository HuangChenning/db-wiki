---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DIAG_PROBLEM.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.179 V$DIAG\_PROBLEM

`V$DIAG_PROBLEM` contains information about all problem metadata records present in the Automatic Diagnostic Repository (ADR) for the current container (PDB).

| Column | Datatype | Description |
| --- | --- | --- |
| `PROBLEM_ID` | `NUMBER` | Displays the ID for the current problem |
| `PROBLEM_KEY` | `VARCHAR2(552)` | Displays the problem key for the current problem |
| `FIRST_INCIDENT` | `NUMBER` | Displays the first incident ID for the current problem |
| `FIRSTINC_TIME` | `TIMESTAMP(9) WITH TIME ZONE` | Displays the timestamp when the first incident occurred for the current problem |
| `LAST_INCIDENT` | `NUMBER` | Displays the last incident ID for the current problem |
| `LASTINC_TIME` | `TIMESTAMP(9) WITH TIME ZONE` | Displays the timestamp when the last incident occurred for the current problem |
| `IMPACT1` | `NUMBER` | Displays the first impact for the current problem |
| `IMPACT2` | `NUMBER` | Displays the second impact for the current problem |
| `IMPACT3` | `NUMBER` | Displays the third impact for the current problem |
| `IMPACT4` | `NUMBER` | Displays the fourth impact for the current problem |
| `SERVICE_REQUEST` | `VARCHAR2(66)` | Displays the service request number for the current problem, if a number has been entered in Support Workbench |
| `BUG_NUMBER` | `VARCHAR2(66)` | Displays the bug number for the current problem, if a number has been entered in Support Workbench |
| `CON_UID` | `NUMBER` | Displays the container unique ID to which the data pertains |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |