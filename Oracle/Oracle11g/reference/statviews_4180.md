---
title: DBA_PENDING_TRANSACTIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4180.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_PENDING_TRANSACTIONS` describes unresolved transactions (either due to failure or if the coordinator has not sent a commit/rollback).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FORMATID` | `NUMBER` |  | The format identifier of the transaction identifier |
| `GLOBALID` | `RAW(64)` |  | The global part (gtrid) of the transaction identifier |
| `BRANCHID` | `RAW(64)` |  | The branch qualifier (bqual) of the transaction identifier |