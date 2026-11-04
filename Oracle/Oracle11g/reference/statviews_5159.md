---
title: QUEUE_PRIVILEGES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5159.htm
tags:
  - oracle
  - 11g
  - reference
---

`QUEUE_PRIVILEGES` shows all Advanced Queuing object privileges granted to the session.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(30)` | `NOT NULL` | Name of the user or role to whom access was granted |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `GRANTOR` | `VARCHAR2(30)` | `NOT NULL` | Name of the user who performed the grant |
| `ENQUEUE_PRIVILEGE` | `NUMBER` |  | Permission to `ENQUEUE` to the queue |
| `DEQUEUE_PRIVILEGE` | `NUMBER` |  | Permission to `DEQUEUE` from the queue |