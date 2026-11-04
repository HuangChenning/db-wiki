---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_SCHEDULER_CREDENTIALS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.647 USER\_SCHEDULER\_CREDENTIALS

`USER_SCHEDULER_CREDENTIALS` displays information about the credentials owned by the current user. Its columns (except for `OWNER`) are the same as those in `ALL_SCHEDULER_CREDENTIALS`.

Note:

This view is deprecated in favor of the `USER_CREDENTIALS` view. Oracle recommends that you use `USER_CREDENTIALS` instead. `USER_SCHEDULER_CREDENTIALS` is retained for backward compatibility only.

See Also:

- " [USER\_CREDENTIALS](USER_CREDENTIALS.md) "
- " [ALL\_SCHEDULER\_CREDENTIALS](ALL_SCHEDULER_CREDENTIALS.md) "