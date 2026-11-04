---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_MVIEW_ANALYSIS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.567 USER\_MVIEW\_ANALYSIS

`USER_MVIEW_ANALYSIS` describes all materialized views owned by the current user that potentially support query rewrite and that provide additional information for analysis by applications. Its columns are the same as those in `ALL_MVIEW_ANALYSIS`.

Note:

This view excludes materialized views that reference remote tables or that include references to non-static values such as `SYSDATE` or `USER`. This view also excludes materialized views that were created as snapshots before Oracle8i and that were never altered to enable query rewrite.

See Also:

" [ALL\_MVIEW\_ANALYSIS](ALL_MVIEW_ANALYSIS.md) "