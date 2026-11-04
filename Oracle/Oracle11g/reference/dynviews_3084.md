---
title: "V$STREAMS_TRANSACTION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3084.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$STREAMS_TRANSACTION` displays information about transactions that are being processed by capture processes or apply processes. This view can be used to identify long running transactions and to determine how many logical change records (LCRs) are being processed in each transaction. This view only contains information about captured LCRs. It does not contain information about user-enqueued LCRs or user messages.

This view only shows information about LCRs that are being processed because they satisfied the rule sets for the Streams process at the time of the query. For capture processes, this view only shows information about changes in transactions that the capture process has converted to LCRs. It does not show information about all the active transactions present in the redo log. For apply processes, this view only shows information about LCRs that the apply process has dequeued. It does not show information about LCRs in the apply process's queue.

Information about a transaction remains in the view until the transaction commits or until the entire transaction is rolled back.

| Column | Datatype | Description |
| --- | --- | --- |
| `STREAMS_NAME` | `VARCHAR2(30)` | Name of the Streams process |
| `STREAMS_TYPE` | `VARCHAR2(10)` | Type of the Streams process: - `CAPTURE` - `APPLY` - `PROPAGATION_SENDER` |
| `XIDUSN` | `NUMBER` | Transaction ID undo segment number of the transaction |
| `XIDSLT` | `NUMBER` | Transaction ID slot number of the transaction |
| `XIDSQN` | `NUMBER` | Transaction ID sequence number of the transaction |
| `CUMULATIVE_MESSAGE_COUNT` | `NUMBER` | Number of LCRs processed in the transaction. If the Streams process is restarted while the transaction is being processed, then this column shows the number of LCRs processed in the transaction since the Streams process was started. |
| `TOTAL_MESSAGE_COUNT` | `NUMBER` | Total Number of LCRs processed in the transaction by an apply process. This column does not pertain to capture processes. |
| `FIRST_MESSAGE_TIME` | `DATE` | Timestamp of the first LCR processed in the transaction. If a capture process is restarted while the transaction is being processed, then this column shows the timestamp of the first LCR processed after the capture process was started. |
| `FIRST_MESSAGE_NUMBER` | `NUMBER` | System change number (SCN) of the first message in the transaction. If a capture process is restarted while the transaction is being processed, then this column shows the SCN of the first message processed after the capture process was started. |
| `LAST_MESSAGE_TIME` | `DATE` | Timestamp of the last LCR processed in the transaction |
| `LAST_MESSAGE_NUMBER` | `NUMBER` | SCN of the most recent message encountered for the transaction |
| `FIRST_MESSAGE_POSITION` | `RAW(64)` | Reserved for internal use |
| `LAST_MESSAGE_POSITION` | `RAW(64)` | Reserved for internal use |
| `TRANSACTION_ID` | `VARCHAR2(128)` | Transaction ID |
| `PURPOSE` <sup>Foot 1</sup> | `VARCHAR2(10)` | Purpose of the components that are processing the transaction: - `Streams` - The transaction is being processed in an Oracle Streams configuration - `XStream` - The transaction is being processed in an XStream configuration |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).