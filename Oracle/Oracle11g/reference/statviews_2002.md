---
title: ALL_PART_HISTOGRAMS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2002.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_PART_HISTOGRAMS` displays the histogram data (endpoints per histogram) for the histograms on the table partitions accessible to the current user.

Related Views

- `DBA_PART_HISTOGRAMS` displays the histogram data for the histograms on all table partitions in the database.
- `USER_PART_HISTOGRAMS` displays the histogram data for the histograms on the table partitions owned by the current user. This view does not display the `OWNER` column.

Note:

These views are populated only if you collect statistics on the index using the `DBMS_STATS` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the table partition |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column |
| `BUCKET_NUMBER` | `NUMBER` |  | Bucket number of the histogram |
| `ENDPOINT_VALUE` | `NUMBER` |  | Normalized endpoint values for the bucket |
| `ENDPOINT_ACTUAL_VALUE` | `VARCHAR2(1000)` |  | Actual (not normalized) string value of the endpoint for the bucket |

See Also:

- ["DBA\_PART\_HISTOGRAMS"](statviews_4173.md)
- ["USER\_PART\_HISTOGRAMS"](statviews_5388.md)