---
title: USER_MVIEW_ANALYSIS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5359.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_MVIEW_ANALYSIS` describes all materialized views owned by the current user that potentially support query rewrite and that provide additional information for analysis by applications. Its columns are the same as those in ["ALL\_MVIEW\_ANALYSIS"](statviews_1144.md).

Note:

This view excludes materialized views that reference remote tables or that include references to non-static values such as `SYSDATE` or `USER`. This view also excludes materialized views that were created as snapshots prior to Oracle8i and that were never altered to enable query rewrite.