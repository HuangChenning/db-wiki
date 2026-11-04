---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_APPLY_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.373 DBA\_HIST\_APPLY\_SUMMARY

`DBA_HIST_APPLY_SUMMARY` displays historical statistics information about each apply process for Oracle GoldenGate, and Oracle XStream. This view is intended for use with Automatic Workload Repository (AWR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `APPLY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the apply process |
| `STARTUP_TIME` | `DATE` | `NOT NULL` | The time that the apply process was last started |
| `READER_TOTAL_MESSAGES_DEQUEUED` | `NUMBER` |  | Total number of messages dequeued since the apply process was last started |
| `READER_LAG` | `NUMBER` |  | For captured messages, the delay (in seconds) between the creation of the last message and it being received by the apply process. For user enqueued messages, the delay between the message being enqueued in the local database and being received by the apply process. |
| `COORD_TOTAL_RECEIVED` | `NUMBER` |  | Total number of transactions received by the coordinator process since the apply process was last started |
| `COORD_TOTAL_APPLIED` | `NUMBER` |  | Total number of transactions applied by the apply process since the apply process was last started |
| `COORD_TOTAL_ROLLBACKS` | `NUMBER` |  | Number of transactions which were rolled back due to unexpected contention |
| `COORD_TOTAL_WAIT_DEPS` | `NUMBER` |  | Number of times since the apply process was last started that an apply server waited to apply a logical change record (LCR) in a transaction until another apply server applied a transaction because of a dependency between the transactions |
| `COORD_TOTAL_WAIT_CMTS` | `NUMBER` |  | Number of times since the apply process was last started that an apply server waited to commit a transaction until another apply server committed a transaction to serialize commits |
| `COORD_LWM_LAG` | `NUMBER` |  | For captured messages, the delay (in seconds) between the creation of the message corresponding to the low watermark and it being applied by the apply process. For user enqueued messages, the delay between the message being enqueued in the local database and being applied by the apply process. |
| `SERVER_TOTAL_MESSAGES_APPLIED` | `NUMBER` |  | Total number of messages applied by all the apply servers since the apply process was last started |
| `SERVER_ELAPSED_DEQUEUE_TIME` | `NUMBER` |  | Time elapsed (in hundredths of a second) dequeuing messages by all the apply servers since the apply process was last started |
| `SERVER_ELAPSED_APPLY_TIME` | `NUMBER` |  | Time elapsed (in hundredths of a second) applying messages by all the apply servers since the apply process was last started |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB |
| `REPLICAT_NAME` | `VARCHAR2(128)` |  | The name of the replicat group created from GGSCI using GoldenGate |
| `UNASSIGNED_COMPLETE_TXN` | `NUMBER` |  | Total number of complete transactions that the coordinator has not assigned to any apply servers |
| `TOTAL_LCRS_RETRIED` | `NUMBER` |  | Total number of LCRs retried by this server |
| `TOTAL_TRANSACTIONS_RETRIED` | `NUMBER` |  | Total transactions retried by this server |
| `TOTAL_ERRORS` | `NUMBER` |  | Number of transactions applied by the apply process that resulted in an apply error since the apply process was last started |
| `SESSION_MODULE` | `VARCHAR2(64)` | `NOT NULL` | Session module. Valid values:  - XStream - GoldenGate |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |