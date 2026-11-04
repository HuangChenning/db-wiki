---
title: USER_DB_LINKS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5280.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_DB_LINKS` describes the database links owned by the current user. Its columns are the same as those in `ALL_DB_LINKS` except that it does not have the `OWNER` column. It also displays an additional column, `PASSWORD`, which is no longer used and for which nothing is returned. The `PASSWORD` column is maintained for backward compatibility only.

See Also:

["ALL\_DB\_LINKS"](statviews_1067.md)