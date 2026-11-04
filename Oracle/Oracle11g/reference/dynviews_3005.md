---
title: "V$SEGSTAT_NAME"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3005.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SEGSTAT_NAME` displays information about segment-level statistics properties.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC#` | `NUMBER` | Statistic number |
| `NAME` | `VARCHAR2(64)` | Name of the statistic |
| `SAMPLED` | `VARCHAR2(3)` | Indicates whether the statistic was collected by sampling (`YES`) or not (`NO`) |