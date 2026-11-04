---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EMON.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.194 V$EMON

`V$EMON` displays performance statistics per event monitor (EMON) worker for diagnosability of notifications. All processing time and latency is in seconds.

| Column | Datatype | Description |
| --- | --- | --- |
| `EMON#` | `NUMBER` | EMON identifier (0 - 9) |
| `SID` | `NUMBER` | Session identifier |
| `STARTUP_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when this EMON worker was started |
| `SERVER_TYPE` | `VARCHAR2(8)` | Notification quality of the service provided by EMON:  - `REGULAR` - `RELIABLE` |
| `STATUS` | `VARCHAR2(6)` | EMON status:  - `IDLE` - `ACTIVE` |
| `STATUS_CHANGE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time at which EMON switched to the current STATUS |
| `NUM_NTFNS` | `NUMBER` | Total number of notifications (including grouping notifications) |
| `NUM_GROUPING_NTFNS` | `NUMBER` | Number of grouping notifications |
| `NUM_NTFNS_ALL_GROUPS` | `NUMBER` | Total number of events in all notification groups |
| `NUM_OCI_NTFNS` | `NUMBER` | Number of OCI notifications |
| `NUM_PLSQL_NTFNS` | `NUMBER` | Number of PL/SQL notifications |
| `NUM_EMAIL_NTFNS` | `NUMBER` | Number of E-mail notifications |
| `NUM_HTTP_NTFNS` | `NUMBER` | Number of HTTP notifications |
| `NUM_EVENTS_PROCESSED` | `NUMBER` | Number of events posted by a publisher for which notifications have been delivered |
| `NUM_EVENTS_PENDING` | `NUMBER` | Number of events posted by a publisher for which notifications are not yet delivered |
| `NUM_ANONYMOUS_NTFNS` | `NUMBER` | Number of anonymous notifications |
| `NUM_AQ_NTFNS` | `NUMBER` | Number of AQ notifications |
| `NUM_DBCHANGE_NTFNS` | `NUMBER` | Number of DBChange notifications |
| `TOTAL_ANONYMOUS_NTFN_TIME` | `NUMBER` | Total time to process Anonymous notifications |
| `TOTAL_AQ_NTFN_TIME` | `NUMBER` | Total time to process AQ notifications |
| `TOTAL_DBCHANGE_NTFN_TIME` | `NUMBER` | Total time to process dbchange notifications |
| `TOTAL_PLSQL_NTFN_TIME` | `NUMBER` | Total time to process PL/SQL notifications |
| `TOTAL_OCI_NTFN_TIME` | `NUMBER` | Total time to process OCI notifications |
| `TOTAL_EMAIL_NTFN_TIME` | `NUMBER` | Total time to process E-mail notifications |
| `TOTAL_HTTP_NTFN_TIME` | `NUMBER` | Total time to process HTTP notifications |
| `TOTAL_EMON_LATENCY` | `NUMBER` | Total latency in processing events |
| `REGISTRATIONS_EXPIRED` | `NUMBER` | Number of expired registrations |
| `REGISTRATIONS_PURGED` | `NUMBER` | Number of purged registrations |
| `REGISTRATIONS_INVALID` | `NUMBER` | Number of registrations invalidated due to notification delivery failure |
| `LAST_UPDATE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when statistics were last updated |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. The `CON_ID` value in this view is always 0. The rows pertain to the entire CDB or to the non-CDB. |