---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-LOGSTDBY.html
tags:
  - oracle
  - 12c
  - reference
---

| Column | Datatype | Description |
| --- | --- | --- |
| `SERIAL#` | `NUMBER` | SQL Session serial number. This data is used when joining this view with the `V$SESSION` and `V$PX_SESSION` views. |
| `LOGSTDBY_ID` | `NUMBER` | Parallel query slave ID |
| `PID` | `VARCHAR2(24)` | Process ID of the SQL apply process |
| `TYPE` | `VARCHAR2(128)` | Indicates the task being performed by the process (`COORDINATOR`, `APPLIER`, `ANALYZER`, `READER`, `PREPARER`, or `BUILDER`) |
| `STATUS_CODE` | `NUMBER` | Status number (or Oracle error code) belonging to the STATUS message |
| `STATUS` | `VARCHAR2(256)` | Description of the current activity of the process |
| `HIGH_SCN` | `NUMBER` | Highest system change number (SCN) seen by the process. This column is used to confirm the progress of the individual process. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |