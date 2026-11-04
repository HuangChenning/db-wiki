---
title: "V$FLASHBACK_TXN_GRAPH"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1147.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FLASHBACK_TXN_GRAPH` displays a tabular representation of the transaction dependency graph. For each dependency edge, there could be multiple rows, one for each conflicting operation..

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
| `NUM_PREDS` | `NUMBER` | Number of predecessors of the transaction specified by `XID` in the transaction graph |
| `NUM_SUCCS` | `NUMBER` | Number of successors of the transaction specified by `XID` in the transaction graph |
| `DEP_XID` | `RAW(8)` | One dependent transaction ID of the transaction specified by `XID`. This is a particular child of `XID`. |
| `DEP_TXN_NAME` | `VARCHAR2(255)` | Transaction name, if any, for the transaction specified by `DEP_XID` |
| `TXN_CONF_SQL_ID` | `NUMBER` | SQL ID of undo SQL executed in the context of `XID` which conflicts with the dependent transaction |
| `DEP_TXN_CONF_SQL_ID` | `NUMBER` | SQL ID of undo SQL executed in the context of `DEP_XID` which conflicts with `XID` |
| `CONFLICT_TYPE` | `VARCHAR2(32)` | The type of conflict that the conflict resolution method is used to resolve: delete, uniqueness, or update |