---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SUBPART_HISTOGRAMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.96 ALL\_SUBPART\_HISTOGRAMS

`ALL_SUBPART_HISTOGRAMS` displays the actual histogram data (end-points per histogram) for histograms on table subpartitions accessible to the current user.

Related Views

- `DBA_SUBPART_HISTOGRAMS` displays this information for all subpartitions in the database.
- `USER_SUBPART_HISTOGRAMS` displays this information for subpartitions of all partitioned objects owned by the current user. This view does not display the `OWNER` column.

Note:

These views are populated only if you collect statistics on the index using the `DBMS_STATS` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `SUBPARTITION_NAME` | `VARCHAR2(128)` |  | Table subpartition name |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Column name |
| `BUCKET_NUMBER` | `NUMBER` |  | Bucket number |
| `ENDPOINT_VALUE` | `NUMBER` |  | Normalized endpoint values for this bucket |
| `ENDPOINT_ACTUAL_VALUE` | `VARCHAR2(4000)` |  | Actual (not normalized) string value of the endpoint for this bucket |
| `ENDPOINT_ACTUAL_VALUE_RAW` | `RAW(1000)` |  | Endpoint actual value in raw format |
| `ENDPOINT_REPEAT_COUNT` | `NUMBER` |  | Frequency of the endpoint (applies only to hybrid histograms, and is set to 0 for other histogram types) |

See Also:

- " [DBA\_SUBPART\_HISTOGRAMS](DBA_SUBPART_HISTOGRAMS.md) "
- " [USER\_SUBPART\_HISTOGRAMS](USER_SUBPART_HISTOGRAMS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS059) for more information about the `DBMS_STATS` package