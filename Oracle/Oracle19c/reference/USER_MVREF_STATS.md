---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/USER_MVREF_STATS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.567 USER\_MVREF\_STATS

`USER_MVREF_STATS` shows the `REFRESH_ID` associated with each refresh run of each materialized view for the database that is accessible to the current user. It also provides some basic timing statistics related to that materialized view’s refresh in that run.

Its columns (except for `MV_OWNER`) are the same as those in `DBA_MVREF_STATS`.

See Also:

" [DBA\_MVREF\_STATS](DBA_MVREF_STATS.md) "