---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PROPAGATION_SENDER.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.134 V$PROPAGATION\_SENDER

The values are reset to zero when the database (or instance in an Oracle Real Application Clusters (Oracle RAC) environment) restarts, when propagation migrates to another instance, or when an unscheduled propagation is attempted.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue identifier of the queue |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | Schema of the queue |
| `QUEUE_NAME` | `VARCHAR2(128)` | Name of the queue |
| `DST_QUEUE_SCHEMA` | `VARCHAR2(128)` | Destination schema of the queue |
| `DST_QUEUE_NAME` | `VARCHAR2(128)` | Name of the destination queue |
| `STARTUP_TIME` | `DATE` | Time at which the propagation started |
| `DBLINK` | `VARCHAR2(395)` | Name of the destination database link |
| `HIGH_WATER_MARK` | `NUMBER` | High watermark of the messages sent |
| `ACKNOWLEDGEMENT` | `NUMBER` | Acknowledgement of the messages received by the receiver |
| `SCHEDULE_STATUS` | `VARCHAR2(128)` | Status of the propagation schedule |
| `TOTAL_MSGS` | `NUMBER` | Total messages propagated |
| `TOTAL_BYTES` | `NUMBER` | Total bytes propagated |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` | Elapsed dequeue time (in hundredths of a second) |
| `ELAPSED_PICKLE_TIME` | `NUMBER` | Elapsed pickle time (time taken to linearize a logical change record (LCR) into a stream of bytes that can be sent over the network) (in hundredths of a second) |
| `ELAPSED_PROPAGATION_TIME` | `NUMBER` | Elapsed propagation time (in hundredths of a second) |
| `ELAPSED_RULE_TIME` | `NUMBER` | Elapsed rule time (in hundredths of a second) |
| `MAX_NUM_PER_WIN` | `NUMBER` | Maximum bytes per window |
| `MAX_SIZE` | `NUMBER` | Maximum bytes sent per window |
| `LAST_MSG_LATENCY` | `NUMBER` | Last propagated message latency |
| `LAST_MSG_ENQUEUE_TIME` | `TIMESTAMP(6)` | Last propagated message enqueue time |
| `LAST_MSG_PROPAGATION_TIME` | `TIMESTAMP(6)` | Last time when the message was propagated |
| `LAST_LCR_LATENCY` | `NUMBER` | Last propagated LCR latency |
| `LAST_LCR_CREATION_TIME` | `DATE` | Last propagated LCR timestamp |
| `LAST_LCR_PROPAGATION_TIME` | `DATE` | Last time when the LCR was propagated |
| `DST_DATABASE_NAME` | `VARCHAR2(395)` | Global name of the destination database |
| `SESSION_ID` | `NUMBER` | Session ID of the propagation sender process |
| `SERIAL#` | `NUMBER` | Serial number of the propagation sender process |
| `SPID` | `VARCHAR2(24)` | Process identification number of the propagation sender process |
| `PROPAGATION_NAME` | `VARCHAR2(128)` | Name of the propagation |
| `STATE` | `VARCHAR2(128)` | State of the propagation sender process:  - `Initializing` - `Initializing propagation receiver` - `Browsing LCRs` - `Evaluating rules` - `Dequeueing LCRs` - `Sending LCRs` - `Waiting for apply to be enabled` - `Waiting for apply database to start` - `Waiting for propagation to be enabled` - `Waiting for capture to terminate` - `Waiting for a subscriber to be added` - `Suspended due to a dropped subscriber` - `Suspended for auto split/merge` - `Waiting on empty queue`  When the `SCHEDULE_STATUS` column is not `SCHEDULE OPTIMIZED`, the state is the value of the `SCHEDULE_STATUS` column. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |