---
title: "V$AQ"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1010.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$AQ` displays statistics for the queues in the database.

| Column | Datatype | Description |
| --- | --- | --- |
| `QID` | `NUMBER` | Unique queue identifier |
| `WAITING` | `NUMBER` | Number of messages in the queue in the state ' `WAITING` ' |
| `READY` | `NUMBER` | Number of messages in the queue in the state ' `READY` ' |
| `EXPIRED` | `NUMBER` | Number of messages in the queue the state ' `EXPIRED` ' |
| `TOTAL_WAIT` | `NUMBER` | Total wait time of all ' `READY` ' messages in the queue |
| `AVERAGE_WAIT` | `NUMBER` | Average wait time of ' `READY` ' messages in the queue |