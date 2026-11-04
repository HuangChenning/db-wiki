---
title: DBA_DDL_LOCKS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3147.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_DDL_LOCKS` lists all DDL locks held in the database and all outstanding requests for a DDL lock.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SESSION_ID` | `NUMBER` |  | Session identifier |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the lock |
| `NAME` | `VARCHAR2(30)` |  | Name of the lock |
| `TYPE` | `VARCHAR2(40)` |  | Lock type: - `Cursor` - `Table/Procedure/Type` - `Body` - `Trigger` - `Index` - `Cluster` - `Java Source` - `Java Resource` - `Java Data` |
| `MODE_HELD` | `VARCHAR2(9)` |  | Lock mode: |
| `MODE_REQUESTED` | `VARCHAR2(9)` |  | Lock request type: |