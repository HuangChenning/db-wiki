---
title: ALL_SUMDELTA
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2096.htm
tags:
  - oracle
  - 11g
  - reference
---

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