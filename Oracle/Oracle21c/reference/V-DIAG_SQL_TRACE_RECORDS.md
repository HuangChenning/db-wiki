---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DIAG_SQL_TRACE_RECORDS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.182 V$DIAG\_SQL\_TRACE\_RECORDS

`V$DIAG_SQL_TRACE_RECORDS` contains all SQL\_TRACE data that is present in the trace files that are part of the current Automatic Diagnostic Repository (ADR). This view also supports GV$ global views.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADR_HOME` | `VARCHAR2(444)` | Path to current ADR home |
| `TRACE_FILENAME` | `VARCHAR2(68)` | Displays the name of the process trace file |
| `RECORD_LEVEL` | `NUMBER` | Displays the level of the trace record |
| `PARENT_LEVEL` | `NUMBER` | Displays the top parent level of the trace record |
| `RECORD_TYPE` | `NUMBER` | Displays the type of the trace record. Possible values include:  - `1`: Regular trace record - `2`: Freeform trace record - `3`: Begin Section trace record - `4`: Begin Dump trace record - `5`: Bucket Dump Begin trace record - `6`: Section End trace record - `7`: Dump End trace record - `8`: Bucket Dump End trace record |
| `TIMESTAMP` | `TIMESTAMP(3) WITH TIME ZONE` | Displays the timestamp when the trace record was produced |
| `PAYLOAD` | `VARCHAR2(4000)` | Displays the trace record payload (contents) |
| `SECTION_ID` | `NUMBER` | Displays the section ID / dump ID of the trace record |
| `SECTION_NAME` | `VARCHAR2(64)` | Displays the section name / dump name of the trace record |
| `COMPONENT_NAME` | `VARCHAR2(64)` | Displays the component name which produced the trace record |
| `OPERATION_NAME` | `VARCHAR2(64)` | Displays the operation name which produced the trace record |
| `FILE_NAME` | `VARCHAR2(64)` | Displays the name of the code file where this trace record is produced |
| `FUNCTION_NAME` | `VARCHAR2(64)` | Displays the function which produced this trace record |
| `LINE_NUMBER` | `NUMBER` | Displays the line number in the code file which produced this trace record |
| `THREAD_ID` | `VARCHAR2(64)` | Displays the operating system thread ID of the process which produced the trace record |
| `SESSION_ID` | `NUMBER` | Displays the user session ID which generated the trace record |
| `SERIAL#` | `NUMBER` | Displays the user session serial number which produced the trace record |
| `SECURITY_LABEL` | `VARCHAR2(16)` | Displays the trace record security label classification. Possible values:  - `ALGORITHM` - `CONFIG` - `DATA` - `INTERNAL` - `KEYS` - `METADATA` - `NONE` - `PROGRAM` - `STATIC` - `UNKNOWN` |
| `CON_UID` | `NUMBER` | Displays the container unique ID where the trace record was produced |
| `CONTAINER_NAME` | `VARCHAR2(64)` | Displays the container name where the trace record was produced |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |