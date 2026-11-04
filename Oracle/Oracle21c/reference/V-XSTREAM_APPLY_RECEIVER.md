---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-XSTREAM_APPLY_RECEIVER.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.139 V$XSTREAM\_APPLY\_RECEIVER

The values are reset to zero when the database (or instance in an Oracle Real Application Clusters (Oracle RAC) environment) restarts, when apply migrates to another instance, or when the XStream process is stopped.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID of the apply receiver |
| `SERIAL#` | `NUMBER` | Serial number of the apply receiver |
| `APPLY_NAME` | `VARCHAR2(128)` | Name of the apply process |
| `STARTUP_TIME` | `DATE` | Startup time of the apply process |
| `SOURCE_DATABASE_NAME` | `VARCHAR2(128)` | Name of the source database |
| `ACKNOWLEDGEMENT` | `NUMBER` | Acknowledgement SCN of the messages received by the receiver |
| `LAST_RECEIVED_MSG` | `NUMBER` | Last received message |
| `TOTAL_MESSAGES_RECEIVED` | `NUMBER` | Total number of messages received |
| `TOTAL_AVAILABLE_MESSAGES` | `NUMBER` | Number of available messages |
| `STATE` | `VARCHAR2(44)` | State of the apply receiver:  - Initializing - Sending unapplied txns - Waiting for message from client - Waiting for LCR from client - Receiving LCRs - Evaluating rules - Enqueueing LCRS - Waiting for memory - Waiting for apply to read - Waiting for client flush request to complete - Waiting for client commit to complete |
| `LAST_RECEIVED_MSG_POSITION` | `RAW(64)` | Last received message position |
| `ACKNOWLEDGEMENT_POSITION` | `RAW(64)` | Acknowledgement position of the messages received by the receiver. Corresponds to `ACKNOWLEDGEMENT`, except the value is in position rather than SCN. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |