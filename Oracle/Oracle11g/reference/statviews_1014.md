---
title: ALL_APPLY_PROGRESS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1014.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_APPLY_PROGRESS` displays information about the progress made by the apply processes that dequeue events from queues accessible to the current user. This view only contains information about captured events. It does not contain information about user-enqueued events.

Related View

`DBA_APPLY_PROGRESS` displays information about the progress made by all apply processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APPLY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the apply process |
| `SOURCE_DATABASE` | `VARCHAR2(128)` | `NOT NULL` | Global name of the source database of the changes that are applied by the apply process |
| `APPLIED_MESSAGE_NUMBER` | `NUMBER` | `NOT NULL` | Message number up to which all transactions have definitely been applied. This value is the low watermark for the apply process. That is, messages with a commit message number less than or equal to this message number have definitely been applied, but some messages with a higher commit message number may also have been applied. |
| `OLDEST_MESSAGE_NUMBER` | `NUMBER` | `NOT NULL` | Earliest message number of the transactions currently being dequeued and applied |
| `APPLY_TIME` | `DATE` |  | Time at which the message with the message number displayed in the `APPLIED_MESSAGE_NUMBER` column was applied |
| `APPLIED_MESSAGE_CREATE_TIME` | `DATE` |  | Time at which the message with the message number displayed in the `APPLIED_MESSAGE_NUMBER` column was created at its source database |
| `OLDEST_TRANSACTION_ID` | `VARCHAR2(128)` |  | Oldest transaction ID of interest. (useful for detecting long-running or large transactions) |
| `SPILL_MESSAGE_NUMBER` | `NUMBER` |  | Spill low watermark. Any message with a lower SCN has either been applied or spilled to disk (it will be dequeued from the Streams queue and capture will not need to resend any logical change records (LCRs) with a lower SCN). Spilled messages may not have been applied yet. |

See Also:

["DBA\_APPLY\_PROGRESS"](statviews_3061.md)