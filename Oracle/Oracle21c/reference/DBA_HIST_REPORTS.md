---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_REPORTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.33 DBA\_HIST\_REPORTS

`DBA_HIST_REPORTS` displays information about XML reports captured into Automatic Workload Repository (AWR).

The reports themselves belong to components such as SQL Monitor, DBOP, and Real-Time ADDM.

Each XML report contains details about some activity of a component. For example, a SQL Monitor report contains a detailed report about a particular execution of a SQL statement, or a Real-Time ADDM report contains system performance data analyzed by Real-Time ADDM.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | ID of the first Automatic Workload Repository (AWR) snapshot that will be taken after this report is generated |
| `DBID` | `NUMBER` |  | Database ID of the current database for the report |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number (for an Oracle RAC system) |
| `REPORT_ID` | `NUMBER` |  | ID of the captured report |
| `COMPONENT_ID` | `NUMBER` |  | ID of the component (for example, SQL Monitor) whose report is captured |
| `SESSION_ID` | `NUMBER` |  | ID of the session corresponding to the captured report (currently used only for SQL Monitor reports) |
| `SESSION_SERIAL#` | `NUMBER` |  | Session serial number corresponding to the captured report (currently used only for SQL Monitor reports) |
| `PERIOD_START_TIME` | `DATE` |  | Time when the activity period started |
| `PERIOD_END_TIME` | `DATE` |  | Time when the activity period ended |
| `GENERATION_TIME` | `DATE` |  | Time when this report was generated |
| `COMPONENT_NAME` | `VARCHAR2(128)` |  | Name of the component whose report this is |
| `REPORT_NAME` | `VARCHAR2(128)` |  | Name of this report |
| `REPORT_PARAMETERS` | `VARCHAR2(1024)` |  | Parameters associated with this report |
| `KEY1` | `VARCHAR2(128)` |  | Key1 associated with the captured report |
| `KEY2` | `VARCHAR2(128)` |  | Key2 associated with the captured report |
| `KEY3` | `VARCHAR2(128)` |  | Key3 associated with the captured report |
| `KEY4` | `VARCHAR2(256)` |  | Key4 associated with the captured report |
| `GENERATION_COST_SECONDS` | `NUMBER` |  | Time taken to generate this report (in seconds) |
| `REPORT_SUMMARY` | `VARCHAR2(4000)` |  | Summary of this report |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [DBA\_HIST\_REPORTS\_DETAILS](DBA_HIST_REPORTS_DETAILS.md) "