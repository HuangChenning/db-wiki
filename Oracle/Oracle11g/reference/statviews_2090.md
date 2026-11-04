---
title: ALL_SUBPART_HISTOGRAMS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2090.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SUBPART_HISTOGRAMS` displays the actual histogram data (end-points per histogram) for histograms on table subpartitions accessible to the current user.

Related Views

- `DBA_SUBPART_HISTOGRAMS` displays this information for all subpartitions in the database.
- `USER_SUBPART_HISTOGRAMS` displays this information for subpartitions of all partitioned objects owned by the current user. This view does not display the `OWNER` column.

Note:

These views are populated only if you collect statistics on the index using the `DBMS_STATS` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Table subpartition name |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Column name |
| `BUCKET_NUMBER` | `NUMBER` |  | Bucket number |
| `ENDPOINT_VALUE` | `NUMBER` |  | Normalized endpoint values for this bucket |
| `ENDPOINT_ACTUAL_VALUE` | `VARCHAR2(1000)` |  | Actual (not normalized) string value of the endpoint for this bucket |