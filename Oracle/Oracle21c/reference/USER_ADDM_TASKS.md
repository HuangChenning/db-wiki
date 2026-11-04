---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_ADDM_TASKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.270 USER\_ADDM\_TASKS

`USER_ADDM_TASKS` displays information about the ADDM tasks owned by the current user.

The view contains one row for each row in the related `USER_ADVISOR_TASKS` view that has `ADVISOR_NAME=ADDM` and `STATUS=COMPLETED`. Its columns (except for `OWNER`) are the same as those in `DBA_ADDM_TASKS`.

See Also:

" [DBA\_ADDM\_TASKS](DBA_ADDM_TASKS.md) "