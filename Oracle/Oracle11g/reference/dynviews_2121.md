---
title: "V$QUEUE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2121.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$QUEUE` contains information on the shared server message queues.

| Column | Datatype | Description |
| --- | --- | --- |
| `PADDR` | `RAW(4 \| 8)` | Address of the process that owns the queue |
| `TYPE` | `VARCHAR2(10)` | Type of queue: |
| `QUEUED` | `NUMBER` | Number of items in the queue |
| `WAIT` | `NUMBER` | Total time that all items in this queue have waited (in hundredths of a second). Divide by `TOTALQ` for average wait per item. |
| `TOTALQ` | `NUMBER` | Total number of items that have ever been in the queue |