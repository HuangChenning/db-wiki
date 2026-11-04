---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_APPLY_ENQUEUE.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_APPLY_ENQUEUE` displays information about the apply enqueue actions for the rules where the destination queue exists and is accessible to the current user.

Related View

`DBA_APPLY_ENQUEUE` displays information about the apply enqueue actions for all rules in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the rule |
| `DESTINATION_QUEUE_NAME` | `VARCHAR2(4000)` |  | Name of the queue where events satisfying the rule will be enqueued |

See Also:

- " [DBA\_APPLY\_ENQUEUE](DBA_APPLY_ENQUEUE.md) "
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=STRMS128) for instructions on specifying that an apply process enqueue messages
- [Oracle Streams Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=STRMS560) for information about enqueue destinations for messages during apply