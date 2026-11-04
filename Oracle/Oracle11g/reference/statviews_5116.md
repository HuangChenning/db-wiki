---
title: DBMS_LOCK_ALLOCATED
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5116.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBMS_LOCK_ALLOCATED` describes user-allocated locks.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the lock |
| `LOCKID` | `NUMBER(38)` |  | Lock identifier number |
| `EXPIRATION` | `DATE` |  | Planned lock expiration date (updates whenever the allocation procedure is run) |