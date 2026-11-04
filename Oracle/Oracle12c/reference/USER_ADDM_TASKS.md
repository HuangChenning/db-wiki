---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_ADDM_TASKS.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_ADDM_TASKS` displays information about the ADDM tasks owned by the current user.

The view contains one row for each row in the related `USER_ADVISOR_TASKS` view that has `ADVISOR_NAME=ADDM` and `STATUS=COMPLETED`. Its columns (except for `OWNER`) are the same as those in `DBA_ADDM_TASKS`.

See Also:

" [DBA\_ADDM\_TASKS](DBA_ADDM_TASKS.md) "