---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_DB_LINKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.439 USER\_DB\_LINKS

`USER_DB_LINKS` describes the database links owned by the current user. Its columns are the same as those in `ALL_DB_LINKS` except that it does not have the `OWNER` column.

It also displays an additional column, `PASSWORD`, which is no longer used and for which nothing is returned. The `PASSWORD` column is maintained for backward compatibility only.

See Also:

" [ALL\_DB\_LINKS](ALL_DB_LINKS.md) "