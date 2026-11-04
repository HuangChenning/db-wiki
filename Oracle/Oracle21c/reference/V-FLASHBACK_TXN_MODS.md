---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FLASHBACK_TXN_MODS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.238 V$FLASHBACK\_TXN\_MODS

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
| `OPERATION` | `VARCHAR2(128)` | Operation (such as insert/update/delete) performed by the forward-going operation |
| `BACKEDOUT` | `NUMBER` | Indicates whether the transaction has been backed out as of now |
| `CONFLICT_MOD` | `NUMBER` | If the concerned modification is causing a conflict |
| `MODS_PER_LCR` | `NUMBER` | Sometimes an LCR could cause multiple modifications (for example, an update of an IOT could actually be a delete followed by an insert) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [DBA\_FLASHBACK\_TXN\_REPORT](DBA_FLASHBACK_TXN_REPORT.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS66407) for more information about the `DBMS_FLASHBACK.TRANSACTION_BACKOUT` procedures