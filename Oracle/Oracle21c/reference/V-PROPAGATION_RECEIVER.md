---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PROPAGATION_RECEIVER.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.133 V$PROPAGATION\_RECEIVER

The values are reset to zero when the database (or instance in an Oracle Real Application Clusters (Oracle RAC) environment) restarts, when propagation migrates to another instance, or when an unscheduled propagation is attempted.

| Column | Datatype | Description |
| --- | --- | --- |
| `SRC_QUEUE_SCHEMA` | `VARCHAR2(128)` | Name of the source schema |
| `SRC_QUEUE_NAME` | `VARCHAR2(128)` | Name of the source queue |
| `SRC_DBNAME` | `VARCHAR2(395)` | Name of the source database |
| `DST_QUEUE_SCHEMA` | `VARCHAR2(128)` | Name of the destination schema |
| `DST_QUEUE_NAME` | `VARCHAR2(128)` | Name of the destination queue |
| `STARTUP_TIME` | `DATE` | Startup time of this schedule. This time changes when the source/destination database gets restarted. |
| `HIGH_WATER_MARK` | `NUMBER` | High watermark of the messages received |
| `ACKNOWLEDGEMENT` | `NUMBER` | Acknowledgement of the messages received by the receiver |
| `LAST_RECEIVED_MSG` | `NUMBER` | Last received message |
| `TOTAL_MSGS` | `NUMBER` | Total number of messages |
| `ELAPSED_UNPICKLE_TIME` | `NUMBER` | Elapsed unpickle time |
| `ELAPSED_RULE_TIME` | `NUMBER` | Elapsed rule time |
| `ELAPSED_ENQUEUE_TIME` | `NUMBER` | Elapsed enqueue time |
| `SESSION_ID` | `NUMBER` | Session ID of the propagation receiver |
| `SERIAL#` | `NUMBER` | Serial number of the propagation receiver |
| `SPID` | `VARCHAR2(24)` | Process identification number of the propagation receiver |
| `PROPAGATION_NAME` | `VARCHAR2(128)` | Name of the propagation on the source database |
| `STATE` | `VARCHAR2(43)` | State of the propagation receiver:  - `Initializing` - `Sending unapplied txns` - `Waiting for message from client` - `Receiving LCRs` - `Evaluating rules` - `Enqueueing LCRS` - `Waiting for memory` - `Waiting for apply to read` - `Waiting for message from propagation sender`  When the propagation schedule is not optimized, the state is `Normal`. |
| `LAST_RECEIVED_MSG_POSITION` | `RAW(64)` | Last received message position. Corresponds to `LAST_RECEIVED_MSG`, except the value is in position rather than SCN. Position is used by XStream to determine ordering. |
| `ACKNOWLEDGEMENT_POSITION` | `RAW(64)` | Acknowledgement position of the messages received by the receiver. Corresponds to `ACKNOWLEDGEMENT`, except the value is in position rather than SCN. Position is used by XStream to determine ordering. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |