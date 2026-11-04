---
title: "V$SGASTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3036.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SGASTAT` displays detailed information on the system global area (SGA).

| Column | Datatype | Description |
| --- | --- | --- |
| `POOL` | `VARCHAR2(12)` | Designates the pool in which the memory in `NAME` resides: - `shared pool` - Memory is allocated from the shared pool - `large pool` - Memory is allocated from the large pool - `java pool` - Memory is allocated from the Java pool - `streams pool` - Memory is allocated from the Streams pool |
| `NAME` | `VARCHAR2(26)` | SGA component name |
| `BYTES` | `NUMBER` | Memory size (in bytes) |