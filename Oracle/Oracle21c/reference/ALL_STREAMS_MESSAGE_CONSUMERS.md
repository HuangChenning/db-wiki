---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_STREAMS_MESSAGE_CONSUMERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.90 ALL\_STREAMS\_MESSAGE\_CONSUMERS

`ALL_STREAMS_MESSAGE_CONSUMERS` displays information about the Replication messaging clients accessible to the current user.

Related View

`DBA_STREAMS_MESSAGE_CONSUMERS` displays information about all Replication messaging clients in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAMS_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the messaging client |
| `QUEUE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue |
| `QUEUE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the queue |
| `RULE_SET_NAME` | `VARCHAR2(128)` |  | Name of the positive rule set |
| `RULE_SET_OWNER` | `VARCHAR2(128)` |  | Owner of the positive rule set |
| `NEGATIVE_RULE_SET_NAME` | `VARCHAR2(128)` |  | Name of the negative rule set |
| `NEGATIVE_RULE_SET_OWNER` | `VARCHAR2(128)` |  | Owner of the negative rule set |
| `NOTIFICATION_TYPE` | `VARCHAR2(9)` |  | Type of the notification action:  - `PROCEDURE` - `MAIL` - `HTTP` |
| `NOTIFICATION_ACTION` | `VARCHAR2(256)` |  | Notification action |
| `NOTIFICATION_CONTEXT` | `ANYDATA` |  | Context for the notification action |

See Also:

" [DBA\_STREAMS\_MESSAGE\_CONSUMERS](DBA_STREAMS_MESSAGE_CONSUMERS.md) "