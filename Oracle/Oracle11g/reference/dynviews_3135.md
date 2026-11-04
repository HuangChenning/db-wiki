---
title: "V$XSTREAM_OUTBOUND_SERVER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3135.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$XSTREAM_OUTBOUND_SERVER` displays statistics about an outbound server. An outbound server sends LCRs to the XStream client application.

Note:

When the `COMMITTED_DATA_ONLY` column is `YES` in the `V$XSTREAM_OUTBOUND_SERVER` view, the `V$STREAMS_APPLY_SERVER` view provides additional information about the outbound server process, and information about the apply server background processes used by the outbound server.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID of the outbound server's session |
| `SERIAL#` | `NUMBER` | Serial number of the outbound server's session |
| `SPID` | `VARCHAR2(12)` | Process identification number of the operating-system process that sends LCRs to the client application |
| `SERVER_NAME` | `VARCHAR2(30)` | Name of the outbound server |
| `STARTUP_TIME` | `DATE` | Time when the client application attached to the outbound server |
| `STATE` | `VARCHAR2(37)` | State of the outbound server  When the `COMMITTED_DATA_ONLY` column shows `YES`, the following states are possible:  - `INITIALIZING` - Starting up the outbound server. - `IDLE` - Performing no work because there are no LCRs to send to the XStream client application. - `GET` `TRANSACTIONS` - Receiving transactions from the outbound server's apply coordinator. - `SEND` `TRANSACTION` - Sending a transaction to an XStream client application. - `WAIT` `FOR` `NEXT` `CHUNK` - Waiting for the next set of LCRs for a large transaction. - `TRANSACTION` `CLEANUP` - Cleaning up an applied transaction, which includes removing LCRs from the outbound server's queue. - `WAIT` `FOR` `CLIENT` - Waiting for an XStream client application to request more LCRs.  When the `COMMITTED_DATA_ONLY` column shows `NO`, the following states are possible:  - `INITIALIZING` - Starting up the outbound server. - `INITIALIZING` `RULE` `EVALUATION` `CONTEXT` - Initializing the context to evaluate the outbound server's rules. - `IDLE` - Performing no work because there is no LCR to send to the XStream client application. - `BROWSING` `LCR` - Browsing the outbound server's queue for next LCR. - `EVALUATING` `RULES` - Evaluating an LCR against a rule set. - `DEQUEUING` `LCR` - Dequeuing an LCR from the outbound server's queue. - `SENDING` `LCR` - Sending an LCR to an XStream client application. - `WAITING` `FOR` `CAPTURE` `TO` `TERMINATE` - Waiting for the capture process to become disabled. - `SUSPENDED` `DUE` `TO` `A` `DROPPED` `SUBSCRIBER` - Suspended because a connected subscriber was dropped. For example, a subscriber can be dropped during a split or merge operation. - `SUSPENDED` `FOR` `AUTO` `SPLIT` / `MERGE` - Suspended because an automatic split or merge operation is being performed. - `WAITING` `ON` `EMPTY` `QUEUE` - Waiting for more LCRs from the capture process. - `WAITING` `FOR` `CLIENT` - Waiting for the XStream client application to request more LCRs. - `WAITING` `FOR` `CAPTURE` `TO` `INITIALIZE` - Waiting for the capture process to finish the data dictionary build. - `WAITING` `TO` `ATTACH` `TO` `CAPTURE` - Waiting for the outbound server to attach to the capture process.  When a state refers to a capture process, it is the capture process that captures changes for the outbound server. When a state refers to a propagation, it is the outbound server that sends LCRs to the XStream client application. |
| `XIDUSN` | `NUMBER` | Transaction ID undo segment number of the transaction currently being processed  This column is populated only if the `COMMITTED_DATA_ONLY` column shows `YES`. When the `COMMITTED_DATA_ONLY` column shows `NO`, this column is `NULL`. |
| `XIDSLT` | `NUMBER` | Transaction ID slot number of the transaction currently being processed  This column is populated only if the `COMMITTED_DATA_ONLY` column shows `YES`. When the `COMMITTED_DATA_ONLY` column shows `NO`, this column is `NULL`. |
| `XIDSQN` | `NUMBER` | Transaction ID sequence number of the transaction currently being processed  This column is populated only if the `COMMITTED_DATA_ONLY` column shows `YES`. When the `COMMITTED_DATA_ONLY` column shows `NO`, this column is `NULL`. |
| `COMMITSCN` | `NUMBER` | Commit SCN of the transaction currently being processed  This column is populated only if the `COMMITTED_DATA_ONLY` column shows `YES`. When the `COMMITTED_DATA_ONLY` column shows `NO`, this column is `NULL`. |
| `TOTAL_TRANSACTIONS_SENT` | `NUMBER` | Total number of transactions sent by the outbound server to the XStream client application since the last time the client application attached to the outbound server  This column is populated only if the `COMMITTED_DATA_ONLY` column shows `YES`. When the `COMMITTED_DATA_ONLY` column shows `NO`, this column is `NULL`. |
| `MESSAGE_SEQUENCE` | `NUMBER` | Number of the current LCR being processed by the outbound server. This value is reset to 1 at the beginning of each transaction.  This column is populated only if the `COMMITTED_DATA_ONLY` column shows `YES`. When the `COMMITTED_DATA_ONLY` column shows `NO`, this column is `NULL`. |
| `TOTAL_MESSAGES_SENT` | `NUMBER` | Total number of LCRs sent by the outbound server to the XStream client application since the last time the client application attached to the outbound server |
| `SEND_TIME` | `DATE` | Time the last LCR was sent by the outbound server to the XStream client application |
| `LAST_SENT_MESSAGE_NUMBER` | `NUMBER` | Message number of the last LCR sent by the outbound server to the XStream client application |
| `LAST_SENT_MESSAGE_CREATE_TIME` | `DATE` | Creation time at the source database of the last LCR sent by the outbound server to the client application |
| `ELAPSED_SEND_TIME` | `NUMBER` | Time elapsed (in hundredths of a second) sending LCRs to the XStream client application since the last time the client application attached to the outbound server |
| `COMMIT_POSITION` | `RAW(64)` | Commit position of the transaction currently being processed  This column is populated only if the `COMMITTED_DATA_ONLY` column shows `YES`. When the `COMMITTED_DATA_ONLY` column shows `NO`, this column is `NULL`. |
| `LAST_SENT_POSITION` | `RAW(64)` | Position of the last LCR sent to the XStream client application  This column is populated only if the `COMMITTED_DATA_ONLY` column shows `YES`. When the `COMMITTED_DATA_ONLY` column shows `NO`, this column is `NULL`. |
| `BYTES_SENT` | `NUMBER` | Total number of bytes sent by the outbound server to the XStream client application since the last time the client application attached to the outbound server |
| `COMMITTED_DATA_ONLY` | `VARCHAR2(3)` | `YES` if the outbound server can send only LCRs in committed transactions to the XStream client application. A committed transaction is an assembled, noninterleaving transaction with no rollbacks.  `NO` if the outbound server can send LCRs in transactions that have not yet committed to the XStream client application. This mode is for internal Oracle use only. |

Note:

The `V$XSTREAM_OUTBOUND_SERVER` view is available starting with Oracle Database 11g Release 2 (11.2.0.2).