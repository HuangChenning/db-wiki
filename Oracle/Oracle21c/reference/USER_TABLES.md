---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.727 USER\_TABLES

`USER_TABLES` describes the relational tables owned by the current user. Its columns (except for `OWNER`) are the same as those in `ALL_TABLES`.

To gather statistics for this view, use the `DBMS_STATS` package.

See Also:

" [ALL\_TABLES](ALL_TABLES.md) "