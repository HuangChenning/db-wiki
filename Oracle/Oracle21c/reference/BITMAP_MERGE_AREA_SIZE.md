---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/BITMAP_MERGE_AREA_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.34 BITMAP\_MERGE\_AREA\_SIZE

`BITMAP_MERGE_AREA_SIZE` specifies the amount of memory Oracle uses to merge bitmaps retrieved from a range scan of the index.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1048576` (1 MB) |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Range of values | Operating system-dependent |
| Basic | No |

Note:

Oracle does not recommend using the `BITMAP_MERGE_AREA_SIZE` parameter unless the instance is configured with the shared server option. Oracle recommends that you enable automatic sizing of SQL working areas by setting `PGA_AGGREGATE_TARGET` instead. `BITMAP_MERGE_AREA_SIZE` is retained for backward compatibility.

`BITMAP_MERGE_AREA_SIZE` is relevant only for systems containing bitmap indexes. A larger value usually improves performance, because the bitmap segments must be sorted before being merged into a single bitmap.

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL-GUID-B5E41901-933E-4A31-B5D6-9771FD435EC0) for more information on using bitmap indexes for performance