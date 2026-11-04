---
title: "V$SQLSTATS_PLAN_HASH"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3070.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQLSTATS_PLAN_HASH` displays basic performance statistics for SQL cursors and contains one row per execution plan of a SQL statement (that is, one row per unique combination of `SQL_ID` and `PLAN_HASH_VALUE`).

The columns for `V$SQLSTATS_PLAN_HASH` are the same as those for `V$SQLSTATS`.

See Also:

["V$SQLSTATS"](dynviews_3069.md)