---
title: "V$ROLLNAME"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2151.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ROLLNAME` lists the names of all online rollback segments. It can only be accessed when the database is open.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USN` | `NUMBER` |  | Rollback (undo) segment number |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Rollback segment name |