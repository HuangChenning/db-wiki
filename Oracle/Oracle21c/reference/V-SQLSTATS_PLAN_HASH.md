---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQLSTATS_PLAN_HASH.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.77 V$SQLSTATS\_PLAN\_HASH

`V$SQLSTATS_PLAN_HASH` displays basic performance statistics for SQL cursors and contains one row per execution plan of a SQL statement (that is, one row per unique combination of `SQL_ID` and `PLAN_HASH_VALUE`).

The columns for `V$SQLSTATS_PLAN_HASH` are the same as those for `V$SQLSTATS`.

See Also:

" [V$SQLSTATS](V-SQLSTATS.md) "