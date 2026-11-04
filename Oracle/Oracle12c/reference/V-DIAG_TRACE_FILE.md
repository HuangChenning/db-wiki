---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-DIAG_TRACE_FILE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$DIAG_TRACE_FILE` contains information about all trace files present in the Automatic Diagnostic Repository (ADR) for the current container (PDB). This view also supports GV$ global views.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADR_HOME` | `VARCHAR2(444)` | Path to the current ADR home |
| `TRACE_FILENAME` | `VARCHAR2(68)` | Displays the name of the process trace file |
| `CHANGE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Displays the change time timestamp of the process trace file |
| `MODIFY_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Displays the last modification timestamp of the process trace file |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).