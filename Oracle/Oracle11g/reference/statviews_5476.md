---
title: USER_TAB_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5476.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_TAB_COLUMNS` describes the columns of the tables, views, and clusters owned by the current user. Its columns (except for `OWNER`) are the same as those in ["ALL\_TAB\_COLUMNS"](statviews_2103.md). To gather statistics for this view, use the `DBMS_STATS` package.