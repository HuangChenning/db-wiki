---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_REPLICATION_PROCESS_EVENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.31 ALL\_REPLICATION\_PROCESS\_EVENTS

`ALL_REPLICATION_PROCESS_EVENTS` provides information about the replication processes events accessible to the current user.

Related View

`DBA_REPLICATION_PROCESS_EVENTS` provides information about the replication processes events in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAMS_TYPE` | `VARCHAR2(10)` |  | Streams type:  - `XStream` - `GoldenGate` |
| `PROCESS_TYPE` | `VARCHAR2(27)` |  | Process type:  - `Capture` - `Capture server` - `Apply Coordinator` - `Apply Server` - `Apply Network Receiver` - `Apply Reader` - `Apply Hash server` |
| `STREAMS_NAME` | `VARCHAR2(128)` | `NOT NULL` | Streams name |
| `EVENT_NAME` | `VARCHAR2(128)` |  | Event name:  - `START` - `STOP` - `ABORT` - `CREATE` - `DROP` - `PARAMETER CHANGE` - `HANDLER CREATE` - `HANDLER REMOVE` - `ALTER` |
| `DESCRIPTION` | `VARCHAR2(2000)` |  | Event description |
| `EVENT_TIME` | `TIMESTAMP(6)` |  | Time when the event occurred |
| `ERROR_NUMBER` | `NUMBER` |  | Error number (valid when event is Error) |
| `ERROR_MESSAGE` | `VARCHAR2(2000)` |  | Error Message (valid when event is an error) |

See Also:

" [DBA\_REPLICATION\_PROCESS\_EVENTS](DBA_REPLICATION_PROCESS_EVENTS.md) "