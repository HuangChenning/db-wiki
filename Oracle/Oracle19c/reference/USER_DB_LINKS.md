---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/USER_DB_LINKS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.427 USER\_DB\_LINKS

`USER_DB_LINKS` describes the database links owned by the current user. Its columns are the same as those in `ALL_DB_LINKS` except that it does not have the `OWNER` column.

It also displays an additional column, `PASSWORD`, which is no longer used and for which nothing is returned. The `PASSWORD` column is maintained for backward compatibility only.

See Also:

" [ALL\_DB\_LINKS](ALL_DB_LINKS.md) "