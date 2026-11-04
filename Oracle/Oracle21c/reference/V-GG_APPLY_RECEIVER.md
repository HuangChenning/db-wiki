---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-GG_APPLY_RECEIVER.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.263 V$GG\_APPLY\_RECEIVER

`V$GG_APPLY_RECEIVER` displays information about the message receiver of the Replicat process.

The values are reset to zero when the database (or instance in an Oracle Real Application Clusters (Oracle RAC) environment) restarts and when the Replicat process is stopped.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID of the apply receiver |
| `SERIAL#` | `NUMBER` | Serial number of the apply receiver |
| `APPLY_NAME` | `VARCHAR2(128)` | Name of the apply process |
| `STARTUP_TIME` | `DATE` | Startup time of the apply process |
| `SOURCE_DATABASE_NAME` | `VARCHAR2(128)` | Name of the source database |
| `ACKNOWLEDGEMENT` | `NUMBER` | acknowledgment of the messages received by the receiver |
| `LAST_RECEIVED_MSG` | `NUMBER` | Last received message |
| `TOTAL_MESSAGES_RECEIVED` | `NUMBER` | Total number of messages received |
| `TOTAL_AVAILABLE_MESSAGES` | `NUMBER` | Number of available messages |
| `STATE` | `VARCHAR2(46)` | State of the apply receiver:  - Initializing - Sending unapplied txns - Waiting for message from client - Receiving LCRs - Evaluating rules - Enqueueing LCRS - Waiting for memory - Waiting for apply to read - Waiting for message from Replicat - Waiting for Replicat flush request to complete - Waiting for Replicat commit to complete |
| `LAST_RECEIVED_MSG_POSITION` | `VARCHAR2(64)` | Last received message position |
| `ACKNOWLEDGEMENT_POSITION` | `VARCHAR2(64)` | acknowledgment position of the messages received by the receiver. Corresponds to `ACKNOWLEDGEMENT`, except the value is in position rather than SCN. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `OS_PROCESS_ID` | `VARCHAR2(12)` | The OS process ID of the apply receiver process |
| `CURRENT_POSITION` | `VARCHAR2(81)` | The trail position of the current record processed by the apply receiver |
| `TOTAL_TRANSACTIONS` | `NUMBER` | The total number of transactions processed by the apply receiver |
| `TOTAL_COMMITS` | `NUMBER` | The total number of commits executed by the apply receiver |
| `TOTAL_ERRORS` | `NUMBER` | The total number of errors encountered by the apply receiver |