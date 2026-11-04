---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/USER_MVREF_RUN_STATS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.566 USER\_MVREF\_RUN\_STATS

`USER_MVREF_RUN_STATS` has information about each refresh run for the materialized views accessible for the current database user, with each run being identified by the `REFRESH_ID`. The information includes timing statistics related to the run and the parameters specified in that run.

Its columns (except for `RUN_OWNER`) are the same as those in `DBA_MVREF_RUN_STATS`.

See Also:

" [DBA\_MVREF\_RUN\_STATS](DBA_MVREF_RUN_STATS.md) "