---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-XSTREAM_TRANSACTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.145 V$XSTREAM\_TRANSACTION

`V$XSTREAM_TRANSACTION` displays information about transactions that are being processed by capture processes, outbound servers, and inbound servers. This view can identify long running transactions and to display how many LCRs are being processed in each transaction. This view only contains information about captured LCRs. It does not contain information about user-enqueued LCRs or user messages.

This view only shows information about LCRs that are being processed because they satisfied the rule sets for the component at the time of the query. For capture processes, this view only shows information about changes in transactions that the capture process has converted into LCRs. It does not show information about all the active transactions present in the redo log.

For outbound servers, this view only shows information about LCRs that the outbound server has dequeued. It does not show information about LCRs in the outbound server's queue. For outbound servers, information about a transaction remains in the view until the transaction is sent to the XStream client application.

For inbound servers, information about a transaction remains in the view until the transaction commits or until the entire transaction is rolled back.

| Column | Datatype | Description |
| --- | --- | --- |
| `COMPONENT_NAME` | `VARCHAR2(128)` | Name of the component |
| `COMPONENT_TYPE` | `VARCHAR2(20)` | Type of component  - `CAPTURE` - Capture process - `APPLY` - Apply reader subcomponent in an outbound server or inbound server - `PROPAGATION_SENDER` - Propagation sender that sends LCRs from a capture process to an outbound server |
| `XIDUSN` | `NUMBER` | Transaction ID undo segment number of the transaction |
| `XIDSLT` | `NUMBER` | Transaction ID slot number of the transaction |
| `XIDSQN` | `NUMBER` | Transaction ID sequence number of the transaction |
| `CUMULATIVE_MESSAGE_COUNT` | `NUMBER` | Number of LCRs processed in the transaction. If a component is restarted while the transaction is being processed, then this column shows the number of LCRs processed in the transaction since the component was started. |
| `TOTAL_MESSAGE_COUNT` | `NUMBER` | Total number of LCRs processed in the transaction by an outbound server or inbound server. This column does not pertain to capture processes. |
| `FIRST_MESSAGE_TIME` | `DATE` | Time stamp of the first LCR processed in the transaction. If a capture process is restarted while the transaction is being processed, then this column shows the time stamp of the first LCR processed after the capture process was started. |
| `FIRST_MESSAGE_NUMBER` | `NUMBER` | SCN of the first message in the transaction. If a capture process is restarted while the transaction is being processed, then this column shows the SCN of the first message processed after the capture process was started. |
| `LAST_MESSAGE_TIME` | `DATE` | Time stamp of the last LCR processed in the transaction |
| `LAST_MESSAGE_NUMBER` | `NUMBER` | SCN of the most recent message encountered for the transaction |
| `FIRST_MESSAGE_POSITION` | `RAW(64)` | Position of the first message seen by an XStream inbound server  This column is populated only for an apply process that is functioning as an XStream inbound server. |
| `LAST_MESSAGE_POSITION` | `RAW(64)` | Position of the last message seen by an XStream inbound server. This column is populated only for an apply process that is functioning as an XStream inbound server. |
| `TRANSACTION_ID` | `VARCHAR2(128)` | Transaction ID for an XStream inbound server. This column is populated only for an apply process that is functioning as an XStream inbound server. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |