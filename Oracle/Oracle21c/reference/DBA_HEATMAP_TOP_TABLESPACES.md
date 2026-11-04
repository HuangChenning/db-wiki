---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HEATMAP_TOP_TABLESPACES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.354 DBA\_HEATMAP\_TOP\_TABLESPACES

`DBA_HEATMAP_TOP_TABLESPACES` displays heat map information for the top 100 tablespaces.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(128)` |  | Tablespace name |
| `SEGMENT_COUNT` | `NUMBER` |  | Segments in the tablespace |
| `ALLOCATED_BYTES` | `NUMBER` |  | Total bytes allocated to the objects in the tablespace |
| `MIN_WRITETIME` | `DATE` |  | Minimum write time of objects tracked |
| `MAX_WRITETIME` | `DATE` |  | Maximum write time of objects tracked |
| `AVG_WRITETIME` | `DATE` |  | Average write time of objects tracked |
| `MIN_READTIME` | `DATE` |  | Minimum read time of objects tracked |
| `MAX_READTIME` | `DATE` |  | Maximum read time of objects tracked |
| `AVG_READTIME` | `DATE` |  | Average read time of objects tracked |
| `MIN_FTSTIME` | `DATE` |  | Minimum full table scan time of objects tracked |
| `MAX_FTSTIME` | `DATE` |  | Maximum full table scan time of objects tracked |
| `AVG_FTSTIME` | `DATE` |  | Average full table scan time of objects tracked |
| `MIN_LOOKUPTIME` | `DATE` |  | Minimum lookup time of objects tracked |
| `MAX_LOOKUPTIME` | `DATE` |  | Maximum lookup time of objects tracked |
| `AVG_LOOKUPTIME` | `DATE` |  | Average lookup time of objects tracked |