---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_INDEXES.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.522 USER\_INDEXES

`USER_INDEXES` describes indexes owned by the current user. To gather statistics for this view, use the `DBMS_STATS` package. This view supports parallel partitioned index scans. Its columns (except for `OWNER` and `TABLE_TYPE`) are the same as those in `ALL_INDEXES`.

See Also:

" [ALL\_INDEXES](ALL_INDEXES.md) "