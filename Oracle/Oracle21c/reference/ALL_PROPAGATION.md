---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_PROPAGATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.18 ALL\_PROPAGATION

`ALL_PROPAGATION` displays information about the propagations that have a source queue accessible to the current user.

Related View

`DBA_PROPAGATION` displays information about all propagations in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROPAGATION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the propagation |
| `SOURCE_QUEUE_OWNER` | `VARCHAR2(128)` |  | Owner of the source queue of the propagation |
| `SOURCE_QUEUE_NAME` | `VARCHAR2(128)` |  | Name of the source queue of the propagation |
| `DESTINATION_QUEUE_OWNER` | `VARCHAR2(128)` |  | Owner of the destination queue of the propagation |
| `DESTINATION_QUEUE_NAME` | `VARCHAR2(128)` |  | Name of the destination queue of the propagation |
| `DESTINATION_DBLINK` | `VARCHAR2(128)` |  | Database link to propagate events from the source queue to the destination queue |
| `RULE_SET_OWNER` | `VARCHAR2(128)` |  | Owner of the propagation positive rule set |
| `RULE_SET_NAME` | `VARCHAR2(128)` |  | Name of the propagation positive rule set |
| `NEGATIVE_RULE_SET_OWNER` | `VARCHAR2(128)` |  | Owner of the propagation negative rule set |
| `NEGATIVE_RULE_SET_NAME` | `VARCHAR2(128)` |  | Name of the propagation negative rule set |
| `QUEUE_TO_QUEUE` | `VARCHAR2(5)` |  | Indicates whether the propagation is a queue-to-queue propagation (`TRUE`) or not (`FALSE`). A queue-to-queue propagation always has its own exclusive propagation job to propagate messages from the source queue to the destination queue. |
| `STATUS` | `VARCHAR2(8)` |  | Status of the propagation:  - `DISABLED` - `ENABLED` - `ABORTED` |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message last encountered by propagation |
| `ERROR_DATE` | `DATE` |  | Time that propagation last encountered an error |
| `ORIGINAL_PROPAGATION_NAME` | `VARCHAR2(128)` |  | Original propagation from which the propagation is cloned |
| `ORIGINAL_SOURCE_QUEUE_OWNER` | `VARCHAR2(128)` |  | Source queue owner of the original propagation |
| `ORIGINAL_SOURCE_QUEUE_NAME` | `VARCHAR2(128)` |  | Source queue name of the original propagation |
| `ACKED_SCN` | `NUMBER` |  | Acknowledged SCN of the subscribers of captured messages in the destination queue for the propagation |
| `AUTO_MERGE_THRESHOLD` | `NUMBER` |  | Merge threshold value for merging the propagation back to the original source queue |

See Also:

" [DBA\_PROPAGATION](DBA_PROPAGATION.md) "