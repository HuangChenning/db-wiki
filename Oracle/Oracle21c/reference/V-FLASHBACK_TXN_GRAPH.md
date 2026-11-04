---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FLASHBACK_TXN_GRAPH.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.237 V$FLASHBACK\_TXN\_GRAPH

`V$FLASHBACK_TXN_GRAPH` displays a tabular representation of the transaction dependency graph. For each dependency edge, there could be multiple rows, one for each conflicting operation.

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [DBA\_FLASHBACK\_TXN\_REPORT](DBA_FLASHBACK_TXN_REPORT.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS66407) for more information about the `DBMS_FLASHBACK.TRANSACTION_BACKOUT` procedures