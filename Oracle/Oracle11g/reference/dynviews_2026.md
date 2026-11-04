---
title: "V$LOADPSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2026.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOADPSTAT` contains statistics about the number of rows loaded into a partition, or subpartition, during a load using the Direct Path API.

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNER` | `VARCHAR2(31)` | Schema name |
| `TABNAME` | `VARCHAR2(31)` | Table name |
| `PARTNAME` | `VARCHAR2(31)` | Partition name |
| `LOADED` | `NUMBER` | Number of rows loaded |