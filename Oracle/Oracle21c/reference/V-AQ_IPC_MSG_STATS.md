---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_IPC_MSG_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.21 V$AQ\_IPC\_MSG\_STATS

`V$AQ_IPC_MSG_STATS` displays the statistics of each IPC message class, such as the total number of invocations of a message class, total pending message/processed message count, and last failure related data. Information like total processed message count, average pending time/average processing time gives a real-time outline of AQ IPC background state.

| Column | Datatype | Description |
| --- | --- | --- |
| `MSG_CLASS_NAME` | `VARCHAR2(30)` | Message class name |
| `TOTAL_MSG_CALLS` | `NUMBER` | Total number of calls for this message class |
| `TOTAL_ACTIVE_MSGS` | `NUMBER` | Total number of active messages presently processed by workers and primary |
| `TOTAL_PENDING_MSGS` | `NUMBER` | Total number of pending messages in the primary's local context |
| `TOTAL_PROCESSED_MSGS` | `NUMBER` | Total number of processed messages |
| `LAST_RECEIVED_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the last message of this type was received in the primary's context list |
| `LAST_PROCESS_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the last message was picked for processing |
| `LAST_DONE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the last message was done processing |
| `AVERAGE_PENDING_TIME` | `NUMBER` | Average pending time for this message class (in seconds) |
| `AVERAGE_PROCESSING_TIME` | `NUMBER` | Average processing time for this message class (in seconds) |
| `LAST_FAILURE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time of the last failure for this message class |
| `LAST_ERROR_MSG` | `VARCHAR2(512)` | Last error message for this message class |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |