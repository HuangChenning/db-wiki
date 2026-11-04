---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_REPORTS_DETAILS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.35 DBA\_HIST\_REPORTS\_DETAILS

`DBA_HIST_REPORTS_DETAILS` displays details about each report captured in Automatic Workload Repository (AWR).

Metadata for each report appears in the `DBA_HIST_REPORTS` view while the actual report is available in the `DBA_HIST_REPORTS_DETAILS` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | ID of the first AWR snapshot that will be taken after this report is generated |
| `DBID` | `NUMBER` |  | Database ID of the current database for the report |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number (for an Oracle RAC system) |
| `REPORT_ID` | `NUMBER` |  | ID of the captured report |
| `SESSION_ID` | `NUMBER` |  | ID of the session corresponding to the captured report (currently used only for SQL Monitor reports) |
| `SESSION_SERIAL#` | `NUMBER` |  | Session serial number relevant to this report (currently used only for SQL Monitor reports) |
| `GENERATION_TIME` | `DATE` |  | Time when this report was generated |
| `REPORT_COMPRESSED` | `BLOB` |  | Actual XML report in compressed form |
| `REPORT` | `CLOB` |  | Full uncompressed report |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [DBA\_HIST\_REPORTS](DBA_HIST_REPORTS.md) "