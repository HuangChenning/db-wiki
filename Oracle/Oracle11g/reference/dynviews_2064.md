---
title: "V$METRICGROUP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2064.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$METRICGROUP` displays information about the metric group for each of the four major Streams components: capture, propagation, apply, and queue.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_ID` | `NUMBER` | Internal ID associated with each group |
| `NAME` | `VARCHAR2(64)` | External name of the group |
| `INTERVAL_SIZE` | `NUMBER` | How often to collect statistics |
| `MAX_INTERVAL` | `NUMBER` | Total number of intervals over which statistics should be collected |