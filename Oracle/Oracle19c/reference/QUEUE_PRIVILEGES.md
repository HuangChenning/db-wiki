---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/QUEUE_PRIVILEGES.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.222 QUEUE\_PRIVILEGES

`QUEUE_PRIVILEGES` shows all Advanced Queuing object privileges granted to the session.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(128)` | `NOT NULL` | Name of the user or role to whom access was granted |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `GRANTOR` | `VARCHAR2(128)` | `NOT NULL` | Name of the user who performed the grant |
| `ENQUEUE_PRIVILEGE` | `NUMBER` |  | Permission to `ENQUEUE` to the queue |
| `DEQUEUE_PRIVILEGE` | `NUMBER` |  | Permission to `DEQUEUE` from the queue |