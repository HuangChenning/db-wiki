---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_MVREF_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.579 USER\_MVREF\_STATS

`USER_MVREF_STATS` shows the `REFRESH_ID` associated with each refresh run of each materialized view for the database that is accessible to the current user. It also provides some basic timing statistics related to that materialized view’s refresh in that run.

Its columns (except for `MV_OWNER`) are the same as those in `DBA_MVREF_STATS`.

See Also:

" [DBA\_MVREF\_STATS](DBA_MVREF_STATS.md) "