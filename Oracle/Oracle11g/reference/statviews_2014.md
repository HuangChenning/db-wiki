---
title: ALL_PROPAGATION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2014.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_PROPAGATION` displays information about the Streams propagations that have a source queue accessible to the current user.

Related View

`DBA_PROPAGATION` displays information about all Streams propagations in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROPAGATION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the Streams propagation |
| `SOURCE_QUEUE_OWNER` | `VARCHAR2(30)` |  | Owner of the source queue of the propagation |
| `SOURCE_QUEUE_NAME` | `VARCHAR2(30)` |  | Name of the source queue of the propagation |
| `DESTINATION_QUEUE_OWNER` | `VARCHAR2(30)` |  | Owner of the destination queue of the propagation |
| `DESTINATION_QUEUE_NAME` | `VARCHAR2(30)` |  | Name of the destination queue of the propagation |
| `DESTINATION_DBLINK` | `VARCHAR2(128)` |  | Database link to propagate events from the source queue to the destination queue |
| `RULE_SET_OWNER` | `VARCHAR2(30)` |  | Owner of the propagation positive rule set |
| `RULE_SET_NAME` | `VARCHAR2(30)` |  | Name of the propagation positive rule set |
| `NEGATIVE_RULE_SET_OWNER` | `VARCHAR2(30)` |  | Owner of the propagation negative rule set |
| `NEGATIVE_RULE_SET_NAME` | `VARCHAR2(30)` |  | Name of the propagation negative rule set |
| `QUEUE_TO_QUEUE` | `VARCHAR2(5)` |  | Indicates whether the propagation is a queue-to-queue propagation (`TRUE`) or not (`FALSE`). A queue-to-queue propagation always has its own exclusive propagation job to propagate messages from the source queue to the destination queue. |
| `STATUS` | `VARCHAR2(8)` |  | Status of the propagation: - `DISABLED` - `ENABLED` - `ABORTED` |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message last encountered by propagation |
| `ERROR_DATE` | `DATE` |  | Time that propagation last encountered an error |
| `ORIGINAL_PROPAGATION_NAME` | `VARCHAR2(30)` |  | Original propagation from which the propagation is cloned |
| `ORIGINAL_SOURCE_QUEUE_OWNER` | `VARCHAR2(30)` |  | Source queue owner of the original propagation |
| `ORIGINAL_SOURCE_QUEUE_NAME` | `VARCHAR2(30)` |  | Source queue name of the original propagation |
| `ACKED_SCN` | `NUMBER` |  | Acknowledged SCN of the subscribers of captured messages in the destination queue for the propagation |
| `AUTO_MERGE_THRESHOLD` | `NUMBER` |  | Merge threshold value for merging the propagation back to the original source queue. This is used as the value for the `merge_threshold` parameter in the `DBMS_STREAMS_ADM.MERGE_STREAMS_JOB` procedure. |

See Also:

["DBA\_PROPAGATION"](statviews_4188.md)