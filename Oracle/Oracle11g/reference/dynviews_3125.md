---
title: "V$WAITSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3125.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$WAITSTAT` displays block contention statistics. This table is only updated when timed statistics are enabled.

| Column | Datatype | Description |
| --- | --- | --- |
| `CLASS` | `VARCHAR2(18)` | Class of the block |
| `COUNT` | `NUMBER` | Number of waits by this `OPERATION` for this `CLASS` of block |
| `TIME` | `NUMBER` | Sum of all wait times for all the waits by this `OPERATION` for this `CLASS` of block (in centiseconds) |