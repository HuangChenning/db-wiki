---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_OBJECT_USAGE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.590 USER\_OBJECT\_USAGE

`USER_OBJECT_USAGE` displays statistics about index usage gathered from the database for the indexes owned by the current user.

You can use this view to monitor index usage. All indexes owned by the current user that have been used at least once can be monitored and displayed in this view. Its columns (except for `OWNER`) are the same as those in `DBA_OBJECT_USAGE`.

See Also:

" [DBA\_OBJECT\_USAGE](DBA_OBJECT_USAGE.md) "