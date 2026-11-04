---
title: USER_PUBLISHED_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5402.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_PUBLISHED_COLUMNS` describes the source table columns owned by the current user which have been published for the source tables. This view is intended for use by Change Data Capture subscribers. Its columns (except for `CHANGE_TABLE_SCHEMA` and `CHANGE_TABLE_NAME`) are the same as those in `DBA_PUBLISHED_COLUMNS`.

See Also:

["DBA\_PUBLISHED\_COLUMNS"](statviews_4190.md)