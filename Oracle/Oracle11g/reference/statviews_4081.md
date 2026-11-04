---
title: DBA_INDEXES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4081.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_INDEXES` describes all indexes in the database. To gather statistics for this view, use the `DBMS_STATS` package. This view supports parallel partitioned index scans. Its columns are the same as those in ["ALL\_INDEXES"](statviews_1109.md).