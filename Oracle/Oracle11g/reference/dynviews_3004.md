---
title: "V$SEGSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3004.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SEGSTAT` displays information about segment-level statistics.

| Column | Datatype | Description |
| --- | --- | --- |
| `TS#` | `NUMBER` | Tablespace number |
| `OBJ#` | `NUMBER` | Dictionary object number |
| `DATAOBJ#` | `NUMBER` | Data object number |
| `STATISTIC_NAME` | `VARCHAR2(64)` | Name of the statistic |
| `STATISTIC#` | `NUMBER` | Statistic number |
| `VALUE` | `NUMBER` | Statistic value |