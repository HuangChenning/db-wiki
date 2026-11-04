---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_REPORTS_CONTROL.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.34 DBA\_HIST\_REPORTS\_CONTROL

`DBA_HIST_REPORTS_CONTROL` contains control information about the report capture mechanism that automatically captures XML reports to Automatic Workload Repository (AWR).

Reports are captured automatically for components like SQL Monitor and Real-Time Automatic Database Diagnostic Monitor (Real-Time ADDM).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` |  | Database ID of the current database for the report |
| `EXECUTION_MODE` | `VARCHAR2(12)` |  | Mode of execution of automatic report capture. Possible values:  - `REGULAR`: Regular per-minute report capture subject to DBTIME budget - `FULL_CAPTURE`: Report capture will be run per minute without the DBTIME budget constraints and is provided to capture a more comprehensive set of reports  NOTE: The `FULL_CAPTURE` mode can be started and ended respectively by executing the `START_REPORT_CAPTURE` and `FINISH_REPORT_CAPTURE` APIs in the `DBMS_AUTO_REPORT` package. At all other times, the execution mode should be `REGULAR`. |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS74518) for more information about the `DBMS_AUTO_REPORT` package