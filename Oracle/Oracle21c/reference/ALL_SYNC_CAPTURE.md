---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SYNC_CAPTURE.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.100 ALL\_SYNC\_CAPTURE

`ALL_SYNC_CAPTURE` displays information about the synchronous capture processes that store the captured changes in queues accessible to the current user.

Related View

`DBA_SYNC_CAPTURE` displays information about all synchronous capture processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the capture process |
| `QUEUE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue used for holding captured changes |
| `QUEUE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the queue used for holding captured changes |
| `RULE_SET_NAME` | `VARCHAR2(128)` |  | Rule set used by the capture process |
| `RULE_SET_OWNER` | `VARCHAR2(128)` |  | Owner of the rule set |
| `CAPTURE_USER` | `VARCHAR2(128)` |  | Current user who is enqueuing captured messages |

See Also:

" [DBA\_SYNC\_CAPTURE](DBA_SYNC_CAPTURE.md) "