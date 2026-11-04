---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_OBJECT_USAGE.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_OBJECT_USAGE` displays statistics about index usage gathered from the database for the indexes owned by the current user.

You can use this view to monitor index usage. All indexes owned by the current user that have been used at least once can be monitored and displayed in this view. Its columns (except for `OWNER`) are the same as those in `DBA_OBJECT_USAGE`.

See Also:

" [DBA\_OBJECT\_USAGE](DBA_OBJECT_USAGE.md) "