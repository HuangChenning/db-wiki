---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_INDEXES.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.114 DBA\_INDEXES

`DBA_INDEXES` describes all indexes in the database. To gather statistics for this view, use the `DBMS_STATS` package. This view supports parallel partitioned index scans. Its columns (except for `TABLE_TYPE`) are the same as those in `ALL_INDEXES`.

See Also:

" [ALL\_INDEXES](ALL_INDEXES.md) "