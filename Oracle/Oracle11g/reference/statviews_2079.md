---
title: ALL_STREAMS_MESSAGE_CONSUMERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2079.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_STREAMS_MESSAGE_CONSUMERS` displays information about the Streams messaging clients accessible to the current user.

Related View

`DBA_STREAMS_MESSAGE_CONSUMERS` displays information about all Streams messaging clients in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAMS_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the messaging client |
| `QUEUE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue |
| `QUEUE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue |
| `RULE_SET_NAME` | `VARCHAR2(30)` |  | Name of the positive rule set |
| `RULE_SET_OWNER` | `VARCHAR2(30)` |  | Owner of the positive rule set |
| `NEGATIVE_RULE_SET_NAME` | `VARCHAR2(30)` |  | Name of the negative rule set |
| `NEGATIVE_RULE_SET_OWNER` | `VARCHAR2(30)` |  | Owner of the negative rule set |
| `NOTIFICATION_TYPE` | `VARCHAR2(9)` |  | Type of the notification action: |
| `NOTIFICATION_ACTION` | `VARCHAR2(256)` |  | Notification action |
| `NOTIFICATION_CONTEXT` | `ANYDATA` |  | Context for the notification action |

See Also:

["DBA\_STREAMS\_MESSAGE\_CONSUMERS"](statviews_5007.md)