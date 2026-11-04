---
title: DBA_FLASHBACK_TXN_STATE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3193.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_FLASHBACK_TXN_STATE` displays information about the compensating status of all transactions in the database. For each compensating transaction, there could be multiple rows, where each row provides the dependency relation between the transactions that have been compensated by the compensating transaction.

Related View

`USER_FLASHBACK_TXN_STATE` displays information about the compensating status of the transactions owned by the current user. This view does not display the `USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPENSATING_XID` | `RAW(8)` |  | Transaction ID of the compensating transaction |
| `XID` | `RAW(8)` |  | A transaction that has been compensated by the compensating transaction |
| `DEPENDENT_XID` | `RAW(8)` |  | A dependent transaction of `XID`  Note: In the case of `BACKOUT_MODE` = `CASCADE`, there must be another row with `XID` = `DEPENDENT_XID` of this column. |
| `BACKOUT_MODE` | `VARCHAR2(16)` |  | Mode in which `XID` was backed out: |
| `USERNAME` | `VARCHAR2(30)` | `NOT NULL` | User who is performing the compensating transaction |

See Also:

["USER\_FLASHBACK\_TXN\_STATE"](statviews_5313.md)