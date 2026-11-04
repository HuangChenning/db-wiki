---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_MVREF_RUN_STATS.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_MVREF_RUN_STATS` has information about each refresh run for the materialized views accessible for the current database user, with each run being identified by the `REFRESH_ID`. The information includes timing statistics related to the run and the parameters specified in that run.

Its columns (except for `RUN_OWNER`) are the same as those in `DBA_MVREF_RUN_STATS`.

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [DBA\_MVREF\_RUN\_STATS](DBA_MVREF_RUN_STATS.md) "