---
title: ALL_APPLY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1004.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_APPLY` displays information about the apply processes that dequeue messages from queues accessible to the current user.

Related View

`DBA_APPLY` displays information about all apply processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APPLY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the apply process |
| `QUEUE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue from which the apply process dequeues |
| `QUEUE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue from which the apply process dequeues |
| `APPLY_CAPTURED` | `VARCHAR2(3)` |  | Indicates whether the apply process applies captured messages (`YES`) or user-enqueued messages (`NO`) |
| `RULE_SET_NAME` | `VARCHAR2(30)` |  | Name of the positive rule set used by the apply process for filtering |
| `RULE_SET_OWNER` | `VARCHAR2(30)` |  | Owner of the positive rule set used by the apply process for filtering |
| `APPLY_USER` | `VARCHAR2(30)` |  | User who is applying messages |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | Database link to which changes are applied. If NULL, then changes are applied to the local database. |
| `APPLY_TAG` | `RAW(2000)` |  | Tag associated with redo log records that are generated when changes are made by the apply process |
| `DDL_HANDLER` | `VARCHAR2(98)` |  | Name of the user-specified DDL handler, which handles DDL logical change records |
| `PRECOMMIT_HANDLER` | `VARCHAR2(98)` |  | Name of the user-specified pre-commit handler |
| `MESSAGE_HANDLER` | `VARCHAR2(98)` |  | Name of the user-specified procedure that handles dequeued messages other than logical change records |
| `STATUS` | `VARCHAR2(8)` |  | Status of the apply process: - `DISABLED` - `ENABLED` - `ABORTED` |
| `MAX_APPLIED_MESSAGE_NUMBER` | `NUMBER` |  | System change number (SCN) corresponding to the apply process high watermark for the last time the apply process was stopped using the `DBMS_APPLY_ADM.STOP_APPLY` procedure with the `force` parameter set to `false`. The apply process high watermark is the SCN beyond which no messages have been applied. |
| `NEGATIVE_RULE_SET_NAME` | `VARCHAR2(30)` |  | Name of the negative rule set used by the apply process for filtering |
| `NEGATIVE_RULE_SET_OWNER` | `VARCHAR2(30)` |  | Owner of the negative rule set used by the apply process for filtering |
| `STATUS_CHANGE_TIME` | `DATE` |  | Time that the `STATUS` of the apply process was changed |
| `ERROR_NUMBER` | `NUMBER` |  | Error number if the apply process was aborted |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message if the apply process was aborted |
| `MESSAGE_DELIVERY_MODE` | `VARCHAR2(10)` |  | Reserved for internal use |
| `PURPOSE` <sup>Foot 1</sup> | `VARCHAR2(19)` |  | Purpose of the apply process: - `Streams` - An apply process in an Oracle Streams configuration - `XStream` `Streams` - An apply process in an Oracle Streams configuration with XStream capabilities enabled by the `DBMS_XSTREAM_ADM`.`ENABLE_GG_XSTREAM_FOR_STREAMS` procedure - `XStream` `Out` - An XStream outbound server in an XStream Out configuration - `XStream` `In` - An XStream inbound server in an XStream In configuration - `AUDIT` `VAULT` - An apply process in an audit vault configuration - `CHANGE` `DATA` `CAPTURE` - An apply process in a change data capture configuration |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

["DBA\_APPLY"](statviews_3047.md)