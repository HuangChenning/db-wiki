---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_MVREF_RUN_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.578 USER\_MVREF\_RUN\_STATS

`USER_MVREF_RUN_STATS` has information about each refresh run for the materialized views accessible for the current database user, with each run being identified by the `REFRESH_ID`. The information includes timing statistics related to the run and the parameters specified in that run.

Its columns (except for `RUN_OWNER`) are the same as those in `DBA_MVREF_RUN_STATS`.

See Also:

" [DBA\_MVREF\_RUN\_STATS](DBA_MVREF_RUN_STATS.md) "