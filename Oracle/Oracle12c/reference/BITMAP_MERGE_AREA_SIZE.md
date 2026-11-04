---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/BITMAP_MERGE_AREA_SIZE.html
tags:
  - oracle
  - 12c
  - reference
---

`BITMAP_MERGE_AREA_SIZE` specifies the amount of memory Oracle uses to merge bitmaps retrieved from a range scan of the index.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1048576` (1 MB) |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | Operating system-dependent |
| Basic | No |

Note:

Oracle does not recommend using the `BITMAP_MERGE_AREA_SIZE` parameter unless the instance is configured with the shared server option. Oracle recommends that you enable automatic sizing of SQL working areas by setting `PGA_AGGREGATE_TARGET` instead. `BITMAP_MERGE_AREA_SIZE` is retained for backward compatibility.

`BITMAP_MERGE_AREA_SIZE` is relevant only for systems containing bitmap indexes. A larger value usually improves performance, because the bitmap segments must be sorted before being merged into a single bitmap.

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGSQL867) for more information on using bitmap indexes for performance