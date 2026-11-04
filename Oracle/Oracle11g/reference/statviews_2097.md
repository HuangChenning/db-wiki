---
title: ALL_SYNC_CAPTURE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2097.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SYNC_CAPTURE` displays information about the synchronous capture processes that store the captured changes in queues accessible to the current user.

Related View

`DBA_SYNC_CAPTURE` displays information about all synchronous capture processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the capture process |
| `QUEUE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue used for holding captured changes |
| `QUEUE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue used for holding captured changes |
| `RULE_SET_NAME` | `VARCHAR2(30)` |  | Rule set used by the capture process |
| `RULE_SET_OWNER` | `VARCHAR2(30)` |  | Owner of the rule set |
| `CAPTURE_USER` | `VARCHAR2(30)` |  | Current user who is enqueuing captured messages |

See Also:

["DBA\_SYNC\_CAPTURE"](statviews_5037.md)