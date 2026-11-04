---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_PENDING_TRANSACTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.242 DBA\_PENDING\_TRANSACTIONS

`DBA_PENDING_TRANSACTIONS` describes unresolved transactions (either due to failure or if the coordinator has not sent a commit/rollback).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FORMATID` | `NUMBER` |  | The format identifier of the transaction identifier |
| `GLOBALID` | `RAW(64)` |  | The global part (gtrid) of the transaction identifier |
| `BRANCHID` | `RAW(64)` |  | The branch qualifier (bqual) of the transaction identifier |