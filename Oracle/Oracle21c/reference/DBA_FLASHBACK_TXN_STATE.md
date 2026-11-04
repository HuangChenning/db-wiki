---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_FLASHBACK_TXN_STATE.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.333 DBA\_FLASHBACK\_TXN\_STATE

`DBA_FLASHBACK_TXN_STATE` displays information about the compensating status of all transactions in the database.

For each compensating transaction, there could be multiple rows, where each row provides the dependency relation between the transactions that have been compensated by the compensating transaction.

Related View

`USER_FLASHBACK_TXN_STATE` displays information about the compensating status of the transactions owned by the current user. This view does not display the `USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPENSATING_XID` | `RAW(8)` |  | Transaction ID of the compensating transaction |
| `XID` | `RAW(8)` |  | A transaction that has been compensated by the compensating transaction |
| `DEPENDENT_XID` | `RAW(8)` |  | A dependent transaction of `XID`  Note: In the case of `BACKOUT_MODE` = `CASCADE`, there must be another row with `XID` = `DEPENDENT_XID` of this column. |
| `BACKOUT_MODE` | `VARCHAR2(16)` |  | Mode in which `XID` was backed out:  - `NOCASCADE` - `NOCASCADE_FORCE` - `NONCONFLICT_ONLY` - `CASCADE` |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | User who is performing the compensating transaction |

See Also:

" [USER\_FLASHBACK\_TXN\_STATE](USER_FLASHBACK_TXN_STATE.md) "