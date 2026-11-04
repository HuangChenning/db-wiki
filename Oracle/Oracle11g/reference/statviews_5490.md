---
title: USER_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5490.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_TABLES` describes the relational tables owned by the current user. Its columns (except for `OWNER`) are the same as those in `ALL_TABLES`. To gather statistics for this view, use the `DBMS_STATS` package.

See Also:

["ALL\_TABLES"](statviews_2117.md)