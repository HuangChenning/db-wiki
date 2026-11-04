---
title: "V$FLASHBACK_TXN_MODS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1148.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FLASHBACK_TXN_MODS` displays the individual modifications of all the transactions in memory.

This view is relevant AFTER a compensating transaction has been started through the `DBMS_FLASHBACK.TRANSACTION_BACKOUT()` set of functions, and is no longer relevant once the compensating transaction is either committed or rolled back. It also provides a tabular representation of the undo SQL that is not available through the CLOB XML construct in the `DBA_FLASHBACK_TXN_REPORT` view.

| Column | Datatype | Description |
| --- | --- | --- |
| `COMPENSATING_XID` | `RAW(8)` | Transaction ID of the compensating transaction |
| `COMPENSATING_TXN_NAME` | `VARCHAR2(255)` | Name of the compensating transaction |
| `XID` | `RAW(8)` | Transaction ID of a relevant transaction found in memory |
| `TXN_NAME` | `VARCHAR2(255)` | Name of the transaction with `XID` as the transaction ID; NULL if none |
| `PARENT_XID` | `RAW(8)` | Parent transaction ID (for a PDML transaction) |
| `INTERESTING` | `NUMBER` | If the transaction is in the transaction dependency graph |
| `ORIGINAL` | `NUMBER` | If the transaction is part of the input set provided |
| `BACKOUT_SEQ` | `NUMBER` | Order in which the transaction has been backed out |
| `UNDO_SQL` | `VARCHAR2(4000)` | Undo SQL for the modification |
| `UNDO_SQL_SQN` | `NUMBER` | Order in which the given SQL has been executed to back out this transaction |
| `UNDO_SQL_SUB_SQN` | `NUMBER` | If the undo SQL is greater than 4000 bytes, then a sequence number, starting from `1`, of a 4000-byte division of the undo SQL |
| `BACKOUT_SQL_ID` | `NUMBER` | SQL ID of the undo SQL (used only for this compensating transaction) |
| `OPERATION` | `VARCHAR2(30)` | Operation (such as insert/update/delete) performed by the forward-going operation |
| `BACKEDOUT` | `NUMBER` | Indicates whether the transaction has been backed out as of now |
| `CONFLICT_MOD` | `NUMBER` | If the concerned modification is causing a conflict |
| `MODS_PER_LCR` | `NUMBER` | Sometimes an LCR could cause multiple modifications (for example, an update of an IOT could actually be a delete followed by an insert) |