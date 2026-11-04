---
title: USER_NESTED_TABLE_COLS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5369.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_NESTED_TABLE_COLS` describes the columns of the nested tables owned by the current user. Its columns (except for `OWNER`) are the same as those in ["ALL\_NESTED\_TABLE\_COLS"](statviews_1154.md). To gather statistics for this view, use the `DBMS_STATS` package.