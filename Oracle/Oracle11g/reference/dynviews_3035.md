---
title: "V$SGAINFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3035.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SGAINFO` displays size information about the SGA, including the sizes of different SGA items, the granule size, and free memory.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(32)` | Name of the SGA size item |
| `BYTES` | `NUMBER` | Size of the item (in bytes) |
| `RESIZEABLE` | `VARCHAR2(3)` | Indicates whether the statistic is resizeable (Yes) or not (`No`) |