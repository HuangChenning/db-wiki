---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_INDEXES.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_INDEXES` describes indexes owned by the current user. To gather statistics for this view, use the `DBMS_STATS` package. This view supports parallel partitioned index scans. Its columns (except for `OWNER`) are the same as those in `ALL_INDEXES`.

See Also:

" [ALL\_INDEXES](ALL_INDEXES.md) "