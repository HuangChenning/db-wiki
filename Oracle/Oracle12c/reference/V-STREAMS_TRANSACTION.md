---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-STREAMS_TRANSACTION.html
tags:
  - oracle
  - 12c
  - reference
---

`V$STREAMS_TRANSACTION` displays information about transactions that are being processed by capture processes or apply processes. This view can be used to identify long running transactions and to determine how many logical change records (LCRs) are being processed in each transaction. This view only contains information about captured LCRs. It does not contain information about user-enqueued LCRs or user messages.

This view only shows information about LCRs that are being processed because they satisfied the rule sets for the Streams process at the time of the query. For capture processes, this view only shows information about changes in transactions that the capture process has converted to LCRs. It does not show information about all the active transactions present in the redo log. For apply processes, this view only shows information about LCRs that the apply process has dequeued. It does not show information about LCRs in the apply process's queue.

Information about a transaction remains in the view until the transaction commits or until the entire transaction is rolled back.

| Column | Datatype | Description |
| --- | --- | --- |
| `STREAMS_NAME` | `VARCHAR2(128)` | Name of the Streams process |
| `STREAMS_TYPE` | `VARCHAR2(20)` | Type of the Streams process:  - `CAPTURE` - `APPLY` - `PROPAGATION_SENDER` |
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
| `PURPOSE` | `CHAR(7)` | Purpose of the components that are processing the transaction:  - `Streams` - The transaction is being processed in an Oracle Streams configuration |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |