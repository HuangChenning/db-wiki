---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-SQLSTATS_PLAN_HASH.html
tags:
  - oracle
  - 12c
  - reference
---

`V$SQLSTATS_PLAN_HASH` displays basic performance statistics for SQL cursors and contains one row per execution plan of a SQL statement (that is, one row per unique combination of `SQL_ID` and `PLAN_HASH_VALUE`).

The columns for `V$SQLSTATS_PLAN_HASH` are the same as those for `V$SQLSTATS`.

See Also:

" [V$SQLSTATS](V-SQLSTATS.md) "