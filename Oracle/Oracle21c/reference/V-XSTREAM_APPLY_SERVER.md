---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-XSTREAM_APPLY_SERVER.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.140 V$XSTREAM\_APPLY\_SERVER

An apply server receives messages from the apply coordinator for an apply process. For each message received, an apply server either applies the message or sends the message to the appropriate apply handler. An apply server is a subcomponent of an apply process, outbound server, or inbound server.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID of the apply server's session |
| `SERIAL#` | `NUMBER` | Serial number of the apply server's session |
| `APPLY#` | `NUMBER` | Apply process number. An apply process is an Oracle background process, prefixed by `ap`. |
| `APPLY_NAME` | `VARCHAR2(128)` | Name of the apply process |
| `SERVER_ID` | `NUMBER` | Parallel execution server number of the apply server |
| `STATE` | `VARCHAR2(20)` | State of the apply server:  - `INITIALIZING` - Starting up - `IDLE` - Performing no work - `RECORD LOW-WATERMARK` - Performing an administrative job that maintains information about the apply progress, which is used in the `ALL_APPLY_PROGRESS` and `DBA_APPLY_PROGRESS` data dictionary views - `ADD PARTITION` - Performing an administrative job that adds a partition that is used for recording information about in-progress transactions - `DROP PARTITION` - Performing an administrative job that purges rows that were used to record information about in-progress transactions - `EXECUTE TRANSACTION` - Applying a transaction - `WAIT COMMIT` - Waiting to commit a transaction until all other transactions with a lower commit SCN are applied. This state is possible only if the `COMMIT_SERIALIZATION` apply process parameter is set to a value other than `DEPENDENT_TRANSACTIONS` and the `PARALLELISM` apply process parameter is set to a value greater than `1`. - `WAIT DEPENDENCY` - Waiting to apply a logical change record (LCR) in a transaction until another transaction, on which it has a dependency, is applied. This state is possible only if the `PARALLELISM` apply process parameter is set to a value greater than `1`. - `ROLLBACK TRANSACTION` - Rolling back a transaction - `TRANSACTION CLEANUP` - Cleaning up an applied transaction, which includes removing LCRs from the apply process's queue - `WAIT` `FOR` `CLIENT` - Waiting for an XStream client application to request more LCRs - `WAIT` `FOR` `NEXT` `CHUNK` - Waiting for the next set of LCRs for a large transaction |
| `XIDUSN` | `NUMBER` | Transaction ID undo segment number of the transaction currently being applied |
| `XIDSLT` | `NUMBER` | Transaction ID slot number of the transaction currently being applied |
| `XIDSQN` | `NUMBER` | Transaction ID sequence number of the transaction currently being applied |
| `COMMITSCN` | `NUMBER` | Commit system change number (SCN) of the transaction currently being applied |
| `DEP_XIDUSN` | `NUMBER` | Transaction ID undo segment number of a transaction on which the transaction being applied by this apply server depends |
| `DEP_XIDSLT` | `NUMBER` | Transaction ID slot number of a transaction on which the transaction being applied by this apply server depends |
| `DEP_XIDSQN` | `NUMBER` | Transaction ID sequence number of a transaction on which the transaction being applied by this apply server depends |
| `DEP_COMMITSCN` | `NUMBER` | Commit system change number (SCN) of the transaction on which this apply server depends |
| `MESSAGE_SEQUENCE` | `NUMBER` | Number of the current message being applied by the apply server. This value is reset to `1` at the beginning of each transaction. |
| `TOTAL_ASSIGNED` | `NUMBER` | Total number of transactions assigned to the apply server since the apply process was last started |
| `TOTAL_ADMIN` | `NUMBER` | Total number of administrative jobs done by the apply server since the apply process was last started. See the `STATE` information in this view for the types of administrative jobs. |
| `TOTAL_ROLLBACKS` | `NUMBER` | Number of transactions assigned to this server which were rolled back |
| `TOTAL_MESSAGES_APPLIED` | `NUMBER` | Total number of messages applied by this apply server since the apply process was last started |
| `APPLY_TIME` | `DATE` | Time the last message was applied |
| `APPLIED_MESSAGE_NUMBER` | `NUMBER` | Number of the last message applied |
| `APPLIED_MESSAGE_CREATE_TIME` | `DATE` | Creation time at the source database of the last captured message applied. No information about user-enqueued messages is recorded in this column. |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` | Time elapsed (in hundredths of a second) dequeuing messages since the apply process was last started |
| `ELAPSED_APPLY_TIME` | `NUMBER` | Time elapsed (in hundredths of a second) applying messages since the apply process was last started |
| `COMMIT_POSITION` | `RAW(64)` | Commit position of the transaction. This column is populated only for an apply process that is functioning as an XStream inbound server. |
| `DEP_COMMIT_POSITION` | `RAW(64)` | Commit position of the transaction the worker depends on. This column is populated only for an apply process that is functioning as an XStream inbound server. |
| `LAST_APPLY_POSITION` | `RAW(64)` | For inbound servers, the position of the last message applied; for outbound servers, the position of the last message sent to the XStream client application. This column is populated only for an apply process that is functioning as an XStream outbound server or inbound server. |
| `TRANSACTION_ID` | `VARCHAR2(128)` | Transaction ID that the worker is applying. This column is populated only for an apply process that is functioning as an XStream inbound server. |
| `DEP_TRANSACTION_ID` | `VARCHAR2(128)` | Transaction ID of the transaction the worker depends on. This column is populated only for an apply process that is functioning as an XStream inbound server. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `TOTAL_LCRS_RETRIED` | `NUMBER` | Total number of LCRs retried by this server |
| `LCR_RETRY_ITERATION` | `NUMBER` | Retry iteration for this transaction by this server |
| `TOTAL_TXNS_RETRIED` | `NUMBER` | Total transactions retried by this server |
| `TXN_RETRY_ITERATION` | `NUMBER` | Retry iteration for this transaction by this server |
| `TOTAL_TXNS_RECORDED` | `NUMBER` | Total transactions recorded in error queue by this server |

Note:

The `ELAPSED_SCHEDULE_TIME` column is only populated if the `TIMED_STATISTICS` initialization parameter is set to `true`, or if the `STATISTICS_LEVEL` initialization parameter is set to `TYPICAL` or `ALL`.

See Also:

- " [TIMED\_STATISTICS](TIMED_STATISTICS.md) "
- " [STATISTICS\_LEVEL](STATISTICS_LEVEL.md) "