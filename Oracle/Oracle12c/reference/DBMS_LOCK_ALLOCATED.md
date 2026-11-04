---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBMS_LOCK_ALLOCATED.html
tags:
  - oracle
  - 12c
  - reference
---

`DBMS_LOCK_ALLOCATED` describes user-allocated locks.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the lock |
| `LOCKID` | `NUMBER(38)` |  | Lock identifier number |
| `EXPIRATION` | `DATE` |  | Planned lock expiration date (updates whenever the allocation procedure is run) |