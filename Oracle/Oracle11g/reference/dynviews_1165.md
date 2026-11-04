---
title: "V$GG_APPLY_RECEIVER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1165.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$GG_APPLY_RECEIVER` displays information about the message receiver of the Replicat process. The values are reset to zero when the database (or instance in an Oracle Real Application Clusters (Oracle RAC) environment) restarts and when the Replicat process is stopped..

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID of the apply receiver |
| `SERIAL#` | `NUMBER` | Serial number of the apply receiver |
| `APPLY_NAME` | `VARCHAR2(30)` | Name of the apply process |
| `STARTUP_TIME` | `DATE` | Startup time of the apply process |
| `SOURCE_DATABASE_NAME` | `VARCHAR2(128)` | Name of the source database |
| `ACKNOWLEDGEMENT` | `NUMBER` | acknowledgment of the messages received by the receiver |
| `LAST_RECEIVED_MSG` | `NUMBER` | Last received message |
| `TOTAL_MESSAGES_RECEIVED` | `NUMBER` | Total number of messages received |
| `TOTAL_AVAILABLE_MESSAGES` | `NUMBER` | Number of available messages |
| `STATE` | `VARCHAR2(46)` | State of the apply receiver: - Initializing - Sending unapplied txns - Waiting for message from client - Receiving LCRs - Evaluating rules - Enqueueing LCRS - Waiting for memory - Waiting for apply to read - Waiting for message from Replicat - Waiting for Replicat flush request to complete - Waiting for Replicat commit to complete |
| `LAST_RECEIVED_MSG_POSITION` | `VARCHAR2(64)` | Last received message position |
| `ACKNOWLEDGEMENT_POSITION` | `VARCHAR2(64)` | acknowledgment position of the messages received by the receiver. Corresponds to `ACKNOWLEDGEMENT`, except the value is in position rather than SCN. |

Note:

This view is available starting with Oracle Database 11g Release 2 (11.2.0.4).