---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBMS_LOCK_ALLOCATED.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.173 DBMS\_LOCK\_ALLOCATED

`DBMS_LOCK_ALLOCATED` describes user-allocated locks.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the lock |
| `LOCKID` | `NUMBER(38)` |  | Lock identifier number |
| `EXPIRATION` | `DATE` |  | Planned lock expiration date (updates whenever the allocation procedure is run) |