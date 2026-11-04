---
title: "V$GLOBAL_TRANSACTION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1168.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$GLOBAL_TRANSACTION` displays information on the currently active global transactions.

| Column | Datatype | Description |
| --- | --- | --- |
| `FORMATID` | `NUMBER` | Format identifier of the global transaction |
| `GLOBALID` | `RAW(64)` | Global transaction identifier of the global transaction |
| `BRANCHID` | `RAW(64)` | Branch qualifier of the global transaction |
| `BRANCHES` | `NUMBER` | Total number of branches in the global transaction |
| `REFCOUNT` | `NUMBER` | Number of siblings for the global transaction (must be the same as branches) |
| `PREPARECOUNT` | `NUMBER` | Number of branches of the global transaction that have prepared |
| `STATE` | `VARCHAR2(38)` | State of the branch of the global transaction: - `ACTIVE` - `COLLECTING` - `FINALIZED` - `FAILED` - `RECOVERING` - `UNASSOCIATED` - `FORGOTTEN` - `READY FOR RECOVERY` - `NO-READONLY FAILED` - `SIBLING INFO WRITTEN` - `[ORACLE COORDINATED]ACTIVE` - `[ORACLE COORDINATED]COLLECTING` - `[ORACLE COORDINATED]FINALIZED` - `[ORACLE COORDINATED]FAILED` - `[ORACLE COORDINATED]RECOVERING` - `[ORACLE COORDINATED]UNASSOCIATED` - `[ORACLE COORDINATED]FORGOTTEN` - `[ORACLE COORDINATED]READY FOR RECOVERY` - `[ORACLE COORDINATED]NO-READONLY FAILED` - `[MULTINODE]ACTIVE` - `[MULTINODE]COLLECTING` - `[MULTINODE]FINALIZED` - `[MULTINODE]FAILED` - `[MULTINODE]RECOVERING` - `[MULTINODE]UNASSOCIATED` - `[MULTINODE]FORGOTTEN` - `[MULTINODE]READY FOR RECOVERY` - `[MULTINODE]NO-READONLY FAILED` - `[MULTINODE]SIBLING INFO WRITTEN` - `COMBINATION` |
| `FLAGS` | `NUMBER` | The numerical representation of the state |
| `COUPLING` | `VARCHAR2(15)` | Indicates whether the branches are free (`FREE`), loosely coupled (`LOOSELY COUPLED`), or tightly coupled (`TIGHTLY COUPLED`) |