---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_HEAT_MAP_SEGMENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.205 ALL\_HEAT\_MAP\_SEGMENT

The timestamps in the view are coarse with a granularity of a day reflecting the flush times of the heat map.

Related Views

- `DBA_HEAT_MAP_SEGMENT` displays the latest segment access time for all segments.
- `USER_HEAT_MAP_SEGMENT` displays the latest segment access time for all segments owned by the user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Table owner |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(128)` |  | Name of the sub-object |
| `SEGMENT_WRITE_TIME` | `DATE` |  | Latest timestamp on which the segment has write access |
| `SEGMENT_READ_TIME` | `DATE` |  | Latest timestamp on which the segment has read access |
| `FULL_SCAN` | `DATE` |  | Latest timestamp on which the segment has full table scan |
| `LOOKUP_SCAN` | `DATE` |  | Latest timestamp on which the segment has index scan |

See Also:

- " [DBA\_HEAT\_MAP\_SEGMENT](DBA_HEAT_MAP_SEGMENT.md) "
- " [USER\_HEAT\_MAP\_SEGMENT](USER_HEAT_MAP_SEGMENT.md) "