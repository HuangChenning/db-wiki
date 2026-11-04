---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_HEAT_MAP_SEG_HISTOGRAM.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_HEAT_MAP_SEG_HISTOGRAM` displays segment access information for all segments visible to the user.

Related Views

- `DBA_HEAT_MAP_SEG_HISTOGRAM` displays segment access information for all segments.
- `USER_HEAT_MAP_SEG_HISTOGRAM` displays segment access information for segments owned by the user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Table owner |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(128)` |  | Name of the sub-object |
| `TRACK_TIME` | `DATE` |  | System time when the segment access was tracked |
| `SEGMENT_WRITE` | `VARCHAR2(3)` |  | Indicates whether the segment has write access (`YES` or `NO`) |
| `FULL_SCAN` | `VARCHAR2(3)` |  | Indicates whether the segment has full table scan (`YES` or `NO`) |
| `LOOKUP_SCAN` | `VARCHAR2(3)` |  | Indicates whether the segment has lookup scan (`YES` or `NO`) |