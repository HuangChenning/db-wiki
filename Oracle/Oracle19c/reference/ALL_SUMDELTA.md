---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_SUMDELTA.html
tags:
  - oracle
  - 19c
  - reference
---

## 3.98 ALL\_SUMDELTA

`ALL_SUMDELTA` lists direct path load entries accessible to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLEOBJ#` | `NUMBER` | `NOT NULL` | Object number of the table |
| `PARTITIONOBJ#` | `NUMBER` | `NOT NULL` | Object number of table partitions (if the table is partitioned) |
| `DMLOPERATION` | `VARCHAR2(1)` |  | Type of DML operation applied to the table |
| `SCN` | `NUMBER` | `NOT NULL` | SCN when the bulk DML occurred |
| `TIMESTAMP` | `DATE` | `NOT NULL` | Timestamp of the log entry |
| `LOWROWID` | `ROWID` | `NOT NULL` | Start ROWID in the loaded rowid range |
| `HIGHROWID` | `ROWID` | `NOT NULL` | End ROWID in the loaded rowid range |
| `SEQUENCE` | `NUMBER` |  | Sequence number of the direct load |
| `XID` | `NUMBER` |  | Transaction ID |