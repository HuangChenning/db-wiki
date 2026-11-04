---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_MVREF_STATS.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_MVREF_STATS` shows the `REFRESH_ID` associated with each refresh run of each materialized view for the database that is accessible to the current user. It also provides some basic timing statistics related to that materialized view’s refresh in that run.

Its columns (except for `MV_OWNER`) are the same as those in `DBA_MVREF_STATS`.

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [DBA\_MVREF\_STATS](DBA_MVREF_STATS.md) "