---
title: "V$SGA"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3029.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SGA` displays summary information about the system global area (SGA).

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(20)` | SGA component group |
| `VALUE` | `NUMBER` | Memory size (in bytes) |