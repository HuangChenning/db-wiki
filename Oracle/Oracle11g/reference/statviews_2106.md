---
title: ALL_TAB_HISTOGRAMS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2106.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TAB_HISTOGRAMS` describes histograms on tables and views accessible to the current user.

Related Views

- `DBA_TAB_HISTOGRAMS` describes histograms on all tables and views in the database.
- `USER_TAB_HISTOGRAMS` describes histograms on all tables and views owned by the current user. This view does not display the `OWNER` column.

Note:

These views are populated only if you collect statistics on the index using the `DBMS_STATS` package. For more information, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_stats.htm#ARPLS059).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Column name or attribute of the object type column |
| `ENDPOINT_NUMBER` | `NUMBER` |  | Histogram bucket number |
| `ENDPOINT_VALUE` | `NUMBER` |  | Normalized endpoint value for this bucket |
| `ENDPOINT_ACTUAL_VALUE` | `VARCHAR2(1000)` |  | Actual (not normalized) string value of the endpoint for this bucket |