---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TRANSACTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.369 TRANSACTIONS

`TRANSACTIONS` specifies how many rollback segments to online when `UNDO_MANAGEMENT` `=` `MANUAL`.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Derived: (1.1 \* `SESSIONS`) |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 4 to 2 <sup>31</sup> - 1 |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

The maximum number of concurrent transactions is now restricted by undo tablespace size (`UNDO_MANAGEMENT` `=` `AUTO`) or the number of online rollback segments (`UNDO_MANAGEMENT` `=` `MANUAL`).