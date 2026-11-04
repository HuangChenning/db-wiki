---
title: DBA_DML_LOCKS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3157.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_DML_LOCKS` lists all DML locks held in the database and all outstanding requests for a DML lock.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SESSION_ID` | `NUMBER` |  | Session holding or acquiring the lock |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the lock |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the lock |
| `MODE_HELD` | `VARCHAR2(13)` |  | The type of lock held. The values are: |
| `MODE_REQUESTED` | `VARCHAR2(13)` |  | Lock request type. The values are: - `ROWS_S` (`SS`): row share lock - `ROW-X` (`SX`): row exclusive lock - `SHARE` (`S`): share lock - `S/ROW-X` (`SSX`): exclusive lock - `NONE`: Lock identifier obtained; lock not held or requested |
| `LAST_CONVERT` | `NUMBER` |  | Time since current mode was granted |
| `BLOCKING_OTHERS` | `VARCHAR2(40)` |  | Blocking others |