---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DIAG_APP_TRACE_FILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.175 V$DIAG\_APP\_TRACE\_FILE

`V$DIAG_APP_TRACE_FILE` contains information about all trace files present in the Automatic Diagnostic Repository (ADR) for the current container (PDB) which contain application trace data (SQL\_TRACE or OPTIMIZER\_TRACE event data). This view also supports GV$ global views.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADR_HOME` | `VARCHAR2(444)` | Path to the current ADR home |
| `TRACE_FILENAME` | `VARCHAR2(68)` | Displays the name of the process trace file |
| `CHANGE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Displays the change time timestamp of the process trace fiile |
| `MODIFY_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Displays the last modification timestamp of the process trace file |
| `SQL_TRACE` | `VARCHAR2(1)` | Identifies if the process trace file contains SQL\_TRACE data. Possible values include:  - `Y`: This value is used when the process trace file contains SQL\_TRACE event data - `N`: This value indicates that the process trace does not contain SQL\_TRACE data |
| `OPTIMIZER_TRACE` | `VARCHAR2(1)` | Identifies if the process trace file contains OPTIMIZER\_TRACE data. Possible values include:  - `Y`: This value is used when the process trace file contains OPTIMIZER\_TRACE event data - `N`: This value indicates that the process trace does not contain OPTIMIZER\_TRACE data |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |