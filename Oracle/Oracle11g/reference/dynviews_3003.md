---
title: "V$SEGMENT_STATISTICS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3003.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SEGMENT_STATISTICS` displays information about segment-level statistics.

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(30)` | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(30)` | Name of the subobject |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | Name of the table space to which the object belongs |
| `TS#` | `NUMBER` | Tablespace number |
| `OBJ#` | `NUMBER` | Dictionary object number of the object |
| `DATAOBJ#` | `NUMBER` | Data object number of the object |
| `OBJECT_TYPE` | `VARCHAR2(18)` | Type of the object |
| `STATISTIC_NAME` | `VARCHAR2(64)` | Name of the statistic |
| `STATISTIC#` | `NUMBER` | Statistic number |
| `VALUE` | `NUMBER` | Statistic value |