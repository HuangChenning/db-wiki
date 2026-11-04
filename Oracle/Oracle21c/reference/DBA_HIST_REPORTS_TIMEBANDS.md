---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_REPORTS_TIMEBANDS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.36 DBA\_HIST\_REPORTS\_TIMEBANDS

`DBA_HIST_REPORTS_TIMEBANDS` contains bands of time with a new row created every day corresponding to a band of time.

Each band of time represents a period of time, and has a row for every report captured automatically into Automatic Workload Repository (AWR) during that time. If the activity period of a report spans across two bands of time (for example. the activity started before midnight and ended after midnight), then the view contains two rows for that report, with one row for each band of time. The view is partitioned to provide fast access to all reports captured in a given time frame.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | The AWR snapshot id corresponding to the report |
| `DBID` | `NUMBER` |  | Database ID of the current database for the report |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number (for an Oracle RAC system) |
| `CON_DBID` | `NUMBER` |  | CDB ID of the captured report |
| `COMPONENT_ID` | `NUMBER` |  | ID of the component (for example, SQL Monitor) whose report is captured |
| `COMPONENT_NAME` | `VARCHAR2(128)` |  | Name of the component whose report is captured |
| `BAND_START_TIME` | `DATE` |  | Starting time of the time band |
| `BAND_LENGTH` | `NUMBER` |  | Length of time band in days (currently unused) |
| `REPORT_ID` | `NUMBER` |  | ID of the captured report |
| `REPORT_GENERATION_TIME` | `DATE` |  | Time when the report was generated |
| `PERIOD_START_TIME` | `DATE` |  | Time when the activity period started |
| `PERIOD_END_TIME` | `DATE` |  | Time when the activity period ended |
| `KEY1` | `VARCHAR2(128)` |  | Key1 associated with the captured report |
| `KEY2` | `VARCHAR2(128)` |  | Key2 associated with the captured report |
| `KEY3` | `VARCHAR2(128)` |  | Key3 associated with the captured report |
| `KEY4` | `VARCHAR2(256)` |  | Key4 associated with the captured report |
| `SESSION_ID` | `NUMBER` |  | ID of the session corresponding to the captured report (currently used only for SQL Monitor reports) |
| `SESSION_SERIAL#` | `NUMBER` |  | Session serial number corresponding to the captured report (currently used only for SQL Monitor reports) |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |