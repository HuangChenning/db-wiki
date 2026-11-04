---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_QUEUE_EVENT_STREAMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.19 ALL\_QUEUE\_EVENT\_STREAMS

`ALL_QUEUE_EVENT_STREAMS` describes the Transactional Event Queue (TEQ) event streams accessible to the current user.

Related Views

- `DBA_QUEUE_EVENT_STREAMS` describes all TEQ event streams in the database.
- `USER_QUEUE_EVENT_STREAMS` describes the TEQ event streams owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the queue |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue |
| `QUEUE_ID` | `NUMBER` | `NOT NULL` | Queue ID |
| `EVENT_STREAM_ID` | `NUMBER` | `NOT NULL` | Event stream ID |
| `DELAY_EVENT_STREAM_ID` | `NUMBER` |  | Delay event stream ID |
| `ENQUEUE_INSTANCE` | `NUMBER` | `NOT NULL` | Event stream enqueue instance ID |
| `EVENT_STREAM_TYPE` | `VARCHAR2(10)` |  | Type of event stream. Possible values:  - `VOLATILE` - `PERSISTENT` |

Note:

This view is available starting with Oracle Database 21c.

See Also:

- " [DBA\_QUEUE\_EVENT\_STREAMS](DBA_QUEUE_EVENT_STREAMS.md) "
- " [USER\_QUEUE\_EVENT\_STREAMS](USER_QUEUE_EVENT_STREAMS.md) "
- [Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Transactional Event Queues and Advanced Queuing