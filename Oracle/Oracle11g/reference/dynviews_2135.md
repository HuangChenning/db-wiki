---
title: "V$RESOURCE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2135.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RESOURCE` contains resource name and address information.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of the resource object |
| `TYPE` | `VARCHAR2(2)` | Resource type; the resource types are listed in [Table 8-1](dynviews_2027.md) |
| `ID1` | `NUMBER` | Resource identifier #1 |
| `ID2` | `NUMBER` | Resource identifier #2 |