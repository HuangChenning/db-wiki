---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ACCHK_EVENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.3 DBA\_ACCHK\_EVENTS

`DBA_ACCHK_EVENTS` displays information about events that occurred during an Application Continuity Protection Check (ACCHK) workload run.

Each row in this view represents one trace record for an event. You can use this view in conjunction with the `DBA_ACCHK_STATISTICS` view. Join the `SESSION_ID` and `SERIAL#` columns in this view with the `SESSION_ID` and `SERIAL#` columns in `DBA_ACCHK_STATISTICS` to view Application Continuity protection statistics for a particular session.

The `ACCHK_READ` role allows users with no administrative privileges to query this view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INST_ID` | `NUMBER` |  | Identifier for the instance in which the trace record was generated |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `TIMESTAMP` | `TIMESTAMP(3) WITH TIME ZONE` |  | Time at which the event occurred |
| `SESSION_ID` | `NUMBER` |  | ID of the session that generated the trace record |
| `SERIAL#` | `NUMBER` |  | Serial number of the session that generated the trace record |
| `SERVICE_NAME` | `VARCHAR2(64)` |  | Service name of the session that generated the trace record |
| `PROGRAM` | `VARCHAR2(84)` |  | Name of the operating system program that generated the trace record |
| `MODULE` | `VARCHAR2(64)` |  | Name of the module that generated the trace record |
| `ACTION` | `VARCHAR2(64)` |  | Name of the action that generated the trace record |
| `SQL_ID` | `VARCHAR2(13)` |  | SQL identifier of the SQL statement that generated the trace record |
| `CALL_NAME` | `VARCHAR2(20)` |  | Name of the user call that generated the trace record |
| `EVENT_TYPE` | `VARCHAR2(16)` |  | Event type. Possible values:  - `DISABLED` - The event caused capture or replay to be disabled. Refer to the `ERROR_CODE` column for more information. - `NEVER` `ENABLED` - Neither Application Continuity nor Transparent Application Continuity was enabled for the session when the event occurred. - `NOT` `ENABLING` - The event describes why the database could not reenable protection after protection was disabled. Refer to the `ERROR_CODE` column for more information. - `REPLAY` `FAILED` - The event describes why the session did not fail over. This event only occurs if Application Continuity could not fail over. Refer to the `ERROR_CODE` column for more information. |
| `ERROR_CODE` | `NUMBER` |  | If an error occurred, this column displays the error code: `ORA-` `number`. Otherwise, the value of this column is `0`. |

Note:

This view is available starting with Oracle Database 21c.

See Also:

" [DBA\_ACCHK\_STATISTICS](DBA_ACCHK_STATISTICS.md) "