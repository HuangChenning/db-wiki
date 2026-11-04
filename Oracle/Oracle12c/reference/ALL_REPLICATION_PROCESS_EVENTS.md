---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_REPLICATION_PROCESS_EVENTS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_REPLICATION_PROCESS_EVENTS` provides information about the replication processes events accessible to the current user.

Related View

`DBA_REPLICATION_PROCESS_EVENTS` provides information about the replication processes events in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAMS_TYPE` | `VARCHAR2(10)` |  | Streams type:  - `Streams` - `XStream` - `GoldenGate` |
| `PROCESS_TYPE` | `VARCHAR2(27)` |  | Process type:  - `Capture` - `Capture server` - `Apply Coordinator` - `Apply Server` - `Apply Network Receiver` - `Apply Reader` - `Apply Hash server` |
| `STREAMS_NAME` | `VARCHAR2(128)` | `NOT NULL` | Streams name |
| `EVENT_NAME` | `VARCHAR2(128)` |  | Event name:  - `START` - `STOP` - `ABORT` - `CREATE` - `DROP` - `PARAMETER CHANGE` - `HANDLER CREATE` - `HANDLER REMOVE` - `ALTER` |
| `DESCRIPTION` | `VARCHAR2(2000)` |  | Event description |
| `EVENT_TIME` | `TIMESTAMP(6)` |  | Time when the event occurred |
| `ERROR_NUMBER` | `NUMBER` |  | Error number (valid when event is Error) |
| `ERROR_MESSAGE` | `VARCHAR2(2000)` |  | Error Message (valid when event is an error) |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1)

See Also:

" [DBA\_REPLICATION\_PROCESS\_EVENTS](DBA_REPLICATION_PROCESS_EVENTS.md) "