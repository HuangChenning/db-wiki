---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBMS_LOCK_ALLOCATED.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.176 DBMS\_LOCK\_ALLOCATED

`DBMS_LOCK_ALLOCATED` describes user-allocated locks.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the lock |
| `LOCKID` | `NUMBER(38)` |  | Lock identifier number |
| `EXPIRATION` | `DATE` |  | Planned lock expiration date (updates whenever the allocation procedure is run) |