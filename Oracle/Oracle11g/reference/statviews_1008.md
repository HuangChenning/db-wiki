---
title: ALL_APPLY_ENQUEUE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1008.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_APPLY_ENQUEUE` displays information about the apply enqueue actions for the rules where the destination queue exists and is accessible to the current user.

Related View

`DBA_APPLY_ENQUEUE` displays information about the apply enqueue actions for all rules in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule |
| `DESTINATION_QUEUE_NAME` | `VARCHAR2(4000)` |  | Name of the queue where events satisfying the rule will be enqueued |

See Also:

["DBA\_APPLY\_ENQUEUE"](statviews_3051.md)