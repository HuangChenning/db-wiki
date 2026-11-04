---
title: "V$REPLQUEUE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2132.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$REPLQUEUE` displays statistics about the replication deferred transactions queue. All values are stored since the start of the current database instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `TXNS_ENQUEUED` | `NUMBER` | Number of transactions enqueued in the deferred transactions queue |
| `CALLS_ENQUEUED` | `NUMBER` | Number of calls enqueued into the deferred transactions queue |
| `TXNS_PURGED` | `NUMBER` | Number of transactions purged from the deferred transactions queue |
| `LAST_ENQUEUE_TIME` | `DATE` | Date when the last transaction was enqueued into the deferred transaction queue (null if no transactions have been enqueued into the deferred transaction queue since the instance started) |
| `LAST_PURGE_TIME` | `DATE` | Date when the last transaction was purged from the deferred transaction queue (null if no transactions have been purged from the deferred transaction queue since the instance started) |